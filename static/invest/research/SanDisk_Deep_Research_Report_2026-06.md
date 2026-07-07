# SanDisk (SNDK) Deep Research Report

Coverage date: 2026-06-27
Last updated: 2026-07-07
Ticker: NASDAQ: SNDK
Disclaimer: This report is for informational and research purposes only. It does not constitute investment advice. Please conduct your own due diligence. All prices and market caps are point-in-time snapshots; financial figures are per company disclosure unless noted otherwise.

> **Background & fiscal-year note:** SanDisk was originally founded in 1988 (as SunDisk), acquired by Western Digital in 2016, and spun off again as an independent pure-play NAND flash company on February 21, 2025. The spin-off separated WDC's flash storage business (branded SanDisk + WD flash products) from its HDD business (retained under Western Digital). SanDisk's fiscal year ends around late June. In this report **FY2026** is the year ending ~June 27, 2026; **Q3 FY2026** is the quarter ended April 3, 2026 (reported April 30, 2026), the latest quarter as of publication. This report is **initial coverage**. Read alongside this center's NVIDIA, Broadcom, SK hynix and Micron reports — SanDisk is the NAND flash leg of the AI memory value chain.

---

## Executive Summary

**One-line thesis:** SanDisk is the world's largest pure-play NAND flash company — when AI data centers generate and store petabytes of training data, inference outputs, and model checkpoints, the storage layer beneath the compute is dominated by NAND SSDs. Freshly spun off from Western Digital, SanDisk has delivered a quarter for the record books: Q3 FY2026 revenue of **$5.95B** (+97% Q/Q, +251% Y/Y), GAAP gross margin of **78.4%**, operating margin of **69.1%**, and FCF of **$3.0B** — numbers that look more like a software platform than a memory manufacturer. The market has noticed: market cap has surged to ~**$310B**. But NAND is one of the most cyclical sub-sectors in semiconductors, and the question is not whether these margins are real (they are), but how long they last.

**Verdict:** **Cautious / medium conviction.** SanDisk's execution in the NAND up-cycle is extraordinary, and the AI-driven storage demand story has clear, quantifiable tailwinds (Datacenter revenue +233% Q/Q). But the v5 scenario grid puts more weight on cycle math than on linear growth: a **$310B market cap on ~$19B FY2026E revenue (~16x P/S) already prices in sustained peak margins**, while NAND pricing is historically boom-bust.

**Current market read (latest market-data snapshot, ~2026-06-28, reflecting the prior trading session):** SNDK was last quoted around ~**$2,091**, market cap ~**$309.6B** (CompaniesMarketCap); it had set an all-time-high close of ~$2,335 (~$346B) on June 25. Computed on ~**148M shares outstanding**, this ranks SanDisk among the ~50 largest companies globally. (The diluted share count is ~**157M**, the basis for per-share earnings.) The 52-week range is ~**$40.10 - $2,354.39** — an extreme range reflecting the post-spin re-rating from a single-digit reference price to a ~$300B+ AI beneficiary. Financial source: [SanDisk Q3 FY2026 8-K](https://www.sec.gov/Archives/edgar/data/2023554/000162828026028879/sndkq3-26ex991xpressrelease.htm); quote references: [CompaniesMarketCap SNDK](https://companiesmarketcap.com/sandisk/marketcap/), [Yahoo Finance SNDK](https://finance.yahoo.com/quote/SNDK/).

**Key data:**

| Metric | Value |
|--------|-------|
| Price (latest snapshot, ~2026-06-28) | ~$2,091 (CompaniesMarketCap; prior trading session) |
| Market cap | ~$309.6B |
| Diluted shares | ~157M (EPS basis, Q3 FY2026); ~148M shares outstanding (market-cap basis); ~158M guided for Q4 |
| EV/Sales (FY2026E) | ~16x (FY2026E revenue ~$19.0-19.5B; zero debt) |
| FY2026E P/S | ~16x |
| TTM P/E (GAAP) | ~65-70x (9-mo FY2026 net income $4.53B: Q1 $112M + Q2 $803M + Q3 $3,615M) |
| Q3 FY2026 revenue | $5.95B (+97% Q/Q, +251% Y/Y) |
| Q3 FY2026 Datacenter | $1.47B (+233% Q/Q, +645% Y/Y) |
| Q3 FY2026 Edge | $3.66B (+118% Q/Q) |
| Q3 FY2026 Consumer | $820M (-10% Q/Q) |
| Q3 FY2026 GAAP gross margin | 78.4% |
| Q3 FY2026 GAAP operating margin | 69.1% |
| Q3 FY2026 GAAP diluted EPS | $23.03 |
| Q3 FY2026 non-GAAP diluted EPS | $23.41 |
| Q3 FY2026 operating cash flow | $3.04B |
| Q3 FY2026 free cash flow (FCF) | $2.99B |
| Cash (Apr 3, 2026) | $3.74B |
| Total debt | $0 (zero-debt balance sheet) |
| Shareholders' equity | $13.78B |
| YTD (9mo) revenue | $11.28B; YTD non-GAAP EPS $31.32 |
| Q4 FY2026 guidance | revenue $7.75-8.25B, non-GAAP EPS $30-33, GM 79-81% |
| Long-term supply backlog (NBM) | ~$42B min. contracted revenue, 5 deals, up to 5-yr; ~$11B financial guarantees; >1/3 of FY2027 bit shipments |
| Share repurchase authorization | $6.0B (Board-approved, Q3 FY2026) |
| Primary competitors | Samsung, SK hynix (Solidigm), Micron, Kioxia |
| CEO | David Goeckeler |

---

## 1. Business Overview

SanDisk is a **pure-play NAND flash memory company** — it designs, manufactures, and sells flash storage products across the entire value chain, from NAND wafers (sourced through its Flash Ventures JV with Kioxia, extended through 2034) to finished SSDs, memory cards, and embedded storage modules. Post-spin, the company paid off all $1.9B of debt and operates with a **zero-debt balance sheet**.

**Three reporting segments (Q3 FY2026 disclosed):**

- **Datacenter ($1.47B, +233% Q/Q, +645% Y/Y):** enterprise NVMe SSDs for hyperscale clouds and AI training/inference clusters. This is the growth engine — AI data centers require massive, fast storage for training datasets, model checkpoints, and inference caching. Management characterizes this as a "fundamental inflection point" with a "deliberate shift toward highest-value end markets, led by Datacenter."
- **Edge ($3.66B, +118% Q/Q, +295% Y/Y):** client SSDs, embedded storage (eMMC/UFS for smartphones, automotive, IoT), and industrial applications. The largest segment by revenue, benefiting from the same NAND pricing tailwinds.
- **Consumer ($820M, -10% Q/Q, +44% Y/Y):** memory cards, USB drives, retail SSDs. The legacy consumer business — cash-generative but declining as a share of total (14% in Q3).

**The business model:** NAND flash is a **commodity memory business with intense cyclicality.** SanDisk's profitability is overwhelmingly driven by NAND pricing. When supply is tight and demand is strong, gross margins can exceed 75% (as in Q3 FY2026); when oversupply hits, prices can fall below cash cost. SanDisk manufactures NAND through its joint venture with Kioxia (formerly Toshiba Memory), sharing fab capacity and R&D costs. A key benefit of the JV structure is **lower standalone capex** — Q3 FY2026 net capex was just $45M against $3.0B of FCF.

---

## 2. Industry & Competitive Position

### 2.1 The NAND oligopoly: five players, extreme cyclicality

The global NAND flash market is controlled by five major players:

1. **Samsung (~35-38% share):** largest and most vertically integrated.
2. **SK hynix / Solidigm (~20-23%):** acquired Intel's NAND/SSD business; strong in enterprise QLC SSDs.
3. **Kioxia / SanDisk (~20-22% combined):** co-own NAND fabs through their JV (now extended to 2034).
4. **Micron (~12-15%):** only U.S.-based NAND manufacturer with its own fabs.
5. **YMTC (Yangtze Memory):** China-based, largely restricted from global markets by export controls.

**All five share one characteristic: NAND is brutally cyclical.** Fab capacity takes 2-3 years to build and comes online in large chunks. Demand surges (AI, smartphones, PCs) drive prices up; capacity overshoots drive them down. SanDisk's Q3 FY2026 margins (78.4% gross, 69.1% operating) are extraordinary — and historically, margins at these levels attract capacity expansion that eventually breaks the cycle.

### 2.2 The AI storage thesis: real, quantified, and now partly contracted

SanDisk's Q3 FY2026 Datacenter results validate the AI storage thesis in hard numbers: $1.47B in a single quarter, up 233% sequentially, growing 6.5x year-over-year. Hyperscalers are building AI infrastructure at unprecedented scale, and storage is a companion investment alongside compute.

**The $42B long-term backlog — NAND's attempt to de-cyclicalize.** The quarter's most consequential development is structural, not merely cyclical: SanDisk has signed five **New Business Model (NBM)** agreements with hyperscale customers (three in Q3, two in early Q4) carrying a **minimum ~$42B of contracted revenue over terms of up to five years**, backed by **~$11B of third-party financial guarantees** (with ~$400M of prepayments already on the Q3 balance sheet; a missed quarterly purchase commitment triggers the guarantee). Management says these deals will cover **more than one-third of FY2027 bit shipments**, with an ambition to exceed 50%; near-term contract pricing is mostly fixed while longer-dated tranches are more variable (CFO Luis Visoso). This is an explicit attempt to break the historical NAND pattern — in which multi-year fab investment collides with quarterly spot pricing — by converting a slice of output into contracted, guarantee-backed revenue. If it holds, it raises the trough of the next down-cycle. *(Caliber: the existence of the NBM agreements and "firm financial commitments" is in the Q3 FY2026 8-K; the specific $42B / $11B / $400M figures, the immediate-trigger mechanism, the fixed-vs-variable pricing split and the >1/3 FY2027 coverage are management's Q3 FY2026 earnings-call statements — see Sources — pending confirmation in the contract filings.)*

But the cycle is dampened, not abolished. Even at the >50% ambition, roughly half of volume still marks to spot; the $11B of guarantees is a fraction of the $42B backlog; and all five NAND players are adding capacity. The question is whether AI demand growth plus contracted backlog outruns capacity additions, or whether 78% gross margins are simply the peak of this cycle.

### 2.3 Competitive dynamics: SanDisk's position

**Strengths:**
- **JV with Kioxia (extended to 2034):** shared fab costs give SanDisk cost-competitive NAND supply without full capex burden (Q3 capex just $45M).
- **Zero-debt balance sheet:** $3.74B cash, no debt — financial flexibility in a capital-intensive industry.
- **Enterprise SSD momentum:** Datacenter revenue growing 6.5x Y/Y with NBM agreements.
- **Pure-play focus:** sole focus on NAND, unlike Samsung (diversified) or Micron (DRAM-dominated).

**Weaknesses:**
- **No DRAM diversification:** no offsetting revenue stream in a NAND down-cycle.
- **JV dependency:** fab investment decisions require Kioxia alignment.
- **Commodity pricing:** NAND is commoditized; sustainable pricing power is limited.

---

## 3. Financial Health

### 3.1 Q3 FY2026: a quarter that redefines what a NAND company can earn

| Metric | Q3 FY2026 | Q2 FY2026 | Q/Q | Q3 FY2025 | Y/Y |
|--------|-----------|-----------|-----|-----------|-----|
| Revenue | $5,950M | $3,025M | +97% | $1,695M | +251% |
| GAAP Gross Margin | 78.4% | 50.9% | +27.5pp | — | — |
| GAAP Op Income | $4,111M | $1,065M | +286% | — | — |
| GAAP Op Margin | 69.1% | 35.2% | +33.9pp | — | — |
| GAAP Net Income | $3,615M | $803M | +350% | — | — |
| GAAP Diluted EPS | $23.03 | $5.15 | +347% | — | — |
| Non-GAAP Diluted EPS | $23.41 | $6.20 | +278% | — | — |

This is a "peak of the cycle" print. Revenue nearly doubled sequentially as NAND prices surged and Datacenter demand exploded. Gross margin at 78.4% is extraordinary for a memory manufacturer — it reflects the extreme operating leverage of the NAND business model when pricing is strong and fixed costs (fab depreciation) are spread across higher ASPs.

### 3.2 Cash flow and balance sheet: fortress-grade

- **Operating cash flow: $3.04B** in a single quarter.
- **Free cash flow: $2.99B** — Q3 FCF alone exceeds most semiconductor companies' annual FCF.
- **Cash: $3.74B** as of April 3, 2026.
- **Total debt: $0** — the company paid off all $1.9B of legacy debt post-spin. CEO David Goeckeler: "zero-debt balance sheet."
- **Shareholders' equity: $13.78B.**

The balance sheet is a competitive advantage — in a capital-intensive, cyclical industry, zero debt means no refinancing risk and full capacity to invest through the cycle. The Board also authorized a **$6.0B share repurchase program** in Q3 FY2026.

### 3.3 Guidance implies the cycle is still accelerating

| Metric | Q4 FY2026 Guidance |
|--------|-------------------|
| Revenue | $7,750M - $8,250M |
| Gross Margin | 79.0% - 81.0% (non-GAAP) |
| Non-GAAP Diluted EPS | $30.00 - $33.00 |
| Diluted Shares | ~158M |

Q4 guidance at $7.75-8.25B implies another ~30-39% sequential revenue growth and gross margins still expanding to ~80%. This would bring FY2026 full-year revenue to approximately **$19.0-19.5B** — placing SanDisk's forward P/S at ~16x, materially lower than the ~24x TTM multiple initially screened. However, 80% gross margins are peak-of-cycle, not mid-cycle; normalized margins over a full NAND cycle are substantially lower.

---

## 4. Management & Governance

**CEO David Goeckeler** leads SanDisk post-spin. Key governance items:

- **Spin-off execution:** paid off all legacy debt, established zero-debt balance sheet, extended Kioxia JV to 2034 — clean execution.
- **Strategic pivot to Datacenter:** management has explicitly shifted toward "highest-value end markets, led by Datacenter," validated by 233% Q/Q Datacenter growth and NBM agreements.
- **Capital allocation:** authorized a **$6.0B share repurchase program**; balancing growth investment with shareholder returns from a zero-debt position.
- **JV governance with Kioxia:** the manufacturing JV extended through 2034 provides long-term supply visibility but requires partner alignment on capacity expansion decisions.

**Management grade: A- (excellent post-spin execution, strategic pivot to Datacenter, fortress balance sheet; capital allocation through the cycle and JV governance remain to be proven over a full cycle).**

---

## 5. Bull Case

**Core thesis:** AI data centers are generating a structural step-change in storage demand, and SanDisk — as the largest pure-play NAND company with a zero-debt balance sheet — is delivering peak-cycle earnings that may prove more durable than prior NAND cycles.

1. **AI storage demand is quantified, contracted, and accelerating.** Datacenter revenue +233% Q/Q, +645% Y/Y; the five NBM agreements lock in a **~$42B minimum-revenue backlog (up to 5-yr) backed by ~$11B of guarantees**, covering >1/3 of FY2027 shipments — demand visibility no prior NAND cycle had (see §2.2).
2. **Margins are at software-company levels.** 78.4% gross margin, 69.1% operating margin, $3.0B quarterly FCF — if AI demand extends the cycle, these margins can persist longer than skeptics expect.
3. **Zero debt, massive cash generation.** $3.74B cash, no debt, $3.0B quarterly FCF — SanDisk can fund growth, buybacks, and dividends simultaneously.
4. **JV with Kioxia provides structural cost advantage.** Shared fab investment means capex is just 0.8% of revenue in Q3 ($45M on $5.95B).
5. **Forward valuation is more reasonable than it first appears.** FY2026E P/S ~16x on ~$19B revenue; if FY2027 sustains or grows from here, the stock screens cheaper than AI chip peers.

---

## 6. Bear Case

**Core thesis:** NAND is cyclical, and at $310B on peak-cycle earnings, the stock is priced for margins that history says will mean-revert — when they do, the downside from peak-cycle multiples is severe.

1. **78-80% gross margins are unsustainable.** Every prior NAND cycle has seen margins revert sharply as capacity comes online. At peak-cycle margins, even a normalization to 50-55% gross margin (still excellent by historical standards) would cut earnings significantly. The $42B NBM backlog softens but does not remove this: it covers only ~1/3 of FY2027 volume (longer-dated tranches are variable-priced), so the majority of NAND output still marks to spot as ASPs roll over.
2. **No full-year guidance — only one quarter at a time.** Management provided Q4 guidance but no FY2027 outlook. The lack of visibility beyond one quarter in a cyclical industry is a risk.
3. **No DRAM buffer.** When NAND prices fall, SanDisk has no other memory product to offset — unlike Samsung, SK hynix, and Micron.
4. **JV dependency limits autonomy in capacity decisions.** Major fab investments require Kioxia alignment; Kioxia's own strategic priorities (potential IPO, Japanese government interests) may not always align with SanDisk shareholders.
5. **The spin-off honeymoon effect.** Post-spin pure-plays often get an initial re-rating; if operational execution disappoints or the cycle turns, the de-rating can be swift and amplified by the lack of a diversified business base.

---

## 7. Key Uncertainties

1. **Duration of peak margins.** How long can 78-80% gross margins persist? This is the single most important valuation variable. When we'll know more: track NAND contract price indices (DRAMeXchange, TrendForce) and quarterly gross margin disclosures.
2. **Datacenter demand sustainability.** Is +233% Q/Q Datacenter growth a one-time catch-up or a sustained trajectory? NBM agreement conversion rates will be informative.
3. **Kioxia JV capacity expansion cadence.** New fab announcements are a leading indicator of future oversupply. The JV extension to 2034 provides stability but the pace of capacity addition is the key variable.
4. **Capital allocation post-spin.** With zero debt and $3.0B quarterly FCF, how management allocates capital (buybacks, dividends, fab investment, M&A) will define the multi-year shareholder return profile.
5. **China / YMTC.** While currently restricted, YMTC's technology progress and potential policy shifts could reshape the NAND supply landscape.

**Thesis-breaking events:**
- If NAND contract prices decline for **two consecutive quarters**, the up-cycle thesis is challenged.
- If Datacenter revenue growth decelerates sharply (below +50% Q/Q), the AI storage narrative weakens.
- If SanDisk/Kioxia announce a **major new fab expansion**, it signals future oversupply and margin compression.

---

## 8. Valuation Context

> The following is valuation "context," not a price target or a buy/sell recommendation.

- **FY2026E P/S ~16x:** market cap ~$309.6B / FY2026E revenue ~$19.0-19.5B (YTD $11.28B + Q4 guidance $7.75-8.25B). For context: NVIDIA ~19x on ~$253B TTM revenue, Broadcom ~24x on ~$75B TTM revenue. SanDisk at 16x P/S on $19B revenue is priced between these AI chip leaders — despite being in a more cyclical, lower-moat industry. Note that the 16x is on **peak-cycle** revenue; in a NAND down-cycle, revenue can contract 20-40%, and P/S on normalized revenue would be substantially higher.
- **TTM P/E ~65-70x (GAAP):** 9-month FY2026 GAAP net income was **$4.53B** (Q1 $112M + Q2 $803M + Q3 $3,615M), so TTM net income is ~$4.5-4.8B and the trailing P/E on ~$310B market cap is ~65-70x (and ~73x against the late-June high). By comparison, NVIDIA trades at ~25x forward and Broadcom at ~33x — SanDisk's *trailing* multiple is ~2x+ higher, though largely because the cycle just inflected and the back quarters were trough earnings. However, on a **forward** basis (if Q4 annualized: $30-33 EPS × 4 ≈ $120-132), the forward P/E drops to ~15-16x — explaining the bull case. The bear case is that the forward estimate rests on peak-cycle EPS that will not annualize.
- **EV/Sales ~16x:** with zero debt and $3.74B cash, EV is ~$306B — essentially market cap. EV-based multiples mirror equity-based ones.
- **Reading the multiple:** SanDisk's valuation is largely a bet on **NAND cycle duration.** At 16x peak-cycle P/S and ~15-16x annualized forward P/E, the stock looks reasonable — but only if current earnings are sustainable. If margins normalize to mid-cycle levels, both the multiple and earnings contract — the classic commodity-cycle double compression. The new variable is the **$42B NBM backlog**: if contracted, guarantee-backed revenue genuinely raises the cycle trough, the double compression is partially capped; if it merely re-times the same cyclical revenue, the bear math holds. The bull case is that AI plus contracts structurally extend the cycle; the bear case is that history repeats.

**Scenario grid:**

| Scenario | Driver assumptions (NAND pricing / NBM coverage / margin / multiple regime) | Valuation implication (rich / fair / cheap vs today) | Probability weight |
|----------|----------------------------------------------------------------------------|------------------------------------------------------|--------------------|
| Bull | AI storage demand accelerates; NAND supply stays disciplined; NBM filings confirm roughly $42B minimum revenue and coverage moves toward more than half of FY2027 bits; 75%+ gross margin persists; the market treats SanDisk as a structural AI storage asset rather than a commodity-cycle name | The $2,090.71 price looks fair only if the NBM structure lifts the trough and extends peak-like margins through FY2027 | 20% |
| Base | NAND up-cycle extends through FY2027, but gross margin eases from 78-80% toward 60-65%; NBM contracts help but still cover only part of output; P/S compresses toward 10-12x as growth decelerates; buybacks cushion but do not erase cycle risk | The current price largely prices an optimistic version of this scenario: strong execution, but limited cushion if margins normalize | 40% |
| Bear | NAND oversupply emerges, contract prices decline, Kioxia / SanDisk capacity additions point to looser supply, NBM terms prove less protective than management's framing, and gross margin falls toward 40-50%; the market re-rates SanDisk from AI growth story to commodity cyclical | The current price would be rich because earnings and the multiple would contract together | 40% |

**What's priced in & the expectation gap:** At the $2,090.71 price anchor and Q4 annualized EPS of about $120-132, the stock looks like only about 16x peak run-rate earnings. That is the trap in NAND: at 12-15x through-cycle sustainable EPS, today's price implies roughly `$2,090.71 / 15 ≈ $139` to `$2,090.71 / 12 ≈ $174` of sustainable EPS, above even the Q4 annualized guide. Our 20% bull / 40% base / 40% bear grid says the market is underwriting a structurally higher trough before the NBM evidence has proved it. The expectation gap is therefore negative: AI storage demand is real, but peak-cycle mean reversion is not fully priced.

---

## 9. Catalysts & Monitoring Checklist

**Near-term (0-6 months):**
- Q4 FY2026 results (~July 2026): delivery against $7.75-8.25B / $30-33 EPS guidance.
- NAND contract price trends (monthly/quarterly indices).
- Kioxia JV capacity expansion or new fab announcements.
- Hyperscaler capex guidance (MSFT, GOOG, META, AMZN) — storage is derivative of total infrastructure spend.

**Medium-term (6-18 months):**
- FY2027 outlook — will management provide full-year guidance?
- Capital allocation execution (buyback pace, dividend initiation, fab investment).
- The next NAND cycle phase — are prices still rising, stabilizing, or falling?

**Long-term (18+ months):**
- SanDisk's market share trajectory within the NAND oligopoly.
- Whether SanDisk diversifies beyond NAND (CXL memory, storage-class memory).
- Structural impact of AI on long-term NAND demand growth rate.

**Metrics to monitor continuously:** NAND ASP trends, quarterly gross margin, Datacenter revenue growth rate, bit growth vs. ASP changes, Kioxia fab utilization, hyperscaler storage spend, forward NAND supply/demand balance.

---

## 10. Conclusion

SanDisk's chain-validation job is to test whether AI data-center demand is reaching the storage layer with enough force to change NAND cycle economics. If Datacenter revenue, NAND contract pricing, and NBM commitments keep compounding, the AI infrastructure chain is broader than compute and power. If NAND pricing or margins roll over, storage remains the chain's most cyclical leg.

The expectation gap is negative: at $2,090.71, the market is underwriting roughly $139-174 of through-cycle sustainable EPS on a 12-15x memory-cycle frame, which is above even the Q4 annualized EPS guide of about $120-132; our 20% bull / 40% base / 40% bear grid says the NBM structure has not yet proved that peak NAND earnings are sustainable.

The current stance is **cautious, medium conviction**. The bull case is powerful because NBM contracts and AI storage demand may raise the next trough. But the base and bear cases carry 80% combined weight and both include gross-margin normalization from the 78-80% zone. Medium conviction reflects strong current evidence in Q3 results, FCF, zero debt, and NBM commitments, offset by the still-unproven durability of NAND pricing and contract protection.

Upgrade trigger: move to neutral-watch or constructive if FY2026 Q4 delivers the $7.75-8.25B revenue and 79-81% gross-margin guide, NBM filings confirm roughly $42B of minimum revenue with coverage moving toward more than half of FY2027 bits, and NAND contract prices plus industry capex still show supply discipline. Downgrade trigger: move to bearish-avoid if NAND contract prices weaken for consecutive periods, gross margin falls materially from the 78-80% peak, NBM coverage or guarantees fall short of management's framing, or SanDisk/Kioxia capacity additions point to 2027 oversupply.

---

## Appendix: Sources & Assumptions

**Primary sources:**
- [SanDisk Q3 FY2026 8-K / Press Release (SEC)](https://www.sec.gov/Archives/edgar/data/2023554/000162828026028879/sndkq3-26ex991xpressrelease.htm) — quarter ended April 3, 2026, reported April 30, 2026
- [SanDisk Q3 FY2026 earnings release (IR site)](https://investor.sandisk.com/news-releases/news-release-details/sandisk-reports-fiscal-third-quarter-2026-financial-results)
- [SanDisk Q3 FY2026 earnings call transcript (Motley Fool)](https://www.fool.com/earnings/call-transcripts/2026/04/30/sandisk-sndk-q3-2026-earnings-transcript/) — source for the NBM specifics: CFO Luis Visoso (~$42B minimum contractual revenue from the three Q3 contracts; >$11B financial guarantees; $400M prepayments; over one-third of FY2027 bits; fixed near-term / variable longer-dated pricing) and CEO David Goeckeler (>50% ambition; missed commitment → immediate financial commitments). The 8-K confirms the five NBM agreements and "firm financial commitments" but not these line items.
- $6.0B share-repurchase authorization: per the Q3 FY2026 8-K.
- Market cap reference: [CompaniesMarketCap SNDK](https://companiesmarketcap.com/sandisk/marketcap/), [Yahoo Finance SNDK](https://finance.yahoo.com/quote/SNDK/)
- Company/product information: [SanDisk official website](https://www.sandisk.com/)
- Spin-off background: SEC filings, public reporting on Western Digital's 2023 spin-off announcement and February 2025 completion

**Key assumptions & basis:**
- Market cap ~$309.6B per CompaniesMarketCap (late June 2026) ≈ ~148M shares outstanding × ~$2,091; it reached ~$346B at the June 25 all-time-high close (~$2,335). Diluted share count ~157M is the per-share-earnings basis ($3,615M ÷ $23.03); ~158M guided for Q4.
- FY2026E revenue ~$19.0-19.5B = YTD 9-month $11,283M + Q4 guidance midpoint ~$8,000M. FY2026E P/S ~16x.
- 9-month FY2026 GAAP net income $4.53B (Q1 $112M + Q2 $803M + Q3 $3,615M); TTM net income ~$4.5-4.8B including Q4 FY2025. Trailing GAAP P/E ~65-70x; the back quarters were trough earnings, so the trailing multiple overstates run-rate profitability.
- Forward P/E (annualized Q4) = $30-33 EPS × 4 ≈ $120-132; at $309.6B / 157M shares = ~$1,972 price, forward P/E ≈ 15-16x. This is an illustrative annualization, not a forecast.
- Q3 FY2026 segment data, margins, cash flow, and balance sheet figures are directly from the April 30, 2026 8-K Exhibit 99.1. The $6.0B buyback is Board-authorized per the 8-K; the ~$42B NBM backlog, ~$11B guarantees, and >1/3 FY2027 coverage are management's Q3 FY2026 earnings-call disclosures (not financial-statement line items) and should be reconciled as contracts are filed.
- This report is **initial coverage**; it includes no prior-cycle standalone comparison. Refresh price, guidance, and valuation anchors once Q4 FY2026 results and FY2027 guidance are disclosed.
