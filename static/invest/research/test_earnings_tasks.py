#!/usr/bin/env python3
import unittest
from datetime import date, datetime, timezone
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from earnings_tasks import build_payload, build_tasks


def calendar(*entries):
    return {"schemaVersion": 1, "defaultTimezone": "America/New_York", "entries": list(entries)}


class EarningsTaskTests(unittest.TestCase):
    def test_confirmed_day_only_triggers_three_day_window(self):
        data = calendar({"reportId": "a", "expectedDate": "2026-08-04", "precision": "day", "status": "issuer-confirmed"})
        self.assertEqual(build_tasks(data, date(2026, 8, 3))[0]["window"], "T-1")
        self.assertEqual(build_tasks(data, date(2026, 8, 4))[0]["window"], "T")
        self.assertEqual(build_tasks(data, date(2026, 8, 5))[0]["window"], "T+1")
        self.assertEqual(build_tasks(data, date(2026, 8, 6)), [])

    def test_recorded_day_never_creates_research_update(self):
        data = calendar({"reportId": "a", "expectedDate": "2026-08-05", "precision": "day", "status": "recorded"})
        rows = build_tasks(data, date(2026, 8, 3))  # Monday
        self.assertEqual(rows[0]["type"], "source-verification")
        self.assertNotEqual(rows[0]["type"], "research-update")

    def test_month_unknown_and_stale_are_monday_only(self):
        data = calendar(
            {"reportId": "a", "expectedDate": "2026-09", "precision": "month", "status": "estimated"},
            {"reportId": "b", "expectedDate": None, "precision": "unknown", "status": "unknown"},
            {"reportId": "c", "expectedDate": "2026-07", "precision": "month", "status": "stale"},
        )
        self.assertEqual(len(build_tasks(data, date(2026, 8, 3))), 3)
        self.assertEqual(build_tasks(data, date(2026, 8, 4)), [])

    def test_estimated_day_enters_weekly_date_completion(self):
        data = calendar({"reportId": "a", "expectedDate": "2026-08-10", "precision": "day", "status": "estimated"})
        rows = build_tasks(data, date(2026, 8, 3))
        self.assertEqual(rows[0]["type"], "date-completion")

    def test_lapsed_day_dates_enter_weekly_maintenance(self):
        data = calendar({"reportId": "a", "expectedDate": "2026-08-04", "precision": "day", "status": "issuer-confirmed"})
        rows = build_tasks(data, date(2026, 8, 10))  # Monday, T+6
        self.assertEqual(rows[0]["type"], "calendar-maintenance")
        self.assertEqual(rows[0]["window"], "stale")
        self.assertEqual(build_tasks(data, date(2026, 8, 11)), [])  # non-Monday stays quiet

    def test_ids_are_stable_dedupe_keys(self):
        data = calendar({"reportId": "a", "expectedDate": "2026-08-04", "precision": "day", "status": "issuer-confirmed"})
        row = build_tasks(data, date(2026, 8, 4))[0]
        self.assertEqual(row["id"], "earnings:a:2026-08-04:T")

    def test_aware_datetime_uses_each_entry_event_timezone(self):
        data = calendar(
            {
                "reportId": "us",
                "expectedDate": "2026-10-27",
                "precision": "day",
                "status": "issuer-confirmed",
            },
            {
                "reportId": "kr",
                "expectedDate": "2026-10-27",
                "precision": "day",
                "status": "issuer-confirmed",
                "timezone": "Asia/Seoul",
            },
        )
        rows = build_tasks(data, datetime(2026, 10, 26, 22, tzinfo=timezone.utc))
        self.assertEqual({row["reportId"]: row["window"] for row in rows}, {"us": "T-1", "kr": "T"})

    def test_naive_datetime_is_rejected(self):
        data = calendar({"reportId": "a", "expectedDate": "2026-08-04", "precision": "day", "status": "issuer-confirmed"})
        with self.assertRaisesRegex(ValueError, "timezone-aware"):
            build_tasks(data, datetime(2026, 8, 4))

    def test_payload_preserves_full_instant_for_replay(self):
        data = calendar(
            {
                "reportId": "kr",
                "expectedDate": "2026-09",
                "precision": "month",
                "status": "estimated",
                "timezone": "Asia/Seoul",
            }
        )
        noon = datetime(2026, 8, 2, 12, tzinfo=timezone.utc)
        late = datetime(2026, 8, 2, 22, tzinfo=timezone.utc)
        noon_payload = build_payload(data, noon, noon)
        late_payload = build_payload(data, late, late)
        self.assertEqual(noon_payload["generatedAt"], "2026-08-02T12:00:00Z")
        self.assertEqual(late_payload["reference"], {"mode": "instant", "value": "2026-08-02T22:00:00Z"})
        self.assertEqual(noon_payload["tasks"], [])
        self.assertEqual(len(late_payload["tasks"]), 1)

    def test_literal_date_replay_is_explicit_in_payload(self):
        data = calendar({"reportId": "a", "expectedDate": None, "precision": "unknown", "status": "unknown"})
        generated_at = datetime(2026, 8, 2, 22, tzinfo=timezone.utc)
        payload = build_payload(data, date(2026, 8, 3), generated_at)
        self.assertEqual(payload["generatedAt"], "2026-08-02T22:00:00Z")
        self.assertEqual(payload["reference"], {"mode": "literal-date", "value": "2026-08-03"})


CALL_REASON = (
    "Issuer-confirmed earnings call window (release time unconfirmed); "
    "first verify actual release filing/press release, then update the research package."
)


def call(expected_date="2026-10-21", tz="America/Los_Angeles", status="issuer-confirmed"):
    return {
        "eventType": "call",
        "timezone": tz,
        "expectedDate": expected_date,
        "localTime": "14:00",
        "precision": "day",
        "status": status,
        "sourceUrl": "https://issuer.example/ir/call",
        "sourceType": "issuer-ir",
        "verifiedAt": "2026-10-20",
    }


RELEASES = {
    # Release states that cannot trigger research-update on their own (v7 §4.1 Case 2).
    "estimated": {"expectedDate": "2026-11-20", "precision": "day", "status": "estimated"},
    "unknown": {"expectedDate": None, "precision": "unknown", "status": "unknown"},
    "stale": {"expectedDate": "2026-07", "precision": "month", "status": "stale"},
    "recorded": {"expectedDate": "2026-11-20", "precision": "day", "status": "recorded"},
}


class EarningsCallTaskTests(unittest.TestCase):
    def test_confirmed_call_triggers_window_for_every_unconfirmed_release_state(self):
        for status, release in RELEASES.items():
            data = calendar(dict(release, reportId="a", call=call()))
            for day, window in ((date(2026, 10, 20), "T-1"), (date(2026, 10, 21), "T"), (date(2026, 10, 22), "T+1")):
                with self.subTest(status=status, window=window):
                    rows = [row for row in build_tasks(data, day) if row["type"] == "research-update"]
                    self.assertEqual(
                        rows,
                        [
                            {
                                "id": f"earnings:a:call-2026-10-21:{window}",
                                "reportId": "a",
                                "type": "research-update",
                                "window": window,
                                "expectedDate": "2026-10-21",
                                "reason": CALL_REASON,
                            }
                        ],
                    )
            with self.subTest(status=status, window="outside"):
                self.assertEqual(
                    [row for row in build_tasks(data, date(2026, 10, 23)) if row["type"] == "research-update"], []
                )
                self.assertEqual(
                    [row for row in build_tasks(data, date(2026, 10, 19)) if row["type"] == "research-update"], []
                )

    def test_stale_call_never_triggers_research_update(self):
        data = calendar(dict(RELEASES["estimated"], reportId="a", call=call(status="stale")))
        self.assertEqual(build_tasks(data, date(2026, 10, 21)), [])

    def test_lapsed_estimated_release_does_not_swallow_monday_call_window(self):
        # Release estimate 10-22 has lapsed by Monday 10-26; the call on 10-27 is still T-1.
        data = calendar(
            {"reportId": "a", "expectedDate": "2026-10-22", "precision": "day", "status": "estimated",
             "call": call("2026-10-27", "America/New_York")}
        )
        rows = {row["id"]: row["type"] for row in build_tasks(data, date(2026, 10, 26))}
        self.assertEqual(
            rows,
            {
                "earnings:a:2026-10-22:stale": "calendar-maintenance",
                "earnings:a:call-2026-10-27:T-1": "research-update",
            },
        )

    def test_confirmed_release_keeps_current_behavior_and_ignores_same_day_call(self):
        data = calendar(
            {"reportId": "a", "expectedDate": "2026-10-21", "precision": "day", "status": "issuer-confirmed",
             "call": call("2026-10-21", "America/New_York")}
        )
        for day, window in ((date(2026, 10, 20), "T-1"), (date(2026, 10, 21), "T"), (date(2026, 10, 22), "T+1")):
            with self.subTest(window=window):
                self.assertEqual([row["id"] for row in build_tasks(data, day)], [f"earnings:a:2026-10-21:{window}"])
        # Lapsed: only the release's own Monday maintenance, no call duplicate.
        self.assertEqual([row["id"] for row in build_tasks(data, date(2026, 10, 26))], ["earnings:a:2026-10-21:stale"])

    def test_confirmed_release_ignores_call_on_another_day(self):
        data = calendar(
            {"reportId": "a", "expectedDate": "2026-10-21", "precision": "day", "status": "issuer-confirmed",
             "call": call("2026-10-23", "America/New_York")}
        )
        self.assertEqual(build_tasks(data, date(2026, 10, 24)), [])

    def test_call_window_uses_call_timezone_pt_vs_et(self):
        # 04:30Z on 10-21 is still 10-20 in Los Angeles (T-1) but already 10-21 in New York (T).
        instant = datetime(2026, 10, 21, 4, 30, tzinfo=timezone.utc)
        data = calendar(
            dict(RELEASES["estimated"], reportId="pt", call=call("2026-10-21", "America/Los_Angeles")),
            dict(RELEASES["estimated"], reportId="et", call=call("2026-10-21", "America/New_York")),
        )
        rows = {row["reportId"]: row["window"] for row in build_tasks(data, instant)}
        self.assertEqual(rows, {"pt": "T-1", "et": "T"})

    def test_call_timezone_overrides_release_timezone(self):
        # Release timezone is Seoul; the call is in New York and must be counted there.
        instant = datetime(2026, 10, 21, 2, tzinfo=timezone.utc)  # 10-21 Seoul, 10-20 New York
        data = calendar(
            dict(RELEASES["estimated"], reportId="a", timezone="Asia/Seoul", call=call("2026-10-21", "America/New_York"))
        )
        self.assertEqual([row["window"] for row in build_tasks(data, instant)], ["T-1"])

    def test_lapsed_call_enters_monday_maintenance(self):
        data = calendar(dict(RELEASES["estimated"], reportId="a", call=call("2026-10-21")))
        rows = build_tasks(data, date(2026, 10, 26))  # Monday, call T+5; release still in the future
        self.assertEqual(
            [(row["id"], row["type"]) for row in rows],
            [
                ("earnings:a:2026-11-20:complete-date", "date-completion"),
                ("earnings:a:call-2026-10-21:stale", "calendar-maintenance"),
            ],
        )
        self.assertEqual(build_tasks(data, date(2026, 10, 27)), [])  # non-Monday stays quiet

    def test_lapsed_stale_call_also_enters_monday_maintenance(self):
        data = calendar(dict(RELEASES["recorded"], reportId="a", call=call("2026-10-21", status="stale")))
        ids = [row["id"] for row in build_tasks(data, date(2026, 10, 26))]
        self.assertIn("earnings:a:call-2026-10-21:stale", ids)

    def test_lapsed_call_is_not_duplicated_when_release_already_needs_maintenance(self):
        for status in ("unknown", "stale"):
            data = calendar(dict(RELEASES[status], reportId="a", call=call("2026-10-21")))
            with self.subTest(status=status):
                rows = build_tasks(data, date(2026, 10, 26))
                self.assertEqual([row["type"] for row in rows], ["calendar-maintenance"])
                self.assertFalse(rows[0]["id"].startswith("earnings:a:call-"))

    def test_lapsed_call_defers_to_lapsed_release_across_timezones(self):
        # 06:00Z Tue 10-27 is still Monday 10-26 in Los Angeles but Tuesday in New York;
        # the lapsed ET release owns roll-over maintenance, so the PT call adds nothing.
        data = calendar(
            {"reportId": "a", "expectedDate": "2026-10-21", "precision": "day", "status": "estimated",
             "call": call("2026-10-21", "America/Los_Angeles")}
        )
        self.assertEqual(build_tasks(data, datetime(2026, 10, 27, 6, tzinfo=timezone.utc)), [])

    def test_call_and_release_dedupe_keys_never_collide(self):
        # Same date on both events still yields two distinct keys.
        data = calendar(
            {"reportId": "a", "expectedDate": "2026-10-21", "precision": "day", "status": "estimated",
             "call": call("2026-10-21", "America/New_York")}
        )
        ids = [row["id"] for row in build_tasks(data, date(2026, 10, 19))]  # Monday, call T-2
        self.assertEqual(ids, ["earnings:a:2026-10-21:complete-date"])
        ids = [row["id"] for row in build_tasks(data, date(2026, 10, 21))]
        self.assertEqual(ids, ["earnings:a:call-2026-10-21:T"])


if __name__ == "__main__":
    unittest.main()
