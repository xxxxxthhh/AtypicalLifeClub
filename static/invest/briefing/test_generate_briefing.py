#!/usr/bin/env python3
import json
import os
import subprocess
import sys
import tempfile
import unittest
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_briefing as briefing
from check_alerts import calculate_deviation

METALS_FIXTURE = briefing.ROOT.parent / "metals" / "fixtures" / "metals-2026-08-28.json"
GENERATED_AT = datetime(2026, 9, 1, 3, 7, tzinfo=timezone.utc)
# The commit that landed the MiniMax H1 signal (evidence dated 2026-08-26).
MINIMAX_LANDING = "8440a5e4ef19"


def bars(final_return, end="2026-08-28", count=92):
    """`count` weekday closes ending on `end`: a ±1% baseline, then `final_return`."""
    closes = [100.0]
    for step in range(count - 2):
        closes.append(closes[-1] * (1.01 if step % 2 == 0 else 0.99))
    closes.append(closes[-1] * (1 + final_return))
    days, day = [], date.fromisoformat(end)
    while len(days) < count:
        if day.weekday() < 5:
            days.append(day.isoformat())
        day -= timedelta(days=1)
    return [{"date": day, "close": round(close, 4), "volume": 1} for day, close in zip(reversed(days), closes)]


def signal(signal_id, evidence_date, tickers=("AAA",), report_ids=()):
    return {
        "id": signal_id,
        "date": evidence_date,
        "title": {"zh": f"标题 {signal_id}", "en": f"Title {signal_id}"},
        "tickers": list(tickers),
        "reportIds": list(report_ids),
    }


def report(report_id, last_update, label="2026 Initial Coverage"):
    return {
        "id": report_id,
        "company": f"Company {report_id}",
        "ticker": f"NYSE: {report_id.upper()}",
        "priceSymbol": report_id.upper(),
        "lastUpdate": last_update,
        "versionLabel": label,
        "file": f"/invest/research/reports/view.html?id={report_id}",
    }


def verdict(report_id, stance="neutral-watch", conviction="medium", stale=False):
    return {"reportId": report_id, "stance": stance, "conviction": conviction, "stale": stale, "stanceDate": "2026-08-01"}


def currency_data(end="2026-08-30", days=40):
    last = date.fromisoformat(end)
    rows = []
    for offset in range(days - 1, -1, -1):
        # The last row sits on the mean, so every pair reads about 0σ.
        wobble = 0 if offset == 0 else (0.01 if offset % 2 else -0.01)
        rows.append({
            "date": (last - timedelta(days=offset)).isoformat(),
            "rates": {"CNY": 7 + wobble, "SGD": 1.3 + wobble, "JPY": 150 + wobble, "AUD": 1.5 + wobble},
        })
    return {"historical": rows}


def world():
    return {
        "signals": [signal("old", "2026-08-01")],
        "reports": [report("r1", "2026-08-01")],
        "verdicts": {"entries": [verdict("r1")]},
        "calendar": {"schemaVersion": 1, "defaultTimezone": "America/New_York", "entries": []},
        "prices": {"entries": [{"reportId": "r1", "lastDate": "2026-08-28"}]},
        "metals": {"metals": {"GC=F": bars(0.001)}, "etfs": {"GLD": bars(0.001)}},
        "currency": currency_data(),
    }


class MetalsTests(unittest.TestCase):
    def test_frozen_2026_08_28_fixture_lists_exactly_palladium_futures_and_gold_etf(self):
        fixture = json.loads(METALS_FIXTURE.read_text(encoding="utf-8"))

        rows = briefing.metals_section(fixture, {})

        self.assertEqual(
            [(row["metal"], row["leg"], row["changePct"], row["z"], row["asOf"]) for row in rows],
            [("钯金", "PA=F", 6.8, 2.67, "2026-08-28"), ("黄金", "GLD", -3.24, -2.05, "2026-08-28")],
        )

    def test_frozen_fixture_z_values_match_the_pinned_caliber(self):
        fixture = json.loads(METALS_FIXTURE.read_text(encoding="utf-8"))
        expected = {"PA=F": 2.6739, "GLD": -2.0533, "PALL": 1.9333, "GC=F": -1.8937}
        for symbol, z in expected.items():
            closes = [row["close"] for row in fixture[symbol]]
            self.assertAlmostEqual(briefing.return_z(closes, len(closes) - 1)[1], z, places=4, msg=symbol)

    def test_same_direction_legs_collapse_to_the_larger_move(self):
        rows = briefing.metals_section({"GC=F": bars(0.03), "GLD": bars(0.05)}, {})
        self.assertEqual([(row["metal"], row["leg"]) for row in rows], [("黄金", "GLD")])
        self.assertNotIn("conflict", rows[0])

    def test_opposite_legs_are_both_kept_and_marked(self):
        rows = briefing.metals_section({"GC=F": bars(-0.05), "GLD": bars(0.04)}, {})
        self.assertEqual({row["leg"] for row in rows}, {"GC=F", "GLD"})
        self.assertTrue(all(row["conflict"] for row in rows))

    def test_legs_on_different_dates_are_not_merged(self):
        rows = briefing.metals_section({"GC=F": bars(0.05, end="2026-08-28"), "GLD": bars(0.05, end="2026-08-27")}, {})
        self.assertEqual([(row["leg"], row["asOf"]) for row in rows], [("GLD", "2026-08-27"), ("GC=F", "2026-08-28")])

    def test_one_crossing_leg_lists_the_metal_and_a_quiet_metal_is_absent(self):
        rows = briefing.metals_section({"PA=F": bars(0.05), "PALL": bars(0.015), "SI=F": bars(0.001)}, {})
        self.assertEqual([(row["metal"], row["leg"]) for row in rows], [("钯金", "PA=F")])

    def test_fewer_than_92_closes_is_skipped_not_judged(self):
        self.assertEqual(briefing.metals_section({"GC=F": bars(0.5, count=91)}, {}), [])
        self.assertEqual(len(briefing.metals_section({"GC=F": bars(0.5, count=92)}, {})), 1)

    def test_a_bar_the_previous_briefing_already_saw_is_not_reported_again(self):
        series = {"GC=F": bars(0.05)}
        self.assertEqual(briefing.metals_section(series, {"GC=F": "2026-08-28"}), [])
        self.assertEqual(len(briefing.metals_section(series, {"GC=F": "2026-08-27"})), 1)

    def test_every_bar_that_landed_since_the_cursor_gets_its_turn(self):
        rows = bars(0.05, end="2026-08-27", count=93)
        rows.append({"date": "2026-08-28", "close": rows[-1]["close"] * 1.001, "volume": 1})

        listed = briefing.metals_section({"GC=F": rows}, {"GC=F": "2026-08-26"})

        self.assertEqual([row["asOf"] for row in listed], ["2026-08-27"])


class CurrencyTests(unittest.TestCase):
    def test_lists_all_four_pairs_with_the_check_alerts_caliber(self):
        data = currency_data()
        data["historical"][-1]["rates"]["CNY"] = 7.5

        rows = briefing.currency_section(data)

        self.assertEqual([row["pair"] for row in rows], ["USD/CNY", "USD/SGD", "USD/JPY", "USD/AUD"])
        self.assertEqual(rows[0]["z"], round(calculate_deviation("CNY", data)["deviation"], 2))
        self.assertEqual([row["level"] for row in rows], ["alert", "none", "none", "none"])
        self.assertTrue(all(row["window"] == 365 and row["asOf"] == "2026-08-30" for row in rows))

    def test_warning_starts_at_one_and_a_half_sigma(self):
        data = currency_data()
        result = calculate_deviation("SGD", data)
        data["historical"][-1]["rates"]["SGD"] = result["mean"] + 1.75 * result["stdev"]
        self.assertEqual(briefing.currency_section(data)[1]["level"], "warning")


class ResearchTests(unittest.TestCase):
    def snapshot(self, **overrides):
        return {"signals": [], "reports": [], "verdicts": {"entries": []}, **overrides}

    def test_a_signal_is_new_when_its_id_first_appears_whatever_its_evidence_date(self):
        base = self.snapshot(signals=[signal("old", "2026-08-30")], reports=[report("r1", "2026-08-01")])
        current = self.snapshot(
            signals=[signal("old", "2026-08-30"), signal("late", "2026-08-26", tickers=("0100.HK", "BBB"), report_ids=("r1",))],
            reports=[report("r1", "2026-08-01")],
        )

        items = briefing.research_section(base, current)

        self.assertEqual(items, [{
            "kind": "signal",
            "ticker": "0100.HK/BBB",
            "text": "标题 late",
            "url": "https://atypicallife.club/invest/research/reports/view.html?id=r1",
            "evidenceDate": "2026-08-26",
        }])

    def test_a_signal_without_a_report_has_no_url(self):
        items = briefing.research_section(self.snapshot(), self.snapshot(signals=[signal("solo", "2026-08-30")]))
        self.assertIsNone(items[0]["url"])

    def test_reports_are_listed_when_new_or_when_last_update_advances(self):
        base = self.snapshot(reports=[report("same", "2026-08-01"), report("moved", "2026-08-01")])
        current = self.snapshot(
            reports=[report("same", "2026-08-01"), report("moved", "2026-08-30", "2026 Q2 Update"), report("born", "2026-08-29")]
        )

        items = briefing.research_section(base, current)

        self.assertEqual(
            [(item["kind"], item["ticker"], item["text"]) for item in items],
            [("report", "BORN", "新报告：Company born（2026 Initial Coverage）"),
             ("report", "MOVED", "报告更新：Company moved（2026 Q2 Update）")],
        )

    def test_verdict_changes_are_listed_against_the_previous_value(self):
        base = self.snapshot(verdicts={"entries": [verdict("r1"), verdict("r2")]})
        current = self.snapshot(
            reports=[report("r1", "2026-08-01")],
            verdicts={"entries": [verdict("r1", stance="cautious", stale=True), verdict("r2"), verdict("r3")]},
        )
        base["reports"] = current["reports"]

        items = briefing.research_section(base, current)

        self.assertEqual(
            [(item["kind"], item["text"]) for item in items],
            [("verdict", "Company r1：stance neutral-watch → cautious；stale False → True")],
        )

    def test_sources_without_a_previous_value_are_skipped_not_fatal(self):
        base = {"signals": None, "reports": None, "verdicts": None}
        current = self.snapshot(
            signals=[signal("a", "2026-08-30")], reports=[report("r1", "2026-08-30")], verdicts={"entries": [verdict("r1")]}
        )
        self.assertEqual(briefing.research_section(base, current), [])

    def test_real_history_replay_surfaces_the_late_minimax_h1_signal(self):
        # ci-smoke checks out one commit deep; this runs wherever history is present.
        probe = briefing.git(briefing.REPO, "rev-parse", "--verify", "--quiet", f"{MINIMAX_LANDING}^^{{commit}}")
        if probe.returncode != 0:
            self.skipTest("repository history is too shallow for the 2026-08-31 replay")
        base = briefing.load_snapshot(briefing.REPO, probe.stdout.strip())
        current = briefing.load_snapshot(briefing.REPO, briefing.resolve_sha(briefing.REPO, MINIMAX_LANDING))

        signals = [item for item in briefing.research_section(base, current) if item["kind"] == "signal"]

        self.assertEqual([(item["ticker"], item["evidenceDate"]) for item in signals], [("0100.HK", "2026-08-26")])
        self.assertTrue(signals[0]["text"].startswith("MiniMax H1 2026"))


class EarningsTests(unittest.TestCase):
    def calendar(self, *entries):
        return {"schemaVersion": 1, "defaultTimezone": "America/New_York", "entries": list(entries)}

    def entry(self, company, expected, precision="day", **extra):
        return {"reportId": company.lower(), "company": company, "expectedDate": expected, "precision": precision,
                "status": "issuer-confirmed", "session": "after-close", **extra}

    def test_window_is_five_weekdays_and_only_day_precision(self):
        data = self.calendar(
            self.entry("Today", "2026-08-31"),
            self.entry("Soon", "2026-09-02"),
            self.entry("Edge", "2026-09-07"),
            self.entry("Beyond", "2026-09-08"),
            self.entry("Past", "2026-08-28"),
            self.entry("Vague", "2026-09-01", precision="month"),
            self.entry("Unknown", None, precision="unknown"),
        )

        rows = briefing.earnings_section(data, date(2026, 8, 31))  # Monday

        self.assertEqual(
            [(row["company"], row["tradingDaysAway"]) for row in rows], [("Today", 0), ("Soon", 2), ("Edge", 5)]
        )
        self.assertEqual(rows[1], {"date": "2026-09-02", "company": "Soon", "session": "after-close",
                                   "status": "issuer-confirmed", "tradingDaysAway": 2})

    def test_a_weekend_does_not_count_as_trading_days(self):
        rows = briefing.earnings_section(self.calendar(self.entry("Monday", "2026-08-31")), date(2026, 8, 29))
        self.assertEqual(rows[0]["tradingDaysAway"], 1)

    def test_an_instant_is_read_in_each_event_timezone(self):
        data = self.calendar(self.entry("Taipei", "2026-09-02", timezone="Asia/Taipei"), self.entry("NewYork", "2026-09-02"))
        reference = datetime(2026, 9, 1, 23, 30, tzinfo=timezone.utc)

        rows = briefing.earnings_section(data, reference)

        self.assertEqual({row["company"]: row["tradingDaysAway"] for row in rows}, {"Taipei": 0, "NewYork": 1})


class CursorTests(unittest.TestCase):
    """The generator against a real repository, committed the way the workflow will."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        self.out = self.repo / briefing.BRIEFING_DIR
        self.env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.com",
                    "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.com"}
        self.git("init", "-q", "-b", "main")
        self.world = world()
        self.start = self.commit_world()

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.repo, env=self.env, check=True, capture_output=True, text=True).stdout.strip()

    def commit_world(self):
        for name, path in briefing.SOURCES.items():
            target = self.repo / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(json.dumps(self.world[name]), encoding="utf-8")
        return self.commit_all("data")

    def commit_all(self, message):
        self.git("add", "-A")
        self.git("commit", "-q", "--allow-empty", "-m", message)
        return self.git("rev-parse", "HEAD")

    def run_briefing(self, day, since=None):
        """Generate from HEAD and publish the result, as update-briefing.yml will."""
        payload = briefing.generate(self.repo, self.out, date.fromisoformat(day), date.fromisoformat(day),
                                    GENERATED_AT, since_sha=since, as_of_sha="HEAD")
        self.commit_all("briefing")
        return payload

    def texts(self, payload):
        return [item["text"] for item in payload["sections"]["research"]]

    def test_first_briefing_needs_an_explicit_cursor(self):
        with self.assertRaisesRegex(briefing.BriefingError, "--since-sha"):
            self.run_briefing("2026-08-31")

    def test_same_day_rerun_keeps_the_baseline_and_accumulates(self):
        self.world["signals"].append(signal("first", "2026-08-26"))
        first_source = self.commit_world()
        first = self.run_briefing("2026-08-31", since=self.start)
        self.world["signals"].append(signal("second", "2026-08-31"))
        second_source = self.commit_world()

        second = self.run_briefing("2026-08-31")

        self.assertEqual((first["previousSourceMainSha"], first["sourceMainSha"]), (self.start, first_source))
        self.assertEqual((second["previousSourceMainSha"], second["sourceMainSha"]), (self.start, second_source))
        self.assertEqual(self.texts(first), ["标题 first"])
        self.assertEqual(self.texts(second), ["标题 first", "标题 second"])

    def test_next_day_starts_from_the_last_source_and_repeats_nothing(self):
        self.world["signals"].append(signal("first", "2026-08-26"))
        source = self.commit_world()
        self.run_briefing("2026-08-31", since=self.start)

        next_day = self.run_briefing("2026-09-01")

        self.assertEqual(next_day["previousSourceMainSha"], source)
        self.assertEqual(next_day["sections"]["research"], [])
        self.assertEqual(next_day["asOf"]["research"], "2026-08-31")

    def test_a_metals_bar_that_lands_late_appears_the_next_day_exactly_once(self):
        day_one = self.run_briefing("2026-08-31", since=self.start)
        gold = self.world["metals"]["metals"]["GC=F"]
        gold.append({"date": "2026-08-31", "close": round(gold[-1]["close"] * 1.06, 4), "volume": 1})
        self.commit_world()

        day_two = self.run_briefing("2026-09-01")
        day_three = self.run_briefing("2026-09-02")

        self.assertEqual(day_one["sections"]["metals"], [])
        self.assertEqual([(row["metal"], row["leg"], row["asOf"]) for row in day_two["sections"]["metals"]],
                         [("黄金", "GC=F", "2026-08-31")])
        self.assertEqual(day_two["asOf"]["metals"], "2026-08-31")
        self.assertEqual(day_three["sections"]["metals"], [])

    def test_a_cursor_that_is_not_an_ancestor_fails_closed(self):
        self.git("checkout", "-q", "-b", "side")
        stray = self.commit_all("rewritten history")
        self.git("checkout", "-q", "main")
        self.commit_all("main moves on")

        with self.assertRaisesRegex(briefing.BriefingError, "not an ancestor"):
            self.run_briefing("2026-08-31", since=stray)
        self.assertFalse((self.out / "latest.json").exists())

    def test_a_missing_source_fails_closed(self):
        (self.repo / briefing.SOURCES["prices"]).unlink()
        self.commit_all("prices vanished")

        with self.assertRaisesRegex(briefing.BriefingError, "prices"):
            self.run_briefing("2026-08-31", since=self.start)

    def test_a_quiet_weekend_still_writes_an_empty_briefing(self):
        payload = self.run_briefing("2026-08-29", since=self.start)

        self.assertTrue(payload["empty"])
        self.assertEqual([row["level"] for row in payload["sections"]["currency"]], ["none"] * 4)
        self.assertEqual(json.loads((self.out / "latest.json").read_text(encoding="utf-8")), payload)
        self.assertIn("今日无重要变化", (self.out / "2026-08-29.md").read_text(encoding="utf-8"))

    def test_a_rerun_that_finds_nothing_new_leaves_the_files_alone(self):
        self.run_briefing("2026-08-31", since=self.start)
        published = (self.out / "latest.json").read_text(encoding="utf-8")
        self.commit_all("unrelated commit moves main")

        self.assertIsNone(self.run_briefing("2026-08-31"))
        self.assertEqual((self.out / "latest.json").read_text(encoding="utf-8"), published)

    def test_markdown_labels_every_number_with_its_window_and_as_of(self):
        self.world["calendar"]["entries"].append({
            "reportId": "r1", "company": "Broadcom", "expectedDate": "2026-09-02", "precision": "day",
            "status": "issuer-confirmed", "session": "after-close",
        })
        gold = self.world["metals"]["metals"]["GC=F"]
        gold.append({"date": "2026-08-31", "close": round(gold[-1]["close"] * 0.94, 4), "volume": 1})
        self.commit_world()

        self.run_briefing("2026-08-31", since=self.start)
        text = (self.out / "2026-08-31.md").read_text(encoding="utf-8")

        self.assertIn("## 金属 · as of 2026-08-31", text)
        self.assertIn("σ(90日)，GC=F @ 2026-08-31", text)
        self.assertIn("- [2σ] 黄金", text)
        self.assertIn("## 汇率 · as of 2026-08-30", text)
        self.assertIn("σ(1y)", text)
        self.assertIn("- 2026-09-02 盘后 Broadcom（issuer-confirmed）· 2 个交易日后", text)


if __name__ == "__main__":
    unittest.main()
