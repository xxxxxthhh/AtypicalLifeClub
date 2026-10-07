#!/usr/bin/env python3
"""Regression tests for the metals daily updater."""

import math
from pathlib import Path
import sys
import tempfile
import types
import unittest


sys.modules.setdefault("yfinance", types.SimpleNamespace())
sys.path.insert(0, str(Path(__file__).resolve().parent))

import update_data


class UpsertRecordTests(unittest.TestCase):
    def test_skips_non_finite_close_without_overwriting_existing_record(self):
        history = [{"date": "2026-06-18", "close": 25.3, "volume": 119900}]

        result = update_data.upsert_record(
            history,
            {"date": "2026-06-18", "close": math.nan, "volume": 116233},
        )

        self.assertEqual(result, "skipped")
        self.assertEqual(
            history,
            [{"date": "2026-06-18", "close": 25.3, "volume": 119900}],
        )

    def test_keeps_existing_record_when_only_same_day_volume_changes(self):
        history = [{"date": "2026-06-18", "close": 25.3, "volume": 119900}]

        result = update_data.upsert_record(
            history,
            {"date": "2026-06-18", "close": 25.3, "volume": 116233},
        )

        self.assertEqual(result, "unchanged")
        self.assertEqual(
            history,
            [{"date": "2026-06-18", "close": 25.3, "volume": 119900}],
        )

    def test_updates_existing_record_when_close_changes(self):
        history = [{"date": "2026-06-18", "close": 25.3, "volume": 119900}]

        result = update_data.upsert_record(
            history,
            {"date": "2026-06-18", "close": 25.31, "volume": 116233},
        )

        self.assertEqual(result, "updated")
        self.assertEqual(
            history,
            [{"date": "2026-06-18", "close": 25.31, "volume": 116233}],
        )


class SaveDataTests(unittest.TestCase):
    def test_rejects_non_finite_numbers_when_serializing(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "historical.json"

            with self.assertRaises(ValueError):
                update_data.save_data(path, {"close": math.nan})

            self.assertFalse(path.exists())


class RefreshWindowTests(unittest.TestCase):
    def setUp(self):
        from unittest.mock import patch
        self.patch = patch
        self.data = {
            "metadata": {"metals": {"GC=F": {}}, "etfs": {"GLD": {}}, "last_updated": "old"},
            "metals": {"GC=F": [{"date": "2026-10-02", "close": 10, "volume": 1}]},
            "etfs": {"GLD": [{"date": "2026-10-02", "close": 20, "volume": 1}]},
            "current": {},
        }

    def run_main(self, responses):
        with self.patch.object(update_data, "load_data", return_value=self.data), \
             self.patch.object(update_data, "fetch_recent", side_effect=responses), \
             self.patch.object(update_data, "save_data", return_value=True) as save, \
             self.patch.object(sys, "argv", ["update_data.py"]):
            result = update_data.main()
        return result, save

    def test_backfills_missed_bars_and_keeps_source_dates_without_weekends(self):
        result, save = self.run_main([
            [{"date": day, "close": close, "volume": 1} for day, close in
             [("2026-10-02", 10), ("2026-10-05", 11), ("2026-10-06", 12)]],
            [{"date": day, "close": close, "volume": 1} for day, close in
             [("2026-10-02", 20), ("2026-10-05", 21), ("2026-10-06", 22)]],
        ])
        self.assertIsNone(result)
        save.assert_called_once()
        self.assertEqual([r["date"] for r in self.data["etfs"]["GLD"]],
                         ["2026-10-02", "2026-10-05", "2026-10-06"])
        self.assertEqual(self.data["current"]["GLD"]["date"], "2026-10-06")
        self.assertEqual(self.data["current"]["GLD"]["change"], 1)

    def test_one_symbol_source_failure_preserves_entire_snapshot(self):
        import copy
        before = copy.deepcopy(self.data)
        result, save = self.run_main([
            [{"date": "2026-10-06", "close": 12, "volume": 1}], [],
        ])
        self.assertEqual(result, 1)
        save.assert_not_called()
        self.assertEqual(self.data, before)

    def test_market_holiday_does_not_require_a_quote_dated_today(self):
        self.data["current"] = update_data.build_current(self.data)
        result, save = self.run_main([
            self.data["metals"]["GC=F"][:], self.data["etfs"]["GLD"][:],
        ])
        self.assertIsNone(result)
        save.assert_not_called()
        self.assertEqual(self.data["metadata"]["last_updated"], "old")

    def test_fetch_recent_returns_all_source_bars(self):
        from datetime import datetime
        rows = [(datetime(2026, 10, day), {"Close": 10 + day, "Volume": 100}) for day in (2, 5, 6)]
        frame = types.SimpleNamespace(empty=False, iterrows=lambda: iter(rows))
        ticker = types.SimpleNamespace(history=lambda **kwargs: frame)
        with self.patch.object(update_data.yf, "Ticker", return_value=ticker, create=True):
            records = update_data.fetch_recent("GC=F")
        self.assertEqual([row["date"] for row in records], ["2026-10-02", "2026-10-05", "2026-10-06"])

    def test_fetch_recent_rejects_partial_non_finite_window(self):
        from datetime import datetime
        rows = [(datetime(2026, 10, 5), {"Close": 10}),
                (datetime(2026, 10, 6), {"Close": math.nan})]
        frame = types.SimpleNamespace(empty=False, iterrows=lambda: iter(rows))
        ticker = types.SimpleNamespace(history=lambda **kwargs: frame)
        with self.patch.object(update_data.yf, "Ticker", return_value=ticker, create=True):
            self.assertEqual(update_data.fetch_recent("GC=F"), [])


if __name__ == "__main__":
    unittest.main()
