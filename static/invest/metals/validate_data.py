#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validate metals data file shape and basic integrity constraints.
"""

import json
import math
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "historical.json"

EXPECTED_METALS = ["GC=F", "SI=F", "PL=F", "PA=F", "HG=F"]
EXPECTED_ETFS = ["COPX", "GLD", "SLV", "CPER", "DBB", "REMX", "LIT", "PPLT", "PALL"]

# A single-day move larger than this is treated as an unadjusted corporate
# action (or a corrupt row) rather than a market move. See
# docs/daily-briefing-plan.md section 3.3 — the 2026-05-18 PPLT/PALL splits
# passed every existing check while poisoning every volatility calculation that
# crossed them.
#
# Threshold chosen from the data, not from intuition. Over 9,082 consecutive
# pairs (2024-02 .. 2026-08) the largest genuine move is SI=F -31.35% on
# 2026-01-30, independently corroborated by SLV -28.54%, PL=F -19.04% and
# PPLT -18.44% the same day (a real precious-metals selloff, not a split). The
# smallest ordinary forward split, 2:1, is -50%. 0.35 sits between the two with
# margin on both sides and fires on zero rows of the current, corrected file.
#
# Known gap: a small split such as 3:2 (-33%) falls under this threshold. That
# is deliberate — the primary defence is update_data.apply_new_splits(), which
# reads the split feed directly and is size-agnostic. This check is the net for
# when that layer fails silently, so it targets the splits big enough to wreck a
# volatility series. Do NOT lower it to catch small splits by widening the
# knownSplits whitelist; a whitelist that grows with market volatility becomes a
# mute switch (see section 9 of the plan).
MAX_DAILY_MOVE = 0.35


def fail(message):
    print(f"❌ 校验失败: {message}")
    sys.exit(1)


def parse_date(value, field_name):
    try:
        return datetime.strptime(value, "%Y-%m-%d")
    except Exception:
        fail(f"{field_name} 不是 YYYY-MM-DD: {value}")


def assert_numeric(value, field_name):
    if not isinstance(value, (int, float)) or not math.isfinite(value):
        fail(f"{field_name} 不是数字: {value}")


def parse_known_splits(metadata):
    """Return {(symbol, date): ratio} from metadata.knownSplits, failing on bad entries."""
    entries = metadata.get("knownSplits", [])
    if not isinstance(entries, list):
        fail("metadata.knownSplits 必须是数组")

    known = {}
    for idx, entry in enumerate(entries):
        where = f"metadata.knownSplits[{idx}]"
        if not isinstance(entry, dict):
            fail(f"{where} 必须是对象")

        for field in ("symbol", "date", "ratio", "reason"):
            if field not in entry:
                fail(f"{where} 缺少 {field}")

        # strptime accepts "2026-5-18", but row dates are always zero-padded, so a
        # non-canonical entry would look declared while never matching anything.
        parsed = parse_date(entry["date"], f"{where}.date")
        if parsed.strftime("%Y-%m-%d") != entry["date"]:
            fail(f"{where}.date 必须是零补齐的 YYYY-MM-DD: {entry['date']}")

        assert_numeric(entry["ratio"], f"{where}.ratio")
        if entry["ratio"] <= 0:
            fail(f"{where}.ratio 必须为正数: {entry['ratio']}")
        if not str(entry.get("reason", "")).strip():
            fail(f"{where}.reason 不能为空——白名单条目必须写明已核实的公司行为")

        known[(entry["symbol"], entry["date"])] = entry["ratio"]

    return known


def validate_continuity(history, symbol, known_splits, label):
    """Fail on any single-day move larger than MAX_DAILY_MOVE that no declared
    split explains at the declared magnitude."""
    for prev, row in zip(history, history[1:]):
        previous_close = prev["close"]
        if previous_close == 0:
            continue

        move = row["close"] / previous_close - 1
        if abs(move) <= MAX_DAILY_MOVE:
            continue

        ratio = known_splits.get((symbol, row["date"]))
        if ratio is not None:
            # A whitelist entry names *which* corporate action happened, and its
            # ratio fixes exactly how large the resulting jump must be. So divide
            # the declared ratio back out: what remains has to be an ordinary
            # trading day. The three reachable states, for a declared 10:1:
            #
            #   already back-adjusted  move ≈ that day's real move (-0.35% for
            #                          PPLT 2026-05-18) — never reaches here at
            #                          all, so the entry sits inert as an audit
            #                          record, which is the file's normal state
            #   not yet back-adjusted  move ≈ 1/ratio - 1 = -90.04%, and the
            #                          residual collapses back to -0.35%
            #   adjusted a second time move ≈ ratio - 1 = +896.48%, residual
            #                          ≈ ratio² - 1 ≈ +9865%. Not ordinary.
            #
            # Testing the residual rather than mere (symbol, date) membership is
            # the entire point of this branch. Membership alone let exactly the
            # pollution this whitelist exists to document slip through: drop
            # metadata.lastSplitApplied, let the updater re-divide PPLT
            # 2026-05-15 a second time (17.903 → 1.7903), and the +896.48% jump
            # was waved past because the entry said "a jump belongs here" while
            # saying nothing about how big. A whitelist that declares a date but
            # not a magnitude is a mute switch with extra steps.
            #
            # Reusing MAX_DAILY_MOVE as the residual bound introduces no new
            # constant: once the declared split is removed, the day is held to
            # precisely the standard every other day is held to. Float and
            # rounding noise are irrelevant at this scale — closes carry 4
            # decimals, so the residual error is at most ~1e-5 relative, four
            # orders of magnitude inside a 0.35 bound. No epsilon fudge needed.
            residual = row["close"] * ratio / previous_close - 1
            if abs(residual) <= MAX_DAILY_MOVE:
                continue

            fail(
                f"{label}.{symbol} {prev['date']} → {row['date']} 单日变动 {move * 100:.1f}%，"
                f"与 metadata.knownSplits 声明的 {ratio:g}:1 对不上："
                f"按该比例还原后仍有 {residual * 100:.1f}%（阈值 ±{MAX_DAILY_MOVE * 100:.0f}%）。"
                f"已回改的历史这一天根本不该有跳变，未回改的应恰好是 {(1 / ratio - 1) * 100:.1f}%；"
                f"两者都不是，最常见的成因是历史被重复复权。"
                f"白名单声明的是幅度，不是豁免——不要靠它消音。"
            )

        fail(
            f"{label}.{symbol} {prev['date']} → {row['date']} 单日变动 {move * 100:.1f}%"
            f"（阈值 ±{MAX_DAILY_MOVE * 100:.0f}%），且不在 metadata.knownSplits 白名单里。"
            f"若确为已核实的公司行为，请补一条含 symbol/date/ratio/reason 的白名单条目；"
            f"否则这是数据污染，不要靠白名单消音。"
        )


def validate_history(data, section, symbols, label, known_splits=None):
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

        validate_continuity(history, symbol, known_splits or {}, label)

    print(f"  ✓ {label}: {len(symbols)} 个品种校验通过（含单日跳变检查）")


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

    known_splits = parse_known_splits(metadata)

    print(f"  ✓ metadata 校验通过（knownSplits {len(known_splits)} 条）")

    # Validate history sections
    validate_history(data, "metals", EXPECTED_METALS, "metals", known_splits)
    validate_history(data, "etfs", EXPECTED_ETFS, "etfs", known_splits)

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
