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


if __name__ == "__main__":
    unittest.main()
