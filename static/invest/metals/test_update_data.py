#!/usr/bin/env python3
"""Regression tests for the metals daily updater."""

from datetime import datetime, time as time_of_day
import json
import math
from pathlib import Path
import sys
import tempfile
import unittest
from zoneinfo import ZoneInfo


sys.path.insert(0, str(Path(__file__).resolve().parent))

import fetch_historical
import update_data


NY = ZoneInfo("America/New_York")


def ny(text):
    """A timezone-aware New York instant, written as 'YYYY-MM-DD HH:MM'."""
    return datetime.strptime(text, "%Y-%m-%d %H:%M").replace(tzinfo=NY)


def rows(*pairs):
    return [{"date": date, "close": close, "volume": 0} for date, close in pairs]


def history(*pairs):
    return [{"date": date, "close": close, "volume": 100} for date, close in pairs]


def chart_result(symbol, bars, splits=None, timezone_name="America/New_York"):
    """A minimal Yahoo chart payload.

    Bars are stamped the way Yahoo actually stamps them: futures at exchange
    -local midnight, listed products at the 09:30 open.
    """
    stamp_at = time_of_day(0, 0) if symbol.endswith("=F") else time_of_day(9, 30)
    tz = ZoneInfo(timezone_name)

    def stamp(date, at):
        return int(datetime.combine(
            datetime.strptime(date, "%Y-%m-%d").date(), at, tzinfo=tz
        ).timestamp())

    result = {
        "meta": {"exchangeTimezoneName": timezone_name},
        "timestamp": [stamp(date, stamp_at) for date, _c, _v in bars],
        "indicators": {"quote": [{
            "close": [close for _d, close, _v in bars],
            "volume": [volume for _d, _c, volume in bars],
        }]},
    }
    if splits:
        result["events"] = {"splits": {
            str(stamp(date, time_of_day(9, 30))): {
                "date": stamp(date, time_of_day(9, 30)),
                "numerator": float(numerator),
                "denominator": float(denominator),
            }
            for date, numerator, denominator in splits
        }}
    return result


def sample_data():
    return {
        "metadata": {"metals": {}, "etfs": {}},
        "metals": {},
        "etfs": {
            "PPLT": [
                {"date": "2026-05-15", "close": 179.03, "volume": 0},
                {"date": "2026-05-18", "close": 17.84, "volume": 0},
            ]
        },
    }


class ApplyNewSplitsTests(unittest.TestCase):
    """A silent split lookup failure is how the 2026-05-18 splits got in."""

    def setUp(self):
        self._real = update_data.fetch_split_bundle
        self.addCleanup(setattr, update_data, "fetch_split_bundle", self._real)

    def stub(self, value):
        update_data.fetch_split_bundle = lambda symbol: value

    def unadjusted_bundle(self):
        # Vendor closes are split-adjusted; local 179.03 is not.
        return ([("2026-05-18", 10.0)], {"2026-05-15": 17.903, "2026-05-18": 17.84})

    def test_new_split_back_adjusts_only_earlier_rows(self):
        self.stub(self.unadjusted_bundle())
        data = sample_data()
        changed, failed = update_data.apply_new_splits(data)

        self.assertTrue(changed)
        self.assertEqual(failed, [])
        self.assertEqual([r["close"] for r in data["etfs"]["PPLT"]], [17.903, 17.84])
        self.assertEqual(data["metadata"]["lastSplitApplied"], {"PPLT": "2026-05-18"})
        self.assertEqual(data["metadata"]["splitAdjustments"][0]["rowsAdjusted"], 1)

    def test_already_applied_split_is_idempotent(self):
        self.stub(self.unadjusted_bundle())
        data = sample_data()
        data["metadata"]["lastSplitApplied"] = {"PPLT": "2026-05-18"}
        changed, failed = update_data.apply_new_splits(data)

        self.assertFalse(changed)
        self.assertEqual(failed, [])
        self.assertEqual([r["close"] for r in data["etfs"]["PPLT"]], [179.03, 17.84])

    def test_lookup_failure_is_reported_not_swallowed(self):
        self.stub(None)
        data = sample_data()
        changed, failed = update_data.apply_new_splits(data)

        self.assertFalse(changed)
        self.assertEqual(failed, ["PPLT"])
        self.assertEqual([r["close"] for r in data["etfs"]["PPLT"]], [179.03, 17.84])


class SplitIdempotenceTests(unittest.TestCase):
    """Losing the cursor must not cost you the data.

    Codex deleted metadata.lastSplitApplied from the committed file and reran:
    PPLT 2026-05-15 was divided by ten a second time, 17.903 -> 1.7903, turning
    the step to its 05-18 neighbour into +896%.  The cursor is now a fast path
    only; the prices themselves decide.
    """

    def setUp(self):
        self._real = update_data.fetch_split_bundle
        self.addCleanup(setattr, update_data, "fetch_split_bundle", self._real)

    def stub(self, events, reference):
        update_data.fetch_split_bundle = lambda symbol: (events, reference)

    def adjusted_data(self):
        return {
            "metadata": {"metals": {}, "etfs": {}},
            "metals": {},
            "etfs": {"PPLT": history(("2026-05-15", 17.903), ("2026-05-18", 17.84))},
        }

    def test_missing_cursor_does_not_divide_already_adjusted_history(self):
        self.stub([("2026-05-18", 10.0)], {"2026-05-15": 17.903, "2026-05-18": 17.84})
        data = self.adjusted_data()

        changed, failed = update_data.apply_new_splits(data)

        self.assertEqual(failed, [])
        self.assertEqual([r["close"] for r in data["etfs"]["PPLT"]], [17.903, 17.84])
        # The cursor is restored so the next run takes the fast path.
        self.assertEqual(data["metadata"]["lastSplitApplied"], {"PPLT": "2026-05-18"})
        self.assertTrue(changed)

    def test_rerunning_after_a_wipe_is_a_fixed_point(self):
        self.stub([("2026-05-18", 10.0)], {"2026-05-15": 17.903, "2026-05-18": 17.84})
        data = self.adjusted_data()

        for _ in range(3):
            data["metadata"].pop("lastSplitApplied", None)
            update_data.apply_new_splits(data)

        self.assertEqual([r["close"] for r in data["etfs"]["PPLT"]], [17.903, 17.84])

    def test_anchors_matching_neither_hypothesis_fail_the_run(self):
        self.stub([("2026-05-18", 10.0)], {"2026-05-15": 50.0, "2026-05-18": 17.84})
        data = self.adjusted_data()

        changed, failed = update_data.apply_new_splits(data)

        self.assertFalse(changed)
        self.assertEqual(failed, ["PPLT"])
        self.assertEqual([r["close"] for r in data["etfs"]["PPLT"]], [17.903, 17.84])

    def test_no_vendor_coverage_for_our_rows_fails_rather_than_guesses(self):
        self.stub([("2026-05-18", 10.0)], {"2026-05-18": 17.84})
        data = self.adjusted_data()

        _changed, failed = update_data.apply_new_splits(data)

        self.assertEqual(failed, ["PPLT"])
        self.assertEqual([r["close"] for r in data["etfs"]["PPLT"]], [17.903, 17.84])

    def test_split_with_no_earlier_rows_only_records_the_cursor(self):
        self.stub([("2026-05-18", 10.0)], {"2026-05-18": 17.84})
        data = {
            "metadata": {"metals": {}, "etfs": {}},
            "metals": {},
            "etfs": {"PPLT": history(("2026-05-18", 17.84))},
        }

        _changed, failed = update_data.apply_new_splits(data)

        self.assertEqual(failed, [])
        self.assertEqual([r["close"] for r in data["etfs"]["PPLT"]], [17.84])
        self.assertEqual(data["metadata"]["lastSplitApplied"], {"PPLT": "2026-05-18"})

    def test_two_stacked_pending_splits_resolve_in_sequence(self):
        # Raw prices; a 2:1 on 03-02 and a 5:1 on 06-01 are both outstanding, so
        # the pre-03-02 row must end up divided by ten in total.
        self.stub(
            [("2026-03-02", 2.0), ("2026-06-01", 5.0)],
            {"2026-03-01": 10.0, "2026-04-01": 20.0, "2026-07-01": 22.0},
        )
        data = {
            "metadata": {"metals": {}, "etfs": {}},
            "metals": {},
            "etfs": {"XX": history(
                ("2026-03-01", 100.0), ("2026-04-01", 100.0), ("2026-07-01", 22.0)
            )},
        }

        _changed, failed = update_data.apply_new_splits(data)

        self.assertEqual(failed, [])
        self.assertEqual(
            [r["close"] for r in data["etfs"]["XX"]], [10.0, 20.0, 22.0]
        )
        self.assertEqual(data["metadata"]["lastSplitApplied"], {"XX": "2026-06-01"})

    def test_older_split_applied_newer_one_pending(self):
        # 03-02 (2:1) is already in the rows, 06-01 (5:1) is not.
        self.stub(
            [("2026-03-02", 2.0), ("2026-06-01", 5.0)],
            {"2026-03-01": 10.0, "2026-04-01": 20.0, "2026-07-01": 22.0},
        )
        data = {
            "metadata": {"metals": {}, "etfs": {}},
            "metals": {},
            "etfs": {"XX": history(
                ("2026-03-01", 50.0), ("2026-04-01", 100.0), ("2026-07-01", 22.0)
            )},
        }

        _changed, failed = update_data.apply_new_splits(data)

        self.assertEqual(failed, [])
        self.assertEqual([r["close"] for r in data["etfs"]["XX"]], [10.0, 20.0, 22.0])


class SplitMetadataRebuildTests(unittest.TestCase):
    """A full rebuild used to drop the bookkeeping and arm the next daily run."""

    def test_existing_split_metadata_is_carried_forward(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "historical.json"
            path.write_text(json.dumps({"metadata": {
                "lastSplitApplied": {"PPLT": "2026-05-18"},
                "knownSplits": [{"symbol": "PPLT"}],
                "splitAdjustments": [{"symbol": "PPLT"}],
                "lookback_days": 730,
            }}), encoding="utf-8")

            carried = fetch_historical.load_existing_metadata(path)

        self.assertEqual(
            sorted(carried), ["knownSplits", "lastSplitApplied", "splitAdjustments"]
        )

    def test_missing_file_carries_nothing_without_raising(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            self.assertEqual(
                fetch_historical.load_existing_metadata(Path(tmpdir) / "nope.json"), {}
            )

    def test_rebuilt_series_seeds_cursors_because_chart_closes_are_adjusted(self):
        seeded = fetch_historical.seed_split_cursors(
            {}, {"PPLT": [("2026-05-18", 10.0)], "GLD": []}
        )
        self.assertEqual(seeded, {"PPLT": "2026-05-18"})

    def test_seeding_never_walks_a_cursor_backwards(self):
        seeded = fetch_historical.seed_split_cursors(
            {"PPLT": "2026-06-01"}, {"PPLT": [("2026-05-18", 10.0)]}
        )
        self.assertEqual(seeded, {"PPLT": "2026-06-01"})

    def test_unreadable_events_leave_the_cursor_unseeded(self):
        seeded = fetch_historical.seed_split_cursors({}, {"PPLT": None})
        self.assertEqual(seeded, {})


class CompletedRowsTests(unittest.TestCase):
    """The bar for a session still in progress must never reach history."""

    def test_rejects_futures_bar_while_its_session_is_still_open(self):
        # Monday 11:14 ET, exactly the moment the live probe saw GC=F already
        # carrying an 08-31 bar at the running price rather than a close.
        kept = fetch_historical.completed_rows(
            "GC=F",
            rows(("2026-08-28", 4478.1), ("2026-08-31", 4480.4)),
            ny("2026-08-31 11:14"),
            NY,
        )
        self.assertEqual([r["date"] for r in kept], ["2026-08-28"])

    def test_accepts_futures_bar_once_the_publication_buffer_has_passed(self):
        kept = fetch_historical.completed_rows(
            "GC=F", rows(("2026-08-31", 4480.4)), ny("2026-08-31 17:20"), NY
        )
        self.assertEqual([r["date"] for r in kept], ["2026-08-31"])

    def test_the_closing_bell_alone_is_not_enough(self):
        # A bar read at the closing second can still be a provisional print.
        for at in ("2026-08-31 17:00", "2026-08-31 17:19"):
            with self.subTest(at=at):
                self.assertEqual(
                    fetch_historical.completed_rows(
                        "GC=F", rows(("2026-08-31", 4480.4)), ny(at), NY
                    ),
                    [],
                )

    def test_etf_closes_an_hour_before_the_futures_session(self):
        bar = rows(("2026-08-31", 100.0))
        at_1620 = ny("2026-08-31 16:20")

        self.assertEqual(fetch_historical.completed_rows("GLD", bar, at_1620, NY), bar)
        self.assertEqual(fetch_historical.completed_rows("GC=F", bar, at_1620, NY), [])

    def test_scheduler_delay_still_refuses_the_next_days_bar(self):
        # The job nominally runs 01:00 UTC (21:00 ET).  Even six hours late, the
        # session it would be reading into is still open.
        kept = fetch_historical.completed_rows(
            "HG=F",
            rows(("2026-08-31", 6.681), ("2026-09-01", 6.7)),
            ny("2026-09-01 03:00"),
            NY,
        )
        self.assertEqual([r["date"] for r in kept], ["2026-08-31"])

    def test_rejects_weekend_dated_bars_however_late_we_look(self):
        kept = fetch_historical.completed_rows(
            "GC=F",
            rows(("2026-08-29", 4470.0), ("2026-08-30", 4475.0), ("2026-08-31", 4480.4)),
            ny("2026-09-02 21:00"),
            NY,
        )
        self.assertEqual([r["date"] for r in kept], ["2026-08-31"])

    def test_requires_a_timezone_aware_observation(self):
        with self.assertRaises(ValueError):
            fetch_historical.completed_rows(
                "GC=F", rows(("2026-08-31", 1.0)), datetime(2026, 8, 31, 21, 0), NY
            )


class ParseChartRowsTests(unittest.TestCase):
    def test_dates_come_from_the_exchange_timezone_not_utc(self):
        # A futures bar is stamped at exchange-local midnight, which is the next
        # calendar day in UTC.  Reading it in UTC would file it a day late.
        result = chart_result("GC=F", [("2026-08-31", 4480.4, 117116)])
        self.assertEqual(
            fetch_historical.parse_chart_rows(result),
            [{"date": "2026-08-31", "close": 4480.4, "volume": 117116}],
        )

    def test_drops_null_closes_without_shifting_the_other_rows(self):
        result = chart_result(
            "GLD", [("2026-08-27", 422.6, 7089000), ("2026-08-28", None, 0)]
        )
        self.assertEqual(
            [r["date"] for r in fetch_historical.parse_chart_rows(result)],
            ["2026-08-27"],
        )


class ParseSplitEventsTests(unittest.TestCase):
    """"Could not ask" must stay distinguishable from "there was no split"."""

    def setUp(self):
        self._real = fetch_historical.fetch_chart_result
        self.addCleanup(setattr, fetch_historical, "fetch_chart_result", self._real)
        self.addCleanup(setattr, update_data, "fetch_chart_result", self._real)

    def stub(self, fn):
        fetch_historical.fetch_chart_result = fn
        update_data.fetch_chart_result = fn

    def test_ratio_is_numerator_over_denominator(self):
        self.stub(lambda symbol, days, events=None: chart_result(
            "PPLT", [("2026-05-18", 17.84, 1)], splits=[("2026-05-18", 10, 1)]
        ))
        events, reference = update_data.fetch_split_bundle("PPLT")
        self.assertEqual(events, [("2026-05-18", 10.0)])
        self.assertEqual(reference, {"2026-05-18": 17.84})

    def test_three_for_two_is_not_rounded_away(self):
        self.stub(lambda symbol, days, events=None: chart_result(
            "PPLT", [("2026-05-18", 17.84, 1)], splits=[("2026-05-18", 3, 2)]
        ))
        events, _reference = update_data.fetch_split_bundle("PPLT")
        self.assertEqual(events, [("2026-05-18", 1.5)])

    def test_absent_events_key_means_no_splits_not_a_failure(self):
        self.stub(lambda symbol, days, events=None: chart_result(
            "GLD", [("2026-08-28", 408.89, 1)]
        ))
        events, _reference = update_data.fetch_split_bundle("GLD")
        self.assertEqual(events, [])

    def test_request_failure_returns_none_so_the_run_aborts(self):
        def boom(symbol, days, events=None):
            raise OSError("connection reset")

        self.stub(boom)
        self.assertIsNone(update_data.fetch_split_bundle("PPLT"))

    def test_event_missing_numerator_raises_rather_than_reporting_no_splits(self):
        result = {
            "meta": {"exchangeTimezoneName": "America/New_York"},
            "events": {"splits": {"1779111000": {
                "date": 1779111000, "splitRatio": "10:1",
            }}},
        }
        with self.assertRaises(ValueError):
            fetch_historical.parse_split_events(result)

    def test_malformed_event_makes_the_bundle_unavailable(self):
        self.stub(lambda symbol, days, events=None: {
            "meta": {"exchangeTimezoneName": "America/New_York"},
            "events": {"splits": {"1779111000": {
                "date": 1779111000, "splitRatio": "10:1",
            }}},
        })
        self.assertIsNone(update_data.fetch_split_bundle("PPLT"))

    def test_nonsensical_ratio_raises(self):
        result = {
            "meta": {"exchangeTimezoneName": "America/New_York"},
            "events": {"splits": {"1779111000": {
                "date": 1779111000, "numerator": 10.0, "denominator": 0.0,
            }}},
        }
        with self.assertRaises(ValueError):
            fetch_historical.parse_split_events(result)


class WindowDaysTests(unittest.TestCase):
    """A fixed window can only ever repair what falls inside it."""

    def test_fresh_history_asks_for_the_rolling_window(self):
        self.assertEqual(
            update_data.window_days(
                history(("2026-08-28", 1.0)), ny("2026-08-31 21:00")
            ),
            update_data.RECENT_WINDOW_DAYS,
        )

    def test_a_long_outage_asks_far_enough_back_to_catch_up(self):
        self.assertGreaterEqual(
            update_data.window_days(
                history(("2026-07-02", 1.0)), ny("2026-08-31 21:00")
            ),
            60 + update_data.CATCHUP_OVERLAP_DAYS,
        )

    def test_empty_history_asks_for_everything_we_keep(self):
        self.assertEqual(
            update_data.window_days([], ny("2026-08-31 21:00")),
            update_data.MAX_CATCHUP_DAYS,
        )

    def test_a_very_stale_file_is_capped_at_the_history_we_keep(self):
        self.assertEqual(
            update_data.window_days(
                history(("2019-01-02", 1.0)), ny("2026-08-31 21:00")
            ),
            update_data.MAX_CATCHUP_DAYS,
        )


class ReconcileWindowTests(unittest.TestCase):
    """Upserting can add and correct, but never retract."""

    def test_removes_a_phantom_row_the_source_does_not_have(self):
        local = history(
            ("2026-08-28", 4478.1), ("2026-08-30", 4479.0), ("2026-08-31", 4480.4)
        )
        removed = update_data.reconcile_window(
            local, rows(("2026-08-28", 4478.1), ("2026-08-31", 4480.4))
        )

        self.assertEqual(removed, 1)
        self.assertEqual([r["date"] for r in local], ["2026-08-28", "2026-08-31"])

    def test_a_completed_row_beyond_the_covered_range_is_never_touched(self):
        # Last night's run stored a complete 08-31; a mid-session run today only
        # covers through 08-28.  Deleting outside the evidence would be the very
        # data loss this function is meant to prevent.
        local = history(("2026-08-28", 4478.1), ("2026-08-31", 4480.4))
        removed = update_data.reconcile_window(local, rows(("2026-08-28", 4478.1)))

        self.assertEqual(removed, 0)
        self.assertEqual([r["date"] for r in local], ["2026-08-28", "2026-08-31"])

    def test_rows_before_the_covered_range_are_left_alone(self):
        local = history(("2026-01-05", 1.0), ("2026-08-28", 4478.1))
        removed = update_data.reconcile_window(local, rows(("2026-08-28", 4478.1)))

        self.assertEqual(removed, 0)
        self.assertEqual(len(local), 2)

    def test_an_empty_source_window_removes_nothing(self):
        local = history(("2026-08-28", 4478.1))
        self.assertEqual(update_data.reconcile_window(local, []), 0)
        self.assertEqual(len(local), 1)


class RollingWindowTests(unittest.TestCase):
    """One bar, written once and never revisited, is what broke the file."""

    def setUp(self):
        self._real = fetch_historical.fetch_chart_result
        self.addCleanup(setattr, fetch_historical, "fetch_chart_result", self._real)

    def stub(self, bars):
        fetch_historical.fetch_chart_result = (
            lambda symbol, days, events=None: chart_result(symbol, bars)
        )

    def test_window_repairs_a_bar_the_exchange_revised_after_we_stored_it(self):
        local = [
            {"date": "2026-08-27", "close": 4609.7, "volume": 5558},
            {"date": "2026-08-28", "close": 4478.1, "volume": 5558},
        ]
        self.stub([("2026-08-27", 4609.7, 5558), ("2026-08-28", 4491.6, 6000)])

        changed, failed = update_data.update_section(
            {"GC=F": local}, ["GC=F"], ny("2026-08-31 21:00")
        )

        self.assertTrue(changed)
        self.assertEqual(failed, [])
        self.assertEqual(
            local,
            [
                {"date": "2026-08-27", "close": 4609.7, "volume": 5558},
                {"date": "2026-08-28", "close": 4491.6, "volume": 6000},
            ],
        )

    def test_window_backfills_a_missed_run_without_disturbing_older_rows(self):
        local = [{"date": "2026-08-26", "close": 4598.2, "volume": 1051}]
        self.stub([
            ("2026-08-26", 4598.2, 1051),
            ("2026-08-27", 4609.7, 5558),
            ("2026-08-28", 4478.1, 5558),
            ("2026-08-31", 4480.4, 117116),
        ])

        changed, _failed = update_data.update_section(
            {"GC=F": local}, ["GC=F"], ny("2026-08-31 21:00")
        )

        self.assertTrue(changed)
        self.assertEqual(
            [r["date"] for r in local],
            ["2026-08-26", "2026-08-27", "2026-08-28", "2026-08-31"],
        )
        self.assertEqual(local[0]["close"], 4598.2)

    def test_session_in_progress_never_reaches_history(self):
        local = [{"date": "2026-08-28", "close": 4478.1, "volume": 5558}]
        self.stub([("2026-08-28", 4478.1, 5558), ("2026-08-31", 4480.4, 117116)])

        changed, _failed = update_data.update_section(
            {"GC=F": local}, ["GC=F"], ny("2026-08-31 11:14")
        )

        self.assertFalse(changed)
        self.assertEqual([r["date"] for r in local], ["2026-08-28"])

    def test_sunday_bar_never_reaches_history(self):
        local = [{"date": "2026-08-28", "close": 4478.1, "volume": 5558}]
        self.stub([
            ("2026-08-28", 4478.1, 5558),
            ("2026-08-30", 4479.0, 12),   # Sunday: Monday's session opening
            ("2026-08-31", 4480.4, 117116),
        ])

        update_data.update_section({"GC=F": local}, ["GC=F"], ny("2026-08-31 21:00"))

        self.assertEqual([r["date"] for r in local], ["2026-08-28", "2026-08-31"])

    def test_a_stored_sunday_row_is_swept_out_by_reconciliation(self):
        local = history(
            ("2026-08-28", 4478.1), ("2026-08-30", 4479.0), ("2026-08-31", 4480.4)
        )
        self.stub([("2026-08-28", 4478.1, 5558), ("2026-08-31", 4480.4, 117116)])

        changed, _failed = update_data.update_section(
            {"GC=F": local}, ["GC=F"], ny("2026-08-31 21:00")
        )

        self.assertTrue(changed)
        self.assertEqual([r["date"] for r in local], ["2026-08-28", "2026-08-31"])

    def test_a_hole_older_than_the_window_is_left_alone_not_silently_healed(self):
        """The documented limit of a rolling window, asserted rather than assumed.

        Reconciliation heals phantom rows inside the covered range and the
        catch-up window closes a trailing gap, but a hole in the middle of
        history that predates the request survives untouched.  Closing it needs
        the periodic full-history audit noted in update_data.window_days.
        """
        local = history(
            ("2026-07-13", 1.0),   # 2026-07-14 is missing, as it was for real
            ("2026-07-15", 1.0),
            ("2026-08-24", 4640.8), ("2026-08-28", 4478.1),
        )
        self.stub([("2026-08-24", 4640.8, 1), ("2026-08-28", 4478.1, 1)])

        changed, failed = update_data.update_section(
            {"GC=F": local}, ["GC=F"], ny("2026-08-31 21:00")
        )

        self.assertFalse(changed)
        self.assertEqual(failed, [])
        self.assertNotIn("2026-07-14", [r["date"] for r in local])
        self.assertEqual(len(local), 4)

    def test_nothing_changes_when_the_window_only_confirms_what_we_have(self):
        local = [{"date": "2026-08-28", "close": 4478.1, "volume": 5558}]
        self.stub([("2026-08-28", 4478.1, 5558)])

        changed, failed = update_data.update_section(
            {"GC=F": local}, ["GC=F"], ny("2026-08-31 21:00")
        )

        self.assertFalse(changed)
        self.assertEqual(failed, [])


class FetchFailureTests(unittest.TestCase):
    """A failed request is not "nothing happened today"."""

    def setUp(self):
        self._real = fetch_historical.fetch_chart_result
        self.addCleanup(setattr, fetch_historical, "fetch_chart_result", self._real)
        self.addCleanup(setattr, update_data, "fetch_chart_result", self._real)

    def test_failure_is_distinct_from_an_empty_window(self):
        def boom(symbol, days, events=None):
            raise OSError("connection reset")

        fetch_historical.fetch_chart_result = boom
        self.assertIsNone(
            update_data.fetch_recent("GC=F", ny("2026-08-31 21:00"), [])
        )

    def test_a_successful_empty_window_is_not_a_failure(self):
        fetch_historical.fetch_chart_result = (
            lambda symbol, days, events=None: chart_result(symbol, [])
        )
        self.assertEqual(
            update_data.fetch_recent("GC=F", ny("2026-08-31 21:00"), []), []
        )

    def test_one_failing_symbol_is_reported_by_update_section(self):
        def half_broken(symbol, days, events=None):
            if symbol == "GC=F":
                raise OSError("connection reset")
            return chart_result(symbol, [("2026-08-31", 40.0, 10)])

        fetch_historical.fetch_chart_result = half_broken
        section = {"GC=F": history(("2026-08-28", 4478.1)), "SI=F": []}

        _changed, failed = update_data.update_section(
            section, ["GC=F", "SI=F"], ny("2026-08-31 21:00")
        )

        self.assertEqual(failed, ["GC=F"])

    def run_main(self, path, chart):
        fetch_historical.fetch_chart_result = chart
        update_data.fetch_chart_result = chart
        argv = sys.argv
        sys.argv = ["update_data.py", str(path)]
        self.addCleanup(setattr, sys, "argv", argv)
        update_data.main()

    def fixture(self, tmpdir):
        path = Path(tmpdir) / "historical.json"
        path.write_text(json.dumps({
            "metadata": {
                "metals": {"GC=F": {}, "SI=F": {}},
                "etfs": {},
                "lastSplitApplied": {},
            },
            "current": {},
            "metals": {
                "GC=F": [{"date": "2026-08-28", "close": 4478.1, "volume": 1}],
                "SI=F": [{"date": "2026-08-28", "close": 50.0, "volume": 1}],
            },
            "etfs": {},
        }, indent=2), encoding="utf-8")
        return path

    def test_a_single_symbol_failure_writes_nothing_and_exits_nonzero(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = self.fixture(tmpdir)
            before = path.read_bytes()

            def half_broken(symbol, days, events=None):
                if events == "splits":
                    return chart_result(symbol, [("2026-08-28", 1.0, 1)])
                if symbol == "GC=F":
                    raise OSError("connection reset")
                return chart_result(symbol, [
                    ("2026-08-28", 50.0, 1), ("2026-08-31", 51.0, 1),
                ])

            with self.assertRaises(SystemExit) as caught:
                self.run_main(path, half_broken)

            self.assertNotEqual(caught.exception.code, 0)
            self.assertEqual(path.read_bytes(), before)

    def test_a_fully_successful_run_does_write(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = self.fixture(tmpdir)

            # Dates comfortably in the past, so the completeness filter cannot
            # make this test depend on when it is run.
            def working(symbol, days, events=None):
                if events == "splits":
                    return chart_result(symbol, [("2026-08-28", 1.0, 1)])
                return chart_result(symbol, [
                    ("2026-08-26", 49.0, 1),
                    ("2026-08-27", 49.5, 1),
                    ("2026-08-28", 50.0, 1),
                ])

            self.run_main(path, working)

            saved = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(
                [r["date"] for r in saved["metals"]["SI=F"]],
                ["2026-08-26", "2026-08-27", "2026-08-28"],
            )


class RebuildFailureTests(unittest.TestCase):
    """A rebuild must not turn a failed fetch into an empty series.

    The rebuild path is run by hand, but one bad run used to wipe a symbol's
    entire two years -- quietly, because `[]` is a well-formed value that reads
    as a result rather than as the failure it actually was.
    """

    def setUp(self):
        self._real = fetch_historical.fetch_chart_result
        self.addCleanup(setattr, fetch_historical, "fetch_chart_result", self._real)
        self.addCleanup(setattr, fetch_historical.time, "sleep", fetch_historical.time.sleep)
        fetch_historical.time.sleep = lambda seconds: None

    def run_main(self, path):
        argv = sys.argv
        sys.argv = ["fetch_historical.py", str(path)]
        self.addCleanup(setattr, sys, "argv", argv)
        fetch_historical.main()

    @staticmethod
    def good(symbol):
        return chart_result(
            symbol, [("2026-08-27", 10.0, 1), ("2026-08-28", 11.0, 1)]
        )

    def assert_aborts_without_writing(self, chart):
        fetch_historical.fetch_chart_result = chart
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "historical.json"
            path.write_text('{"metadata": {"lookback_days": 730}}', encoding="utf-8")
            before = path.read_bytes()

            with self.assertRaises(SystemExit) as caught:
                self.run_main(path)

            self.assertNotEqual(caught.exception.code, 0)
            self.assertEqual(path.read_bytes(), before)

    def test_one_failing_symbol_aborts_the_whole_rebuild(self):
        def half_broken(symbol, days, events=None):
            if symbol == "PA=F":
                raise OSError("connection reset")
            return self.good(symbol)

        self.assert_aborts_without_writing(half_broken)

    def test_a_failing_etf_aborts_it_too(self):
        def half_broken(symbol, days, events=None):
            if symbol == "REMX":
                raise OSError("connection reset")
            return self.good(symbol)

        self.assert_aborts_without_writing(half_broken)

    def test_an_empty_series_is_a_failure_not_a_result(self):
        def one_empty(symbol, days, events=None):
            if symbol == "SI=F":
                return chart_result(symbol, [])
            return self.good(symbol)

        self.assert_aborts_without_writing(one_empty)

    def test_a_fully_successful_rebuild_writes_every_symbol(self):
        fetch_historical.fetch_chart_result = (
            lambda symbol, days, events=None: self.good(symbol)
        )
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "historical.json"

            self.run_main(path)

            saved = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(
                sorted(saved["metals"]), sorted(fetch_historical.METALS)
            )
            self.assertEqual(sorted(saved["etfs"]), sorted(fetch_historical.ETFS))
            self.assertTrue(all(saved["metals"].values()))
            self.assertTrue(all(saved["etfs"].values()))


class UpsertRecordTests(unittest.TestCase):
    def test_skips_non_finite_close_without_overwriting_existing_record(self):
        local = [{"date": "2026-06-18", "close": 25.3, "volume": 119900}]

        result = update_data.upsert_record(
            local,
            {"date": "2026-06-18", "close": math.nan, "volume": 116233},
        )

        self.assertEqual(result, "skipped")
        self.assertEqual(
            local,
            [{"date": "2026-06-18", "close": 25.3, "volume": 119900}],
        )

    def test_keeps_existing_record_when_only_same_day_volume_changes(self):
        local = [{"date": "2026-06-18", "close": 25.3, "volume": 119900}]

        result = update_data.upsert_record(
            local,
            {"date": "2026-06-18", "close": 25.3, "volume": 116233},
        )

        self.assertEqual(result, "unchanged")
        self.assertEqual(
            local,
            [{"date": "2026-06-18", "close": 25.3, "volume": 119900}],
        )

    def test_updates_existing_record_when_close_changes(self):
        local = [{"date": "2026-06-18", "close": 25.3, "volume": 119900}]

        result = update_data.upsert_record(
            local,
            {"date": "2026-06-18", "close": 25.31, "volume": 116233},
        )

        self.assertEqual(result, "updated")
        self.assertEqual(
            local,
            [{"date": "2026-06-18", "close": 25.31, "volume": 116233}],
        )


class SaveDataTests(unittest.TestCase):
    def test_rejects_non_finite_numbers_when_serializing(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "historical.json"

            with self.assertRaises(ValueError):
                update_data.save_data(path, {"close": math.nan})

            self.assertFalse(path.exists())


if __name__ == "__main__":
    unittest.main()
