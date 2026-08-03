#!/usr/bin/env python3
from pathlib import Path
import random
import sys
import unittest


sys.path.insert(0, str(Path(__file__).resolve().parent))

import generate_feed


def report(report_id, last_update, coverage_date):
    return {
        "id": report_id,
        "lastUpdate": last_update,
        "date": coverage_date,
        "title": report_id,
        "file": f"/invest/research/{report_id}.md",
    }


def selected(reports, limit):
    ranked = sorted(reports, key=generate_feed.feed_rank, reverse=True)[:limit]
    return [entry["id"] for entry in ranked]


class FeedRankTests(unittest.TestCase):
    def test_newer_last_update_outranks_older(self):
        older = report("older", "2026-07-01", "2026-07-01")
        newer = report("newer", "2026-07-31", "2026-01-01")
        self.assertEqual(selected([older, newer], 1), ["newer"])

    def test_coverage_date_breaks_a_last_update_tie(self):
        # The batch-pass case: a refreshed old report and a new initiation share
        # lastUpdate, so the newer coverage must win rather than array position.
        refreshed = report("refreshed-old", "2026-07-31", "2026-02-01")
        initiation = report("new-initiation", "2026-07-31", "2026-07-01")
        self.assertEqual(selected([refreshed, initiation], 1), ["new-initiation"])

    def test_membership_is_stable_under_reordering(self):
        reports = [
            report(f"r{i:02d}", "2026-07-31", f"2026-{1 + i % 7:02d}-01") for i in range(30)
        ]
        baseline = selected(reports, 20)
        rng = random.Random(20260731)
        for _ in range(10):
            shuffled = reports[:]
            rng.shuffle(shuffled)
            self.assertEqual(selected(shuffled, 20), baseline)

    def test_id_breaks_a_full_tie(self):
        first = report("aaa", "2026-07-31", "2026-07-01")
        second = report("bbb", "2026-07-31", "2026-07-01")
        self.assertEqual(selected([first, second], 1), selected([second, first], 1))

    def test_missing_coverage_date_does_not_crash(self):
        dateless = {"id": "dateless", "lastUpdate": "2026-07-31"}
        dated = report("dated", "2026-07-31", "2026-07-01")
        self.assertEqual(selected([dateless, dated], 1), ["dated"])


class LiveDataTests(unittest.TestCase):
    def test_archives_are_dropped_before_live_reports(self):
        reports = generate_feed.load_reports()
        ranked = selected(reports, generate_feed.FEED_ITEM_LIMIT)
        dropped = [entry["id"] for entry in reports if entry["id"] not in ranked]
        for report_id in dropped:
            self.assertTrue(
                report_id.endswith("-pre-rerun") or report_id.endswith("-pre-chain"),
                f"the feed cut dropped a live report: {report_id}",
            )

    def test_every_live_report_ranks_above_every_archive(self):
        reports = generate_feed.load_reports()
        ranked = sorted(reports, key=generate_feed.feed_rank, reverse=True)
        live_count = sum(1 for report in reports if report.get("isCurrent") is not False)

        self.assertTrue(any(report.get("isCurrent") is False for report in reports))
        self.assertTrue(all(report.get("isCurrent") is not False for report in ranked[:live_count]))
        self.assertTrue(all(report.get("isCurrent") is False for report in ranked[live_count:]))

    def test_committed_book_fits_under_the_cap(self):
        self.assertLessEqual(len(generate_feed.load_reports()), generate_feed.FEED_ITEM_LIMIT)


if __name__ == "__main__":
    unittest.main()
