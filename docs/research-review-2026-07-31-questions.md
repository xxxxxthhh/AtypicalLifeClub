# Open questions from the 2026-07-31 full review pass

Branch: `codex/full-report-review-2026-07-31`

These are the decisions the review pass deliberately did **not** make on its own. Each one
changes published investment judgment, scope, or tooling behaviour, so it is left to the owner.
Answer them in one pass at the end; nothing here blocks the rest of the review.

---

## Q1 — STRUCTURAL: after a 25–55% decline, does a stance premised on "too expensive" survive?

**Status: raised. Every affected stance held unchanged pending your answer. This is one decision
you make once and I apply across the set — not sixteen separate questions.**

Seventeen reports fell more than 25% from their own price anchors in July 2026 (verified as a real
move, no corporate actions). Most of them carried a `cautious` or `bearish-avoid` stance whose
stated reason was **an arithmetic claim about a multiple**. Those stances were *right* — the
verdict ledger shows them outperforming their benchmarks on the way down. The problem is that the
specific arithmetic that justified them no longer holds, because the multiple compressed.

Where the arithmetic has been re-checked so far:

| Report | Stance | The claim that justified it | Status after re-anchoring |
|---|---|---|---|
| bloom-energy-2026 | cautious | "~26x 2026E sales pre-pays for everything going right" | **Dissolved.** ~11.9x on *raised* guidance; the 32%+ gross-margin bar it set was cleared (34.3%) |
| aaoi-2026 | cautious | "~26.6x EV/sales already assumes financial conversion" | **Dissolved.** ~11.7x; execution risks unchanged and unresolved |
| sandisk-2026 | cautious | "price implies $139–174 sustainable EPS, *above* the $120–132 peak guide" | **Inverted.** Now implies ~$68–85, *below* peak — the market is pricing a trough 35–45% under peak |

The remaining high-drift reports (SK hynix, Corning, Marvell, Coherent, Almonty, Nebius, CoreWeave,
Oklo, Lam, KLA, NeoVolta, Applied Materials, Vertiv, Micron) are being re-anchored the same way and
will mostly land in the same place.

**The genuine question is which of these two readings you want applied as policy:**

1. **"The caution has done its job."** A stance premised on valuation should relax when the
   valuation premise is removed. Under this reading several of these move to `neutral-watch`,
   and SanDisk arguably further, since its own arithmetic now points the other way.
2. **"Price falling is not evidence."** None of the *execution* questions were answered by the
   drawdown — SanDisk's NBM coverage is still unproven, AAOI's customer concentration and cash
   burn are unchanged, Bloom's 2 GW ramp still awaits H2. A cheaper price on unresolved risk is
   not the same as resolved risk, especially with ~18 of these names reporting within two weeks
   (Q2). Under this reading everything holds until the prints land.

**My recommendation: option 2 for now, then revisit in ~2 weeks**, for one specific reason — the
drawdown and the upcoming earnings wave are not independent. A market that repriced this hard
across an entire chain may be anticipating weak prints. Relaxing stances *just before* the
evidence arrives would be the worst-timed version of this decision. But I have deliberately not
made that call myself, and the reports say so in-text rather than quietly holding.

A third option, if you prefer: **re-weight the scenario grids without moving the stance labels**,
which records that the valuation leg weakened without asserting a new direction.

Every affected report carries a `scenario-grid-reweight-pending` monitoring item so nothing
silently drops off the review queue while this is open.

## Q2 — A large earnings wave lands within days of this pass. Second pass, or let the daily job catch it?

At the time of this review it is **2026-07-30, mid-session US time**. The review is anchored to
the **2026-07-29 close** (last completed session). Within the next two weeks a large share of
coverage reports:

| Date | Reporting |
|---|---|
| 2026-07-30 (after close, i.e. hours after this pass) | **AMZN, COIN, TEM** |
| 2026-08-04 | AMD, ANET, NRG, SPOT |
| 2026-08-05 | SNDK |
| 2026-08-06 | AAOI, CEG, ABNB |
| 2026-08-07 | OKLO, VST |
| 2026-08-10 | HIMS |
| 2026-08-11 | CRWV |
| 2026-08-12 | NBIS, COHR |
| 2026-08-13 | AMAT |

That is ~18 of 48 reports. Notably **Amazon, Coinbase and Tempus report tonight**, and all three
are in the untracked-legacy group whose reports are already the least verified.

**Question:** do you want a follow-up integration pass in ~2 weeks once this wave has reported,
or is the normal per-earnings workflow enough? This pass makes no attempt to anticipate them.

---

## Q3 — Should the 10 untracked legacy reports get `priceSymbol`? (scope change)

`tempus-ai`, `spotify`, `salesforce`, `paypal`, `netflix`, `igv`, `hims`, `coinbase`, `amzn`,
`airbnb` have **no `priceSymbol`**, so they have no price ledger entry, no drift signal, no
verdict-ledger tracking, and never appear in the rerun queue. They are the least-verified
reports in the set precisely because nothing flags them.

Adding `priceSymbol` would pull them into the tracking system — but that is a scope change with
consequences (they would enter the verdict ledger and start accruing measured stance
performance), so I have not done it silently.

`igv-2026` is an ETF, so it would need the benchmark/ETF treatment rather than a plain symbol.

---

## Q4 — `update_prices.py` records in-progress sessions as closes (tooling bug found during the pass)

`update_prices.py` sets `attempted_at = datetime.now(timezone.utc).date()` and fetches through
that date inclusive, taking whatever bar exists. **Run during US market hours it stores a live
intraday bar in `lastClose` as though it were a settled close.** `update_verdicts.py` has the
same pattern for benchmark series.

This is not hypothetical — it happened during this pass, and the numbers moved between fetches.
Meta showed a true 07-29 close of $585.61 against a drifting 07-30 intraday print near $532.80.
Publishing a report anchored to that would have put a moving number in a research document.

I pinned this pass to the last completed session manually. **Should I add a completed-session
guard to both scripts** (skip today's bar unless the session has closed), or do you prefer to
keep the daily job as-is and handle it by convention?

---

## Q5 — Peer-comparison tables are partly unverified

Peer tables (e.g. Bloom's FCEL/PLUG rows) still carry February-baseline market caps that were
not re-checked in this pass. I labelled them as unverified rather than refreshing every peer,
since peers are outside coverage and refreshing them would roughly multiply the work.

**Confirm this is the right call**, or say the word and I will re-verify peer rows too.
