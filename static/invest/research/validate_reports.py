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
    "titleEn",
    "summary",
    "tags",
    "category",
    "date",
    "lastUpdate",
    "file",
    "markdownFiles"
]
VERSION_TYPES = {"initial", "incremental", "full-cycle"}
PREVIOUS_REPORT_FIELDS = [
    "id",
    "label",
    "labelEn",
    "file",
    "date",
    "lastUpdate",
    "summary",
    "summaryEn",
]

# Phase 0 enrichment fields (docs/research-hub-enhancement-plan.md, Part A).
STANCE_VALUES = {"constructive", "neutral-watch", "high-risk-watch", "bearish-avoid"}
THESIS_VALUES = {"bull", "bear", "either"}
THEME_VALUES = {
    "concentration",
    "leverage-solvency",
    "demand",
    "circularity",
    "pricing",
    "optionality",
    "execution",
    "regulatory",
    "valuation",
}
MONITORING_ITEM_ID_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
BILINGUAL_KEYS = ("zh", "en")
# Chain requirement (spec A.7 step 3): stance/priceAsOf/reportedPeriod/monitoring[]
# are mandatory for current chainLayer reports. Enabled only after the backfill so
# the migration never leaves CI red; keep True once flipped.
ENFORCE_CHAIN_ENRICHMENT = True


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


def validate_report_reference(report_id, field_name, reports_by_id):
    ensure_non_empty_string(report_id, field_name)
    if report_id not in reports_by_id:
        fail(f"{field_name} references unknown report id: {report_id}")


def validate_previous_report(report, report_idx, reports_by_id):
    previous = report["previousAnnualReport"]
    field_prefix = f"report[{report_idx}].previousAnnualReport"
    if not isinstance(previous, dict):
        fail(f"{field_prefix} must be an object")

    for field in PREVIOUS_REPORT_FIELDS:
        if field not in previous:
            fail(f"{field_prefix} missing required field: {field}")
        ensure_non_empty_string(previous[field], f"{field_prefix}.{field}")

    parse_date(previous["date"], f"{field_prefix}.date")
    parse_date(previous["lastUpdate"], f"{field_prefix}.lastUpdate")

    previous_id = previous["id"]
    if previous_id == report["id"]:
        fail(f"{field_prefix}.id must not reference the current report")
    validate_report_reference(previous_id, f"{field_prefix}.id", reports_by_id)

    expected_file = f"/invest/research/reports/view.html?id={previous_id}"
    if previous["file"] != expected_file:
        fail(f"{field_prefix}.file should be {expected_file}, got: {previous['file']}")

    previous_report = reports_by_id[previous_id]
    if previous_report.get("isCurrent") is not False:
        fail(f"{field_prefix}.id must reference an archived report with isCurrent=false")


def validate_version_metadata(report, report_idx, reports_by_id):
    version_type = report.get("versionType")
    if version_type is not None:
        if version_type not in VERSION_TYPES:
            fail(
                f"report[{report_idx}].versionType must be one of "
                f"{sorted(VERSION_TYPES)}: {version_type}"
            )

    for field in ("period", "versionLabel"):
        if field in report:
            ensure_non_empty_string(report[field], f"report[{report_idx}].{field}")

    if "isCurrent" in report and not isinstance(report["isCurrent"], bool):
        fail(f"report[{report_idx}].isCurrent must be a boolean when present")

    for field in ("supersedes", "diffBase"):
        if field in report:
            validate_report_reference(report[field], f"report[{report_idx}].{field}", reports_by_id)
            if report[field] == report["id"]:
                fail(f"report[{report_idx}].{field} must not reference itself")

    has_previous = "previousAnnualReport" in report
    if has_previous:
        validate_previous_report(report, report_idx, reports_by_id)
        if version_type != "full-cycle":
            fail(
                f"report[{report_idx}].previousAnnualReport requires "
                "versionType=full-cycle"
            )

    if version_type == "full-cycle":
        for field in ("supersedes", "diffBase", "previousAnnualReport"):
            if field not in report:
                fail(f"report[{report_idx}] full-cycle report missing: {field}")
    elif version_type in {"initial", "incremental"}:
        for field in ("supersedes", "diffBase"):
            if field in report:
                fail(f"report[{report_idx}].{field} requires versionType=full-cycle")


def validate_bilingual_text(value, field_name):
    if not isinstance(value, dict):
        fail(f"{field_name} must be an object with zh and en")
    for lang in BILINGUAL_KEYS:
        ensure_non_empty_string(value.get(lang), f"{field_name}.{lang}")


def validate_monitoring(report, report_idx):
    monitoring = report["monitoring"]
    prefix = f"report[{report_idx}].monitoring"
    if not isinstance(monitoring, list) or not monitoring:
        fail(f"{prefix} must be a non-empty array")

    seen_ids = set()
    for item_idx, item in enumerate(monitoring):
        item_prefix = f"{prefix}[{item_idx}]"
        if not isinstance(item, dict):
            fail(f"{item_prefix} must be an object")

        item_id = item.get("id")
        ensure_non_empty_string(item_id, f"{item_prefix}.id")
        if not MONITORING_ITEM_ID_RE.fullmatch(item_id):
            fail(f"{item_prefix}.id should be kebab-case ([a-z0-9-]): {item_id}")
        if item_id in seen_ids:
            fail(f"{prefix} has duplicate item id: {item_id}")
        seen_ids.add(item_id)

        for field in ("metric", "trigger", "latest"):
            if field not in item:
                fail(f"{item_prefix} missing required field: {field}")
            validate_bilingual_text(item[field], f"{item_prefix}.{field}")

        thesis = item.get("thesis")
        if thesis not in THESIS_VALUES:
            fail(f"{item_prefix}.thesis must be one of {sorted(THESIS_VALUES)}: {thesis}")

        ensure_non_empty_string(item.get("nextCheck"), f"{item_prefix}.nextCheck")

        theme = item.get("theme")
        if theme is not None and theme not in THEME_VALUES:
            fail(f"{item_prefix}.theme must be one of {sorted(THEME_VALUES)}: {theme}")


def validate_enrichment_fields(report, report_idx, reports_by_id):
    if "stance" in report and report["stance"] not in STANCE_VALUES:
        fail(
            f"report[{report_idx}].stance must be one of "
            f"{sorted(STANCE_VALUES)}: {report['stance']}"
        )

    if "priceAsOf" in report:
        ensure_non_empty_string(report["priceAsOf"], f"report[{report_idx}].priceAsOf")
        parse_date(report["priceAsOf"], f"report[{report_idx}].priceAsOf")

    if "reportedPeriod" in report:
        ensure_non_empty_string(report["reportedPeriod"], f"report[{report_idx}].reportedPeriod")

    if "related" in report:
        related = report["related"]
        if not isinstance(related, list) or not related:
            fail(f"report[{report_idx}].related must be a non-empty array when present")
        if len(set(related)) != len(related):
            fail(f"report[{report_idx}].related has duplicate ids")
        for rel_idx, rel_id in enumerate(related):
            validate_report_reference(rel_id, f"report[{report_idx}].related[{rel_idx}]", reports_by_id)
            if rel_id == report["id"]:
                fail(f"report[{report_idx}].related must not reference itself")

    if "monitoring" in report:
        validate_monitoring(report, report_idx)

    is_current_chain = bool(report.get("chainLayer")) and report.get("isCurrent") is not False
    if ENFORCE_CHAIN_ENRICHMENT and is_current_chain:
        for field in ("stance", "priceAsOf", "reportedPeriod", "monitoring"):
            if field not in report:
                fail(
                    f"report[{report_idx}] ({report['id']}) is a current chainLayer "
                    f"report and must carry enrichment field: {field}"
                )


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

    reports_by_id = {}
    for idx, report in enumerate(reports):
        if not isinstance(report, dict):
            fail(f"report[{idx}] must be an object")

        report_id = report.get("id")
        ensure_non_empty_string(report_id, f"report[{idx}].id")
        if not re.fullmatch(r"[a-z0-9-]+", report_id):
            fail(f"report[{idx}].id should match [a-z0-9-]+: {report_id}")
        if report_id in reports_by_id:
            fail(f"duplicate report id: {report_id}")
        reports_by_id[report_id] = report

    for idx, report in enumerate(reports):
        for field in REQUIRED_FIELDS:
            if field not in report:
                fail(f"report[{idx}] missing required field: {field}")

        report_id = report["id"]

        for field in ("company", "ticker", "title", "titleEn", "summary", "category"):
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

        markdown_files = report["markdownFiles"]
        if not isinstance(markdown_files, dict):
            fail(f"report[{idx}].markdownFiles must be an object")

        for lang in ("zh", "en"):
            if lang not in markdown_files:
                fail(f"report[{idx}].markdownFiles missing language: {lang}")

            markdown_url = markdown_files[lang]
            ensure_non_empty_string(markdown_url, f"report[{idx}].markdownFiles.{lang}")
            if not markdown_url.startswith("/invest/research/"):
                fail(
                    f"report[{idx}].markdownFiles.{lang} should start with /invest/research/: {markdown_url}"
                )
            if not markdown_url.endswith(".md"):
                fail(
                    f"report[{idx}].markdownFiles.{lang} should point to a .md file: {markdown_url}"
                )

            markdown_rel = markdown_url.replace("/invest/research/", "", 1)
            markdown_file = ROOT / markdown_rel
            if not markdown_file.exists():
                fail(
                    f"report[{idx}] markdown file not found for {lang}: {markdown_file}"
                )

        if markdown_files["zh"] == markdown_files["en"]:
            fail(
                f"report[{idx}].markdownFiles.zh and .en must be different files"
            )

        validate_version_metadata(report, idx, reports_by_id)
        validate_enrichment_fields(report, idx, reports_by_id)

    print(f"OK: validated {len(reports)} reports in {REPORTS_JSON}")


if __name__ == "__main__":
    main()
