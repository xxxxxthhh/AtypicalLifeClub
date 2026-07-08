from __future__ import annotations

import math
from datetime import datetime
from typing import Final, Union


Json = Union[None, bool, int, float, str, list["Json"], dict[str, "Json"]]

BOOK_BENCHMARK: Final = "SMH"
NEUTRAL_STANCE: Final = "neutral-watch"
STANCE_ORDER: Final = ("bullish", "constructive", "neutral-watch", "cautious", "bearish-avoid")


class CalibrationHistoryError(ValueError):
    pass


def build_snapshot(verdicts: Json) -> dict[str, Json]:
    root = _dict(verdicts, "verdicts.json")
    generated_at = _date_text(root.get("generatedAt"), "verdicts.json.generatedAt")
    calls = _scored_calls(root)
    topline = _summary(calls, "bookRelativePct")
    by_benchmark: dict[str, Json] = {}
    for symbol in sorted({str(call["benchmarkSymbol"]) for call in calls}):
        bucket = [call for call in calls if call["benchmarkSymbol"] == symbol]
        by_benchmark[symbol] = _summary(bucket, "relativePct")
    return {
        "date": generated_at,
        "scoredCount": topline["scoredCount"],
        "medianRelativePct": topline["medianRelativePct"],
        "nonNeutralBeatRate": topline["nonNeutralBeatRate"],
        "byBenchmark": by_benchmark,
    }


def upsert_snapshot(history: Json, snapshot: dict[str, Json]) -> list[dict[str, Json]]:
    rows = [_dict(row, f"calibration-history[{index}]").copy() for index, row in enumerate(_list(history, "calibration-history"))]
    snapshot_date = _date_text(snapshot.get("date"), "snapshot.date")
    out: list[dict[str, Json]] = []
    replaced = False
    for row in rows:
        row_date = row.get("date")
        if row_date == snapshot_date:
            if not replaced:
                out.append(snapshot.copy())
                replaced = True
            continue
        out.append(row)
    if not replaced:
        out.append(snapshot.copy())
    out.sort(key=lambda row: _date_text(row.get("date"), "calibration-history.date"))
    return out


def validate_history_rows(history: Json, current_verdicts: Json) -> None:
    rows = _list(history, "calibration-history")
    previous_date: str | None = None
    seen: set[str] = set()
    current_snapshot = build_snapshot(current_verdicts)
    current_date = str(current_snapshot["date"])
    current_row: dict[str, Json] | None = None
    for index, item in enumerate(rows):
        row = _dict(item, f"calibration-history[{index}]")
        row_date = _date_text(row.get("date"), f"calibration-history[{index}].date")
        if row_date in seen:
            raise CalibrationHistoryError(f"calibration-history date duplicated: {row_date}")
        if previous_date is not None and row_date <= previous_date:
            raise CalibrationHistoryError(
                f"calibration-history dates must be strictly ascending: {previous_date} -> {row_date}"
            )
        seen.add(row_date)
        previous_date = row_date
        if row_date == current_date:
            current_row = row
    if current_row is None:
        raise CalibrationHistoryError(f"calibration-history missing current verdict date: {current_date}")
    if current_row != current_snapshot:
        raise CalibrationHistoryError(f"calibration-history current row does not match verdicts.json: {current_date}")


def _scored_calls(root: dict[str, Json]) -> list[dict[str, Json]]:
    calls: list[dict[str, Json]] = []
    for index, item in enumerate(_list(root.get("entries"), "verdicts.json.entries")):
        entry = _dict(item, f"verdicts.json.entries[{index}]")
        call = _scored_call(entry, f"verdicts.json.entries[{index}]", "stance")
        if call is not None:
            calls.append(call)
    for index, item in enumerate(_list(root.get("closed"), "verdicts.json.closed")):
        entry = _dict(item, f"verdicts.json.closed[{index}]")
        if entry.get("migration") is True:
            continue
        call = _scored_call(entry, f"verdicts.json.closed[{index}]", "fromStance")
        if call is not None:
            calls.append(call)
    return calls


def _scored_call(entry: dict[str, Json], label: str, stance_field: str) -> dict[str, Json] | None:
    if not _is_number(entry.get("relativePct")):
        return None
    book_symbol = _string(entry.get("bookBenchmarkSymbol"), f"{label}.bookBenchmarkSymbol")
    if book_symbol != BOOK_BENCHMARK:
        raise CalibrationHistoryError(f"{label}.bookBenchmarkSymbol must be {BOOK_BENCHMARK}")
    return {
        "stance": _string(entry.get(stance_field), f"{label}.{stance_field}"),
        "benchmarkSymbol": _string(entry.get("benchmarkSymbol"), f"{label}.benchmarkSymbol"),
        "relativePct": _number(entry.get("relativePct"), f"{label}.relativePct"),
        "bookRelativePct": _number(entry.get("bookRelativePct"), f"{label}.bookRelativePct"),
    }


def _summary(calls: list[dict[str, Json]], field: str) -> dict[str, Json]:
    values = [_number(call.get(field), field) for call in calls]
    non_neutral = [call for call in calls if call.get("stance") != NEUTRAL_STANCE]
    beats = [call for call in non_neutral if _number(call.get(field), field) > 0]
    stances: dict[str, Json] = {}
    for stance in _ordered_stances(calls):
        stance_values = [_number(call.get(field), field) for call in calls if call.get("stance") == stance]
        stances[stance] = {
            "scoredCount": len(stance_values),
            "medianRelativePct": _median(stance_values),
        }
    return {
        "scoredCount": len(values),
        "medianRelativePct": _median(values),
        "nonNeutralBeatRate": None if not non_neutral else len(beats) / len(non_neutral),
        "byStance": stances,
    }


def _ordered_stances(calls: list[dict[str, Json]]) -> list[str]:
    present = {str(call.get("stance")) for call in calls}
    ordered = [stance for stance in STANCE_ORDER if stance in present]
    return ordered + sorted(present - set(ordered))


def _median(values: list[float]) -> Json:
    if not values:
        return None
    ordered = sorted(values)
    mid = len(ordered) // 2
    value = ordered[mid] if len(ordered) % 2 else (ordered[mid - 1] + ordered[mid]) / 2
    return round(value, 1)


def _date_text(value: Json, label: str) -> str:
    text = _string(value, label)
    try:
        datetime.strptime(text, "%Y-%m-%d")
    except ValueError as exc:
        raise CalibrationHistoryError(f"{label} must be YYYY-MM-DD: {text}") from exc
    return text


def _dict(value: Json, label: str) -> dict[str, Json]:
    if not isinstance(value, dict):
        raise CalibrationHistoryError(f"{label} must be an object")
    return value


def _list(value: Json, label: str) -> list[Json]:
    if not isinstance(value, list):
        raise CalibrationHistoryError(f"{label} must be an array")
    return value


def _string(value: Json, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise CalibrationHistoryError(f"{label} must be a non-empty string")
    return value


def _number(value: Json, label: str) -> float:
    if not _is_number(value):
        raise CalibrationHistoryError(f"{label} must be a finite number")
    return float(value)


def _is_number(value: Json) -> bool:
    return not isinstance(value, bool) and isinstance(value, (int, float)) and math.isfinite(float(value))
