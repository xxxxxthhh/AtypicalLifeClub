#!/usr/bin/env python3
"""Unit tests for the quarterly-note data appendix generator (v6 spec §3.3).

The appendix is the only place the "breached but never re-adjudicated" question is
answered in prose form, so its selection rule is pinned here against the same two
cases as the ledger page's Trigger Watch section, plus the dating and determinism
guarantees that make the output safe to paste into a human-authored note.
"""
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from datetime import date
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))

import generate_calibration_note as gcn


AS_OF = date(2026, 4, 15)


def chain_report(**overrides):
    report = {
        "id": "fixture-2026",
        "chainLayer": "power",
        "stance": "constructive",
        "conviction": "medium",
        "stanceHistory": [{"stance": "constructive", "conviction": "medium", "date": "2026-01-10", "price": 10}],
        "stanceTriggers": {"downgrade": {"zh": "zh", "en": "en", "monitoringIds": ["linked-item"]}},
        "monitoring": [
            {"id": "linked-item", "metric": {"zh": "指标", "en": "Metric"},
             "reading": "breached", "readingAsOf": "2026-04-08"}
        ],
    }
    report.update(overrides)
    return report


class BreachedWithoutFlipTests(unittest.TestCase):
    def test_breached_with_unchanged_stance_is_listed(self):
        rows = gcn.breached_without_flip([chain_report()], AS_OF)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["reportId"], "fixture-2026")
        self.assertEqual(rows[0]["readingAsOf"], "2026-04-08")
        self.assertEqual(rows[0]["daysSinceBreach"], 7)
        self.assertEqual(rows[0]["metrics"], ["linked-item"])

    def test_stance_changed_after_reading_clears_the_row(self):
        report = chain_report(
            stance="cautious",
            stanceHistory=[
                {"stance": "constructive", "conviction": "medium", "date": "2026-01-10", "price": 10},
                {"stance": "cautious", "conviction": "medium", "date": "2026-04-09", "price": 9},
            ],
        )
        self.assertEqual(gcn.breached_without_flip([report], AS_OF), [])

    def test_stance_dated_on_the_reading_day_still_lists(self):
        report = chain_report(
            stanceHistory=[{"stance": "constructive", "conviction": "medium", "date": "2026-04-08", "price": 10}]
        )
        self.assertEqual(len(gcn.breached_without_flip([report], AS_OF)), 1)

    def test_unlinked_breached_item_is_not_watched(self):
        report = chain_report(
            stanceTriggers={"downgrade": {"zh": "zh", "en": "en", "monitoringIds": ["other-item"]}},
            monitoring=[
                {"id": "other-item", "metric": {"en": "Other"}},
                {"id": "linked-item", "metric": {"en": "Metric"},
                 "reading": "breached", "readingAsOf": "2026-04-08"},
            ],
        )
        self.assertEqual(gcn.breached_without_flip([report], AS_OF), [])

    def test_within_and_ungraded_are_not_listed(self):
        within = chain_report(
            monitoring=[{"id": "linked-item", "metric": {"en": "M"},
                         "reading": "within", "readingAsOf": "2026-04-08"}]
        )
        ungraded = chain_report(id="ungraded-2026", monitoring=[{"id": "linked-item", "metric": {"en": "M"}}])
        self.assertEqual(gcn.breached_without_flip([within, ungraded], AS_OF), [])

    def test_rows_sort_longest_standing_breach_first(self):
        older = chain_report(
            id="older-2026",
            monitoring=[{"id": "linked-item", "metric": {"en": "M"},
                         "reading": "breached", "readingAsOf": "2026-03-01"}],
        )
        rows = gcn.breached_without_flip([chain_report(id="newer-2026"), older], AS_OF)
        self.assertEqual([row["reportId"] for row in rows], ["older-2026", "newer-2026"])

    def test_the_shipped_book_has_no_breached_without_flip(self):
        reports = json.loads(gcn.REPORTS_JSON.read_text(encoding="utf-8"))
        chain = [r for r in reports if gcn.is_current_chain_report(r)]
        self.assertEqual(gcn.breached_without_flip(chain, AS_OF), [])


class ScoredCallTests(unittest.TestCase):
    VERDICTS = {
        "generatedAt": "2026-04-15",
        "entries": [
            {"reportId": "a-2026", "stance": "constructive", "relativePct": 4.0, "benchmarkSymbol": "SMH"},
            {"reportId": "b-2026", "stance": "cautious", "status": "pending", "benchmarkSymbol": "XLU"},
        ],
        "closed": [
            {"reportId": "c-2026", "fromStance": "neutral-watch", "relativePct": -2.0,
             "benchmarkSymbol": "SMH", "startDate": "2026-01-01", "endDate": "2026-02-01"},
            {"reportId": "d-2026", "fromStance": "cautious", "relativePct": 9.9,
             "benchmarkSymbol": "SMH", "migration": True,
             "startDate": "2026-01-01", "endDate": "2026-02-01"},
        ],
    }

    def test_pending_and_migration_rows_are_excluded(self):
        calls = gcn.scored_calls(self.VERDICTS)
        self.assertEqual([c["reportId"] for c in calls], ["a-2026", "c-2026"])

    def test_bucket_order_puts_the_book_default_first(self):
        symbols = sorted(["XLU", "SMH", "COPX"], key=gcn.bucket_sort_key)
        self.assertEqual(symbols, ["SMH", "COPX", "XLU"])


class RenderTests(unittest.TestCase):
    BENCHMARKS = {"default": "SMH", "layerDefaults": {}, "symbols": {"SMH": {"name": {"en": "Semis"}}}}

    def render(self, reports, verdicts):
        return gcn.render(reports, verdicts, self.BENCHMARKS)

    def test_appendix_is_dated_from_verdicts_not_today(self):
        text = self.render([chain_report()], {"generatedAt": "2026-04-15", "entries": [], "closed": []})
        self.assertIn("data appendix (2026-04-15)", text)

    def test_output_is_deterministic(self):
        reports = [chain_report(id="b-2026"), chain_report(id="a-2026")]
        verdicts = {"generatedAt": "2026-04-15", "entries": [], "closed": []}
        first = self.render(reports, verdicts)
        second = self.render(list(reversed(reports)), verdicts)
        self.assertEqual(first, second)

    def test_empty_breach_list_renders_as_the_healthy_state(self):
        report = chain_report(monitoring=[{"id": "linked-item", "metric": {"en": "M"}}])
        text = self.render([report], {"generatedAt": "2026-04-15", "entries": [], "closed": []})
        self.assertIn("None. (Empty is the healthy state", text)

    def test_no_conclusions_or_recommendations_are_emitted(self):
        # The generator produces data only; the human writes the conclusions section.
        text = self.render([chain_report()], {"generatedAt": "2026-04-15", "entries": [], "closed": []})
        lowered = text.lower()
        for banned in ("we recommend", "conclusion:", "should buy", "should sell"):
            self.assertNotIn(banned, lowered)

    def test_pipes_in_rationale_are_escaped(self):
        report = chain_report(
            benchmarkSymbol="URA",
            benchmarkRationale={"en": "a | b", "zh": "甲 | 乙"},
        )
        text = self.render([report], {"generatedAt": "2026-04-15", "entries": [], "closed": []})
        self.assertIn("a \\| b", text)


class InputValidationTests(unittest.TestCase):
    def load_verdicts_from(self, payload):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "verdicts.json"
            path.write_text(payload, encoding="utf-8")
            original = gcn.VERDICTS_JSON
            gcn.VERDICTS_JSON = path
            try:
                return gcn.load_verdicts()
            finally:
                gcn.VERDICTS_JSON = original

    def expect_fail(self, payload):
        with redirect_stdout(io.StringIO()), self.assertRaises(SystemExit):
            self.load_verdicts_from(payload)

    def test_missing_generated_at_fails(self):
        self.expect_fail(json.dumps({"entries": [], "closed": []}))

    def test_malformed_generated_at_fails(self):
        self.expect_fail(json.dumps({"generatedAt": "31-07-2026"}))

    def test_non_object_verdicts_fails(self):
        self.expect_fail("[]")

    def test_invalid_json_fails(self):
        self.expect_fail("{not json")

    def test_valid_payload_loads(self):
        loaded = self.load_verdicts_from(json.dumps({"generatedAt": "2026-04-15"}))
        self.assertEqual(loaded["generatedAt"], "2026-04-15")


if __name__ == "__main__":
    unittest.main()
