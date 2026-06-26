# Broadcom (AVGO) Deep Research Report

Coverage date: 2026-06-26
Last updated: 2026-06-26
Ticker: NASDAQ: AVGO
Disclaimer: This report is for informational and research purposes only. It does not constitute investment advice. Please conduct your own due diligence.

> **Fiscal-year note:** Broadcom's fiscal year ends in early November. In this report **FY2025** is the year ended 2025-11-02; **Q2 FY2026** is the quarter ended ~2026-05-03 (reported 2026-06-03), the latest quarter as of publication. Broadcom figures always use the company's official fiscal labels. Read alongside this center's NVIDIA and AMD reports — together they form the full picture of AI compute silicon.

---

## Executive Summary

**One-line thesis:** Broadcom is the biggest pick-and-shovel of the "custom AI silicon" counter-movement to NVIDIA's general-purpose GPUs — it designs the custom accelerators (XPUs) for hyperscalers, i.e. the very "deepest structural threat" named in the NVIDIA report — while also owning an underappreciated VMware software cash machine. Q2 FY2026 AI semiconductor revenue was $10.8B (+143%), and management has set an **FY2027 AI revenue target above $100B**. But that target is highly dependent on a handful of hyperscaler customers and is clearly back-end-loaded to FY2027, and the valuation already pays a non-trivial price for the dream.

**Verdict:** **Neutral / high quality but high expectations (watch).** Consistent with this center's stance on NVIDIA, AMD and SK hynix. Broadcom's moat (custom-ASIC design IP + networking + software stickiness) is real, and the two-engine model (AI silicon growth + VMware cash) is strong; but the core tension is that a **$1.8T market cap already prices in a >$100B AI number that is back-end-loaded to FY2027 and tied to a small set of publicly reported customer programs** — like NVIDIA, the risk is not the multiple itself but the denominator (AI capex and custom-silicon order conversion).

**Current market read (as of 2026-06-25):** AVGO last traded around **$378.91**; on ~**4.74B** shares, market cap is ~**$1.80T**. Forward P/E is ~**33x**, between NVIDIA (~25x) and AMD (~58x). Sell-side targets are sentiment inputs only, not valuation anchors for this report. Quote sources: [StockAnalysis AVGO](https://stockanalysis.com/stocks/avgo/), [Yahoo Finance AVGO](https://finance.yahoo.com/quote/AVGO/); financial source: [Broadcom Q2 FY2026 press release](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-second-quarter-fiscal-year-2026-financial).

**Key data:**

| Metric | Value |
|--------|-------|
| Price (2026-06-25) | ~$378.91 |
| Market cap | ~$1.80T (~4.74B shares) |
| Forward P/E | ~33x (vs NVIDIA ~25x, AMD ~58x) |
| EV/TTM Sales | ~24-25x (TTM revenue ~$75B) |
| Q2 FY2026 revenue | $22.19B (+48% YoY) |
| Semiconductor Solutions | $15.01B (+79% YoY) |
| Infrastructure Software (VMware, etc.) | $7.18B (+9% YoY) |
| AI semiconductor revenue | $10.8B (+143% YoY) |
| AI bookings backlog | >$30B |
| Gross margin (GAAP / non-GAAP) | 69.4% / 77.1% |
| Operating margin (GAAP / non-GAAP) | 48.6% / 67.3% |
| Adjusted EBITDA | $15.24B (69% of revenue) |
| Free cash flow | $10.26B (46% of revenue) |
| Total debt | $64.9B (mainly the VMware acquisition) |
| Cash / net debt | $19.63B / ~$45B (Q2 FY2026 quarter-end) |
| EPS (GAAP / non-GAAP) | $1.91 / $2.44 |
| Q3 FY2026 guidance | revenue ~$29.4B (+84% YoY); AI semi $16.0B (+200% YoY) |
| FY2026 AI semi guidance | ~$56B (~+180%) |
| FY2027 AI semi target | >$100B |
| Custom XPU customers / programs | Public reports include Google, Meta, ByteDance, Anthropic, OpenAI and Fujitsu; the $73B backlog is a market estimate, not all official confirmed orders |
| FY2025 revenue | $63.89B (+24% YoY) |

---

## 1. Business Overview

Broadcom is a dual-engine "semiconductors + infrastructure software" company built by Hock Tan through a string of large acquisitions (LSI, Broadcom, CA, Symantec Enterprise, VMware). The model's core is to **acquire moaty, cash-generative assets, cut peripheral lines, raise prices, and expand margins**.

**Two segments:**

- **Semiconductor Solutions (Q2 FY2026 revenue $15.01B, +79% YoY):** three pieces — (1) **AI accelerators (XPUs):** custom AI ASICs designed for hyperscalers; (2) **AI networking:** Ethernet switching (Tomahawk/Jericho), optics, and interconnect — the "plumbing" of AI clusters; (3) **non-AI semis:** broadband, wireless (incl. Apple RF), enterprise storage — more cyclical. AI semis were $10.8B (+143%) this quarter, ~72% of semiconductor revenue.
- **Infrastructure Software (revenue $7.18B, +9% YoY):** centered on VMware (virtualization/private cloud), plus CA and Symantec. This is a **high-margin, sticky, cash-rich** subscription machine that funds debt repayment (from VMware) and dividends.

**The business model:** on the AI side, Broadcom does not sell a general chip; it sells the **design capability + IP + advanced packaging/networking to make a chip cheaper and more power-efficient than buying NVIDIA**. Customers (hyperscalers) bring the volume and workload profile; Broadcom brings design and supply chain. That makes Broadcom the natural hedge to NVIDIA's general-purpose GPU — the more hyperscalers want to reduce NVIDIA dependence, the more they need Broadcom.

**Full-year FY2025:** revenue $63.89B (+24% YoY). FY2026 is accelerating sharply on AI (H1 already $41.5B, Q3 guided to $29.4B).

## 2. Industry & Competitive Position

### 2.1 The moat: custom-ASIC design IP + advanced packaging/networking + software stickiness

Broadcom's edge in custom AI silicon is not "making chips" but "doing the hard part hyperscalers can't do without":

1. **Design IP and advanced packaging/SerDes:** high-speed SerDes, chiplet/2.5D packaging, HBM integration — the hardest parts of a custom large chip, where Broadcom has an industry-leading IP library and tape-out record.
2. **Networking (the plumbing of AI clusters):** Tomahawk/Jericho Ethernet switching + optical interconnect, a direct beneficiary of the "Ethernet replaces InfiniBand" trend — its head-on competition with NVIDIA networking, positioned on the open-ecosystem side.
3. **Software stickiness (VMware):** the private-cloud foundation of nearly every large enterprise, with very high switching costs and stable cash.

### 2.2 It is the hedge to NVIDIA — and sits directly on NVIDIA's share

AI compute silicon competition reduces to "general GPUs (NVIDIA/AMD) vs custom ASICs (Broadcom/Marvell)":

- **For relatively fixed inference workloads**, hyperscalers are strongly motivated to replace general GPUs with cheaper, more power-efficient in-house XPUs. Broadcom is the main enabler of that path.
- The **FY2027 AI >$100B target** rests on a small set of hyperscaler programs and a publicly reported **$73B backlog** estimate: Google (TPU), Meta (MTIA), ByteDance, Anthropic, OpenAI, Fujitsu and others. Per public estimates, just Anthropic (~3GW+ in 2027), OpenAI (~1GW), Meta (2GW+) and Google (3GW+) total 9-10GW of 2027 commitments. Treat this as a market-breakdown / media-reporting input; some orders are not yet official Broadcom-confirmed disclosures.

### 2.3 But the custom-silicon business has its own structural weaknesses

- **Extreme customer concentration:** AI revenue is concentrated in a few hyperscalers, historically in just 2-3. Any large customer's program slip, switch, or in-sourcing causes meaningful volatility.
- **Program-based, lumpy revenue:** ASICs are won "by program/generation," without CUDA-style software lock-in. A customer's next generation could go to a different design partner (Marvell, Alchip) or an in-house team.
- **Not zero-sum with NVIDIA:** many customers buy both NVIDIA GPUs (training) and Broadcom XPUs (inference) heavily. Broadcom's share depends on the "build vs buy" balance, which is itself affected by NVIDIA's TCO/efficiency progress.

## 3. Financial Health

### 3.1 Q2 FY2026: across-the-board records on AI

- Total revenue **$22.19B** (+48% YoY); semiconductors $15.01B (+79%), software $7.18B (+9%).
- AI semis **$10.8B** (+143%), AI bookings backlog **>$30B** — strong visibility.
- Non-GAAP gross margin **77.1%**, operating margin **67.3%**, adjusted EBITDA $15.24B (69% of revenue) — a top-tier margin structure for large-cap tech.
- Q3 FY2026 guidance: revenue ~$29.4B (+84% YoY), AI semis $16.0B (+200% YoY).

### 3.2 Cash is huge, but the VMware debt is the other half you must consolidate

- Free cash flow **$10.26B** (46% of revenue) — extremely strong cash generation.
- But **total debt is $64.9B** (mainly the ~$69B VMware acquisition in 2023). So Broadcom is two stories at once: high AI-semiconductor growth, and a deleveraging project funded by VMware cash + price increases. Interest and debt size are not ignorable in valuation.
- The company pays a steady dividend and retains buyback capacity, but current capital-allocation priority is balancing **AI investment + debt repayment + dividend**.

### 3.3 GAAP vs non-GAAP difference is mainly acquisition amortization

Q2 FY2026 non-GAAP EPS ($2.44) exceeds GAAP ($1.91), driven mainly by **intangible amortization and restructuring** from VMware and prior deals (the norm for Broadcom's M&A model). For Broadcom's earnings, **non-GAAP + free cash flow** reflects true operating power better than GAAP — but remember these adjustments are long-lived and sizeable, not purely one-time.

## 4. Management & Governance

CEO **Hock Tan** is one of the most successful M&A integrators in semiconductor history: a disciplined "acquire — streamline — raise prices — deleverage" cycle has made Broadcom a margin machine with an excellent capital-allocation and cash-return record. His early positioning in custom AI silicon (winning Google's TPU years ago) validates strategic foresight.

**Governance and points to monitor:**

- **M&A dependence and integration controversy:** aggressive VMware price/bundle increases lifted software margins sharply but drew customer pushback and churn risk — the long-run "margin vs customer relationship" tension.
- **Capital allocation:** balancing AI investment, debt repayment and dividends under high leverage is the core question for the next few years.
- **Key-person dependence:** strategy is tightly bound to Hock Tan; succession is a long-term tail consideration.

**Management grade: A (outstanding capital allocation and M&A integration + AI strategic foresight); customer-relationship risk from aggressive integration to be monitored.**

## 5. Bull Case

**Core thesis:** Broadcom is the "higher-certainty pick-and-shovel" of AI capex — it benefits from hyperscalers building their own chips (the counter-movement to NVIDIA) and has VMware cash underneath.

1. **AI semis accelerating beyond expectations.** Q2 +143%, Q3 guide $16B (+200%), FY2026 AI ~$56B, FY2027 >$100B, with publicly reported customer programs and a $73B backlog estimate supporting visibility; the customer/GW/order details still need quarterly reconciliation to official disclosure.
2. **Two engines that hedge each other.** AI silicon provides growth; VMware software provides high-margin cash to deleverage/pay dividends — steadier than a pure-cyclical semi.
3. **Structurally positioned on the "open ecosystem."** Broadcom is on the beneficiary side of both "Ethernet replaces InfiniBand" and "in-house replaces general GPU."
4. **Top-tier margins and cash.** Non-GAAP operating margin 67%, FCF 46% of revenue.
5. **Valuation not extreme relative to AI growth.** ~33x forward, below AMD (~58x), above NVIDIA (~25x); if FY2027 >$100B delivers, the multiple is supported.

## 6. Bear Case

**Core thesis:** the valuation already prices in an AI dream that is back-end-loaded to FY2027 and tied to a few customers; any order slip or customer loss is amplified.

1. **Revenue is heavily back-end-loaded + customer-concentrated.** >$100B is a **FY2027** number; OpenAI XPUs ship in 2027, Anthropic scales in 2027. The price pays for programs not yet delivered; any large customer's slip/switch hits expectations hard.
2. **ASICs have no CUDA-style lock-in.** Custom silicon is a program business; a customer's next generation could go to a different design partner or an in-house team (some hyperscalers are expanding internal chip teams).
3. **$64.9B of debt.** In a higher-rate environment, debt is a real financial constraint and risk; deleveraging consumes cash.
4. **VMware price-hike backlash.** Aggressive pricing lifts software margins short-term but could accelerate mid-term churn to open-source alternatives (Proxmox, Nutanix); software growth (+9%) already looks muted.
5. **Systemic risk shared with NVIDIA.** If AI capex peaks or ROI disappoints, Broadcom as a custom-silicon supplier is also a high-beta link; error tolerance at a $1.8T base is limited.

## 7. Key Uncertainties

1. **Conversion of the FY2027 >$100B AI target.** What share of backlog converts to revenue, and when? Do OpenAI/Anthropic XPUs ramp on schedule? When we'll know more: quarterly AI-semi revenue and backlog disclosure.
2. **Customer concentration and the "build" balance.** Will hyperscalers internalize more design (in-house teams) or keep outsourcing to Broadcom? How much do rivals like Marvell take?
3. **VMware customer retention.** After aggressive price hikes, what does the enterprise renewal/churn curve look like? Can the software segment hold its cash quality?
4. **Deleveraging pace.** The repayment speed of $64.9B of debt and the rate environment, and the impact on EPS and capital allocation.
5. **The AI capex cycle (shared with NVIDIA).** Can hyperscaler capex be supported by real ROI?

**Thesis-breaking events:**
- If a **major XPU customer publicly slips or switches**, the credibility of FY2027 >$100B is badly hit and the bull thesis is damaged.
- If VMware shows a **visible wave of customer churn**, the "software cash machine" narrative weakens.
- If signs of an AI-capex peak emerge, custom silicon and general GPUs get re-rated together.

## 8. Valuation Context

> The following is valuation "context," not a price target or a buy/sell recommendation.

- **Forward P/E ~33x:** between NVIDIA (~25x) and AMD (~58x). Seen together: NVIDIA is "biggest but lowest multiple," AMD is "challenger with highest multiple," and Broadcom sits in the middle — the market awards it a "high-certainty pick-and-shovel + software cash" premium, below the pure-GPU challenger's optimistic multiple.
- **EV/TTM Sales ~24-25x:** TTM revenue ~$75B (FY2025 $63.9B + AI acceleration); EV ~$1.84-1.85T (market cap + ~$45B net debt). Note: unlike NVIDIA (net cash), Broadcom is **net-debt**, so EV is above market cap, lifting EV-based multiples.
- **Reading the multiple:** as with NVIDIA, Broadcom's valuation risk is not the multiple but the **denominator (FY2027 AI delivery)**. The difference: Broadcom's delivery is more back-end-loaded, more tied to a few customers, and carries $64.9B of debt — a notch less error-tolerant than NVIDIA.

**Scenario framing (illustrative, not a forecast):**
- **Base (~50%):** AI orders deliver broadly on schedule with some slippage, FY2027 AI approaches but does not necessarily hit $100B, VMware cash steadies deleveraging, and the multiple holds in the low-thirties — the stock tracks AI-revenue delivery.
- **Bull (~25%):** all 6 customer programs ship on time + new customers join, FY2027 AI exceeds $100B, software retention holds, and multiple and earnings rise together.
- **Bear (~25%):** a major customer slips/switches + capex peaks + VMware churn; AI expectations are cut, the market re-rates "the back-loaded dream," and with the debt constraint, multiple and earnings fall together.

## 9. Catalysts & Monitoring Checklist

**Near-term (0-6 months):**
- Q3 FY2026 results (~September 2026): whether it delivers the $29.4B / AI $16B guide and whether AI backlog keeps expanding.
- New XPU customer or large-order confirmations (e.g. formal landing of the OpenAI order).
- Hyperscaler (GOOG/META/ByteDance, etc.) capex and in-house chip roadmaps.

**Medium-term (6-18 months):**
- Updated visibility on the FY2027 >$100B AI target and backlog conversion.
- VMware customer retention and software-growth trend.
- Deleveraging progress (debt/EBITDA).

**Long-term (18+ months):**
- The share trajectory of custom ASICs vs general GPUs in AI compute.
- Broadcom's share on the networking (Ethernet-replacement) side.

**Metrics to monitor continuously:** AI-semi sequential revenue, AI backlog, customer concentration, software retention, net debt/EBITDA, non-GAAP operating margin and FCF.

## 10. Conclusion

Broadcom is the complementary pole to NVIDIA in AI compute silicon: when hyperscalers want to reduce dependence on NVIDIA's general-purpose GPUs, Broadcom is the biggest enabler — with a VMware software cash machine underneath. The moat (design IP + networking + software stickiness) is real, margins and cash generation are top-tier, and AI acceleration (Q2 +143%) is strong. **As with NVIDIA, this is not a "are the fundamentals good enough" question.**

The real tension is that a **$1.8T market cap already prices in a >$100B AI number that is back-end-loaded to FY2027, tied to six hyperscaler customers, and carried atop $64.9B of debt.** Seen together, the valuation spectrum is clear — NVIDIA largest but lowest multiple (~25x), AMD challenger with the highest (~58x), Broadcom in the middle (~33x); Broadcom's specifics are that its delivery is more back-end-loaded, its customers more concentrated, and it is net-debt.

So, consistent with this center's stance on NVIDIA, AMD and SK hynix, **we assign a neutral / high-quality-but-high-expectations (watch) view**: bullish on the long-term theme (custom silicon + AI networking + software cash) with medium conviction; neutral on near-term entry given "back-loaded delivery + customer concentration + high debt," waiting for harder signals from on-time XPU shipments and backlog conversion. This answers the "custom ASIC" coverage gap flagged by the 2026 H1 review — only by putting NVIDIA (the general-GPU leader) and Broadcom (the custom-ASIC pick-and-shovel) in one frame can the AI-compute-silicon share battle be fully assessed.

## Appendix: Sources & Assumptions

**Primary sources:**
- [Broadcom Q2 FY2026 press release](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-second-quarter-fiscal-year-2026-financial) (quarter ended ~2026-05-03, reported 2026-06-03)
- [Broadcom Q2 FY2026 8-K (SEC)](https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000051/avgo-05032026x8kxex99.htm)
- [Broadcom Q2 FY2026 earnings call transcript (Motley Fool)](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/)
- Quote & market cap: [StockAnalysis AVGO](https://stockanalysis.com/stocks/avgo/), [Yahoo Finance AVGO](https://finance.yahoo.com/quote/AVGO/), [Macrotrends market cap](https://www.macrotrends.net/stocks/charts/AVGO/broadcom/market-cap)
- Custom XPU customers & FY2027 target: public reporting and breakdowns (2026 H1, incl. Tom's Hardware, Jon Peddie)

**Key assumptions & basis:**
- Market cap estimated at ~4.74B shares × $378.91 (share count as of 2025-11-28); sources put market cap in the ~$1.79-1.87T range depending on date.
- TTM revenue ≈ FY2025 $63.89B − H1 FY2025 ~$29.96B + H1 FY2026 ($19.31B + $22.19B) ≈ ~$75B; EV adds back ~$45B net debt (total debt $64.9B − Q2 quarter-end cash of $19.63B).
- Forward P/E ~33x (Yahoo, 2026-06-24), NVIDIA ~25x, AMD ~58x reflect a mid-2026 market read and move with price and expectations.
- The 6-customer XPU list, $73B backlog and per-customer GW commitments are public-reporting estimates; some orders (e.g. the OpenAI $10B) are not officially confirmed. Reconcile to the latest results/official disclosure at the next review.
- This report is **initial coverage**; it includes no prior-cycle comparison. Refresh price, guidance and valuation anchors once subsequent quarters are disclosed.
