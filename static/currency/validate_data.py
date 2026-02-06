#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validate currency data file shape and basic integrity constraints.
"""

import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "historical.json"
EXPECTED_CURRENCIES = ["CNY", "SGD", "JPY", "AUD"]


def fail(message):
    print(f"❌ 校验失败: {message}")
    sys.exit(1)


def parse_date(value, field_name):
    try:
        return datetime.strptime(value, "%Y-%m-%d")
    except Exception:
        fail(f"{field_name} 不是 YYYY-MM-DD: {value}")


def assert_numeric(value, field_name):
    if not isinstance(value, (int, float)):
        fail(f"{field_name} 不是数字: {value}")
    if value <= 0:
        fail(f"{field_name} 必须大于 0: {value}")


def main():
    if not DATA_FILE.exists():
        fail(f"找不到数据文件: {DATA_FILE}")

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    for key in ("metadata", "current", "historical"):
        if key not in data:
            fail(f"缺少顶层字段: {key}")

    metadata = data["metadata"]
    historical = data["historical"]
    current = data["current"]

    if not isinstance(historical, list) or not historical:
        fail("historical 必须是非空数组")

    currencies = metadata.get("currencies")
    if currencies != EXPECTED_CURRENCIES:
        fail(f"metadata.currencies 不匹配: {currencies}")

    base_currency = metadata.get("base_currency") or metadata.get("base")
    if base_currency != "USD":
        fail(f"metadata.base_currency/base 必须是 USD: {base_currency}")

    seen_dates = set()
    ordered_dates = []
    for idx, row in enumerate(historical):
        if "date" not in row or "rates" not in row:
            fail(f"historical[{idx}] 缺少 date 或 rates")

        date_value = row["date"]
        parse_date(date_value, f"historical[{idx}].date")

        if date_value in seen_dates:
            fail(f"historical 日期重复: {date_value}")
        seen_dates.add(date_value)
        ordered_dates.append(date_value)

        rates = row["rates"]
        if not isinstance(rates, dict):
            fail(f"historical[{idx}].rates 不是对象")

        for curr in EXPECTED_CURRENCIES:
            if curr not in rates:
                fail(f"historical[{idx}].rates 缺少货币: {curr}")
            assert_numeric(rates[curr], f"historical[{idx}].rates.{curr}")

    if ordered_dates != sorted(ordered_dates):
        fail("historical 日期不是升序")

    start_date = metadata.get("start_date")
    end_date = metadata.get("end_date")
    total_days = metadata.get("total_days")

    if start_date != ordered_dates[0]:
        fail(f"metadata.start_date 不匹配: {start_date} != {ordered_dates[0]}")
    if end_date != ordered_dates[-1]:
        fail(f"metadata.end_date 不匹配: {end_date} != {ordered_dates[-1]}")
    if total_days != len(historical):
        fail(f"metadata.total_days 不匹配: {total_days} != {len(historical)}")

    if "date" not in current or "rates" not in current:
        fail("current 缺少 date 或 rates")
    parse_date(current["date"], "current.date")
    for curr in EXPECTED_CURRENCIES:
        if curr not in current["rates"]:
            fail(f"current.rates 缺少货币: {curr}")
        assert_numeric(current["rates"][curr], f"current.rates.{curr}")

    if "last_updated" not in metadata:
        fail("metadata 缺少 last_updated")

    print("✅ 数据校验通过")


if __name__ == "__main__":
    main()
