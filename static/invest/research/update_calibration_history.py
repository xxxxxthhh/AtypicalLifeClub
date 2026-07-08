#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Final, Union

import calibration_history


Json = Union[None, bool, int, float, str, list["Json"], dict[str, "Json"]]

ROOT: Final = Path(__file__).resolve().parent
VERDICTS_JSON: Final = ROOT / "data" / "verdicts.json"
CALIBRATION_HISTORY_JSON: Final = ROOT / "data" / "calibration-history.json"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def load_json(path: Path, fallback: Json | None = None) -> Json:
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        if fallback is not None:
            return fallback
        fail(f"missing file: {path}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path}: {exc}")


def save_json(path: Path, data: Json) -> bool:
    encoded = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    previous = path.read_text(encoding="utf-8") if path.exists() else None
    if previous == encoded:
        return False
    path.write_text(encoded, encoding="utf-8")
    return True


def main() -> None:
    verdicts = load_json(VERDICTS_JSON)
    history = load_json(CALIBRATION_HISTORY_JSON, fallback=[])
    try:
        snapshot = calibration_history.build_snapshot(verdicts)
        updated = calibration_history.upsert_snapshot(history, snapshot)
        calibration_history.validate_history_rows(updated, verdicts)
    except calibration_history.CalibrationHistoryError as exc:
        fail(str(exc))
    changed = save_json(CALIBRATION_HISTORY_JSON, updated)
    print(
        f"Saved calibration history row for {snapshot['date']} to {CALIBRATION_HISTORY_JSON}"
        if changed
        else f"No calibration history changes detected for {snapshot['date']}"
    )


if __name__ == "__main__":
    main()
