# Research Hub v5 — Opinionated Verdicts & Expectations Discipline Spec

**Status:** Draft for user review · **Owner:** (unassigned — handoff to implementing agent) · **Author:** planning session, 2026-07-07
**Depends on:** Phase 0 (`34997b0`), Dashboard v2 (`d091cbf`), v3 Tracking (shipped through `45df76a`), v4 Coverage Depth & Tier (merged via `codex-research-hub-v4`, `1aa16d3`..`68f03aa`), all on `main`. v4's tier gate and the 12 depth upgrades are **shipped**; this cycle does not touch depth or tiers.
**Scope of this doc:** three tracks — **Track 1 verdict system redesign** (a stance schema that forces a directional, falsifiable call and makes "neutral" the expensive option instead of the default), **Track 2 expectations discipline** (a scenario grid + "what's priced in" module in every full report, so the stance is the *output of a documented calculation*, not a mood), and **Track 3 verdict ledger** (score every published stance against subsequent price action vs the SMH benchmark, so opinions have a track record and calibration improves). Track 1 is schema/validator/UI; Track 2 is content, run via the `company-research-publishing` skill; Track 3 is data/page work on the `prices.json` pipeline (per-report legs exist; the SMH benchmark leg must be added, §4.1a).

This spec is **self-contained** — an implementing agent should not need the originating chat.

**The problem it attacks:** the hub's verdicts are structurally mushy. Of the 35 current-chain reports, **24 are `neutral-watch`, 10 are `high-risk-watch`, 1 is `bearish-avoid`, and 0 are `constructive`** — the only positive value in the enum has never been used. A research book where 69% of names are "neutral" and 0% are "own this" does not support investment decisions; it describes companies. The neutrality is not an accident of the companies covered (the book includes names the reports themselves call "world-class assets" in an "AI supercycle") — it is the equilibrium the current system produces, for four identifiable reasons (§0). v5 changes the incentives and the format so the natural output is a dated, falsifiable, directional view.

---

## 0. Context & grounded facts (verified 2026-07-07)

| Fact | Value | Consequence |
|---|---|---|
| Stance distribution | 35 current-chain reports: `neutral-watch` 24, `high-risk-watch` 10, `bearish-avoid` 1, `constructive` 0. The 20 stance-less entries are archived `*-pre-rerun` versions and non-chain app reports (out of scope) | The problem is real and measurable; the acceptance test for this cycle is distribution + quality of rationale, not vibes |
| Stance enum | `validate_reports.py` `STANCE_VALUES` = `{constructive, neutral-watch, high-risk-watch, bearish-avoid}` (Phase 0 spec §A.2). 3 of 4 values are defensive; `constructive` has no assignment criteria anywhere in the skill or spec, so writers never reach for it | Root cause #1: the menu itself is risk-shaped. Track 1 replaces it |
| Methodology pressure | Skill doctrine (`references/research-methodology.md`): principle 3 "steelman both bull and bear," principle 6 "valuation is context only… no target prices." Nothing requires the conclusion to say **which side wins at today's price** | Root cause #2: the doctrine has a strong prior toward the middle and no counter-force. Track 2 adds the counter-force without breaking principle 6 |
| Accountability | v3 shipped price tracking (`prices.json`: per-report `basePrice`@`baseDate`, `lastClose`, `changePct`, refreshed by `update_prices.py` cron) and a rerun queue — but **nothing ever scores a stance**. A neutral call is never wrong, so neutral is the dominant strategy | Root cause #3: no feedback loop. Track 3 builds the scorecard on data that already exists |
| Semantic overload | `neutral-watch` currently covers ≥3 distinct states: "great company, fully priced" (TSMC: "中性观察/高质量但高预期"), "genuinely balanced," and "not enough conviction yet." `high-risk-watch` conflates direction with variance (OKLO = positive-skew lottery ticket; VST = crowded trade risk — same label) | Root cause #4: the labels can't express skew vs conviction separately. Track 1's two-axis design fixes this |
| `reports.json` fields in play | `stance`, `priceAsOf`, `reportedPeriod`, `monitoring[]` (required on current-chain), `coverageTier`, `versionType`, `lastUpdate`; enrichment enforced via `ENFORCE_CHAIN_ENRICHMENT = True` in `validate_reports.py` (blog repo, `static/invest/research/`) | Track 1 extends this validator; the warn-first→enforce flip pattern is established (used twice already) |
| `prices.json` | 35 entries: `{reportId, symbol, status, baseDate, basePrice, lastDate, lastClose, changePct, currency}`. `basePrice` is anchored at the report's `priceAsOf`. **SMH is NOT in the set**: `smh-2026` exists in `reports.json` as the v4 benchmark ETF report but has no `chainLayer`, no `priceSymbol`, no `priceAsOf`, no `stance` — and `update_prices.py` selects only current reports with a `chainLayer` + `priceSymbol` (`update_prices.py:99-102`) | Track 3 must **add benchmark ingestion** (§4.1a) — the per-report deltas exist, but the SMH leg does not. Also: because each report's stance window starts on its own date, the benchmark needs a *historical series*, not just base/last snapshots |
| The 35 current-chain set | = 33 `full` single-company + `neov-2026` (lite, single-company, `chainLayer: power`) + `copx-2026` (lite ETF, `chainLayer: resources`). `smh-2026` has no `chainLayer` → **outside the 35**, carries no stance, and is exempt from Tracks 1–2 by the existing chain predicate | Track 2 scope must name the lite/ETF variants explicitly (§3.3a); smh serves only as the Track 3 benchmark |
| Judgment history | Principle 11 + `incremental-revision-rules.md`: reruns/archives preserve old views; but a stance *change without a rerun* currently has nowhere to live | Track 1 adds `stanceHistory[]` so a stance flip is cheap (incremental update) yet auditable |
| Rendering | Pure static HTML + vanilla JS, `localize()`/`PAGE_LABELS` ZH/EN, DESIGN.md tokens. **Locked design rule: no red/green/amber or stance-colored judgment visuals** — stance chips are neutral-styled text | All new UI (verdict chip upgrade, ledger page) obeys this; the *text* carries the opinion, not the color |
| Dual-repo | Blog repo (this one) owns `reports.json`, validators, pages. Skill git source `~/Documents/codex-private-skills` owns templates, methodology, `check_research_package.py`; deploy by single-file copy to `~/.codex/skills/...` (never `install-local.sh` — it wipes skills) | Track 2's template/doctrine edits go to the skill git repo first, then deploy-copy |

---

## 1. Locked decisions (do not re-litigate)

1. **Stance = skew × conviction, two axes.** Direction alone can't express "OKLO: probably fails, but the payoff if it works dominates" vs "TSMC: excellent, fully priced." The verdict is (a) *expected risk/reward skew at today's price* and (b) *how much evidence backs it*. One label that mixes them (like `high-risk-watch`) is retired.
2. **The stance is derived, not declared.** §10 of every full report must show its work: scenario weights (Track 2) → expectation gap vs what's priced in → stance. A stance the reader can't recompute from the report's own scenario grid fails review.
3. **Neutral pays a tax.** `neutral-watch` remains legal but becomes the *most* demanding stance: it requires an explicit "what's priced in" statement plus **both** upgrade and downgrade triggers. "Neutral because we didn't decide" no longer passes the validator.
4. **No target prices — still.** Principle 6 survives amended: no single-point price targets, ever. What *is* now required: scenario **assumption ranges** (growth/margin/multiple, dated) and an **expectation-gap statement** ("at $434 the market is underwriting ~X% CAGR at Y% margins; our base case is Z"). Assumptions are falsifiable; price targets are marketing.
5. **Stance changes are cheap; silence is not.** A stance flip ships as an incremental update (new `stanceHistory[]` entry + refreshed `priceAsOf` + a dated ~200-word rationale in the report's update log), *not* a full rerun. A stance untouched for >120 days with fired monitoring triggers is flagged stale by the ledger.
6. **The ledger is benchmark-relative.** Absolute price moves flatter everything in a bull tape. Every scored call is measured against SMH over the identical window. A `constructive` call that lags SMH is a miss even if it's up.
7. **No quotas.** There is no target stance distribution. The forcing functions are per-report (tax, derivation, ledger); if the honest answer after the scenario work is still neutral, neutral stands. But the quarterly calibration note (§4.3) must discuss the distribution explicitly.
8. **Design rule holds.** All verdict UI uses neutral DESIGN.md chips — the words carry the opinion. No red/green.
9. **Warn-first rollout.** New required fields land with `ENFORCE_STANCE_V2 = False`, backfill proceeds report-by-report, flip to `True` when the 35 current-chain reports pass — same pattern as `ENFORCE_CHAIN_ENRICHMENT` and v4's tier gate.

---

## 2. Track 1 — verdict schema v2 (blog repo: schema + validator + UI)

### 2.1 Schema — replaces the flat `stance` enum

```jsonc
// reports.json, per current-chain report
"stance": "constructive",            // NEW enum, see 2.2
"conviction": "medium",              // NEW: high | medium | low
"stanceRationale": {                 // NEW: the one-line expectation-gap statement
  "zh": "市场在 $2.25T 定价了 N2/CoWoS 持续紧张到 2027；我们的 base case 同意方向但认为 2026H2 增速见顶,倾斜转平",
  "en": "At $2.25T the market prices N2/CoWoS tightness through 2027; our base case agrees on direction but sees growth peaking in H2'26 — skew flattens"
},
"stanceTriggers": {                  // NEW: required for ALL stances; both keys required for neutral-watch
  "upgrade":   { "zh": "…", "en": "…" },   // what makes this more bullish (metric + threshold)
  "downgrade": { "zh": "…", "en": "…" }    // what makes this more bearish
},
"stanceHistory": [                   // NEW: append-only; seeded with one entry at backfill
  { "stance": "neutral-watch", "conviction": "medium", "date": "2026-07-02", "price": 434.16 }
]
```

### 2.2 The new `stance` enum (5 values, skew-shaped)

| Value | Meaning (skew at today's price) | Chip label zh / en | Migration from old enum |
|---|---|---|---|
| `bullish` | Clearly positive asymmetry; would add on weakness | 看多 / Bullish | — (new; expect few, high bar) |
| `constructive` | Positive skew; build gradually, size by conviction | 偏多 / Constructive | `constructive` (unused) — now has criteria |
| `neutral-watch` | Balanced *after doing the scenario work*; taxed (§2.3) | 中性观察 / Neutral | `neutral-watch` — each of the 24 re-adjudicated, not carried over |
| `cautious` | Negative skew; don't add, trim into strength | 谨慎 / Cautious | most `high-risk-watch` where the risk is downside-shaped |
| `bearish-avoid` | Negative asymmetry; avoid / exit | 回避 / Avoid | `bearish-avoid` (CRWV) |

`high-risk-watch` is **retired**. Its 10 reports split by what the risk actually is: positive-skew venture bets (e.g. OKLO, NBIS pattern) become `constructive` or `bullish` with `conviction: low`; crowded/levered names (e.g. VST, ORCL pattern) become `cautious`. **Every one of the 35 is re-adjudicated individually during backfill (§3.3) — no mechanical mapping.** The table's last column is a starting hypothesis only.

### 2.3 Validator — `validate_reports.py`

Under `ENFORCE_STANCE_V2` (module-level flag, warn-first):

- `stance` ∈ new 5-value set; old values fail with a migration hint.
- Current-chain reports require `conviction`, `stanceRationale` (zh+en, non-empty), `stanceTriggers.downgrade` (zh+en).
- **Neutral tax:** if `stance == "neutral-watch"`, `stanceTriggers.upgrade` is also required, and `stanceRationale` must be present (it always is) — the rationale for neutral must state what's priced in (content-reviewed, not regex-enforced).
- `stanceHistory` required, non-empty, entries `{stance, conviction, date, price}`, dates ascending, last entry must match the top-level `stance`/`conviction`.
- **Legacy carve-out:** top-level `stance` accepts v2 values only, but `stanceHistory[].stance` accepts the union of v2 + legacy values (`high-risk-watch`, plus old-enum spellings) for **non-last** entries — history is evidence and is never rewritten. Only the last entry must be v2. `conviction` is optional on legacy entries (it didn't exist pre-v5).
- Archived (`isCurrent: false`) and non-chain reports: exempt, old values tolerated (do not rewrite history).

### 2.4 Frontend

- **`reports/view.html` + `index.html` cards:** stance chip renders new label + conviction as suffix text (e.g. "偏多 · 低确信 / Constructive · Low conviction"); `stanceRationale` renders as one line under the chip on view.html. Neutral chip styling, `localize()` for zh/en.
- **`monitoring-dashboard.html` verdict board:** group/order by stance (bullish → avoid), conviction shown; add a small distribution line ("24 neutral / 0 bullish" today — make the imbalance visible).
- **`coverage-map.html`:** stance text in node tooltips updates to new labels. No color changes anywhere.

---

## 3. Track 2 — expectations discipline (content, via publishing skill)

The stance must be recomputable from the report. Two new required blocks; scope by tier/type is exact (§3.3a):

### 3.1 §8 valuation gains a scenario grid + priced-in statement

- **Scenario grid** (table, 3 rows bull/base/bear): key driver assumptions (2–4 per scenario: revenue growth, margin, multiple regime — *drivers the report's own `monitoring[]` already tracks*), qualitative valuation implication (rich/fair/cheap vs today, or multiple range), and a **subjective probability weight** (rounded to 10%, sums to 100%).
- **Priced-in paragraph**: reverse-engineer what today's dated price implies (implied growth via simple multiple-vs-growth comparison or DCF-lite; show the arithmetic assumptions inline). Then state the **expectation gap**: base case vs implied. This paragraph is the source of `stanceRationale`.
- No single-point price target appears anywhere (locked decision 4).

### 3.2 §10 conclusion derives the verdict

§10 must contain, in order: (1) the chain-validation job (unchanged), (2) the expectation-gap sentence, (3) the stance + conviction **with the scenario weights cited** ("60/30/10 with the bear case requiring X — skew positive → constructive, medium conviction"), (4) the upgrade/downgrade triggers (mirrors `stanceTriggers`).

### 3.3 Backfill: re-adjudicate all 35, pilot-first

- **Pilot (3 reports, 1 PR each):** `tsmc-2026` (the archetypal "quality but neutral" — does the grid move it or justify the tax?), `oklo-2026` (tests skew-vs-conviction separation on a venture bet), `micron-2026` (tests a cyclical with live HBM drivers). Pilots set the format; user reviews before batch.
- **Batch (remaining 32 of the 35):** ships as **incremental updates** (Track 2 block per §3.3a scope + §10 rewrite + Track 1 fields for all; no re-research of the fact base — same "vetted fact base" rule as v4 Track 1). Batch by chain layer, one PR per 3–5 reports is acceptable here (unlike full reruns) since the fact bases are untouched.

### 3.3a Scope by report type (exact)

| Set | Track 1 fields (stance v2 etc.) | Track 2 block |
|---|---|---|
| 33 `full` single-company (incl. 3 pilots) | required | full scenario grid + priced-in paragraph (§3.1) |
| `neov-2026` (lite single-company) | required | **same scenario grid, reduced drivers** (2 per scenario is acceptable at lite depth) — a stance must be derivable regardless of tier |
| `copx-2026` (lite ETF) | required | **ETF variant**: no company scenario grid; instead a short "factor skew" block (underlying-commodity scenario + fund premium/flows) from which §10 derives the stance. `check_research_package.py`'s grid requirement keys off tier+type, reusing v4's ETF carve-out |
| `smh-2026` (benchmark ETF, no `chainLayer`) | **exempt from both tracks** (outside the chain predicate; carries no stance by design) | none — Track 3 benchmark only |
- **Seeding rule (deterministic, no ambiguity):** every backfilled report seeds `stanceHistory[]` with entry 1 = its **pre-v5 legacy stance** at the original `priceAsOf`/`basePrice` (legacy value verbatim — allowed by the §2.3 carve-out, no `conviction`). If the v2 re-adjudication changes the verdict (all 10 `high-risk-watch` by definition, plus any neutral that moves), append entry 2 = the v2 stance at the backfill date/price. If the verdict is materially unchanged (e.g. `neutral-watch` → `neutral-watch`), entry 1 is simply re-expressed with the new `conviction` added and no second entry — the clock keeps the original date. Legacy→v2 intervals created by migration render in the ledger's closed table flagged **"migration"** and are excluded from calibration stats (§4.2) — the enum change is not a call.

### 3.4 Skill repo (`~/Documents/codex-private-skills`) changes

- `assets/templates/report.zh.md` / `report.en.md`: scenario-grid table skeleton in §8, §10 four-part structure, enrichment comment block updated for the new fields.
- `references/research-methodology.md`: amend principle 6 (assumption ranges + expectation gap required; point targets still banned); add **principle 13: "Verdicts are derived and scored."**
- `references/valuation-methods.md`: add the reverse-multiple / DCF-lite "priced-in" recipe (one page, with a worked example).
- `check_research_package.py`: full-tier gate additionally requires a ≥3-row table in §8 containing scenario keywords (bull/base/bear · 牛/基准/熊) — same keyword-detection style as the existing module checks.
- Deploy by single-file copy; commit to the skill git repo in the same cycle.

---

## 4. Track 3 — verdict ledger (accountability)

### 4.1 Data — `scripts` + `data/verdicts.json` (generated)

Extend `update_prices.py` (or a sibling `update_verdicts.py` reusing its fetch layer) to emit `data/verdicts.json` on the same cron:

```jsonc
{ "generatedAt": "2026-07-07", "benchmark": "SMH", "entries": [ {
  "reportId": "tsmc-2026", "stance": "neutral-watch", "conviction": "medium",
  "stanceDate": "2026-07-02", "priceAtStance": 434.16, "lastClose": 441.02,
  "changePct": 1.6, "benchmarkChangePct": 2.3, "relativePct": -0.7,
  "daysHeld": 5, "stale": false     // stale: >120d AND any monitoring nextCheck passed
} ] }
```

`priceAtStance` comes from the last `stanceHistory[]` entry (falling back to `prices.json` `basePrice` when dates match). Benchmark window = same stanceDate→lastDate window on SMH. Prior `stanceHistory[]` entries yield **closed intervals** (entry price → next-entry price, vs SMH), so flips accumulate a record (migration intervals flagged and excluded from stats, §3.3). New validator `validate_verdicts.py` mirroring `validate_prices.py` conventions; wire into CI beside it.

### 4.1a Benchmark ingestion (prerequisite — SMH is not in the price pipeline today)

`smh-2026` currently has no `priceSymbol`/`priceAsOf`, and `update_prices.py:99-102` selects only current reports with a `chainLayer`, so SMH never enters `prices.json`. Two changes:

1. **Metadata:** add `priceSymbol: "SMH"` and `benchmark: true` to `smh-2026` in `reports.json`; widen the `update_prices.py` selection predicate to `(chainLayer OR benchmark) AND isCurrent ≠ false AND priceSymbol` so SMH gets a normal `prices.json` entry (snapshot uses; keeps the ticker sourced from data, not hardcoded). `validate_reports.py` allows `benchmark` as a boolean and continues to exempt benchmark-only reports from chain enrichment.
2. **Series:** snapshots aren't enough — every report's stance window starts on a different date, so the verdicts generator fetches the **SMH daily-close history** covering `min(stanceHistory dates)→today` through the same fetch layer `update_prices.py` uses (keep `test_update_prices.py` green; follow `validate_prices.py` failure-status conventions on fetch errors). Closes are looked up per window edge (nearest prior trading day); the resolved per-entry benchmark values are persisted in `verdicts.json` so the page never fetches.

### 4.2 Page — `verdict-ledger.html` (判断记录 / Verdict Ledger)

Static page, existing conventions (vanilla JS, `localize()`, DESIGN.md, linked from the hub nav + monitoring dashboard):

- **Open calls table:** report, stance+conviction chip, stance date, price@stance, now, Δ%, Δ vs SMH, days held, stale flag. Sortable by relative delta. Neutral rows show deltas too — a "neutral" that SMH beat by 40% is information.
- **Closed calls table:** every completed `stanceHistory[]` interval: old stance, window, Δ vs SMH over the interval. Legacy→v2 migration intervals render here flagged "migration."
- **Calibration strip:** counts by stance, median relative delta per stance bucket, % of non-neutral calls beating SMH — **migration intervals excluded**. Plain numbers, no scoring colors.

### 4.3 Cadence — quarterly calibration note

A short dated markdown note (pattern: existing signal/review notes) each quarter: distribution of stances, best/worst relative calls, which `stanceTriggers` fired without a stance change (misses of process, not just outcome), and whether the neutral share is justified. First one due with the quarter after backfill completes. This is authored (skill checklist item), not generated.

---

## 5. Delivery slicing & gates

| PR | Content | Gate |
|---|---|---|
| PR-1 | Track 1 schema + `validate_reports.py` v2 rules (`ENFORCE_STANCE_V2 = False`) + chip UI reading old *and* new enums | validators green on untouched data; `hugo --minify` clean |
| PR-2 | **Skill repo first**: templates + methodology + valuation recipe + `check_research_package.py` grid gate (git source, then deploy-copy) — the pilots must be authored against and prove the gate, not manual discipline | skill repo tests green; gate verified to *fail* on a current un-upgraded report |
| PR-3..5 | Pilot reports ×3 (TSMC, OKLO, MU): scenario grid + §10 + new fields + seeded `stanceHistory[]`, authored with the PR-2 template and passing the PR-2 gate | per-report: `check_research_package.py`, `validate_reports.py`, zh/en parity; **user reviews pilot format before batch**; gate/template fixes discovered here go back to the skill repo in the same PR |
| PR-6..N | Batch backfill, 3–5 reports per PR by chain layer | same per-report gates |
| PR-N+1 | Flip `ENFORCE_STANCE_V2 = True`; retire old enum values for current-chain top-level `stance` (history keeps legacy values, §2.3) | full CI green |
| PR-N+2 | Track 3: benchmark ingestion (§4.1a) + verdicts generator + `validate_verdicts.py` + `verdict-ledger.html` + nav links | `test_update_prices.py` + `validate_prices.py` green with SMH included; generated file validates; page renders both open and (initially near-empty) closed tables |

Tracks 1→2→3 in that order (with the skill-repo PR-2 fronting Track 2); Track 3 can start after PR-1 (schema exists) but ships after enough backfill to be non-embarrassing (≥15 reports).

## 6. Acceptance criteria

- [ ] All 35 current-chain reports carry new-enum top-level `stance`, `conviction`, `stanceRationale`, `stanceTriggers` (downgrade always; upgrade for neutrals), non-empty `stanceHistory[]`; zero `high-risk-watch` remaining as a **top-level** stance (legacy values persist inside `stanceHistory[]` per §2.3); archived reports untouched; `smh-2026` untouched by Tracks 1–2.
- [ ] Track 2 blocks per §3.3a scope: all 33 full reports + neov have a bull/base/bear scenario grid with probability weights summing to 100% and a priced-in paragraph; copx has the ETF factor-skew variant; §10 cites the weights; zero single-point price targets (grep-audit both languages).
- [ ] The 24 former neutrals were each re-adjudicated with the grid; whatever the resulting distribution, each surviving `neutral-watch` passes the tax (both triggers + priced-in statement). The verdict board shows the distribution line.
- [ ] SMH is ingested per §4.1a (`priceSymbol`/`benchmark` on `smh-2026`, widened `update_prices.py` predicate, SMH entry present in `prices.json`); `verdict-ledger.html` renders live open-call deltas vs SMH from generated `verdicts.json`; a manual stance flip on one report (test fixture or real) produces a closed interval row; migration intervals are flagged and excluded from calibration stats.
- [ ] Skill git repo updated + deploy-copied; a fresh report generated from the updated template passes all gates with the new fields.
- [ ] `ENFORCE_STANCE_V2 = True` on main with CI green; ZH/EN parity holds on every touched report.

## 7. Risks & gotchas

- **Fake conviction is worse than honest neutrality.** The pilot review must check that grids aren't reverse-engineered to justify a pre-chosen stance. The tell: probability weights that are all 60/30/10 regardless of name.
- **Scenario weights drift stale faster than fact bases.** That's what `stanceTriggers` + the stale flag + locked decision 5 (cheap flips) are for — enforce in the quarterly note.
- **`update_prices.py` has tests** (`test_update_prices.py`); extend rather than fork the fetch layer, keep the tests green, and follow `validate_prices.py`'s failure-status conventions for symbols that error.
- **Don't rewrite archived reports** to the new enum — history is evidence (principle 11).
- **Skill deploy trap** (recurring): edit `~/Documents/codex-private-skills`, copy files; never run `install-local.sh`.

## 8. Out of scope (explicitly)

- Target prices, position sizing, portfolio construction, or any per-user advice (site remains research, not signals-for-sale).
- Auto-derived stances (no rule that flips a stance from price moves — humans flip, ledger records).
- Backtesting old archived stances retroactively; the ledger's clock starts at backfill.
- Pre/post-earnings expectation notes and a chain-level "posture" aggregate — good v6 candidates once the ledger has a quarter of data; noted here so they aren't re-invented from scratch.
