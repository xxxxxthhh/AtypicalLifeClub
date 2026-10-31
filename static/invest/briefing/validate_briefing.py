#!/usr/bin/env python3
"""Fail-closed check of the published briefing (docs/daily-briefing-plan.md §4.3).

latest.json is a public URL and a downstream contract, so every key is on a
whitelist: a field nobody declared here cannot ride along, which is what keeps
the substance of unreviewed open items out of it (§6.1).

    python3 static/invest/briefing/validate_briefing.py
"""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LATEST_JSON = ROOT / "latest.json"

SHA = re.compile(r"[0-9a-f]{40}")
TIMESTAMP = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")
REQUIRED = {"date", "generatedAt", "sourceMainSha", "previousSourceMainSha", "empty", "asOf", "sections"}
OPTIONAL = {"openItemCount"}
AS_OF = {"currency", "metals", "prices", "research"}
# Per section: required keys and their types, then optional keys.
SECTIONS = {
    "research": ({"kind": str, "ticker": str, "text": str, "url": (str, type(None)), "evidenceDate": str}, {}),
    "earnings": ({"date": str, "company": str, "session": str, "status": str, "tradingDaysAway": int}, {}),
    "metals": (
        {"metal": str, "leg": str, "price": (int, float), "changePct": (int, float), "z": (int, float),
         "window": int, "level": str, "asOf": str},
        {"conflict": bool},
    ),
    "currency": (
        {"pair": str, "rate": (int, float), "z": (int, float), "window": int, "level": str, "asOf": str},
        {},
    ),
}
DATE_FIELDS = {"research": "evidenceDate", "earnings": "date", "metals": "asOf", "currency": "asOf"}
LEVELS = {"metals": {"alert"}, "currency": {"none", "warning", "alert"}}
WINDOWS = {"metals": 90, "currency": 365}
RESEARCH_KINDS = {"signal", "report", "verdict"}
# DESIGN.md: investment judgment is never encoded as red / green / amber.
JUDGMENT_MARKS = "🔴🟠🟡🟢🟥🟧🟨🟩"


def is_date(value) -> bool:
    try:
        return isinstance(value, str) and date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def validate_payload(payload) -> list[str]:
    if not isinstance(payload, dict):
        return ["latest.json must be an object"]
    errors = [f"missing field: {key}" for key in sorted(REQUIRED - payload.keys())]
    errors += [f"undeclared field: {key}" for key in sorted(payload.keys() - REQUIRED - OPTIONAL)]
    if errors:
        return errors

    if not is_date(payload["date"]):
        errors.append("date must be YYYY-MM-DD")
    if not isinstance(payload["generatedAt"], str) or not TIMESTAMP.fullmatch(payload["generatedAt"]):
        errors.append("generatedAt must be a UTC timestamp ending in Z")
    for key in ("sourceMainSha", "previousSourceMainSha"):
        if not isinstance(payload[key], str) or not SHA.fullmatch(payload[key]):
            errors.append(f"{key} must be a 40-character commit SHA")
    if not isinstance(payload["empty"], bool):
        errors.append("empty must be a boolean")
    if "openItemCount" in payload and (
        isinstance(payload["openItemCount"], bool)
        or not isinstance(payload["openItemCount"], int)
        or payload["openItemCount"] < 0
    ):
        errors.append("openItemCount must be a non-negative integer; omit it when the queue is unreadable")

    as_of = payload["asOf"]
    if not isinstance(as_of, dict) or set(as_of) != AS_OF:
        errors.append(f"asOf must have exactly: {', '.join(sorted(AS_OF))}")
    else:
        errors += [f"asOf.{key} must be YYYY-MM-DD" for key in sorted(AS_OF) if not is_date(as_of[key])]

    sections = payload["sections"]
    if not isinstance(sections, dict) or set(sections) != set(SECTIONS):
        return errors + [f"sections must have exactly: {', '.join(SECTIONS)}"]
    for name, (required, optional) in SECTIONS.items():
        if not isinstance(sections[name], list):
            errors.append(f"sections.{name} must be an array")
            continue
        for index, row in enumerate(sections[name]):
            errors += validate_row(f"sections.{name}[{index}]", name, row, required, optional)
    if errors:
        return errors

    noteworthy = bool(
        sections["research"]
        or sections["earnings"]
        or sections["metals"]
        or any(row["level"] != "none" for row in sections["currency"])
    )
    if payload["empty"] == noteworthy:
        errors.append("empty must be true exactly when no section has anything to report")
    return errors


def validate_row(where: str, section: str, row, required: dict, optional: dict) -> list[str]:
    if not isinstance(row, dict):
        return [f"{where} must be an object"]
    errors = [f"{where} missing {key}" for key in sorted(required.keys() - row.keys())]
    errors += [f"{where} has undeclared field {key}" for key in sorted(row.keys() - required.keys() - optional.keys())]
    for key, kind in {**required, **optional}.items():
        # bool is an int in Python; a true/false must not pass for a number.
        if key in row and (not isinstance(row[key], kind) or (isinstance(row[key], bool) and kind is not bool)):
            errors.append(f"{where}.{key} has the wrong type")
    if errors:
        return errors

    if not is_date(row[DATE_FIELDS[section]]):
        errors.append(f"{where}.{DATE_FIELDS[section]} must be YYYY-MM-DD")
    if section in LEVELS:
        if row["level"] not in LEVELS[section]:
            errors.append(f"{where}.level must be one of {sorted(LEVELS[section])}")
        if row["window"] != WINDOWS[section]:
            errors.append(f"{where}.window must be {WINDOWS[section]}")
    if section == "research" and row["kind"] not in RESEARCH_KINDS:
        errors.append(f"{where}.kind must be one of {sorted(RESEARCH_KINDS)}")
    return errors


def validate_markdown(text: str) -> list[str]:
    found = sorted({mark for mark in JUDGMENT_MARKS if mark in text})
    return [f"markdown uses judgment-coloured marks: {' '.join(found)}"] if found else []


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else LATEST_JSON
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"FAIL: missing file: {path}")
        sys.exit(1)
    except json.JSONDecodeError as error:
        print(f"FAIL: invalid JSON in {path}: {error}")
        sys.exit(1)

    errors = validate_payload(payload)
    if not errors:
        markdown = path.with_name(f"{payload['date']}.md")
        if markdown.exists():
            errors = validate_markdown(markdown.read_text(encoding="utf-8"))
        else:
            errors = [f"missing {markdown.name} beside latest.json"]
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        sys.exit(1)
    print(f"OK: briefing {payload['date']} is valid")


if __name__ == "__main__":
    main()
