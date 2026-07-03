#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["yfinance"]
# ///
# ─── How to run ───
# python3 static/invest/research/update_prices.py

from __future__ import annotations

import json
import math
import sys
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Final, Union

import yfinance as yf


Json = Union[None, bool, int, float, str, list["Json"], dict[str, "Json"]]
PriceEntry = dict[str, Json]
Report = dict[str, Json]

ROOT: Final = Path(__file__).resolve().parent
REPORTS_JSON: Final = ROOT / "data" / "reports.json"
PRICES_JSON: Final = ROOT / "data" / "prices.json"
MAX_CARRIED_FORWARD_DAYS: Final = 10
PRICE_FIELDS: Final = (
    "baseDate",
    "basePrice",
    "lastDate",
    "lastClose",
    "changePct",
    "currency",
)


@dataclass(frozen=True, slots=True)
class PriceQuote:
    date: date
    close: float


class PriceDataUnavailable(Exception):
    pass


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def iso_day(day: date) -> str:
    return day.isoformat()


def parse_day(value: Json, label: str) -> date:
    if not isinstance(value, str):
        raise PriceDataUnavailable(f"{label} is not a date string")
    return datetime.strptime(value, "%Y-%m-%d").date()


def finite_float(value: Json) -> float | None:
    if not isinstance(value, (int, float)):
        return None
    number = float(value)
    return number if math.isfinite(number) else None


def load_json(path: Path) -> Json:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_json(path: Path, data: Json) -> bool:
    serialized = json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    if path.exists() and path.read_text(encoding="utf-8") == serialized:
        return False
    path.write_text(serialized, encoding="utf-8")
    return True


def load_reports() -> list[Report]:
    data = load_json(REPORTS_JSON)
    if not isinstance(data, list):
        fail("reports.json must be an array")
    reports: list[Report] = []
    for item in data:
        if isinstance(item, dict):
            reports.append(item)
    return reports


def current_chain_reports(reports: list[Report]) -> list[Report]:
    selected: list[Report] = []
    for report in reports:
        symbol = report.get("priceSymbol")
        if (
            report.get("isCurrent") is not False
            and report.get("chainLayer")
            and isinstance(symbol, str)
            and symbol.strip()
        ):
            selected.append(report)
    return selected


def load_previous_entries(path: Path = PRICES_JSON) -> dict[str, PriceEntry]:
    if not path.exists():
        return {}
    data = load_json(path)
    if not isinstance(data, dict):
        return {}
    entries = data.get("entries")
    if not isinstance(entries, list):
        return {}
    previous: dict[str, PriceEntry] = {}
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        report_id = entry.get("reportId")
        if isinstance(report_id, str):
            previous[report_id] = entry
    return previous


def report_string(report: Report, field: str) -> str:
    value = report.get(field)
    if not isinstance(value, str) or not value.strip():
        raise PriceDataUnavailable(f"{report.get('id', '<unknown>')} missing {field}")
    return value


def build_ok_entry(report: Report, quotes: list[PriceQuote], attempted_at: date, currency: str | None) -> PriceEntry:
    report_id = report_string(report, "id")
    symbol = report_string(report, "priceSymbol")
    price_as_of = parse_day(report.get("priceAsOf"), f"{report_id}.priceAsOf")
    base_quotes = [quote for quote in quotes if quote.date <= price_as_of]
    if not base_quotes:
        raise PriceDataUnavailable(f"{symbol}: no close on or before {price_as_of}")
    if not quotes:
        raise PriceDataUnavailable(f"{symbol}: no usable closes")

    base = max(base_quotes, key=lambda quote: quote.date)
    latest = max(quotes, key=lambda quote: quote.date)
    change_pct = round((latest.close - base.close) / base.close * 100, 1)
    entry: PriceEntry = {
        "reportId": report_id,
        "symbol": symbol,
        "status": "ok",
        "attemptedAt": iso_day(attempted_at),
        "baseDate": iso_day(base.date),
        "basePrice": round(base.close, 4),
        "lastDate": iso_day(latest.date),
        "lastClose": round(latest.close, 4),
        "changePct": change_pct,
    }
    if currency:
        entry["currency"] = currency
    return entry


def previous_has_price_fields(previous: PriceEntry) -> bool:
    return all(field in previous for field in PRICE_FIELDS if field != "currency")


def build_failure_entry(
    report_id: str,
    symbol: str,
    attempted_at: date,
    previous: PriceEntry | None,
) -> PriceEntry:
    if previous and previous_has_price_fields(previous):
        entry: PriceEntry = {
            "reportId": report_id,
            "symbol": symbol,
            "status": "carried-forward",
            "attemptedAt": iso_day(attempted_at),
        }
        for field in PRICE_FIELDS:
            if field in previous:
                entry[field] = previous[field]
        return entry

    return {
        "reportId": report_id,
        "symbol": symbol,
        "status": "missing",
        "attemptedAt": iso_day(attempted_at),
    }


def entry_is_stale(entry: PriceEntry, max_age_days: int = MAX_CARRIED_FORWARD_DAYS) -> bool:
    if entry.get("status") == "missing":
        return True
    try:
        last_date = parse_day(entry.get("lastDate"), "lastDate")
        attempted_at = parse_day(entry.get("attemptedAt"), "attemptedAt")
    except PriceDataUnavailable:
        return False
    return (attempted_at - last_date).days > max_age_days


def normalize_quote(index_value: Json, close_value: Json) -> PriceQuote | None:
    close = finite_float(close_value)
    if close is None or close <= 0:
        return None
    if hasattr(index_value, "date"):
        quote_date = index_value.date()
    else:
        quote_date = parse_day(str(index_value)[:10], "quote.date")
    return PriceQuote(date=quote_date, close=close)


def fetch_quotes(symbol: str, start: date, end: date) -> tuple[list[PriceQuote], str | None]:
    ticker = yf.Ticker(symbol)
    history = ticker.history(start=iso_day(start), end=iso_day(end + timedelta(days=1)), interval="1d")
    if getattr(history, "empty", True):
        return [], currency_from_ticker(ticker)

    quotes: list[PriceQuote] = []
    for index_value, row in history.iterrows():
        close_value = row.get("Close")
        quote = normalize_quote(index_value, close_value)
        if quote:
            quotes.append(quote)
    return quotes, currency_from_ticker(ticker)


def currency_from_ticker(ticker) -> str | None:
    fast_info = getattr(ticker, "fast_info", None)
    if isinstance(fast_info, dict):
        currency = fast_info.get("currency")
        if isinstance(currency, str) and currency.strip():
            return currency
    info = getattr(ticker, "info", None)
    if isinstance(info, dict):
        currency = info.get("currency")
        if isinstance(currency, str) and currency.strip():
            return currency
    return None


def build_price_entries(reports: list[Report], attempted_at: date, previous: dict[str, PriceEntry]) -> tuple[list[PriceEntry], int]:
    entries: list[PriceEntry] = []
    failure_count = 0
    for report in current_chain_reports(reports):
        report_id = report_string(report, "id")
        symbol = report_string(report, "priceSymbol")
        price_as_of = parse_day(report.get("priceAsOf"), f"{report_id}.priceAsOf")
        try:
            quotes, currency = fetch_quotes(symbol, price_as_of - timedelta(days=10), attempted_at)
            entry = build_ok_entry(report, quotes, attempted_at, currency)
            print(f"  OK {symbol}: {entry['lastClose']} ({entry['lastDate']})")
        except Exception as exc:
            failure_count += 1
            entry = build_failure_entry(report_id, symbol, attempted_at, previous.get(report_id))
            print(f"  {entry['status']} {symbol}: {exc}")
        entries.append(entry)
    return entries, failure_count


def main() -> None:
    attempted_at = datetime.now(timezone.utc).date()
    reports = load_reports()
    previous = load_previous_entries()
    entries, failure_count = build_price_entries(reports, attempted_at, previous)
    data: Json = {
        "generatedAt": iso_day(attempted_at),
        "entries": entries,
    }
    changed = save_json(PRICES_JSON, data)
    print(f"Saved {len(entries)} price entries to {PRICES_JSON}" if changed else "No price data changes detected")

    if failure_count > len(entries) / 2:
        fail(f"{failure_count}/{len(entries)} price fetches failed")
    stale_entries = [entry for entry in entries if entry_is_stale(entry)]
    if stale_entries:
        names = ", ".join(str(entry.get("symbol")) for entry in stale_entries)
        fail(f"missing or stale price data requires attention: {names}")


if __name__ == "__main__":
    main()
