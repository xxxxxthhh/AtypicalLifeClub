#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
# ─── How to run ───
# python3 static/invest/research/generate_calibration_note.py
# python3 static/invest/research/generate_calibration_note.py > /tmp/calibration-2026-07-31.md
#
# Manual only — never wire this into the cron. It emits the DATA APPENDIX for the
# quarterly calibration note (v5 §4.3, v6 spec §3.3): stance distribution, best and
# worst relative call per benchmark bucket, the full breached-without-flip list, the
# neutral share, and every benchmark override with its rationale verbatim (spec §8).
#
# It never writes conclusions or recommendations. The human author writes the
# conclusions section on top of this output; the generator's job is to make the
# numbers non-negotiable, not to interpret them.
#
# Output is deterministic: it is dated from verdicts.json `generatedAt` (never
# date.today()), and every list is explicitly sorted. Re-running against unchanged
# inputs produces byte-identical markdown.

from __future__ import annotations

import json
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Final, Optional, Union

Json = Union[None, bool, int, float, str, list["Json"], dict[str, "Json"]]

ROOT: Final = Path(__file__).resolve().parent
REPORTS_JSON: Final = ROOT / "data" / "reports.json"
VERDICTS_JSON: Final = ROOT / "data" / "verdicts.json"
BENCHMARKS_JSON: Final = ROOT / "data" / "benchmarks.json"

BOOK_BENCHMARK: Final = "SMH"
NEUTRAL_STANCE: Final = "neutral-watch"
STANCE_ORDER: Final = ("bullish", "constructive", NEUTRAL_STANCE, "cautious", "bearish-avoid")
CONVICTION_ORDER: Final = ("high", "medium", "low")


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def load_json(path: Path) -> Json:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing file: {path}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path}: {exc}")
    return None


def load_reports() -> list[dict]:
    data = load_json(REPORTS_JSON)
    if not isinstance(data, list):
        fail("reports.json must be an array")
    for index, item in enumerate(data):
        if not isinstance(item, dict):
            fail(f"reports.json[{index}] must be an object")
    return data


def load_verdicts() -> dict:
    data = load_json(VERDICTS_JSON)
    if not isinstance(data, dict):
        fail("verdicts.json must be an object")
    generated_at = data.get("generatedAt")
    if not isinstance(generated_at, str) or not generated_at.strip():
        fail("verdicts.json is missing generatedAt — the appendix must be dated from it")
    try:
        datetime.strptime(generated_at, "%Y-%m-%d")
    except ValueError:
        fail(f"verdicts.json generatedAt is not YYYY-MM-DD: {generated_at}")
    return data


def load_benchmarks() -> dict:
    data = load_json(BENCHMARKS_JSON)
    if not isinstance(data, dict):
        fail("benchmarks.json must be an object")
    return data


def is_current_chain_report(report: dict) -> bool:
    return bool(report.get("chainLayer")) and report.get("isCurrent") is not False


def parse_day(value: object) -> Optional[date]:
    if not isinstance(value, str):
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None


def bucket_sort_key(symbol: str) -> tuple:
    # The book default leads; everything else is alphabetical so reruns are stable.
    return (0 if symbol == BOOK_BENCHMARK else 1, symbol)


def scored_calls(verdicts: dict) -> list[dict]:
    """Open scored entries plus non-migration closed intervals, each with its own bucket."""
    calls: list[dict] = []
    for entry in verdicts.get("entries") or []:
        if not isinstance(entry, dict) or not isinstance(entry.get("relativePct"), (int, float)):
            continue
        calls.append({
            "reportId": entry.get("reportId"),
            "stance": entry.get("stance"),
            "relativePct": float(entry["relativePct"]),
            "benchmarkSymbol": entry.get("benchmarkSymbol") or "—",
            "window": "open",
        })
    for entry in verdicts.get("closed") or []:
        if not isinstance(entry, dict) or entry.get("migration"):
            continue
        if not isinstance(entry.get("relativePct"), (int, float)):
            continue
        calls.append({
            "reportId": entry.get("reportId"),
            "stance": entry.get("fromStance"),
            "relativePct": float(entry["relativePct"]),
            "benchmarkSymbol": entry.get("benchmarkSymbol") or "—",
            "window": f"{entry.get('startDate')}→{entry.get('endDate')}",
        })
    calls.sort(key=lambda call: (str(call["reportId"]), str(call["window"])))
    return calls


def linked_monitoring_ids(report: dict) -> set:
    ids = set()
    triggers = report.get("stanceTriggers")
    if not isinstance(triggers, dict):
        return ids
    for side in ("upgrade", "downgrade"):
        value = triggers.get(side)
        if isinstance(value, dict) and isinstance(value.get("monitoringIds"), list):
            ids.update(value["monitoringIds"])
    return ids


def current_stance_date(report: dict) -> Optional[str]:
    history = report.get("stanceHistory")
    if not isinstance(history, list) or not history:
        return None
    last = history[-1]
    return last.get("date") if isinstance(last, dict) else None


def breached_without_flip(reports: list[dict], as_of: date) -> list[dict]:
    """Mirror of buildTriggerWatchRows() in tracking-rules.js (v6 spec §3.3).

    A linked monitoring item reads "breached" and the stance has not moved since
    that grade. A stance dated exactly on readingAsOf still counts as unchanged.
    """
    rows: list[dict] = []
    for report in reports:
        if not is_current_chain_report(report):
            continue
        linked = linked_monitoring_ids(report)
        if not linked:
            continue
        stance_date = current_stance_date(report)
        breached = []
        for item in report.get("monitoring") or []:
            if not isinstance(item, dict) or item.get("reading") != "breached":
                continue
            if item.get("id") not in linked:
                continue
            graded_on = parse_day(item.get("readingAsOf"))
            if graded_on is None:
                continue
            if stance_date is not None and stance_date > item["readingAsOf"]:
                continue
            breached.append((item["readingAsOf"], item))
        if not breached:
            continue
        breached.sort(key=lambda pair: (pair[0], pair[1].get("id") or ""))
        oldest_date, oldest_item = breached[0]
        rows.append({
            "reportId": report.get("id"),
            "stance": report.get("stance"),
            "conviction": report.get("conviction"),
            "stanceDate": stance_date,
            "readingAsOf": oldest_date,
            "daysSinceBreach": max(0, (as_of - parse_day(oldest_date)).days),
            "metrics": [item.get("id") for _, item in breached],
        })
    rows.sort(key=lambda row: (-row["daysSinceBreach"], str(row["reportId"])))
    return rows


def benchmark_overrides(reports: list[dict]) -> list[dict]:
    overrides = []
    for report in reports:
        symbol = report.get("benchmarkSymbol")
        if not isinstance(symbol, str) or not symbol:
            continue
        rationale = report.get("benchmarkRationale") or {}
        overrides.append({
            "reportId": report.get("id"),
            "chainLayer": report.get("chainLayer"),
            "benchmarkSymbol": symbol,
            "rationaleEn": rationale.get("en", ""),
            "rationaleZh": rationale.get("zh", ""),
        })
    overrides.sort(key=lambda row: str(row["reportId"]))
    return overrides


def call_label(call: dict) -> str:
    # A report can hold both the best and the worst call in a bucket across different
    # windows, so the window is part of the identity, not decoration.
    return f"{call['reportId']} ({call['stance']}, {call['window']})"


def signed_pct(value: float) -> str:
    return f"{'+' if value > 0 else ''}{value:.1f}%"


def cell(value: object) -> str:
    text = "—" if value is None else str(value)
    return text.replace("|", "\\|")


def render(reports: list[dict], verdicts: dict, benchmarks: dict) -> str:
    generated_at = verdicts["generatedAt"]
    as_of = parse_day(generated_at)
    chain = sorted(
        (r for r in reports if is_current_chain_report(r)),
        key=lambda r: str(r.get("id")),
    )
    lines: list[str] = []
    lines.append(f"# Quarterly calibration note — data appendix ({generated_at})")
    lines.append("")
    lines.append(
        "Generated by `generate_calibration_note.py` from `reports.json`, `verdicts.json` "
        "and `benchmarks.json`. Data only — the conclusions section is written by hand on "
        "top of this appendix (v5 §4.3)."
    )
    lines.append("")

    # ─── 1. stance distribution ───
    lines.append("## 1. Stance distribution")
    lines.append("")
    lines.append(f"Current-chain reports: {len(chain)}.")
    lines.append("")
    lines.append("| Stance | Total | " + " | ".join(f"{c} conviction" for c in CONVICTION_ORDER) + " |")
    lines.append("|---|---:|" + "---:|" * len(CONVICTION_ORDER))
    unknown_stances = sorted({
        str(r.get("stance")) for r in chain if r.get("stance") not in STANCE_ORDER
    })
    for stance in STANCE_ORDER + tuple(unknown_stances):
        matching = [r for r in chain if r.get("stance") == stance]
        counts = [str(sum(1 for r in matching if r.get("conviction") == c)) for c in CONVICTION_ORDER]
        lines.append(f"| {cell(stance)} | {len(matching)} | " + " | ".join(counts) + " |")
    neutral = sum(1 for r in chain if r.get("stance") == NEUTRAL_STANCE)
    neutral_share = (neutral / len(chain) * 100) if chain else 0.0
    lines.append("")
    lines.append(f"Neutral share: {neutral}/{len(chain)} ({neutral_share:.1f}%).")
    lines.append("")

    # ─── 2. best / worst per benchmark bucket ───
    lines.append("## 2. Best and worst relative call per benchmark bucket")
    lines.append("")
    calls = scored_calls(verdicts)
    if not calls:
        lines.append("No scored calls yet.")
        lines.append("")
    else:
        buckets: dict = {}
        for call in calls:
            buckets.setdefault(call["benchmarkSymbol"], []).append(call)
        symbols = sorted(benchmarks.get("symbols") or {})
        lines.append(f"Benchmark symbols configured: {', '.join(symbols) if symbols else '—'}.")
        lines.append("")
        lines.append("| Bucket | Calls | Best | vs bench | Worst | vs bench |")
        lines.append("|---|---:|---|---:|---|---:|")
        for symbol in sorted(buckets, key=bucket_sort_key):
            group = buckets[symbol]
            best = max(group, key=lambda c: (c["relativePct"], str(c["reportId"])))
            worst = min(group, key=lambda c: (c["relativePct"], str(c["reportId"])))
            lines.append(
                f"| {cell(symbol)} | {len(group)} | {cell(call_label(best))} "
                f"| {signed_pct(best['relativePct'])} | {cell(call_label(worst))} "
                f"| {signed_pct(worst['relativePct'])} |"
            )
        lines.append("")

    # ─── 3. breached without a stance flip ───
    lines.append("## 3. Breached without a stance flip")
    lines.append("")
    lines.append(
        "Linked monitoring items graded `breached` whose report has not changed stance "
        "since the grade. Same selection as the ledger's Trigger Watch section."
    )
    lines.append("")
    rows = breached_without_flip(chain, as_of)
    if not rows:
        lines.append("None. (Empty is the healthy state, not a missing query.)")
        lines.append("")
    else:
        lines.append("| Report | Stance | Conviction | Breached items | Graded | Stance date | Days |")
        lines.append("|---|---|---|---|---|---|---:|")
        for row in rows:
            lines.append(
                f"| {cell(row['reportId'])} | {cell(row['stance'])} | {cell(row['conviction'])} "
                f"| {cell(', '.join(row['metrics']))} | {cell(row['readingAsOf'])} "
                f"| {cell(row['stanceDate'])} | {row['daysSinceBreach']} |"
            )
        lines.append("")

    # ─── 4. reading coverage ───
    lines.append("## 4. Reading coverage")
    lines.append("")
    lines.append("| Grade | Items |")
    lines.append("|---|---:|")
    total_items = 0
    tally = {"within": 0, "breached": 0, "unclear": 0, "ungraded": 0}
    for report in chain:
        for item in report.get("monitoring") or []:
            if not isinstance(item, dict):
                continue
            total_items += 1
            tally[item.get("reading") or "ungraded"] = tally.get(item.get("reading") or "ungraded", 0) + 1
    for grade in ("within", "breached", "unclear", "ungraded"):
        lines.append(f"| {grade} | {tally.get(grade, 0)} |")
    lines.append(f"| **total** | {total_items} |")
    lines.append("")

    # ─── 5. benchmark overrides (spec §8 audit trail) ───
    lines.append("## 5. Benchmark overrides")
    lines.append("")
    lines.append("Every per-report override with its `benchmarkRationale` verbatim (spec §8).")
    lines.append("")
    overrides = benchmark_overrides(reports)
    if not overrides:
        lines.append("None.")
        lines.append("")
    else:
        lines.append("| Report | Layer | Benchmark | Rationale (en) | Rationale (zh) |")
        lines.append("|---|---|---|---|---|")
        for row in overrides:
            lines.append(
                f"| {cell(row['reportId'])} | {cell(row['chainLayer'])} "
                f"| {cell(row['benchmarkSymbol'])} | {cell(row['rationaleEn'])} "
                f"| {cell(row['rationaleZh'])} |"
            )
        lines.append("")

    return "\n".join(lines) + "\n"


def main() -> None:
    sys.stdout.write(render(load_reports(), load_verdicts(), load_benchmarks()))


if __name__ == "__main__":
    main()
