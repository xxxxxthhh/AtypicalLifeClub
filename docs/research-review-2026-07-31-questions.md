# Open questions from the 2026-07-31 full review pass

Branch: `codex/full-report-review-2026-07-31`

These are the decisions the review pass deliberately did **not** make on its own. Each one
changes published investment judgment, scope, or tooling behaviour, so it is left to the owner.
Answer them in one pass at the end; nothing here blocks the rest of the review.

---

## Q1 — STRUCTURAL: after a 25–55% decline, does a stance premised on "too expensive" survive?

**Status: ANSWERED 2026-07-31 — owner ruled for option 1, generalized: a report's published
stance and rationale must be true at the CURRENT price.** A reader at any time must see an
assessment of the present setup, anchored to the latest completed close — never a stale judgment
waiting for future evidence. Applied 2026-07-31 across all 17 reports carrying the
`scenario-grid-reweight-pending` marker (branch `codex/q1-stance-readjudication-2026-07-31`).
Critically, this was **not** "flip everything cheap": prices bounced hard on 07-30 (SNDK +26%,
BE +26.5%, NBIS +27%, AMAT +15% — but VRT only +2%), so each report's arithmetic was recomputed
fresh at the latest completed close (07-30 US; 07-31 KRX for SK hynix) before re-deriving the
stance. Outcomes:

| Report | Old stance | New stance | One-line reason |
|---|---|---|---|
| applied-materials-2026 | cautious | **neutral-watch** | at $501.77, ~11.1x EV/annualized sales sits just above the report's own 8–10x band — the mildly negative gap is gone |
| lam-research-2026 | neutral-watch | neutral-watch | at $297.72, ~13.8x EV/June-annualized: elevated but no longer stretched; skew still balanced |
| kla-2026 | cautious | **neutral-watch** | at $180.33, ~17.3x EV/annualized rev vs improved Q4 evidence — the below-embedded-expectation claim fails; premium multiple caps it at neutral |
| nebius-2026 | cautious | cautious | +27% bounce restored the premise: ~47x P/S is again paying for the winning-neocloud story |
| coreweave-2026 | bearish-avoid | bearish-avoid | the case is EV-anchored (~$66B on ~$32.9B net debt, only ~−8% from anchor); structural legs unchanged |
| vertiv-2026 | cautious | **neutral-watch** | at $227.50 / ~34x raised guide, the reverse-multiple frame implies ~10% EPS CAGR, not ~24% — the bar the caution rested on is gone |
| corning-2026 | neutral-watch | neutral-watch | at $135.22, ~43.4x 2026E core EPS still underwrites multi-year optical growth; neutral remains true |
| aaoi-2026 | cautious | cautious | multiple arithmetic stays dissolved (~13.8x), but negative OCF, ATM dilution and concentration are independent legs; rationale re-founded |
| sandisk-2026 | cautious | **neutral-watch** | at $1,279.96 the 12–15x frame implies $85–107 sustainable EPS, still below the $120–132 peak guide — inversion held through the bounce |
| sk-hynix-2026 | cautious | **neutral-watch** | at ₩1,718,000, P/S ~6.5x ≈ February's 6.3x start; the 28x/16x arithmetic is gone; peak-cycle durability caps it at neutral |
| almonty-2026 | cautious | cautious | ~66x sales was never the basis — Sangdong execution risk vs the scarcity option is untouched by price |
| bloom-energy-2026 | cautious | **neutral-watch** | at $207.12, ~15.1x the raised guide vs the ~26x premise, with the report's own 32%+ GM bar cleared (34.3%) |
| neov-2026 | cautious | cautious | sub-$100M micro-cap; contraction/dilution/runway legs untouched by the price move |
| oklo-2026 | constructive | constructive | at $41.09 (~$7.1B cap) the positive skew vs the ~$12.6B grid reference is wider than before |
| micron-2026 | cautious | cautious | at $874.66 implied sustainable EPS $58–73 still exceeds the weighted ~$53 — the gap narrowed but holds |
| marvell-2026 | cautious | cautious | ~14.1x EV/Sales on the *undelivered* FY2027 outlook still pre-pays a clean ramp; weakened negative gap survives |
| coherent-2026 | cautious | **neutral-watch** | at $249.06, implied ~16–24% growth is at/below delivered demand evidence; unproven FCF conversion caps it at neutral |

Scenario-grid probability weights were re-checked and retained on all 17 (they encode
fundamental path probabilities, not the old multiple); the grids' valuation-implication columns
are marked to be read against the new anchors, and every `scenario-grid-reweight-pending`
monitoring item is discharged.

*The original question as raised:*

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

**Status: SUBSUMED by the Q1 ruling (2026-07-31).** Under "the stance must be true at the
current price", every earnings print is integrated through the normal per-earnings workflow and
the daily job, and each integration re-derives the assessment at the then-current close — so no
separate scheduled second pass is needed. The 17 re-adjudicated reports each carry their next
print date in their monitoring items.

*The original question as raised:*

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
