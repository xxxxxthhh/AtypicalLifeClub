# Research Hub v6 — Benchmark Fidelity, Trigger Loop & Demand-Layer Completion Spec

**Status:** Draft for user review · **Owner:** (unassigned — handoff to implementing agent) · **Author:** planning session, 2026-07-08
**Depends on:** v5 fully shipped on `main` (`30d22fd`): stance v2 schema + `ENFORCE_STANCE_V2 = True` (`a447147`), scenario grids + priced-in on all 35 current-chain reports, Track 3 verdict ledger (`update_verdicts.py` / `validate_verdicts.py` / `verdict-ledger.html`, SMH ingested, CI + daily cron wired, review fixes in `0f49834`). v4 tier gate and coverage queue (`planned[]`: CCJ/MP/ALAB/PWR/AMKR) are live.
**Scope of this doc:** three tracks — **Track 1 benchmark fidelity** (score each stance against a benchmark that matches its layer, not SMH-for-everything, plus a calibration history so drift is plottable), **Track 2 trigger loop** (make `stanceTriggers` machine-checkable through graded monitoring readings, so "trigger fired but stance didn't move" is computed, not confessed), and **Track 3 demand-layer completion** (MSFT + GOOG initiations, AMZN chainization, and execution of the v4 `planned[]` queue). A **stretch goal** (§5) defines the paper book. Track 1 is data/generator/page work; Track 2 is schema + skill-side authoring discipline; Track 3 is content via the `company-research-publishing` skill.

This spec is **self-contained** — an implementing agent should not need the originating chat.

**The problem it attacks:** v5 made every verdict dated, directional, and scored — but the score itself is now the weakest link. All 35 reports are scored against SMH, a semiconductor basket, while 8 power reports, 3 datacenter-facility reports, and 2 resources reports have nothing to do with semiconductor beta: their "relative delta" measures whether semis fell, not whether the call was right (§0). Meanwhile the ledger's most valuable question — *which published triggers have already fired without a stance change* — still depends on quarterly human honesty, and the demand-risk layer that anchors the whole AI-infra book is missing two of the three hyperscalers. v6 makes the scoreboard honest, the discipline mechanical, and the book complete on its most load-bearing layer.

---

## 0. Context & grounded facts (verified 2026-07-08)

| Fact | Value | Consequence |
|---|---|---|
| Single-benchmark mis-scoring | All 35 open calls score vs SMH. Power-layer relative deltas after ~1 week: `-7.6, -6.7, -4.8, -3.6, +2.0, +2.8, +4.9, +8.0` — a ±8% spread driven mostly by the semis/utilities divergence, not by call quality. GEV ranks best-in-book (+11.4% at one point) for being *not a semiconductor* | Track 1: per-layer benchmark assignment. Without it, calibration stats reward/punish sector mix and the ledger trains the wrong instinct |
| Layer membership | `power`: NRG, GEV, BE, NEOV, 688676.SS (Jinpan), OKLO, CEG, VST (8) · `datacenter-facility`: EQIX, VRT, DLR (3) · `resources`: ALM, COPX (2) · `demand-risk`: NBIS, CRWV, META, ORCL (4) · remaining 18 across foundry/semicap/EDA/compute/custom-silicon/memory/networking/optical are legitimately semis (SMH holds their top names) | The mapping table (§2.2) is short: 4 layers need a non-SMH default, plus 2 per-report overrides (VRT, COPX) |
| Ledger plumbing | `update_verdicts.py` fetches one `BenchmarkSeries` (symbol from the `benchmark: true` report, i.e. smh-2026) and passes it to every entry. `verdicts.json` top level has a single `"benchmark": "SMH"`. `validate_verdicts.py --strict-coverage` runs in the daily cron; lenient mode in ci-smoke | Track 1 generalizes: series-per-symbol dict, `benchmarkSymbol` on each entry, validator follows. The strict/lenient split is settled — do not reopen it |
| Calibration is snapshot-only | `verdicts.json` is overwritten daily; no time series of median-relative or beat-rate exists, so calibration *drift* (the §4.3 quarterly question) can't be plotted | Track 1 adds an append-only `calibration-history.json` (one row/day from the cron) |
| `stanceTriggers` are prose | Bilingual free text (`upgrade`/`downgrade`); `monitoring[]` items have `id`, `metric`, `trigger`, `latest`, `nextCheck(Date)` but **no graded state** — nothing records whether the latest reading is inside or beyond the published trigger | Track 2: grade the reading (`within / breached / unclear`) at update time; machines aggregate, humans still judge. Full NLP-style auto-detection is explicitly out of scope |
| Quarterly calibration note (v5 §4.3) | Authored, zero shipped so far; first one due after backfill quarter. The hardest section ("triggers that fired without a stance change") has no data source | Track 2's graded readings make that section a query; a small generator emits the data appendix so the human writes only conclusions |
| Demand-risk hole | Layer has NBIS, CRWV, META, ORCL. **MSFT and GOOG — the #1/#2 AI-capex buyers — are absent**; AMZN exists only as a non-chain 2026-02 report (`amzn-2026`, no `chainLayer`/stance/grid) | Track 3 P1. The book's demand-validation layer currently can't answer its own core question |
| v4 queue already promised | `coverage-map.json` `planned[]`: CCJ (resources), MP (resources), ALAB (interconnect), PWR (power), AMKR (advanced-packaging). `interconnect` and `advanced-packaging` layers exist with **0 nodes** | Track 3 P2 executes the queue; two empty layers get their first nodes. No new planning needed — it's committed metadata |
| Authoring pipeline | `company-research-publishing` skill (git source `~/Documents/codex-private-skills`, deploy by single-file copy; **never `install-local.sh`**) gates full-tier reports: modules + ≥20-row table spine + scenario grid + priced-in + stance v2 fields. Skill main is ahead-3 of its origin (unpushed) | Track 3 initiations are standard skill runs; Track 2 needs one skill-side checklist edit. Push the skill repo before v6 content starts |
| Design & i18n rules | DESIGN.md: no red/green/amber judgment visuals; sign/text carries direction. All pages bilingual via `PAGE_LABELS`/`localize()`; zh `html lang` is `zh-CN` | All v6 UI (benchmark column, trigger watch, drift chart) inherits these; the drift chart uses neutral tokens only |

---

## 1. Principles (locked)

1. **A score is only as honest as its yardstick.** Every stance is scored against the benchmark that its layer actually competes with. SMH stays the *book-level* reference; it stops being the *per-call* one where it misleads.
2. **Humans grade readings; machines flag inaction.** Trigger detection is a human judgment recorded as an enum at update time — the system's job is to make the *consequence* (breached + stance unchanged + N days) impossible to ignore, not to parse prose.
3. **The ledger accumulates; it never rewrites.** Benchmark reassignment applies from v6 forward — existing closed intervals keep their SMH scoring, flagged as such (same philosophy as migration flags).
4. **Coverage grows where the thesis is weakest, not where it's most comfortable.** The demand layer is the book's falsification surface; it gets filled before any new supply-side name.
5. **No quotas, no scoring colors, cheap flips** — all v5 locked decisions carry over unchanged.

---

## 2. Track 1 — benchmark fidelity (make the scoreboard honest)

### 2.1 Data — `data/benchmarks.json` (new, hand-authored config)

```jsonc
{
  "default": "SMH",
  "layerDefaults": {
    "power": "XLU",
    "datacenter-facility": "SRVR",
    "resources": "COPX",
    "demand-risk": "QQQ"
  },
  "symbols": {
    "SMH":  { "name": { "zh": "半导体 ETF", "en": "Semiconductors" } },
    "XLU":  { "name": { "zh": "公用事业 ETF", "en": "Utilities" } },
    "SRVR": { "name": { "zh": "数据中心/基础设施 REIT ETF", "en": "Data-center & infra REITs" } },
    "COPX": { "name": { "zh": "铜矿 ETF", "en": "Copper miners" } },
    "QQQ":  { "name": { "zh": "纳指 100 ETF", "en": "Nasdaq-100" } }
  }
}
```

Resolution order per report: `report.benchmarkSymbol` (new optional field in `reports.json`) → `layerDefaults[chainLayer]` → `default`. Rules:

- **Self-benchmark ban — scoped to current-chain scored reports only:** a report with a `chainLayer` (i.e. one that receives verdicts) must not resolve to its own `priceSymbol` (`copx-2026` would self-score as 0.0 forever). Validator hard-fails on that case. **Benchmark-only sleeves are exempt** — `smh-2026` (`benchmark: true`, no `chainLayer`) legitimately carries `priceSymbol: "SMH"` and never receives a verdict; the rule must not scan it.
- **Overrides carry a structured rationale:** `benchmarkRationale` (bilingual `{zh, en}`, new optional field) is **required whenever `benchmarkSymbol` differs from the layer default / book default**, validator-enforced. This is the audit trail against benchmark shopping: the quarterly note generator lists every override with its rationale verbatim.
- **Decided overrides (review round 1):**
  - `copx-2026` → `"SMH"` — COPX is held as the resources-side expression of AI electrification; the fair question is whether that leg adds value over the book's core beta, and reusing the book default avoids a new symbol dependency for one report. (`PICK` was considered and rejected: it answers "was copper the right mining bet," which is not the book's question.)
  - `vrt-2026` → `"SMH"` — VRT is an equipment maker inside `datacenter-facility`, not a REIT.
  - `demand-risk` layer default is `QQQ` (decided, was open question): the layer's read-through is mega-cap platform capex absorption; QQQ is the honest yardstick for platform names, where SMH would let them free-ride semis drawdowns.
  - `jinpan/688676.SS` and other non-US listings keep their layer default unless FX/segment noise proves otherwise (quarterly-note question, not a v6 blocker).
- Candidate symbols were **not availability-checked in this session** — implementer's step 1 is to verify XLU/SRVR/COPX/QQQ return usable daily closes through the `update_prices.py` fetch layer in the deployment environment, and substitute (e.g. XLRE for SRVR) if not.

### 2.2 Generator & validator

- `update_verdicts.py`: fetch one `BenchmarkSeries` per distinct resolved symbol (min stance date across the reports assigned to it, same buffer); each open entry and **new** closed interval gains `"benchmarkSymbol"`. Top-level `"benchmark"` is kept (book-level reference = SMH) for backward compatibility; entries are authoritative.
- **Grandfathering:** closed intervals created before v6 keep SMH numbers and gain `"benchmarkSymbol": "SMH"` retroactively (mechanical relabel of what was actually used — not a rescore, per principle 3). Since all 26 existing closed intervals are migration-flagged and excluded from calibration anyway, this is cosmetic.
- `validate_verdicts.py`: `benchmarkSymbol` required on scored entries, must equal the resolution result recomputed from `reports.json` + `benchmarks.json`; self-benchmark check (above); everything else unchanged.
- `benchmarks.json` is validated by `validate_reports.py` (schema: default present, symbols cover all values used) — one function, not a new validator.

### 2.3 Page — `verdict-ledger.html`

**No misleading intermediate state:** the current page hard-codes "vs SMH" in headers, hero copy, and mixes all calls in one calibration pool. The moment the generator writes per-layer `relativePct`, that page copy becomes wrong — so the minimal compatibility changes ship **in the same PR as the generator change (PR-1)**, not later:

- (PR-1) table headers become "vs benchmark / 相对基准"; each row shows its `benchmarkSymbol`; hero copy drops the fixed SMH claim; calibration never averages across benchmarks (simplest compliant form: group by benchmark, or restrict the strip to the SMH bucket with an explicit label until PR-2).
- (PR-2) full per-bucket calibration presentation, plus the book-level reference line (all calls vs SMH, explicitly labeled) so the pre-v6 number keeps a home without silently changing meaning.
- (PR-2) new small **drift chart**: SVG line of daily median-relative and beat-rate from `calibration-history.json` (§2.4), neutral tokens, no fills implying good/bad.

### 2.4 Calibration history

Daily cron writes one row to `data/calibration-history.json` after validation: `{date, scoredCount, medianRelativePct, nonNeutralBeatRate, byBenchmark: {...}}`, where `date` = the verdicts `generatedAt`. **Upsert semantics, not blind append:** at most one row per `generatedAt` date; a same-day rerun (`workflow_dispatch`, failure retry) replaces that day's row instead of duplicating it or tripping a monotonicity check. Prior days' rows are never touched (history is evidence). Validator checks: dates strictly unique and ascending, and the row matching the current verdicts `generatedAt` recomputable from `verdicts.json` — earlier rows are not revalidated.

---

## 3. Track 2 — trigger loop (make inaction visible)

### 3.1 Schema (`reports.json`, warn-first)

- `monitoring[]` items gain two optional fields:
  - `reading`: `"within" | "breached" | "unclear"` — the author's grade of `latest` against `trigger`, set whenever `latest` is updated.
  - `readingAsOf`: `YYYY-MM-DD` — when that grade was made. Required iff `reading` present.
- `stanceTriggers.upgrade/downgrade` gain optional `monitoringIds: []` referencing `monitoring[].id` in the same report — the explicit link "this prose trigger is watched by these dashboard items." Validator checks referential integrity; duplicates fail.
- Rollout: `ENFORCE_TRIGGER_LINKS` warn-first flag, same pattern as `ENFORCE_STANCE_V2` (third use of the established mechanism). Enforcement target: every current-chain report's `stanceTriggers.downgrade` has ≥1 `monitoringIds` entry; `reading` itself stays optional forever (absence = "not yet graded", rendered as such).

### 3.2 Backfill

One skill-assisted pass over the 35 current-chain reports: link each trigger side to its obvious monitoring items (most reports were written with this correspondence in mind — e.g. ASML's downgrade trigger names EUV bookings, which is monitoring item `euv-high-na-orders`), grade current readings. Anything genuinely unlinkable gets a new monitoring item (that's a content gap worth surfacing, not a schema failure).

### 3.3 Surfacing

- **Ledger page, new "Trigger watch" section** (between open calls and closed intervals): rows where any linked item has `reading: "breached"` and the stance is unchanged since `readingAsOf` — columns: report, stance, breached metric, days since breach. Factual tone: "已触发未复核 / breached, not yet re-adjudicated". Empty state is the healthy state.
- **Monitoring dashboard**: the kill-criteria board shows the grade chip (within/breached/ungraded) per item — text chip, neutral styling.
- **Quarterly note generator** (`generate_calibration_note.py`, run manually): emits a dated markdown data appendix — stance distribution, best/worst relative calls per benchmark bucket, full breached-without-flip list, neutral share. The human writes the conclusions section on top (v5 §4.3 stays authored; only its data gathering is automated).

---

## 4. Track 3 — demand-layer completion & queue execution (content)

Standard `company-research-publishing` skill runs; every report full-tier, bilingual, grid + priced-in + v5 stance fields + trigger links (§3.1) from day one. Order:

| # | Name | Layer | Why now |
|---|---|---|---|
| P1a | **MSFT** initiation | demand-risk | #1 AI capex buyer; the book scores GPU/HBM/power scarcity without covering the balance sheet most of it lands on. Core read-through: Azure AI revenue vs capex absorption |
| P1b | **GOOG** initiation | demand-risk | #2 buyer *and* the strongest own-silicon (TPU) counterfactual to the merchant-silicon layer — direct cross-check for NVDA/AVGO theses |
| P1c | **AMZN chainization** | demand-risk | Cheapest full slot in the book: 2026-02 report exists; rerun to current numbers + `chainLayer: demand-risk` + full v5/v6 fields, archive the old version per incremental-revision rules |
| P2 | **CCJ, MP, ALAB, PWR, AMKR** (v4 `planned[]`) | resources ×2, interconnect, power, advanced-packaging | Committed queue; ALAB and AMKR give the two empty layers their first nodes. Sequence within P2 at implementer's discretion; CCJ first pairs naturally with the OKLO trigger set |

After P1+P2 the chain book is 35 → **43**, demand-risk 4 → 7, and no layer is empty. Benchmarks: all eight resolve correctly under §2.1 — interconnect/packaging → SMH via book default; demand-risk → **QQQ** (decided, §2.1); CCJ/MP → COPX via resources default (implementer sanity-checks that a copper-miners basket is acceptable for uranium/rare-earth names — if not, per-report overrides with `benchmarkRationale`, e.g. URA for CCJ).

**Explicitly out of v6:** second coverage map (stablecoin/AI-software chains), further supply-side names beyond the committed queue, scout list changes.

---

## 5. Stretch — paper book (only if Tracks 1–3 land early)

Map stance×conviction to paper weights (proposal: bullish·high 5% / bullish·medium 4% / constructive·high 4% / constructive·medium 3% / constructive·low 1.5% / neutral 0 / cautious 0 / bearish-avoid 0; cash earns nothing; rebalance only on stance flips), compute a daily book NAV vs SMH in the cron, append to `calibration-history.json`, render one more line on the drift chart. Answers the only question the per-call ledger can't: *is the book as a whole worth following?* Cut first if anything slips — it depends on Track 1's multi-benchmark plumbing but nothing depends on it.

---

## 6. Delivery slicing & gates

| PR | Content | Gate |
|---|---|---|
| PR-1 | `benchmarks.json` + resolution in `update_verdicts.py` + validator (incl. `benchmarkRationale` requirement, scoped self-benchmark ban) + grandfather relabel + fetch-layer availability check for XLU/SRVR/COPX/QQQ + **minimal ledger-page compatibility (§2.3 PR-1 items)** | all validators green; verdicts regenerate with per-entry `benchmarkSymbol`; page shows per-row benchmark and never averages across benchmarks; unit tests for resolution order + scoped self-benchmark rejection + rationale enforcement |
| PR-2 | Full per-bucket calibration + book-level SMH reference line + `calibration-history.json` cron upsert + drift chart | page renders all buckets; same-day rerun of the cron leaves exactly one row per `generatedAt` (upsert verified by test); browser smoke zh/en |
| PR-3 | Track 2 schema (`reading`/`readingAsOf`/`monitoringIds`, `ENFORCE_TRIGGER_LINKS = False`) + monitoring-dashboard grade chips | validators green on untouched data (warn only); referential-integrity unit tests |
| PR-4 | Trigger backfill ×35 + flip `ENFORCE_TRIGGER_LINKS = True` + ledger "Trigger watch" section + note generator | strict validator green; one manufactured breach (fixture) produces a trigger-watch row; generator output validates as the quarterly-note appendix |
| PR-5..N | Track 3 content: P1a/P1b/P1c, then P2 ×5, batched like the v5 backfill (short branches, review branch, integrate) | per-report: `check_research_package.py`, `validate_reports.py`, zh/en parity; **user reviews MSFT (first initiation) before the rest proceed** |
| Stretch | Paper book weights + NAV line | NAV recomputable from verdicts history; documented weight table in DESIGN.md or spec appendix |

Track order 1 → 2 → 3 for infrastructure, but Track 3 content can start any time after PR-1 (new reports need `benchmarkSymbol` resolution to exist so their first verdicts are scored correctly).

## 7. Acceptance criteria

- [ ] Every scored verdict entry carries a `benchmarkSymbol` that matches the documented resolution; no **current-chain scored** report resolves to its own symbol (benchmark-only sleeves exempt); every override carries a bilingual `benchmarkRationale`; power/facility/resources calls no longer move ±5% on semis-only days (spot-check vs a known divergence date).
- [ ] At no merged commit does the ledger page display a non-SMH relative delta under an SMH label (PR-1 ships the §2.3 compatibility items with the generator change).
- [ ] Calibration strip is grouped by benchmark bucket; book-level SMH line preserved; drift chart renders ≥7 days of `calibration-history.json`, with exactly one row per `generatedAt` date surviving same-day reruns.
- [ ] All 35 (→43) current-chain reports link `stanceTriggers.downgrade` to ≥1 monitoring item; a `breached` grade with an unchanged stance surfaces on the ledger within one cron cycle; `ENFORCE_TRIGGER_LINKS = True` on main with CI green.
- [ ] MSFT/GOOG initiated and AMZN chainized at full tier with grids, priced-in, v5 fields, trigger links; v4 `planned[]` queue executed (interconnect and advanced-packaging non-empty); demand-risk = 7 nodes.
- [ ] Quarterly note generator emits an appendix the first real note actually uses (dogfood on the Q3-2026 note).
- [ ] ZH/EN parity on every touched surface; no judgment colors anywhere new.

## 8. Risks & gotchas

- **Benchmark shopping.** Per-report overrides are an invitation to pick flattering yardsticks. Mitigation is structural, not honor-system: `benchmarkRationale` is validator-required on every override (§2.1) and the quarterly note generator lists all overrides with rationales verbatim. Layer defaults are the norm; overrides the audited exception.
- **Graded readings can rot** exactly like stale prices. `readingAsOf` older than the item's `nextCheckDate` renders as "ungraded" (fact, not alarm) — a grade past its own check date is not a grade.
- **Benchmark symbol availability/consistency in the fetch environment is unverified** (§2.1). Do the availability check *before* building anything on a symbol; this spec names candidates, not commitments.
- **Hyperscaler initiations are scope traps.** MSFT/GOOG reports serve the *demand-risk read-through* (capex absorption, AI revenue validation, own-silicon substitution) — they are not full platform teardowns. The chainRole framing (demand anchor, same as META) bounds the module list.
- **Two flags in flight.** `ENFORCE_TRIGGER_LINKS` overlaps Track 3 backfill; new reports must be authored link-complete from day one so the flip never waits on content (the v5 lesson: warn-first windows should shrink, not stretch).

## 9. Open questions for review

~~1. `copx-2026` benchmark: **decided SMH** (review round 1, §2.1 — rationale recorded there; user may veto).~~
~~2. demand-risk layer default: **decided QQQ** (review round 1, §2.1).~~
3. Stretch paper book: in or out of the v6 acceptance bar?
4. Track 3 P2 sequencing: any name the user wants front-loaded besides CCJ?
