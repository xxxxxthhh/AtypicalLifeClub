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
                "priceAsOf": "2026-07-01",
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
        reports = [{"id": "sk-hynix-2026", "priceSymbol": "000660.KS", "priceAsOf": "2026-08-28"}]
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
        reports = [{"id": "sk-hynix-2026", "priceSymbol": "000660.KS", "priceAsOf": "2026-08-28"}]
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

    def test_rejects_fallback_close_even_when_change_pct_is_consistent(self):
        reports = [{"id": "seagate-2026", "priceSymbol": "STX", "priceAsOf": "2026-09-22"}]
        data = {
            "generatedAt": "2026-09-23",
            "entries": [{
                "reportId": "seagate-2026",
                "symbol": "STX",
                "status": "ok",
                "attemptedAt": "2026-09-23",
                "baseDate": "2026-09-21",
                "basePrice": 877.33,
                "lastDate": "2026-09-23",
                "lastClose": 923.86,
                "changePct": 5.3,
            }],
        }

        output = StringIO()
        with redirect_stdout(output), self.assertRaises(SystemExit):
            validate_prices.validate_prices_data(data, reports)
        self.assertIn("baseDate must match", output.getvalue())


if __name__ == "__main__":
    unittest.main()
