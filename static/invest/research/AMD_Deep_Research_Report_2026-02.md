# Advanced Micro Devices (AMD) Deep Research Report

Coverage date: 2026-02-04
Last updated: 2026-06-22
Ticker: NASDAQ: AMD
Disclaimer: This report is for informational and research purposes only. It does not constitute investment advice. Please conduct your own due diligence.

---

## June 22, 2026 Full Rerun Summary

**One-line thesis:** AMD's fundamental evidence is stronger than it was in the February report, and the data center / AI infrastructure story has moved from optionality toward delivery validation. But at roughly **$537.37** per share and about **$887B** of market capitalization, the stock has already priced in very aggressive 2026-2027 execution.

**Current view:** Downgrade the old "cautiously bullish" framing to **Neutral / watchlist: stronger fundamentals, very low valuation margin for error**. The key question is no longer whether AMD has improved; it is whether the current price already discounts Meta/Helios, MI450, EPYC, ROCm progress, and margin expansion all at once.

**Current market reference (latest verifiable U.S. close as of June 18, 2026):** AMD closed at approximately **$537.37**. Using an approximate 1.65B diluted share base, market cap is roughly **$887B**. Netting Q1 2026 cash and short-term investments of $12.347B against total debt of $3.224B implies enterprise value of roughly **$878B**. Market data source: [MarketWatch AMD quote](https://www.marketwatch.com/investing/stock/amd); financial data source: [AMD Q1 2026 Financial Results](https://ir.amd.com/news-events/press-releases/detail/1284/amd-reports-first-quarter-2026-financial-results).

**Updated valuation read-through:** AMD reported Q1 2026 free cash flow of $2.566B. Annualized mechanically, that is about $10.264B, or an FCF yield of roughly **1.2%** on the current market cap. Using FY2025 revenue of $34.6B, Q1 2026 revenue of $10.253B, and implied Q1 2025 revenue of about $7.438B, TTM revenue is roughly **$37.4B**. That implies EV/TTM Sales of about **23.4x**. If FY2026 revenue lands around $45.7-50.0B, EV/Forward Sales would still be roughly **17.6-19.2x**. On Q1 non-GAAP EPS of $1.37 annualized, the stock trades at about **98x**; even at $6.00 of FY2026 non-GAAP EPS, it would still be about **90x**.

**Previous version:** [View the 2026 pre-rerun version](/invest/research/reports/view.html?id=amd-2026-pre-rerun). This report should be read as the complete latest report produced by integrating the previous version plus this cycle's diff, not as a partial rerun-stage update note.

### Quick Stats

| Metric | Current | February baseline (old) |
|--------|---------|--------------------------|
| Share price | $537.37 (June 18, 2026 close) | old $207.32 (Feb 16) |
| Market cap | ~$887B | old ~$338B |
| Enterprise value | ~$878B | — |
| P/E | ~98x (Q1 annualized non-GAAP) | old 36-40x (forward) |
| EV/Sales | ~23.4x TTM / 17.6-19.2x 2026E | old 5.2x (forward) |
| FCF yield | ~1.2% | old ~2.3% |
| Debt/Equity | 0.06 | 0.06 |
| Net cash | ~$9.1B | old ~$3.9B |
| FY2025 revenue / growth | $34.6B / +34% | $34.6B / +34% |
| FY2025 free cash flow | $5.6B | $5.6B |


## Historical Update Summary

This section now summarizes the full rerun deltas as a clean baseline, while the full previous version remains available in the Previous view.

- Investment stance shifted from “cautiously bullish” to “neutral / watch”: valuation now constrains upside more than fundamentals alone.
- Valuation references were refreshed from the February framework to the current one: around **$887B** market cap and EV/TTM Sales around **23.4x**.
- Customer counterparty verification is now tied to AMD’s disclosed 6GW multi-year, multi-generation agreement with **Meta**; OpenAI remains to be reverified at a deployment-meaningful scale.
- Report structure remains intact for business, competition, financial health, management, bull/bear, key uncertainties, valuation, catalysts, and conclusion, with the analytical backbone now anchored to **Q1 2026 + Q2 guidance + H2 Meta/Helios delivery validation**.

---

## 1. Current Fact Base

### 1.1 Q1 2026 Financial Results

AMD reported Q1 2026 results on May 5, 2026:

| Metric | Q1 2026 | Y/Y | Note |
|--------|---------|-----|------|
| Revenue | $10.253B | +38% | Roughly flat Q/Q |
| GAAP gross margin | 53% | +3 ppt | Down 1 ppt Q/Q |
| Non-GAAP gross margin | 55% | +1 ppt | Down 2 ppt Q/Q |
| GAAP EPS | $0.84 | +91% | Strong earnings leverage |
| Non-GAAP EPS | $1.37 | +43% | About $5.48 annualized |
| Non-GAAP operating margin | 25% | +1 ppt | Down 3 ppt Q/Q |
| Free cash flow | $2.566B | quarterly record | About $10.264B annualized |

Q2 2026 guidance calls for revenue of approximately **$11.2B, plus or minus $300M**, implying about 46% year-over-year growth at the midpoint, with non-GAAP gross margin around 56%. Growth remains strong, but the share price now requires several more quarters of clean execution.

### 1.2 Segment Mix Has Shifted Toward Data Center

Q1 2026 segment performance:

| Segment | Q1 2026 Revenue | Y/Y | Current reading |
|---------|-----------------|-----|-----------------|
| Data Center | $5.8B | +57% | EPYC demand and Instinct ramp are the main growth driver |
| Client | $2.9B | +26% | Ryzen demand and PC share gains |
| Gaming | $720M | +11% | Radeon demand partly offset by lower semi-custom revenue |
| Embedded | $873M | +6% | Recovering, but not the valuation driver |

The February report was built around Q4 2025 and FY2025. This full rerun resets the analytical base to **Q1 2026 + Q2 guidance + H2 2026 Meta/Helios delivery validation**.

### 1.3 Baseline Business Profile and Model

AMD is a fabless high-performance computing chip company. Its core assets are not manufacturing capacity, but CPU/GPU/SoC architecture design, chiplet integration, software and hardware roadmaps, and the ability to productize custom platforms for large customers. Manufacturing depends mainly on foundry partners such as TSMC, so AMD has lower capital intensity than an IDM model, while advanced-node, advanced-packaging, and geopolitical supply-chain concentration remain long-term risks.

The four operating segments carry different economics:

| Segment | Role | Economic traits | Current importance |
|---------|------|-----------------|--------------------|
| Data Center | EPYC server CPUs + Instinct AI GPUs | High ASPs, concentrated customers, long validation cycles, highest margin upside | Core valuation driver |
| Client | Ryzen desktop and mobile CPUs | More cyclical; affected by PC shipments and channel inventory | Scale and cash-flow stabilizer |
| Gaming | Radeon GPUs + semi-custom console chips | Discrete GPU competition is intense; semi-custom follows console cycles | Non-core, but broadens ecosystem reach |
| Embedded | Xilinx FPGA / adaptive SoC assets | Long product lives, sticky customers, steadier demand profile | Portfolio resilience |

Commercially, AMD sells chips and platform products to OEMs, cloud providers, system integrators, enterprise customers, and distribution channels. The AI data center business looks more like project-based platform selling: customers assess GPU performance, CPU attach, networking and rack architecture, software stack, supply assurance, and total cost of ownership together. Client and gaming remain more standard product-cycle businesses, with stronger exposure to macro demand and channel inventory.

AMD's moat can be separated into three layers:

1. **CPU moat:** the x86 duopoly, EPYC performance-per-watt gains, and cloud qualification cycles give server CPU share gains persistence.
2. **AI GPU moat:** still much weaker than NVIDIA's; the ROCm / CUDA ecosystem gap remains the biggest constraint. AMD's opening comes from multi-vendor sourcing, price/performance windows, and customized platform partnerships.
3. **System-level moat:** Helios, MI450/MI455X, 6th Gen EPYC Venice, advanced packaging, and regional supply-chain investments show AMD trying to move from "chip substitute" to "second AI infrastructure platform."

AMD analysis therefore cannot be reduced to the AI GPU line alone. The AI narrative drives valuation elasticity, but EPYC, Client, Embedded, and the Xilinx assets determine whether AMD has enough cash flow and customer depth to move through an AI investment cycle.

### 1.4 FY2025 Baseline Recap and Prior-Quarter Segments

As a pre-rerun fact-base comparison, AMD's FY2025: revenue $34.6B (+34% YoY, a record); non-GAAP gross margin 54-57%; non-GAAP operating income $7.8B; non-GAAP net income $6.8B (+42%); non-GAAP EPS $5.53 (+40%); free cash flow $5.6B (nearly double 2024's $2.4B).

Prior-quarter (Q4 2025) segment mix by revenue and share:

| Segment | Q4 2025 revenue | Y/Y | Share |
|---------|-----------------|-----|-------|
| Data Center | $5.4B | +39% | ~52% |
| Client | $3.1B | +34% | ~30% |
| Gaming | $843M | +50% | ~8% |
| Embedded | $950M | +3% | ~9% |

Q4 2025 non-GAAP operating margin was about 28%; Q4 2025 total revenue was about $10.3B (+34%), giving a direct sequential reference for Q1 2026's $10.253B and Data Center $5.8B. These are February-baseline figures; the body's judgment is anchored to Q1 2026 plus Q2 guidance.

---

## 2. Business and Competitive Position

### 2.1 AMD Is Moving From Chip Supplier to AI Infrastructure Platform Vendor

The key change is not simply that AMD is selling more GPUs. The strategic narrative is moving from single-chip substitution toward rack-scale AI infrastructure:

- EPYC CPUs continue to gain server share and provide the platform attach point.
- Instinct GPUs are ramping through MI300/MI350, with MI450/MI455X and Helios carrying H2 2026 validation.
- ROCm still trails CUDA materially, but multi-supplier strategies give AMD a real entry window.
- Helios rack-scale architecture ties CPU, GPU, networking, software, and systems partners into a more complete AI infrastructure offering.

### 2.2 Meta 6GW Is the Verified Anchor, Not OpenAI

On February 24, 2026, AMD and Meta announced a multi-year, multi-generation partnership to deploy up to **6GW** of AMD Instinct GPUs. The first **1GW** deployment is expected to begin shipping in H2 2026 and is based on custom MI450-architecture GPUs, 6th Gen EPYC "Venice" CPUs, ROCm, and Helios rack-scale architecture. The agreement also includes performance-based warrants for Meta to acquire up to **160M** AMD common shares tied to deployment milestones. Source: [AMD and Meta 6GW Partnership](https://ir.amd.com/news-events/press-releases/detail/1279/amd-and-meta-announce-expanded-strategic-partnership-to-deploy-6-gigawatts-of-amd-gpus).

This is a major strategic validation, but it also concentrates the 2026 thesis:

- If Meta deployment starts cleanly, AMD's AI platform credibility improves sharply.
- If timing slips, scale is reduced, or margins disappoint, the current valuation becomes fragile.

### 2.3 Supply Chain and Ecosystem Are Entering the Proof Phase

On May 21, 2026, AMD announced more than **$10B** of planned Taiwan ecosystem investment over five years to expand advanced packaging and AI infrastructure supply capacity. AMD also disclosed that 6th Gen EPYC "Venice" CPUs had entered TSMC 2nm production ramp, with future production planned at TSMC Arizona. Sources: [Taiwan Ecosystem Investment](https://ir.amd.com/news-events/press-releases/detail/1286/amd-announces-more-than-10-billion-in-taiwan-ecosystem-investments-to-accelerate-ai-infrastructure), [Venice Production Ramp](https://ir.amd.com/news-events/press-releases/detail/1287/amd-announces-production-ramp-of-next-generation-amd-epyc-processor-venice-on-tsmc-2nm-process-technology).

On June 8, 2026, AMD announced up to **GBP 2B** of investment in the United Kingdom over five years to support AI innovation, research computing, and talent development. Source: [UK AI Investment](https://ir.amd.com/news-events/press-releases/detail/1288/amd-commits-up-to-2-billion-to-accelerate-ai-innovation-and-research-in-the-united-kingdom).

These are not near-term earnings catalysts by themselves. They are evidence that AMD is trying to build the regional supply chain and sovereign AI channels needed for Helios-scale adoption.

### 2.4 Market Size, Share, and Ecosystem Gap

**Addressable market (February baseline):**

- AI accelerators (data center GPU): about $27-37B in 2026, $125-325B by 2034, CAGR ~22-36%.
- Server CPU: about $13.9B in 2026, mid-single-digit growth, x86 dominance challenged by Arm.
- Broader AI infrastructure: 2026 hyperscaler AI capex ~$450B; NVIDIA's estimated 2030 data center capex TAM ~$3-4T.

**Market share (February baseline):**

- AI accelerators: NVIDIA ~86-90%, AMD ~5-8% (growing fast off a low base), Intel ~2-3%.
- Server CPU: AMD gaining share since 2018, estimated ~20-25% (Intel ~75-80%); Arm (AWS Graviton, etc.) is the medium-term threat.

**Ecosystem gap:** CUDA has ~4M developers and 18+ years of optimization; ROCm targets 100K developers in 2026 (~1/40 the size), with a real-world performance gap of ~10-30%; AMD typically prices ~15-40% below NVIDIA to win deals. This is the quantitative reason the AI GPU moat is still fragile while the CPU moat is comparatively stable.

---

## 3. Financial Health

### 3.1 Current Quality Scorecard

| Dimension | Observation | Grade |
|-----------|-------------|-------|
| Growth | Q1 2026 revenue +38%, Data Center +57%, Q2 guide midpoint +46% | A |
| Gross margin | Non-GAAP 55%, Q2 guide 56%, still below NVIDIA | B+ |
| Operating leverage | Non-GAAP operating margin 25%, better Y/Y but down Q/Q | B+ |
| Cash generation | Q1 FCF of $2.566B was a quarterly record | A- |
| Balance sheet | $12.347B cash and short-term investments, $3.224B debt, about $9.1B net cash | A |
| Dilution | Meta warrants for up to 160M shares plus ongoing stock-based compensation | Caution |

AMD's financial health is much stronger than in older AMD cycles. The issue is not solvency or liquidity; it is whether the current valuation demands too much future growth and margin expansion.

### 3.2 Red Flag Review

- [x] GAAP / non-GAAP spread: cash flow must continue validating adjusted earnings.
- [x] Dilution: Meta warrants for up to 160M shares are a key variable.
- [x] Customer and project concentration: Meta/Helios has very high thesis weight.
- [x] Manufacturing concentration: leading-edge production and packaging remain highly tied to TSMC and Taiwan.
- [ ] Near-term solvency risk: not evident.
- [ ] Major audit or disclosure problem: not evident from current sources.

### 3.3 Financial Health Matrix (February baseline)

| Metric | Current (2025) | 3Y ago (2022) | Trend | vs peers | Grade |
|--------|----------------|---------------|-------|----------|-------|
| Revenue growth | 34% | 44% | Still strong | Above most legacy peers | A |
| Gross margin (Non-GAAP) | 54-57% | ~50% | Improving | Below NVDA (~75%), above INTC (~40%) | B+ |
| Operating margin | GAAP 7.7% / Non-GAAP Q4 28% | ~5% | Improving | Below NVDA (~62%) | B |
| FCF conversion | $5.6B / $34.6B = 16% | 13% | Improving | Below NVDA (50%+) | B- |
| Debt/EBITDA | 0.3x | 0.5x | Deleveraging | Excellent | A |
| Cash-to-debt | 1.9x | 3.2x | Solid | Strong | A |
| Interest coverage | >20x | >15x | Strong | Excellent | A |

Overall financial-health grade **B+**: strong growth and cash flow with very low leverage; the real constraint is valuation, not solvency.

### 3.4 Key Financial Trends (February baseline)

- **Revenue trajectory:** 2021 $16.4B (+68%), 2022 $23.6B (+44%), 2023 $22.7B (-4%), 2024 $25.8B (+14%), 2025 $34.6B (+34%), 2026E $45.7B (+32% consensus).
- **Free cash flow:** 2024 $2.4B → 2025 $5.6B, 2026E about $7.2-7.4B.
- **Stock comp and dilution:** FY2025 SBC ~$1.6B (~4.6% of revenue); diluted share count ~1.65B (Q1 2026) after ~$1.3B of buybacks; ~$9.4B remaining buyback authorization; net dilution ~1-2% per year.

---

## 4. Management and Execution Quality

Lisa Su has served as AMD's CEO since 2014 and led the company from a fragile balance-sheet, product-disadvantaged cyclical semiconductor business into the main x86 server CPU challenger and a credible second-tier AI accelerator platform. Zen, the EPYC roadmap, the Xilinx acquisition, chiplet strategy, and the data center product cadence are the clearest evidence of management execution quality.

Current management strengths:

1. **Roadmap continuity:** CPU and GPU product cadence has avoided major disruptive gaps, and EPYC/Ryzen have already shown multiple cycles of execution.
2. **Mostly rational capital allocation:** Xilinx expanded AMD's Embedded / FPGA / adaptive computing footprint. The integration cycle is long, but it improves portfolio resilience.
3. **Relatively disciplined communication:** AMD generally avoids the kind of aggressive far-future extrapolation common in early-stage growth software stories, which matters in a volatile semiconductor cycle.
4. **Large-customer programs are entering the proof phase:** Meta 6GW, Helios, MI450, and Taiwan/UK ecosystem investments require management to prove system-level delivery in 2026-2027.

Management risks to monitor:

- Dilution from stock compensation and potential Meta warrant milestones.
- Whether AI platform investment compresses near-term margins.
- Whether ROCm ecosystem catch-up takes longer than the market expects.
- If AI capex slows, whether management can adjust inventory, supply commitments, and cost structure quickly enough.

Overall, AMD's management remains high quality within semiconductors, but the current valuation already embeds a meaningful "Lisa Su premium." The next evidence the market needs is not historical reputation, but quarterly proof from Meta/Helios, MI450, EPYC Venice, and ROCm.

### 4.1 Management Quantitative Record and Ownership

- **Market cap and stock:** under Lisa Su, market cap grew from about $3B (2014) to roughly $240B+ (2026), about 80x; the stock is up roughly +3,700% over her tenure.
- **Strategic M&A:** the Xilinx acquisition (~$49B) expanded the Embedded / FPGA / adaptive-computing footprint.
- **Ownership and incentives:** Lisa Su holds about 4.1M shares (~$993M as of December 2025); compensation is roughly 75% PRSUs and 25% options, heavily performance-tied.
- **Insider sales:** the February baseline disclosed Lisa Su selling ~$313M since 2021 (including ~138K shares in August 2025 and 125,000 shares on February 11), and EVP Forrest Norrod ~19,450 shares — normal liquidity management given high ownership, but worth tracking.

Management grade **A**.

---

## 5. Bull Case

The bull case is not that AMD is cheap. It is that AMD can evolve from NVIDIA's secondary alternative into a durable second AI infrastructure platform.

The case requires:

1. Meta's first 1GW deployment begins shipping in H2 2026 as planned and becomes visible in revenue.
2. MI450/Helios meets hyperscaler requirements on performance, power, stability, and delivery.
3. ROCm keeps narrowing the real-world usability gap with CUDA, at least in selected inference and private-cloud use cases.
4. EPYC server CPUs continue gaining share and improve platform attach economics.
5. Non-GAAP gross margin holds in the 55-60% range while operating leverage improves.

If those conditions hold together, AMD could reach a higher revenue tier in 2027-2028 and retain a platform premium.

### 5.1 Bull-Case Quantitative Evidence (February baseline; see body for updates)

1. **AI accelerator inflection:** Q4 2025 Data Center $5.4B (+39%); MI300X memory bandwidth ~60% higher than H100; Oracle launch cluster of 27,000 GPUs, Crusoe 13,000 MI355 (~$400M order); sell-side estimated ~$10-12B AI GPU revenue in 2026, scaling toward "tens of billions" in 2027. Capturing 10-15% of the AI accelerator market in 2027-2028 implies roughly $15-25B in annual revenue at 55%+ gross margin.
2. **CPU cash cow:** EPYC server share ~20-25% (Intel ~75-80%); Client Q4 2025 $3.1B (+34%); the CPU business can sustain ~10-15% annual growth and contribute roughly $15-18B.
3. **Margin expansion:** Q4 2025 non-GAAP operating margin 28%, FY2025 gross margin 54-57%, with ~55%+ gross margin on each incremental AI GPU dollar; non-GAAP operating margin could rise to 30-35% by 2027.
4. **Balance sheet:** net cash ~$9.1B, Debt/Equity 0.06, FCF $5.6B (2026E $7.2-7.4B), ~$9.4B remaining buyback authorization.
5. **ROCm catch-up:** the performance gap narrowed from ~40-50% to 10-30%, targeting 100K+ developers in 2026, at ~15-40% lower price than NVIDIA.

---

## 6. Bear Case

The bear case is also not that AMD is a bad company. It is that the current price requires near-perfect execution while NVIDIA's ecosystem and scale advantage remain very hard to break.

Main risks:

1. NVIDIA remains the overwhelming AI accelerator leader, with AMD used mainly for price discovery and supply-chain diversification.
2. Meta deployment is smaller, slower, or less profitable than the market extrapolates.
3. MI450/Helios underperforms on system-level reliability, software compatibility, or total cost of ownership.
4. AI capex growth slows in 2026-2027, hitting marginal suppliers harder.
5. Any quarterly miss triggers multiple compression from a very elevated starting point.
6. Taiwan supply-chain and export-control risks remain structural.

### 6.1 Bear-Case Quantitative Evidence (February baseline; see body for updates)

1. **CUDA moat:** NVIDIA AI accelerator share ~86-90% (it actually rose in 2025); AMD lost about 1 point of data center share year over year in 2025 despite growth; CUDA ~4M developers vs ROCm's 100K target (~1/40); the real-world performance gap is still ~10-30%; AMD must discount ~15-40%, capping profitability. If NVIDIA holds 80%+ share, AMD's AI GPU TAM may be structurally capped around $5-10B rather than the bull case's $20-30B.
2. **AI spending cycle:** 2026 hyperscaler AI capex ~$450B with unproven ROI; if growth decelerates from ~40% to 15%, AMD AI GPU revenue could peak around $8-10B instead of $20B+.
3. **Execution and concentration:** the top 3-4 customers could be 60%+ of AI GPU revenue; Meta's first 1GW still awaits H2 2026 validation; AMD has a history of delays (Vega, Radeon VII).
4. **Geopolitics and supply chain:** 100% TSMC dependency; China MI308 requires annual licensing, and Q1 2026 China revenue was well below Q4 2025; regulatory change could erase ~$1-2B of revenue at once; a Taiwan Strait conflict scenario could cut revenue 15-20% and reprice the stock 40-50%.
5. **Valuation cushion:** the historical P/E range is ~15-50x, and the stock has repeatedly drawn down 30%+; at bear 2027 revenue $38-42B, 22-25% operating margin, EPS $3.5-4.0, and a historical 22x basis, the mechanical price is about $77-88.

---

## 7. Valuation Rerun

### 7.1 Current Valuation

| Metric | Current read |
|--------|--------------|
| Share price | **$537.37** (June 18, 2026 close) |
| Market cap | About **$887B** |
| Enterprise value | About **$878B** |
| EV/TTM Sales | About **23.4x** |
| EV/Forward Sales | About **17.6-19.2x** assuming FY2026 revenue of $45.7-50.0B |
| Q1 annualized non-GAAP P/E | About **98x** |
| FCF yield | About **1.2%** using annualized Q1 FCF |

### 7.2 Scenario Framework, Not a Price Target

The following is a reverse-engineering framework, not investment advice or a formal price target.

| Scenario | Key assumptions | Mechanical range |
|----------|-----------------|------------------|
| Bear | 2027 revenue $45-50B, EPS $5-7, market assigns 25-35x; limited AI share gains | About $150-280 |
| Base | 2027 revenue $65-75B, EPS $8-11, market assigns 35-45x; Meta/Helios executes but does not reshape the industry | About $330-500 |
| Bull | 2027-2028 revenue $90-110B, EPS $14-20, market sustains 40-50x; AMD becomes the durable #2 AI platform | About $550-900 |

**Interpretation:** The current $537.37 price is already near the lower end of the bull case, not the middle of the base case. Liking AMD as a company and liking the current risk/reward are now two separate conclusions.

### 7.3 Treatment of Old Valuation Ranges

| Old method | Old range | Current treatment |
|------------|-----------|-------------------|
| Base DCF | $120-140 | Stale; retained only as historical record |
| Bull DCF | $180-220 | Old bull case is now below current market price |
| Bear DCF | $70-90 | Still useful only as a stress-case reference |
| P/E comps | $100-120 | Old forward EPS and multiple inputs are stale |
| EV/Sales comps | $110-130 | Old 5-6x forward sales framework does not match today's AI platform premium |

### 7.4 Peer Valuation Comparison (February baseline; AMD row updated to current)

| Company | Forward P/E | EV/Sales | Gross margin | Growth | Position |
|---------|-------------|----------|--------------|--------|----------|
| NVIDIA | 30-35x | 18-20x | ~75% | 40-50% | AI GPU leader (~90% share) |
| AMD | ~98x (Q1 annualized non-GAAP; old 36-40x) | ~23.4x TTM / 17.6-19.2x 2026E (old 5.2x) | 55-56% | Q1 +38%, Q2 guide midpoint ~+46% | AI GPU #2 |
| Intel | 15-20x | 2.5x | ~40% | 5-10% | CPU leader (share under pressure) |
| Broadcom | 25-30x | 12-15x | ~65% | 20-25% | Diversified infra |

Supplemental market cap and revenue (February baseline; AMD updated): AMD market cap ~$887B (old ~$240B), FY2025 revenue $34.6B, net cash ~$9.1B (old ~$3.9B); NVIDIA market cap ~$2.8T, revenue $130B+; Intel market cap ~$180B, revenue ~$55B; Broadcom market cap ~$850B, revenue ~$52B. AMD still trades at a P/E premium to leader NVIDIA, indicating high expectations are already priced in.

---

## 8. Catalysts and Monitoring Checklist

Over the next 12-18 months, delivery quality matters more than headline count:

1. Q2 2026 results vs. the $11.2B revenue guide and 56% non-GAAP gross margin guide.
2. Whether Data Center revenue continues to grow faster than company revenue.
3. Whether Meta's first 1GW deployment begins shipping in H2 2026 and appears in Q3/Q4 results.
4. Whether the MI450/Helios pipeline turns from "forecasts above initial expectations" into orders, revenue, and margin.
5. Auditable signs of ROCm developer adoption, customer migration, and model performance.
6. Net share count after stock compensation, buybacks, and Meta warrant milestones.
7. Whether NVIDIA Rubin / Vera Rubin compresses AMD's performance or price-performance window.

### 8.1 Key Timeline and Run-Rate Targets (February baseline)

- **Key dates:** late April 2026 Q1 results (reported), June Computex (products and roadmap), Q3 (around October) Meta/Helios shipment update, Q4 (January 2027) full-year results and 2027 guidance.
- **Milestone thresholds:** Data Center moving toward a $25-30B annual run rate; AI GPU revenue around $8-10B in 2026; non-GAAP operating margin above 30% by 2027; AI accelerator share toward 10%+ by end of 2026.
- **Product cadence:** MI400 series (CDNA 5) targeting 2nm, 20 PFLOPs FP8, 432GB HBM4; MI455X up to ~3 AI exaflops per rack; MI500 series planned for 2027; NVIDIA Rubin (H2 2026) about +3.3x compute over Blackwell B300.

---

## 9. Key Uncertainties and Thesis-Breaking Conditions

### 9.1 AI Infrastructure Spending Sustainability

AMD's current valuation is highly dependent on hyperscalers and large internet customers continuing to expand AI infrastructure capex. The open questions are:

- Whether enterprise and platform AI workloads can keep absorbing incremental compute in 2026-2027.
- Whether hyperscalers are expanding against real demand or building ahead of demand.
- Whether model training efficiency, inference optimization, and custom ASICs reduce marginal demand for merchant GPUs.

If AI capex growth decelerates sharply, AMD may be more exposed than NVIDIA because it is still the second supplier trying to earn platform status.

### 9.2 Meta Deployment Scale, Timing, and Economics

Meta 6GW is the most important verified customer anchor, but several variables remain open:

- Whether the first 1GW deployment begins shipping in H2 2026 as planned.
- GPU count, ASP, gross margin, and revenue recognition timing behind each gigawatt.
- Whether the broader 6GW roadmap scales linearly or depends on milestones, performance, and budget reconfirmation.
- The net effect of Meta warrants after considering dilution, customer lock-in, and deployment visibility.

The 6GW headline should not be mechanically translated into near-term revenue. The key evidence is whether Q3/Q4 2026 results show shipment, revenue, and margin validation together.

### 9.3 ROCm and Software Ecosystem

ROCm remains the main bottleneck between hardware substitution and platform substitution. Watch:

- Whether developers, frameworks, models, and enterprise customers actually migrate, not just benchmark or pilot.
- Whether CUDA keeps high-value training workloads locked into NVIDIA.
- Whether AMD can build repeatable wins in inference, private cloud, customized systems, and multi-vendor procurement.

If ROCm progresses more slowly than expected, AMD can still benefit from supply-chain diversification, but the platform premium should compress.

### 9.4 Competition and Supply Chain

Competitive risk is broader than NVIDIA alone:

- NVIDIA Rubin / Vera Rubin could widen the performance, software, and system-level gap again.
- Intel stabilization in server CPUs would cap EPYC's medium-term upside.
- Hyperscaler custom ASICs could reduce the long-term TAM for merchant GPUs.
- Advanced-node and advanced-packaging supply remain heavily tied to TSMC and Taiwan; geopolitical risk cannot be diversified away by near-term earnings strength.

### 9.5 Thesis-Breaking Conditions

**Bull case invalidation signals:**

- Meta's first 1GW deployment slips materially beyond 2026, or the broader 6GW roadmap is reduced.
- Data Center revenue growth falls below company-level revenue growth for multiple quarters.
- Non-GAAP gross margin falls back toward 50%, suggesting AI platform pricing or cost pressure.
- ROCm customer cases and developer adoption fail to show auditable progress.
- NVIDIA's next platform narrows AMD's performance-per-dollar window.

**Bear case invalidation signals:**

- Meta/Helios ramps on schedule and shows up in both revenue and margin.
- AMD AI accelerator share reaches a stable double-digit level with new large customers beyond Meta.
- ROCm produces repeatable migration cases in inference and private-cloud workloads.
- Data Center mix lifts company non-GAAP operating margin toward 30%+.
- Valuation resets to a level more directly supportable by FCF, EPS, and verifiable orders.

---

## 10. Conclusion

**Current conclusion:** AMD's company quality and strategic position are stronger than in the February report. But the stock has also moved from "high-valuation growth stock" to "extremely high-expectation pricing." The full rerun changes the report's core stance from "cautiously bullish" to a high-expectation monitoring framework.

**For existing holders:** The key evidence to track is Q2/Q3 Data Center revenue, Meta/Helios shipment evidence, and gross margin. A miss in any of those areas could matter disproportionately.

**For new capital:** The old "wait for a 10-15% pullback" framework is no longer enough. The cleaner threshold is either more fundamental proof or a valuation that can be explained more directly by cash flow and EPS.

**Review windows:** Recheck after Q2 2026 results for Data Center and gross margin; recheck after Q3/Q4 2026 for Meta/Helios shipment evidence.

---

## Appendix

### A. Data Sources and Verification Approach

This version prioritizes AMD official IR materials, earnings releases, investor announcements, and verifiable market quotes. The old OpenAI customer assumption is no longer treated as a current fact; the verified customer anchor is AMD's officially disclosed multi-year, multi-generation 6GW Instinct GPU partnership with Meta.

Market data uses the latest verifiable U.S. close as of June 18, 2026. Valuation multiples are rough frameworks for understanding market-implied expectations, not price targets.

### B. Current Key Assumptions

- AI infrastructure demand remains strong through 2026-2027, though the growth rate may be volatile.
- Meta's first 1GW deployment begins shipment validation in H2 2026.
- EPYC server CPUs continue gaining share and provide the attach base for data center platform sales.
- ROCm narrows the usability gap with CUDA in selected workloads, but does not fully catch NVIDIA's ecosystem in the near term.
- TSMC advanced-node and advanced-packaging supply remains available, with no major geopolitical disruption.

### C. Sensitivity Framework

- **Revenue growth:** If FY2026 revenue lands below $45B, EV/Forward Sales pressure rises further.
- **Gross margin:** If non-GAAP gross margin cannot stay above 55-56%, the AI platform premium should be reassessed.
- **Dilution:** Meta warrants and stock-based compensation require ongoing net share-count monitoring.
- **Valuation multiple:** The current price is highly sensitive to multiple compression; even better fundamentals may not offset a lower multiple.

**Quantified sensitivities (February baseline model):** each ~±5% change in revenue growth moves valuation ~±15-20%; each ~±2% change in AI GPU share (~±$2-3B revenue) moves valuation ~±10%; each ~±2% change in operating margin moves EPS ~±8-10%; each ~±5x change in P/E moves the stock ~±20-25%.

**Base-case assumptions (February):** AI accelerator market CAGR ~25-30% through 2030, AMD AI share ~10-12% and server CPU share ~28-30% by 2027, gross margin stable at 55-57%, operating margin rising to 28-30% by 2027.

### D. Glossary

- **CDNA:** AMD's data center GPU architecture.
- **CUDA:** NVIDIA's parallel computing platform and developer ecosystem.
- **EPYC:** AMD's server CPU product line.
- **FCF:** Free cash flow.
- **Helios:** AMD's rack-scale AI infrastructure architecture.
- **Instinct:** AMD's data center AI accelerator product line.
- **ROCm:** AMD's open-source GPU compute software platform.
- **TAM:** Total addressable market.
- **TSMC:** Taiwan Semiconductor Manufacturing Company.
- **Xilinx:** FPGA / adaptive computing company acquired by AMD in 2022.

---

## Sources

- [AMD Q1 2026 Financial Results](https://ir.amd.com/news-events/press-releases/detail/1284/amd-reports-first-quarter-2026-financial-results)
- [AMD and Meta 6GW Partnership](https://ir.amd.com/news-events/press-releases/detail/1279/amd-and-meta-announce-expanded-strategic-partnership-to-deploy-6-gigawatts-of-amd-gpus)
- [AMD Taiwan Ecosystem Investment](https://ir.amd.com/news-events/press-releases/detail/1286/amd-announces-more-than-10-billion-in-taiwan-ecosystem-investments-to-accelerate-ai-infrastructure)
- [AMD Venice EPYC Production Ramp](https://ir.amd.com/news-events/press-releases/detail/1287/amd-announces-production-ramp-of-next-generation-amd-epyc-processor-venice-on-tsmc-2nm-process-technology)
- [AMD UK AI Investment](https://ir.amd.com/news-events/press-releases/detail/1288/amd-commits-up-to-2-billion-to-accelerate-ai-innovation-and-research-in-the-united-kingdom)
- [MarketWatch AMD quote](https://www.marketwatch.com/investing/stock/amd)

---

**Original report completed:** February 4, 2026
**Full rerun completed:** June 22, 2026
**Next suggested review:** After Q2 2026 results; again after Meta/Helios enters shipment validation
