#!/usr/bin/env python3
"""Build the deterministic daily briefing (docs/daily-briefing-plan.md, Track 2).

Every source is read from git at one locked commit, never from the working
tree, so a live run and a replay take the same path:

    python3 static/invest/briefing/generate_briefing.py
    python3 static/invest/briefing/generate_briefing.py \
        --date 2026-08-31 --since-sha <base> --as-of-sha <current>

"New" is decided by the cursor, not by dates inside the data: an object counts
when it first appears on main after the previous briefing's source commit.
"""

from __future__ import annotations

import argparse
import json
import statistics
import subprocess
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[2]

sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT.parent / "research"))
sys.path.insert(0, str(ROOT.parent / "currency"))
from check_alerts import ALERT_THRESHOLD_SIGMA, WARNING_THRESHOLD_SIGMA, calculate_deviation  # noqa: E402
from earnings_tasks import entry_date, utc_timestamp  # noqa: E402
from validate_briefing import validate_markdown, validate_payload  # noqa: E402

SITE_URL = "https://atypicallife.club"
BRIEFING_DIR = "static/invest/briefing"
LATEST_PATH = f"{BRIEFING_DIR}/latest.json"
SOURCES = {
    "signals": "static/invest/research/data/signals.json",
    "reports": "static/invest/research/data/reports.json",
    "verdicts": "static/invest/research/data/verdicts.json",
    "calendar": "static/invest/research/data/earnings-calendar.json",
    "prices": "static/invest/research/data/prices.json",
    "metals": "static/invest/metals/data/historical.json",
    "currency": "static/invest/currency/data/historical.json",
}

# The owner reads this in China and the 06:15 CST price run lands at 22:15 UTC
# the day before; a UTC date would stamp that briefing a day early.
BRIEFING_TIMEZONE = ZoneInfo("Asia/Shanghai")

# §4.1.1.  The window is 90 *returns* before the day, not 90 calendar days:
# 92 closes.  Read the other way, GLD on 2026-08-28 drops out of the briefing.
METALS_WINDOW = 90
METALS_THRESHOLD = 2.0
# One metal, two legs.  They differ mostly by settlement time (futures 13:30 ET,
# ETF 16:00 ET), so the briefing reports the metal, not the ticker.
METAL_GROUPS = (
    ("黄金", ("GC=F", "GLD")),
    ("白银", ("SI=F", "SLV")),
    ("钯金", ("PA=F", "PALL")),
    ("铂金", ("PL=F", "PPLT")),
    ("铜", ("HG=F", "CPER")),
    ("铜矿股", ("COPX",)),
    ("基本金属", ("DBB",)),
    ("稀土", ("REMX",)),
    ("锂电", ("LIT",)),
)

CURRENCIES = ("CNY", "SGD", "JPY", "AUD")
CURRENCY_WINDOW = 365
EARNINGS_LOOKAHEAD = 5
SESSION_LABELS = {"after-close": "盘后", "before-open": "盘前"}


class BriefingError(Exception):
    """The briefing cannot be produced honestly; nothing is written."""


# --- git ---------------------------------------------------------------------


def git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True)


def resolve_sha(repo: Path, ref: str) -> str:
    result = git(repo, "rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}")
    if result.returncode != 0:
        raise BriefingError(f"cannot resolve commit {ref!r}")
    return result.stdout.strip()


def show_json(repo: Path, sha: str, path: str):
    """The JSON at `path` in commit `sha`, or None when the file is not there."""
    result = git(repo, "show", f"{sha}:{path}")
    if result.returncode != 0:
        return None
    return json.loads(result.stdout)


def load_snapshot(repo: Path, sha: str) -> dict:
    return {name: show_json(repo, sha, path) for name, path in SOURCES.items()}


def choose_base(previous: dict | None, today: str, since_sha: str | None) -> str:
    """§4.2: where this briefing's window starts.

    A same-day rerun keeps the day's first baseline.  Taking the previous run's
    own source instead would diff only first-run → second-run and drop
    everything the first run already listed.
    """
    if since_sha:
        return since_sha
    if previous is None:
        raise BriefingError("no previous latest.json on the source commit; the first briefing needs --since-sha")
    if previous["date"] > today:
        raise BriefingError(f"latest.json is dated {previous['date']}, after {today}; a replay needs --since-sha")
    if previous["date"] == today:
        return previous["previousSourceMainSha"]
    return previous["sourceMainSha"]


# --- metals ------------------------------------------------------------------


def return_z(closes: list[float], index: int) -> tuple[float, float] | None:
    """(return, z) of bar `index` against the 90 returns before it, or None.

    The day itself stays out of its own baseline; an extreme day would otherwise
    shrink its own |z| exactly when it matters.  Sample standard deviation, as
    in check_alerts.py.
    """
    if index < METALS_WINDOW + 1:
        return None
    window = closes[index - METALS_WINDOW - 1 : index + 1]
    returns = [after / before - 1 for before, after in zip(window, window[1:])]
    baseline, today = returns[:-1], returns[-1]
    spread = statistics.stdev(baseline)
    if spread == 0:
        return None
    return today, (today - statistics.mean(baseline)) / spread


def metals_series(data: dict) -> dict[str, list[dict]]:
    """historical.json keeps futures and ETFs apart; the gate treats all 14 alike."""
    return {**data["metals"], **data["etfs"]}


def metals_section(series: dict[str, list[dict]], seen: dict[str, str]) -> list[dict]:
    """Metals whose new bars moved at least 2σ.

    `seen` maps a symbol to the last bar date the previous briefing's source
    already held.  Only later bars are judged, so an alert is reported once and
    a bar that lands late still gets its turn the next day.  A symbol absent
    from `seen` has only its latest bar judged.
    """
    crossings: dict[tuple[str, str], dict] = {}
    for symbol, rows in series.items():
        closes = [row["close"] for row in rows]
        since = seen.get(symbol)
        indexes = range(len(rows) - 1, len(rows)) if since is None else [
            index for index, row in enumerate(rows) if row["date"] > since
        ]
        for index in indexes:
            reading = return_z(closes, index)
            # Compared un-rounded: GLD at -2.0533 and PALL at +1.9333 both
            # display as roughly 2.0.
            if reading is None or abs(reading[1]) < METALS_THRESHOLD:
                continue
            crossings[(symbol, rows[index]["date"])] = {
                "leg": symbol,
                "price": closes[index],
                "changePct": round(reading[0] * 100, 2),
                "z": round(reading[1], 2),
                "window": METALS_WINDOW,
                "level": "alert",
                "asOf": rows[index]["date"],
            }

    listed = []
    for day in sorted({day for _symbol, day in crossings}):
        groups = []
        for metal, legs in METAL_GROUPS:
            crossed = [crossings[(leg, day)] for leg in legs if (leg, day) in crossings]
            # Two legs disagreeing on direction is the reading, not noise:
            # dropping one would be a judgment nothing here supports.
            conflict = len({row["z"] > 0 for row in crossed}) > 1
            crossed.sort(key=lambda row: abs(row["z"]), reverse=True)
            if not conflict:
                crossed = crossed[:1]
            if crossed:
                groups.append([{"metal": metal, **row, **({"conflict": True} if conflict else {})} for row in crossed])
        # Largest move of the day first.
        for group in sorted(groups, key=lambda group: abs(group[0]["z"]), reverse=True):
            listed += group
    return listed


def latest_bar_dates(series: dict[str, list[dict]]) -> dict[str, str]:
    return {symbol: rows[-1]["date"] for symbol, rows in series.items() if rows}


# --- currency ----------------------------------------------------------------


def currency_section(data: dict) -> list[dict]:
    """All four pairs, every day: converting is a standing decision, not an alert.

    Price z over the last 365 rows with the sample standard deviation, by
    calling check_alerts.py itself so the two cannot drift apart.
    """
    as_of = data["historical"][-1]["date"]
    rows = []
    for code in CURRENCIES:
        result = calculate_deviation(code, data, days=CURRENCY_WINDOW)
        if result is None:
            continue
        if result["abs_deviation"] >= ALERT_THRESHOLD_SIGMA:
            level = "alert"
        elif result["abs_deviation"] >= WARNING_THRESHOLD_SIGMA:
            level = "warning"
        else:
            level = "none"
        rows.append({
            "pair": f"USD/{code}",
            "rate": round(result["current"], 4),
            "z": round(result["deviation"], 2),
            "window": CURRENCY_WINDOW,
            "level": level,
            "asOf": as_of,
        })
    return rows


# --- research ----------------------------------------------------------------


def report_url(report: dict | None) -> str | None:
    return f"{SITE_URL}{report['file']}" if report and report.get("file") else None


def research_section(base: dict, current: dict) -> list[dict]:
    """What first reached main inside the cursor window, by stable id.

    `date` and `lastUpdate` on the objects only label the evidence; a signal
    dated five days ago that landed today is today's news.  A source with no
    base snapshot is skipped: without a previous value nothing can be called new.
    """
    reports = {report["id"]: report for report in current["reports"] or []}
    items = []

    if base["signals"] is not None:
        known = {signal["id"] for signal in base["signals"]}
        fresh = [signal for signal in current["signals"] if signal["id"] not in known]
        for signal in sorted(fresh, key=lambda signal: (signal["date"], signal["id"])):
            linked = next((reports[rid] for rid in signal.get("reportIds", []) if rid in reports), None)
            items.append({
                "kind": "signal",
                "ticker": "/".join(signal["tickers"]),
                "text": signal["title"]["zh"],
                "url": report_url(linked),
                "evidenceDate": signal["date"],
            })

    if base["reports"] is not None:
        before = {report["id"]: report for report in base["reports"]}
        for report in sorted(reports.values(), key=lambda report: (report["lastUpdate"], report["id"])):
            previous = before.get(report["id"])
            if previous is not None and report["lastUpdate"] <= previous["lastUpdate"]:
                continue
            verb = "新报告" if previous is None else "报告更新"
            items.append({
                "kind": "report",
                "ticker": report.get("priceSymbol") or report["ticker"],
                "text": f"{verb}：{report['company']}（{report['versionLabel']}）",
                "url": report_url(report),
                "evidenceDate": report["lastUpdate"],
            })

    if base["verdicts"] is not None and current["verdicts"] is not None:
        before = {entry["reportId"]: entry for entry in base["verdicts"]["entries"]}
        for entry in sorted(current["verdicts"]["entries"], key=lambda entry: entry["reportId"]):
            previous = before.get(entry["reportId"])
            if previous is None:
                continue
            changes = [
                f"{label} {previous.get(field)} → {entry.get(field)}"
                for field, label in (("stance", "stance"), ("conviction", "conviction"), ("stale", "stale"))
                if previous.get(field) != entry.get(field)
            ]
            if not changes:
                continue
            report = reports.get(entry["reportId"])
            items.append({
                "kind": "verdict",
                "ticker": (report or {}).get("priceSymbol") or entry["reportId"],
                "text": f"{(report or {}).get('company', entry['reportId'])}：{'；'.join(changes)}",
                "url": report_url(report),
                "evidenceDate": entry["stanceDate"],
            })

    return items


# --- earnings ----------------------------------------------------------------


def weekdays_until(today: date, target: date) -> int:
    """Weekdays after `today` up to and including `target`.

    No exchange holiday calendar: the entries span several markets and a holiday
    only makes an event look one trading day further than it is.
    """
    return sum((today + timedelta(days=step)).weekday() < 5 for step in range(1, (target - today).days + 1))


def earnings_section(calendar: dict, reference: date | datetime) -> list[dict]:
    """Day-precision earnings dates within the next five trading days."""
    rows = []
    for entry in calendar["entries"]:
        if entry["precision"] != "day":
            continue
        expected = date.fromisoformat(entry["expectedDate"])
        today = entry_date(calendar, entry, reference)
        if expected < today:
            continue
        away = weekdays_until(today, expected)
        if away > EARNINGS_LOOKAHEAD:
            continue
        rows.append({
            "date": entry["expectedDate"],
            "company": entry["company"],
            "session": entry["session"],
            "status": entry["status"],
            "tradingDaysAway": away,
        })
    return sorted(rows, key=lambda row: (row["date"], row["company"]))


# --- assembly ----------------------------------------------------------------


def build_payload(
    base: dict,
    current: dict,
    previous: dict | None,
    today: date,
    reference: date | datetime,
    base_sha: str,
    current_sha: str,
    generated_at: datetime,
) -> dict:
    series = metals_series(current["metals"])
    seen = latest_bar_dates(metals_series(base["metals"])) if base["metals"] else {}
    sections = {
        "research": research_section(base, current),
        "earnings": earnings_section(current["calendar"], reference),
        "metals": metals_section(series, seen),
        "currency": currency_section(current["currency"]),
    }

    if sections["research"]:
        research_as_of = today.isoformat()
    elif previous is not None:
        research_as_of = previous["asOf"]["research"]
    else:
        research_as_of = max(report["lastUpdate"] for report in current["reports"])

    return {
        "date": today.isoformat(),
        "generatedAt": utc_timestamp(generated_at),
        "sourceMainSha": current_sha,
        "previousSourceMainSha": base_sha,
        # "Nothing worth sending today" (Principle 4).  The four currency pairs
        # are listed every day, so they only count once one crosses 1.5σ;
        # otherwise no day could ever be empty.
        "empty": not (
            sections["research"]
            or sections["earnings"]
            or sections["metals"]
            or any(row["level"] != "none" for row in sections["currency"])
        ),
        "asOf": {
            "currency": current["currency"]["historical"][-1]["date"],
            "metals": max(latest_bar_dates(series).values()),
            "prices": max(entry["lastDate"] for entry in current["prices"]["entries"]),
            "research": research_as_of,
        },
        "sections": sections,
    }


def signed(value: float, digits: int = 2) -> str:
    return f"{value:+.{digits}f}"


def render_markdown(payload: dict) -> str:
    """Human-readable copy.  Neutral markers only: no judgment colours or lights."""
    sections, as_of = payload["sections"], payload["asOf"]
    lines = [f"# ALC 每日简报 · {payload['date']}", ""]
    if payload["empty"]:
        lines += ["今日无重要变化。", ""]

    if sections["research"]:
        lines.append(f"## 研究 · as of {as_of['research']}")
        for item in sections["research"]:
            text = f"[{item['text']}]({item['url']})" if item["url"] else item["text"]
            lines.append(f"- {item['ticker']} · {text}（证据日 {item['evidenceDate']}）")
        lines.append("")

    if sections["earnings"]:
        lines.append("## 财报前瞻 · 未来 5 个交易日")
        for row in sections["earnings"]:
            session = SESSION_LABELS.get(row["session"])
            when = "今天" if row["tradingDaysAway"] == 0 else f"{row['tradingDaysAway']} 个交易日后"
            lines.append(f"- {row['date']} {session + ' ' if session else ''}{row['company']}（{row['status']}）· {when}")
        lines.append("")

    if sections["metals"]:
        lines.append(f"## 金属 · as of {as_of['metals']}")
        for row in sections["metals"]:
            conflict = "，两腿方向相反" if row.get("conflict") else ""
            lines.append(
                f"- [2σ] {row['metal']} {row['price']:g}（{signed(row['changePct'])}%，"
                f"z {signed(row['z'])}σ({row['window']}日)，{row['leg']} @ {row['asOf']}{conflict}）"
            )
        lines.append("")

    if sections["currency"]:
        lines.append(f"## 汇率 · as of {as_of['currency']}")
        for row in sections["currency"]:
            marker = {"alert": "[2σ] ", "warning": "[1.5σ] "}.get(row["level"], "")
            lines.append(f"- {marker}{row['pair']} {row['rate']:.4f} · z {signed(row['z'])}σ(1y)")
        lines.append("")

    lines.append(f"来源 main `{payload['sourceMainSha'][:12]}`，自 `{payload['previousSourceMainSha'][:12]}` 起。")
    return "\n".join(lines) + "\n"


def same_content(previous: dict | None, payload: dict) -> bool:
    """True when a rerun found nothing new; the files are then left alone."""
    if previous is None:
        return False
    volatile = ("generatedAt", "sourceMainSha")
    return {k: v for k, v in previous.items() if k not in volatile} == {
        k: v for k, v in payload.items() if k not in volatile
    }


def generate(
    repo: Path,
    output_dir: Path,
    today: date,
    reference: date | datetime,
    generated_at: datetime,
    since_sha: str | None = None,
    as_of_sha: str | None = None,
) -> dict | None:
    """Write today's briefing and return it, or None when nothing changed."""
    if as_of_sha is None:
        # The workflow_run payload's head_sha is the commit the upstream job
        # started from, not the data commit it pushed; only our own fetch knows
        # what main is now.
        if git(repo, "fetch", "--quiet", "origin", "main").returncode != 0:
            raise BriefingError("cannot fetch origin/main")
        as_of_sha = "origin/main"
    current_sha = resolve_sha(repo, as_of_sha)

    previous = show_json(repo, current_sha, LATEST_PATH)
    if previous is not None and validate_payload(previous):
        raise BriefingError("published latest.json is invalid; its cursor cannot be trusted")
    base_sha = resolve_sha(repo, choose_base(previous, today.isoformat(), since_sha))
    if git(repo, "merge-base", "--is-ancestor", base_sha, current_sha).returncode != 0:
        raise BriefingError(
            f"cursor {base_sha[:12]} is not an ancestor of {current_sha[:12]}: "
            "history was rewritten or the clone is too shallow"
        )

    current = load_snapshot(repo, current_sha)
    missing = sorted(name for name, value in current.items() if value is None)
    if missing:
        raise BriefingError(f"source commit {current_sha[:12]} lacks: {', '.join(missing)}")

    payload = build_payload(
        load_snapshot(repo, base_sha), current, previous, today, reference, base_sha, current_sha, generated_at
    )
    markdown = render_markdown(payload)
    errors = validate_payload(payload) + validate_markdown(markdown)
    if errors:
        raise BriefingError("generated briefing is invalid: " + "; ".join(errors))

    if same_content(previous, payload):
        return None
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "latest.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (output_dir / f"{payload['date']}.md").write_text(markdown, encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", type=date.fromisoformat, help="Briefing date; defaults to today in Asia/Shanghai.")
    parser.add_argument("--since-sha", help="Cursor base. Required for the first briefing and for replays.")
    parser.add_argument("--as-of-sha", help="Source commit to read; defaults to a freshly fetched origin/main.")
    parser.add_argument("--output-dir", type=Path, default=ROOT)
    args = parser.parse_args()
    now = datetime.now(timezone.utc)

    try:
        payload = generate(
            REPO,
            args.output_dir,
            today=args.date or now.astimezone(BRIEFING_TIMEZONE).date(),
            reference=args.date or now,
            generated_at=now,
            since_sha=args.since_sha,
            as_of_sha=args.as_of_sha,
        )
    except BriefingError as error:
        print(f"FAIL: {error}")
        sys.exit(1)
    if payload is None:
        print("Briefing unchanged; nothing written")
    else:
        counts = ", ".join(f"{name} {len(rows)}" for name, rows in payload["sections"].items())
        print(f"Wrote briefing {payload['date']} (empty={payload['empty']}; {counts}) to {args.output_dir}")


if __name__ == "__main__":
    main()
