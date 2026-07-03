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


if __name__ == "__main__":
    unittest.main()
