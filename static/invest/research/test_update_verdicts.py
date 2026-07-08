#!/usr/bin/env python3
import io
import sys
import types
import unittest
from contextlib import redirect_stdout
from datetime import date
from pathlib import Path


sys.modules.setdefault("yfinance", types.SimpleNamespace())
sys.path.insert(0, str(Path(__file__).resolve().parent))

import update_verdicts as uv


def series(*pairs):
    quotes = tuple(uv.PriceQuote(date=d, close=c) for d, c in pairs)
    return uv.BenchmarkSeries(symbol="SMH", quotes=quotes)


class BenchmarkSeriesTests(unittest.TestCase):
    def test_close_uses_nearest_prior_trading_day(self):
        smh = series((date(2026, 6, 30), 655.9), (date(2026, 7, 2), 592.3), (date(2026, 7, 6), 604.3))
        # 2026-07-04/05 are weekend — nearest prior close is 2026-07-02
        self.assertEqual(smh.close_on_or_before(date(2026, 7, 5)), 592.3)
        self.assertEqual(smh.close_on_or_before(date(2026, 7, 6)), 604.3)

    def test_close_before_series_start_raises(self):
        smh = series((date(2026, 7, 2), 592.3))
        with self.assertRaises(uv.PriceDataUnavailable):
            smh.close_on_or_before(date(2026, 6, 1))


class MigrationTests(unittest.TestCase):
    def test_legacy_seed_without_conviction_is_migration(self):
        self.assertTrue(uv.is_migration({"date": "2026-07-02", "stance": "neutral-watch", "price": 1.0}))

    def test_v2_entry_with_conviction_is_not_migration(self):
        self.assertFalse(
            uv.is_migration({"date": "2026-07-02", "stance": "cautious", "conviction": "medium", "price": 1.0})
        )


class OpenCallTests(unittest.TestCase):
    def setUp(self):
        self.smh = series((date(2026, 7, 2), 592.29), (date(2026, 7, 6), 604.30))
        self.report = {
            "id": "asml-2026",
            "stance": "neutral-watch",
            "conviction": "medium",
            "stanceHistory": [
                {"date": "2026-07-02", "stance": "neutral-watch", "conviction": "medium", "price": 1769.32}
            ],
        }
        self.price_entry = {"lastClose": 1825.07, "lastDate": "2026-07-06"}

    def test_open_call_scores_relative_to_benchmark(self):
        entry = uv.open_call_entry(self.report, self.price_entry, self.smh, date(2026, 7, 8))
        self.assertEqual(entry["changePct"], 3.2)  # (1825.07-1769.32)/1769.32
        self.assertEqual(entry["benchmarkChangePct"], 2.0)  # (604.30-592.29)/592.29
        self.assertEqual(entry["relativePct"], 1.2)
        self.assertEqual(entry["daysHeld"], 4)
        self.assertFalse(entry["stale"])

    def test_missing_price_yields_no_price_status(self):
        entry = uv.open_call_entry(self.report, None, self.smh, date(2026, 7, 8))
        self.assertEqual(entry["status"], "no-price")
        self.assertNotIn("changePct", entry)

    def test_missing_stance_history_fails_cleanly(self):
        report = {"id": "broken-2026", "stance": "constructive", "conviction": "medium"}
        with redirect_stdout(io.StringIO()), self.assertRaises(SystemExit):
            uv.open_call_entry(report, self.price_entry, self.smh, date(2026, 7, 8))


class ClosedIntervalTests(unittest.TestCase):
    def test_migration_interval_flagged_and_scored(self):
        smh = series((date(2026, 6, 22), 500.0), (date(2026, 7, 2), 592.29))
        report = {
            "id": "oklo-2026",
            "stanceHistory": [
                {"date": "2026-06-22", "stance": "high-risk-watch", "price": 58.40},
                {"date": "2026-07-02", "stance": "constructive", "conviction": "low", "price": 52.36},
            ],
        }
        intervals = uv.closed_interval_entries(report, smh)
        self.assertEqual(len(intervals), 1)
        row = intervals[0]
        self.assertTrue(row["migration"])
        self.assertEqual(row["fromStance"], "high-risk-watch")
        self.assertEqual(row["toStance"], "constructive")
        self.assertEqual(row["changePct"], -10.3)  # (52.36-58.40)/58.40
        self.assertEqual(row["benchmarkChangePct"], 18.5)  # (592.29-500)/500
        self.assertEqual(row["relativePct"], -28.8)


if __name__ == "__main__":
    unittest.main()
