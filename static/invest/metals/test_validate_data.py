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


class SplitMagnitudeTests(unittest.TestCase):
    """A whitelist entry declares a magnitude, not an exemption.

    Every close below is the real PPLT/PALL series around the 2026-05-18 splits:
    back-adjusted as committed, raw as Yahoo served it, and double-adjusted as
    reproduced by deleting metadata.lastSplitApplied and re-running the updater.
    """

    PPLT = {("PPLT", "2026-05-18"): 10.0}
    PALL = {("PALL", "2026-05-18"): 5.0}

    def assert_fails_on_magnitude(self, closes, symbol, known):
        """Fail, and fail *because* the move contradicts the declared ratio."""
        captured = StringIO()
        with redirect_stdout(captured):
            with self.assertRaises(SystemExit):
                validate_data.validate_continuity(history(*closes), symbol, known, "etfs")
        self.assertIn("对不上", captured.getvalue())
        return captured.getvalue()

    def test_back_adjusted_history_passes(self):
        """The committed state: the jump is already gone, the entry sits inert."""
        with redirect_stdout(StringIO()):
            validate_data.validate_continuity(
                history(17.903, 17.84, 17.42), "PPLT", self.PPLT, "etfs"
            )

    def test_raw_split_jump_at_declared_ratio_passes(self):
        """Un-back-adjusted history: -90.04%, exactly what 10:1 predicts."""
        with redirect_stdout(StringIO()):
            validate_data.validate_continuity(
                history(179.03, 17.84, 17.42), "PPLT", self.PPLT, "etfs"
            )

    def test_double_adjusted_jump_fails(self):
        """The hole this closes: +896.48% waved through by a whitelisted date."""
        message = self.assert_fails_on_magnitude((1.7903, 17.84, 17.42), "PPLT", self.PPLT)
        self.assertIn("896.5%", message)

    def test_double_adjusted_jump_fails_for_pall(self):
        """Same defect at a different ratio: 5:1 double-adjusted is +396.43%."""
        self.assert_fails_on_magnitude((5.1508, 25.57, 24.55), "PALL", self.PALL)

    def test_wrong_magnitude_for_declared_ratio_fails(self):
        """Declared 10:1, but the data jumped by 5:1 (-80.1%). Not explained."""
        self.assert_fails_on_magnitude((89.515, 17.84, 17.42), "PPLT", self.PPLT)

    def test_reverse_split_is_handled_symmetrically(self):
        """ratio < 1 (a 1:10 reverse split) multiplies instead of divides."""
        with redirect_stdout(StringIO()):
            validate_data.validate_continuity(
                history(1.7903, 17.903, 17.42), "PPLT", {("PPLT", "2026-05-18"): 0.1}, "etfs"
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
