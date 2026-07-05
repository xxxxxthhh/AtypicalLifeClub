# Research Hub v4 — Coverage Depth & Tier Governance Spec

**Status:** Ready to implement · **Owner:** (unassigned — handoff to implementing agent) · **Author:** planning session, 2026-07-06
**Depends on:** Phase 0 (`34997b0`), Dashboard v2 (`d091cbf`), and v3 Tracking (`34cba79` spec / shipped through `45df76a`), all on `main`. The v3 accountability loop (price tracking, rerun queue, signal cadence, RSS, market-context strip) is **shipped**; this cycle does not touch it.
**Scope of this doc:** three tracks — **Track 1 depth upgrades** (raise the 12 structurally-incomplete chain reports to the full depth contract), **Track 2 breadth** (add CCJ/MP to `planned[]`, add SMH as a benchmark ETF report, and scout new-layer names), and **Track 3 tier governance** (a `coverageTier` field + a depth gate that catches thin `initial` reports so they can no longer ship silently). Track 3 is the site/tooling enhancement; Tracks 1–2 are the content track, run via the `company-research-publishing` skill.

This spec is **self-contained** — an implementing agent should not need the originating chat. The problem it attacks: the coverage queue (`planned[]`) is empty, but the chain is not uniformly deep. Some `initial` reports meet the house depth contract (TSM, META, ORCL at 12 §/ ~60 table rows) while others ship as **zero-table ~700-word stubs** (ASML, AMAT, LAM, KLA, SNPS, CDNS) or **half-depth lite reports** (NRG, EQIX, CEG, VST, COHR, DLR). These thin reports pass CI because the depth gate is `full-cycle`-only. v4 closes the loop the other direction from v3: v3 made the hub *accountable after publication*; v4 makes it *uniformly deep at publication* and makes depth a governed, enforced contract instead of an editorial hope.

---

## 0. Context & grounded facts (verified 2026-07-06)

| Fact | Value | Consequence |
|---|---|---|
| `reports.json` | 54 entries, 45 current (`isCurrent ≠ false`). **35 current-chain entries** = those with a `chainLayer` set (identical to the 35 `priceSymbol` / `prices.json` entries) | Tracks 1 & 3 operate on the 35 current-chain set; the 10 non-chain legacy reports (tempus-ai, igv, airbnb, hims, salesforce, coinbase, amzn, netflix, spotify, paypal) are out of scope here |
| Depth split of the 35 chain reports (measured per-language, min of zh/en, 2026-07-06) | The clean structural break is the **`##` count**, not row count: **12 reports have 7 `##`** (incomplete module set) — 6 zero-table stubs (ASML, AMAT, LAM, KLA, SNPS, CDNS) + 6 lite (NRG, VST, COHR, DLR, EQIX, CEG, 32–34 rows). **22 reports have 11–14 `##`** (complete analytical module set), with table density spanning 21→93 rows by template era. 1 ETF (copx, 13 §/79 rows). Full authoritative table in §2.1 | Track 1's committed set = the **12** structurally-incomplete reports. The 22 complete reports are tagged `full`; the 6 table-light ones (see §2.1) are an optional density backlog, **not** mislabeled |
| Floor calibration lesson | A literal `≥12 ## AND ≥40 rows` floor (an earlier draft of this spec) misclassifies `sk-hynix` (93 rows/11 §) and `neov` (52 rows/11 §) as "below full" on an 11-vs-12 `##` technicality — nonsensical. The `full` floor is therefore defined on **module completeness + a real table spine**, not an arbitrary row count (§4.1/§4.3) | Prevents the tier gate from becoming fake governance in either direction |
| Depth gate | `check_research_package.py` (skill repo `~/Documents/codex-private-skills`) runs a depth gate **only for `versionType == "full-cycle"`** (ratio vs `diffBase` baseline). `initial` reports have **no** depth requirement — `validate_reports.py:141,151` only distinguishes required *metadata* fields by version type | The 6 zero-table stubs are `initial`, so nothing fails them. Track 3 fixes this |
| `validate_reports.py` | blog-repo CI validator, stdlib only, `fail()` + `sys.exit(1)` on first error. Enrichment lives in `validate_enrichment_fields()`; the chain predicate is `is_current_chain = bool(report.get("chainLayer")) and report.get("isCurrent") is not False`; precedent flag `ENFORCE_CHAIN_ENRICHMENT = True` was flipped after a backfill | Track 3 adds `coverageTier` validation here, mirrors the `ENFORCE_*` flip pattern |
| `check_research_package.py` | skill-repo depth checker: keyword-based core-module detection on `#`-headings per language; hard-fails on number-density / table-row ratios and a per-section stub floor; flags `--min-depth-ratio` `--min-table-ratio` `--section-min-chars` `--no-depth-check`; per-report escape hatch `depthBaselineWaived`. **Source of truth is the git repo `~/Documents/codex-private-skills`**; deploy by single-file copy to `~/.codex/skills/company-research-publishing/scripts/` (do **not** run `install-local.sh`, it `rm -rf`s every skill) | Track 3 extends this with an **absolute** per-tier floor for `initial`/`incremental` reports (they have no baseline to diff) |
| `coverage-map.json` | keys `page`/`layers`/`roles`/`planned`/`crossChecks`; `planned[]` is **empty** (queue exhausted); 12 `layers` incl. `semicap-equipment`, `eda-ip`, `foundry` (hidden while its only member renders elsewhere); 10 `crossChecks` incl. the new `semicap-eda-capex-commitment` | Track 2 refills `planned[]` and may add layers/crossChecks; `validate_coverage_map.py` already covers `planned[]` schema |
| Reference full report shape | Contemporary template: TSM 12 `##` / 60 rows, META 12 / 66. Older complete reports run lighter: NVDA 12 / 21, BROADCOM 12 / 23. The stubs: 7 `##` / 0 | The `full` **gate floor** = module completeness + table spine (§4.3); the **authoring target** for new/upgraded full reports = the contemporary ~40–66-row template (§2.2). Floor ≠ target |
| Source material for the 12 thin reports | each stub/lite already carries a **web-verified Q1 2026 fact base + a `prices.json` price ledger** (e.g. ASML: Q1 net sales EUR 8.767B, backlog EUR 38.8B, ADR $1,769.32) | Track 1 is *depth expansion over a vetted fact base*, not from-scratch research — do not re-derive, do not fabricate new actuals |
| Pages / rendering | pure static HTML + vanilla JS, `localize()` + `PAGE_LABELS` for ZH/EN, DESIGN.md tokens, no libraries. `index.html` cards, `reports/view.html?id=`, `coverage-map.html` nodes | Track 3's tier chip follows these conventions |
| Design system | `DESIGN.md` is now formal; **locked rule: no red/green/amber or stance-colored judgment visuals** | The tier chip is a neutral chip, never color-graded |

---

## 1. Locked decisions (do not re-litigate)

1. **Depth is measured, not vibed.** The house standard is the Batch-1 depth contract: 12 numbered `##` sections, the standard data tables (quant snapshot, segment breakdown, financial-health matrix, multi-method valuation, peer comparison), bull/bear with explicit price levels, key uncertainties + thesis-breakers, catalysts (near/med/long), appendix & sources. Do **not** chase raw word count — density (numbers, tables, segment detail) is the target; body-size is advisory only.
2. **Preserve the vetted fact base.** Track 1 keeps each report's existing web-verified Q1 2026 actuals and price ledger; it *adds* scaffolding (tables, segment breakdowns, valuation paths, peer tables, catalysts). Do not fabricate new quarters or restate figures the report did not already establish. Where a figure is counterintuitive, add a caliber/source note (company-disclosed / as-reported).
3. **EN/ZH parity is exact.** Every upgraded report ends with identical `##` / `###` / table-row counts across the two language files and zero `~~` redline artifacts, matching current practice.
4. **`coverageTier` is a governed contract, not a downgrade license.** The tier a report declares sets the depth floor it is gated against. The *goal of this cycle* is that all 12 thin reports reach `full`. `seed` and `lite` remain valid declared states for genuinely new initiations and interim drafts, but a report may not sit below its layer's intended depth indefinitely — the rerun/queue surfaces persist, the tier chip makes the state visible.
5. **The tier gate rolls out warn-first.** Backfill `coverageTier` on all 35 current-chain reports, land the validator in advisory mode, upgrade the 12, then flip `ENFORCE_COVERAGE_TIER = True` — mirroring how `ENFORCE_CHAIN_ENRICHMENT` was flipped only after its backfill so CI never goes red mid-migration.
6. **Factual board carries over.** The tier chip is a neutral chip (DESIGN.md tokens), never color-graded by "good/bad." It states a fact ("this report is at Full depth"), not a quality verdict.
7. **ETFs are exempt from the single-company depth contract.** SMH (Track 2) and the existing igv/copx use a holdings/factor refresh, not the 12-section company template; their `coverageTier` is `lite` with an ETF carve-out in the gate (see §4.2).
8. **One report per branch/PR** for content (Track 1 upgrades and Track 2 new reports), gated by the validators + `hugo --minify` + review, matching existing practice. Track 3 (tooling) is its own PR set.

---

## 2. Track 1 — depth upgrades (content, via publishing skill)

Raise the **12 structurally-incomplete** chain reports (7-`##`, incomplete module set) to the full depth contract. Each is a `versionType: initial` report **staying `initial`** (it is still the first real coverage of the name — this is not a rerun of a prior version); the change is depth, and its `coverageTier` flips `seed`/`lite` → `full` when it lands.

### 2.1 Measured tier inventory (authoritative, per-language min of zh/en, 2026-07-06)

This is the single source of truth for the PR-1 backfill (§5). Tier is assigned by the §4.1 floor: **seed** = 0 tables; **lite** = has tables but incomplete module set (the 7-`##` reports); **full** = complete module set + real table spine.

| Tier | Count | Reports (`##` / rows) |
|---|---|---|
| **seed** → Track 1 | 6 | asml (7/0), applied-materials (7/0), lam-research (7/0), kla (7/0), synopsys (7/0), cadence (7/0) |
| **lite** → Track 1 | 6 | nrg (7/32), vistra (7/32), coherent (7/32), digital-realty (7/32), eqix (7/33), constellation-energy (7/34) |
| **full** (already) | 16 | corning (12/42), sandisk (12/42), jinpan (12/42), arista (12/44), oklo (12/51), neov (11/52), bloom-energy (12/54), nebius (12/58), micron (12/58), marvell (12/59), tsmc (12/60), oracle (12/60), almonty (12/66), meta (12/66), sk-hynix (11/93), amd (14/83) |
| **full** — *density backlog* (complete but table-light vs the contemporary norm; optional later re-deepen, **not** this cycle's commitment, **not** mislabeled) | 6 | nvidia (12/21), broadcom (12/23), gevernova (12/27), coreweave (12/30), aaoi (12/34), vertiv (12/39) |
| **lite** — ETF carve-out (§4.2) | 1 | copx (13/79) |

**Committed Track 1 upgrade set = the 12 seed+lite reports** (the only ones below the module-completeness floor). The 6 density-backlog reports are already `full` (complete structure); whether to re-deepen them to the contemporary ~40+-row norm is an **open decision** (see §2.5) — the default is *defer*, tag them `full` now.

### 2.1a The 12 committed targets, in execution order

Worst-first: the 6 zero-table stubs (they currently fail the *spirit* of the contract hardest), then the 6 lite reports (which already have ~32-row tables and only need to reach 12 sections / ~60 rows).

| # | Report id | Ticker | Layer | Current shape | Target | Fact-base already present |
|---|---|---|---|---|---|---|
| 1 | `asml-2026` | ASML | semicap-equipment | 7 §/0 tbl/822w | full | Q1 net sales EUR 8.767B, GM 53.0%, Q4 bookings EUR 13.158B (EUV 7.4B), backlog EUR 38.8B, ADR $1,769.32 |
| 2 | `applied-materials-2026` | AMAT | semicap-equipment | 7 §/0 tbl/703w | full | Q1 actuals + price ledger in current stub |
| 3 | `lam-research-2026` | LRCX | semicap-equipment | 7 §/0 tbl/693w | full | " |
| 4 | `kla-2026` | KLAC | semicap-equipment | 7 §/0 tbl/715w | full | " |
| 5 | `synopsys-2026` | SNPS | eda-ip | 7 §/0 tbl/655w | full | " (fold in the pending Ansys-deal caliber note) |
| 6 | `cadence-2026` | CDNS | eda-ip | 7 §/0 tbl/650w | full | " |
| 7 | `nrg-2026` | NRG | power | 7 §/32 tbl/1456w | full | watch the ~$12B LS Power gas-fleet deal (don't repeat the Calpine/CEG miss) |
| 8 | `eqix-2026` | EQIX | datacenter-facility | 7 §/33 tbl/1314w | full | AFFO-based multiples, interconnection/xScale |
| 9 | `constellation-energy-2026` | CEG | power | 7 §/34 tbl/1300w | full | Calpine acquisition already in the fact base — keep it |
| 10 | `vistra-2026` | VST | power | 7 §/32 tbl/1136w | full | pairs NRG |
| 11 | `coherent-2026` | COHR | optical | 7 §/32 tbl/1124w | full | optical/datacom transceivers, laser mix |
| 12 | `digital-realty-2026` | DLR | datacenter-facility | 7 §/32 tbl/1089w | full | lease/backlog, pairs EQIX |

### 2.2 Per-report depth contract (the "full" target)

Each upgraded report must, in **both** language files:

- **12 numbered `##` sections** following the house template: (1) business & chain role, (2) competitive position, (3) financial-health matrix, (4) red-flag / caliber check, (5) bull case, (6) bear case, (7) key uncertainties & thesis-breakers, (8) multi-method valuation, (9) catalysts (near/med/long), (10) peer comparison, + executive summary and appendix & sources. Adjust numbering to the existing house template; keep the chain-role framing the stub already leads with.
- **Standard data tables** totalling **≥ 40 table rows** (this is the *authoring target* for a newly-upgraded full report, ~55–65 matching TSM/META; the mechanical *gate floor* in §4.3 is lower — module completeness + a real table spine — so it does not retroactively fail the older complete reports): a quantitative snapshot table, a segment/revenue breakdown, a financial-health matrix, a multi-method valuation table, and a peer-comparison table. The 6 lite reports keep their existing ~32 rows and extend; the 6 stubs build all tables from their existing prose figures.
- **Bull and bear cases with explicit price levels** and measurable thesis-breakers (kill-criteria), matching the CRWV/NBIS pattern.
- **Heading keywords that satisfy the module detector** (see §4.4): ZH must use 牛市/熊市/催化/监测/不确定性/附录 (not bare 看多/看空/观察); EN bull/bear/catalyst-monitoring/uncertainties/appendix.
- **Caliber notes** on counterintuitive or company-disclosed figures; the appendix carries the peer table + key assumptions + source links (per the coinbase reference template).
- **Cross-check wiring:** each report's monitoring items should reference the relevant `crossChecks` id (`semicap-eda-capex-commitment` for the semicap/EDA six; `merchant-power-capacity` for NRG/CEG/VST; `facility-interconnection-leasing` for EQIX/DLR; `chip-vs-downstream` for COHR).

### 2.3 Metadata on upgrade

- Keep `versionType: initial`, `chainLayer`, `chainRole`, `priceSymbol`, `stance`, `priceAsOf`, `reportedPeriod`, `monitoring[]` as-is (refresh `priceAsOf`/price ledger only if a newer close is pulled).
- Set `coverageTier: "full"` (Track 3 field).
- Bump `lastUpdate` to the upgrade date so the report re-surfaces in the RSS feed (`generate_feed.py` sorts by `lastUpdate`) and the rerun queue re-ages it. Run `generate_feed.py` after editing `reports.json`.
- Scrub any restated old anchor from `summary`/`highlights` (the metadata stale-pattern check has **no allowlist**); on-line `old`/`旧` tags only protect body lines.

### 2.4 Per-report verification loop

`python3 static/invest/research/validate_reports.py` → `check_research_package.py static/invest/research --report-id <id>` (now exercising the new tier floor, §4.3) → EN/ZH `##`/`###`/table-row parity + zero `~~` → `hugo --minify` then `git checkout -- hugo_stats.json`. Interleave ~1 Batch-2 legacy rerun per 1–2 upgrades if capacity allows (out of scope to require here; the v3 rerun queue ranks them).

### 2.5 Open decision — density backlog (6 legacy-light full reports)

nvidia (21 rows), broadcom (23), gevernova (27), coreweave (30), aaoi (34), vertiv (39) are structurally complete (`full`) but table-light versus the contemporary ~40–66-row template. They are **not** mislabeled — they carry the full module set — and re-deepening them is lower-value than fixing the 12 incomplete reports. **Default: defer** (tag `full` now, leave for a later densification pass; the v3 rerun queue will surface them by age/drift). If the reviewer prefers a stricter bar, promote them into Track 1 as a second wave (Track 1b) — but do not gate this cycle on them. This is the "expand Track 1 **or** tag them at their honest tier" fork; the spec takes the honest-tier path by default.

---

## 3. Track 2 — breadth (content + data)

Refill the coverage queue and scout genuinely new chain questions. Two sub-parts: the **confirmed tail** (CCJ/MP/SMH, previously specced, just never landed) and a **scout longlist** evaluated against a rubric.

### 3.1 Confirmed tail

Two of the three go into `planned[]`; SMH does not (schema constraint — see the caution box).

**Into `planned[]`** (data-only PR, see §5) with bilingual gap labels, then written as full reports via the skill (born at `coverageTier: full`):

| Ticker | Layer (`coverage-map` id) | Role | Cross-check pairing |
|---|---|---|---|
| **CCJ** | `resources` | check | uranium fuel cycle = picks-and-shovels check on the OKLO high-risk-watch position and the CEG/VST nuclear-baseload reads |
| **MP** | `resources` | anchor | magnets / rare-earth = strategic-metals + policy continuation of the Almonty (tungsten) line; ties to GEV/VRT/motor supply |

**SMH — benchmark ETF, NOT a `planned[]` entry.** `validate_coverage_map.py:125` requires every `planned[]` item to carry a `layer` that hits a known layer id, and a semis ETF spans compute/semicap/memory/etc. with **no single-name layer** — so a layer-less SMH entry would fail the validator. Follow the **igv precedent**: igv (software ETF) is a report in `reports.json` with **no `chainLayer`** and **no coverage-map node**. SMH is added the same way — a benchmark report (`coverageTier: lite`, ETF carve-out §4.2), tracked in `reports.json`, tagged as a benchmark in `tags`, but *not* a chain node. (If you instead want SMH visible as a benchmark node on `coverage-map.html`, that requires first making `layer` optional for a new `kind: "benchmark"` planned item in the schema + validator + renderer — a deliberate scope add, not assumed here.)

### 3.2 Scout longlist → evaluate, then `planned[]`

The user asked to scout new layers. Evaluate each against the **selection rubric** and add only those that pass:

**Rubric (all four must hold):** (a) validates or falsifies a *distinct* chain question not already answered by an existing report; (b) is a public, liquid name with disclosed financials (no thin-float or private-only); (c) pairs as a named cross-check with ≥1 covered report; (d) has a real 2026 fact base to anchor a full report.

| Candidate | Proposed layer | Distinct question it answers | Note |
|---|---|---|---|
| **ALAB** (Astera Labs) | new `interconnect` layer (or fold into `networking`) | Does PCIe/CXL retimer/interconnect content scale with GPU-cluster fan-out — a *different* bottleneck than Ethernet fabric (ANET) or optics (COHR/AAOI)? | strongest scout candidate; likely a new layer |
| **PWR** (Quanta) | `power` (grid-EPC) | Is the grid-*construction* constraint (EPC labor/backlog) confirming the equipment-order reads (GEV/金盘/VRT)? | roadmap already preferred PWR over ETN (overlap with VRT+GEV) |
| **Advanced-packaging / substrate name** (e.g. Amkor `AMKR`, or an OSAT/substrate/inspection name) | new `advanced-packaging` layer or fold into `semicap-equipment` | Is CoWoS / HBM-stacking / substrate capacity the *real* choke point behind foundry capex (TSM) and memory (MU/SK hynix)? | pick one name; confirm public + liquid |
| **Liquid-cooling pure-play** | `datacenter-facility` | Is direct-liquid-cooling adoption a distinct signal from VRT's blended thermal mix? | **only if** a genuine public pure-play with disclosed financials exists; else drop — do not force a thin-float name (rubric b) |

For any candidate that introduces a **new layer**, add a `layers[]` entry (bilingual title + description) and, where it enables a new falsification path, a `crossChecks[]` entry (bilingual `if`/`then`, stable `id`) in the same data-only PR. **Gotcha:** `validate_coverage_map.py` hard-checks `layers` against a frozen `EXPECTED_LAYERS` list **by ids and order** (line 29/110) and `roles` against `EXPECTED_ROLES` — a new layer or role id must be added to that constant in the same PR or CI fails. The chain graph on `coverage-map.html` also renders layers in that fixed order, so pick the insertion point deliberately (e.g. `interconnect` adjacent to `networking`).

### 3.3 Interleave with the Batch-2 legacy backlog (advisory)

The **non-chain** legacy reports still on `incremental` (airbnb, amzn, netflix, spotify, paypal, igv, salesforce) — those with **no `chainLayer`** — are a separate, older depth backlog, **not required by this cycle**. The v3 rerun queue ranks them; fold in opportunistically, do not block Track 1/2 on them.

**Not in that group (they ARE current-chain, so they get a `coverageTier` in PR-1):** `neov-2026` (`chainLayer: power`, `reports.json:3115`) measures 11 §/52 rows → complete module set → tag **`full`** (not an upgrade target). `copx-2026` (`chainLayer: resources`, `reports.json:3227`) measures 13 §/79 rows but is an ETF → tag **`lite`** with the ETF carve-out (§4.2), holdings-refresh not single-company depth. Both therefore have a definite tier and do not leave a gap in the PR-Flip condition (§6).

---

## 4. Track 3 — tier governance gate (site/tooling enhancement)

Make depth a first-class, enforced field so a thin `initial`/`incremental` report can no longer ship silently. Three pieces: the `coverageTier` field + CI field/consistency/table-floor validation (`validate_reports.py`), the absolute per-tier depth floor for `initial`/`incremental` reports (`check_research_package.py`, skill repo), and a neutral tier chip in the UI.

### 4.1 Schema — `coverageTier`

```jsonc
{
  "id": "asml-2026",
  "chainLayer": "semicap-equipment",
  "coverageTier": "full",   // NEW: "seed" | "lite" | "full"
  // ...all other fields unchanged...
}
```

Tier definitions — assigned on **module completeness + table presence**, not an absolute row count (the row-count knife misclassifies deep-but-fewer-sections reports like sk-hynix 93 rows / 11 §; see §0):
- **`seed`** — first-look note: the 6–7-section shape (exec summary, business/chain role, bull/bear, monitoring, valuation, conclusion, appendix), **no data tables**. Legitimate for a just-initiated name that anchors a layer before its full write-up.
- **`lite`** — has data tables (≥1 table, ≥6 rows) but an **incomplete module set** — the 7-`##` reports that fold competition / financial-health / key-uncertainties / peer into fewer sections. The current NRG/EQIX/CEG/VST/COHR/DLR level.
- **`full`** — the **complete analytical module set** present (business, competition, financial-health, bull, bear, key-uncertainties, valuation, catalysts, peer, appendix — detected by the heading-keyword detector; empirically the ≥11-`##` reports) **and** a real table spine, with EN/ZH parity. Table density beyond the spine varies by template era (21→93 rows); the *authoring target* for a newly-upgraded full report is the contemporary ~40–66-row template (§2.2), but that is a target, not the gate floor (§4.3).

### 4.2 CI validation — `validate_reports.py` (blog repo)

In `validate_enrichment_fields()` (stdlib, per existing style):

1. **Value check:** if `coverageTier` present, it must be one of `{"seed","lite","full"}`.
2. **Version consistency:** `versionType == "full-cycle"` ⇒ `coverageTier` must be `"full"` (a full rerun cannot be a seed/lite); `seed`/`lite` are only valid on `initial`/`incremental`.
3. **Zero-table backstop (closes the exact hole the user named):** for a current-chain report with `coverageTier ∈ {"lite","full"}` **and** not an ETF (`"ETF" not in report["tags"]`, per point 5), open both `markdownFiles` and assert each contains ≥1 markdown table (a line matching `^\s*\|.*\|`). This is a cheap CI-hard check so a `lite`/`full` report with zero tables fails `validate_reports.py` even though the rich density gate lives in the skill checker. (Reading the two files is a small addition; the validator already resolves and stats them.)
4. **Required-after-backfill:** add `ENFORCE_COVERAGE_TIER = False` next to `ENFORCE_CHAIN_ENRICHMENT`. When `True`, every current-chain report must carry `coverageTier`. Flip to `True` in the final PR, after the backfill + the 12 upgrades, exactly as `ENFORCE_CHAIN_ENRICHMENT` was flipped.
5. **ETF carve-out:** detect ETFs by the existing convention **`"ETF" in report["tags"]`** (confirmed: igv/copx carry an `"ETF"` tag; `category` is `tech`/`energy`/`nuclear`, there is no `etf` category — do not add one). An ETF is exempt from checks (2)-consistency-to-full and (3)-table-floor and may sit at `lite` without the single-company table set.

### 4.3 Depth floor — `check_research_package.py` (skill repo `~/Documents/codex-private-skills`)

Today the depth gate runs only for `full-cycle` — confirmed at `check_research_package.py:247` (`if depth_config is not None and report.get("versionType") == "full-cycle": validate_depth(...)`). Extend it so `initial`/`incremental` reports are gated by an **absolute** floor keyed on `coverageTier` (no `diffBase` baseline exists for these versions):

- **`coverageTier == "full"`** (and `versionType ∈ {"initial","incremental"}`): **(primary)** require all core modules detected by the keyword-on-headings detector — this is the check that separates the 7-`##` lite reports (which lack competition / financial-health / key-uncertainties / peer as distinct sections) from complete reports; **(spine guard)** ≥20 table rows per language — set **below the current lightest complete report (nvidia @ 21 rows)** so no existing `full` report is retroactively failed, while still rejecting a module-complete-but-table-hollow report; **(stub floor)** the existing per-section floor (no core section with 0 tables AND <2 numbers AND <120 non-ws chars). Aggregate failures across both languages before `fail()` (the fail-fast fix already applied to the ratio gate — don't let a ZH failure mask EN). Note: the ~40-row figure in §2.2 is the *authoring target* for new/upgraded full reports, **not** this gate floor.
- **`coverageTier == "lite"`**: require ≥1 table with ≥6 rows per language; warn (do not fail) if <7 `##`.
- **`coverageTier == "seed"`**: **warn** (do not fail) if 0 tables — the warning is the nudge to graduate to `lite`; never hard-fail a declared seed.
- Thresholds are flags (`--full-spine-rows 20`, `--lite-min-rows 6`) with the same `depthBaselineWaived` escape hatch honored. `full-cycle` behavior (the ratio-vs-baseline gate) is unchanged.
- **Deploy:** edit the source at `~/Documents/codex-private-skills/skills/company-research-publishing/scripts/check_research_package.py`, then single-file copy to `~/.codex/skills/company-research-publishing/scripts/check_research_package.py` (the checker is self-contained/stdlib-only; do not run `install-local.sh`). Commit the skill-source change (prior skill edits have been left uncommitted — commit this one).

### 4.4 Skill checklist sync (`~/Documents/codex-private-skills`)

- `SKILL.md` / `publishing-contract.md`: new chain reports declare `coverageTier`; new/upgraded reports tagged `full` target the §2.2 contemporary contract and every `full` report must pass the §4.3 gate floor; the ZH heading-keyword requirement (牛市/熊市/催化/监测/附录) is restated so the module detector matches.
- Note the metadata stale-pattern "no allowlist" rule and the `hugo_stats.json` re-dirty gotcha in the checklist if not already present.

### 4.5 Frontend — neutral tier chip

- **`index.html` cards** (current-chain only): one neutral chip per card next to the existing v3 price/rerun chips — `完整 / Full`, `精简 / Lite`, `初览 / Seed`. New `PAGE_LABELS` keys in both languages. DESIGN.md neutral chip treatment; **no color grading** (locked decision 6). Hidden when `coverageTier` absent (graceful degradation, matching the price-chip pattern).
- **`reports/view.html?id=`**: the tier as a small fact in the report header meta row.
- **`coverage-map.html`** (optional, nice-to-have): render the tier as a lane/node annotation so the chain graph shows depth coverage at a glance. Skip without regret if it crowds the node cards.

---

## 5. Delivery slicing & gates

Track 3 (tooling) lands first so it can enforce Track 1 as it proceeds; the backfill is warn-mode so nothing goes red mid-migration.

| PR | Track | Contents | Depends on | Gates |
|---|---|---|---|---|
| PR-1 | 3 | `coverageTier` schema + `validate_reports.py` (value/consistency/table-floor, `ENFORCE_COVERAGE_TIER=False`) + backfill `coverageTier` on all 35 current-chain **at each report's measured tier per the §2.1 inventory** (6 `seed`, 6 `lite`, 22 `full`, copx `lite`+ETF-carve-out) + tier chip on `index.html`/`view.html` | — | `validate_reports.py` · `validate_coverage_map.py` · `validate_prices.py` · `hugo --minify` |
| Skill-PR | 3 | `check_research_package.py` per-tier floor (§4.3) + `SKILL.md`/`publishing-contract.md` checklist (§4.4), committed in `~/Documents/codex-private-skills`, redeployed by single-file copy | with PR-1 | skill repo checks + a manual `--report-id` run on one stub (should now fail if tagged `full`) and one full report (should pass) |
| PR-2…13 | 1 | one PR per committed upgrade, worst-first (§2.1a order); each flips its `coverageTier`→`full`, bumps `lastUpdate`, regenerates `feed.xml` | Skill-PR (gate must exist to prove the upgrade) | `validate_reports.py` · `check_research_package.py --report-id` (tier floor) · valuation-sensitive run with that report's tokens · EN/ZH parity · `hugo --minify` |
| PR-Flip | 3 | flip `ENFORCE_COVERAGE_TIER=True` once every current-chain report carries its measured-tier `coverageTier` and the 12 committed upgrades are `full` | PR-2…13 | full CI |
| PR-F0 | 2 | `coverage-map.json` `planned[]` += CCJ/MP (**not** SMH — §3.1) with bilingual gap labels; new `layers[]`/`crossChecks[]` (+ `EXPECTED_LAYERS`/`EXPECTED_ROLES` update) for any new-layer scout winner (data-only) | — | `validate_coverage_map.py` · `hugo --minify` |
| PR-Fn | 2 | one PR per new report (CCJ, MP, SMH-as-benchmark-ETF, scout winners) via the skill, born at the correct tier | PR-F0, Skill-PR | same as PR-2…13 (ETF: lighter, no valuation-sensitive) |

Skill PRs are one commit in `~/Documents/codex-private-skills`, redeployed; they ride with their site/content PRs.

---

## 6. Acceptance criteria (verify before merge, per PR)

- **PR-1:** all 35 current-chain reports carry a valid `coverageTier` **matching the §2.1 measured inventory** (spot-check: sk-hynix/neov = `full`, the 6 stubs = `seed`, the 6 lite-power = `lite`, copx = `lite`); `validate_reports.py` passes with `ENFORCE_COVERAGE_TIER=False`; a temporary mutation making a `lite`/`full` report's table-count zero **fails** the new backstop; tier chip renders in ZH and EN with no color grading; a report with `coverageTier` removed still renders (graceful).
- **Skill-PR:** `check_research_package.py --report-id asml-2026` (a `seed` at this point) **warns but does not fail**; forcing `asml-2026` to `coverageTier: full` while still thin **fails** the tier floor (missing modules + no table spine); a genuinely-complete report tagged `full` (e.g. `tsmc-2026`, and also the lightest one, `nvidia-2026` @ 21 rows) **passes**; the 7-`##` `nrg-2026` tagged `full` **fails** on module-completeness (proves the gate has teeth); both-language failures are aggregated, not fail-fast-masked.
- **PR-2…13 (each upgrade):** EN/ZH exact `##`/`###`/table-row parity, zero `~~`; clears the `full` **gate floor** (complete module set + ≥20-row spine) via `check_research_package.py --report-id <id>` with no waiver, and meets the **authoring target** (~40+ rows / 12 `##`); no restated old anchor in `summary`/`highlights`; `feed.xml` regenerated (CI feed-sync gate green); the report's stub figures are preserved, no fabricated new quarter.
- **PR-Flip:** CI green with `ENFORCE_COVERAGE_TIER=True`; temporarily dropping `coverageTier` from any current-chain report fails CI; **no report is tagged above its measured tier** (mutating a `lite` report to `full` must fail the skill gate).
- **PR-F0:** `planned[]` renders CCJ/MP on `coverage-map.html` (SMH is not here); any new layer/crossCheck validates and renders bilingually with `EXPECTED_LAYERS`/`EXPECTED_ROLES` updated.
- **PR-Fn:** each new report passes the same gates as an upgrade; ETF reports pass the lite/carve-out path (no single-company table requirement).
- **All:** no color-coded judgment anywhere (locked decision 6); language toggle re-renders every new element; `git checkout -- hugo_stats.json` before any content commit.

---

## 7. Risks & gotchas (carried from prior cycles — read before starting)

- **Depth gate fail-fast masks the second language.** `check_research_package.py` historically `fail()`+`exit`ed on the first failing language (files ordered zh→en), so a ZH pass could hide a worse EN. The ratio gate was fixed to aggregate; the new absolute tier floor must aggregate too.
- **Metadata stale-pattern has no allowlist.** Old anchors in `summary`/`highlights`/`lastUpdate`/`title`/`titleEn` hard-fail the valuation-sensitive check with no on-line `old`/`旧` rescue. Scrub old values from the card metadata; tagged old→now values live only in the body Changes/valuation tables.
- **Module detector is keyword-on-headings, per language.** ZH bull/bear/catalysts/uncertainties/appendix need 牛市/熊市/催化(监测)/不确定性(失效条件)/附录(关键假设); bare 看多/看空/观察窗口 do **not** match. Set headings correctly from the start of each upgrade.
- **`hugo --minify` re-dirties `hugo_stats.json`.** `git checkout -- hugo_stats.json` before every content commit.
- **Skill deploy path.** Edit `~/Documents/codex-private-skills` (source of truth); deploy the checker by single-file copy, not `install-local.sh` (which wipes all skills). Commit the skill-source change.
- **Concurrent edits.** The repo is operated on mid-session; before committing verify `git rev-parse --abbrev-ref HEAD` + `reports.json` idx0, and isolate a fresh feature branch with `git reset --hard origin/main` (untracked report files survive `--hard`).
- **Do not re-init covered names.** ANET, and everything in the 35, are already covered — this cycle deepens, it does not re-initiate. Track 2 adds only genuinely new names.
- **Verify 2026 numbers against live web,** not Jan-2026 training priors — the H1-2026 AI supercycle makes stale priors read as "too high" (the MU/MRVL near-false-flag lesson). Every headline number in an upgrade must be web-verifiable.

## 8. Out of scope (explicitly)

- The v3 accountability loop (price tracking, rerun queue, signal cadence, RSS, market-context strip) — shipped, untouched.
- The 10 non-chain legacy reports' full-cycle depth reruns — separate backlog, ranked by the v3 queue, not required here.
- Any stance-accuracy scoring, portfolio/returns tracking, or color-graded quality verdicts (locked decisions 6; carried from v3).
- New JS libraries, build-time frameworks, server components — static HTML + vanilla JS only.
- Forcing a thin-float or private-only name into Track 2 to fill a layer — the rubric (§3.2) gates that out.
