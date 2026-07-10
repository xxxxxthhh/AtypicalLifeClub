#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validate static/invest/research/data/reports.json schema and file references.
"""
from __future__ import annotations

# noqa: SIZE_OK - legacy single-file publishing validator; split in dedicated cleanup.

import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPORTS_JSON = ROOT / "data" / "reports.json"
REQUIRED_FIELDS = [
    "id",
    "company",
    "ticker",
    "title",
    "titleEn",
    "summary",
    "tags",
    "category",
    "date",
    "lastUpdate",
    "file",
    "markdownFiles"
]
VERSION_TYPES = {"initial", "incremental", "full-cycle"}
COVERAGE_TIER_VALUES = {"seed", "lite", "full"}
PREVIOUS_REPORT_FIELDS = [
    "id",
    "label",
    "labelEn",
    "file",
    "date",
    "lastUpdate",
    "summary",
    "summaryEn",
]

# Phase 0 enrichment fields (docs/research-hub-enhancement-plan.md, Part A).
# v5 stance schema (docs/research-hub-v5-stance-conviction-plan.md, Track 1):
# the 5-value skew-shaped enum replaces the legacy 4-value set; legacy values stay
# tolerated (top-level while ENFORCE_STANCE_V2 is off, stanceHistory forever).
STANCE_V2_VALUES = {"bullish", "constructive", "neutral-watch", "cautious", "bearish-avoid"}
LEGACY_STANCE_VALUES = {"constructive", "neutral-watch", "high-risk-watch", "bearish-avoid"}
STANCE_VALUES = STANCE_V2_VALUES | LEGACY_STANCE_VALUES
CONVICTION_VALUES = {"high", "medium", "low"}
STANCE_TRIGGER_KEYS = {"upgrade", "downgrade"}
THESIS_VALUES = {"bull", "bear", "either"}
THEME_VALUES = {
    "concentration",
    "leverage-solvency",
    "demand",
    "circularity",
    "pricing",
    "optionality",
    "execution",
    "regulatory",
    "valuation",
}
MONITORING_ITEM_ID_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
NEXT_CHECK_DATE_RE = re.compile(r"\d{4}-(0[1-9]|1[0-2])")
PRICE_SYMBOL_RE = re.compile(r"[A-Z0-9.\-=]+")
ENGLISH_MARKDOWN_CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
REPORT_MODULE_CONTRACT = "heading-comment-v1"
REPORT_MODULE_IDS = {
    "overview",
    "business",
    "competition",
    "financial",
    "management",
    "bullBear",
    "uncertainties",
    "valuation",
    "catalysts",
    "conclusion",
    "appendix",
}
REPORT_MODULE_MARKER_RE = re.compile(
    r"^##\s+(.+?)\s+<!-- report-module:([A-Za-z][A-Za-z0-9-]*) -->\s*$"
)
BILINGUAL_KEYS = ("zh", "en")
MARKDOWN_URL_PREFIX = "/invest/research/"
# Chain requirement (spec A.7 step 3): stance/priceAsOf/reportedPeriod/monitoring[]
# are mandatory for current chainLayer reports. Enabled only after the backfill so
# the migration never leaves CI red; keep True once flipped.
ENFORCE_CHAIN_ENRICHMENT = True
ENFORCE_COVERAGE_TIER = True
# Stance v2 requirements (spec §2.3): warn-first during the report-by-report backfill,
# now enforced since all 35 current-chain reports pass; keep True once flipped. This
# also retires legacy top-level stance values for current-chain reports (history keeps
# them via the carve-out). Structural checks on the new fields stay hard regardless of
# the flag — only the presence/migration requirements are gated (same rollout pattern
# as ENFORCE_CHAIN_ENRICHMENT).
ENFORCE_STANCE_V2 = True
# v6 (docs/research-hub-v6-plan.md §2.1): benchmarks.json sits next to reports.json
# and drives per-layer benchmark resolution. validate_benchmarks_config() enforces
# the schema; the resolution mirror lives in update_verdicts.py / validate_verdicts.py.
BENCHMARKS_JSON = ROOT / "data" / "benchmarks.json"


def fail(message):
    print(f"FAIL: {message}")
    sys.exit(1)


def stance_v2_issue(message):
    if ENFORCE_STANCE_V2:
        fail(message)
    print(f"WARN: {message}")


def parse_date(value, field_name):
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except (TypeError, ValueError):
        fail(f"{field_name} is not YYYY-MM-DD: {value}")


def ensure_non_empty_string(value, field_name):
    if not isinstance(value, str) or not value.strip():
        fail(f"{field_name} must be a non-empty string")


def validate_report_reference(report_id, field_name, reports_by_id):
    ensure_non_empty_string(report_id, field_name)
    if report_id not in reports_by_id:
        fail(f"{field_name} references unknown report id: {report_id}")


def validate_previous_report(report, report_idx, reports_by_id):
    previous = report["previousAnnualReport"]
    field_prefix = f"report[{report_idx}].previousAnnualReport"
    if not isinstance(previous, dict):
        fail(f"{field_prefix} must be an object")

    for field in PREVIOUS_REPORT_FIELDS:
        if field not in previous:
            fail(f"{field_prefix} missing required field: {field}")
        ensure_non_empty_string(previous[field], f"{field_prefix}.{field}")

    parse_date(previous["date"], f"{field_prefix}.date")
    parse_date(previous["lastUpdate"], f"{field_prefix}.lastUpdate")

    previous_id = previous["id"]
    if previous_id == report["id"]:
        fail(f"{field_prefix}.id must not reference the current report")
    validate_report_reference(previous_id, f"{field_prefix}.id", reports_by_id)

    expected_file = f"/invest/research/reports/view.html?id={previous_id}"
    if previous["file"] != expected_file:
        fail(f"{field_prefix}.file should be {expected_file}, got: {previous['file']}")

    previous_report = reports_by_id[previous_id]
    if previous_report.get("isCurrent") is not False:
        fail(f"{field_prefix}.id must reference an archived report with isCurrent=false")


def validate_version_metadata(report, report_idx, reports_by_id):
    version_type = report.get("versionType")
    if version_type is not None:
        if version_type not in VERSION_TYPES:
            fail(
                f"report[{report_idx}].versionType must be one of "
                f"{sorted(VERSION_TYPES)}: {version_type}"
            )

    for field in ("period", "versionLabel"):
        if field in report:
            ensure_non_empty_string(report[field], f"report[{report_idx}].{field}")

    if "isCurrent" in report and not isinstance(report["isCurrent"], bool):
        fail(f"report[{report_idx}].isCurrent must be a boolean when present")

    for field in ("supersedes", "diffBase"):
        if field in report:
            validate_report_reference(report[field], f"report[{report_idx}].{field}", reports_by_id)
            if report[field] == report["id"]:
                fail(f"report[{report_idx}].{field} must not reference itself")

    has_previous = "previousAnnualReport" in report
    if has_previous:
        validate_previous_report(report, report_idx, reports_by_id)
        if version_type != "full-cycle":
            fail(
                f"report[{report_idx}].previousAnnualReport requires "
                "versionType=full-cycle"
            )

    if version_type == "full-cycle":
        for field in ("supersedes", "diffBase", "previousAnnualReport"):
            if field not in report:
                fail(f"report[{report_idx}] full-cycle report missing: {field}")
    elif version_type in {"initial", "incremental"}:
        for field in ("supersedes", "diffBase"):
            if field in report:
                fail(f"report[{report_idx}].{field} requires versionType=full-cycle")


def validate_bilingual_text(value, field_name):
    if not isinstance(value, dict):
        fail(f"{field_name} must be an object with zh and en")
    for lang in BILINGUAL_KEYS:
        ensure_non_empty_string(value.get(lang), f"{field_name}.{lang}")


def validate_monitoring(report, report_idx):
    monitoring = report["monitoring"]
    prefix = f"report[{report_idx}].monitoring"
    if not isinstance(monitoring, list) or not monitoring:
        fail(f"{prefix} must be a non-empty array")

    seen_ids = set()
    for item_idx, item in enumerate(monitoring):
        item_prefix = f"{prefix}[{item_idx}]"
        if not isinstance(item, dict):
            fail(f"{item_prefix} must be an object")

        item_id = item.get("id")
        ensure_non_empty_string(item_id, f"{item_prefix}.id")
        if not MONITORING_ITEM_ID_RE.fullmatch(item_id):
            fail(f"{item_prefix}.id should be kebab-case ([a-z0-9-]): {item_id}")
        if item_id in seen_ids:
            fail(f"{prefix} has duplicate item id: {item_id}")
        seen_ids.add(item_id)

        for field in ("metric", "trigger", "latest"):
            if field not in item:
                fail(f"{item_prefix} missing required field: {field}")
            validate_bilingual_text(item[field], f"{item_prefix}.{field}")

        thesis = item.get("thesis")
        if thesis not in THESIS_VALUES:
            fail(f"{item_prefix}.thesis must be one of {sorted(THESIS_VALUES)}: {thesis}")

        ensure_non_empty_string(item.get("nextCheck"), f"{item_prefix}.nextCheck")

        next_check_date = item.get("nextCheckDate")
        if next_check_date is not None:
            ensure_non_empty_string(next_check_date, f"{item_prefix}.nextCheckDate")
            if not NEXT_CHECK_DATE_RE.fullmatch(next_check_date):
                fail(f"{item_prefix}.nextCheckDate must be YYYY-MM: {next_check_date}")

        theme = item.get("theme")
        if theme is not None and theme not in THEME_VALUES:
            fail(f"{item_prefix}.theme must be one of {sorted(THEME_VALUES)}: {theme}")


def validate_stance_triggers(report, report_idx):
    triggers = report["stanceTriggers"]
    prefix = f"report[{report_idx}].stanceTriggers"
    if not isinstance(triggers, dict) or not triggers:
        fail(f"{prefix} must be a non-empty object")
    for key in triggers:
        if key not in STANCE_TRIGGER_KEYS:
            fail(f"{prefix} has unknown key (allowed: {sorted(STANCE_TRIGGER_KEYS)}): {key}")
    for key, value in triggers.items():
        validate_bilingual_text(value, f"{prefix}.{key}")


def validate_stance_history(report, report_idx):
    history = report["stanceHistory"]
    prefix = f"report[{report_idx}].stanceHistory"
    if not isinstance(history, list) or not history:
        fail(f"{prefix} must be a non-empty array")

    previous_date = None
    for entry_idx, entry in enumerate(history):
        entry_prefix = f"{prefix}[{entry_idx}]"
        if not isinstance(entry, dict):
            fail(f"{entry_prefix} must be an object")

        is_last = entry_idx == len(history) - 1
        # Legacy carve-out (spec §2.3): history is evidence and is never rewritten, so
        # non-last entries may keep legacy stance values and omit conviction.
        allowed_stances = STANCE_V2_VALUES if is_last else STANCE_VALUES
        stance = entry.get("stance")
        if stance not in allowed_stances:
            fail(
                f"{entry_prefix}.stance must be one of "
                f"{sorted(allowed_stances)}: {stance}"
            )

        conviction = entry.get("conviction")
        if is_last or conviction is not None:
            if conviction not in CONVICTION_VALUES:
                fail(
                    f"{entry_prefix}.conviction must be one of "
                    f"{sorted(CONVICTION_VALUES)}: {conviction}"
                )

        entry_date = entry.get("date")
        ensure_non_empty_string(entry_date, f"{entry_prefix}.date")
        parse_date(entry_date, f"{entry_prefix}.date")
        if previous_date is not None and entry_date < previous_date:
            fail(f"{prefix} dates must be ascending: {previous_date} -> {entry_date}")
        previous_date = entry_date

        price = entry.get("price")
        if isinstance(price, bool) or not isinstance(price, (int, float)) or price <= 0:
            fail(f"{entry_prefix}.price must be a positive number: {price}")

    last = history[-1]
    if "stance" in report and last.get("stance") != report["stance"]:
        fail(
            f"{prefix} last entry stance must match top-level stance: "
            f"{last.get('stance')} != {report['stance']}"
        )
    if "conviction" in report and last.get("conviction") != report["conviction"]:
        fail(
            f"{prefix} last entry conviction must match top-level conviction: "
            f"{last.get('conviction')} != {report['conviction']}"
        )


def validate_stance_v2_requirements(report, report_idx):
    """Warn-first stance v2 requirements for current-chain reports (spec §2.3).

    Archived (isCurrent=false) and non-chain reports are exempt; their old
    top-level stance values stay tolerated via STANCE_VALUES.
    """
    if not is_current_chain_report(report):
        return

    label = f"report[{report_idx}] ({report['id']})"
    stance = report.get("stance")
    if stance is not None and stance not in STANCE_V2_VALUES:
        stance_v2_issue(
            f"{label}.stance uses legacy value '{stance}'; migrate to one of "
            f"{sorted(STANCE_V2_VALUES)} (see docs/research-hub-v5-stance-conviction-plan.md §2.2)"
        )

    for field in ("conviction", "stanceRationale", "stanceHistory"):
        if field not in report:
            stance_v2_issue(f"{label} is a current chainLayer report and must carry {field}")

    triggers = report.get("stanceTriggers")
    if not isinstance(triggers, dict) or "downgrade" not in triggers:
        stance_v2_issue(f"{label} must carry stanceTriggers.downgrade (zh+en)")
    # Neutral tax (spec locked decision 3): neutral also names its upgrade trigger.
    if stance == "neutral-watch" and (not isinstance(triggers, dict) or "upgrade" not in triggers):
        stance_v2_issue(f"{label} stance=neutral-watch also requires stanceTriggers.upgrade (zh+en)")


def is_current_chain_report(report):
    return bool(report.get("chainLayer")) and report.get("isCurrent") is not False


def _resolved_benchmark_default(report, benchmarks_cfg):
    if not isinstance(benchmarks_cfg, dict):
        return None
    layer = report.get("chainLayer")
    if isinstance(layer, str):
        layer_defaults = benchmarks_cfg.get("layerDefaults")
        if isinstance(layer_defaults, dict):
            sym = layer_defaults.get(layer)
            if isinstance(sym, str) and sym:
                return sym
    default = benchmarks_cfg.get("default")
    return default if isinstance(default, str) else None


def validate_benchmarks_config(benchmarks_cfg):
    if not isinstance(benchmarks_cfg, dict):
        fail("benchmarks.json must be an object")
    default = benchmarks_cfg.get("default")
    ensure_non_empty_string(default, "benchmarks.json.default")
    layer_defaults = benchmarks_cfg.get("layerDefaults")
    if layer_defaults is not None:
        if not isinstance(layer_defaults, dict):
            fail("benchmarks.json.layerDefaults must be an object when present")
        for layer, sym in layer_defaults.items():
            if not isinstance(layer, str) or not layer:
                fail(f"benchmarks.json.layerDefaults has non-string key: {layer!r}")
            if not isinstance(sym, str) or not sym:
                fail(f"benchmarks.json.layerDefaults[{layer!r}] must be a non-empty string")
    symbols = benchmarks_cfg.get("symbols")
    if not isinstance(symbols, dict) or not symbols:
        fail("benchmarks.json.symbols must be a non-empty object")
    used = {default}
    if isinstance(layer_defaults, dict):
        used |= set(layer_defaults.values())
    for sym in used:
        if sym not in symbols:
            fail(f"benchmarks.json: symbol '{sym}' is used (default or layerDefault) but not defined in .symbols")
    for sym, meta in symbols.items():
        if not isinstance(sym, str) or not sym:
            fail(f"benchmarks.json.symbols has non-string key: {sym!r}")
        if not isinstance(meta, dict) or "name" not in meta:
            fail(f"benchmarks.json.symbols[{sym!r}] must have a 'name' object")
        name = meta["name"]
        if not isinstance(name, dict) or "zh" not in name or "en" not in name:
            fail(f"benchmarks.json.symbols[{sym!r}].name must have {{zh, en}}")
        for lang in ("zh", "en"):
            ensure_non_empty_string(name[lang], f"benchmarks.json.symbols[{sym!r}].name.{lang}")


def is_etf_report(report):
    return "ETF" in report.get("tags", [])


def resolve_markdown_file(markdown_url, field_name):
    ensure_non_empty_string(markdown_url, field_name)
    if not markdown_url.startswith(MARKDOWN_URL_PREFIX):
        fail(f"{field_name} should start with {MARKDOWN_URL_PREFIX}: {markdown_url}")
    if not markdown_url.endswith(".md"):
        fail(f"{field_name} should point to a .md file: {markdown_url}")

    markdown_rel = markdown_url.replace(MARKDOWN_URL_PREFIX, "", 1)
    markdown_file = (ROOT / markdown_rel).resolve()
    try:
        markdown_file.relative_to(ROOT)
    except ValueError:
        fail(f"{field_name} must stay under {ROOT}: {markdown_url}")
    return markdown_file


def markdown_has_table(markdown_url, field_name):
    markdown_file = resolve_markdown_file(markdown_url, field_name)
    if not markdown_file.exists():
        fail(f"{field_name} markdown file not found: {markdown_file}")
    with open(markdown_file, "r", encoding="utf-8") as file:
        return any(re.match(r"\s*\|.*\|", line) for line in file)


def validate_english_markdown(markdown_file, field_name):
    with open(markdown_file, "r", encoding="utf-8") as file:
        for line_no, line in enumerate(file, start=1):
            if not ENGLISH_MARKDOWN_CJK_RE.search(line):
                continue

            snippet = line.strip()
            if len(snippet) > 120:
                snippet = f"{snippet[:117]}..."
            fail(
                f"{field_name} contains CJK text at "
                f"{markdown_file.name}:{line_no}: {snippet}"
            )


def validate_module_contract(
    markdown_file: Path,
    module_contract: str | None,
    field_name: str,
) -> None:
    if module_contract is None:
        return
    if module_contract != REPORT_MODULE_CONTRACT:
        fail(
            f"{field_name} uses unsupported module contract: "
            f"{module_contract}"
        )

    with open(markdown_file, "r", encoding="utf-8") as file:
        for line_no, raw_line in enumerate(file, start=1):
            line = raw_line.rstrip("\n")
            heading_match = re.match(r"^(#{2,3})\s+", line)
            marker_count = line.count("report-module")
            location = f"{markdown_file.name}:{line_no}"

            if heading_match is None or heading_match.group(1) != "##":
                if marker_count:
                    fail(
                        f"{field_name} has malformed report-module marker at "
                        f"{location}: markers belong on H2 headings"
                    )
                continue
            if marker_count == 0:
                fail(
                    f"{field_name} has missing report-module marker at "
                    f"{location}"
                )
            if marker_count > 1:
                fail(
                    f"{field_name} has duplicate report-module markers at "
                    f"{location}"
                )

            marker_match = REPORT_MODULE_MARKER_RE.fullmatch(line)
            if marker_match is None:
                fail(
                    f"{field_name} has malformed report-module marker at "
                    f"{location}; expected <!-- report-module:<id> --> at "
                    "the end of the H2"
                )
            module_id = marker_match.group(2)
            if module_id not in REPORT_MODULE_IDS:
                fail(
                    f"{field_name} has unknown report module id "
                    f"'{module_id}' at {location}"
                )


def validate_coverage_tier(report, report_idx):
    coverage_tier = report.get("coverageTier")
    is_current_chain = is_current_chain_report(report)

    if coverage_tier is None:
        if ENFORCE_COVERAGE_TIER and is_current_chain:
            fail(
                f"report[{report_idx}] ({report['id']}) is a current chainLayer "
                "report and must carry coverageTier"
            )
        return

    if coverage_tier not in COVERAGE_TIER_VALUES:
        fail(
            f"report[{report_idx}].coverageTier must be one of "
            f"{sorted(COVERAGE_TIER_VALUES)}: {coverage_tier}"
        )

    version_type = report.get("versionType")
    is_etf = is_etf_report(report)
    if version_type == "full-cycle" and coverage_tier != "full" and not is_etf:
        fail(f"report[{report_idx}].coverageTier must be full for full-cycle reports")
    if coverage_tier in {"seed", "lite"} and version_type not in {"initial", "incremental"} and not is_etf:
        fail(
            f"report[{report_idx}].coverageTier={coverage_tier} is only valid "
            "for initial/incremental reports"
        )

    if not is_current_chain or coverage_tier not in {"lite", "full"} or is_etf:
        return

    markdown_files = report.get("markdownFiles", {})
    for lang in ("zh", "en"):
        markdown_url = markdown_files.get(lang)
        field_name = f"report[{report_idx}].markdownFiles.{lang}"
        if not markdown_has_table(markdown_url, field_name):
            fail(
                f"report[{report_idx}] ({report['id']}) coverageTier={coverage_tier} "
                f"requires at least one markdown table in {lang}"
            )


def validate_enrichment_fields(report, report_idx, reports_by_id, benchmarks_cfg):
    if "priceSymbol" in report:
        ensure_non_empty_string(report["priceSymbol"], f"report[{report_idx}].priceSymbol")
        if not PRICE_SYMBOL_RE.fullmatch(report["priceSymbol"]):
            fail(f"report[{report_idx}].priceSymbol is not Yahoo-compatible: {report['priceSymbol']}")

    if "stance" in report and report["stance"] not in STANCE_VALUES:
        fail(
            f"report[{report_idx}].stance must be one of "
            f"{sorted(STANCE_VALUES)}: {report['stance']}"
        )

    if "conviction" in report and report["conviction"] not in CONVICTION_VALUES:
        fail(
            f"report[{report_idx}].conviction must be one of "
            f"{sorted(CONVICTION_VALUES)}: {report['conviction']}"
        )

    if "stanceRationale" in report:
        validate_bilingual_text(report["stanceRationale"], f"report[{report_idx}].stanceRationale")

    if "stanceTriggers" in report:
        validate_stance_triggers(report, report_idx)

    if "stanceHistory" in report:
        validate_stance_history(report, report_idx)

    # Benchmark-only reports (e.g. smh-2026, spec §4.1a): schema-tolerated now,
    # consumed by the Track 3 price pipeline later.
    if "benchmark" in report and not isinstance(report["benchmark"], bool):
        fail(f"report[{report_idx}].benchmark must be a boolean when present")

    # v6 (docs/research-hub-v6-plan.md §2.1): per-report benchmark override. Only
    # meaningful on current-chain reports; when it differs from the layer/book
    # default it must carry a bilingual rationale (the audit trail against
    # benchmark shopping). Rationale without an override is an orphan.
    if "benchmarkSymbol" in report:
        ensure_non_empty_string(report["benchmarkSymbol"], f"report[{report_idx}].benchmarkSymbol")
        symbols = benchmarks_cfg.get("symbols") if isinstance(benchmarks_cfg, dict) else None
        if isinstance(symbols, dict) and report["benchmarkSymbol"] not in symbols:
            fail(
                f"report[{report_idx}].benchmarkSymbol '{report['benchmarkSymbol']}' "
                "is not defined in benchmarks.json.symbols"
            )
        if is_current_chain_report(report):
            resolved_default = _resolved_benchmark_default(report, benchmarks_cfg)
            if report["benchmarkSymbol"] != resolved_default:
                rationale = report.get("benchmarkRationale")
                if not isinstance(rationale, dict) or "zh" not in rationale or "en" not in rationale:
                    fail(
                        f"report[{report_idx}] ({report['id']}) benchmarkSymbol "
                        f"'{report['benchmarkSymbol']}' overrides the resolved default "
                        f"'{resolved_default}' and must carry benchmarkRationale.{{zh,en}}"
                    )
                validate_bilingual_text(rationale, f"report[{report_idx}].benchmarkRationale")
        else:
            fail(
                f"report[{report_idx}] ({report['id']}) has benchmarkSymbol but is not a "
                "current-chain report; the override is only meaningful on chain reports"
            )
    elif "benchmarkRationale" in report:
        fail(
            f"report[{report_idx}] ({report['id']}) has benchmarkRationale without a "
            "benchmarkSymbol override"
        )

    if "priceAsOf" in report:
        ensure_non_empty_string(report["priceAsOf"], f"report[{report_idx}].priceAsOf")
        parse_date(report["priceAsOf"], f"report[{report_idx}].priceAsOf")

    if "reportedPeriod" in report:
        ensure_non_empty_string(report["reportedPeriod"], f"report[{report_idx}].reportedPeriod")

    if "related" in report:
        related = report["related"]
        if not isinstance(related, list) or not related:
            fail(f"report[{report_idx}].related must be a non-empty array when present")
        if len(set(related)) != len(related):
            fail(f"report[{report_idx}].related has duplicate ids")
        for rel_idx, rel_id in enumerate(related):
            validate_report_reference(rel_id, f"report[{report_idx}].related[{rel_idx}]", reports_by_id)
            if rel_id == report["id"]:
                fail(f"report[{report_idx}].related must not reference itself")

    if "monitoring" in report:
        validate_monitoring(report, report_idx)

    validate_coverage_tier(report, report_idx)

    is_current_chain = is_current_chain_report(report)
    if ENFORCE_CHAIN_ENRICHMENT and is_current_chain:
        for field in ("stance", "priceAsOf", "reportedPeriod", "monitoring"):
            if field not in report:
                fail(
                    f"report[{report_idx}] ({report['id']}) is a current chainLayer "
                    f"report and must carry enrichment field: {field}"
                )

    validate_stance_v2_requirements(report, report_idx)


def validate_price_symbol_uniqueness(reports):
    seen = {}
    for idx, report in enumerate(reports):
        is_current_chain = bool(report.get("chainLayer")) and report.get("isCurrent") is not False
        symbol = report.get("priceSymbol")
        if not is_current_chain or symbol is None:
            continue
        if symbol in seen:
            fail(
                f"report[{idx}].priceSymbol duplicates current-chain report "
                f"{seen[symbol]}: {symbol}"
            )
        seen[symbol] = report["id"]


def main():
    if not REPORTS_JSON.exists():
        fail(f"missing file: {REPORTS_JSON}")

    with open(REPORTS_JSON, "r", encoding="utf-8") as file:
        try:
            reports = json.load(file)
        except json.JSONDecodeError as exc:
            fail(f"invalid JSON: {exc}")

    if not isinstance(reports, list) or not reports:
        fail("reports.json must be a non-empty array")

    reports_by_id = {}
    for idx, report in enumerate(reports):
        if not isinstance(report, dict):
            fail(f"report[{idx}] must be an object")

        report_id = report.get("id")
        ensure_non_empty_string(report_id, f"report[{idx}].id")
        if not re.fullmatch(r"[a-z0-9-]+", report_id):
            fail(f"report[{idx}].id should match [a-z0-9-]+: {report_id}")
        if report_id in reports_by_id:
            fail(f"duplicate report id: {report_id}")
        reports_by_id[report_id] = report

    # v6 (docs/research-hub-v6-plan.md §2.1): benchmarks.json drives per-report
    # override validation below.
    if not BENCHMARKS_JSON.exists():
        fail(f"missing file: {BENCHMARKS_JSON}")
    with open(BENCHMARKS_JSON, "r", encoding="utf-8") as file:
        try:
            benchmarks_cfg = json.load(file)
        except json.JSONDecodeError as exc:
            fail(f"invalid JSON in {BENCHMARKS_JSON}: {exc}")
    validate_benchmarks_config(benchmarks_cfg)

    for idx, report in enumerate(reports):
        for field in REQUIRED_FIELDS:
            if field not in report:
                fail(f"report[{idx}] missing required field: {field}")

        report_id = report["id"]

        for field in ("company", "ticker", "title", "titleEn", "summary", "category"):
            ensure_non_empty_string(report[field], f"report[{idx}].{field}")

        parse_date(report["date"], f"report[{idx}].date")
        parse_date(report["lastUpdate"], f"report[{idx}].lastUpdate")

        if not isinstance(report["tags"], list) or not report["tags"]:
            fail(f"report[{idx}].tags must be a non-empty array")
        for tag_idx, tag in enumerate(report["tags"]):
            ensure_non_empty_string(tag, f"report[{idx}].tags[{tag_idx}]")

        highlights = report.get("highlights")
        if highlights is not None:
            if not isinstance(highlights, list):
                fail(f"report[{idx}].highlights must be an array when present")
            for hl_idx, highlight in enumerate(highlights):
                ensure_non_empty_string(highlight, f"report[{idx}].highlights[{hl_idx}]")

        file_url = report["file"]
        ensure_non_empty_string(file_url, f"report[{idx}].file")
        expected_url = f"/invest/research/reports/view.html?id={report_id}"
        if file_url != expected_url:
            fail(
                f"report[{idx}].file should be {expected_url}, got: {file_url}"
            )

        markdown_files = report["markdownFiles"]
        if not isinstance(markdown_files, dict):
            fail(f"report[{idx}].markdownFiles must be an object")

        module_contract = report.get("moduleContract")
        if module_contract is not None and module_contract != REPORT_MODULE_CONTRACT:
            fail(
                f"report[{idx}].moduleContract must be "
                f"'{REPORT_MODULE_CONTRACT}': {module_contract}"
            )

        for lang in ("zh", "en"):
            if lang not in markdown_files:
                fail(f"report[{idx}].markdownFiles missing language: {lang}")

            markdown_url = markdown_files[lang]
            field_name = f"report[{idx}].markdownFiles.{lang}"
            markdown_file = resolve_markdown_file(markdown_url, field_name)
            if not markdown_file.exists():
                fail(
                    f"report[{idx}] markdown file not found for {lang}: {markdown_file}"
                )
            if lang == "en" and report.get("isCurrent") is not False:
                validate_english_markdown(markdown_file, field_name)
            validate_module_contract(markdown_file, module_contract, field_name)

        if markdown_files["zh"] == markdown_files["en"]:
            fail(
                f"report[{idx}].markdownFiles.zh and .en must be different files"
            )

        validate_version_metadata(report, idx, reports_by_id)
        validate_enrichment_fields(report, idx, reports_by_id, benchmarks_cfg)

    validate_price_symbol_uniqueness(reports)
    print(f"OK: validated {len(reports)} reports in {REPORTS_JSON}")


if __name__ == "__main__":
    main()
