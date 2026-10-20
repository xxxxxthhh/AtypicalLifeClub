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


def calendar_with_call() -> dict:
    """An estimated release with an issuer-confirmed PT call, as in the v7 model."""
    return {
        "schemaVersion": 1,
        "asOf": "2026-10-20",
        "defaultTimezone": "America/New_York",
        "entries": [
            {
                "reportId": "example-2026",
                "company": "Example",
                "fiscalPeriod": "Q3 2026",
                "expectedDate": "2026-10-22",
                "precision": "day",
                "status": "estimated",
                "session": "unspecified",
                "sourceUrl": None,
                "sourceType": "monitoring",
                "verifiedAt": "2026-09-08",
                "call": {
                    "eventType": "call",
                    "timezone": "America/Los_Angeles",
                    "expectedDate": "2026-10-26",
                    "localTime": "14:00",
                    "precision": "day",
                    "status": "issuer-confirmed",
                    "sourceUrl": "https://issuer.example/investors/news/call",
                    "sourceType": "issuer-ir",
                    "verifiedAt": "2026-10-20",
                },
            }
        ],
    }


class EarningsCallValidationTests(unittest.TestCase):
    def test_call_on_unconfirmed_release_passes(self):
        validate(REPORTS, calendar_with_call())

    def test_call_on_confirmed_release_passes(self):
        calendar = valid_calendar()
        call = calendar_with_call()["entries"][0]["call"]
        calendar["entries"][0]["call"] = dict(call, verifiedAt="2026-08-01")
        validate(REPORTS, calendar)

    def test_call_does_not_relax_release_session_rule(self):
        # A confirmed call time never lets the release become issuer-confirmed without its own session.
        calendar = calendar_with_call()
        calendar["entries"][0].update(
            {"status": "issuer-confirmed", "sourceType": "issuer-ir", "sourceUrl": "https://issuer.example/ir"}
        )
        with self.assertRaisesRegex(ValueError, "known event session"):
            validate(REPORTS, calendar)

    def test_call_requires_every_field(self):
        for field in ("eventType", "timezone", "expectedDate", "localTime", "precision", "status",
                      "sourceUrl", "sourceType", "verifiedAt"):
            calendar = calendar_with_call()
            del calendar["entries"][0]["call"][field]
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, "fields mismatch"):
                validate(REPORTS, calendar)

    def test_call_rejects_unknown_fields_such_as_session(self):
        calendar = calendar_with_call()
        calendar["entries"][0]["call"]["session"] = "after-close"
        with self.assertRaisesRegex(ValueError, "extra=\\['session'\\]"):
            validate(REPORTS, calendar)

    def test_call_must_be_an_object(self):
        calendar = calendar_with_call()
        calendar["entries"][0]["call"] = "2026-10-26 14:00"
        with self.assertRaisesRegex(ValueError, "call must be an object"):
            validate(REPORTS, calendar)

    def test_call_event_type_must_be_call(self):
        calendar = calendar_with_call()
        calendar["entries"][0]["call"]["eventType"] = "release"
        with self.assertRaisesRegex(ValueError, "eventType must be call"):
            validate(REPORTS, calendar)

    def test_call_timezone_must_be_iana(self):
        for value in ("PT", "Mars/Olympus_Mons", "", None):
            calendar = calendar_with_call()
            calendar["entries"][0]["call"]["timezone"] = value
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, "call timezone must be an IANA"):
                validate(REPORTS, calendar)

    def test_call_expected_date_must_be_a_day(self):
        calendar = calendar_with_call()
        calendar["entries"][0]["call"]["expectedDate"] = "2026-10"
        with self.assertRaisesRegex(ValueError, "call expectedDate must be YYYY-MM-DD"):
            validate(REPORTS, calendar)

    def test_call_local_time_format(self):
        for value in ("2:00 p.m.", "24:00", "14:60", "1400", None):
            calendar = calendar_with_call()
            calendar["entries"][0]["call"]["localTime"] = value
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, "localTime"):
                validate(REPORTS, calendar)
        calendar = calendar_with_call()
        calendar["entries"][0]["call"]["localTime"] = "unspecified"
        validate(REPORTS, calendar)

    def test_call_precision_must_be_day(self):
        calendar = calendar_with_call()
        calendar["entries"][0]["call"]["precision"] = "month"
        with self.assertRaisesRegex(ValueError, "call precision must be day"):
            validate(REPORTS, calendar)

    def test_call_status_is_limited(self):
        for value in ("estimated", "recorded", "unknown"):
            calendar = calendar_with_call()
            calendar["entries"][0]["call"]["status"] = value
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, "issuer-confirmed or stale"):
                validate(REPORTS, calendar)

    def test_call_requires_issuer_ir_https_source(self):
        for update in ({"sourceType": "monitoring"}, {"sourceUrl": "http://issuer.example/x"}, {"sourceUrl": None}):
            calendar = calendar_with_call()
            calendar["entries"][0]["call"].update(update)
            with self.subTest(update=update), self.assertRaisesRegex(ValueError, "issuer-ir and an HTTPS"):
                validate(REPORTS, calendar)

    def test_call_verified_at_cannot_exceed_as_of(self):
        calendar = calendar_with_call()
        calendar["entries"][0]["call"]["verifiedAt"] = "2026-10-21"
        with self.assertRaisesRegex(ValueError, "call verifiedAt cannot be later"):
            validate(REPORTS, calendar)

    def test_stale_call_must_be_before_as_of(self):
        calendar = calendar_with_call()
        calendar["entries"][0]["call"].update({"status": "stale", "expectedDate": "2026-10-20"})
        with self.assertRaisesRegex(ValueError, "call stale day must be earlier"):
            validate(REPORTS, calendar)
        calendar["entries"][0]["call"]["expectedDate"] = "2026-10-19"
        validate(REPORTS, calendar)

    def test_issuer_confirmed_call_may_be_in_the_past(self):
        # The T and T+1 windows must survive asOf advancing past the call date.
        calendar = calendar_with_call()
        calendar["asOf"] = "2026-10-27"
        validate(REPORTS, calendar)

    def test_fiscal_period_must_be_non_empty_string(self):
        for value in ("", "  ", 3, None):
            calendar = calendar_with_call()
            calendar["entries"][0]["fiscalPeriod"] = value
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, "fiscalPeriod"):
                validate(REPORTS, calendar)


if __name__ == "__main__":
    unittest.main()
