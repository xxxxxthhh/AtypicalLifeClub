# NVIDIA (NVDA) Deep Research Report

Coverage date: 2026-06-26
Last updated: 2026-07-07
Ticker: NASDAQ: NVDA
Disclaimer: This report is for informational and research purposes only. It does not constitute investment advice. Please conduct your own due diligence.

> **Fiscal-year note:** NVIDIA's fiscal year ends in late January. In this report **FY2026** is the year ended 2026-01-25; **Q1 FY2027** is the quarter ended 2026-04-26 (reported 2026-05-20), the latest quarter as of publication. Unlike the calendar-quarter convention used in this center's other reports, NVIDIA figures always use the company's official fiscal labels. Read alongside this center's Broadcom, AMD, GE Vernova and Bloom Energy reports — NVIDIA and Broadcom form the "compute side" of AI infrastructure, while GE Vernova and Bloom are the "power side"; only together can the full AI-infrastructure chain be assessed.

---

## Executive Summary

**One-line thesis:** NVIDIA is the indispensable hub of this AI-compute cycle — the CUDA software ecosystem + a full-stack system (GPU + NVLink + networking) + an annual product cadence form the strongest moat in the market today, and Q1 FY2027 revenue of $81.6B (+85% YoY) with Data Center at $75.2B (+92%) is still accelerating. But it is already the world's most valuable company (~$4.68T), so **the core question is not "is it good" but "at what slope can a base this large keep beating expectations, with zero China Data Center revenue assumed, custom-ASIC competition rising, and the durability of AI capex unproven."**

**Verdict:** **Constructive / medium conviction.** The v5 scenario grid separates skew from conviction: NVIDIA's accelerator profit pool, rack/system attach, networking/software moat, and annual platform cadence still make the base case positively skewed; custom ASICs, China at zero, AI capex slope, and circular-financing impairment would reset the earnings denominator, so the stance does not move to bullish.

**Current market read (as of 2026-06-26):** the Research Hub price ledger anchors NVDA at a **$192.53** close; on ~**24.30B** diluted shares (FY2026 year-end), market cap is ~**$4.68T**, the largest in the world. The 52-week range is ~**$151.49 - $236.54**, leaving the stock ~19% below its 52-week high. Quote sources: [Yahoo Finance NVDA](https://finance.yahoo.com/quote/NVDA/), [CompaniesMarketCap NVDA](https://companiesmarketcap.com/nvidia/marketcap/); financial sources: [NVIDIA Q1 FY2027 press release](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027), [NVIDIA FY2026 results](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026).

**Key data:**

| Metric | Value |
|--------|-------|
| Price (2026-06-26) | $192.53 |
| Market cap | ~$4.68T (~24.30B shares; world's #1) |
| 52-week range | $151.49 - $236.54 |
| Forward P/E (FY2027E) | ~25x (vs AMD ~58x, Broadcom ~33x) |
| P/E (FY2026 GAAP) | ~39x ($4.68T / FY2026 net income $120.1B) |
| EV/TTM Sales | ~18-19x (TTM revenue ~$253B) |
| Q1 FY2027 revenue | $81.6B (+85% YoY, +20% QoQ) |
| Q1 FY2027 Data Center | $75.2B (+92% YoY, +21% QoQ) |
| Q1 FY2027 Gaming | $7.07B (+58% YoY) |
| Q1 FY2027 gross margin (GAAP / non-GAAP) | 74.9% / 75.0% |
| Q1 FY2027 EPS (GAAP / non-GAAP) | $2.39 / $1.87 (GAAP includes a $15.9B unrealized equity gain) |
| Q2 FY2027 guidance | revenue $91.0B ±2%, GM ~75% (**assumes no China Data Center compute revenue**) |
| FY2026 revenue | $215.9B (+65% YoY) |
| FY2026 Data Center | ~$193.7B |
| FY2026 GAAP net income / EPS | $120.1B / $4.90 |
| FY2026 gross margin (GAAP / non-GAAP) | 71.1% / 71.3% |
| Cash & marketable securities | $50.3B |
| Capital return | +$80B buyback authorization + quarterly dividend $0.01→$0.25 |
| AI ecosystem equity investments / commitments (public reporting) | 2026 H1 public-report estimate >$40B (incl. OpenAI, CoreWeave, etc.); not all of it is company-disclosed cash deployment |

---

## 1. Business Overview

Founded in 1993, NVIDIA started in graphics (GPUs) and, with the 2006 launch of **CUDA**, turned the GPU from "rendering games" into a "general-purpose parallel computing engine," becoming the de facto hardware standard for AI training and inference. Today it is not a "chip vendor" but a vendor of **AI-infrastructure systems**.

**Revenue is heavily concentrated in Data Center:**

- **Data Center (~92% of Q1 FY2027):** the absolute core. It includes GPUs for AI training/inference (Hopper → Blackwell → Blackwell Ultra/GB300 → Rubin), rack-scale systems (GB200/GB300 NVL72), networking (NVLink, InfiniBand, Spectrum-X Ethernet) and the software stack. Q1 FY2027 Data Center revenue was $75.2B (+92% YoY), driven by the Blackwell 300 (GB300) ramp and strong networking demand.
- **Gaming (~9%):** GeForce RTX; Q1 FY2027 revenue $7.07B (+58% YoY) — still a steady cash cow, but a supporting act next to Data Center.
- **Pro Visualization, Auto & Robotics:** smaller, long-dated optionality (autonomous driving, humanoid robotics via Jetson/Thor, Omniverse digital twins), with limited revenue contribution today.

**The business model:** NVIDIA does not sell a single GPU; it sells the full design of an "AI factory." Customers (clouds, sovereign AI, enterprises) buy a system that directly produces tokens — silicon + interconnect + a software stack (CUDA, cuDNN, TensorRT, NIM microservices). That hardware-software bundle makes switching costs enormous once a customer builds on CUDA, and is the root cause of durable 70%+ gross margins.

**Full-year FY2026:** revenue $215.9B (+65% YoY), GAAP net income $120.1B, diluted EPS $4.90, GAAP gross margin 71.1%. Data Center was ~$193.7B for the year, about 90% of total revenue.

## 2. Industry & Competitive Position

### 2.1 The moat is three layers (CUDA + full-stack systems + cadence), not one

NVIDIA's moat is often reduced to "CUDA lock-in," but it is really three stacked layers:

1. **Software (CUDA + ecosystem):** nearly two decades of developer ecosystem, libraries and tooling — the hardest part to replicate. Even a competitor with comparable silicon faces the migration wall of "the customer's existing CUDA code base."
2. **Full-stack systems:** after acquiring Mellanox, NVIDIA bundles the GPU, NVLink (chip-to-chip interconnect) and InfiniBand/Spectrum-X (node-to-node networking) into rack-scale solutions. The bottleneck in AI training shifted long ago from single-chip compute to interconnect bandwidth, and NVIDIA leads there too.
3. **Cadence:** the company has compressed iteration to an **annual cadence** (Hopper→Blackwell→Blackwell Ultra→Rubin), keeping competitors a generation behind with each performance/efficiency jump.

### 2.2 The real structural threat is custom ASICs, not AMD

Competition comes from two directions with very different threat levels:

- **AMD (head-on GPU competitor):** the MI450/MI400 series is a credible "second source," and public reports indicate Meta may deploy up to 6GW of MI450s (multi-year contract value estimated ~$60B). But the gap is still vast: NVIDIA's FY2026 Data Center revenue was ~$193.7B vs AMD Instinct's estimated ~$7-8B. AMD is gaining, but the absolute gap is still widening. AMD's value is more "a bargaining chip and supply redundancy for hyperscalers" than a near-term disruptor.
- **Custom ASICs (the deeper structural threat):** hyperscaler in-house silicon is the more fundamental erosion of NVIDIA's share and pricing power. As design partner, Broadcom's AI ASIC revenue reportedly topped $20B in its FY2025 (Broadcom's fiscal year ended Nov 2025), behind Google TPU, Meta MTIA, Microsoft Maia, and OpenAI / Anthropic in-house accelerator programs. Treat this as a public-reporting / industry-breakdown data point, not a fully company-confirmed customer disclosure; it should be reconciled to Broadcom's official disclosures at the next review. The logic is direct: for relatively fixed inference workloads, hyperscalers are motivated to replace general-purpose GPUs with cheaper, more power-efficient dedicated chips and reinvest the savings in more compute.

**Key judgment:** NVIDIA's lead in **training** and on the **frontier / fast-evolving workloads** is hard to dislodge near-term; but in **inference** and **mature workloads**, custom ASICs will keep eating incremental share. The question is not whether NVIDIA loses leadership, but **what level its share of the total AI-compute pie settles at** as it falls from near-monopoly.

### 2.3 Customers are concentrated and are "both customer and competitor"

Data Center revenue is concentrated in a few hyperscalers (Microsoft, Amazon, Google, Meta) and emerging AI clouds (CoreWeave, Oracle, etc.). That creates a double tension:

- **Concentration risk:** the capex decisions of a few customers directly set NVIDIA's quarterly slope.
- **Customers are competitors:** those same names are replacing GPUs internally with Broadcom/in-house silicon. NVIDIA's response is to embed itself in customers' compute expansion (see the equity investments + compute lock-in in Section 7) — which also fuels the "circular financing" debate.

## 3. Financial Health

### 3.1 Q1 FY2027: a record set with "China at zero"

Q1 FY2027 (ended 2026-04-26) is a "still accelerating despite missing a leg" print:

- Total revenue **$81.6B** (+85% YoY, +20% QoQ); Data Center **$75.2B** (+92% YoY).
- GAAP / non-GAAP gross margin **74.9% / 75.0%**, recovering from FY2026's full-year 71% — showing the early-Blackwell-ramp margin drag is largely worked off.
- Non-GAAP diluted EPS **$1.87** (+140% YoY).
- **The single most important sentence: guidance (Q2 FY2027 revenue $91.0B ±2%) assumes no China Data Center compute revenue**, and there were no Hopper Data Center shipments to China in the quarter (vs $4.6B a year earlier). In other words, this record print was achieved with the China market essentially zeroed.

### 3.2 GAAP profit is inflated by a $15.9B unrealized equity gain — read with care

Q1 FY2027 shows an anomaly: **GAAP EPS ($2.39) is higher than non-GAAP EPS ($1.87)**. The cause is **net gains from equity securities of $15.9B** in the quarter, primarily **unrealized** appreciation in publicly-held and non-marketable equity stakes (e.g., CoreWeave).

Two implications:

1. **Trailing GAAP P/E will be artificially depressed and distorted.** Folding non-cash, non-operating investment gains into net income makes the GAAP-based P/E look cheaper than the true operating earnings power. For NVIDIA's earnings, the **non-GAAP operating basis is more reliable than GAAP**.
2. **It ties the income statement directly to the AI capital cycle.** When AI valuations rise, NVIDIA's GAAP profit is amplified by the mark-ups; if AI private/public valuations pull back, this flows the other way — a new source of income-statement volatility that moves with the AI cycle.
3. **Concentration risk in the equity portfolio is not fully transparent.** The CoreWeave stake (~$2B at IPO) accounts for only a fraction of the $15.9B Q1 gain; the bulk likely comes from private-company mark-ups whose valuations are mark-to-model rather than mark-to-market, and whose concentration across a few large positions is not publicly broken out. A concentrated pullback in AI private valuations would flow through GAAP earnings disproportionately.

### 3.3 Balance sheet solid, capital return turning aggressive

- Cash and marketable securities of **$50.3B**, small debt, positive net cash — a sound structure.
- Capital return stepped up sharply: a **new $80B buyback authorization** and the quarterly dividend raised from $0.01 to **$0.25** (25x). This usually signals management's high confidence in free-cash-flow durability.
- But read it alongside 2026 H1 public reports of **>$40B** in AI ecosystem equity investments / commitments (Section 7). "Large buybacks/dividends and large outbound investing at the same time" is not contradictory (FCF is ample), but the direction of the investing (into ecosystem partners / potential customers) is the heart of the valuation debate.

## 4. Management & Governance

Founder-CEO **Jensen Huang** has led since 1993 and is one of the most successful founder-CEOs in semiconductor history: the decade-plus of "no visible return" investment in CUDA, the early bet on the data-center pivot, and reshaping the company from a gaming-graphics vendor into an AI-infrastructure platform all validate his long-term strategic judgment and execution. Management's track record on product cadence and guidance delivery is excellent.

**Governance and points to monitor:**

- **Capital allocation enters a new phase:** from "almost no dividend, asset-light" to "$80B buyback + dividend + large AI ecosystem equity investments / commitments." The latter (investing in customers/ecosystem) is a new, sizeable capital-allocation bet whose returns need to be validated over coming quarters.
- **Insider selling:** at all-time-high prices, track founder/executive routine (10b5-1) selling cadence as a sentiment/valuation reference, not a short thesis.
- **Key-person dependence:** strategy is tightly bound to Jensen Huang — a tail consideration to include in long-term governance.

**Management grade: A (outstanding execution + long-term strategic foresight); the new capital-allocation direction remains to be proven.**

## 5. Bull Case

**Core thesis:** AI compute demand is still early, NVIDIA is the unavoidable hub of this generation of AI infrastructure, and the current multiple (~25x forward) is not expensive relative to its growth (+85%).

1. **Strong demand visibility, growth still accelerating.** Q1 FY2027 +85%, with Q2 guidance of $91B implying further sequential expansion — and that is **ex-China**. New demand layers (sovereign AI, enterprise inference, agentic AI) are still opening.
2. **A three-layer moat (CUDA + systems + cadence) that no one can replicate full-stack near-term.** Even if share falls from monopoly, expansion of the absolute pie can sustain revenue for years.
3. **Gross margin back to 75%, strong cash generation.** The $80B buyback + 25x dividend hike are hard signals of FCF durability.
4. **The multiple is not extreme.** ~25x forward, below AMD (~58x) and Broadcom (~33x). "Most expensive absolute market cap" coexists with "a not-expensive relative multiple" — if earnings deliver, the multiple is supported.
5. **China is pure optionality.** Guidance already assumes China at zero; any easing of export policy is **pure incremental upside** you don't have to pay for.

## 6. Bear Case

**Core thesis:** at a $4.68T base, any "AI-capex peak/digestion" signal is amplified; the denominator (earnings expectation), not the numerator (the multiple), is the real risk source.

1. **Law of large numbers + the capex cycle.** Data Center revenue is already running above a $300B annual rate; sustaining high growth requires hyperscalers to **raise capex year after year**. If AI investment ROI disappoints or macro tightens, capex peaks before revenue — and NVIDIA is the highest-beta link in that chain.
2. **Custom ASICs keep eating inference share.** Public reporting indicates Broadcom's AI ASIC revenue already topped $20B in its FY2025 (Broadcom fiscal year ended Nov 2025) and that it is involved in multiple hyperscaler in-house programs. Inference is the larger, more standardized workload — exactly the ASIC home turf.
3. **Structural loss of the China market.** A market once estimated to grow toward ~$50B has had the door shut, and geopolitical risk is two-sided (accelerating China domestic substitution + reversible U.S. policy).
4. **"Circular financing" concerns.** Public reports indicate NVIDIA has built large equity-investment or commitment exposure to AI ecosystem partners / potential customers (incl. OpenAI, CoreWeave, etc.), while Q1 GAAP profit includes a $15.9B net gain from equity securities. The structure is being compared to dot-com-era "vendor financing" — if AI private valuations pull back, it creates a double hit of "investment write-downs + slowing end demand."
5. **Expectations are very high, error tolerance very low.** The market has priced in years of high growth. A single quarter's guidance miss, or one hyperscaler cutting capex, could trigger a sharp valuation reset (see the same-cycle lesson of Salesforce being "narrative-repriced").

## 7. Key Uncertainties

1. **Sustainability and ROI of AI capex.** Can hyperscaler AI capex be supported by real application revenue / productivity returns? This is the biggest binary variable in the whole chain. When we'll know more: watch each quarter's capex guidance and AI-revenue disclosure from Microsoft/Google/Meta/Amazon.
2. **The quality of "circular financing."** Per public reporting / market breakdowns, NVIDIA has investment or commitment exposure to OpenAI (reported $30B, cut from an earlier $100B LOI), CoreWeave (reported 7% stake, $2B @ $87.20/share), IREN, Nebius, etc.; is this "rational ecosystem lock-in" or "manufacturing its own demand"? The key is whether these investees' end demand is real and self-sustaining. The next review should reconcile this with NVIDIA's official disclosures and investee financing documents.
3. **The pace of custom-ASIC substitution.** How steep is the migration of inference workloads to ASICs? Can NVIDIA defend with Rubin's efficiency/TCO advantage?
4. **China policy path.** Will export controls tighten further, hold, or see a "pay-for-access" easing? Either direction materially changes the value of the China option.
5. **Gross-margin durability.** How long can a 75% gross margin hold under competitive (ASIC/AMD) price pressure and mix shift (systems vs chips)?

**Thesis-breaking events:**
- If hyperscalers cut capex guidance for **two consecutive quarters**, the bull thesis (demand acceleration) is materially challenged.
- If a major hyperscaler **publicly shifts training workloads at scale to in-house/ASIC**, the moat narrative is damaged.
- If an AI private-valuation drawdown forces NVIDIA to take a **large write-down on its investment portfolio**, the "circular financing" bear thesis is confirmed.

## 8. Valuation Context

> The following is valuation "context," not a price target or a buy/sell recommendation.

- **Forward P/E ~25x (FY2027E, Non-GAAP basis):** the most counter-intuitive part of NVIDIA's valuation — as the world's largest company, its forward multiple is **below** AMD (~58x) and Broadcom (~33x). On +85% growth, the PEG framing is not expensive. Note that this is a Non-GAAP consensus estimate; GAAP earnings include large equity mark-ups ($15.9B in Q1 FY2027 alone) that artificially depress the multiple — Non-GAAP is the correct basis here. Also note that the comparison to AMD's ~58x is across very different earnings bases: NVIDIA at 25x sits on a ~$300B+ annualized revenue / $120B+ net income base, while AMD at 58x is priced on earnings that are just inflecting from a much lower base; direct comparison requires this context.
- **FY2026 GAAP P/E ~39x:** based on $4.68T market cap / $120.1B FY2026 net income. Note that from Q1 FY2027 GAAP net income includes large equity mark-ups, which will distort trailing GAAP P/E lower thereafter — use non-GAAP operating earnings instead.
- **EV/TTM Sales ~18-19x:** TTM revenue ~$253B (FY2026 $215.9B − Q1 FY26 ~$44B + Q1 FY27 $81.6B); EV ~$4.72T (market cap − ~$42B net cash).
- **Reading the multiple:** NVIDIA's valuation risk is **not the multiple itself** but the **earnings-expectation denominator** the multiple implies. If the AI super-cycle runs another 2-3 years, the current multiple is low; if capex peaks within 12-18 months, the "high growth" assumption behind a 25x forward P/E gets reset quickly, and multiple and earnings contract together.

**Scenario grid:**

| Scenario | Driver assumptions (profit pool / attach / moat / denominator) | Valuation implication (rich / fair / cheap vs today) | Subjective probability weight |
| --- | --- | --- | --- |
| Bull | The AI accelerator profit pool keeps expanding; inference, sovereign AI, and agentic workloads lift rack-level demand; Blackwell/Rubin system attach, NVLink/networking, and software expand profit per rack; China partly reopens; custom ASICs mainly take mature inference rather than frontier training workloads | Today looks cheap: the earnings denominator keeps moving up, and a mid-20s forward P/E can be absorbed without multiple expansion | 30% |
| Base | Q2 FY2027 broadly delivers the $91.0B guide, Data Center growth slows but remains strong; rack/system attach and the networking/software moat offset some GPU ASP normalization; custom ASICs take incremental share in inference and mature workloads; China remains near zero; the multiple stays in the mid- to high-20s | Today is fair to slightly cheap: the market prices an AI super-cycle but has not fully capitalized the protection that system attach plus software/networking moat provide to the profit pool | 50% |
| Bear | hyperscaler capex weakens for consecutive quarters, Data Center revenue stalls sequentially; custom ASICs accelerate substitution in inference and mature workloads; China becomes a larger permanent gap; OpenAI/CoreWeave-type investments or demand backstops create impairment / circular-financing concerns; forward P/E and the earnings denominator reset together | Today looks rich: the risk is not the multiple alone but simultaneous compression in earnings expectations and multiple | 20% |

**What's priced in & the expectation gap:** At the $192.53 close on Jun 26, 2026 and roughly $4.68T market cap, the market is not pricing a generic AI CAGR; it is pricing a combined GPU+networking+systems+software machine that protects the accelerator profit pool. A mid-20s forward P/E does not look extreme because the denominator already sits on a $300B+ annualized revenue / $120B+ profit base; the real implied ask is Q2's $91.0B revenue guide, 75% gross margin, rack/system attach, and networking/software moat continuing to defend the profit pool while custom ASIC and China risks do not quickly reset the denominator. Our base case says those conditions mostly hold, leaving a modestly positive expectation gap at today's price.

## 9. Catalysts & Monitoring Checklist

**Near-term (0-6 months):**
- Q2 FY2027 results (~August 2026): whether it delivers the $91B guide, holds 75% gross margin, and the next-quarter guidance slope.
- Hyperscaler (MSFT/GOOG/META/AMZN) quarterly capex-guidance direction.
- Any change in China export policy.
- Rubin platform launch/shipment timeline and early orders.

**Medium-term (6-18 months):**
- Actual custom-ASIC penetration data in inference workloads.
- Valuation and impairment trends in NVIDIA's investment portfolio (OpenAI/CoreWeave, etc.).
- Whether evidence of "real revenue/ROI" at the AI application layer emerges.

**Long-term (18+ months):**
- The expansion rate of the total AI-compute pie and NVIDIA's share trajectory within it.
- Whether new growth layers (robotics/autonomy/sovereign AI) convert into meaningful revenue.

**Metrics to monitor continuously:** Data Center sequential slope, non-GAAP gross margin, hyperscaler capex, ASIC share, China policy, and changes in the fair value of the investment portfolio.

## 10. Conclusion

NVIDIA's chain-validation job is to test whether the AI compute profit pool remains led by general-purpose accelerators, rack/system attach, NVLink/networking, and the CUDA/software moat, rather than being reset by hyperscaler custom ASICs, the China gap, or capex digestion. Q1 FY2027 growth of +85% with China at zero validates demand strength; the remaining question is whether that strength keeps protecting the earnings denominator.

The expectation gap is modestly positive: at $192.53, roughly $4.68T market cap, and a mid-20s forward P/E, the market is pricing continued accelerator profit-pool expansion rather than a generic AI CAGR; our base case sees rack/system attach, networking/software moat, and the annual platform cadence still protecting the earnings denominator, while custom ASIC and China risks are not yet large enough to offset that advantage.

The current stance is **constructive, medium conviction**. The 30% bull / 50% base / 20% bear scenario grid gives positive skew: the bull case comes from profit-pool expansion, system attach, and software/networking moat; the base case comes from Q2 guide delivery and gradual custom-ASIC penetration; the bear case comes from capex, ASIC, China, and circular financing compressing the earnings denominator together. Conviction is medium because financial and ecosystem evidence are very strong, but customer capex and ASIC substitution remain high-impact variables.

Move to bullish if Q2 FY2027 delivers the $91.0B revenue guide, Data Center sequential slope and 75% non-GAAP gross margin both hold, rack/system attach and networking/software attach expand the profit pool, and ASIC/China/circular-financing risks do not rise. Move to neutral-watch or cautious if hyperscaler capex weakens for consecutive quarters, Data Center revenue stalls sequentially, custom ASICs keep taking incremental profit pool in inference/mature workloads, or China / portfolio impairments reset the earnings denominator.

## Appendix: Sources & Assumptions

**Primary sources:**
- [NVIDIA Q1 FY2027 press release](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027) (quarter ended 2026-04-26, reported 2026-05-20)
- [NVIDIA Q1 FY2027 8-K (SEC)](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000051/q1fy27pr.htm)
- [NVIDIA FY2026 / Q4 results](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026)
- Quote & market cap: [Yahoo Finance NVDA](https://finance.yahoo.com/quote/NVDA/), [CompaniesMarketCap NVDA](https://companiesmarketcap.com/nvidia/marketcap/), [Macrotrends market cap/shares](https://www.macrotrends.net/stocks/charts/NVDA/nvidia/market-cap)
- Competition & valuation comps: Broadcom custom ASIC and AMD MI450 (public reporting / industry breakdowns, 2026 H1; not all items are direct company disclosures)
- "Circular financing" / reported OpenAI investment or LOI cut to $30B: public reporting (2026 H1; treated as a risk hypothesis pending official-document reconciliation)

**Key assumptions & basis:**
- Market cap estimated at ~24.30B shares × $192.53; different sources put market cap in the ~$4.6-5.0T range depending on date and methodology.
- TTM revenue ≈ FY2026 $215.9B − Q1 FY26 ~$44B + Q1 FY27 $81.6B ≈ $253B; EV nets out ~$42B of net cash.
- Forward P/E ~25x, AMD ~58x, Broadcom ~33x reflect a mid-2026 (~May) market read and move with price and expectations.
- Figures labeled FY2026 / Q1 FY2027 are company-reported; competitor figures are public-reporting estimates and should be reconciled to the latest 10-Q/results at the next review.
- This report is **initial coverage**; it includes no prior-cycle comparison. The 2026-07-07 v5 backfill adds the stance/conviction frame through scenario assumptions, probability weights, and priced-in expectations. Refresh price, guidance and valuation anchors once subsequent quarters are disclosed.
