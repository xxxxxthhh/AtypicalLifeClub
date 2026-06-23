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
