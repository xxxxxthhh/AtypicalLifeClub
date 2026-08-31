#!/usr/bin/env python3
"""Regression tests for metals data validation."""

import math
from pathlib import Path
import sys
from contextlib import redirect_stdout
from io import StringIO
import unittest


sys.path.insert(0, str(Path(__file__).resolve().parent))

import validate_data


def history(*closes):
    """Build a minimal ascending history from 2026-05-15."""
    days = ["2026-05-15", "2026-05-18", "2026-05-19"]
    return [{"date": d, "close": c, "volume": 0} for d, c in zip(days, closes)]


class ContinuityValidationTests(unittest.TestCase):
    """The 2026-05-18 PPLT/PALL splits passed every pre-existing check."""

    def test_undeclared_jump_fails(self):
        with redirect_stdout(StringIO()):
            with self.assertRaises(SystemExit):
                validate_data.validate_continuity(
                    history(179.03, 17.90, 17.42), "PPLT", {}, "etfs"
                )

    def test_declared_jump_passes(self):
        known = {("PPLT", "2026-05-18"): 10.0}
        with redirect_stdout(StringIO()):
            validate_data.validate_continuity(
                history(179.03, 17.90, 17.42), "PPLT", known, "etfs"
            )

    def test_ordinary_move_passes(self):
        with redirect_stdout(StringIO()):
            validate_data.validate_continuity(
                history(17.90, 17.42, 17.84), "PPLT", {}, "etfs"
            )

    def test_whitelist_is_symbol_and_date_specific(self):
        """A split declared for another symbol must not silence this one."""
        known = {("PALL", "2026-05-18"): 5.0}
        with redirect_stdout(StringIO()):
            with self.assertRaises(SystemExit):
                validate_data.validate_continuity(
                    history(179.03, 17.90, 17.42), "PPLT", known, "etfs"
                )


class KnownSplitsMetadataTests(unittest.TestCase):
    VALID = {"symbol": "PPLT", "date": "2026-05-18", "ratio": 10.0, "reason": "verified 10:1 forward split"}

    def test_valid_entry_parses(self):
        with redirect_stdout(StringIO()):
            known = validate_data.parse_known_splits({"knownSplits": [dict(self.VALID)]})
        self.assertEqual(known, {("PPLT", "2026-05-18"): 10.0})

    def test_missing_ratio_fails(self):
        entry = dict(self.VALID)
        del entry["ratio"]
        with redirect_stdout(StringIO()):
            with self.assertRaises(SystemExit):
                validate_data.parse_known_splits({"knownSplits": [entry]})

    def test_malformed_date_fails(self):
        entry = dict(self.VALID, date="2026-5-18")
        with redirect_stdout(StringIO()):
            with self.assertRaises(SystemExit):
                validate_data.parse_known_splits({"knownSplits": [entry]})

    def test_blank_reason_fails(self):
        """A whitelist entry without a stated reason is a mute switch."""
        entry = dict(self.VALID, reason="   ")
        with redirect_stdout(StringIO()):
            with self.assertRaises(SystemExit):
                validate_data.parse_known_splits({"knownSplits": [entry]})


class NumericValidationTests(unittest.TestCase):
    def test_rejects_nan_values(self):
        with redirect_stdout(StringIO()):
            with self.assertRaises(SystemExit):
                validate_data.assert_numeric(math.nan, "row.close")

    def test_rejects_infinite_values(self):
        with redirect_stdout(StringIO()):
            with self.assertRaises(SystemExit):
                validate_data.assert_numeric(math.inf, "row.close")


if __name__ == "__main__":
    unittest.main()
