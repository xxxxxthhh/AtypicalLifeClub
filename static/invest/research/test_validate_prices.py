#!/usr/bin/env python3
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import sys
import unittest


sys.path.insert(0, str(Path(__file__).resolve().parent))

import validate_prices


class ValidatePricesTests(unittest.TestCase):
    def test_accepts_ok_price_entry(self):
        reports = [
            {
                "id": "nebius-2026",
                "priceSymbol": "NBIS",
            }
        ]
        data = {
            "generatedAt": "2026-07-03",
            "entries": [
                {
                    "reportId": "nebius-2026",
                    "symbol": "NBIS",
                    "status": "ok",
                    "attemptedAt": "2026-07-03",
                    "baseDate": "2026-07-01",
                    "basePrice": 200.0,
                    "lastDate": "2026-07-03",
                    "lastClose": 250.0,
                    "changePct": 25.0,
                    "currency": "USD",
                }
            ],
        }

        validate_prices.validate_prices_data(data, reports)

    def test_rejects_missing_entry_with_price_fields(self):
        reports = [{"id": "nebius-2026", "priceSymbol": "NBIS"}]
        data = {
            "generatedAt": "2026-07-03",
            "entries": [
                {
                    "reportId": "nebius-2026",
                    "symbol": "NBIS",
                    "status": "missing",
                    "attemptedAt": "2026-07-03",
                    "lastClose": 250.0,
                }
            ],
        }

        with redirect_stdout(StringIO()):
            with self.assertRaises(SystemExit):
                validate_prices.validate_prices_data(data, reports)

    def test_rejects_inconsistent_change_pct(self):
        reports = [{"id": "nebius-2026", "priceSymbol": "NBIS"}]
        data = {
            "generatedAt": "2026-07-03",
            "entries": [
                {
                    "reportId": "nebius-2026",
                    "symbol": "NBIS",
                    "status": "ok",
                    "attemptedAt": "2026-07-03",
                    "baseDate": "2026-07-01",
                    "basePrice": 200.0,
                    "lastDate": "2026-07-03",
                    "lastClose": 250.0,
                    "changePct": 5.0,
                }
            ],
        }

        with redirect_stdout(StringIO()):
            with self.assertRaises(SystemExit):
                validate_prices.validate_prices_data(data, reports)

    def test_rejects_ok_status_when_last_close_is_older_than_attempt(self):
        reports = [{"id": "sk-hynix-2026", "priceSymbol": "000660.KS"}]
        data = {
            "generatedAt": "2026-08-31",
            "entries": [
                {
                    "reportId": "sk-hynix-2026",
                    "symbol": "000660.KS",
                    "status": "ok",
                    "attemptedAt": "2026-08-31",
                    "baseDate": "2026-08-28",
                    "basePrice": 1_653_000.0,
                    "lastDate": "2026-08-28",
                    "lastClose": 1_653_000.0,
                    "changePct": 0.0,
                    "currency": "KRW",
                }
            ],
        }

        with redirect_stdout(StringIO()):
            with self.assertRaises(SystemExit):
                validate_prices.validate_prices_data(data, reports)

    def test_accepts_carried_forward_status_for_older_close(self):
        reports = [{"id": "sk-hynix-2026", "priceSymbol": "000660.KS"}]
        data = {
            "generatedAt": "2026-08-31",
            "entries": [
                {
                    "reportId": "sk-hynix-2026",
                    "symbol": "000660.KS",
                    "status": "carried-forward",
                    "attemptedAt": "2026-08-31",
                    "baseDate": "2026-08-28",
                    "basePrice": 1_653_000.0,
                    "lastDate": "2026-08-28",
                    "lastClose": 1_653_000.0,
                    "changePct": 0.0,
                    "currency": "KRW",
                }
            ],
        }

        validate_prices.validate_prices_data(data, reports)


if __name__ == "__main__":
    unittest.main()
