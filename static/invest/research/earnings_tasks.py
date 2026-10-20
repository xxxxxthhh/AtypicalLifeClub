#!/usr/bin/env python3
"""Build the deterministic earnings research task queue."""

from __future__ import annotations

import argparse
import json
from datetime import date, datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parent
CALENDAR_JSON = ROOT / "data" / "earnings-calendar.json"
TASKS_JSON = ROOT / "data" / "earnings-tasks.json"


def load_calendar(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


CALL_UPDATE_REASON = (
    "Issuer-confirmed earnings call window (release time unconfirmed); "
    "first verify actual release filing/press release, then update the research package."
)


def task(
    report_id: str, expected_date: str | None, kind: str, window: str, reason: str, *, call: bool = False
) -> dict:
    date_key = f"call-{expected_date}" if call else expected_date or "unknown"
    return {
        "id": f"earnings:{report_id}:{date_key}:{window}",
        "reportId": report_id,
        "type": kind,
        "window": window,
        "expectedDate": expected_date,
        "reason": reason,
    }


def local_date(timezone_name: str, reference: date | datetime) -> date:
    if isinstance(reference, datetime):
        if reference.tzinfo is None:
            raise ValueError("reference datetime must be timezone-aware")
        return reference.astimezone(ZoneInfo(timezone_name)).date()
    return reference


def entry_date(calendar: dict, entry: dict, reference: date | datetime) -> date:
    return local_date(entry.get("timezone", calendar["defaultTimezone"]), reference)


def call_tasks(entry: dict, reference: date | datetime, release_maintenance: bool) -> list[dict]:
    """Tasks driven by the call sub-object; only used while the release is unconfirmed."""
    call = entry.get("call")
    if not call or (entry["status"] == "issuer-confirmed" and entry["precision"] == "day"):
        return []
    report_id = entry["reportId"]
    today = local_date(call["timezone"], reference)
    offset = (today - date.fromisoformat(call["expectedDate"])).days
    window = {-1: "T-1", 0: "T", 1: "T+1"}.get(offset)
    if window and call["status"] == "issuer-confirmed":
        return [task(report_id, call["expectedDate"], "research-update", window, CALL_UPDATE_REASON, call=True)]
    if offset > 1 and today.weekday() == 0 and not release_maintenance:
        return [
            task(
                report_id,
                call["expectedDate"],
                "calendar-maintenance",
                "stale",
                "Earnings call date has passed; roll the entry to the next cycle.",
                call=True,
            )
        ]
    return []


def build_tasks(calendar: dict, reference: date | datetime) -> list[dict]:
    tasks: list[dict] = []
    for entry in calendar["entries"]:
        report_id = entry["reportId"]
        expected = entry.get("expectedDate")
        precision = entry["precision"]
        status = entry["status"]
        today = entry_date(calendar, entry, reference)
        weekly = today.weekday() == 0

        lapsed = precision == "day" and (today - date.fromisoformat(expected)).days > 1

        if weekly and lapsed:
            tasks.append(
                task(report_id, expected, "calendar-maintenance", "stale", "Earnings date has passed; roll the entry to the next cycle.")
            )
        elif status == "issuer-confirmed" and precision == "day":
            offset = (today - date.fromisoformat(expected)).days
            window = {-1: "T-1", 0: "T", 1: "T+1"}.get(offset)
            if window:
                tasks.append(
                    task(
                        report_id,
                        expected,
                        "research-update",
                        window,
                        "Issuer-confirmed earnings window; verify release and update the research package.",
                    )
                )
        elif weekly and status == "recorded":
            tasks.append(
                task(report_id, expected, "source-verification", "verify", "Confirm the recorded date on issuer IR.")
            )
        elif weekly and status == "estimated":
            tasks.append(
                task(
                    report_id,
                    expected,
                    "date-completion",
                    "complete-date",
                    "Replace the estimate with an issuer-sourced day.",
                )
            )
        elif weekly and status in {"unknown", "stale"}:
            tasks.append(
                task(report_id, expected, "calendar-maintenance", status, f"Resolve {status} earnings calendar data.")
            )
        # The release already owns roll-over maintenance when it has lapsed or is unknown/stale.
        tasks.extend(call_tasks(entry, reference, lapsed or status in {"unknown", "stale"}))
    return sorted(tasks, key=lambda row: row["id"])


def utc_timestamp(value: datetime) -> str:
    if value.tzinfo is None:
        raise ValueError("generated_at must be timezone-aware")
    return value.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def build_payload(calendar: dict, reference: date | datetime, generated_at: datetime) -> dict:
    if isinstance(reference, datetime):
        reference_metadata = {"mode": "instant", "value": utc_timestamp(reference)}
    else:
        reference_metadata = {"mode": "literal-date", "value": reference.isoformat()}
    return {
        "schemaVersion": 1,
        "generatedAt": utc_timestamp(generated_at),
        "reference": reference_metadata,
        "tasks": build_tasks(calendar, reference),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--date",
        type=date.fromisoformat,
        help="Use one literal local date for every entry; defaults to the current instant converted per event timezone.",
    )
    parser.add_argument("--calendar", type=Path, default=CALENDAR_JSON)
    parser.add_argument("--output", type=Path, default=TASKS_JSON)
    args = parser.parse_args()
    now = datetime.now(timezone.utc)
    reference = args.date or now

    payload = build_payload(load_calendar(args.calendar), reference, now)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(payload['tasks'])} earnings task(s) to {args.output}")


if __name__ == "__main__":
    main()
