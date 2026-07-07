#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
# ─── How to run ───
# python3 static/invest/research/validate_verdicts.py

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
VERDICTS_JSON: Final = ROOT / "data" / "verdicts.json"

STANCE_V2_VALUES: Final = {"bullish", "constructive", "neutral-watch", "cautious", "bearish-avoid"}
# stanceHistory keeps legacy values for non-last entries (spec §2.3), so a closed
# interval's fromStance may be a legacy value; toStance is always v2.
LEGACY_STANCE_VALUES: Final = {"high-risk-watch"}
STANCE_VALUES: Final = STANCE_V2_VALUES | LEGACY_STANCE_VALUES
CONVICTION_VALUES: Final = {"high", "medium", "low"}
PCT_TOLERANCE: Final = 0.15


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


def require_enum(value: Json, allowed: set[str], label: str) -> str:
    text = require_string(value, label)
    if text not in allowed:
        fail(f"{label} must be one of {sorted(allowed)}: {text}")
    return text


def require_bool(value: Json, label: str) -> bool:
    if not isinstance(value, bool):
        fail(f"{label} must be a boolean")
    return value


def check_relative(change_pct: float, benchmark_pct: float, relative_pct: float, label: str) -> None:
    expected = round(change_pct - benchmark_pct, 1)
    if abs(relative_pct - expected) > PCT_TOLERANCE:
        fail(f"{label}.relativePct inconsistent: {relative_pct} vs expected {expected}")


def check_change(start: float, end: float, change_pct: float, label: str) -> None:
    expected = round((end - start) / start * 100, 1)
    if abs(change_pct - expected) > PCT_TOLERANCE:
        fail(f"{label}.changePct inconsistent: {change_pct} vs expected {expected}")


def current_chain_ids(reports: list[Json]) -> set[str]:
    ids: set[str] = set()
    for index, item in enumerate(reports):
        report = require_dict(item, f"reports.json[{index}]")
        if report.get("chainLayer") and report.get("isCurrent") is not False:
            ids.add(require_string(report.get("id"), f"reports.json[{index}].id"))
    return ids


def validate_open_entry(entry: dict[str, Json], index: int, chain_ids: set[str], seen: set[str]) -> None:
    label = f"verdicts.json.entries[{index}]"
    report_id = require_string(entry.get("reportId"), f"{label}.reportId")
    if report_id not in chain_ids:
        fail(f"{label}.reportId is not a current-chain report: {report_id}")
    if report_id in seen:
        fail(f"duplicate open-call reportId: {report_id}")
    seen.add(report_id)

    require_enum(entry.get("stance"), STANCE_V2_VALUES, f"{label}.stance")
    require_enum(entry.get("conviction"), CONVICTION_VALUES, f"{label}.conviction")
    stance_date = parse_date(entry.get("stanceDate"), f"{label}.stanceDate")
    require_positive_number(entry.get("priceAtStance"), f"{label}.priceAtStance")

    # "no-price" (tracker has no close) and "pending" (call newer than the latest
    # close) both carry no scorable delta yet — spec §4.1a / §4.2.
    if entry.get("status") in {"no-price", "pending"}:
        require_number(entry.get("daysHeld"), f"{label}.daysHeld")
        require_bool(entry.get("stale"), f"{label}.stale")
        return

    price_at_stance = float(entry["priceAtStance"])
    last_date = parse_date(entry.get("lastDate"), f"{label}.lastDate")
    if last_date < stance_date:
        fail(f"{label}.lastDate must be >= stanceDate")
    last_close = require_positive_number(entry.get("lastClose"), f"{label}.lastClose")
    change_pct = require_number(entry.get("changePct"), f"{label}.changePct")
    benchmark_pct = require_number(entry.get("benchmarkChangePct"), f"{label}.benchmarkChangePct")
    relative_pct = require_number(entry.get("relativePct"), f"{label}.relativePct")
    check_change(price_at_stance, last_close, change_pct, label)
    check_relative(change_pct, benchmark_pct, relative_pct, label)

    days_held = require_number(entry.get("daysHeld"), f"{label}.daysHeld")
    if days_held != (last_date - stance_date).days:
        fail(f"{label}.daysHeld inconsistent: {days_held}")
    require_bool(entry.get("stale"), f"{label}.stale")


def validate_closed_entry(entry: dict[str, Json], index: int, chain_ids: set[str]) -> None:
    label = f"verdicts.json.closed[{index}]"
    report_id = require_string(entry.get("reportId"), f"{label}.reportId")
    if report_id not in chain_ids:
        fail(f"{label}.reportId is not a current-chain report: {report_id}")

    require_enum(entry.get("fromStance"), STANCE_VALUES, f"{label}.fromStance")
    require_enum(entry.get("toStance"), STANCE_V2_VALUES, f"{label}.toStance")
    if entry.get("toConviction") is not None:
        require_enum(entry.get("toConviction"), CONVICTION_VALUES, f"{label}.toConviction")

    start_date = parse_date(entry.get("startDate"), f"{label}.startDate")
    end_date = parse_date(entry.get("endDate"), f"{label}.endDate")
    if end_date < start_date:
        fail(f"{label}.endDate must be >= startDate")
    start_price = require_positive_number(entry.get("startPrice"), f"{label}.startPrice")
    end_price = require_positive_number(entry.get("endPrice"), f"{label}.endPrice")
    change_pct = require_number(entry.get("changePct"), f"{label}.changePct")
    benchmark_pct = require_number(entry.get("benchmarkChangePct"), f"{label}.benchmarkChangePct")
    relative_pct = require_number(entry.get("relativePct"), f"{label}.relativePct")
    check_change(start_price, end_price, change_pct, label)
    check_relative(change_pct, benchmark_pct, relative_pct, label)

    if require_number(entry.get("daysHeld"), f"{label}.daysHeld") != (end_date - start_date).days:
        fail(f"{label}.daysHeld inconsistent")
    require_bool(entry.get("migration"), f"{label}.migration")


def validate_verdicts_data(data: Json, reports: list[Json]) -> None:
    root = require_dict(data, "verdicts.json")
    parse_date(root.get("generatedAt"), "verdicts.json.generatedAt")
    require_string(root.get("benchmark"), "verdicts.json.benchmark")
    entries = require_list(root.get("entries"), "verdicts.json.entries")
    closed = require_list(root.get("closed"), "verdicts.json.closed")

    chain_ids = current_chain_ids(reports)
    seen: set[str] = set()
    for index, item in enumerate(entries):
        validate_open_entry(require_dict(item, f"verdicts.json.entries[{index}]"), index, chain_ids, seen)
    missing = chain_ids - seen
    if missing:
        fail(f"verdicts.json.entries missing current-chain reports: {sorted(missing)}")

    for index, item in enumerate(closed):
        validate_closed_entry(require_dict(item, f"verdicts.json.closed[{index}]"), index, chain_ids)


def main() -> None:
    reports = require_list(load_json(REPORTS_JSON), "reports.json")
    verdicts = load_json(VERDICTS_JSON)
    validate_verdicts_data(verdicts, reports)
    print(f"OK: validated verdict ledger in {VERDICTS_JSON}")


if __name__ == "__main__":
    main()
