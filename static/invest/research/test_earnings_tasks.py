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


if __name__ == "__main__":
    unittest.main()
