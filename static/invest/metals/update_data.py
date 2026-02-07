#!/usr/bin/env python3
"""
Daily update script for Metals module.
Fetches latest prices and appends to historical.json.
Designed to be run by GitHub Actions daily.
"""

import json
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
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def fetch_latest(symbol):
    """Fetch the most recent trading day's close."""
    try:
        ticker = yf.Ticker(symbol)
        df = ticker.history(period="5d", interval="1d")
        if df.empty:
            return None
        last = df.iloc[-1]
        return {
            "date": last.name.strftime("%Y-%m-%d"),
            "close": round(float(last["Close"]), 4),
            "volume": int(last["Volume"]) if "Volume" in last else 0,
        }
    except Exception as e:
        print(f"  ✗ {symbol}: {e}")
        return None


def upsert_record(history_list, record):
    """Insert or update a record by date."""
    for i, existing in enumerate(history_list):
        if existing["date"] == record["date"]:
            history_list[i] = record
            return "updated"
    history_list.append(record)
    history_list.sort(key=lambda x: x["date"])
    return "added"


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DATA_PATH
    print(f"Loading data from {path}")
    data = load_data(path)

    today = datetime.now().strftime("%Y-%m-%d")
    print(f"Fetching latest data ({today})\n")

    metals_symbols = list(data["metadata"]["metals"].keys())
    etf_symbols = list(data["metadata"]["etfs"].keys())

    # Update metals
    for symbol in metals_symbols:
        record = fetch_latest(symbol)
        if record:
            result = upsert_record(data["metals"][symbol], record)
            print(f"  ✓ {symbol}: {record['close']} ({result})")

    # Update ETFs
    for symbol in etf_symbols:
        record = fetch_latest(symbol)
        if record:
            result = upsert_record(data["etfs"][symbol], record)
            print(f"  ✓ {symbol}: {record['close']} ({result})")

    # Rebuild current prices
    current = {}
    all_data = {**data["metals"], **data["etfs"]}
    for symbol, history in all_data.items():
        if len(history) >= 2:
            latest = history[-1]
            prev = history[-2]
            change = latest["close"] - prev["close"]
            pct = (change / prev["close"] * 100) if prev["close"] else 0
            current[symbol] = {
                "price": latest["close"],
                "change": round(change, 4),
                "changePct": round(pct, 2),
                "date": latest["date"],
            }

    data["current"] = current
    data["metadata"]["last_updated"] = datetime.now().isoformat()

    save_data(path, data)
    print(f"\n✅ Updated! Saved to {path}")


if __name__ == "__main__":
    main()
