#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validate static/invest/research/data/reports.json schema and file references.
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPORTS_JSON = ROOT / "data" / "reports.json"
REQUIRED_FIELDS = [
    "id",
    "company",
    "ticker",
    "title",
    "summary",
    "tags",
    "category",
    "date",
    "lastUpdate",
    "file",
    "markdownFile"
]


def fail(message):
    print(f"FAIL: {message}")
    sys.exit(1)


def parse_date(value, field_name):
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except Exception:
        fail(f"{field_name} is not YYYY-MM-DD: {value}")


def ensure_non_empty_string(value, field_name):
    if not isinstance(value, str) or not value.strip():
        fail(f"{field_name} must be a non-empty string")


def main():
    if not REPORTS_JSON.exists():
        fail(f"missing file: {REPORTS_JSON}")

    with open(REPORTS_JSON, "r", encoding="utf-8") as file:
        try:
            reports = json.load(file)
        except json.JSONDecodeError as exc:
            fail(f"invalid JSON: {exc}")

    if not isinstance(reports, list) or not reports:
        fail("reports.json must be a non-empty array")

    seen_ids = set()
    for idx, report in enumerate(reports):
        if not isinstance(report, dict):
            fail(f"report[{idx}] must be an object")

        for field in REQUIRED_FIELDS:
            if field not in report:
                fail(f"report[{idx}] missing required field: {field}")

        report_id = report["id"]
        ensure_non_empty_string(report_id, f"report[{idx}].id")
        if not re.fullmatch(r"[a-z0-9-]+", report_id):
            fail(f"report[{idx}].id should match [a-z0-9-]+: {report_id}")
        if report_id in seen_ids:
            fail(f"duplicate report id: {report_id}")
        seen_ids.add(report_id)

        for field in ("company", "ticker", "title", "summary", "category"):
            ensure_non_empty_string(report[field], f"report[{idx}].{field}")

        parse_date(report["date"], f"report[{idx}].date")
        parse_date(report["lastUpdate"], f"report[{idx}].lastUpdate")

        if not isinstance(report["tags"], list) or not report["tags"]:
            fail(f"report[{idx}].tags must be a non-empty array")
        for tag_idx, tag in enumerate(report["tags"]):
            ensure_non_empty_string(tag, f"report[{idx}].tags[{tag_idx}]")

        highlights = report.get("highlights")
        if highlights is not None:
            if not isinstance(highlights, list):
                fail(f"report[{idx}].highlights must be an array when present")
            for hl_idx, highlight in enumerate(highlights):
                ensure_non_empty_string(highlight, f"report[{idx}].highlights[{hl_idx}]")

        file_url = report["file"]
        ensure_non_empty_string(file_url, f"report[{idx}].file")
        expected_url = f"/invest/research/reports/view.html?id={report_id}"
        if file_url != expected_url:
            fail(
                f"report[{idx}].file should be {expected_url}, got: {file_url}"
            )

        markdown_url = report["markdownFile"]
        ensure_non_empty_string(markdown_url, f"report[{idx}].markdownFile")
        if not markdown_url.startswith("/invest/research/"):
            fail(
                f"report[{idx}].markdownFile should start with /invest/research/: {markdown_url}"
            )

        markdown_rel = markdown_url.replace("/invest/research/", "", 1)
        markdown_file = ROOT / markdown_rel
        if not markdown_file.exists():
            fail(
                f"report[{idx}] markdown file not found: {markdown_file}"
            )

    print(f"OK: validated {len(reports)} reports in {REPORTS_JSON}")


if __name__ == "__main__":
    main()
