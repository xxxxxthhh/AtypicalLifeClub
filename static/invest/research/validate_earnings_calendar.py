#!/usr/bin/env python3
"""Validate the earnings calendar against current non-ETF reports."""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


ROOT = Path(__file__).resolve().parent
REPORTS_JSON = ROOT / "data" / "reports.json"
CALENDAR_JSON = ROOT / "data" / "earnings-calendar.json"
PRECISIONS = {"day", "month", "unknown"}
STATUSES = {"issuer-confirmed", "recorded", "estimated", "stale", "unknown"}
SESSIONS = {"before-open", "after-close", "during-market", "unspecified", "not-applicable"}
SOURCE_TYPES = {"issuer-ir", "report-body", "monitoring", "none"}


def fail(message: str) -> None:
    raise ValueError(message)


def parse_date(value: object, label: str) -> date:
    try:
        return date.fromisoformat(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        fail(f"{label} must be YYYY-MM-DD")


def parse_month(value: object, label: str) -> date:
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}", value):
        fail(f"{label} must be YYYY-MM")
    try:
        return date.fromisoformat(f"{value}-01")
    except ValueError:
        fail(f"{label} must be a real calendar month")


def validate_timezone(value: object, label: str) -> None:
    if not isinstance(value, str) or not value:
        fail(f"{label} must be an IANA timezone")
    try:
        ZoneInfo(value)
    except ZoneInfoNotFoundError:
        fail(f"{label} must be an IANA timezone")


def is_https_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def validate(reports: list[dict], calendar: dict) -> None:
    if calendar.get("schemaVersion") != 1 or not isinstance(calendar.get("entries"), list):
        fail("calendar must have schemaVersion 1 and an entries array")
    as_of = parse_date(calendar.get("asOf"), "calendar asOf")
    validate_timezone(calendar.get("defaultTimezone"), "calendar defaultTimezone")
    current_reports = {
        report["id"]: report
        for report in reports
        if report.get("isCurrent") is not False
        and not report["id"].endswith(("-pre-rerun", "-pre-chain"))
        and "ETF" not in report.get("tags", [])
    }
    current = set(current_reports)
    ids = [entry.get("reportId") for entry in calendar["entries"]]
    if len(ids) != len(set(ids)):
        fail("calendar reportId values must be unique")
    if set(ids) != current:
        fail(f"calendar coverage mismatch; missing={sorted(current-set(ids))}, extra={sorted(set(ids)-current)}")

    for entry in calendar["entries"]:
        prefix = entry["reportId"]
        precision = entry.get("precision")
        status = entry.get("status")
        expected = entry.get("expectedDate")
        source_type = entry.get("sourceType")
        source_url = entry.get("sourceUrl")
        session = entry.get("session")
        if precision not in PRECISIONS or status not in STATUSES or entry.get("session") not in SESSIONS:
            fail(f"{prefix}: invalid precision, status, or session")
        if source_type not in SOURCE_TYPES:
            fail(f"{prefix}: invalid sourceType")
        if not isinstance(entry.get("company"), str) or not entry["company"].strip():
            fail(f"{prefix}: company must be a non-empty string")
        if entry["company"] != current_reports[prefix].get("company"):
            fail(f"{prefix}: company must match reports.json")
        verified_at = parse_date(entry.get("verifiedAt"), f"{prefix}: verifiedAt")
        if verified_at > as_of:
            fail(f"{prefix}: verifiedAt cannot be later than calendar asOf")
        validate_timezone(entry.get("timezone", calendar["defaultTimezone"]), f"{prefix}: timezone")

        if precision == "day":
            expected_day = parse_date(expected, f"{prefix}: day-precision expectedDate")
            if session == "not-applicable":
                fail(f"{prefix}: day precision requires an event session")
        elif precision == "month":
            expected_month = parse_month(expected, f"{prefix}: month-precision expectedDate")
        elif precision == "unknown" and expected is not None:
            fail(f"{prefix}: unknown precision requires null expectedDate")
        if precision in {"month", "unknown"} and session != "not-applicable":
            fail(f"{prefix}: {precision} precision requires not-applicable session")

        if source_url is not None and not is_https_url(source_url):
            fail(f"{prefix}: sourceUrl must be an HTTPS URL or null")
        if source_type == "none" and source_url is not None:
            fail(f"{prefix}: sourceType none requires null sourceUrl")

        if status == "unknown":
            if precision != "unknown" or source_type != "none":
                fail(f"{prefix}: unknown status requires unknown precision and sourceType none")
        elif status == "estimated":
            if precision not in {"day", "month"} or source_type != "monitoring":
                fail(f"{prefix}: estimated status requires day/month precision and sourceType monitoring")
        elif status == "recorded":
            if precision != "day" or source_type != "report-body":
                fail(f"{prefix}: recorded status requires day precision and sourceType report-body")
        if status == "issuer-confirmed":
            if precision != "day" or source_type != "issuer-ir" or not is_https_url(source_url):
                fail(f"{prefix}: issuer-confirmed requires an issuer IR HTTPS source and verified day")
            if session not in {"before-open", "after-close", "during-market"}:
                fail(f"{prefix}: issuer-confirmed requires a known event session")
        elif status == "stale":
            if precision not in {"day", "month"} or source_type == "none":
                fail(f"{prefix}: stale status requires dated, previously sourced calendar data")
            if precision == "day" and expected_day >= as_of:
                fail(f"{prefix}: stale day must be earlier than calendar asOf")
            if precision == "month" and expected_month >= as_of.replace(day=1):
                fail(f"{prefix}: stale month must be earlier than calendar asOf month")


def main() -> None:
    try:
        validate(
            json.loads(REPORTS_JSON.read_text(encoding="utf-8")),
            json.loads(CALENDAR_JSON.read_text(encoding="utf-8")),
        )
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"FAIL: {error}")
        sys.exit(1)
    print("PASS: earnings calendar is valid and covers every current non-ETF report")


if __name__ == "__main__":
    main()
