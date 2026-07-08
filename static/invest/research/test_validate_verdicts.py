#!/usr/bin/env python3
import copy
import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))

import validate_verdicts as vv


TEST_BENCHMARKS = {
    "default": "SMH",
    "layerDefaults": {"power": "XLU", "resources": "COPX"},
    "symbols": {"SMH": {}, "XLU": {}, "COPX": {}},
}


def report(report_id: str, **overrides) -> dict[str, vv.Json]:
    base = {"id": report_id, "chainLayer": "compute", "isCurrent": True}
    base.update(overrides)
    return base


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


def verdict_entry(report_id: str, benchmark_symbol: str = "SMH") -> dict[str, vv.Json]:
    return {
        "reportId": report_id,
        "stance": "constructive",
        "conviction": "medium",
        "stanceDate": "2026-07-02",
        "priceAtStance": 10.0,
        "benchmarkSymbol": benchmark_symbol,
        "lastDate": "2026-07-07",
        "lastClose": 12.0,
        "changePct": 20.0,
        "benchmarkChangePct": 5.0,
        "relativePct": 15.0,
        "bookBenchmarkSymbol": "SMH",
        "bookBenchmarkChangePct": 5.0,
        "bookRelativePct": 15.0,
        "daysHeld": 5,
        "stale": False,
    }


def closed_entry(report_id: str, benchmark_symbol: str, migration: bool) -> dict[str, vv.Json]:
    return {
        "reportId": report_id,
        "fromStance": "high-risk-watch" if migration else "cautious",
        "toStance": "cautious",
        "toConviction": "medium",
        "startDate": "2026-06-22",
        "startPrice": 100.0,
        "endDate": "2026-07-02",
        "endPrice": 110.0,
        "changePct": 10.0,
        "benchmarkChangePct": 4.0,
        "relativePct": 6.0,
        "bookBenchmarkSymbol": "SMH",
        "bookBenchmarkChangePct": 4.0,
        "bookRelativePct": 6.0,
        "daysHeld": 10,
        "migration": migration,
        "benchmarkSymbol": benchmark_symbol,
    }


def verdicts(entries, closed=None, generated_at: str = "2026-07-08") -> dict[str, vv.Json]:
    return {"generatedAt": generated_at, "benchmark": "SMH", "entries": entries, "closed": closed or []}


def options(prices_data, reports_list, strict=False):
    return vv.ValidationOptions(
        prices=prices_data,
        strict_coverage=strict,
        benchmarks=TEST_BENCHMARKS,
        reports_by_id={r["id"]: r for r in reports_list},
    )


def expect_fail(test, data, reports_list, opts):
    with redirect_stdout(io.StringIO()), test.assertRaises(SystemExit):
        vv.validate_verdicts_data(data, reports_list, opts)


class CoverageTests(unittest.TestCase):
    def test_missing_current_chain_report_warns_when_coverage_is_not_strict(self):
        reports = [report("alpha"), report("beta")]
        warnings = vv.validate_verdicts_data(
            verdicts([verdict_entry("alpha")]), reports, options(prices("alpha"), reports)
        )
        self.assertEqual(warnings, ["verdicts.json.entries missing current-chain reports: ['beta']"])

    def test_missing_current_chain_report_fails_when_coverage_is_strict(self):
        reports = [report("alpha"), report("beta")]
        expect_fail(self, verdicts([verdict_entry("alpha")]), reports, options(prices("alpha"), reports, strict=True))

    def test_verdicts_generated_at_must_not_lag_prices(self):
        reports = [report("alpha")]
        expect_fail(
            self,
            verdicts([verdict_entry("alpha")], generated_at="2026-07-07"),
            reports,
            options(prices("alpha", generated_at="2026-07-08"), reports),
        )

    def test_scored_open_entry_must_match_price_snapshot(self):
        reports = [report("alpha")]
        stale = copy.deepcopy(verdict_entry("alpha"))
        stale["lastClose"] = 11.0
        stale["changePct"] = 10.0
        stale["relativePct"] = 5.0
        stale["bookRelativePct"] = 5.0
        expect_fail(self, verdicts([stale]), reports, options(prices("alpha"), reports))

    def test_scored_open_entry_requires_book_level_smh_reference(self):
        reports = [report("nrg", chainLayer="power", priceSymbol="NRG")]
        missing = copy.deepcopy(verdict_entry("nrg", "XLU"))
        del missing["bookRelativePct"]
        expect_fail(self, verdicts([missing]), reports, options(prices("nrg"), reports))

    def test_book_level_relative_must_match_book_benchmark(self):
        reports = [report("nrg", chainLayer="power", priceSymbol="NRG")]
        broken = copy.deepcopy(verdict_entry("nrg", "XLU"))
        broken["bookBenchmarkChangePct"] = 9.0
        broken["bookRelativePct"] = 15.0
        expect_fail(self, verdicts([broken]), reports, options(prices("nrg"), reports))


class BenchmarkSymbolTests(unittest.TestCase):
    def test_override_symbol_passes_when_it_matches_resolution(self):
        # copx-style: priceSymbol COPX + resources layer, but overridden to SMH.
        reports = [report("copx", chainLayer="resources", priceSymbol="COPX", benchmarkSymbol="SMH")]
        warnings = vv.validate_verdicts_data(
            verdicts([verdict_entry("copx", "SMH")]), reports, options(prices("copx"), reports)
        )
        self.assertEqual(warnings, [])

    def test_self_benchmark_is_rejected(self):
        # No override: resources layer default COPX == its own priceSymbol → banned.
        reports = [report("selfhit", chainLayer="resources", priceSymbol="COPX")]
        expect_fail(self, verdicts([verdict_entry("selfhit", "COPX")]), reports, options(prices("selfhit"), reports))

    def test_benchmark_symbol_must_match_resolution(self):
        # Entry claims XLU but a compute report resolves to SMH.
        reports = [report("alpha")]
        expect_fail(self, verdicts([verdict_entry("alpha", "XLU")]), reports, options(prices("alpha"), reports))

    def test_migration_interval_grandfathered_to_smh_passes(self):
        # Power report resolves to XLU, but its migration closed interval is SMH — OK.
        reports = [report("nrg", chainLayer="power", priceSymbol="NRG")]
        warnings = vv.validate_verdicts_data(
            verdicts([verdict_entry("nrg", "XLU")], closed=[closed_entry("nrg", "SMH", migration=True)]),
            reports,
            options(prices("nrg"), reports),
        )
        self.assertEqual(warnings, [])

    def test_migration_interval_on_layer_benchmark_is_rejected(self):
        # A migration interval must be grandfathered to SMH, not the layer benchmark.
        reports = [report("nrg", chainLayer="power", priceSymbol="NRG")]
        expect_fail(
            self,
            verdicts([verdict_entry("nrg", "XLU")], closed=[closed_entry("nrg", "XLU", migration=True)]),
            reports,
            options(prices("nrg"), reports),
        )

    def test_real_flip_uses_layer_benchmark(self):
        # A non-migration closed interval scores vs the report's resolved benchmark.
        reports = [report("nrg", chainLayer="power", priceSymbol="NRG")]
        warnings = vv.validate_verdicts_data(
            verdicts([verdict_entry("nrg", "XLU")], closed=[closed_entry("nrg", "XLU", migration=False)]),
            reports,
            options(prices("nrg"), reports),
        )
        self.assertEqual(warnings, [])


if __name__ == "__main__":
    unittest.main()
