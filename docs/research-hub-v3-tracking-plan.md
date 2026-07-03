# Research Hub v3 — Tracking & Accountability Spec

**Status:** Ready to implement · **Owner:** (unassigned — handoff to implementing agent) · **Author:** planning session, 2026-07-03 · **Revised:** 2026-07-03 after plan review (P1: feed ordering by `lastUpdate`, price-staleness visibility, missing-price handling in the queue; P2: signal anchors + PR-3 dependency, `planned[]` split out of PR-1)
**Depends on:** Phase 0 (`34997b0`, spec: `docs/research-hub-enhancement-plan.md`) and Dashboard v2 (`d091cbf`, spec: `docs/research-hub-dashboard-v2-plan.md`), both shipped to `main`.
**Scope of this doc:** five site workstreams in priority order **A price tracking → B rerun queue → C signal cadence → D RSS feed → E market-context strip**, plus **F coverage queue** (content track, runs in parallel via the `company-research-publishing` skill, not by the site-implementing agent).

This spec is **self-contained** — an implementing agent should not need the originating chat. The problem it attacks: the hub now *presents* research well (Phase 0 structured fields, v2 temporal/relational visuals, cross-check radar) but does not *hold itself accountable*. Nothing tracks what happened to a covered name after publication, nothing ranks which report most urgently needs a rerun, the radar has no operating cadence, and readers have no way to subscribe to updates. v3 closes the loop: publish → track → re-check → record.

---

## 0. Context & grounded facts (verified 2026-07-03)

| Fact | Value | Consequence |
|---|---|---|
| `reports.json` | 37 entries, 37 unique ids (`versionType`: 10 initial / 9 full-cycle / 18 incremental); **18 current-chain entries** carry `stance` + `priceAsOf` + `reportedPeriod` + `monitoring[]` (gate `ENFORCE_CHAIN_ENRICHMENT = True` in `validate_reports.py`) | A/B operate on the 18 current-chain entries only |
| `ticker` field | display string, e.g. `"NASDAQ: NBIS"`, dual-listed `"NASDAQ: ALM / TSX: AII"`, KRX `"KRX: 000660"`, A-share `"688676.SH"` | not machine-fetchable → A introduces `priceSymbol` |
| `monitoring[]` | 68 items across the 18 chain reports; 27 carry `nextCheckDate`, 41 event-driven | C's `monitoringRefs` address space |
| `signals.json` | 1 entry (`meta-cloud-compute-resale`, 2026-07-01); validated by `validate_signals()` in `validate_coverage_map.py`: unique `id`, `date` = `YYYY-MM-DD`, bilingual `title`/`detail`, `crossChecks[]` ≥ 1 referencing known crossCheck ids, `tickers[]` strings | C extends this schema and validator |
| `coverage-map.json` | keys `page`/`layers`/`roles`/`planned`/`crossChecks`; `planned[]` = TSM (foundry), MU (memory-storage), CEG/VST (power) | F extends `planned[]`; chain graph on `coverage-map.html` already renders planned nodes |
| Pages | `index.html` (A-Z index, search, coverage cards), `coverage-map.html` (chain graph), `monitoring-dashboard.html` (verdict board, freshness strip, next-check timeline, kill-criteria board, cross-check radar), `reports/view.html?id=` | A/B/C add sections to these existing pages, no new pages |
| Data pipelines | GitHub Actions: `update-currency-data.yml` (daily 00:00 UTC), `update-metals-data.yml` (daily 01:00 UTC; **uses `yfinance`**); pattern = fetch script → validate script → commit if changed | A clones this pattern at 02:00 UTC |
| CI | `ci-smoke.yml` on push/PR: `validate_reports.py`, `validate_coverage_map.py`, currency + metals validators, `hugo --minify` | every PR adds/keeps these gates green |
| Rendering stack | pure static HTML + vanilla JS, client-side `fetch` of the JSON data files, `localize()` + `PAGE_LABELS` for ZH/EN, theme CSS variables, hand-built inline SVG, **no libraries** | all v3 UI follows the same conventions |
| Site base URL | `https://atypicallife.club/` (`hugo.toml`) | D uses it for absolute feed links |
| Publishing skill | `company-research-publishing`; **source of truth is the git repo `~/Documents/codex-private-skills`** (the deployed `~/.codex/skills` copy is wiped by `install-local.sh`) | C.5/D.3 skill-checklist edits go to the source repo |

---

## 1. Locked decisions (do not re-litigate)

1. **Factual board carries over** (inherited from Phase 0 / v2). Price changes, staleness, and signal reads are rendered as **neutral facts** — no green/red, no status colors, no "right/wrong" verdicts on stances. A stance chip is never color-mapped; a price change is text (`+12.3%` / `−8.1%`) in the same neutral chip treatment as everything else.
2. **No stance scoring.** The ledger juxtaposes stance and subsequent price change and lets the reader judge. Stances like `neutral-watch` are not directional bets; the site must never compute or display an accuracy metric.
3. **`prices.json` is generated data**, committed daily by the Action (same as currency/metals `historical.json`). Every page that consumes it must degrade gracefully — if the file is missing, malformed, or a `reportId` is absent, the price chips/sections simply don't render. An Action outage must never break a page.
4. **`priceSymbol` stays optional in the validator.** It is backfilled for all 18 current-chain entries in PR-1, and the publishing-skill checklist requires it for new chain reports, but there is no gate flip in `validate_reports.py` without a separate decision.
5. **Workstream order A → B → C → D → E.** B consumes A's data. E is a go/no-go decided after A–C are live. F (content) runs in parallel and never blocks on the site track.
6. **No new dependencies.** `yfinance` in the Python pipeline only (already used by metals); zero new JS libraries; feed generation is stdlib-only Python.
7. **Signals are append-only.** Existing entries are never edited except to backfill the new optional fields (C.2); corrections are new entries.

---

## 2. Workstream A — price tracking & stance ledger (PR-1)

The single highest-leverage change: it turns "we wrote a deep report" into "and here is what the market did since, next to what we said." It also produces the data B needs.

### 2.1 Schema — `priceSymbol` (the only `reports.json` change in v3)

```jsonc
{
  "id": "nebius-2026",
  "ticker": "NASDAQ: NBIS",       // unchanged, display string
  "priceSymbol": "NBIS",          // NEW, OPTIONAL: Yahoo-Finance-compatible symbol
  // ...all other fields unchanged...
}
```

- Backfill all 18 current-chain entries (identifiable as the entries carrying `stance`). Symbol mapping:

| ticker (display) | priceSymbol |
|---|---|
| NASDAQ: NVDA / AMD / AVGO / SNDK / CRWV / NBIS / AAOI / NEOV | `NVDA` `AMD` `AVGO` `SNDK` `CRWV` `NBIS` `AAOI` `NEOV` |
| NYSE: ANET / VRT / GLW / GEV / BE / OKLO | `ANET` `VRT` `GLW` `GEV` `BE` `OKLO` |
| NYSEARCA: COPX | `COPX` |
| KRX: 000660 (SK hynix) | `000660.KS` |
| 688676.SH (金盘科技) | `688676.SS` |
| NASDAQ: ALM / TSX: AII (Almonty) | `ALM` (primary US listing) |

- Dual-listing rule: always the primary/most-liquid listing, one symbol per report.
- `validate_reports.py`: if `priceSymbol` is present it must be a non-empty string matching `^[A-Z0-9.\-=]+$`; uniqueness across **current-chain** entries only (superseded versions of the same company may repeat it). Optional field — absence is never an error (locked decision 4).

### 2.2 Pipeline — `static/invest/research/update_prices.py`

Stateless recompute on every run (mirrors `metals/update_data.py` conventions: `SCRIPT_DIR`-relative paths, `ensure_ascii=False, indent=2, allow_nan=False`, skip write when content unchanged).

For each current-chain report with `priceSymbol`:
1. Fetch daily closes from `priceAsOf − 10d` through today via `yfinance`.
2. `basePrice` = close of the latest trading day ≤ `priceAsOf` (handles weekends/holidays).
3. `lastClose`/`lastDate` = most recent available close.
4. `changePct` = `(lastClose − basePrice) / basePrice × 100`, rounded to 1 decimal. Base and last are in the same listing currency, so no FX handling is needed.

Output `static/invest/research/data/prices.json`:

```jsonc
{
  "generatedAt": "2026-07-03",
  "entries": [
    {
      "reportId": "nebius-2026",
      "symbol": "NBIS",
      "status": "ok",            // "ok" | "carried-forward" | "missing"
      "attemptedAt": "2026-07-03", // date of the last fetch attempt (updated every run)
      "baseDate": "2026-07-01",
      "basePrice": 240.11,
      "lastDate": "2026-07-02",
      "lastClose": 231.40,
      "changePct": -3.6,
      "currency": "USD"          // from yfinance metadata; display-only
    }
  ]
}
```

Failure tolerance — **staleness must be visible, never silent**:
- fetch succeeded → `status: "ok"`, all fields refreshed;
- fetch failed but a previous entry exists → `status: "carried-forward"`: previous price fields kept unchanged, `attemptedAt` updated. The stale `lastDate` is the fact the UI surfaces (§2.5);
- fetch failed and no previous entry → `status: "missing"`: price fields omitted, only `reportId`/`symbol`/`status`/`attemptedAt` present;
- exit non-zero when **more than half** of the symbols fail in one run (so one flaky KRX/A-share day doesn't kill the run), **or** when any entry's `lastDate` lags `attemptedAt` by more than 10 calendar days (persistent per-symbol failure must fail the Action loudly instead of accumulating carried-forward staleness). Log every non-ok symbol to stdout.

### 2.3 Validator — `static/invest/research/validate_prices.py`

Structural checks only (no freshness gate — a PR must not fail CI because the daily Action hasn't run; freshness enforcement lives in the Action, §2.2):
- top-level `generatedAt` = `YYYY-MM-DD`; `entries[]` list;
- every `reportId` exists in `reports.json` and that report carries `priceSymbol` = `symbol`;
- `status` present and one of `ok` / `carried-forward` / `missing`; `attemptedAt` = `YYYY-MM-DD`;
- for `status` ≠ `missing`: `basePrice`/`lastClose` positive numbers, `baseDate ≤ lastDate ≤ attemptedAt`, `changePct` consistent with the two prices within ±0.15pp; for `missing`: price fields must be absent;
- no duplicate `reportId`.

Add as a step in `ci-smoke.yml` after the coverage-map validator.

### 2.4 Workflow — `.github/workflows/update-research-prices.yml`

Clone of `update-metals-data.yml`: daily cron `0 2 * * *` (staggered after currency 00:00 and metals 01:00), `workflow_dispatch`, `pip install yfinance`, run `update_prices.py` → `validate_prices.py` → commit `static/invest/research/data/prices.json` with message `Update research price data - $(date +'%Y-%m-%d')`.

### 2.5 Rendering

All client-side, fetching `data/prices.json` alongside the existing fetches. If the whole file is missing or malformed, price chips/sections degrade away without breaking the page (locked decision 3). When the file exists but a current-chain report has a `missing` or absent entry, the stance ledger and rerun queue render that report as `无价格数据 / price unavailable` so missing data is visible rather than treated as zero drift.

1. **`index.html` report cards** (current-chain only): one neutral chip per card — `自报告 −3.6%（基准 2026-07-01）` / `−3.6% since report (base 2026-07-01)`. When the entry's `status` ≠ `ok`, the chip appends `· 数据截至 2026-06-25` / `· data as of 2026-06-25` (`lastDate`) so carried-forward staleness is visible at the point of use. New `PAGE_LABELS` keys in both languages.
2. **`monitoring-dashboard.html` verdict board rows**: append the same fact to each row rendered by `renderVerdictRow()` — change-since-report plus base date, with the same stale-date suffix rule.
3. **Stance ledger** — new compact section on `monitoring-dashboard.html`, placed after the Verdict Board: one row per current-chain report with columns *company/ticker · stance chip (existing neutral chip) · report date · price base date · change since report · price as of (`lastDate`) · last update*. Default sort: |changePct| descending (largest moves first — that is where a stance most needs re-reading); entries without a usable price (`missing` or absent) sort last and render `无价格数据 / price unavailable` instead of a number. Rows link to `reports/view.html?id=`. No color anywhere (locked decisions 1–2); the section caption states plainly that stances are not directional calls and the ledger is a fact table, in both languages.

### 2.6 Skill sync

`company-research-publishing` checklist (edit in `~/Documents/codex-private-skills`, then redeploy): new chain reports must set `priceSymbol`; reruns must keep it consistent with the primary listing.

---

## 3. Workstream B — staleness & rerun queue (PR-2)

Turns "which report should we rerun next" from judgment into a queue. Pure client-side computation over `reports.json` + `prices.json`; **no schema change, no pipeline change**.

- For each current-chain report: `ageDays` = today − `priceAsOf`; `driftPct` = |`changePct`| from A when the price entry exists with `status` ≠ `missing` (carried-forward entries use their stale value and show `lastDate`), otherwise the report is **untracked**.
- **Untracked is a first-class state, never zero.** An untracked report renders a neutral `无价格数据 / price unavailable` chip in place of the drift figure, is ranked by the age term alone, and is **always listed** in the queue section (below the scored candidates if it doesn't meet the age rule) — missing data must be visible as missing, never disguised as "no drift".
- **Rerun-candidate rule (locked constants, defined once in JS):** `ageDays > 60` **or** `driftPct ≥ 25`.
- **Queue score** = `ageDays / 60 + driftPct / 25` (each term = 1.0 exactly at its threshold; transparent and shown in the section caption; untracked reports show `ageDays / 60 + ?`).

Rendering:
1. **Rerun queue** — new section on `monitoring-dashboard.html` after the stance ledger: candidates only, ranked by score descending, each row = company · neutral facts (`价格基准 87 天前 · 期间 ±31%` / `price base 87d ago · ±31% since`) · link to the report. Empty state (no candidates) renders the caption plus `当前无复核候选 / no rerun candidates` — the empty state is itself the good news and must be visible, not hidden.
2. **`index.html` cards**: a neutral `复核候选 / rerun candidate` chip on qualifying cards, next to A's price chip.

Operating rule (documented in the section caption and `static/invest/research/README.md`): the queue **ranks** rerun work — including the outstanding Batch-2 rerun backlog — but a human decides; nothing fires automatically.

---

## 4. Workstream C — signal cadence & backlinks (PR-3)

The radar shipped with one entry and no contract for when entries get written. C gives it a cadence and wires signals into the monitoring items and report pages, turning the kill-criteria board into a living log ("this item last fired on …").

### 4.1 Schema — two optional fields on signal entries

```jsonc
{
  "id": "meta-cloud-compute-resale",
  // ...existing fields unchanged...
  "reportIds": ["coreweave-2026", "nebius-2026"],          // NEW, OPTIONAL: covered reports this signal reads on
  "monitoringRefs": ["coreweave-2026:capacity-resale-check"] // NEW, OPTIONAL: "reportId:monitoringItemId" pairs this signal is a read for
}
```

`validate_signals()` in `validate_coverage_map.py` additionally loads `reports.json` and checks: every `reportIds[]` entry is a known report id; every `monitoringRefs[]` entry splits on the **first** `:` into a known report id and a `monitoring[]` item id existing on that report. Both fields optional, may be empty-absent.

### 4.2 Backfill

Populate both fields on the existing `meta-cloud-compute-resale` entry: `reportIds` = the current-chain ids for CRWV, NBIS, MU (not yet covered — omit), SNDK, AMD, SK hynix as applicable; `monitoringRefs` = whichever of those reports' `monitoring[]` items track capacity-resale / neocloud-financing / memory-cycle reads (the implementing agent maps them by reading `monitoring[]` of those reports; include only genuine matches, an empty list is acceptable).

### 4.3 Rendering

1. **Signal-level anchors**: the radar section today only has cross-check-level anchors; each rendered signal entry gains `id="signal-{signal.id}"`. All links below target these anchors.
2. **Kill-criteria board** (`monitoring-dashboard.html`): for each monitoring item referenced by ≥ 1 signal's `monitoringRefs`, append a neutral chip `最近读数 2026-07-01 / last read 2026-07-01` (latest signal date), linking (scroll) to `#signal-{id}` of that latest signal. Items with no reads render unchanged — absence of the chip is the fact.
3. **`reports/view.html`**: new `相关信号 / Related signals` block below the report header — signals whose `reportIds` include this report (fallback when `reportIds` absent: signal `tickers[]` ∩ report `priceSymbol` — this is why PR-3 depends on PR-1, see §8), newest first, each linking to its `#signal-{id}` anchor. Hidden when empty.
4. **Radar entries**: tickers that correspond to covered reports become links to `reports/view.html?id=`.

### 4.4 Operating cadence (process, not code)

Documented in `static/invest/research/README.md`: **whenever a monitoring item fires — a dated `nextCheckDate` read arrives or an event-driven trigger occurs — a signal entry is appended** with `monitoringRefs` naming the item(s) it reads on, before or with the report update it motivates. Signals are append-only (locked decision 7).

### 4.5 Skill sync

`company-research-publishing` checklist (source repo, see §0): when a report update is motivated by a monitoring read, the same PR appends the corresponding `signals.json` entry with `reportIds` + `monitoringRefs`.

---

## 5. Workstream D — RSS feed (PR-4)

Readers currently have no subscription path into the research section (Hugo's built-in RSS covers only blog posts, not the static research hub).

- **`static/invest/research/generate_feed.py`** (stdlib only): reads `reports.json`, emits `static/invest/research/feed.xml` — RSS 2.0, channel title `Atypical Life Club · 研究报告 / Research Reports`, link `https://atypicallife.club/invest/research/`; one `<item>` per report entry (all 37 — every `versionType` is a publication event), newest 50 sorted by **`lastUpdate` (fallback `date`) descending**; item title = `title` + ` / ` + `titleEn`, link = absolute `https://atypicallife.club` + `file`, `guid` = link + `#` + id + `@` + `lastUpdate` (fallback `date`), `pubDate` = RFC-822 from **`lastUpdate` (fallback `date`)**, description = `summary` (plain text, escaped). Rationale: the feed is a **changelog, not an archive index** — many incremental entries carry a February `date` but a June `lastUpdate` (e.g. `netflix-2026`: `2026-02-10` / `2026-06-26`); sorting by `date` would bury every in-place update. Embedding `lastUpdate` in the `guid` makes an updated report re-surface as a new item in readers. Deterministic output (stable ordering, no timestamps other than item dates) so the sync gate below works.
- **CI sync gate** in `ci-smoke.yml`: run `generate_feed.py` then `git diff --exit-code static/invest/research/feed.xml` — the committed feed must match the committed `reports.json`.
- **`index.html`**: `<link rel="alternate" type="application/rss+xml" ...>` in `<head>` plus a small RSS link in the page header/footer.
- **Skill sync** (source repo): publishing checklist adds "run `generate_feed.py` after editing `reports.json`".

---

## 6. Workstream E — market-context strip (PR-5, go/no-go after A–C ship)

A one-line strip at the top of `index.html` connecting the three invest modules: latest USD/CNY (from `../currency/data/historical.json`), latest gold + copper (from `../metals/data/historical.json`), and the newest signal headline (from `data/signals.json`), each linking to its module/section. Client-side fetch of existing files only — zero new pipeline. Whole strip hides on any fetch failure. Decide go/no-go once A–C are live and the page's information density can be judged; skip without regret if it crowds the header.

---

## 7. Workstream F — coverage queue (content track, parallel)

Not for the site-implementing agent. Each item is a full research report produced with the `company-research-publishing` skill under the Batch-1 depth contract, one branch/PR per report, gated by the validators + `hugo --minify` + review. Order within the table is the recommended order; the first three are the previously locked roadmap.

| # | Ticker | Layer (`coverage-map` id) | Role | Rationale / cross-check pairing |
|---|---|---|---|---|
| 1 | **TSM** | `foundry` | anchor | single manufacturing choke point of the entire chain; already in `planned[]` |
| 2 | **CEG / VST** | `power` | anchor + check pair | power-supply constraint; pairs with GEV/金盘/VRT equipment reads; in `planned[]` |
| 3 | **MU** | `memory-storage` | check | third memory read vs SNDK/SK hynix; hardest-hit name in the 2026-07-01 Meta signal; in `planned[]` |
| 4 | **META** | `demand-risk` | demand anchor | first buy-side anchor — hyperscaler capex is the chain's cash source; principal of the capacity-resale cross-check |
| 5 | **ORCL** | `demand-risk` | check | RPO/backlog structure = architecture check on the CRWV "contracts shield risk" thesis (same method as NBIS-vs-CRWV) |
| 6 | **MRVL** | `custom-merchant-silicon` | check | custom-ASIC #2 = counter-check on the AVGO custom-silicon narrative and indirectly on NVDA share assumptions |
| 7 | **COHR** (alt: 中际旭创 `300308.SZ`) | `optical` | anchor | optical-module gap — current optical leg is only GLW (fiber) + AAOI (small-cap); default COHR, A-share alternative acceptable |
| 8 | **DLR** (alt: EQIX) | `datacenter-facility` | check | DC-REIT lease pricing/vacancy = the most objective third-party read on "glut vs scarcity"; complements VRT equipment view |
| 9 | **CCJ** | `resources` | check | uranium fuel cycle = picks-and-shovels check on the OKLO high-risk-watch position |
| 10 | **MP** | `resources` | anchor | strategic-metals/policy continuation of the Almonty (tungsten) line |
| 11 | **SMH** | (ETF, no layer) | benchmark | sector benchmark anchoring single-name views in relative terms, like IGV for software |

Supporting actions:
- **`coverage-map.json` `planned[]`**: add entries #4–#8 (ticker, layer, bilingual gap label) so the chain graph shows the queue — as its own small **data-only PR (PR-F0)**, not mixed into PR-1's review scope; validator already covers `planned[]`. #9–#11 are added when their turn approaches.
- **Interleaving with the Batch-2 rerun backlog** (9 single-company + 2 ETF reruns outstanding): recommended cadence ≈ one rerun per 1–2 new reports; once Workstream B is live, its queue ranking replaces gut feel for choosing which rerun goes next.
- Every new chain report sets `priceSymbol` (A) and inherits the signal cadence (C) from day one.

---

## 8. Delivery slicing & gates

| PR | Contents | Depends on | Gates |
|---|---|---|---|
| PR-F0 | F: `coverage-map.json` `planned[]` additions #4–#8 (data-only) | — | `validate_coverage_map.py` · `hugo --minify` |
| PR-1 | A: `priceSymbol` backfill + validator tweak, `update_prices.py`, `validate_prices.py`, workflow, `prices.json` (first run committed manually), card chips + verdict-row facts + stance ledger | — | `validate_reports.py` · `validate_coverage_map.py` · `validate_prices.py` · `hugo --minify` |
| PR-2 | B: rerun queue section + card badges + README operating rule | PR-1 | same |
| PR-3 | C: signals schema + validator + backfill, signal anchors, last-read chips, view-page backlinks, README cadence rule | PR-1 (ticker fallback matches on `priceSymbol`) | same |
| PR-4 | D: `generate_feed.py` + `feed.xml` + CI sync gate + head/footer links | — | same + feed sync gate |
| PR-5 | E: context strip | go/no-go after A–C | same |
| Skill PRs | §2.6 + §4.5 + §5 checklist items, one commit in `~/Documents/codex-private-skills`, then redeploy | with their site PRs | skill repo's own checks |

Acceptance criteria (verify before merge, per PR):
- **PR-1:** `prices.json` has all 18 chain entries **with `status: "ok"`** and sane values (fix symbols/retry until true — carried-forward/missing entries are not an acceptable initial state); Action runs green on `workflow_dispatch`; chips/ledger render in ZH and EN; a mocked `carried-forward` entry shows its `lastDate` suffix; temporarily renaming `prices.json` breaks nothing visible.
- **PR-2:** queue ordering matches the published formula on hand-checked examples; a mocked missing-price report renders as `price unavailable`, never as ±0%; empty state renders.
- **PR-3:** validator rejects an unknown `reportId`/`monitoringRef` (test by temporary mutation); each rendered signal has its `#signal-{id}` anchor; last-read chip appears on the backfilled items and scrolls to the right entry; view-page block hidden for reports with no signals.
- **PR-4:** `feed.xml` validates against an RSS validator; items are ordered by `lastUpdate` (verify `netflix-2026` surfaces with its June date, not February); CI sync gate fails when `reports.json` changes without regeneration (test by temporary mutation).
- **All:** no color-coded judgment anywhere (locked decision 1); language toggle re-renders every new element.

## 9. Out of scope (explicitly)

- Stance accuracy scores, win rates, or any right/wrong presentation (locked decision 2).
- Portfolio/position tracking, returns simulation, alerts/notifications to readers.
- Charting libraries, build-time JS frameworks, server-side components.
- Automatic rerun triggering — the queue ranks, humans decide.
- Intraday or non-close price data; FX conversion between listings.
