#!/usr/bin/env python3
import copy
import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))

import validate_verdicts as vv


def report(report_id: str) -> dict[str, vv.Json]:
    return {"id": report_id, "chainLayer": "compute", "isCurrent": True}


def price_entry(report_id: str) -> dict[str, vv.Json]:
    return {
        "reportId": report_id,
        "symbol": report_id.upper(),
        "status": "ok",
        "attemptedAt": "2026-07-08",
        "baseDate": "2026-07-02",
        "basePrice": 10.0,
        "lastDate": "2026-07-07",
        "lastClose": 12.0,
        "changePct": 20.0,
        "currency": "USD",
    }


def prices(*report_ids: str, generated_at: str = "2026-07-08") -> dict[str, vv.Json]:
    return {"generatedAt": generated_at, "entries": [price_entry(report_id) for report_id in report_ids]}


def verdict_entry(report_id: str) -> dict[str, vv.Json]:
    return {
        "reportId": report_id,
        "stance": "constructive",
        "conviction": "medium",
        "stanceDate": "2026-07-02",
        "priceAtStance": 10.0,
        "lastDate": "2026-07-07",
        "lastClose": 12.0,
        "changePct": 20.0,
        "benchmarkChangePct": 5.0,
        "relativePct": 15.0,
        "daysHeld": 5,
        "stale": False,
    }


def verdicts(entries: list[dict[str, vv.Json]], generated_at: str = "2026-07-08") -> dict[str, vv.Json]:
    return {"generatedAt": generated_at, "benchmark": "SMH", "entries": entries, "closed": []}


class ValidateVerdictsTests(unittest.TestCase):
    def test_missing_current_chain_report_warns_when_coverage_is_not_strict(self) -> None:
        warnings = vv.validate_verdicts_data(
            verdicts([verdict_entry("alpha")]),
            [report("alpha"), report("beta")],
            vv.ValidationOptions(prices=prices("alpha"), strict_coverage=False),
        )

        self.assertEqual(warnings, ["verdicts.json.entries missing current-chain reports: ['beta']"])

    def test_missing_current_chain_report_fails_when_coverage_is_strict(self) -> None:
        with redirect_stdout(io.StringIO()), self.assertRaises(SystemExit):
            vv.validate_verdicts_data(
                verdicts([verdict_entry("alpha")]),
                [report("alpha"), report("beta")],
                vv.ValidationOptions(prices=prices("alpha"), strict_coverage=True),
            )

    def test_verdicts_generated_at_must_not_lag_prices_generated_at(self) -> None:
        with redirect_stdout(io.StringIO()), self.assertRaises(SystemExit):
            vv.validate_verdicts_data(
                verdicts([verdict_entry("alpha")], generated_at="2026-07-07"),
                [report("alpha")],
                vv.ValidationOptions(prices=prices("alpha", generated_at="2026-07-08"), strict_coverage=False),
            )

    def test_scored_open_entry_must_match_price_snapshot(self) -> None:
        stale_verdict = copy.deepcopy(verdict_entry("alpha"))
        stale_verdict["lastClose"] = 11.0
        stale_verdict["changePct"] = 10.0
        stale_verdict["relativePct"] = 5.0

        with redirect_stdout(io.StringIO()), self.assertRaises(SystemExit):
            vv.validate_verdicts_data(
                verdicts([stale_verdict]),
                [report("alpha")],
                vv.ValidationOptions(prices=prices("alpha"), strict_coverage=False),
            )


if __name__ == "__main__":
    unittest.main()
