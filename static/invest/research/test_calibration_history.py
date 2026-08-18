#!/usr/bin/env python3
import copy
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))

import calibration_history as ch


def open_entry(report_id, stance, benchmark_symbol, relative_pct, book_relative_pct):
    return {
        "reportId": report_id,
        "stance": stance,
        "benchmarkSymbol": benchmark_symbol,
        "relativePct": relative_pct,
        "bookBenchmarkSymbol": "SMH",
        "bookRelativePct": book_relative_pct,
    }


def closed_entry(report_id, from_stance, benchmark_symbol, relative_pct, book_relative_pct):
    return {
        "reportId": report_id,
        "fromStance": from_stance,
        "toStance": "neutral-watch",
        "benchmarkSymbol": benchmark_symbol,
        "relativePct": relative_pct,
        "bookBenchmarkSymbol": "SMH",
        "bookRelativePct": book_relative_pct,
        "migration": False,
    }


def verdicts():
    return {
        "generatedAt": "2026-07-08",
        "benchmark": "SMH",
        "entries": [
            open_entry("alpha", "constructive", "SMH", 4.0, 4.0),
            open_entry("beta", "cautious", "XLU", 2.0, -1.0),
            {"reportId": "pending", "stance": "constructive", "status": "pending"},
        ],
        "closed": [
            closed_entry("gamma", "bearish-avoid", "XLU", 3.0, -2.0),
            {
                "reportId": "migration",
                "fromStance": "high-risk-watch",
                "benchmarkSymbol": "SMH",
                "relativePct": 8.0,
                "migration": True,
            },
        ],
    }


class CalibrationSnapshotTests(unittest.TestCase):
    def test_snapshot_uses_book_level_smh_topline_and_bucket_relative_metrics(self):
        snapshot = ch.build_snapshot(verdicts())

        self.assertEqual(snapshot["date"], "2026-07-08")
        self.assertEqual(snapshot["scoredCount"], 3)
        self.assertEqual(snapshot["medianRelativePct"], -1.0)
        self.assertEqual(snapshot["nonNeutralBeatRate"], 1 / 3)
        self.assertEqual(snapshot["byBenchmark"]["SMH"]["medianRelativePct"], 4.0)
        self.assertEqual(snapshot["byBenchmark"]["SMH"]["nonNeutralBeatRate"], 1.0)
        self.assertEqual(snapshot["byBenchmark"]["XLU"]["scoredCount"], 2)
        self.assertEqual(snapshot["byBenchmark"]["XLU"]["medianRelativePct"], 2.5)
        self.assertEqual(snapshot["byBenchmark"]["XLU"]["nonNeutralBeatRate"], 1.0)
        self.assertEqual(snapshot["byBenchmark"]["XLU"]["byStance"]["cautious"]["medianRelativePct"], 2.0)

    def test_snapshot_is_keyed_by_the_scored_session_not_the_run_clock(self):
        data = verdicts()
        data["generatedAt"] = "2026-08-07"  # run slipped past UTC midnight
        data["dataAsOf"] = "2026-08-06"  # closes it actually scored
        self.assertEqual(ch.build_snapshot(data)["date"], "2026-08-06")

    def test_snapshot_falls_back_to_generated_at_for_pre_data_as_of_ledgers(self):
        self.assertEqual(ch.build_snapshot(verdicts())["date"], "2026-07-08")


class CalibrationHistoryTests(unittest.TestCase):
    def test_delayed_run_does_not_overwrite_the_next_days_row(self):
        # The 2026-08-06 loss: the delayed run keyed its snapshot off the clock
        # (08-07), so the real 08-07 run replaced it and that session vanished.
        delayed = verdicts()
        delayed["generatedAt"] = "2026-08-07"
        delayed["dataAsOf"] = "2026-08-06"
        next_day = verdicts()
        next_day["generatedAt"] = "2026-08-07"
        next_day["dataAsOf"] = "2026-08-07"

        history = ch.upsert_snapshot([], ch.build_snapshot(delayed))
        history = ch.upsert_snapshot(history, ch.build_snapshot(next_day))

        self.assertEqual([row["date"] for row in history], ["2026-08-06", "2026-08-07"])
        ch.validate_history_rows(history, next_day)

    def test_validation_finds_the_row_of_a_run_that_slipped_past_midnight(self):
        # The row-presence check must look for the scored session too. If it
        # kept keying off generatedAt it would hunt for 08-07, miss the 08-06
        # row this run just wrote, and turn CI red on exactly the runs the
        # dataAsOf split exists to protect.
        delayed = verdicts()
        delayed["generatedAt"] = "2026-08-07"
        delayed["dataAsOf"] = "2026-08-06"

        history = ch.upsert_snapshot([], ch.build_snapshot(delayed))

        self.assertEqual([row["date"] for row in history], ["2026-08-06"])
        ch.validate_history_rows(history, delayed)


    def test_upsert_replaces_same_day_and_keeps_dates_ascending(self):
        snapshot = ch.build_snapshot(verdicts())
        stale_same_day = copy.deepcopy(snapshot)
        stale_same_day["scoredCount"] = 99
        history = [
            {"date": "2026-07-07", "scoredCount": 1, "medianRelativePct": 1.0, "nonNeutralBeatRate": 1.0, "byBenchmark": {}},
            stale_same_day,
        ]

        updated = ch.upsert_snapshot(history, snapshot)

        self.assertEqual([row["date"] for row in updated], ["2026-07-07", "2026-07-08"])
        self.assertEqual(updated[1]["scoredCount"], 3)

    def test_validate_history_rejects_duplicate_dates(self):
        snapshot = ch.build_snapshot(verdicts())
        with self.assertRaises(ch.CalibrationHistoryError):
            ch.validate_history_rows([snapshot, copy.deepcopy(snapshot)], verdicts())

    def test_validate_history_requires_current_verdicts_row(self):
        with self.assertRaises(ch.CalibrationHistoryError):
            ch.validate_history_rows([], verdicts())

    def test_validate_history_recomputes_current_row(self):
        snapshot = ch.build_snapshot(verdicts())
        broken = copy.deepcopy(snapshot)
        broken["medianRelativePct"] = 12.3
        with self.assertRaises(ch.CalibrationHistoryError):
            ch.validate_history_rows([broken], verdicts())


if __name__ == "__main__":
    unittest.main()
