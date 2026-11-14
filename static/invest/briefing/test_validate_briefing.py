#!/usr/bin/env python3
import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_briefing import validate_markdown, validate_payload


def payload():
    return {
        "date": "2026-08-31",
        "generatedAt": "2026-08-31T02:47:12Z",
        "sourceMainSha": "a" * 40,
        "previousSourceMainSha": "b" * 40,
        "empty": False,
        "asOf": {"currency": "2026-08-29", "metals": "2026-08-28", "prices": "2026-08-28", "research": "2026-08-31"},
        "sections": {
            "research": [{"kind": "signal", "ticker": "MRVL", "text": "标题", "url": None, "evidenceDate": "2026-08-26"}],
            "earnings": [{"date": "2026-09-02", "company": "Broadcom", "session": "after-close",
                          "status": "issuer-confirmed", "tradingDaysAway": 2}],
            "metals": [{"metal": "钯金", "leg": "PA=F", "price": 1428.6, "changePct": 6.8, "z": 2.67,
                        "window": 90, "level": "alert", "asOf": "2026-08-28"}],
            "currency": [{"pair": "USD/CNY", "rate": 6.7285, "z": -1.43, "window": 365, "level": "none",
                          "asOf": "2026-08-29"}],
        },
    }


def quiet():
    data = payload()
    data["empty"] = True
    data["sections"].update(research=[], earnings=[], metals=[])
    return data


class ValidatePayloadTests(unittest.TestCase):
    def assert_rejected(self, data, fragment):
        errors = validate_payload(data)
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_accepts_a_full_and_a_quiet_briefing(self):
        self.assertEqual(validate_payload(payload()), [])
        self.assertEqual(validate_payload(quiet()), [])

    def test_cursor_shas_are_required_and_full_length(self):
        data = payload()
        del data["previousSourceMainSha"]
        self.assert_rejected(data, "missing field: previousSourceMainSha")
        data = payload()
        data["sourceMainSha"] = "abc1234"
        self.assert_rejected(data, "sourceMainSha must be a 40-character commit SHA")

    def test_every_section_needs_its_own_as_of(self):
        data = payload()
        del data["asOf"]["metals"]
        self.assert_rejected(data, "asOf must have exactly")
        data = payload()
        data["asOf"]["research"] = "08-31"
        self.assert_rejected(data, "asOf.research must be YYYY-MM-DD")

    def test_undeclared_fields_cannot_ride_along(self):
        data = payload()
        data["deferredOpenItems"] = [{"id": "P-9", "title": "ALAB 权证冲减收入 2.60%"}]
        self.assert_rejected(data, "undeclared field: deferredOpenItems")
        data = payload()
        data["sections"]["research"][0]["decisionNeeded"] = "…"
        self.assert_rejected(data, "undeclared field decisionNeeded")

    def test_open_item_count_is_a_bare_count_or_absent(self):
        data = payload()
        data["openItemCount"] = 12
        self.assertEqual(validate_payload(data), [])
        for bad in (-1, "12", True, None):
            data["openItemCount"] = bad
            self.assert_rejected(data, "openItemCount must be a non-negative integer")

    def test_empty_must_agree_with_the_sections(self):
        data = payload()
        data["empty"] = True
        self.assert_rejected(data, "empty must be true exactly when")
        data = quiet()
        data["empty"] = False
        self.assert_rejected(data, "empty must be true exactly when")

    def test_a_flagged_currency_pair_makes_the_day_not_empty(self):
        data = quiet()
        data["sections"]["currency"][0]["level"] = "warning"
        self.assert_rejected(data, "empty must be true exactly when")
        data["empty"] = False
        self.assertEqual(validate_payload(data), [])

    def test_levels_and_windows_are_pinned_per_section(self):
        data = payload()
        data["sections"]["metals"][0]["level"] = "warning"
        self.assert_rejected(data, "sections.metals[0].level")
        data = payload()
        data["sections"]["metals"][0]["window"] = 62
        self.assert_rejected(data, "sections.metals[0].window must be 90")
        data = payload()
        data["sections"]["currency"][0]["level"] = "red"
        self.assert_rejected(data, "sections.currency[0].level")

    def test_rows_need_every_field_with_the_right_type(self):
        data = payload()
        del data["sections"]["currency"][0]["asOf"]
        self.assert_rejected(data, "sections.currency[0] missing asOf")
        data = payload()
        data["sections"]["metals"][0]["z"] = "2.67"
        self.assert_rejected(data, "sections.metals[0].z has the wrong type")
        data = payload()
        data["sections"]["earnings"][0]["tradingDaysAway"] = True
        self.assert_rejected(data, "sections.earnings[0].tradingDaysAway has the wrong type")

    def test_all_four_sections_must_be_present(self):
        data = copy.deepcopy(payload())
        del data["sections"]["earnings"]
        self.assert_rejected(data, "sections must have exactly")


class ValidateMarkdownTests(unittest.TestCase):
    def test_neutral_markers_pass(self):
        self.assertEqual(validate_markdown("- [2σ] 黄金 408.89（-3.24%）\n- [1.5σ] USD/CNY"), [])

    def test_judgment_lights_are_rejected(self):
        self.assertTrue(validate_markdown("🔴 黄金 -3.38%"))
        self.assertTrue(validate_markdown("🟡 USD/CNY"))


if __name__ == "__main__":
    unittest.main()
