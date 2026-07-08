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
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Final, Union

import calibration_history


Json = Union[None, bool, int, float, str, list["Json"], dict[str, "Json"]]

ROOT: Final = Path(__file__).resolve().parent
REPORTS_JSON: Final = ROOT / "data" / "reports.json"
PRICES_JSON: Final = ROOT / "data" / "prices.json"
VERDICTS_JSON: Final = ROOT / "data" / "verdicts.json"
CALIBRATION_HISTORY_JSON: Final = ROOT / "data" / "calibration-history.json"

STANCE_V2_VALUES: Final = {"bullish", "constructive", "neutral-watch", "cautious", "bearish-avoid"}
# stanceHistory keeps legacy values for non-last entries (spec §2.3), so a closed
# interval's fromStance may be a legacy value; toStance is always v2.
LEGACY_STANCE_VALUES: Final = {"high-risk-watch"}
STANCE_VALUES: Final = STANCE_V2_VALUES | LEGACY_STANCE_VALUES
CONVICTION_VALUES: Final = {"high", "medium", "low"}
PCT_TOLERANCE: Final = 0.15
PRICE_TOLERANCE: Final = 0.0001
STRICT_COVERAGE_FLAG: Final = "--strict-coverage"
# v6 (docs/research-hub-v6-plan.md §2.1): per-layer benchmark resolution.
BENCHMARKS_JSON: Final = ROOT / "data" / "benchmarks.json"
LEGACY_BENCHMARK: Final = "SMH"  # migration intervals are grandfathered to this (§2.2)


@dataclass(frozen=True, slots=True)
class ValidationOptions:
    prices: Json
    strict_coverage: bool
    benchmarks: Json  # parsed benchmarks.json for resolution recompute + self-ban
    reports_by_id: dict[str, dict[str, Json]]


@dataclass(slots=True)
class OpenEntryValidationState:
    chain_ids: set[str]
    seen: set[str]
    price_entries: dict[str, dict[str, Json]]
    benchmarks: Json
    reports_by_id: dict[str, dict[str, Json]]


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


def check_relative(
    change_pct: float,
    benchmark_pct: float,
    relative_pct: float,
    label: str,
    relative_field: str = "relativePct",
) -> None:
    expected = round(change_pct - benchmark_pct, 1)
    if abs(relative_pct - expected) > PCT_TOLERANCE:
        fail(f"{label}.{relative_field} inconsistent: {relative_pct} vs expected {expected}")


def check_change(start: float, end: float, change_pct: float, label: str) -> None:
    expected = round((end - start) / start * 100, 1)
    if abs(change_pct - expected) > PCT_TOLERANCE:
        fail(f"{label}.changePct inconsistent: {change_pct} vs expected {expected}")


def validate_book_reference(entry: dict[str, Json], change_pct: float, label: str) -> None:
    book_symbol = require_string(entry.get("bookBenchmarkSymbol"), f"{label}.bookBenchmarkSymbol")
    if book_symbol != LEGACY_BENCHMARK:
        fail(f"{label}.bookBenchmarkSymbol must be {LEGACY_BENCHMARK}: {book_symbol}")
    book_benchmark_pct = require_number(entry.get("bookBenchmarkChangePct"), f"{label}.bookBenchmarkChangePct")
    book_relative_pct = require_number(entry.get("bookRelativePct"), f"{label}.bookRelativePct")
    check_relative(change_pct, book_benchmark_pct, book_relative_pct, label, "bookRelativePct")


def price_entries_by_id(prices: Json) -> dict[str, dict[str, Json]]:
    root = require_dict(prices, "prices.json")
    entries = require_list(root.get("entries"), "prices.json.entries")
    result: dict[str, dict[str, Json]] = {}
    for index, item in enumerate(entries):
        entry = require_dict(item, f"prices.json.entries[{index}]")
        report_id = require_string(entry.get("reportId"), f"prices.json.entries[{index}].reportId")
        result[report_id] = entry
    return result


def current_chain_ids(reports: list[Json]) -> set[str]:
    ids: set[str] = set()
    for index, item in enumerate(reports):
        report = require_dict(item, f"reports.json[{index}]")
        if report.get("chainLayer") and report.get("isCurrent") is not False:
            ids.add(require_string(report.get("id"), f"reports.json[{index}].id"))
    return ids


def reports_by_id_map(reports: list[Json]) -> dict[str, dict[str, Json]]:
    result: dict[str, dict[str, Json]] = {}
    for item in reports:
        if isinstance(item, dict) and isinstance(item.get("id"), str):
            result[item["id"]] = item
    return result


def resolve_benchmark_symbol(report: dict[str, Json], benchmarks: Json) -> str:
    """Mirror of update_verdicts.resolve_benchmark_symbol for validator use."""
    bench = require_dict(benchmarks, "benchmarks.json")
    override = report.get("benchmarkSymbol")
    if isinstance(override, str) and override:
        return override
    layer = report.get("chainLayer")
    if isinstance(layer, str):
        layer_defaults = bench.get("layerDefaults")
        if isinstance(layer_defaults, dict):
            sym = layer_defaults.get(layer)
            if isinstance(sym, str) and sym:
                return sym
    return require_string(bench.get("default"), "benchmarks.json.default")


def is_current_chain_report(report: dict[str, Json]) -> bool:
    return bool(report.get("chainLayer")) and report.get("isCurrent") is not False


def validate_benchmark_symbol(
    entry: dict[str, Json],
    report_id: str,
    label: str,
    state: OpenEntryValidationState,
    expected: str | None = None,
) -> None:
    """v6 §2.1: benchmarkSymbol required on scored entries, equals the expected
    resolution, self-benchmark ban scoped to current-chain reports (benchmark-only
    sleeves exempt). `expected` defaults to the report's resolved benchmark; callers
    override it for grandfathered migration intervals (spec §2.2 → SMH)."""
    bench_sym = require_string(entry.get("benchmarkSymbol"), f"{label}.benchmarkSymbol")
    report = state.reports_by_id.get(report_id)
    if report is None:
        fail(f"{label}.reportId not found in reports.json: {report_id}")
    if expected is None:
        expected = resolve_benchmark_symbol(report, state.benchmarks)
    if bench_sym != expected:
        fail(
            f"{label}.benchmarkSymbol ({bench_sym}) does not match expected "
            f"benchmark for {report_id} ({expected})"
        )
    # Self-benchmark ban: a current-chain scored report must not resolve to its
    # own priceSymbol (copx-2026 would otherwise self-score 0.0 forever). The
    # ban is scoped via is_current_chain_report so benchmark-only sleeves
    # (smh-2026: benchmark:true, priceSymbol:SMH, no chainLayer) are exempt.
    if is_current_chain_report(report):
        price_symbol = report.get("priceSymbol")
        if isinstance(price_symbol, str) and price_symbol and bench_sym == price_symbol:
            fail(
                f"{label}.benchmarkSymbol for {report_id} equals its own "
                f"priceSymbol ({bench_sym}) — self-benchmark banned (§2.1)"
            )


def validate_open_entry(
    entry: dict[str, Json],
    index: int,
    state: OpenEntryValidationState,
) -> None:
    label = f"verdicts.json.entries[{index}]"
    report_id = require_string(entry.get("reportId"), f"{label}.reportId")
    if report_id not in state.chain_ids:
        fail(f"{label}.reportId is not a current-chain report: {report_id}")
    if report_id in state.seen:
        fail(f"duplicate open-call reportId: {report_id}")
    state.seen.add(report_id)

    require_enum(entry.get("stance"), STANCE_V2_VALUES, f"{label}.stance")
    require_enum(entry.get("conviction"), CONVICTION_VALUES, f"{label}.conviction")
    stance_date = parse_date(entry.get("stanceDate"), f"{label}.stanceDate")
    require_positive_number(entry.get("priceAtStance"), f"{label}.priceAtStance")

    # v6 §2.1: benchmarkSymbol required on every entry (resolution is a static
    # function of the report, not the price state); validate consistency +
    # self-ban here.
    validate_benchmark_symbol(entry, report_id, label, state)

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
    validate_book_reference(entry, change_pct, label)

    days_held = require_number(entry.get("daysHeld"), f"{label}.daysHeld")
    if days_held != (last_date - stance_date).days:
        fail(f"{label}.daysHeld inconsistent: {days_held}")
    require_bool(entry.get("stale"), f"{label}.stale")

    price_entry = state.price_entries.get(report_id)
    if price_entry is None:
        fail(f"{label}.reportId has scored verdict but no prices.json entry: {report_id}")
    price_last_date = require_string(price_entry.get("lastDate"), f"prices.json[{report_id}].lastDate")
    if price_last_date != entry.get("lastDate"):
        fail(f"{label}.lastDate does not match prices.json for {report_id}: {entry.get('lastDate')} vs {price_last_date}")
    price_last_close = require_positive_number(price_entry.get("lastClose"), f"prices.json[{report_id}].lastClose")
    if abs(last_close - price_last_close) > PRICE_TOLERANCE:
        fail(f"{label}.lastClose does not match prices.json for {report_id}: {last_close} vs {price_last_close}")


def validate_closed_entry(
    entry: dict[str, Json], index: int, chain_ids: set[str], state: OpenEntryValidationState
) -> None:
    label = f"verdicts.json.closed[{index}]"
    report_id = require_string(entry.get("reportId"), f"{label}.reportId")
    if report_id not in chain_ids:
        fail(f"{label}.reportId is not a current-chain report: {report_id}")

    # v6 §2.1/§2.2: closed intervals carry a benchmarkSymbol. Migration intervals
    # are grandfathered to SMH (relabel of what was actually used, not a rescore);
    # real flips use the report's resolved per-layer benchmark.
    migration = entry.get("migration")
    expected_symbol = LEGACY_BENCHMARK if migration is True else None
    validate_benchmark_symbol(entry, report_id, label, state, expected=expected_symbol)

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
    validate_book_reference(entry, change_pct, label)

    if require_number(entry.get("daysHeld"), f"{label}.daysHeld") != (end_date - start_date).days:
        fail(f"{label}.daysHeld inconsistent")
    require_bool(entry.get("migration"), f"{label}.migration")


def validate_verdicts_data(data: Json, reports: list[Json], options: ValidationOptions) -> list[str]:
    root = require_dict(data, "verdicts.json")
    verdicts_generated_at = parse_date(root.get("generatedAt"), "verdicts.json.generatedAt")
    require_string(root.get("benchmark"), "verdicts.json.benchmark")
    entries = require_list(root.get("entries"), "verdicts.json.entries")
    closed = require_list(root.get("closed"), "verdicts.json.closed")
    prices_generated_at = parse_date(require_dict(options.prices, "prices.json").get("generatedAt"), "prices.json.generatedAt")
    if verdicts_generated_at < prices_generated_at:
        fail(
            "verdicts.json.generatedAt must not be older than prices.json.generatedAt: "
            f"{verdicts_generated_at:%Y-%m-%d} vs {prices_generated_at:%Y-%m-%d}"
        )

    chain_ids = current_chain_ids(reports)
    state = OpenEntryValidationState(
        chain_ids=chain_ids,
        seen=set(),
        price_entries=price_entries_by_id(options.prices),
        benchmarks=options.benchmarks,
        reports_by_id=options.reports_by_id,
    )
    for index, item in enumerate(entries):
        validate_open_entry(require_dict(item, f"verdicts.json.entries[{index}]"), index, state)
    missing = chain_ids - state.seen
    warnings: list[str] = []
    if missing:
        message = f"verdicts.json.entries missing current-chain reports: {sorted(missing)}"
        if options.strict_coverage:
            fail(message)
        warnings.append(message)

    for index, item in enumerate(closed):
        validate_closed_entry(
            require_dict(item, f"verdicts.json.closed[{index}]"), index, chain_ids, state
        )
    return warnings


def strict_coverage_from_argv(argv: list[str]) -> bool:
    if not argv:
        return False
    if argv == [STRICT_COVERAGE_FLAG]:
        return True
    if argv == ["--help"]:
        print(f"Usage: python3 static/invest/research/validate_verdicts.py [{STRICT_COVERAGE_FLAG}]")
        sys.exit(0)
    fail(f"unknown arguments: {argv}")


def validate_calibration_history_data(history: Json, verdicts: Json) -> None:
    try:
        calibration_history.validate_history_rows(history, verdicts)
    except calibration_history.CalibrationHistoryError as exc:
        fail(str(exc))


def main() -> None:
    reports = require_list(load_json(REPORTS_JSON), "reports.json")
    verdicts = load_json(VERDICTS_JSON)
    prices = load_json(PRICES_JSON)
    benchmarks = load_json(BENCHMARKS_JSON)
    calibration_history_data = load_json(CALIBRATION_HISTORY_JSON)
    warnings = validate_verdicts_data(
        verdicts,
        reports,
        ValidationOptions(
            prices=prices,
            strict_coverage=strict_coverage_from_argv(sys.argv[1:]),
            benchmarks=benchmarks,
            reports_by_id=reports_by_id_map(reports),
        ),
    )
    validate_calibration_history_data(calibration_history_data, verdicts)
    for warning in warnings:
        print(f"WARN: {warning}")
    print(f"OK: validated verdict ledger in {VERDICTS_JSON}")


if __name__ == "__main__":
    main()
