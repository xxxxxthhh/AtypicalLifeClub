#!/usr/bin/env python3
from datetime import date
from pathlib import Path
import sys
import types
import unittest


sys.modules.setdefault("yfinance", types.SimpleNamespace())
sys.path.insert(0, str(Path(__file__).resolve().parent))

import update_prices


class PriceEntryTests(unittest.TestCase):
    def test_builds_ok_entry_from_latest_close_on_or_before_report_date(self):
        report = {
            "id": "nebius-2026",
            "priceSymbol": "NBIS",
            "priceAsOf": "2026-07-01",
        }
        quotes = [
            update_prices.PriceQuote(date=date(2026, 6, 30), close=200.0),
            update_prices.PriceQuote(date=date(2026, 7, 2), close=250.0),
            update_prices.PriceQuote(date=date(2026, 7, 3), close=260.0),
        ]

        entry = update_prices.build_ok_entry(report, quotes, date(2026, 7, 3), "USD")

        self.assertEqual(entry["status"], "ok")
        self.assertEqual(entry["baseDate"], "2026-06-30")
        self.assertEqual(entry["lastDate"], "2026-07-03")
        self.assertEqual(entry["changePct"], 30.0)

    def test_carried_forward_entry_updates_attempt_date_only(self):
        previous = {
            "reportId": "nebius-2026",
            "symbol": "NBIS",
            "status": "ok",
            "attemptedAt": "2026-07-01",
            "baseDate": "2026-06-30",
            "basePrice": 200.0,
            "lastDate": "2026-07-01",
            "lastClose": 210.0,
            "changePct": 5.0,
            "currency": "USD",
        }

        entry = update_prices.build_failure_entry("nebius-2026", "NBIS", date(2026, 7, 3), previous)

        self.assertEqual(entry["status"], "carried-forward")
        self.assertEqual(entry["attemptedAt"], "2026-07-03")
        self.assertEqual(entry["lastDate"], "2026-07-01")
        self.assertEqual(entry["changePct"], 5.0)

    def test_entry_is_stale_when_last_close_lags_attempt_by_more_than_limit(self):
        entry = {
            "reportId": "nebius-2026",
            "symbol": "NBIS",
            "status": "carried-forward",
            "attemptedAt": "2026-07-20",
            "lastDate": "2026-07-09",
        }

        self.assertTrue(update_prices.entry_is_stale(entry, max_age_days=10))


if __name__ == "__main__":
    unittest.main()
