# Frozen metals fixtures

`metals-2026-08-28.json` — 92 closes per symbol for all fourteen, ending
2026-08-28, taken from the corrected series after PR-1b.

It exists so the briefing's metals gate is replayable. Under the caliber pinned
in §4.1.1 of `docs/daily-briefing-plan.md` (simple returns, the 90 returns
before the day, sample standard deviation, compared un-rounded) this file
yields exactly two rows:

| metal | leg | changePct | z |
|---|---|---|---|
| 钯金 | `PA=F` | +6.80% | +2.6739 |
| 黄金 | `GLD` | −3.24% | −2.0533 |

`PALL` (+1.9333) and `GC=F` (−1.8937) stay out, and both round to about 2.0 —
which is why the threshold compares the un-rounded value.

Replay tests point here, never at live Yahoo. Otherwise "our caliber changed"
and "the vendor revised a number" become the same red light.
