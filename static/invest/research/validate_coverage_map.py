#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
# -*- coding: utf-8 -*-
"""
Validate the AI infrastructure coverage map metadata, cross-check signal log, and page wiring.

# ─── How to run ───
# python3 static/invest/research/validate_coverage_map.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Final, Union

Json = Union[None, bool, int, float, str, list["Json"], dict[str, "Json"]]

ROOT: Final = Path(__file__).resolve().parent
REPORTS_JSON: Final = ROOT / "data" / "reports.json"
COVERAGE_JSON: Final = ROOT / "data" / "coverage-map.json"
SIGNALS_JSON: Final = ROOT / "data" / "signals.json"
COVERAGE_HTML: Final = ROOT / "coverage-map.html"

EXPECTED_LAYERS: Final = [
    "foundry",
    "compute",
    "custom-merchant-silicon",
    "memory-storage",
    "networking",
    "optical",
    "power",
    "datacenter-facility",
    "resources",
    "demand-risk",
]

EXPECTED_ROLES: Final = [
    "dashboard",
    "risk-anchor",
    "architecture-check",
    "common-constraint",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def load_json(path: Path) -> Json:
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        fail(f"missing file: {path}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path}: {exc}")


def require_dict(value: Json, label: str) -> dict[str, Json]:
    if not isinstance(value, dict):
        fail(f"{label} must be an object")
    return value


def require_list(value: Json, label: str) -> list[Json]:
    if not isinstance(value, list):
        fail(f"{label} must be an array")
    return value


def require_string(value: Json, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(f"{label} must be a non-empty string")
    return value


def read_entries(root: dict[str, Json], key: str) -> list[dict[str, Json]]:
    items = require_list(root.get(key), f"coverage-map.json.{key}")
    entries: list[dict[str, Json]] = []
    for index, item in enumerate(items):
        entries.append(require_dict(item, f"coverage-map.json.{key}[{index}]"))
    return entries


def read_ids(entries: list[dict[str, Json]], label: str) -> list[str]:
    ids: list[str] = []
    for index, entry in enumerate(entries):
        ids.append(require_string(entry.get("id"), f"{label}[{index}].id"))
    return ids


def require_bilingual_text(value: Json, label: str) -> None:
    text = require_dict(value, label)
    require_string(text.get("zh"), f"{label}.zh")
    require_string(text.get("en"), f"{label}.en")


def validate_layer_and_role_ids(coverage: dict[str, Json]) -> None:
    layers = read_ids(read_entries(coverage, "layers"), "layers")
    roles = read_ids(read_entries(coverage, "roles"), "roles")

    if layers != EXPECTED_LAYERS:
        fail(f"layer ids/order mismatch: {layers}")
    if roles != EXPECTED_ROLES:
        fail(f"role ids/order mismatch: {roles}")
    if "supplier-layer" in roles:
        fail("supplier-layer role must not be present")


def validate_planned_entries(coverage: dict[str, Json]) -> None:
    layer_ids = set(read_ids(read_entries(coverage, "layers"), "layers"))
    planned_raw = coverage.get("planned", [])
    planned = require_list(planned_raw, "coverage-map.json.planned")

    for index, item in enumerate(planned):
        entry = require_dict(item, f"coverage-map.json.planned[{index}]")
        require_string(entry.get("ticker"), f"coverage-map.json.planned[{index}].ticker")
        layer = require_string(entry.get("layer"), f"coverage-map.json.planned[{index}].layer")
        if layer not in layer_ids:
            fail(f"planned[{index}] has unknown layer: {layer}")
        require_bilingual_text(entry.get("label"), f"coverage-map.json.planned[{index}].label")


def validate_cross_checks(coverage: dict[str, Json]) -> set[str]:
    checks = read_entries(coverage, "crossChecks")
    ids: set[str] = set()
    for index, entry in enumerate(checks):
        check_id = require_string(entry.get("id"), f"coverage-map.json.crossChecks[{index}].id")
        if check_id in ids:
            fail(f"duplicate crossCheck id: {check_id}")
        ids.add(check_id)
        require_bilingual_text(entry.get("if"), f"coverage-map.json.crossChecks[{index}].if")
        require_bilingual_text(entry.get("then"), f"coverage-map.json.crossChecks[{index}].then")
    return ids


def validate_signals(check_ids: set[str]) -> None:
    signals = require_list(load_json(SIGNALS_JSON), "signals.json")
    seen: set[str] = set()
    for index, item in enumerate(signals):
        entry = require_dict(item, f"signals.json[{index}]")
        signal_id = require_string(entry.get("id"), f"signals.json[{index}].id")
        if signal_id in seen:
            fail(f"duplicate signal id: {signal_id}")
        seen.add(signal_id)

        date = require_string(entry.get("date"), f"signals.json[{index}].date")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
            fail(f"signals.json[{index}].date must be YYYY-MM-DD, got: {date}")

        require_bilingual_text(entry.get("title"), f"signals.json[{index}].title")
        require_bilingual_text(entry.get("detail"), f"signals.json[{index}].detail")

        refs = require_list(entry.get("crossChecks"), f"signals.json[{index}].crossChecks")
        if not refs:
            fail(f"signals.json[{index}].crossChecks must reference at least one crossCheck id")
        for ref_index, ref in enumerate(refs):
            ref_id = require_string(ref, f"signals.json[{index}].crossChecks[{ref_index}]")
            if ref_id not in check_ids:
                fail(f"signals.json[{index}] references unknown crossCheck id: {ref_id}")

        tickers = entry.get("tickers", [])
        for ticker_index, ticker in enumerate(require_list(tickers, f"signals.json[{index}].tickers")):
            require_string(ticker, f"signals.json[{index}].tickers[{ticker_index}]")


def validate_report_metadata(reports: list[dict[str, Json]], coverage: dict[str, Json]) -> None:
    layer_ids = set(read_ids(read_entries(coverage, "layers"), "layers"))
    role_ids = set(read_ids(read_entries(coverage, "roles"), "roles"))

    for index, report in enumerate(reports):
        report_id = require_string(report.get("id"), f"report[{index}].id")

        chain_layer = report.get("chainLayer")
        if chain_layer is not None:
            layer = require_string(chain_layer, f"report[{index}].chainLayer")
            if layer not in layer_ids:
                fail(f"{report_id} has unknown chainLayer: {layer}")

        chain_role = report.get("chainRole")
        if chain_role is not None:
            role = require_string(chain_role, f"report[{index}].chainRole")
            if role not in role_ids:
                fail(f"{report_id} has unknown chainRole: {role}")
            if role == "supplier-layer":
                fail(f"{report_id} uses forbidden chainRole supplier-layer")


def validate_page_wiring() -> None:
    try:
        html = COVERAGE_HTML.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing file: {COVERAGE_HTML}")

    required_paths = [
        "/invest/research/data/coverage-map.json",
        "/invest/research/data/reports.json",
    ]
    for path in required_paths:
        if path not in html:
            fail(f"coverage-map.html missing fetch path: {path}")

    if 'if (!layerReports.length) return "";' not in html:
        fail("coverage-map.html must skip empty layers before rendering")

    if 'id="chainGraph"' not in html:
        fail("coverage-map.html missing chainGraph container")
    if "renderChainGraph()" not in html:
        fail("coverage-map.html must render the chain graph section")


def main() -> None:
    coverage = require_dict(load_json(COVERAGE_JSON), "coverage-map.json")
    reports_raw = require_list(load_json(REPORTS_JSON), "reports.json")
    reports = [
        require_dict(item, f"reports.json[{index}]")
        for index, item in enumerate(reports_raw)
    ]

    validate_layer_and_role_ids(coverage)
    validate_planned_entries(coverage)
    check_ids = validate_cross_checks(coverage)
    validate_signals(check_ids)
    validate_report_metadata(reports, coverage)
    validate_page_wiring()
    print("OK: coverage map metadata, signal log, and page wiring are valid")


if __name__ == "__main__":
    main()
