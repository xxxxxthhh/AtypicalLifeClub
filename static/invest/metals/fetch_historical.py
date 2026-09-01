#!/usr/bin/env python3
"""
Fetch historical metals & ETF data using Yahoo Finance public API.
No external dependencies - uses only Python stdlib.
"""

import json
import math
import urllib.request
import time
import sys
import os
from datetime import datetime, time as time_of_day, timedelta, timezone
from zoneinfo import ZoneInfo

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

METALS = {
    "GC=F":  {"name": "Gold",      "unit": "USD/oz"},
    "SI=F":  {"name": "Silver",    "unit": "USD/oz"},
    "PL=F":  {"name": "Platinum",  "unit": "USD/oz"},
    "PA=F":  {"name": "Palladium", "unit": "USD/oz"},
    "HG=F":  {"name": "Copper",    "unit": "USD/lb"},
}

ETFS = {
    "COPX": {"name": "Global X Copper Miners ETF",        "category": "copper"},
    "GLD":  {"name": "SPDR Gold Shares",                  "category": "gold"},
    "SLV":  {"name": "iShares Silver Trust",              "category": "silver"},
    "CPER": {"name": "US Copper Index Fund",              "category": "copper"},
    "DBB":  {"name": "Invesco DB Base Metals Fund",       "category": "base_metals"},
    "REMX": {"name": "VanEck Rare Earth/Strategic Metals", "category": "rare_earth"},
    "LIT":  {"name": "Global X Lithium & Battery Tech",   "category": "lithium"},
    "PPLT": {"name": "abrdn Physical Platinum Shares",    "category": "platinum"},
    "PALL": {"name": "abrdn Physical Palladium Shares",   "category": "palladium"},
}

LOOKBACK_DAYS = 730
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"

# Every symbol in this module trades in New York.  The daily bar for trade date
# D is only final once that symbol's session for D has closed:
#   - CME/COMEX/NYMEX metals futures (GC/SI/PL/PA/HG): the Globex trade date
#     that carries date D opens 18:00 ET on D-1 and ends 17:00 ET on D.
#   - US-listed ETFs: NYSE/Cboe regular close, 16:00 ET on D.
# Half-days (Thanksgiving Friday, Christmas Eve) close at 13:00 ET, i.e. earlier
# than these cutoffs, so the rule is only ever conservative -- it can delay a
# bar, never accept an unfinished one.
FUTURES_SESSION_CLOSE = time_of_day(17, 0)
EQUITY_SESSION_CLOSE = time_of_day(16, 0)
DEFAULT_EXCHANGE_TIMEZONE = "America/New_York"

# The bell is when trading stops, not when the vendor has published a settled
# close; a bar read at the closing second can still carry a provisional print.
# The scheduled run is hours past either cutoff (01:00 UTC is 21:00 ET), so this
# buffer costs nothing in practice and only ever delays a bar by one day.
PUBLICATION_BUFFER = timedelta(minutes=20)


def is_finite_number(value):
    try:
        return math.isfinite(float(value))
    except (TypeError, ValueError):
        return False


def fetch_chart_result(symbol, days, events=None):
    """Return Yahoo's raw chart result for `symbol`, or raise.

    Deliberately does not swallow errors: callers must be able to tell "the
    request failed" from "the request succeeded and found nothing".
    """
    end_ts = int(time.time())
    start_ts = end_ts - (days * 86400)
    url = (
        f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
        f"?period1={start_ts}&period2={end_ts}&interval=1d"
    )
    if events:
        url += f"&events={events}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=15) as resp:
        payload = json.loads(resp.read().decode())
    return payload["chart"]["result"][0]


def exchange_timezone(result):
    """The exchange's own timezone, which is the only frame the bars mean.

    Futures bars are stamped at exchange-local midnight, so deriving the date
    from a scalar UTC offset moves a bar to the wrong calendar day whenever the
    offset in `meta` (always the *current* one) disagrees with the offset in
    force when the bar printed.  A real timezone has no such seam.
    """
    name = (result.get("meta") or {}).get("exchangeTimezoneName") or DEFAULT_EXCHANGE_TIMEZONE
    try:
        return ZoneInfo(name)
    except Exception:
        return ZoneInfo(DEFAULT_EXCHANGE_TIMEZONE)


class IncompleteChartResponse(Exception):
    """The vendor answered 200 but the payload has holes inside its own range.

    A null close on an interior timestamp is not "that day did not trade" -- the
    vendor put the timestamp there, so it believes the session exists. Treating
    the hole as absence is what lets reconcile_window() delete a locally correct
    row: ask for [08-27, 08-28, 08-31] with a null on 08-28 and the good 08-28
    close gets removed. A trailing null is different and expected: that is the
    session still in progress.
    """


def interior_gap_dates(result):
    """Dates the payload lists but leaves without a usable close, ignoring the tail."""
    tz = exchange_timezone(result)
    timestamps = result.get("timestamp") or []
    quotes = (result.get("indicators") or {}).get("quote") or [{}]
    closes = (quotes[0] if quotes else {}).get("close") or []

    if len(timestamps) != len(closes):
        return [f"<timestamp/close length mismatch: {len(timestamps)} vs {len(closes)}>"]

    last_usable = max(
        (i for i, close in enumerate(closes) if is_finite_number(close)),
        default=-1,
    )
    return [
        datetime.fromtimestamp(ts, tz).strftime("%Y-%m-%d")
        for i, (ts, close) in enumerate(zip(timestamps, closes))
        if i < last_usable and not is_finite_number(close)
    ]


def parse_chart_rows(result):
    """Parse a chart result into ascending [{date, close, volume}] records."""
    tz = exchange_timezone(result)
    timestamps = result.get("timestamp") or []
    quotes = (result.get("indicators") or {}).get("quote") or [{}]
    quote = quotes[0] if quotes else {}
    closes = quote.get("close") or []
    volumes = quote.get("volume") or [0] * len(timestamps)

    records = []
    for ts, close, vol in zip(timestamps, closes, volumes):
        if not is_finite_number(close):
            continue
        records.append({
            "date": datetime.fromtimestamp(ts, tz).strftime("%Y-%m-%d"),
            "close": round(float(close), 4),
            "volume": int(vol) if is_finite_number(vol) and vol else 0,
        })
    records.sort(key=lambda row: row["date"])
    return records


def session_close(symbol):
    """Local closing time of the session whose trade date labels the bar."""
    return FUTURES_SESSION_CLOSE if symbol.endswith("=F") else EQUITY_SESSION_CLOSE


def completed_rows(symbol, rows, observed_at, tz=None):
    """Drop bars whose session has not closed yet.

    Yahoo publishes a bar for the session in progress: probed mid-session on
    Monday 2026-08-31 the chart API already returned an 08-31 bar for every
    symbol, carrying the live price rather than a close.  Writing that into
    history is how the old updater recorded 111-114 wrong rows per futures
    contract, all of them dated from the day the daily job took over, and none
    of them ever revisited.

    The test is deterministic and independent of when the job actually runs:
    a bar dated D counts only once `observed_at` has passed D's local session
    close.  GitHub's scheduler can fire hours late -- the same reason
    static/invest/research/update_prices.py::completed_quotes exists -- and a
    late run must still refuse tomorrow's half-formed bar rather than take
    whatever row happens to be last.

    A run landing exactly at the close can still catch a not-quite-final print;
    that is repaired by the rolling window, which re-reads and re-upserts the
    bar on the following runs.
    """
    if observed_at.tzinfo is None or observed_at.utcoffset() is None:
        raise ValueError("observed_at must be timezone-aware")

    tz = tz or ZoneInfo(DEFAULT_EXCHANGE_TIMEZONE)
    closing_time = session_close(symbol)
    completed = []
    for row in rows:
        day = datetime.strptime(row["date"], "%Y-%m-%d").date()

        # Nothing here has a weekend trade date.  The CME's Sunday-evening open
        # belongs to *Monday's* trade date, so a Saturday- or Sunday-dated daily
        # bar is always a mislabelled session in progress rather than a close --
        # 25 of the 28-29 phantom rows in the file are Sundays.  The chart API
        # has never emitted one in a 730-day probe of all 14 symbols; this is the
        # belt to that braces, and it is what the time test alone would miss,
        # since Sunday 17:00 ET is in the past by the time Monday's job runs.
        if day.weekday() >= 5:
            continue

        close_at = datetime.combine(day, closing_time, tzinfo=tz) + PUBLICATION_BUFFER
        if observed_at >= close_at:
            completed.append(row)
    return completed


def fetch_daily_rows(symbol, days, observed_at=None):
    """Completed daily bars for `symbol` over the last `days` calendar days."""
    result = fetch_chart_result(symbol, days)
    gaps = interior_gap_dates(result)
    if gaps:
        raise IncompleteChartResponse(
            f"{symbol}: vendor payload has interior gaps at {', '.join(gaps)}"
        )
    rows = parse_chart_rows(result)
    return completed_rows(
        symbol,
        rows,
        observed_at or datetime.now(timezone.utc),
        exchange_timezone(result),
    )


def parse_split_events(result):
    """[(YYYY-MM-DD, ratio), ...] ascending, from a chart `events=splits` result.

    Yahoo omits the `events` key entirely when the window holds no split, so an
    absent key is a genuine "no splits", not a parse failure.

    A *present* event we cannot read is the opposite, and raises.  Skipping it
    would report "no splits" for a symbol that just split, which is precisely
    the silent-failure shape that let the 2026-05-18 PPLT/PALL splits through.
    """
    events = (result.get("events") or {}).get("splits") or {}
    parsed = []
    for key, event in events.items():
        numerator = event.get("numerator")
        denominator = event.get("denominator")
        stamp = event.get("date")
        if not (is_finite_number(numerator) and is_finite_number(denominator)
                and is_finite_number(stamp)):
            raise ValueError(f"unreadable split event {key!r}: {event!r}")
        if float(denominator) <= 0 or float(numerator) <= 0:
            raise ValueError(f"nonsensical split ratio in event {key!r}: {event!r}")
        date = datetime.fromtimestamp(int(stamp), exchange_timezone(result)).strftime("%Y-%m-%d")
        parsed.append((date, float(numerator) / float(denominator)))
    return sorted(parsed)


def fetch_history_and_splits(symbol, days, observed_at=None):
    """One request, both answers: completed bars and the split events beside them.

    The rebuild path deliberately tolerates a splits-parse failure that the
    daily path refuses.  Here the rows are the product and a bad event must not
    cost us the symbol's entire series; the cursor simply goes unseeded, and
    update_data's anchor check then verifies the split against the data itself.
    """
    result = fetch_chart_result(symbol, days, events="splits")
    rows = completed_rows(
        symbol,
        parse_chart_rows(result),
        observed_at or datetime.now(timezone.utc),
        exchange_timezone(result),
    )
    try:
        splits = parse_split_events(result)
    except Exception as e:
        print(f"  ! {symbol}: split events unreadable ({e}); cursor left unseeded")
        splits = None
    return rows, splits


def build_current(metals_data, etfs_data):
    """Build current prices from latest data points."""
    current = {}
    for symbol, history in {**metals_data, **etfs_data}.items():
        if len(history) >= 2:
            latest = history[-1]
            prev = history[-2]
            change = latest["close"] - prev["close"]
            pct = (change / prev["close"] * 100) if prev["close"] else 0
            current[symbol] = {
                "price": latest["close"],
                "change": round(change, 4),
                "changePct": round(pct, 2),
                "date": latest["date"],
            }
    return current


# Split bookkeeping that a rebuild must never silently drop.  `lastSplitApplied`
# is update_data's fast path, `knownSplits` is the curated audit list, and
# `splitAdjustments` is the running log; wiping any of them turns a stray full
# rebuild into a loaded gun pointed at the next daily run.
SPLIT_METADATA_KEYS = ("lastSplitApplied", "knownSplits", "splitAdjustments")


def load_existing_metadata(path):
    """The split bookkeeping already on disk, so a rebuild carries it forward."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            metadata = json.load(f).get("metadata") or {}
    except (OSError, ValueError):
        return {}
    return {key: metadata[key] for key in SPLIT_METADATA_KEYS if key in metadata}


def seed_split_cursors(carried, observed_splits):
    """Mark every split the rebuilt series already reflects as applied.

    Chart-API closes are split-adjusted at source, so a freshly rebuilt row is
    post-split by construction and must not be back-adjusted again.  Seeding the
    cursor here is what stops the next daily run from dividing two years of
    history a second time.

    A symbol whose events could not be read (None) is left unseeded rather than
    guessed: update_data verifies against the data itself before it divides, so
    an absent cursor is merely slower, never wrong.  Cursors only ever move
    forward -- a rebuild must not walk one backwards.
    """
    seeded = dict(carried)
    for symbol, events in observed_splits.items():
        if not events:
            continue
        latest = max(date for date, _ratio in events)
        if symbol not in seeded or latest > seeded[symbol]:
            seeded[symbol] = latest
    return seeded


def main():
    output_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(SCRIPT_DIR, "data", "historical.json")
    print(f"Building historical data → {output_path}\n")

    carried = load_existing_metadata(output_path)
    if carried:
        print(f"Carrying forward split metadata: {', '.join(sorted(carried))}\n")

    observed_splits = {}
    failures = []

    def fetch_section(symbols):
        section = {}
        for symbol in symbols:
            try:
                rows, splits = fetch_history_and_splits(symbol, LOOKBACK_DAYS)
                # A rebuild that finds nothing over two years has not found
                # "no data", it has failed to ask properly.  Either way the
                # empty list must never reach the file.
                if not rows:
                    raise ValueError(f"no completed sessions in {LOOKBACK_DAYS} days")
            except Exception as e:
                print(f"  ✗ {symbol}: {e}")
                failures.append(symbol)
            else:
                print(f"  ✓ {symbol}: {len(rows)} days")
                section[symbol] = rows
                observed_splits[symbol] = splits
            time.sleep(0.5)
        return section

    print("=== Fetching Metals Spot Data ===")
    metals_data = fetch_section(METALS)

    print("\n=== Fetching ETF Data ===")
    etfs_data = fetch_section(ETFS)

    # Fail closed, exactly as update_data.py does.  Writing the symbols that did
    # come back would erase two years of history for the one that did not, and
    # an empty array is precisely the shape that looks like a legitimate value
    # on the way past every downstream reader.
    if failures:
        print(
            f"\n❌ 取数失败: {', '.join(failures)}\n"
            "   本次不重建、不写入任何文件。把失败的标的写成空数组，等于一次\n"
            "   抹掉它两年的历史，而且抹得像一个合法结果。"
        )
        sys.exit(1)

    current = build_current(metals_data, etfs_data)

    metadata = {
        "metals": METALS,
        "etfs": ETFS,
        "lookback_days": LOOKBACK_DAYS,
        "last_updated": datetime.now().isoformat(),
        "total_metals": len(METALS),
        "total_etfs": len(ETFS),
    }
    metadata.update(carried)
    metadata["lastSplitApplied"] = seed_split_cursors(
        carried.get("lastSplitApplied") or {}, observed_splits
    )

    result = {
        "metadata": metadata,
        "current": current,
        "metals": metals_data,
        "etfs": etfs_data,
    }

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    total = sum(len(v) for v in metals_data.values()) + sum(len(v) for v in etfs_data.values())
    print(f"\n✅ Done! Saved to {output_path}")
    print(f"   Total data points: {total}")


if __name__ == "__main__":
    main()
