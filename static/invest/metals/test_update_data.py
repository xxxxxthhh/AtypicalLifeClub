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


def sample_data():
    return {
        "metadata": {"metals": {}, "etfs": {}},
        "metals": {},
        "etfs": {
            "PPLT": [
                {"date": "2026-05-15", "close": 179.03, "volume": 0},
                {"date": "2026-05-18", "close": 17.84, "volume": 0},
            ]
        },
    }


class ApplyNewSplitsTests(unittest.TestCase):
    """A silent split lookup failure is how the 2026-05-18 splits got in."""

    def setUp(self):
        self._real = update_data.fetch_splits
        self.addCleanup(setattr, update_data, "fetch_splits", self._real)

    def stub(self, value):
        update_data.fetch_splits = lambda symbol: value

    def test_new_split_back_adjusts_only_earlier_rows(self):
        self.stub([("2026-05-18", 10.0)])
        data = sample_data()
        changed, failed = update_data.apply_new_splits(data)

        self.assertTrue(changed)
        self.assertEqual(failed, [])
        self.assertEqual([r["close"] for r in data["etfs"]["PPLT"]], [17.903, 17.84])
        self.assertEqual(data["metadata"]["lastSplitApplied"], {"PPLT": "2026-05-18"})
        self.assertEqual(data["metadata"]["splitAdjustments"][0]["rowsAdjusted"], 1)

    def test_already_applied_split_is_idempotent(self):
        self.stub([("2026-05-18", 10.0)])
        data = sample_data()
        data["metadata"]["lastSplitApplied"] = {"PPLT": "2026-05-18"}
        changed, failed = update_data.apply_new_splits(data)

        self.assertFalse(changed)
        self.assertEqual(failed, [])
        self.assertEqual([r["close"] for r in data["etfs"]["PPLT"]], [179.03, 17.84])

    def test_lookup_failure_is_reported_not_swallowed(self):
        self.stub(None)
        data = sample_data()
        changed, failed = update_data.apply_new_splits(data)

        self.assertFalse(changed)
        self.assertEqual(failed, ["PPLT"])
        self.assertEqual([r["close"] for r in data["etfs"]["PPLT"]], [179.03, 17.84])


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
