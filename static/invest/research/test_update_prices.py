#!/usr/bin/env python3
from datetime import date, datetime, timezone
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

    def test_marks_a_fetched_older_close_as_carried_forward(self):
        report = {
            "id": "sk-hynix-2026",
            "priceSymbol": "000660.KS",
            "priceAsOf": "2026-08-28",
        }
        quotes = [update_prices.PriceQuote(date=date(2026, 8, 28), close=1_653_000.0)]

        entry = update_prices.build_ok_entry(
            report,
            quotes,
            date(2026, 8, 31),
            "KRW",
            fresh_through=date(2026, 8, 31),
        )

        self.assertEqual(entry["status"], "carried-forward")
        self.assertEqual(entry["attemptedAt"], "2026-08-31")
        self.assertEqual(entry["lastDate"], "2026-08-28")

    def test_entry_is_stale_when_last_close_lags_attempt_by_more_than_limit(self):
        entry = {
            "reportId": "nebius-2026",
            "symbol": "NBIS",
            "status": "carried-forward",
            "attemptedAt": "2026-07-20",
            "lastDate": "2026-07-09",
        }

        self.assertTrue(update_prices.entry_is_stale(entry, max_age_days=10))


class CompletedSessionTests(unittest.TestCase):
    def setUp(self):
        self.quotes = [
            update_prices.PriceQuote(date=date(2026, 8, 27), close=100.0),
            update_prices.PriceQuote(date=date(2026, 8, 28), close=110.0),
        ]

    def test_delayed_run_drops_in_progress_korean_bar(self):
        observed_at = datetime(2026, 8, 28, 0, 56, tzinfo=timezone.utc)

        completed = update_prices.completed_quotes("000660.KS", self.quotes, observed_at)

        self.assertEqual([quote.date for quote in completed], [date(2026, 8, 27)])

    def test_same_utc_time_keeps_completed_us_session(self):
        observed_at = datetime(2026, 8, 28, 0, 56, tzinfo=timezone.utc)

        completed = update_prices.completed_quotes("CRM", self.quotes, observed_at)

        self.assertEqual([quote.date for quote in completed], [date(2026, 8, 27)])

    def test_asian_bar_is_kept_after_local_close(self):
        observed_at = datetime(2026, 8, 28, 7, 0, tzinfo=timezone.utc)

        completed = update_prices.completed_quotes("285A.T", self.quotes, observed_at)

        self.assertEqual([quote.date for quote in completed], [date(2026, 8, 27), date(2026, 8, 28)])

    def test_naive_observation_time_fails_closed(self):
        with self.assertRaisesRegex(update_prices.PriceDataUnavailable, "timezone-aware"):
            update_prices.completed_quotes("CRM", self.quotes, datetime(2026, 8, 28, 0, 56))

    def test_expected_fresh_day_uses_each_markets_local_close(self):
        observed_at = datetime(2026, 8, 31, 22, 0, tzinfo=timezone.utc)

        self.assertEqual(
            update_prices.latest_completed_calendar_day("CRM", observed_at),
            date(2026, 8, 31),
        )
        self.assertEqual(
            update_prices.latest_completed_calendar_day("000660.KS", observed_at),
            date(2026, 8, 31),
        )

    def test_expected_fresh_day_stays_on_prior_day_before_asian_close(self):
        observed_at = datetime(2026, 9, 1, 2, 0, tzinfo=timezone.utc)

        self.assertEqual(
            update_prices.latest_completed_calendar_day("000660.KS", observed_at),
            date(2026, 8, 31),
        )

    def test_entry_is_stale_when_price_status_is_missing(self):
        entry = {
            "reportId": "nebius-2026",
            "symbol": "BAD",
            "status": "missing",
            "attemptedAt": "2026-07-03",
        }

        self.assertTrue(update_prices.entry_is_stale(entry, max_age_days=10))


class PricedReportsTests(unittest.TestCase):
    """The ledger predicate: current AND priceSymbol AND priceAsOf."""

    def test_selects_chain_benchmark_and_non_chain_alike(self):
        chain = {"id": "nvidia-2026", "chainLayer": "compute", "priceSymbol": "NVDA", "priceAsOf": "2026-07-30"}
        benchmark = {"id": "smh-2026", "benchmark": True, "priceSymbol": "SMH", "priceAsOf": "2026-07-02"}
        # A plain non-chain report now qualifies; under the old
        # "(chainLayer OR benchmark)" rule it was silently excluded.
        non_chain = {"id": "netflix-2026", "priceSymbol": "NFLX", "priceAsOf": "2026-06-25"}

        selected = update_prices.priced_reports([chain, benchmark, non_chain])

        self.assertEqual([r["id"] for r in selected], ["nvidia-2026", "smh-2026", "netflix-2026"])

    def test_excludes_report_with_symbol_but_no_anchor(self):
        # build_ok_entry anchors basePrice to the last close on or before
        # priceAsOf, so a report without one can only produce a failure entry.
        report = {"id": "coinbase-2026", "priceSymbol": "COIN"}

        self.assertEqual(update_prices.priced_reports([report]), [])

    def test_excludes_report_with_anchor_but_no_symbol(self):
        report = {"id": "no-symbol-2026", "priceAsOf": "2026-07-30"}

        self.assertEqual(update_prices.priced_reports([report]), [])

    def test_excludes_blank_symbol_and_blank_anchor(self):
        blank_symbol = {"id": "blank-symbol", "priceSymbol": "   ", "priceAsOf": "2026-07-30"}
        blank_anchor = {"id": "blank-anchor", "priceSymbol": "ABC", "priceAsOf": "  "}

        self.assertEqual(update_prices.priced_reports([blank_symbol, blank_anchor]), [])

    def test_excludes_superseded_report(self):
        report = {
            "id": "old-2025",
            "isCurrent": False,
            "chainLayer": "compute",
            "priceSymbol": "OLD",
            "priceAsOf": "2025-07-30",
        }

        self.assertEqual(update_prices.priced_reports([report]), [])


if __name__ == "__main__":
    unittest.main()
