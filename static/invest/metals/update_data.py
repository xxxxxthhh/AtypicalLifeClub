#!/usr/bin/env python3
"""
Daily update script for Metals module.
Fetches latest prices and appends to historical.json.
Designed to be run by GitHub Actions daily.
"""

import json
import math
from datetime import datetime, timezone
import sys
import os

from fetch_historical import (
    fetch_chart_result,
    fetch_daily_rows,
    parse_split_events,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "data", "historical.json")

# How far back each run re-reads and re-upserts.  Two reasons it is a window and
# not a single bar:
#   1. The exchange can revise a close after we first stored it.  The old path
#      took only df.iloc[-1], so a bar was written once and never looked at
#      again -- 111-114 rows per futures contract are wrong today precisely
#      because nothing ever went back to check them.
#   2. A skipped or failed run leaves a hole; the next run backfills it.
# 14 calendar days always spans at least nine completed sessions, even across a
# holiday week with two weekends in it, and costs one request per symbol either
# way.
RECENT_WINDOW_DAYS = 14

# Splits only matter for rows we actually store, and history is capped at
# LOOKBACK_DAYS, so a split older than the oldest row would back-adjust nothing.
SPLIT_LOOKBACK_DAYS = 730

ALL_SYMBOLS = [
    "GC=F", "SI=F", "PL=F", "PA=F", "HG=F",
    "COPX", "GLD", "SLV", "CPER", "DBB", "REMX", "LIT", "PPLT", "PALL",
]


def load_data(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(path, data):
    serialized = json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            if f.read() == serialized:
                return False

    with open(path, "w", encoding="utf-8") as f:
        f.write(serialized)
    return True


def is_finite_number(value):
    try:
        return math.isfinite(float(value))
    except (TypeError, ValueError):
        return False


def normalize_volume(value):
    if not is_finite_number(value):
        return 0
    return max(0, int(float(value)))


def normalize_record(record):
    """Return a stable daily record or None when price data is unusable."""
    close = record.get("close")
    if not is_finite_number(close):
        return None

    return {
        "date": record["date"],
        "close": round(float(close), 4),
        "volume": normalize_volume(record.get("volume", 0)),
    }


def fetch_splits(symbol):
    """Return [(YYYY-MM-DD, ratio), ...] ascending, or None when unavailable.

    None means "could not ask" and must not be confused with "no splits": a
    silent failure here is exactly how the 2026-05-18 PPLT/PALL splits poisoned
    two years of history.  Only a failed request or an unparseable response
    yields None -- a well-formed response with no `events` key is Yahoo saying
    the window holds no split, which is the same thing yfinance reported from
    the same endpoint.
    """
    try:
        result = fetch_chart_result(symbol, SPLIT_LOOKBACK_DAYS, events="splits")
        return parse_split_events(result)
    except Exception as e:
        print(f"  ✗ {symbol}: split lookup failed: {e}")
        return None


def apply_new_splits(data):
    """Back-adjust history for any split not yet applied.

    Returns (changed, failed_symbols). A non-empty failed_symbols must abort the
    whole run: the 35% continuity guard in validate_data.py is only a net for
    large splits, and it explicitly delegates small ones (3:2 and the like) to
    this function. If a lookup failed and we appended the day's bar anyway, an
    unadjusted split could slip past both layers.
    """
    metadata = data["metadata"]
    applied = metadata.setdefault("lastSplitApplied", {})
    log = metadata.setdefault("splitAdjustments", [])
    changed = False
    failed = []

    sections = {"metals": data["metals"], "etfs": data["etfs"]}
    for section_name, section in sections.items():
        for symbol, history in section.items():
            events = fetch_splits(symbol)
            if events is None:
                failed.append(symbol)
                continue

            seen = applied.get(symbol)
            for date, ratio in events:
                if seen is not None and date <= seen:
                    continue

                rows = 0
                for row in history:
                    if row["date"] < date:
                        row["close"] = round(row["close"] / ratio, 4)
                        rows += 1

                applied[symbol] = date
                log.append({
                    "symbol": symbol,
                    "date": date,
                    "ratio": ratio,
                    "rowsAdjusted": rows,
                    "appliedAt": datetime.now().isoformat(),
                })
                changed = True
                print(f"  ⚠ {symbol}: {ratio:g}:1 split on {date} — back-adjusted {rows} rows")

    return changed, failed


def fetch_recent(symbol, observed_at):
    """Fetch every completed daily bar in the rolling window, oldest first.

    Bars whose session has not closed yet are dropped upstream by
    fetch_historical.completed_rows; see the reasoning there.
    """
    try:
        return fetch_daily_rows(symbol, RECENT_WINDOW_DAYS, observed_at)
    except Exception as e:
        print(f"  ✗ {symbol}: {e}")
        return []


def apply_rows(history, rows):
    """Upsert every row into `history`, returning a tally of the outcomes."""
    counts = {"added": 0, "updated": 0, "unchanged": 0, "skipped": 0}
    for row in rows:
        counts[upsert_record(history, row)] += 1
    return counts


def update_section(section, symbols, observed_at):
    """Refresh one section in place; True when any row was added or corrected."""
    changed = False
    for symbol in symbols:
        rows = fetch_recent(symbol, observed_at)
        if not rows:
            print(f"  - {symbol}: no completed sessions in the last {RECENT_WINDOW_DAYS} days")
            continue

        counts = apply_rows(section[symbol], rows)
        changed = changed or counts["added"] > 0 or counts["updated"] > 0
        print(
            f"  ✓ {symbol}: {rows[-1]['close']} @ {rows[-1]['date']} "
            f"({counts['added']} added, {counts['updated']} corrected, "
            f"{counts['unchanged']} unchanged)"
        )
    return changed


def upsert_record(history_list, record):
    """Insert or update a record by date."""
    normalized = normalize_record(record)
    if normalized is None:
        return "skipped"

    for i, existing in enumerate(history_list):
        if existing["date"] == normalized["date"]:
            existing_normalized = normalize_record(existing)
            if existing_normalized is None or existing_normalized["close"] != normalized["close"]:
                history_list[i] = normalized
                return "updated"

            existing_volume = existing_normalized["volume"]
            if existing_volume == 0 and normalized["volume"] > 0:
                history_list[i] = normalized
                return "updated"

            return "unchanged"

    history_list.append(normalized)
    history_list.sort(key=lambda x: x["date"])
    return "added"


def build_current(data):
    """Build current prices from the latest two finite records per symbol."""
    current = {}
    all_data = {**data["metals"], **data["etfs"]}
    for symbol, history in all_data.items():
        valid_history = [row for row in history if normalize_record(row) is not None]
        if len(valid_history) >= 2:
            latest = normalize_record(valid_history[-1])
            prev = normalize_record(valid_history[-2])
            change = latest["close"] - prev["close"]
            pct = (change / prev["close"] * 100) if prev["close"] else 0
            current[symbol] = {
                "price": latest["close"],
                "change": round(change, 4),
                "changePct": round(pct, 2),
                "date": latest["date"],
            }
    return current


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DATA_PATH
    print(f"Loading data from {path}")
    data = load_data(path)

    # One clock for the whole run, so every symbol is judged complete against
    # the same instant no matter how long the run takes.
    observed_at = datetime.now(timezone.utc)
    print(f"Fetching latest data (observed at {observed_at.isoformat()})\n")

    # Splits must be applied before the new bar is appended, otherwise a
    # post-split close lands next to un-adjusted history.
    print("=== Checking for splits ===")
    changed_by_split, split_failures = apply_new_splits(data)
    if split_failures:
        print(
            f"\n❌ 拆分查询失败: {', '.join(split_failures)}\n"
            "   本次不写入任何数据。未核对拆分就追加当日价格，会让未复权的拆分\n"
            "   同时绕过本层与 validate_data.py 的 35% 跳变网。"
        )
        sys.exit(1)
    if not changed_by_split:
        print("  ✓ no new splits")
    print()

    metals_symbols = list(data["metadata"]["metals"].keys())
    etf_symbols = list(data["metadata"]["etfs"].keys())
    changed = changed_by_split

    print("=== Metals ===")
    changed |= update_section(data["metals"], metals_symbols, observed_at)

    print("\n=== ETFs ===")
    changed |= update_section(data["etfs"], etf_symbols, observed_at)

    # Rebuild current prices
    current = build_current(data)
    if data.get("current") != current:
        data["current"] = current
        changed = True

    if not changed:
        print("\n✅ No data changes detected; file left untouched")
        return

    data["metadata"]["last_updated"] = datetime.now().isoformat()

    if save_data(path, data):
        print(f"\n✅ Updated! Saved to {path}")
    else:
        print("\n✅ Serialized output unchanged; file left untouched")


if __name__ == "__main__":
    main()
