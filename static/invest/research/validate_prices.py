#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
# ─── How to run ───
# python3 static/invest/research/validate_prices.py

from __future__ import annotations

import json
import math
import sys
from datetime import datetime
from pathlib import Path
from typing import Final, Union


Json = Union[None, bool, int, float, str, list["Json"], dict[str, "Json"]]

ROOT: Final = Path(__file__).resolve().parent
REPORTS_JSON: Final = ROOT / "data" / "reports.json"
PRICES_JSON: Final = ROOT / "data" / "prices.json"
STATUS_VALUES: Final = {"ok", "carried-forward", "missing"}
PRICE_FIELDS: Final = {"baseDate", "basePrice", "lastDate", "lastClose", "changePct", "currency"}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def load_json(path: Path) -> Json:
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        fail(f"missing file: {path}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path}: {exc}")


def require_dict(value: Json, label: str) -> dict[str, Json]:
    if not isinstance(value, dict):
        fail(f"{label} must be an object")
    return value


def require_list(value: Json, label: str) -> list[Json]:
    if not isinstance(value, list):
        fail(f"{label} must be an array")
    return value


def require_string(value: Json, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(f"{label} must be a non-empty string")
    return value


def parse_date(value: Json, label: str) -> datetime:
    text = require_string(value, label)
    try:
        return datetime.strptime(text, "%Y-%m-%d")
    except ValueError:
        fail(f"{label} must be YYYY-MM-DD: {text}")


def require_positive_number(value: Json, label: str) -> float:
    if not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
        fail(f"{label} must be a positive finite number")
    return float(value)


def require_number(value: Json, label: str) -> float:
    if not isinstance(value, (int, float)) or not math.isfinite(value):
        fail(f"{label} must be a finite number")
    return float(value)


def read_reports_by_id(reports: list[Json]) -> dict[str, dict[str, Json]]:
    by_id: dict[str, dict[str, Json]] = {}
    for index, item in enumerate(reports):
        report = require_dict(item, f"reports.json[{index}]")
        report_id = require_string(report.get("id"), f"reports.json[{index}].id")
        by_id[report_id] = report
    return by_id


def validate_missing_entry(entry: dict[str, Json], label: str) -> None:
    present_price_fields = sorted(field for field in PRICE_FIELDS if field in entry)
    if present_price_fields:
        fail(f"{label} status=missing must omit price fields: {present_price_fields}")


def validate_priced_entry(entry: dict[str, Json], label: str) -> None:
    base_date = parse_date(entry.get("baseDate"), f"{label}.baseDate")
    last_date = parse_date(entry.get("lastDate"), f"{label}.lastDate")
    attempted_at = parse_date(entry.get("attemptedAt"), f"{label}.attemptedAt")
    if base_date > last_date:
        fail(f"{label}.baseDate must be <= lastDate")
    if last_date > attempted_at:
        fail(f"{label}.lastDate must be <= attemptedAt")

    base_price = require_positive_number(entry.get("basePrice"), f"{label}.basePrice")
    last_close = require_positive_number(entry.get("lastClose"), f"{label}.lastClose")
    change_pct = require_number(entry.get("changePct"), f"{label}.changePct")
    expected = round((last_close - base_price) / base_price * 100, 1)
    if abs(change_pct - expected) > 0.15:
        fail(f"{label}.changePct inconsistent: {change_pct} vs expected {expected}")


def validate_price_entry(
    entry: dict[str, Json],
    index: int,
    reports_by_id: dict[str, dict[str, Json]],
    seen_report_ids: set[str],
) -> None:
    label = f"prices.json.entries[{index}]"
    report_id = require_string(entry.get("reportId"), f"{label}.reportId")
    if report_id in seen_report_ids:
        fail(f"duplicate price reportId: {report_id}")
    seen_report_ids.add(report_id)
    report = reports_by_id.get(report_id)
    if report is None:
        fail(f"{label}.reportId references unknown report: {report_id}")

    symbol = require_string(entry.get("symbol"), f"{label}.symbol")
    report_symbol = report.get("priceSymbol")
    if report_symbol != symbol:
        fail(f"{label}.symbol must match reports.json priceSymbol for {report_id}: {report_symbol}")

    status = require_string(entry.get("status"), f"{label}.status")
    if status not in STATUS_VALUES:
        fail(f"{label}.status must be one of {sorted(STATUS_VALUES)}: {status}")
    parse_date(entry.get("attemptedAt"), f"{label}.attemptedAt")

    if status == "missing":
        validate_missing_entry(entry, label)
    else:
        validate_priced_entry(entry, label)


def validate_prices_data(data: Json, reports: list[Json]) -> None:
    root = require_dict(data, "prices.json")
    parse_date(root.get("generatedAt"), "prices.json.generatedAt")
    entries = require_list(root.get("entries"), "prices.json.entries")
    reports_by_id = read_reports_by_id(reports)
    seen_report_ids: set[str] = set()
    for index, item in enumerate(entries):
        validate_price_entry(require_dict(item, f"prices.json.entries[{index}]"), index, reports_by_id, seen_report_ids)


def main() -> None:
    reports = require_list(load_json(REPORTS_JSON), "reports.json")
    prices = load_json(PRICES_JSON)
    validate_prices_data(prices, reports)
    print(f"OK: validated research prices in {PRICES_JSON}")


if __name__ == "__main__":
    main()
