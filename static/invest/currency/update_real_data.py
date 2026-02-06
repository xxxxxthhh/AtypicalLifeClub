#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fetch the latest FX rates and upsert a daily snapshot into historical.json.
Uses the same source family as historical bootstrap script (fawazahmed0 API).
"""

import json
import urllib.request
from datetime import datetime
from pathlib import Path

API_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json"
ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "historical.json"
CURRENCIES = ["CNY", "SGD", "JPY", "AUD"]
BASE_CURRENCY = "USD"


def fetch_current_rates():
    """Fetch latest rates from source API."""
    try:
        with urllib.request.urlopen(API_URL, timeout=10) as response:
            payload = json.loads(response.read().decode("utf-8"))

        usd_rates = payload.get("usd", {})
        filtered = {}
        for curr in CURRENCIES:
            key = curr.lower()
            if key in usd_rates:
                filtered[curr] = usd_rates[key]

        if len(filtered) != len(CURRENCIES):
            missing = [c for c in CURRENCIES if c not in filtered]
            raise ValueError(f"missing currencies in API response: {missing}")

        rate_date = payload.get("date", datetime.now().strftime("%Y-%m-%d"))

        return {
            "date": rate_date,
            "base": BASE_CURRENCY,
            "rates": filtered
        }
    except Exception as exc:
        print(f"获取汇率失败: {exc}")
        return None


def load_historical_data():
    """Load existing historical dataset."""
    if not DATA_FILE.exists():
        return None

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as exc:
        print(f"加载历史数据失败: {exc}")
        return None


def save_data(data):
    """Persist dataset."""
    try:
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        return True
    except Exception as exc:
        print(f"保存数据失败: {exc}")
        return False


def upsert_by_date(historical, daily_record):
    """Insert or replace by date while keeping ascending date order."""
    target_date = daily_record["date"]
    updated = False
    for idx, row in enumerate(historical):
        if row.get("date") == target_date:
            historical[idx] = daily_record
            updated = True
            break

    if not updated:
        historical.append(daily_record)

    historical.sort(key=lambda row: row.get("date", ""))


def build_metadata(historical):
    """Build canonical metadata (with compatibility alias)."""
    start_date = historical[0]["date"] if historical else None
    end_date = historical[-1]["date"] if historical else None
    now = datetime.now().isoformat()

    return {
        "base_currency": BASE_CURRENCY,
        "base": BASE_CURRENCY,
        "currencies": CURRENCIES,
        "total_days": len(historical),
        "start_date": start_date,
        "end_date": end_date,
        "last_updated": now
    }


def main():
    print("=" * 50)
    print("更新真实汇率数据")
    print("=" * 50)

    current = fetch_current_rates()
    if not current:
        print("❌ 获取失败")
        return

    print(f"✅ 获取成功: {current['date']}")
    for curr, rate in current["rates"].items():
        print(f"  USD/{curr}: {rate}")

    data = load_historical_data()
    if data is None:
        print("📝 创建新数据文件...")
        historical = [current]
    else:
        historical = data.get("historical", [])
        print(f"✅ 已有 {len(historical)} 天数据")
        upsert_by_date(historical, current)

    output = {
        "metadata": build_metadata(historical),
        "current": current,
        "historical": historical
    }

    print("\n保存数据...")
    if save_data(output):
        print(f"✅ 成功！总共 {len(historical)} 天数据")
    else:
        print("❌ 保存失败")


if __name__ == "__main__":
    main()
