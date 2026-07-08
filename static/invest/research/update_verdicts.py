#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["yfinance"]
# ///
# ─── How to run ───
# python3 static/invest/research/update_verdicts.py
#
# Track 3 verdict ledger (docs/research-hub-v5-stance-conviction-plan.md §4). Scores
# every current-chain report's stance against a per-layer benchmark over the same
# window, and turns prior stanceHistory[] entries into closed intervals. Reuses
# the price fetch layer in update_prices.py; the resolved benchmark values are
# persisted so verdict-ledger.html never fetches.
#
# v6 (docs/research-hub-v6-plan.md Track 1): the benchmark is no longer SMH for
# every entry. resolution order per report:
#   report.benchmarkSymbol (override) → layerDefaults[chainLayer] → "default"
# Each scored entry and NEW closed interval carries its own benchmarkSymbol.
# Pre-v6 closed intervals are relabeled "SMH" retroactively (mechanical relabel,
# NOT a rescore — they were originally computed against SMH; principle 3).

from __future__ import annotations

import sys
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Final, Union

from update_prices import (
    PriceDataUnavailable,
    PriceQuote,
    ROOT,
    REPORTS_JSON,
    fetch_quotes,
    iso_day,
    load_json,
    parse_day,
    save_json,
)

Json = Union[None, bool, int, float, str, list["Json"], dict[str, "Json"]]
Report = dict[str, Json]

PRICES_JSON: Final = ROOT / "data" / "prices.json"
VERDICTS_JSON: Final = ROOT / "data" / "verdicts.json"
BENCHMARKS_JSON: Final = ROOT / "data" / "benchmarks.json"
LEGACY_BENCHMARK: Final = "SMH"  # the score everything was historically computed against
# stale = held long enough that the thesis window is overdue for a look
STALE_DAYS: Final = 120
FETCH_BUFFER_DAYS: Final = 7


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def pct_change(start: float, end: float) -> float:
    return round((end - start) / start * 100, 1)


@dataclass(frozen=True, slots=True)
class BenchmarkSeries:
    symbol: str
    quotes: tuple[PriceQuote, ...]

    def close_on_or_before(self, target: date) -> float:
        prior = [quote for quote in self.quotes if quote.date <= target]
        if not prior:
            raise PriceDataUnavailable(f"{self.symbol}: no close on or before {target}")
        return max(prior, key=lambda quote: quote.date).close


def load_reports() -> list[Report]:
    data = load_json(REPORTS_JSON)
    if not isinstance(data, list):
        fail("reports.json must be an array")
    return [item for item in data if isinstance(item, dict)]


def load_benchmarks() -> dict[str, Json]:
    if not BENCHMARKS_JSON.exists():
        fail(f"missing file: {BENCHMARKS_JSON}")
    data = load_json(BENCHMARKS_JSON)
    if not isinstance(data, dict):
        fail("benchmarks.json must be an object")
    return data


def current_chain_reports(reports: list[Report]) -> list[Report]:
    return [
        report
        for report in reports
        if report.get("chainLayer") and report.get("isCurrent") is not False
    ]


def resolve_benchmark_symbol(report: Report, benchmarks: dict[str, Json]) -> str:
    """Per spec §2.1 resolution order: override → layer default → book default."""
    override = report.get("benchmarkSymbol")
    if isinstance(override, str) and override:
        return override
    layer = report.get("chainLayer")
    if isinstance(layer, str):
        layer_defaults = benchmarks.get("layerDefaults")
        if isinstance(layer_defaults, dict):
            sym = layer_defaults.get(layer)
            if isinstance(sym, str) and sym:
                return sym
    default = benchmarks.get("default")
    if not isinstance(default, str) or not default:
        fail("benchmarks.json.default missing or invalid")
    return default


def price_entries_by_id(prices: Json) -> dict[str, dict[str, Json]]:
    entries = prices.get("entries") if isinstance(prices, dict) else None
    result: dict[str, dict[str, Json]] = {}
    if isinstance(entries, list):
        for entry in entries:
            if isinstance(entry, dict) and isinstance(entry.get("reportId"), str):
                result[entry["reportId"]] = entry
    return result


def history_dates(reports: list[Report]) -> list[date]:
    days: list[date] = []
    for report in reports:
        for entry in report.get("stanceHistory") or []:
            if isinstance(entry, dict):
                days.append(parse_day(entry.get("date"), f"{report.get('id')}.stanceHistory.date"))
    return days


def is_migration(from_entry: dict[str, Json]) -> bool:
    # The backfill seeds entry 1 with the pre-v5 legacy stance and no conviction
    # (spec §3.3); the legacy→v2 transition is a schema migration, not a real call.
    return "conviction" not in from_entry


def monitoring_overdue(report: Report, today: date) -> bool:
    current_month = today.strftime("%Y-%m")
    for item in report.get("monitoring") or []:
        if not isinstance(item, dict):
            continue
        next_check = item.get("nextCheckDate")
        if isinstance(next_check, str) and next_check[:7] < current_month:
            return True
    return False


def open_call_entry(
    report: Report,
    price_entry: dict[str, Json] | None,
    benchmarks: dict[str, BenchmarkSeries],
    benchmark_symbol: str,
    today: date,
) -> dict[str, Json]:
    history = report.get("stanceHistory") or []
    if not history or not isinstance(history[-1], dict):
        fail(f"{report.get('id')}: stanceHistory must contain at least one entry")
    last = history[-1]
    stance_date = parse_day(last.get("date"), f"{report['id']}.stanceHistory[-1].date")
    price_at_stance = float(last["price"])
    entry: dict[str, Json] = {
        "reportId": report["id"],
        "stance": report.get("stance"),
        "conviction": report.get("conviction"),
        "stanceDate": iso_day(stance_date),
        "priceAtStance": round(price_at_stance, 4),
        "benchmarkSymbol": benchmark_symbol,
    }

    priced = (
        isinstance(price_entry, dict)
        and isinstance(price_entry.get("lastClose"), (int, float))
        and isinstance(price_entry.get("lastDate"), str)
    )
    if not priced:
        entry["status"] = "no-price"
        entry["daysHeld"] = max((today - stance_date).days, 0)
        entry["stale"] = False
        return entry

    last_close = float(price_entry["lastClose"])
    last_date = parse_day(price_entry["lastDate"], f"{report['id']}.lastDate")
    if last_date <= stance_date:
        # No post-stance close yet: the call is same-day as (or newer than) the
        # latest tracked close, so there is no elapsed window to score. Stays
        # pending until a later close lands.
        entry["status"] = "pending"
        entry["daysHeld"] = max((today - stance_date).days, 0)
        entry["stale"] = False
        return entry
    change_pct = pct_change(price_at_stance, last_close)
    benchmark = benchmarks[benchmark_symbol]
    benchmark_change = pct_change(
        benchmark.close_on_or_before(stance_date),
        benchmark.close_on_or_before(last_date),
    )
    days_held = (last_date - stance_date).days
    entry.update(
        {
            "lastDate": iso_day(last_date),
            "lastClose": round(last_close, 4),
            "changePct": change_pct,
            "benchmarkChangePct": benchmark_change,
            "relativePct": round(change_pct - benchmark_change, 1),
            "daysHeld": days_held,
            "stale": days_held > STALE_DAYS and monitoring_overdue(report, today),
        }
    )
    return entry


def closed_interval_entries(
    report: Report,
    benchmarks: dict[str, BenchmarkSeries],
    benchmark_symbol: str,
) -> list[dict[str, Json]]:
    history = report.get("stanceHistory") or []
    intervals: list[dict[str, Json]] = []
    for start, end in zip(history, history[1:]):
        migration = is_migration(start)
        # Grandfather (spec §2.2, principle 3): pre-v6 migration intervals were
        # computed against SMH and are relabeled, not rescored — keep them on SMH
        # regardless of the report's current per-layer benchmark. Real (post-v6)
        # flips score against the report's resolved benchmark.
        interval_symbol = LEGACY_BENCHMARK if migration else benchmark_symbol
        benchmark = benchmarks[interval_symbol]
        start_date = parse_day(start.get("date"), f"{report['id']}.stanceHistory.date")
        end_date = parse_day(end.get("date"), f"{report['id']}.stanceHistory.date")
        start_price = float(start["price"])
        end_price = float(end["price"])
        change_pct = pct_change(start_price, end_price)
        benchmark_change = pct_change(
            benchmark.close_on_or_before(start_date),
            benchmark.close_on_or_before(end_date),
        )
        intervals.append(
            {
                "reportId": report["id"],
                "fromStance": start.get("stance"),
                "toStance": end.get("stance"),
                "toConviction": end.get("conviction"),
                "startDate": iso_day(start_date),
                "startPrice": round(start_price, 4),
                "endDate": iso_day(end_date),
                "endPrice": round(end_price, 4),
                "changePct": change_pct,
                "benchmarkChangePct": benchmark_change,
                "relativePct": round(change_pct - benchmark_change, 1),
                "daysHeld": (end_date - start_date).days,
                "migration": migration,
                "benchmarkSymbol": interval_symbol,
            }
        )
    return intervals


def build_verdicts(
    reports: list[Report],
    prices: Json,
    benchmarks_cfg: dict[str, Json],
    benchmark_series: dict[str, BenchmarkSeries],
    today: date,
) -> dict[str, Json]:
    chain = current_chain_reports(reports)
    by_id = price_entries_by_id(prices)
    open_calls: list[dict[str, Json]] = []
    closed: list[dict[str, Json]] = []
    for r in chain:
        sym = resolve_benchmark_symbol(r, benchmarks_cfg)
        open_calls.append(
            open_call_entry(r, by_id.get(r["id"]), benchmark_series, sym, today)
        )
        closed.extend(closed_interval_entries(r, benchmark_series, sym))
    return {
        "generatedAt": iso_day(today),
        # Book-level reference kept for backward compat (spec §2.2 line 76);
        # the per-entry benchmarkSymbol is authoritative.
        "benchmark": benchmarks_cfg.get("default", LEGACY_BENCHMARK),
        "entries": open_calls,
        "closed": closed,
    }


def main() -> None:
    today = datetime.now(timezone.utc).date()
    reports = load_reports()
    chain = current_chain_reports(reports)
    if not chain:
        fail("no current-chain reports to score")

    benchmarks_cfg = load_benchmarks()
    # Resolve the distinct benchmark symbols we need to fetch.
    needed_symbols: set[str] = set()
    for r in chain:
        needed_symbols.add(resolve_benchmark_symbol(r, benchmarks_cfg))
    # Migration intervals are grandfathered to SMH (closed_interval_entries), so
    # ensure that series is fetched even if no open call resolves to it.
    if any(
        is_migration(start)
        for r in chain
        for start, _end in zip(r.get("stanceHistory") or [], (r.get("stanceHistory") or [])[1:])
    ):
        needed_symbols.add(LEGACY_BENCHMARK)

    dates = history_dates(chain)
    if not dates:
        fail("current-chain reports have no stanceHistory dates")
    start = min(dates) - timedelta(days=FETCH_BUFFER_DAYS)

    benchmark_series: dict[str, BenchmarkSeries] = {}
    for sym in sorted(needed_symbols):
        try:
            quotes, _currency = fetch_quotes(sym, start, today)
        except Exception as exc:  # network/fetch failure — same convention as update_prices
            fail(f"benchmark fetch failed for {sym}: {exc}")
        if not quotes:
            fail(f"benchmark {sym}: no closes returned for {start}..{today}")
        benchmark_series[sym] = BenchmarkSeries(
            symbol=sym, quotes=tuple(sorted(quotes, key=lambda q: q.date))
        )

    prices = load_json(PRICES_JSON) if PRICES_JSON.exists() else {}
    data = build_verdicts(reports, prices, benchmarks_cfg, benchmark_series, today)
    changed = save_json(VERDICTS_JSON, data)
    open_count = len(data["entries"])
    closed_count = len(data["closed"])
    bench_counts = {}
    for e in data["entries"]:
        bench_counts[e.get("benchmarkSymbol", "?")] = (
            bench_counts.get(e.get("benchmarkSymbol", "?"), 0) + 1
        )
    bench_summary = ", ".join(f"{k}={v}" for k, v in sorted(bench_counts.items()))
    print(
        f"Saved {open_count} open calls + {closed_count} closed intervals "
        f"to {VERDICTS_JSON} [{bench_summary}]"
        if changed
        else f"No verdict changes detected [{bench_summary}]"
    )


if __name__ == "__main__":
    main()