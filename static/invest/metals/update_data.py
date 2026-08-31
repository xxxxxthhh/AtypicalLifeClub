#!/usr/bin/env python3
"""
Daily update script for Metals module.
Fetches latest prices and appends to historical.json.
Designed to be run by GitHub Actions daily.
"""

import json
import math
import yfinance as yf
from datetime import datetime
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "data", "historical.json")

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
    two years of history.
    """
    try:
        splits = yf.Ticker(symbol).splits
    except Exception as e:
        print(f"  ✗ {symbol}: split lookup failed: {e}")
        return None

    events = []
    for stamp, ratio in splits.items():
        if not is_finite_number(ratio) or float(ratio) <= 0:
            continue
        events.append((stamp.strftime("%Y-%m-%d"), float(ratio)))
    return sorted(events)


def apply_new_splits(data):
    """Back-adjust history for any split not yet applied. Returns True if changed."""
    metadata = data["metadata"]
    applied = metadata.setdefault("lastSplitApplied", {})
    log = metadata.setdefault("splitAdjustments", [])
    changed = False

    sections = {"metals": data["metals"], "etfs": data["etfs"]}
    for section_name, section in sections.items():
        for symbol, history in section.items():
            events = fetch_splits(symbol)
            if events is None:
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

    return changed


def fetch_latest(symbol):
    """Fetch the most recent trading day's close."""
    try:
        ticker = yf.Ticker(symbol)
        df = ticker.history(period="5d", interval="1d")
        if df.empty:
            return None
        last = df.iloc[-1]
        close = last["Close"]
        if not is_finite_number(close):
            print(f"  - {symbol}: skipped non-finite close")
            return None
        return {
            "date": last.name.strftime("%Y-%m-%d"),
            "close": round(float(close), 4),
            "volume": normalize_volume(last["Volume"] if "Volume" in last else 0),
        }
    except Exception as e:
        print(f"  ✗ {symbol}: {e}")
        return None


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

    today = datetime.now().strftime("%Y-%m-%d")
    print(f"Fetching latest data ({today})\n")

    # Splits must be applied before the new bar is appended, otherwise a
    # post-split close lands next to un-adjusted history.
    print("=== Checking for splits ===")
    changed_by_split = apply_new_splits(data)
    if not changed_by_split:
        print("  ✓ no new splits")
    print()

    metals_symbols = list(data["metadata"]["metals"].keys())
    etf_symbols = list(data["metadata"]["etfs"].keys())
    changed = changed_by_split

    # Update metals
    for symbol in metals_symbols:
        record = fetch_latest(symbol)
        if record:
            result = upsert_record(data["metals"][symbol], record)
            changed = changed or result in {"added", "updated"}
            print(f"  ✓ {symbol}: {record['close']} ({result})")

    # Update ETFs
    for symbol in etf_symbols:
        record = fetch_latest(symbol)
        if record:
            result = upsert_record(data["etfs"][symbol], record)
            changed = changed or result in {"added", "updated"}
            print(f"  ✓ {symbol}: {record['close']} ({result})")

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
