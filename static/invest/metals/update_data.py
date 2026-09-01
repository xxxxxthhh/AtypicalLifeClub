#!/usr/bin/env python3
"""
Daily update script for Metals module.
Fetches latest prices and appends to historical.json.
Designed to be run by GitHub Actions daily.
"""

import json
import math
from datetime import datetime, timezone
import sys
import os

from fetch_historical import (
    fetch_chart_result,
    fetch_daily_rows,
    parse_chart_rows,
    parse_split_events,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, "data", "historical.json")

# How far back each run re-reads and re-upserts.  Two reasons it is a window and
# not a single bar:
#   1. The exchange can revise a close after we first stored it.  The old path
#      took only df.iloc[-1], so a bar was written once and never looked at
#      again -- 111-114 rows per futures contract are wrong today precisely
#      because nothing ever went back to check them.
#   2. A skipped or failed run leaves a hole; the next run backfills it.
# 14 calendar days always spans at least nine completed sessions, even across a
# holiday week with two weekends in it, and costs one request per symbol either
# way.
RECENT_WINDOW_DAYS = 14

# Splits only matter for rows we actually store, and history is capped at
# LOOKBACK_DAYS, so a split older than the oldest row would back-adjust nothing.
SPLIT_LOOKBACK_DAYS = 730

# A file staler than this is a rebuild job, not a catch-up job, and asking for
# more than the history we keep would be pointless anyway.
MAX_CATCHUP_DAYS = SPLIT_LOOKBACK_DAYS

# Days of overlap kept when catching up, so the join between old and new rows is
# re-read rather than merely abutted.
CATCHUP_OVERLAP_DAYS = 3

# How many rows before a split we compare against the vendor before touching
# anything, and how far apart they may be.  The two hypotheses -- "already
# adjusted" and "not yet adjusted" -- sit exactly `ratio` apart, and the
# smallest real forward split (5:4) still separates them by 25%, so a 0.5% band
# cannot straddle both.  Anything outside both bands means we do not understand
# the data and must not divide it.
SPLIT_ANCHOR_COUNT = 5
SPLIT_ANCHOR_TOLERANCE = 0.005

ALL_SYMBOLS = [
    "GC=F", "SI=F", "PL=F", "PA=F", "HG=F",
    "COPX", "GLD", "SLV", "CPER", "DBB", "REMX", "LIT", "PPLT", "PALL",
]


def load_data(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(path, data):
    serialized = json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            if f.read() == serialized:
                return False

    with open(path, "w", encoding="utf-8") as f:
        f.write(serialized)
    return True


def is_finite_number(value):
    try:
        return math.isfinite(float(value))
    except (TypeError, ValueError):
        return False


def normalize_volume(value):
    if not is_finite_number(value):
        return 0
    return max(0, int(float(value)))


def normalize_record(record):
    """Return a stable daily record or None when price data is unusable."""
    close = record.get("close")
    if not is_finite_number(close):
        return None

    return {
        "date": record["date"],
        "close": round(float(close), 4),
        "volume": normalize_volume(record.get("volume", 0)),
    }


def fetch_split_bundle(symbol):
    """Return (events, {date: close}) for `symbol`, or None when unavailable.

    One request answers both questions, from one consistent snapshot: which
    splits Yahoo knows about, and what Yahoo's (split-adjusted) closes are for
    the dates we hold.  The second half is what lets us check a split against
    the data instead of trusting a bookkeeping field.

    None means "could not ask" and must not be confused with "no splits": a
    silent failure here is exactly how the 2026-05-18 PPLT/PALL splits poisoned
    two years of history.  A well-formed response with no `events` key is Yahoo
    saying the window holds no split; a response carrying an event we cannot
    parse raises, and lands here as None.
    """
    try:
        result = fetch_chart_result(symbol, SPLIT_LOOKBACK_DAYS, events="splits")
        events = parse_split_events(result)
        reference = {row["date"]: row["close"] for row in parse_chart_rows(result)}
        return events, reference
    except Exception as e:
        print(f"  ✗ {symbol}: split lookup failed: {e}")
        return None


def classify_split_state(history, date, ratio, reference, since=None):
    """Decide from the prices themselves whether `date`'s split is already in.

    Returns "applied", "pending", or None when the data supports neither answer.

    `since` bounds the comparison below by the next split still waiting to be
    processed.  Rows older than that one are a further ratio away from the
    vendor's fully adjusted series, so mixing them in would make the anchors
    contradict each other and sink an otherwise readable pair of stacked splits.

    This is the whole idempotence guarantee.  The old code divided whenever a
    cursor said it had not yet divided, so deleting `metadata.lastSplitApplied`
    -- or restoring an older copy of the file, or a rebuild that dropped the
    field -- made it divide a second time and turned PPLT's 2026-05-15 close
    into 1.7903 against a 17.84 neighbour.  Reading the answer out of the rows
    means repeating the run is harmless no matter what the metadata says.
    """
    earlier = [
        row for row in history
        if row["date"] < date and (since is None or row["date"] >= since)
    ]
    if not earlier:
        # Nothing before the split to back-adjust; recording the cursor is the
        # entire job.
        return "applied"

    anchors = []
    for row in reversed(earlier):  # nearest the split first: densest coverage
        vendor = reference.get(row["date"])
        if vendor is None or not is_finite_number(vendor) or float(vendor) <= 0:
            continue
        if not is_finite_number(row.get("close")):
            continue
        anchors.append((float(row["close"]), float(vendor)))
        if len(anchors) >= SPLIT_ANCHOR_COUNT:
            break

    if not anchors:
        return None

    verdicts = set()
    for local, vendor in anchors:
        if abs(local - vendor) <= SPLIT_ANCHOR_TOLERANCE * vendor:
            verdicts.add("applied")
        elif abs(local - vendor * ratio) <= SPLIT_ANCHOR_TOLERANCE * vendor * ratio:
            verdicts.add("pending")
        else:
            return None

    if len(verdicts) != 1:
        return None
    return verdicts.pop()


def apply_new_splits(data):
    """Back-adjust history for any split not yet applied.

    Returns (changed, failed_symbols). A non-empty failed_symbols must abort the
    whole run: the 35% continuity guard in validate_data.py is only a net for
    large splits, and it explicitly delegates small ones (3:2 and the like) to
    this function. If a lookup failed and we appended the day's bar anyway, an
    unadjusted split could slip past both layers.
    """
    metadata = data["metadata"]
    applied = metadata.setdefault("lastSplitApplied", {})
    log = metadata.setdefault("splitAdjustments", [])
    changed = False
    failed = []

    sections = {"metals": data["metals"], "etfs": data["etfs"]}
    for section_name, section in sections.items():
        for symbol, history in section.items():
            bundle = fetch_split_bundle(symbol)
            if bundle is None:
                failed.append(symbol)
                continue
            events, reference = bundle

            # Every event is classified against the vendor's own closes, every
            # run. The cursor records what we have seen; it decides nothing.
            #
            # It used to short-circuit this loop, and that was the whole defence
            # gone: restore the un-adjusted history, leave metadata.lastSplitApplied
            # in place, and the run reported changed=False / failed=[] while the
            # file sat two years out of scale. A stored field cannot vouch for the
            # state of the data next to it -- only the prices can. Classifying
            # unconditionally also catches the splits too small to trip the 35%
            # continuity guard, such as 5:4, which no threshold will ever see.
            pending = list(events)
            if not pending:
                continue

            # Newest split first.  The vendor's closes are adjusted for *every*
            # split, so a row is only one ratio away from its reference once the
            # later splits have been dealt with; walking backwards means each
            # comparison has exactly one unknown, and it is what lets two
            # stacked splits -- or one applied and one not -- resolve correctly.
            aborted = False
            descending = sorted(pending, reverse=True)
            for position, (date, ratio) in enumerate(descending):
                next_pending = descending[position + 1][0] if position + 1 < len(descending) else None
                state = classify_split_state(history, date, ratio, reference, since=next_pending)
                if state is None:
                    print(
                        f"  ✗ {symbol}: cannot tell whether the {ratio:g}:1 split on "
                        f"{date} is already applied — refusing to adjust"
                    )
                    failed.append(symbol)
                    aborted = True
                    break

                rows = 0
                if state == "pending":
                    for row in history:
                        if row["date"] < date:
                            row["close"] = round(row["close"] / ratio, 4)
                            rows += 1
                    print(f"  ⚠ {symbol}: {ratio:g}:1 split on {date} — back-adjusted {rows} rows")
                    changed = True
                else:
                    print(f"  ✓ {symbol}: {ratio:g}:1 split on {date} already in the data")

                log.append({
                    "symbol": symbol,
                    "date": date,
                    "ratio": ratio,
                    "rowsAdjusted": rows,
                    "state": state,
                    "appliedAt": datetime.now().isoformat(),
                })

            if aborted:
                continue

            cursor = max(date for date, _ratio in pending)
            if applied.get(symbol) != cursor:
                applied[symbol] = cursor
                changed = True

    return changed, failed


def window_days(history, observed_at):
    """Calendar days to request: the rolling window, or enough to catch up.

    A fixed 14-day window can only correct rows inside itself, so a job that
    stops for a month comes back and silently leaves a month-shaped hole -- the
    same class of gap that cost the ETFs 2026-07-14 and 2026-08-03.  Asking from
    the last date we hold (plus overlap, so the seam is re-read rather than just
    abutted) means a long outage heals on the first run back.

    TODO: this still only reconciles what the request covers.  A periodic
    full-history audit against the vendor -- comparing every stored row, not
    just the recent ones -- is the remaining gap; deliberately out of scope here.
    """
    if not history:
        return MAX_CATCHUP_DAYS

    last = datetime.strptime(history[-1]["date"], "%Y-%m-%d").date()
    behind = (observed_at.date() - last).days + CATCHUP_OVERLAP_DAYS
    return max(RECENT_WINDOW_DAYS, min(behind, MAX_CATCHUP_DAYS))


def fetch_recent(symbol, observed_at, history):
    """Completed bars covering `history`'s tail, or None when the request failed.

    None and [] mean genuinely different things and the caller must be able to
    tell them apart.  Collapsing a failed request into "no completed sessions"
    is how a partial run used to look like a successful one: one symbol's fetch
    dies, the rest write normally, the file saves, the workflow exits 0, and the
    hole is only found months later.
    """
    try:
        return fetch_daily_rows(symbol, window_days(history, observed_at), observed_at)
    except Exception as e:
        print(f"  ✗ {symbol}: {e}")
        return None


def window_is_plausible(history, rows):
    """An empty window is only believable for a symbol we hold nothing for.

    These symbols trade every weekday and we ask for at least a fortnight, so a
    successful-but-empty answer for a series with years of history is a vendor
    hiccup wearing the costume of a quiet market. Saying "no completed sessions"
    and moving on is precisely how a failure used to pass for a normal run.
    """
    return bool(rows) or not history


def apply_rows(history, rows):
    """Upsert every row into `history`, returning a tally of the outcomes."""
    counts = {"added": 0, "updated": 0, "unchanged": 0, "skipped": 0}
    for row in rows:
        counts[upsert_record(history, row)] += 1
    return counts


def reconcile_window(history, rows):
    """Drop local rows the vendor does not have inside the range it just covered.

    Upserting alone can only ever add or correct, so a row that should never
    have existed -- a Sunday bar, a session written twice under the wrong date --
    survives forever.  The deletion is bounded by the vendor's own first and last
    returned dates: outside that closed interval we have no evidence, and in
    particular a completed bar we stored last night sits *after* the last date a
    mid-session run returns, so it is never at risk.
    """
    if not rows:
        return 0

    covered = {row["date"] for row in rows}
    first, last = rows[0]["date"], rows[-1]["date"]
    phantoms = {
        row["date"] for row in history
        if first <= row["date"] <= last and row["date"] not in covered
    }
    if phantoms:
        history[:] = [row for row in history if row["date"] not in phantoms]
    return len(phantoms)


def update_section(section, symbols, observed_at):
    """Refresh one section in place.

    Returns (changed, failed_symbols); a non-empty failed_symbols must abort the
    run before anything is written.
    """
    changed = False
    failed = []
    for symbol in symbols:
        history = section[symbol]
        rows = fetch_recent(symbol, observed_at, history)
        if rows is None:
            failed.append(symbol)
            continue
        if not window_is_plausible(history, rows):
            print(
                f"  ✗ {symbol}: source returned no completed sessions for a series "
                f"that already holds {len(history)} of them"
            )
            failed.append(symbol)
            continue
        if not rows:
            print(f"  - {symbol}: source returned no completed sessions")
            continue

        counts = apply_rows(history, rows)
        removed = reconcile_window(history, rows)
        changed = changed or counts["added"] > 0 or counts["updated"] > 0 or removed > 0
        print(
            f"  ✓ {symbol}: {rows[-1]['close']} @ {rows[-1]['date']} "
            f"({counts['added']} added, {counts['updated']} corrected, "
            f"{counts['unchanged']} unchanged, {removed} removed)"
        )
    return changed, failed


def upsert_record(history_list, record):
    """Insert or update a record by date."""
    normalized = normalize_record(record)
    if normalized is None:
        return "skipped"

    for i, existing in enumerate(history_list):
        if existing["date"] == normalized["date"]:
            existing_normalized = normalize_record(existing)
            if existing_normalized is None or existing_normalized["close"] != normalized["close"]:
                history_list[i] = normalized
                return "updated"

            existing_volume = existing_normalized["volume"]
            if existing_volume == 0 and normalized["volume"] > 0:
                history_list[i] = normalized
                return "updated"

            return "unchanged"

    history_list.append(normalized)
    history_list.sort(key=lambda x: x["date"])
    return "added"


def build_current(data):
    """Build current prices from the latest two finite records per symbol."""
    current = {}
    all_data = {**data["metals"], **data["etfs"]}
    for symbol, history in all_data.items():
        valid_history = [row for row in history if normalize_record(row) is not None]
        if len(valid_history) >= 2:
            latest = normalize_record(valid_history[-1])
            prev = normalize_record(valid_history[-2])
            change = latest["close"] - prev["close"]
            pct = (change / prev["close"] * 100) if prev["close"] else 0
            current[symbol] = {
                "price": latest["close"],
                "change": round(change, 4),
                "changePct": round(pct, 2),
                "date": latest["date"],
            }
    return current


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DATA_PATH
    print(f"Loading data from {path}")
    data = load_data(path)

    # One clock for the whole run, so every symbol is judged complete against
    # the same instant no matter how long the run takes.
    observed_at = datetime.now(timezone.utc)
    print(f"Fetching latest data (observed at {observed_at.isoformat()})\n")

    # Splits must be applied before the new bar is appended, otherwise a
    # post-split close lands next to un-adjusted history.
    print("=== Checking for splits ===")
    changed_by_split, split_failures = apply_new_splits(data)
    if split_failures:
        print(
            f"\n❌ 拆分查询失败: {', '.join(split_failures)}\n"
            "   本次不写入任何数据。未核对拆分就追加当日价格，会让未复权的拆分\n"
            "   同时绕过本层与 validate_data.py 的 35% 跳变网。"
        )
        sys.exit(1)
    if not changed_by_split:
        print("  ✓ no new splits")
    print()

    metals_symbols = list(data["metadata"]["metals"].keys())
    etf_symbols = list(data["metadata"]["etfs"].keys())
    changed = changed_by_split

    print("=== Metals ===")
    metals_changed, metals_failed = update_section(data["metals"], metals_symbols, observed_at)

    print("\n=== ETFs ===")
    etfs_changed, etfs_failed = update_section(data["etfs"], etf_symbols, observed_at)

    fetch_failures = metals_failed + etfs_failed
    if fetch_failures:
        print(
            f"\n❌ 取数失败: {', '.join(fetch_failures)}\n"
            "   本次不写入任何数据。只写成功的那部分会让失败的标的停在旧日期，\n"
            "   而 workflow 仍然成功退出——ETF 的 07-14/08-03 缺口就是这样来的。"
        )
        sys.exit(1)

    changed = changed or metals_changed or etfs_changed

    # Rebuild current prices
    current = build_current(data)
    if data.get("current") != current:
        data["current"] = current
        changed = True

    if not changed:
        print("\n✅ No data changes detected; file left untouched")
        return

    data["metadata"]["last_updated"] = datetime.now().isoformat()

    if save_data(path, data):
        print(f"\n✅ Updated! Saved to {path}")
    else:
        print("\n✅ Serialized output unchanged; file left untouched")


if __name__ == "__main__":
    main()
