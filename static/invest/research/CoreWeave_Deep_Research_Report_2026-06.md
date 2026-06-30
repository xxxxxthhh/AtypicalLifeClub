# CoreWeave (CRWV) Deep Research Report

Coverage date: 2026-06-30
Last updated: 2026-06-30
Ticker: NASDAQ: CRWV
Disclaimer: This report is for informational and research purposes only. It does not constitute investment advice. Please conduct your own due diligence. All prices and market caps are point-in-time snapshots; financial figures are per company disclosure unless noted otherwise.

> **Background & framing note:** CoreWeave is an AI "neocloud" — it builds and rents NVIDIA-GPU compute to AI labs and hyperscalers. It IPO'd in March 2025. This report is **initial coverage**, and unlike the rest of this center's AI-infrastructure book it is written **bear-led, as a risk anchor**: every other report here (NVIDIA, Broadcom, Corning, GE Vernova, Bloom, SanDisk, Vertiv) is implicitly long "hyperscaler AI capex stays high." CoreWeave is where that premise is stress-tested. The central question is deliberately skeptical: **is CoreWeave's growth durable economic demand for AI compute, or a leverage-and-circularity-fueled pull-forward that breaks when capex normalizes, GPUs de-rate, or an anchor customer self-builds?** The default posture is doubt; the burden of proof is on the bull.

---

## Executive Summary

**One-line thesis (the falsification question):** CoreWeave is the cleanest test of whether the AI buildout is real economic demand or financed momentum — it pairs a colossal **$99.4B revenue backlog** and 56%-margin adjusted EBITDA with a **widening GAAP net loss (−$740M in Q1 2026)**, ~**$35B of debt**, **$31-35B of 2026 capex**, customer concentration (Microsoft ~67% of FY2025 revenue), and a supplier, **NVIDIA**, that is simultaneously its chip vendor, a shareholder, and a **$6.3B "buyer of last resort."** If that combination is durable demand, it removes a bear overhang for the whole AI chain; if it is circular and leverage-driven, CoreWeave cracks first.

**Verdict:** **High-risk / bear-leaning (avoid-to-watch); the chain's risk anchor.** This is not a "high-quality, high-expectations" name like the rest of the book — it is a high-operating-and-financial-leverage bet whose equity (~$52B market cap) sits on top of ~$33B of net debt (EV ~$89B). The market has already repriced it: the stock is ~**$96**, down ~**47%** from its 2025 highs and barely above the **$87** NVIDIA paid in January 2026. The bull case is real but narrow; the bear case is the base case.

**Current market read (latest market-data snapshot, 2026-06-29 close):** CRWV ~**$96** (down ~47% from 2025 peaks near ~$180). On ~**540M** shares, market cap ~**$52B**; with ~$35B debt and ~$2.3B cash (net debt ~**$33B**), enterprise value is ~**$89B** — i.e., **debt is ~37% of EV**, a very different risk profile from the equity-funded names elsewhere in this book. Financial source: [CoreWeave Q1 2026 8-K (SEC)](https://www.sec.gov/Archives/edgar/data/0001769628/000176962826000220/coreweave1q26earningspress.htm); quote references: [Yahoo Finance CRWV](https://finance.yahoo.com/quote/CRWV/), [StockAnalysis CRWV](https://stockanalysis.com/stocks/crwv/).

**Key data:**

| Metric | Value |
|--------|-------|
| Price (2026-06-29 close) | ~$96 (down ~47% from 2025 peak ~$180) |
| Market cap / EV | ~$52B / ~$89B (~540M shares) |
| Net debt | ~$33B (~$35B debt − ~$2.3B cash) — ~37% of EV |
| Q1 2026 revenue | $2.1B (+112% Y/Y, +32% Q/Q) |
| Q1 2026 GAAP net loss | −$740M (widened from −$315M) |
| Q1 2026 adj EBITDA | $1.2B (~56% margin) |
| Revenue backlog (RPO) | $99.4B (+~50% Q/Q); 36% in <24mo, 75% in <4yr |
| FY2026 guidance | revenue $12-13B; exit ARR $18-19B; **capex $31-35B** |
| TTM revenue / net loss | $6.23B / −$1.59B |
| Customer concentration | Microsoft ~67% of FY2025 rev (guided <50%; "no single >35%" of contracted) |
| Anchor contracts | OpenAI ~$22.4B; Meta up to ~$35.2B; + Anthropic, Google |
| NVIDIA ties (circularity) | supplier + shareholder ($2B at $87, Jan 2026) + **$6.3B capacity backstop** through Apr-2032 |
| Debt cost | interest ~$311M (Q3'25), ~$1.2B+ annualizing & rising; GPU-collateralized DDTLs (SOFR+2.25-4.0%) |
| GPU depreciation | 6-yr useful life (raised from 4-yr, Jan 2023) — contested |
| CEO | Michael Intrator (co-founder) |

---

## 1. Business Overview

CoreWeave operates a **specialized GPU cloud**: it procures NVIDIA accelerators (H100/H200/GB200-class), houses them in leased and partner data centers, and rents the compute under multi-year contracts to AI labs (OpenAI, Anthropic), hyperscalers (Microsoft), and enterprises. The model is **capital-in-advance**: CoreWeave buys/finances GPUs and builds capacity *ahead* of, and against, signed customer contracts.

- **Revenue:** Q1 2026 $2.1B (+112% Y/Y); TTM $6.23B. Growth is extraordinary, but it is **bought** — every dollar of capacity requires GPUs, power, and data-center space funded largely by debt.
- **Backlog (RPO):** $99.4B — the headline bull number. But only **36% is scheduled to convert within 24 months**, and recognized revenue ($2.1B/qtr) is a fraction of it; the backlog leads cash by years and depends on customers honoring multi-year commitments.
- **Profitability:** adjusted EBITDA $1.2B (56% margin) looks software-like — but it sits *above* the enormous depreciation (GPUs), interest (~$35B debt), and stock comp that drive a **−$740M GAAP net loss**. The gap between adjusted EBITDA and GAAP loss is the whole debate.
- **Capex:** guided **$31-35B for 2026** — roughly **3x** expected revenue. This is the defining feature: CoreWeave consumes far more cash than it generates, and the gap is funded by debt and equity.

---

## 2. Industry & Competitive Position

### 2.1 The neocloud model: real demand, financed supply

Neoclouds (CoreWeave, Nebius, Crusoe, Lambda) exist because AI labs needed NVIDIA capacity faster than hyperscalers could provision it, and NVIDIA wanted distribution outside the big three clouds. The demand is real — the four largest AI labs (OpenAI, Anthropic, Meta, Google) have all signed CoreWeave. But the *supply* is financed: GPUs are bought with GPU-collateralized debt, housed in leased space, and underwritten by the customer contracts themselves. The model works while capital is available and contracts hold; it is fragile to either breaking.

### 2.2 The circularity map (why revenue quality is the crux)

The single most important structural feature is that CoreWeave's largest backers and customers overlap:

| Counterparty | Role(s) to CoreWeave | Circularity concern |
|--------------|----------------------|---------------------|
| **NVIDIA** | GPU **supplier** + **shareholder** ($2B at $87, Jan 2026) + **$6.3B capacity backstop** (buyer of last resort to Apr-2032) | NVIDIA helps fund and de-risk the off-take of its own chips |
| **Microsoft** | ~**67%** of FY2025 revenue; also a hyperscale **competitor** building its own capacity | Demand concentrated in a customer that can self-build |
| **OpenAI** | ~$22.4B contracted; also NVIDIA-ecosystem, also diversifying (Stargate/Oracle/Broadcom) | Anchor customer is itself cash-burning and building alternatives |

NVIDIA being supplier, shareholder, *and* backstop is the textbook circularity flag: it inflates both CoreWeave's "demand" and NVIDIA's own reported demand. Management argues concentration is falling (Microsoft guided below 50%, "no single customer >35% of contracted revenue" after the Meta expansion) — but the diversification is *toward* OpenAI, itself a financed, loss-making counterparty.

### 2.3 The self-build threat

CoreWeave's anchors are also the parties most able to bypass it. **Microsoft** (its ~67% customer) is explicitly pursuing AI self-sufficiency — building in-house models (MAI-1, seven models unveiled at Build 2026) and its own Azure capacity. **OpenAI** is diversifying via Stargate (Oracle/SoftBank), custom silicon (Broadcom), and owned compute. And CoreWeave's own attempt to vertically integrate data-center capacity — the **$9B Core Scientific acquisition — was rejected by Core Scientific shareholders in October 2025**, leaving CoreWeave still dependent on leased/partner capacity. Neoclouds risk being a *bridge* that customers cross and then dismantle.

---

## 3. Financial Health

### 3.1 P&L: hyper-growth, widening losses

| Metric | Q1 2026 | Q1 2025 | Change |
|--------|---------|---------|--------|
| Revenue | $2,100M | ~$990M | +112% |
| Adj EBITDA | $1,200M | — | ~56% margin |
| GAAP net loss | −$740M | −$315M | loss widened ~2.3x |
| TTM revenue | $6.23B | — | — |
| TTM net loss | −$1.59B | — | — |
| 2026 capex (guided) | $31–35B | — | ~3x revenue |

Revenue is doubling, and adjusted EBITDA margin (56%) is genuinely high — but the **GAAP loss is widening**, because the costs that adjusted EBITDA excludes (GPU depreciation, ~$1.2B+ interest, SBC) are exactly the costs that define this business. This is the core tension: the metric the bulls cite (adj EBITDA) excludes the metrics the bears cite (D&A, interest).

### 3.2 Capital structure & GPU residual risk (the solvency question)

- **Debt ~$35B** (up from ~$14B in Q3 2025), much of it **GPU-collateralized DDTLs** (SOFR+2.25–4.0%; ~5.9% fixed on the latest) routed through **SPVs that pledge GPUs *and* customer service contracts** as collateral. As of Q3 2025, **$9.7B was due within twelve months**.
- **Interest expense ~$311M in Q3 2025** alone (~3x prior year), annualizing past **~$1.2B** and rising with the debt load — a heavy fixed charge against a GAAP-loss-making P&L.
- **GPU depreciation: 6-year useful life** (raised from 4 years in Jan 2023). Bears (notably Michael Burry) argue this understates true economic depreciation given a ~1–2-year generational cadence (Hopper→Blackwell→Rubin), flattering both earnings and the value of the GPU collateral. Bulls cite a **"value cascade"** — A100s still fully booked; expired H100s rebooked at ~95% of original price — as evidence residual value holds. This is unresolved and central: if the 6-year life is too generous, both reported profitability and collateral coverage are overstated.
- **The structural knot:** the debt is collateralized by the *same* customer contracts that drive revenue. If a key contract weakens, revenue **and** debt collateral are impaired together — the failure modes are correlated, not independent.

### 3.3 Backlog vs cash: the conversion gap

RPO of **$99.4B** is the bull's anchor, but the relevant question is conversion: only ~36% is scheduled within 24 months, recognized revenue is ~$2.1B/quarter, and converting the rest requires **~$31-35B of 2026 capex** (and more beyond) — funded by yet more debt and equity. The backlog is a promise that consumes enormous cash to fulfill; it is not cash.

---

## 4. Management & Governance

**CEO Michael Intrator** co-founded CoreWeave (pivoting from crypto mining to GPU cloud) and led it through a rapid IPO and hyper-scaling. Observations — weighted for a risk-anchor lens:

- **Execution & access to capital:** management has been extraordinarily effective at *raising and deploying capital* — signing the largest AI labs and arranging tens of billions in GPU-backed debt at improving rates. That is a genuine skill, and a risk: the franchise is built on continuous access to financing.
- **Related-party governance:** the NVIDIA relationship (supplier + shareholder + backstop) and large concentrated contracts require careful arm's-length scrutiny; investors should read related-party and contract footnotes closely.
- **Disclosure quality:** the reliance on **adjusted EBITDA** as the headline, alongside a widening GAAP loss and a 6-year GPU life, means the burden is on investors to look through to GAAP, cash, and collateral coverage.
- **Capital-allocation stakes:** committing **$31-35B of 2026 capex** against $12-13B of revenue is an aggressive, largely irreversible bet on demand staying ahead of capacity.

**Management grade: B (exceptional capital-raising and customer-acquisition execution; but the governance/related-party complexity and the leverage-forward strategy raise the risk profile rather than lower it — this is not a conservatively-run balance sheet).**

---

## 5. Bull Case

**Core thesis (steel-manned — "what must be true"):** AI compute demand is real, durable and supply-constrained; CoreWeave's $99.4B backlog from the biggest, most creditworthy AI labs is contracted cash flow that comfortably services its debt, and GPU residual value holds — so the leverage is prudent, not fragile.

1. **Backlog is contracted and blue-chip.** $99.4B from OpenAI, Meta (~$35B), Microsoft, Anthropic, Google — demand visibility no traditional infrastructure firm has.
2. **Unit economics are real.** 56% adjusted EBITDA margin; GPUs rent at high utilization; the "value cascade" keeps older chips earning (H100 rebooked at ~95%).
3. **Debt is contract-backed and de-risking.** Lenders require creditworthy customer contracts to cover repayment; DDTL spreads have tightened (SOFR+4.0%→+2.25%/~5.9%), and "GPU debt has gone investment-grade."
4. **NVIDIA is aligned.** Equity ($2B at $87), supply priority, and the $6.3B backstop are a powerful vote of confidence and a genuine downside cushion on unsold capacity.
5. **First-mover scale & speed.** CoreWeave deploys NVIDIA capacity faster than hyperscalers can self-provision; that operational edge is the moat.

## 6. Bear Case

**Core thesis (the base case):** CoreWeave is a highly-levered, customer-concentrated, circularly-financed bet whose growth is bought with ~$35B of debt and $31-35B/yr of capex, whose anchor customers can self-build, and whose GPU collateral may de-rate faster than the books assume.

1. **Demand may be financed, not purely economic.** Capex ~3x revenue, RPO converting slowly, and a supplier ($6.3B NVIDIA backstop) acting as buyer of last resort — a chunk of "demand" is supplier-funded off-take of NVIDIA's own chips.
2. **Revenue quality is impaired by concentration + circularity.** Microsoft ~67%; NVIDIA is supplier+shareholder+backstop; diversification is *toward* OpenAI, itself loss-making and financed.
3. **The balance sheet is the real story.** Net debt ~$33B (~37% of EV), ~$1.2B+ and rising interest, $9.7B due within a year (as of Q3'25), GPU-collateralized debt whose collateral and revenue fail together. This is a **solvency-sensitive** structure, not just a growth stock.
4. **GPU residual value is an accounting choice.** A 6-year depreciation life against a ~1-2-year generational cadence flatters earnings and collateral; if it normalizes, profitability and coverage deteriorate.
5. **Self-build hollows the anchors.** Microsoft (MAI models, Azure) and OpenAI (Stargate/Oracle/Broadcom) are building around CoreWeave; the failed Core Scientific deal leaves it lease-dependent. Neocloud pricing/utilization can crack first.

---

## 7. Key Uncertainties

Framed as the **four kill-criteria** — the observable that would confirm the bear (and, by extension, flash a warning for the whole AI-infra book):

1. **Real demand vs financing (Pillar 1).** If recognized revenue keeps lagging RPO and a material share of bookings is supplier-backstopped/single-customer, demand is financing-shaped. *Watch:* recognized-revenue-to-RPO conversion; the NVIDIA backstop drawdown.
2. **Revenue quality / circularity (Pillar 2).** If top-2 customers stay >~2/3 of revenue and NVIDIA remains a contracted demand backstop, revenue quality is impaired. *Watch:* customer concentration %, related-party disclosures.
3. **Solvency under GPU-life stress (Pillar 3).** If 24-month debt-service + lease/purchase commitments exceed contracted+liquid cash under a "GPU life = 3 years" stress, the structure is fragile. *Watch:* maturities, interest coverage, depreciation policy, liquidity runway.
4. **Self-build / pricing crack (Pillar 4).** If a top customer publicly cuts commitment or GPU rental ASPs fall with slipping utilization, pricing power breaks. *Watch:* Microsoft/OpenAI capacity commentary, rental ASP & utilization.

**Thesis-breaking (either direction):** a single anchor-customer renegotiation, a debt-covenant or refinancing stumble, or a step-down in GPU residual value would each independently validate the bear; conversely, sustained diversification with self-funding cash flow would refute it and de-risk the whole book.

---

## 8. Valuation Context

> The following is valuation "context," not a price target or a buy/sell recommendation. For a solvency-sensitive, loss-making name, **the balance sheet matters more than the multiple.**

- **The market has already de-rated it.** At ~$96 the stock is down ~47% from 2025 peaks and barely above NVIDIA's $87 January entry — the bear case is **partly priced in**, which cuts both ways (less froth, but the risks are now consensus).
- **EV/revenue ~7x (2026E) / EV/exit-ARR ~4.8x:** EV ~$89B on $12-13B 2026E revenue (exit ARR $18-19B). Not extreme *if* growth and solvency hold — but the multiple is the wrong lens.
- **Adjusted vs GAAP:** EV/adj-EBITDA ~18x (on ~$5B annualized) looks reasonable; but GAAP is loss-making (−$1.59B TTM) and interest (~$1.2B+) plus GPU depreciation are real cash/collateral facts that adjusted EBITDA omits.
- **Reading it:** CoreWeave is priced as an option on AI-capex *continuing* — equity (~$52B) is the thin slice above ~$33B of net debt. If demand and refinancing hold, the equity compounds; if either wobbles, the leverage works violently in reverse. This is a **levered call on the AI buildout**, appropriate only as a small, high-risk, deliberately-sized position — and most useful here as the book's **risk thermometer**, not a core long.

**Scenario framing (illustrative, not a forecast):**
- **Bear / base (~45%):** AI-capex digestion or a customer/refi stumble pressures utilization and the financing flywheel; the levered equity falls 40-70%.
- **Muddle (~35%):** demand holds but losses/interest persist; the stock churns as it grows into the debt, hostage to capital-market access.
- **Bull (~20%):** demand stays supply-constrained, diversification + self-funding arrive, GPU value holds; the equity re-rates sharply — and, importantly, **de-risks the entire AI-infra long book**.

---

## 9. Catalysts & Monitoring Checklist

**Near-term (0-6 months):**
- Q2 2026 results (~Aug 2026): recognized revenue vs RPO, **customer concentration**, interest expense, net loss, liquidity.
- Any debt issuance/refinancing and its **rate** (the cost-of-capital is the lifeline).
- Anchor-customer commentary (Microsoft self-build, OpenAI diversification).

**Medium-term (6-18 months):**
- RPO-to-revenue conversion and capex funding mix (debt vs equity).
- GPU depreciation policy and any residual-value/utilization disclosure.
- Concentration trend as OpenAI/Meta ramp; NVIDIA backstop usage.

**Long-term (18+ months):**
- Whether neoclouds remain essential or are bypassed by hyperscaler self-build.
- The GPU credit cycle — does "GPU-backed debt" survive a demand air-pocket?
- Path (if any) to GAAP profitability and self-funding.

**Metrics to monitor continuously:** recognized-revenue/RPO conversion, customer concentration, net debt & maturities, interest coverage, GPU depreciation/residual, rental ASP & utilization, capex vs operating cash flow, refinancing rate.

---

## 10. Conclusion

CoreWeave is the most important *negative-space* read in this center's AI-infrastructure book. Its $99.4B backlog and 56% adjusted-EBITDA margin are the bull's evidence that AI-compute demand is vast and contracted; its widening GAAP loss, ~$35B of debt, $31-35B of annual capex, ~67% Microsoft concentration, and the NVIDIA supplier-shareholder-backstop triangle are the bear's evidence that the growth is bought and circular. Both readings cannot be fully true, which is exactly why it is the chain's risk anchor.

**Our posture is bear-leaning and deliberate.** This is not a "high-quality, high-expectations" franchise like Vertiv or Corning; it is a solvency-sensitive, highly-levered option on AI-capex continuing, where the equity is a thin slice above ~$33B of net debt and the failure modes (customer, collateral, refinancing) are correlated. The market has already removed much of the froth (the stock is ~$96, ~47% off its highs), so this is less a "short it now" call than a **standing warning instrument**: watch CoreWeave's recognized-revenue conversion, concentration, interest coverage, and GPU residual value as the **earliest, highest-beta signals** of whether the entire AI buildout is real economic demand or financed momentum.

Read against the rest of the book: if CoreWeave's four kill-criteria stay green, it *removes* a bear overhang from NVIDIA, Broadcom, Corning, GE Vernova, Bloom, SanDisk and Vertiv; if they turn red, CoreWeave is where the crack appears first. **We assign a high-risk / bear-leaning (avoid-to-watch) view** — own it, if at all, only as a small, consciously-sized, high-volatility position, and use it primarily as the dashboard's risk gauge.

---

## Appendix: Sources & Assumptions

**Primary sources:**
- [CoreWeave Q1 2026 results 8-K / press release (SEC)](https://www.sec.gov/Archives/edgar/data/0001769628/000176962826000220/coreweave1q26earningspress.htm) — quarter ended March 31, 2026, reported May 7, 2026 (revenue, net loss, adj EBITDA, RPO, guidance)
- [CoreWeave Q1 2026 earnings (CNBC)](https://www.cnbc.com/2026/05/07/coreweave-crwv-q1-earnings-report-2026.html) — $2.1B revenue, $99.4B backlog, capex guide
- [NVIDIA $6.3B capacity backstop (Motley Fool)](https://www.fool.com/investing/2025/10/05/coreweave-nvidia-6-3-billion-backstop-explained/) — buyer of last resort for unsold capacity to Apr-2032; signed 2023, disclosed Sept 2025
- [CoreWeave–OpenAI expansion to up to $22.4B (CoreWeave IR)](https://investors.coreweave.com/news/news-details/2025/CoreWeave-Expands-Agreement-with-OpenAI-by-up-to-6-5B/default.aspx)
- [Core Scientific $9B acquisition rejected (DCD / reporting)](https://www.datacenterdynamics.com/en/news/ai-cloud-firm-coreweave-to-acquire-core-scientific-for-9bn/) — rejected by Core Scientific shareholders, Oct 2025
- GPU depreciation debate: [CNBC](https://www.cnbc.com/2025/11/14/ai-gpu-depreciation-coreweave-nvidia-michael-burry.html); debt structure: [Forbes "GPU Debt Has Gone Investment Grade"](https://www.forbes.com/sites/daraabasiita/2026/06/09/gpu-debt-has-gone-investment-grade-heres-who-holds-the-risk/)
- Quote/valuation references: [Yahoo Finance CRWV](https://finance.yahoo.com/quote/CRWV/), [StockAnalysis CRWV](https://stockanalysis.com/stocks/crwv/)

**Key assumptions & basis:**
- Price ~$96 = 2026-06-29 close (down ~47% from 2025 peaks near ~$180; NVIDIA invested $2B at $87 in Jan 2026). Market cap ~$52B on ~540M shares (share count approximate — verify against the latest 10-Q; multiple share classes). Actual quoted price may differ intraday.
- Net debt ~$33B = ~$35B total debt − ~$2.3B cash → EV ~$89B (per StockAnalysis; includes finance leases — reconcile term loans vs leases vs operating-lease commitments at the next 10-Q).
- Q1 2026 (quarter ended Mar 31, 2026, reported May 7): revenue $2.1B (+112%), GAAP net loss −$740M, adj EBITDA $1.2B (56%), RPO $99.4B; FY2026 guide revenue $12-13B, exit ARR $18-19B, capex $31-35B — per the May 7 8-K. "Adjusted EBITDA" excludes depreciation, interest, stock comp and other items; the GAAP loss is the conservative caliber.
- Customer/contract figures (Microsoft ~67% FY2025; OpenAI ~$22.4B; Meta up to ~$35.2B; NVIDIA $6.3B backstop, $2B equity) are per company disclosures and press; contract values are multi-year ceilings/commitments, not booked revenue.
- Debt detail (≈$14B Q3'25 → ~$35B; $9.7B due <12mo as of Q3'25; interest ~$311M in Q3'25; DDTL SOFR+2.25-4.0%; SPV/GPU collateral) and the 6-year GPU depreciation life are per reporting/filings; recompute coverage and maturities against the latest 10-Q.
- This report is **initial coverage** and **bear-led by design** (the portfolio's risk anchor). Refresh price, RPO conversion, concentration, debt/interest, and GPU-residual disclosures at the next quarterly result.
