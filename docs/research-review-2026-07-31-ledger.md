# Full research review pass — 2026-07-31

Branch: `codex/full-report-review-2026-07-31`

Scope: all 48 live reports in `static/invest/research/data/reports.json`
(56 entries minus 8 `*-pre-rerun` archival versions).

## Method and the two data-integrity findings that shaped this pass

**1. The July 2026 drawdown is real, not a data artifact.** The whole pass rests on
`prices.json` drift, so the drift was verified before anything was written. For every large
mover (SK hynix, SNDK, AAOI, BE, GLW, MRVL) the daily series was pulled across the
`baseDate`→now window and checked for corporate actions: **no splits, no consolidations,
no symbol changes**, and the declines are continuous rather than single-day discontinuities.
Re-running `update_prices.py` left every `baseDate`/`basePrice` anchor unchanged, confirming
the drift is a genuine price move and not a re-derived base.

**2. The price ledger was pinned to the last completed session.**
`update_prices.py` takes `attempted_at = datetime.now(timezone.utc).date()` and fetches
through that day inclusive, with no guard for a session still in progress. Run during US
market hours it records **live intraday bars as if they were closes**. This pass pins the
ledger to **2026-07-29**, the last completed US session. (Meta shows why it matters: a true
07-29 close of $585.61 against a moving 07-30 intraday print of ~$532.80.)

> Follow-up worth considering separately: add a completed-session guard to `update_prices.py`
> so the daily job cannot record an in-progress bar.

## Earnings status — the key scoping finding

An earnings calendar was built for all covered tickers rather than checking company by
company. Using "has an actual reported EPS" as the test for *reported* (a scheduled date with
`eps=nan` is **not** a report):

- **Only one report had an un-integrated reported quarter: `bloom-energy-2026`.**
  Bloom reported 2026-07-28; the report's `lastUpdate` was 2026-07-07.
- Every other late-July reporter had already been integrated by the 07-28/07-30 commits
  (Corning, KLA, Cadence, DLR, PayPal, Vertiv, Lam, Meta, Equinix, SK hynix, GE Vernova,
  TSMC, ASML, Netflix).
- **Tempus, Coinbase and Amazon had NOT reported** at the time of this pass — their
  2026-07-30 dates are scheduled, after the close.

So this pass is overwhelmingly a **valuation-staleness review**, not an earnings-integration
review.

## Drift vs each report's frozen `priceAsOf` anchor (2026-07-29 closes)

17 reports exceed the repo's own rerun threshold (`tracking-rules.js`: drift ≥25% or age >60d).

| Report | Drift | Anchor → 07-29 close | versionType |
|---|---|---|---|
| aaoi-2026 | −55.3% | 171.23 → 76.52 | initial |
| sk-hynix-2026 | −52.0% | ₩2,917,000 → ₩1,401,000 | full-cycle |
| sandisk-2026 | −51.4% | 2090.71 → 1015.89 | initial |
| bloom-energy-2026 | −44.5% | 295.05 → 163.75 | full-cycle |
| corning-2026 | −43.9% | 221.05 → 124.05 | initial |
| marvell-2026 | −33.4% | 245.23 → 163.40 | initial |
| coherent-2026 | −33.4% | 333.36 → 222.05 | initial |
| almonty-2026 | −32.4% | 16.21 → 10.95 | full-cycle |
| nebius-2026 | −30.4% | 213.02 → 148.22 | initial |
| coreweave-2026 | −29.7% | 86.46 → 60.82 | initial |
| oklo-2026 | −29.6% | 52.36 → 36.84 | full-cycle |
| lam-research-2026 | −28.2% | 351.41 → 252.35 | initial |
| kla-2026 | −27.7% | 235.55 → 170.19 | initial |
| neov-2026 | −27.6% | 2.72 → 1.97 | incremental |
| applied-materials-2026 | −27.6% | 603.04 → 436.45 | initial |
| vertiv-2026 | −27.3% | 306.97 → 223.04 | initial |
| micron-2026 | −24.2% | 975.41 → 739.00 | initial |

Mid-drift (10–25%): amd −20.1, minimax −18.3, oracle −17.8, jinpan −17.2, smh −14.9,
synopsys −14.5, gevernova −13.9, tsmc −13.7, asml −12.2, cadence −10.8.
Low-drift (<10%): nrg −9.1, dlr +8.6, ceg +7.8, vistra −5.5, arista −3.7, copx −3.0,
meta −2.4, broadcom −2.3, nvidia −1.3, eqix +0.6.
Untracked (no `priceSymbol`, no drift signal): tempus-ai, spotify, salesforce, paypal,
netflix, igv, hims, coinbase, amzn, airbnb.

## Edit rules applied

- **`versionType=full-cycle` → no `~~` strikethrough in the body** (skill rule, enforced by
  `check_research_package.py`). Use a dated `> **YYYY-MM-DD ... update:**` block, matching the
  SK hynix house pattern. Affects: tempus-ai, sk-hynix, almonty, hims, bloom-energy, coinbase,
  amd, jinpan, oklo.
- **`initial` / `incremental` → redline allowed** (`~~old~~` + dated replacement), matching the
  Lam Research house pattern.
- **Re-anchoring `priceAsOf` without addressing the scenario grid is forbidden here.** It would
  reset drift to ~0 and silently drop the report off the rerun queue while leaving an
  un-rebuilt grid live — strictly worse than leaving it queued. Where the math is re-anchored
  but the scenario *weights* and *stance* are not re-judged, an explicit monitoring marker is
  added so the report stays visible as unfinished.
- **Stance changes are not made silently.** Re-anchoring valuation math is mechanical and is
  done here; re-weighting a scenario grid or flipping a stance is an editorial judgment and is
  raised in `research-review-2026-07-31-questions.md` instead.

## Tiering — how much treatment each report gets

Uniform treatment would be wrong, not just slow. Stamping "scenario grid stale" on a report that
moved −2% devalues the marker exactly where it matters. Reports are tiered by whether the drawdown
broke a *conclusion*, merely a *number*, or nothing:

- **Tier A — conclusion broken** (drift ≥25%, 17 reports). Full treatment: re-anchor price, market
  cap, EV and every derived multiple; mark the scenario grid's relative verdicts stale; add a
  `scenario-grid-reweight-pending` monitoring item; move `priceAsOf`; raise the stance under Q1.
- **Tier B — number stale, conclusion intact** (drift 10–25%). Update the price/market-cap/multiple
  strings and the date. **No grid marker, no stance question, no pending-monitoring item, and
  `priceAsOf` is NOT moved** — moving it would reset drift to ~0 and drop the report off the rerun
  queue without the re-anchor work having been done.
- **Tier C — nothing material moved** (drift <10%). Confirm no price reads as a current claim; many
  already carry frozen-snapshot labels from the July passes. Often zero edits.
- **Untracked (10)** — no `priceSymbol`, no drift signal. Earnings are mostly already integrated;
  the work is confirming no stale valuation claim reads as live.

## Marker vocabulary (enforced by the checker)

`check_research_package.py` only accepts these as "this value is old" markers:
`~~ | update | updated | stale | historical | old | 旧 | 历史 | 更新 | 失效 | 不能再 | 需重算 | 需重建`.
**"prior" / "此前" / "重新锚定" / "原文" do NOT count** and will fail the valuation-sensitive run.
Standardised on **"old"** (EN) and **"旧"** (ZH).

Two further checker constraints found the hard way:
- The **last scenario-grid cell must be a bare integer weight** — annotate the header, never the cell.
- **Metadata has no allowlist.** `summary`, `highlights`, `lastUpdate`, `title`, `titleEn` must not
  contain old anchors at all. `stanceRationale` and `monitoring[]` are *not* scanned, so they may
  (and should) retain the old figures to explain the change.

## Per-report status

Status: `done` / `pending` / `raised` (waiting on a question).

| Report | Tier | Action | Status |
|---|---|---|---|
| bloom-energy-2026 | A | Q2 2026 integration + re-anchor $295.05→$163.75, ~26x→~11.9x | done (stance raised in Q1) |
| aaoi-2026 | A | re-anchor $171.23→$76.52, EV/S ~26.6x→~11.7x | done (stance raised in Q1) |
| sandisk-2026 | A | re-anchor $2,090.71→$1,015.89, P/S ~16x→~7.8x; expectation gap **inverted** | done (stance raised in Q1) |
| sk-hynix-2026 | A | re-anchor ₩2,917,000→₩1,401,000; P/S ~16x→~5.3x, now **below** February's 6.3x; TTM P/E left stale (bridge undisclosed) | done (stance raised in Q1) |
| corning, marvell, coherent, almonty, nebius, coreweave, oklo, lam-research, kla, neov, applied-materials, vertiv, micron | A | re-anchor | pending |
| amd, minimax, oracle, jinpan, smh, synopsys, gevernova, tsmc, asml, cadence | B | number refresh only | pending |
| nrg, dlr, ceg, vistra, arista, copx, meta, broadcom, nvidia, eqix | C | confirm nothing reads as current | pending |
| tempus-ai, spotify, salesforce, paypal, netflix, igv, hims, coinbase, amzn, airbnb | untracked | verify no stale valuation claim | pending |

## Chain-level signal

Logged **once**, not per report: `ai-infra-chain-wide-repricing-2026-07` in `signals.json`, against a
new `chain-wide-repricing` rule added to `coverage-map.json` (the framework had no rule covering a
simultaneous multi-layer repricing). A single name's post-earnings move remains non-loggable per
existing convention.
