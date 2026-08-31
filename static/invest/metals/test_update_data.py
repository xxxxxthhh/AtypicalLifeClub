#!/usr/bin/env python3
"""Regression tests for the metals daily updater."""

from datetime import datetime, time as time_of_day
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


def chart_result(symbol, bars, timezone_name="America/New_York"):
    """A minimal Yahoo chart payload.

    Bars are stamped the way Yahoo actually stamps them: futures at exchange
    -local midnight, listed products at the 09:30 open.
    """
    stamp_at = time_of_day(0, 0) if symbol.endswith("=F") else time_of_day(9, 30)
    tz = ZoneInfo(timezone_name)
    timestamps = [
        int(datetime.combine(
            datetime.strptime(date, "%Y-%m-%d").date(), stamp_at, tzinfo=tz
        ).timestamp())
        for date, _close, _volume in bars
    ]
    return {
        "meta": {"exchangeTimezoneName": timezone_name},
        "timestamp": timestamps,
        "indicators": {"quote": [{
            "close": [close for _date, close, _volume in bars],
            "volume": [volume for _date, _close, volume in bars],
        }]},
    }


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
        self._real = update_data.fetch_splits
        self.addCleanup(setattr, update_data, "fetch_splits", self._real)

    def stub(self, value):
        update_data.fetch_splits = lambda symbol: value

    def test_new_split_back_adjusts_only_earlier_rows(self):
        self.stub([("2026-05-18", 10.0)])
        data = sample_data()
        changed, failed = update_data.apply_new_splits(data)

        self.assertTrue(changed)
        self.assertEqual(failed, [])
        self.assertEqual([r["close"] for r in data["etfs"]["PPLT"]], [17.903, 17.84])
        self.assertEqual(data["metadata"]["lastSplitApplied"], {"PPLT": "2026-05-18"})
        self.assertEqual(data["metadata"]["splitAdjustments"][0]["rowsAdjusted"], 1)

    def test_already_applied_split_is_idempotent(self):
        self.stub([("2026-05-18", 10.0)])
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

    def test_accepts_futures_bar_once_the_session_has_closed(self):
        kept = fetch_historical.completed_rows(
            "GC=F", rows(("2026-08-31", 4480.4)), ny("2026-08-31 17:00"), NY
        )
        self.assertEqual([r["date"] for r in kept], ["2026-08-31"])

    def test_etf_closes_an_hour_before_the_futures_session(self):
        bar = rows(("2026-08-31", 100.0))
        at_1600 = ny("2026-08-31 16:00")

        self.assertEqual(fetch_historical.completed_rows("GLD", bar, at_1600, NY), bar)
        self.assertEqual(fetch_historical.completed_rows("GC=F", bar, at_1600, NY), [])

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


class FetchSplitsTests(unittest.TestCase):
    """"Could not ask" must stay distinguishable from "there was no split"."""

    def setUp(self):
        self._real = fetch_historical.fetch_chart_result
        self.addCleanup(setattr, fetch_historical, "fetch_chart_result", self._real)
        self.addCleanup(setattr, update_data, "fetch_chart_result", self._real)

    def stub(self, fn):
        fetch_historical.fetch_chart_result = fn
        update_data.fetch_chart_result = fn

    def test_ratio_is_numerator_over_denominator(self):
        self.stub(lambda symbol, days, events=None: {
            "meta": {"exchangeTimezoneName": "America/New_York"},
            "events": {"splits": {"1779111000": {
                "date": 1779111000, "numerator": 10.0,
                "denominator": 1.0, "splitRatio": "10:1",
            }}},
        })
        self.assertEqual(update_data.fetch_splits("PPLT"), [("2026-05-18", 10.0)])

    def test_three_for_two_is_not_rounded_away(self):
        self.stub(lambda symbol, days, events=None: {
            "meta": {"exchangeTimezoneName": "America/New_York"},
            "events": {"splits": {"1779111000": {
                "date": 1779111000, "numerator": 3.0, "denominator": 2.0,
            }}},
        })
        self.assertEqual(update_data.fetch_splits("PPLT"), [("2026-05-18", 1.5)])

    def test_absent_events_key_means_no_splits_not_a_failure(self):
        self.stub(lambda symbol, days, events=None: {
            "meta": {"exchangeTimezoneName": "America/New_York"}, "timestamp": [],
        })
        self.assertEqual(update_data.fetch_splits("GLD"), [])

    def test_request_failure_returns_none_so_the_run_aborts(self):
        def boom(symbol, days, events=None):
            raise OSError("connection reset")

        self.stub(boom)
        self.assertIsNone(update_data.fetch_splits("PPLT"))


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
        history = [
            {"date": "2026-08-27", "close": 4609.7, "volume": 5558},
            {"date": "2026-08-28", "close": 4478.1, "volume": 5558},
        ]
        self.stub([("2026-08-27", 4609.7, 5558), ("2026-08-28", 4491.6, 6000)])

        changed = update_data.update_section(
            {"GC=F": history}, ["GC=F"], ny("2026-08-31 21:00")
        )

        self.assertTrue(changed)
        self.assertEqual(
            history,
            [
                {"date": "2026-08-27", "close": 4609.7, "volume": 5558},
                {"date": "2026-08-28", "close": 4491.6, "volume": 6000},
            ],
        )

    def test_window_backfills_a_missed_run_without_disturbing_older_rows(self):
        history = [{"date": "2026-08-26", "close": 4598.2, "volume": 1051}]
        self.stub([
            ("2026-08-27", 4609.7, 5558),
            ("2026-08-28", 4478.1, 5558),
            ("2026-08-31", 4480.4, 117116),
        ])

        changed = update_data.update_section(
            {"GC=F": history}, ["GC=F"], ny("2026-08-31 21:00")
        )

        self.assertTrue(changed)
        self.assertEqual(
            [r["date"] for r in history],
            ["2026-08-26", "2026-08-27", "2026-08-28", "2026-08-31"],
        )
        self.assertEqual(history[0]["close"], 4598.2)

    def test_session_in_progress_never_reaches_history(self):
        history = [{"date": "2026-08-28", "close": 4478.1, "volume": 5558}]
        self.stub([("2026-08-28", 4478.1, 5558), ("2026-08-31", 4480.4, 117116)])

        changed = update_data.update_section(
            {"GC=F": history}, ["GC=F"], ny("2026-08-31 11:14")
        )

        self.assertFalse(changed)
        self.assertEqual([r["date"] for r in history], ["2026-08-28"])

    def test_sunday_bar_never_reaches_history(self):
        history = [{"date": "2026-08-28", "close": 4478.1, "volume": 5558}]
        self.stub([
            ("2026-08-28", 4478.1, 5558),
            ("2026-08-30", 4479.0, 12),   # Sunday: Monday's session opening
            ("2026-08-31", 4480.4, 117116),
        ])

        update_data.update_section({"GC=F": history}, ["GC=F"], ny("2026-08-31 21:00"))

        self.assertEqual([r["date"] for r in history], ["2026-08-28", "2026-08-31"])

    def test_nothing_changes_when_the_window_only_confirms_what_we_have(self):
        history = [{"date": "2026-08-28", "close": 4478.1, "volume": 5558}]
        self.stub([("2026-08-28", 4478.1, 5558)])

        changed = update_data.update_section(
            {"GC=F": history}, ["GC=F"], ny("2026-08-31 21:00")
        )

        self.assertFalse(changed)


class UpsertRecordTests(unittest.TestCase):
    def test_skips_non_finite_close_without_overwriting_existing_record(self):
        history = [{"date": "2026-06-18", "close": 25.3, "volume": 119900}]

        result = update_data.upsert_record(
            history,
            {"date": "2026-06-18", "close": math.nan, "volume": 116233},
        )

        self.assertEqual(result, "skipped")
        self.assertEqual(
            history,
            [{"date": "2026-06-18", "close": 25.3, "volume": 119900}],
        )

    def test_keeps_existing_record_when_only_same_day_volume_changes(self):
        history = [{"date": "2026-06-18", "close": 25.3, "volume": 119900}]

        result = update_data.upsert_record(
            history,
            {"date": "2026-06-18", "close": 25.3, "volume": 116233},
        )

        self.assertEqual(result, "unchanged")
        self.assertEqual(
            history,
            [{"date": "2026-06-18", "close": 25.3, "volume": 119900}],
        )

    def test_updates_existing_record_when_close_changes(self):
        history = [{"date": "2026-06-18", "close": 25.3, "volume": 119900}]

        result = update_data.upsert_record(
            history,
            {"date": "2026-06-18", "close": 25.31, "volume": 116233},
        )

        self.assertEqual(result, "updated")
        self.assertEqual(
            history,
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
