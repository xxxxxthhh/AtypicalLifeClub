#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validate metals data file shape and basic integrity constraints.
"""

import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "historical.json"

EXPECTED_METALS = ["GC=F", "SI=F", "PL=F", "PA=F", "HG=F"]
EXPECTED_ETFS = ["COPX", "GLD", "SLV", "CPER", "DBB", "REMX", "LIT", "PPLT", "PALL"]


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


def validate_history(data, section, symbols, label):
    """Validate a history section (metals or etfs)."""
    if section not in data:
        fail(f"缺少顶层字段: {section}")

    section_data = data[section]
    for symbol in symbols:
        if symbol not in section_data:
            fail(f"{label} 缺少品种: {symbol}")

        history = section_data[symbol]
        if not isinstance(history, list) or not history:
            fail(f"{label}.{symbol} 必须是非空数组")

        seen_dates = set()
        ordered_dates = []
        for idx, row in enumerate(history):
            if "date" not in row or "close" not in row:
                fail(f"{label}.{symbol}[{idx}] 缺少 date 或 close")

            date_value = row["date"]
            parse_date(date_value, f"{label}.{symbol}[{idx}].date")

            if date_value in seen_dates:
                fail(f"{label}.{symbol} 日期重复: {date_value}")
            seen_dates.add(date_value)
            ordered_dates.append(date_value)

            assert_numeric(row["close"], f"{label}.{symbol}[{idx}].close")

        if ordered_dates != sorted(ordered_dates):
            fail(f"{label}.{symbol} 日期不是升序")

    print(f"  ✓ {label}: {len(symbols)} 个品种校验通过")


def main():
    if not DATA_FILE.exists():
        fail(f"找不到数据文件: {DATA_FILE}")

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Check top-level fields
    for key in ("metadata", "current", "metals", "etfs"):
        if key not in data:
            fail(f"缺少顶层字段: {key}")

    metadata = data["metadata"]

    # Validate metadata
    if "metals" not in metadata or "etfs" not in metadata:
        fail("metadata 缺少 metals 或 etfs")

    for symbol in EXPECTED_METALS:
        if symbol not in metadata["metals"]:
            fail(f"metadata.metals 缺少: {symbol}")

    for symbol in EXPECTED_ETFS:
        if symbol not in metadata["etfs"]:
            fail(f"metadata.etfs 缺少: {symbol}")

    if "last_updated" not in metadata:
        fail("metadata 缺少 last_updated")

    print("  ✓ metadata 校验通过")

    # Validate history sections
    validate_history(data, "metals", EXPECTED_METALS, "metals")
    validate_history(data, "etfs", EXPECTED_ETFS, "etfs")

    # Validate current prices
    current = data["current"]
    all_symbols = EXPECTED_METALS + EXPECTED_ETFS
    for symbol in all_symbols:
        if symbol not in current:
            fail(f"current 缺少品种: {symbol}")
        entry = current[symbol]
        if "price" not in entry or "date" not in entry:
            fail(f"current.{symbol} 缺少 price 或 date")
        assert_numeric(entry["price"], f"current.{symbol}.price")
        parse_date(entry["date"], f"current.{symbol}.date")

    print(f"  ✓ current: {len(all_symbols)} 个品种价格校验通过")

    print("\n✅ Metals 数据校验通过")


if __name__ == "__main__":
    main()
