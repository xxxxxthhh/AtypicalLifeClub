#!/usr/bin/env python3
"""
Fetch historical metals & ETF data using Yahoo Finance public API.
No external dependencies - uses only Python stdlib.
"""

import json
import urllib.request
import time
import sys
import os
from datetime import datetime, timedelta

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

METALS = {
    "GC=F":  {"name": "Gold",      "unit": "USD/oz"},
    "SI=F":  {"name": "Silver",    "unit": "USD/oz"},
    "PL=F":  {"name": "Platinum",  "unit": "USD/oz"},
    "PA=F":  {"name": "Palladium", "unit": "USD/oz"},
    "HG=F":  {"name": "Copper",    "unit": "USD/lb"},
}

ETFS = {
    "COPX": {"name": "Global X Copper Miners ETF",        "category": "copper"},
    "GLD":  {"name": "SPDR Gold Shares",                  "category": "gold"},
    "SLV":  {"name": "iShares Silver Trust",              "category": "silver"},
    "CPER": {"name": "US Copper Index Fund",              "category": "copper"},
    "DBB":  {"name": "Invesco DB Base Metals Fund",       "category": "base_metals"},
    "REMX": {"name": "VanEck Rare Earth/Strategic Metals", "category": "rare_earth"},
    "LIT":  {"name": "Global X Lithium & Battery Tech",   "category": "lithium"},
    "PPLT": {"name": "abrdn Physical Platinum Shares",    "category": "platinum"},
    "PALL": {"name": "abrdn Physical Palladium Shares",   "category": "palladium"},
}

LOOKBACK_DAYS = 730
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"


def fetch_yahoo_history(symbol, days):
    """Fetch daily close prices from Yahoo Finance chart API."""
    end_ts = int(time.time())
    start_ts = end_ts - (days * 86400)
    url = (
        f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
        f"?period1={start_ts}&period2={end_ts}&interval=1d"
    )
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())

        result = data["chart"]["result"][0]
        timestamps = result["timestamp"]
        closes = result["indicators"]["quote"][0]["close"]
        volumes = result["indicators"]["quote"][0].get("volume", [0] * len(timestamps))

        records = []
        for ts, close, vol in zip(timestamps, closes, volumes):
            if close is None:
                continue
            dt = datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d")
            records.append({
                "date": dt,
                "close": round(float(close), 4),
                "volume": int(vol) if vol else 0,
            })
        print(f"  ✓ {symbol}: {len(records)} days")
        return records
    except Exception as e:
        print(f"  ✗ {symbol}: {e}")
        return []


def build_current(metals_data, etfs_data):
    """Build current prices from latest data points."""
    current = {}
    for symbol, history in {**metals_data, **etfs_data}.items():
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
    return current


def main():
    output_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(SCRIPT_DIR, "data", "historical.json")
    print(f"Building historical data → {output_path}\n")

    print("=== Fetching Metals Spot Data ===")
    metals_data = {}
    for symbol in METALS:
        metals_data[symbol] = fetch_yahoo_history(symbol, LOOKBACK_DAYS)
        time.sleep(0.5)

    print("\n=== Fetching ETF Data ===")
    etfs_data = {}
    for symbol in ETFS:
        etfs_data[symbol] = fetch_yahoo_history(symbol, LOOKBACK_DAYS)
        time.sleep(0.5)

    current = build_current(metals_data, etfs_data)

    result = {
        "metadata": {
            "metals": METALS,
            "etfs": ETFS,
            "lookback_days": LOOKBACK_DAYS,
            "last_updated": datetime.now().isoformat(),
            "total_metals": len(METALS),
            "total_etfs": len(ETFS),
        },
        "current": current,
        "metals": metals_data,
        "etfs": etfs_data,
    }

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    total = sum(len(v) for v in metals_data.values()) + sum(len(v) for v in etfs_data.values())
    print(f"\n✅ Done! Saved to {output_path}")
    print(f"   Total data points: {total}")


if __name__ == "__main__":
    main()
