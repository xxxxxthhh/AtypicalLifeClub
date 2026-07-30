# Open questions from the 2026-07-31 full review pass

Branch: `codex/full-report-review-2026-07-31`

These are the decisions the review pass deliberately did **not** make on its own. Each one
changes published investment judgment, scope, or tooling behaviour, so it is left to the owner.
Answer them in one pass at the end; nothing here blocks the rest of the review.

---

## Q1 — Bloom Energy: the stance premise dissolved. Re-judge or hold?

**Status: raised, stance held unchanged pending your answer.**

What happened: Bloom reported Q2 2026 on 2026-07-28 and the stock fell over the following
sessions, so the multiple collapsed from **both** directions at once.

| | Prior frame (2026-07-06) | Now (2026-07-29) |
|---|---|---|
| Price | $295.05 | **$163.75** (−44%) |
| Market cap | ~$84B | **~$48B** |
| 2026 revenue reference | ~$3.2B | **$4.05B** (raised guide midpoint, +27%) |
| Market cap / 2026 revenue | ~26x | **~11.9x** |

The report's `cautious` stance rested on an explicit arithmetic claim: at ~26x sales the price
"pre-pays for orders, capacity, margins, and cash conversion to work together," producing a
**negative expectation gap**. At ~11.9x that specific claim does not survive. On top of that,
Q2 cleared the bull case's own stated bar — **product gross margin 34.3% non-GAAP vs a "32%+"
requirement** — and demonstrated order conversion at **+165.5% revenue growth**.

But the report's written upgrade trigger requires **H2 2026** delivery volumes to validate the
2 GW ramp, and Q2 is H1. Service-cost trajectory and customer concentration were **not
disclosed** in the Q2 release, so two of the four execution items remain unverified.

I re-anchored all the arithmetic and rewrote the expectation-gap paragraphs, but did **not**
re-weight the 20/40/40 scenario grid or move the stance — that is your judgment, not a
mechanical update. The report now says so explicitly, and a
`scenario-grid-reweight-pending` monitoring item keeps it visible in the queue.

**Options:**
1. **Hold `cautious` until H2 2026 delivery data** (current state — defensible, trigger not met).
2. **Move to `neutral-watch`** on the grounds that the negative-gap arithmetic is gone even
   though the ramp is unproven.
3. **Re-weight the grid now** (e.g. shift weight from bear toward base) without changing the
   stance label.

My read: option 1 or 2 are both honest; option 2 is arguably more consistent, because holding
`cautious` while stating in the same report that its arithmetic basis has dissolved is a
slightly uncomfortable position. I did not take it unilaterally because the stance is the
product.

---

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
