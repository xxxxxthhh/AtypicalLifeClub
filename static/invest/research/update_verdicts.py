#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["yfinance"]
# ///
# ─── How to run ───
# python3 static/invest/research/update_verdicts.py
#
# Track 3 verdict ledger (docs/research-hub-v5-stance-conviction-plan.md §4). Scores
# every current-chain report's stance against the SMH benchmark over the same window,
# and turns prior stanceHistory[] entries into closed intervals. Reuses the price
# fetch layer in update_prices.py; the resolved benchmark values are persisted so
# verdict-ledger.html never fetches.

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
DEFAULT_BENCHMARK: Final = "SMH"
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


def current_chain_reports(reports: list[Report]) -> list[Report]:
    return [
        report
        for report in reports
        if report.get("chainLayer") and report.get("isCurrent") is not False
    ]


def benchmark_symbol(reports: list[Report]) -> str:
    for report in reports:
        if report.get("benchmark") and isinstance(report.get("priceSymbol"), str):
            return report["priceSymbol"]
    return DEFAULT_BENCHMARK


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
    benchmark: BenchmarkSeries,
    today: date,
) -> dict[str, Json]:
    history = report.get("stanceHistory") or []
    last = history[-1]
    stance_date = parse_day(last.get("date"), f"{report['id']}.stanceHistory[-1].date")
    price_at_stance = float(last["price"])
    entry: dict[str, Json] = {
        "reportId": report["id"],
        "stance": report.get("stance"),
        "conviction": report.get("conviction"),
        "stanceDate": iso_day(stance_date),
        "priceAtStance": round(price_at_stance, 4),
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


def closed_interval_entries(report: Report, benchmark: BenchmarkSeries) -> list[dict[str, Json]]:
    history = report.get("stanceHistory") or []
    intervals: list[dict[str, Json]] = []
    for start, end in zip(history, history[1:]):
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
                "migration": is_migration(start),
            }
        )
    return intervals


def build_verdicts(
    reports: list[Report],
    prices: Json,
    benchmark: BenchmarkSeries,
    today: date,
) -> dict[str, Json]:
    chain = current_chain_reports(reports)
    by_id = price_entries_by_id(prices)
    open_calls = [open_call_entry(r, by_id.get(r["id"]), benchmark, today) for r in chain]
    closed = [interval for r in chain for interval in closed_interval_entries(r, benchmark)]
    return {
        "generatedAt": iso_day(today),
        "benchmark": benchmark.symbol,
        "entries": open_calls,
        "closed": closed,
    }


def main() -> None:
    today = datetime.now(timezone.utc).date()
    reports = load_reports()
    chain = current_chain_reports(reports)
    if not chain:
        fail("no current-chain reports to score")

    symbol = benchmark_symbol(reports)
    start = min(history_dates(chain)) - timedelta(days=FETCH_BUFFER_DAYS)
    try:
        quotes, _currency = fetch_quotes(symbol, start, today)
    except Exception as exc:  # network/fetch failure — same convention as update_prices
        fail(f"benchmark fetch failed for {symbol}: {exc}")
    if not quotes:
        fail(f"benchmark {symbol}: no closes returned for {start}..{today}")
    benchmark = BenchmarkSeries(symbol=symbol, quotes=tuple(sorted(quotes, key=lambda q: q.date)))

    prices = load_json(PRICES_JSON) if PRICES_JSON.exists() else {}
    data = build_verdicts(reports, prices, benchmark, today)
    changed = save_json(VERDICTS_JSON, data)
    open_count = len(data["entries"])
    closed_count = len(data["closed"])
    print(
        f"Saved {open_count} open calls + {closed_count} closed intervals to {VERDICTS_JSON}"
        if changed
        else "No verdict changes detected"
    )


if __name__ == "__main__":
    main()
