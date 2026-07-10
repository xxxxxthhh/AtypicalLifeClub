#!/usr/bin/env python3
"""v6 benchmark-config and per-report override validation (docs/research-hub-v6-plan.md §2.1).

The happy-path override+rationale case is covered by the integration run of
validate_reports.py against the real reports.json (copx-2026 / vertiv-2026); these
unit tests pin the failure modes, which exit inside the benchmark block before the
unrelated enrichment checks run.
"""
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))

import validate_reports as vr


TEST_BENCHMARKS = {
    "default": "SMH",
    "layerDefaults": {"power": "XLU", "resources": "COPX"},
    "symbols": {
        "SMH": {"name": {"zh": "半导体", "en": "Semis"}},
        "XLU": {"name": {"zh": "公用事业", "en": "Utilities"}},
        "COPX": {"name": {"zh": "铜矿", "en": "Copper"}},
    },
}

BILINGUAL = {"zh": "理由", "en": "reason"}


def expect_fail(test, fn):
    with redirect_stdout(io.StringIO()), test.assertRaises(SystemExit):
        fn()


def capture_fail(test, fn):
    output = io.StringIO()
    with redirect_stdout(output), test.assertRaises(SystemExit):
        fn()
    return output.getvalue()


class ModuleContractValidationTests(unittest.TestCase):
    def assert_contract_failure(self, heading, reason):
        with tempfile.TemporaryDirectory() as temp_dir:
            markdown_file = Path(temp_dir) / "fixture.md"
            markdown_file.write_text(
                "# Test report\n\n" + heading + "\nBody.\n",
                encoding="utf-8",
            )
            output = capture_fail(
                self,
                lambda: vr.validate_module_contract(
                    markdown_file,
                    "heading-comment-v1",
                    "report[0].markdownFiles.en",
                ),
            )

        self.assertIn("fixture.md:3", output)
        self.assertIn(reason, output)

    def test_valid_h2_markers_pass(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            markdown_file = Path(temp_dir) / "fixture.md"
            markdown_file.write_text(
                "# Test report\n\n"
                "## Durable economics <!-- report-module:business -->\n"
                "Body.\n\n"
                "### Valuation vocabulary stays inherited\n"
                "Nested body.\n",
                encoding="utf-8",
            )

            vr.validate_module_contract(
                markdown_file,
                "heading-comment-v1",
                "report[0].markdownFiles.en",
            )

    def test_missing_marker_fails_with_file_and_line(self):
        self.assert_contract_failure("## Durable economics", "missing")

    def test_duplicate_marker_fails_with_file_and_line(self):
        self.assert_contract_failure(
            "## Durable economics <!-- report-module:business --> <!-- report-module:financial -->",
            "duplicate",
        )

    def test_malformed_marker_fails_with_file_and_line(self):
        self.assert_contract_failure(
            "## Durable economics <!-- report-module: business -->",
            "malformed",
        )

    def test_unknown_marker_fails_with_file_and_line(self):
        self.assert_contract_failure(
            "## Durable economics <!-- report-module:operations -->",
            "unknown",
        )


class BenchmarksConfigTests(unittest.TestCase):
    def test_valid_config_passes(self):
        vr.validate_benchmarks_config(TEST_BENCHMARKS)  # no raise

    def test_missing_default_fails(self):
        cfg = {"layerDefaults": {}, "symbols": {"SMH": {"name": {"zh": "x", "en": "y"}}}}
        expect_fail(self, lambda: vr.validate_benchmarks_config(cfg))

    def test_layer_default_symbol_must_be_defined(self):
        cfg = {
            "default": "SMH",
            "layerDefaults": {"power": "XLU"},
            "symbols": {"SMH": {"name": {"zh": "x", "en": "y"}}},  # XLU missing
        }
        expect_fail(self, lambda: vr.validate_benchmarks_config(cfg))


class OverrideValidationTests(unittest.TestCase):
    def test_override_differs_from_default_without_rationale_fails(self):
        # resources default is COPX; override SMH differs → rationale required.
        report = {"id": "copx-2026", "chainLayer": "resources", "isCurrent": True, "benchmarkSymbol": "SMH"}
        expect_fail(self, lambda: vr.validate_enrichment_fields(report, 0, {}, TEST_BENCHMARKS))

    def test_unknown_override_symbol_fails(self):
        report = {"id": "x-2026", "chainLayer": "power", "isCurrent": True, "benchmarkSymbol": "ZZZ"}
        expect_fail(self, lambda: vr.validate_enrichment_fields(report, 0, {}, TEST_BENCHMARKS))

    def test_override_on_non_chain_report_fails(self):
        report = {"id": "x-2026", "isCurrent": True, "benchmarkSymbol": "SMH"}  # no chainLayer
        expect_fail(self, lambda: vr.validate_enrichment_fields(report, 0, {}, TEST_BENCHMARKS))

    def test_rationale_without_override_fails(self):
        report = {"id": "x-2026", "chainLayer": "compute", "isCurrent": True, "benchmarkRationale": BILINGUAL}
        expect_fail(self, lambda: vr.validate_enrichment_fields(report, 0, {}, TEST_BENCHMARKS))


if __name__ == "__main__":
    unittest.main()
