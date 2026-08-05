#!/usr/bin/env python3
import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_earnings_calendar import validate


REPORTS = [{"id": "example-2026", "company": "Example"}]


def valid_calendar() -> dict:
    return {
        "schemaVersion": 1,
        "asOf": "2026-08-01",
        "defaultTimezone": "America/New_York",
        "entries": [
            {
                "reportId": "example-2026",
                "company": "Example",
                "expectedDate": "2026-08-04",
                "precision": "day",
                "status": "issuer-confirmed",
                "session": "after-close",
                "sourceUrl": "https://issuer.example/investors/earnings",
                "sourceType": "issuer-ir",
                "verifiedAt": "2026-08-01",
            }
        ],
    }


class EarningsCalendarValidationTests(unittest.TestCase):
    def test_valid_issuer_confirmed_entry_passes(self):
        validate(REPORTS, valid_calendar())

    def test_issuer_confirmed_requires_issuer_https_source(self):
        calendar = valid_calendar()
        calendar["entries"][0].update({"sourceType": "none", "sourceUrl": None})
        with self.assertRaisesRegex(ValueError, "issuer IR HTTPS source"):
            validate(REPORTS, calendar)

    def test_source_url_must_be_https(self):
        calendar = valid_calendar()
        calendar["entries"][0]["sourceUrl"] = "not-a-url"
        with self.assertRaisesRegex(ValueError, "sourceUrl must be an HTTPS URL"):
            validate(REPORTS, calendar)

    def test_status_precision_mismatch_fails_closed(self):
        calendar = valid_calendar()
        calendar["entries"][0].update(
            {
                "expectedDate": "2026-08-04",
                "precision": "day",
                "status": "unknown",
                "sourceType": "none",
                "sourceUrl": None,
            }
        )
        with self.assertRaisesRegex(ValueError, "unknown status requires unknown precision"):
            validate(REPORTS, calendar)

    def test_verified_at_must_be_an_iso_date(self):
        calendar = valid_calendar()
        calendar["entries"][0]["verifiedAt"] = "not-a-date"
        with self.assertRaisesRegex(ValueError, "verifiedAt must be YYYY-MM-DD"):
            validate(REPORTS, calendar)

    def test_verified_at_cannot_exceed_calendar_as_of(self):
        calendar = valid_calendar()
        calendar["entries"][0]["verifiedAt"] = "2026-08-02"
        with self.assertRaisesRegex(ValueError, "cannot be later"):
            validate(REPORTS, calendar)

    def test_invalid_event_timezone_fails_closed(self):
        calendar = valid_calendar()
        calendar["entries"][0]["timezone"] = "Mars/Olympus_Mons"
        with self.assertRaisesRegex(ValueError, "IANA timezone"):
            validate(REPORTS, calendar)

    def test_invalid_calendar_month_fails_closed(self):
        calendar = valid_calendar()
        calendar["entries"][0].update(
            {
                "expectedDate": "2026-13",
                "precision": "month",
                "status": "estimated",
                "session": "not-applicable",
                "sourceType": "monitoring",
                "sourceUrl": None,
            }
        )
        with self.assertRaisesRegex(ValueError, "real calendar month"):
            validate(REPORTS, calendar)

    def test_issuer_confirmed_requires_known_session(self):
        calendar = valid_calendar()
        calendar["entries"][0]["session"] = "unspecified"
        with self.assertRaisesRegex(ValueError, "known event session"):
            validate(REPORTS, calendar)

    def test_company_must_match_report_metadata(self):
        calendar = valid_calendar()
        calendar["entries"][0]["company"] = "Wrong Company"
        with self.assertRaisesRegex(ValueError, "must match reports.json"):
            validate(REPORTS, calendar)

    def test_estimated_day_is_a_valid_third_party_state(self):
        calendar = copy.deepcopy(valid_calendar())
        calendar["entries"][0].update(
            {
                "status": "estimated",
                "sourceType": "monitoring",
                "sourceUrl": None,
                "session": "unspecified",
            }
        )
        validate(REPORTS, calendar)


if __name__ == "__main__":
    unittest.main()
