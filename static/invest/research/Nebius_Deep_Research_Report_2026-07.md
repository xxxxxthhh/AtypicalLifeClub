# Nebius Group (NASDAQ: NBIS) Deep Research Report

Coverage date: 2026-07-01
Last updated: 2026-07-01
Ticker: NASDAQ: NBIS
Disclaimer: This report is for informational and research purposes only. It does not constitute investment advice. Please conduct your own due diligence. All prices and market caps are point-in-time snapshots; financial figures are per company disclosure unless noted otherwise.

> **Background & framing note:** Nebius is an AI "neocloud" — like CoreWeave, it builds and rents NVIDIA-GPU compute to AI labs and hyperscalers. It is the Amsterdam-headquartered, NASDAQ-listed successor to the former **Yandex N.V.**, which sold its Russian businesses in 2024, kept the international AI-infrastructure engineering base and a large cash pile, and renamed itself Nebius Group. This report is **initial coverage**, and its job in this center's AI-infrastructure book is specific: it is the **cross-check ("architecture check") on [CoreWeave](/invest/research/reports/view.html?id=coreweave-2026), the layer's bear-led risk anchor.** CoreWeave asks whether the AI buildout is real demand or leverage-and-circularity. Nebius is the natural control group — a neocloud that funds the same GPU buildout with **cash, customer prepayments, convertibles and equity instead of GPU-collateralized term debt**, is **operating-cash-flow positive**, and carries a portfolio of non-cloud assets. The question this report answers is therefore not "is Nebius cheap" (it is not) but: **does CoreWeave's fragility come from the neocloud *model* — or only from CoreWeave's *balance sheet*?**

---

## Executive Summary

**One-line thesis:** Nebius is the "clean" neocloud — hyper-growth (Q1 2026 revenue **+684%**, AI-cloud ARR **$1.92B** exiting Q1), **positive** adjusted EBITDA and **$2.3B of operating cash flow**, funded by ~**$9.3B of cash**, customer prepayments and convertibles rather than CoreWeave-style GPU-collateralized leverage — but it is priced for perfection (~**17-19x** EV/2026E revenue), its GAAP profit is an accounting artifact of a non-cash ClickHouse mark, and it is quietly accumulating the **same** hyperscaler concentration (Microsoft + Meta) and **same** NVIDIA circularity it is supposed to be the diversified answer to.

**Verdict:** **High-quality-but-high-expectations / high-risk (watch).** This is *not* written bear-led like CoreWeave — Nebius is a genuinely stronger balance sheet and a more integrated, more optionality-rich business. But "stronger than the risk anchor" is not "safe": at ~$60-66B the market already awards Nebius roughly **3x CoreWeave's revenue multiple**, so the entire quality premium — self-funding, vertical integration, ClickHouse/Toloka optionality, Nasdaq-100 membership — is in the price, and the execution bar (a **$20-25B** 2026 capex ramp against $3.0-3.4B of revenue) is extreme. Own it, if at all, as a high-beta long on the AI buildout — and read it against CoreWeave as the tell for whether neocloud risk is *financial* or *fundamental*.

**Current market read (latest snapshot, 2026-07-01):** NBIS ~**$240** (a volatile, high-beta name; it printed ~**$256** and ~**$66B** market cap around its June-22 Nasdaq-100 inclusion, and is up roughly **+165-185% YTD**). On ~**252M** shares (≈253.9M issued), market cap is ~**$61B** at ~$240 (~$60-66B across late-June/early-July). The Q1 2026 balance sheet shows ~**$9.3B cash** against ~**$8.4B** of non-current debt — of which ~$4.34B is convertible notes and ~$2.0B is a prefunded-warrant instrument (quasi-equity, associated with NVIDIA's $2B strategic investment) — leaving Nebius roughly **net-cash-neutral to ~$5B net cash** depending on treatment, and an enterprise value of roughly **$56-61B**, i.e., at or just below market cap. This is the polar opposite of CoreWeave's ~$23-33B net-obligation stack. Sources: [Nebius Q1 2026 press release (SEC 6-K)](https://www.sec.gov/Archives/edgar/data/0001513845/000110465926064092/nbis-20260331xex99d2.htm); quote references: [Yahoo Finance NBIS](https://finance.yahoo.com/quote/NBIS/), [StockAnalysis NBIS](https://stockanalysis.com/stocks/nbis/), [Macrotrends NBIS market cap](https://www.macrotrends.net/stocks/charts/NBIS/nebius-group/market-cap).

**Key data:**

| Metric | Value |
|--------|-------|
| Price (2026-07-01) | ~$240 (high-beta; ~$256 near June-22 Nasdaq-100 inclusion; ~+165-185% YTD) |
| Market cap / EV | ~$61B / ~$56-61B EV (~252M shares; ~$60-66B cap across late-June/early-July) |
| Net cash | ~$9.3B cash vs ~$8.4B non-current debt → roughly net-cash-neutral to ~$5B net cash (treatment-dependent) |
| Q1 2026 revenue | $399.0M (+684% Y/Y); Nebius AI Cloud $389.7M (+841%, 98% of total) |
| Q1 2026 GAAP net income | +$621.2M — **but** driven by a $780.6M non-cash investment revaluation gain (ClickHouse); operating result was a **−$128.0M loss** |
| Q1 2026 adj EBITDA | $129.5M (32% group margin; Nebius AI Cloud margin 45%) — first positive quarter |
| Core AI Cloud ARR (exit Q1) | $1.92B (+674% Y/Y, +54% Q/Q); exited 2025 at ~$1.25B |
| Operating cash flow | +$2,258M (driven largely by customer prepayments) |
| Q1 2026 capex | $2,472.9M |
| FY2026 guidance | revenue $3.0-3.4B; exit ARR $7-9B; group adj EBITDA margin ~40%; **capex $20-25B** (raised from $16-20B) |
| Contracted power | ~3.5 GW now, targeting >4 GW by year-end; >75% owned |
| Anchor contracts | Microsoft up to ~$17.4B (up to ~$19.4B) to 2031; Meta up to ~$27B ($12B dedicated + up to $15B, from early 2027) + prior $3B |
| NVIDIA ties (circularity) | supplier + shareholder ($2B strategic investment, Mar 2026) + Vera Rubin early access |
| Non-core assets / optionality | ClickHouse stake (~$15B round); Toloka (deconsolidated Q2 2025, equity stake); Avride (AV); TripleTen (edtech) |
| CEO / founder | Arkady Volozh (Yandex founder); dual-class (A/B) |

---

## 1. Business Overview

Nebius operates a **full-stack AI cloud**: it designs and integrates its own server/rack hardware and cloud software, houses NVIDIA accelerators (H100/H200/GB200/Blackwell, with Vera Rubin coming for Meta), and rents the compute under multi-year contracts to AI labs, hyperscalers, and enterprises. Unlike CoreWeave's asset-light, lease-and-SPV model, Nebius leans **owned/vertically-integrated**: management says **>75% of contracted power is owned capacity**, and the engineering DNA comes from Yandex's cloud/infrastructure organization.

- **Revenue:** Q1 2026 $399.0M (**+684% Y/Y** from $50.9M). The **Nebius AI Cloud** segment is $389.7M (+841%), **98% of group revenue** — this is, functionally, a pure-play GPU-cloud company with a few non-core satellites.
- **Run-rate (ARR):** core AI-cloud ARR exited Q1 at **$1.92B** (+54% Q/Q, from ~$1.25B at end-2025). Management guides **exit-2026 ARR to $7-9B** — a ~4-5x step that depends on the Microsoft/Meta capacity ramping on schedule.
- **Profitability:** adjusted EBITDA turned **positive at $129.5M** (32% group margin; the AI-cloud segment margin was 45%, up from ~24% in Q4). This is the single sharpest contrast with a typical loss-making neocloud narrative — Nebius already covers cash operating costs.
- **Cash generation:** operating cash flow was **+$2.26B** in Q1, mostly **customer prepayments** on the new mega-contracts. That prepay dynamic is a genuine funding advantage — customers are pre-financing the buildout — but it is front-loaded and should not be read as steady-state FCF.
- **Non-core assets:** Avride (autonomous vehicles — fleet doubled YTD, robot deliveries +178% to 174,000+), TripleTen (edtech, +10% Y/Y), the deconsolidated **Toloka** stake (AI data labeling), and a stake in **ClickHouse** (database company) that management intends, over time, to find "strategic and financial partners" for. These are small today but real optionality.

**Segment mix (Q1 2026):**

| Segment | Q1 2026 revenue | Y/Y | Note |
|---------|-----------------|-----|------|
| Nebius AI Cloud | $389.7M | +841% | 98% of group; 45% adj EBITDA margin; ARR $1.92B |
| Avride | (small) | — | Autonomous vehicles; deliveries +178% Y/Y |
| TripleTen | (small) | +10% | Edtech |
| Toloka | equity stake | — | Deconsolidated Q2 2025 (AI data labeling) |
| ClickHouse | equity stake | — | Revalued at ~$15B round → $780.6M non-cash gain |

---

## 2. Industry & Competitive Position

### 2.1 The neocloud model, funded two different ways

Neoclouds (CoreWeave, Nebius, Crusoe, Lambda, Nscale) exist because AI labs needed NVIDIA capacity faster than hyperscalers could provision it, and NVIDIA wanted distribution beyond the big three clouds. The demand is the same; the **financing** is where CoreWeave and Nebius diverge, and that divergence is the whole reason to cover both:

| Dimension | CoreWeave (risk anchor) | Nebius (this report) |
|-----------|-------------------------|----------------------|
| Balance sheet | ~$25B debt + ~$10B op leases; ~$23-33B net obligations | ~$9.3B cash vs ~$8.4B non-current debt; ~net-cash to ~$5B net cash |
| GAAP result (latest Q) | −$740M net loss | −$128M operating loss (net income +$621M on a non-cash mark) |
| Adj EBITDA | +$1.2B (56%) | +$129.5M (32% group; 45% cloud) |
| Operating cash flow | negative / capex-consuming | **+$2.3B** (prepayment-aided) |
| Funding of capex | GPU-collateralized SPV term loans (DDTLs) | cash + prepayments + convertibles + ABS + ATM |
| Capex vs revenue (2026E) | ~3x | ~**7x** ($20-25B vs $3.0-3.4B) |
| Integration | asset-light, leased/partner sites | vertically integrated, >75% owned power |
| Optionality | none | ClickHouse, Toloka, Avride, TripleTen |

The read-through: Nebius shows that a neocloud **can** scale on a clean balance sheet — so CoreWeave's solvency risk is at least partly a **CoreWeave financing choice**, not an inherent property of the model. But note the sting in the tail: Nebius's **capex-to-revenue is even higher** than CoreWeave's, so the "self-funded" claim is only as durable as continued access to prepayments, convertibles, and asset-backed financing.

### 2.2 Concentration & circularity — Nebius is not immune

The tempting story is "CoreWeave = concentrated & circular, Nebius = diversified & clean." The data only half-supports it:

- **Concentration is rising, not falling.** Nebius's growth is now anchored by two hyperscalers: **Microsoft** (up to ~$17.4B, up to ~$19.4B, to 2031, out of the Vineland NJ site) and **Meta** (up to ~**$27B** — $12B dedicated Vera Rubin capacity from early 2027 plus up to $15B additional — on top of a prior $3B). Combined, that is ~**$46B** of signed hyperscaler commitments. As these ramp through 2027, Nebius is acquiring precisely the **customer-concentration** profile that makes CoreWeave fragile. Management stresses it is "intentional about pairing these key strategic relationships with a diversified core" — a claim to verify, not assume.
- **The NVIDIA circularity is identical.** NVIDIA is Nebius's **supplier + shareholder** ($2B strategic investment, March 2026) — the exact supplier-shareholder overlap flagged as a circularity risk at CoreWeave. So NVIDIA-ecosystem circularity is a **sector feature**, not a CoreWeave idiosyncrasy — an important cross-check finding for the whole book.

### 2.3 What Nebius actually has that CoreWeave does not

- **Vertical integration & owned power** (>75%), giving more control over cost, performance, and deployment speed, and less exposure to third-party landlords.
- **Engineering heritage** from Yandex — a rare, genuinely deep infra/cloud org outside the hyperscalers.
- **Optionality** — the ClickHouse stake alone was marked up by $780.6M in one quarter; Toloka, Avride, and TripleTen are monetizable.
- **Balance-sheet flexibility** — cash + prepayments + converts + an untapped ATM (up to 25M Class A shares) mean it is not hostage to the GPU-debt market the way CoreWeave is.

---

## 3. Financial Health

### 3.1 P&L: hyper-growth, real operating leverage, but a flattered bottom line

| Metric | Q1 2026 | Q1 2025 | Change |
|--------|---------|---------|--------|
| Revenue | $399.0M | $50.9M | +684% |
| Nebius AI Cloud revenue | $389.7M | — | +841% |
| Adj EBITDA | +$129.5M | −$53.7M | turned positive |
| Loss from operations | −$128.0M | — | still operating-loss-making |
| Net income (continuing ops) | +$621.2M | — | non-cash-mark driven |
| Operating cash flow | +$2,258M | −$198M | prepayment swing |
| Capex | $2,472.9M | — | ~ARR-scale in one quarter |

Two things must be held together. First, the **operating leverage is real**: adjusted EBITDA swung from −$53.7M to +$129.5M and the AI-cloud margin nearly doubled Q/Q to 45%. Second, the **GAAP net income of $621.2M is not earnings** — it is overwhelmingly a **$780.6M non-cash gain on the revaluation of equity investments** (chiefly the ClickHouse stake after a funding round at roughly a $15B valuation). Strip the mark and Nebius still posted a **−$128M operating loss**. Anyone citing "Nebius is profitable" without that caveat is misreading the print.

### 3.2 Balance sheet: the clean-neocloud case, with honest caveats

- **Cash ~$9.3B** at March 31, 2026, after a Q1 that added a **$4.34B convertible-notes** placement (a $2.59B 1.25% tranche due 2031 and a $1.75B 2.625% tranche due 2033) and a **$2.0B prefunded-warrant instrument** (quasi-equity, associated with NVIDIA's $2B investment). Non-current debt is ~**$8.4B**.
- **Net position:** treating only the convertibles as debt, Nebius is ~**$5B net cash**; treating the entire ~$8.4B non-current balance as debt, it is ~net-cash-neutral (~$0.9B net cash). Either way it is **nothing like CoreWeave's ~$23-33B net-obligation stack** — there is no GPU-collateralized SPV term-loan tower here, and no "revenue and collateral fail together" knot.
- **Capex funding:** management says **>90% of the projected 2026 capex range is already secured by cash and contractual commitments**, with additional asset-backed financing expected against the Meta and Microsoft contracts and an untapped ATM as backup. That is a materially safer funding stack than CoreWeave's — but $20-25B is still an enormous, largely irreversible bet, and the prepayment tailwind that produced $2.3B of Q1 operating cash flow is front-loaded.

### 3.3 Red-flag check

| Flag | Reading |
|------|---------|
| GAAP earnings quality | **Amber** — net income flattered by a large non-cash investment mark; watch operating income ex-marks. |
| Leverage | **Green** — near-net-cash; converts are low-coupon and long-dated. |
| Customer concentration | **Amber & worsening** — Microsoft + Meta dominate the forward ramp. |
| Related-party / circularity | **Amber** — NVIDIA is supplier + shareholder (same flag as CoreWeave). |
| Dilution | **Amber** — convertibles + up to 25M-share ATM + dual-class structure. |
| Capex intensity | **Amber** — ~7x revenue; self-funding claim depends on markets staying open. |
| Cash generation | **Green (with caveat)** — +$2.3B operating cash flow, but prepayment-driven. |

---

## 4. Management & Governance

**Founder/CEO Arkady Volozh** built Yandex into one of the few non-US, non-Chinese full-stack internet/cloud companies, then — after the 2022 invasion of Ukraine and subsequent sanctions pressure — engineered the 2024 sale of Yandex's Russian operations, retaining the international AI-infrastructure business, its engineering talent, and a large cash balance that seeded the Nebius pivot. Observations:

- **Track record & technical depth:** genuinely rare — this is an operator who has built hyperscale infrastructure before, which is exactly what a neocloud arms race rewards.
- **Capital allocation:** disciplined on the balance sheet relative to peers (equity/convertible/prepay funding over GPU-collateralized debt), but **aggressive on M&A** — Tavily, Eigen AI, and Clarifai were all acquired in 2026 to build inference/agentic capability. Integration risk is real.
- **Governance flags:** **dual-class** (Class A/B) concentrates control with the founder; the multi-asset structure (cloud + Avride + TripleTen + ClickHouse/Toloka stakes) is complex and can obscure the core; and the **Yandex heritage**, while legally resolved, is a lingering perception/geopolitical overhang.
- **Disclosure:** the reliance on adjusted EBITDA and the large non-cash investment mark in GAAP net income put the burden on investors to look through to operating income and cash flow.

**Management grade: B+** (exceptional infrastructure pedigree and a smarter funding strategy than the peer risk anchor; marked down for M&A pace, structural complexity, and dual-class control).

---

## 5. Bull Case

**Core thesis (steel-manned — "what must be true"):** AI-compute demand is real and supply-constrained; Nebius can scale into $7-9B exit ARR (and beyond) **without** CoreWeave-style leverage, because it is operating-cash-flow positive, self-funds capex from cash/prepayments/convertibles, owns its capacity, and has blue-chip contracted demand plus monetizable optionality.

1. **Self-funded hyper-growth.** +684% revenue, positive adjusted EBITDA, +$2.3B operating cash flow, ~$9.3B cash, and >90% of 2026 capex pre-secured — growth without a solvency question.
2. **Blue-chip contracted demand.** ~$46B of Microsoft + Meta commitments (Meta on NVIDIA Vera Rubin from early 2027), plus "4+ customers competing for every GPU" in the core cloud.
3. **Vertical integration & owned power** (>75%) → cost/performance/deployment edge and less landlord dependence than asset-light peers.
4. **Optionality worth real money.** ClickHouse (marked up $780.6M in a quarter), Toloka, Avride, TripleTen — none of which CoreWeave has.
5. **NVIDIA alignment + index tailwind.** $2B NVIDIA investment and Vera Rubin early access; **Nasdaq-100 inclusion (June 22, 2026)** adds passive demand and legitimacy.

**Illustrative upside:** if exit-2026 ARR lands at the high end ($9B) and the market keeps paying a premium multiple for the cleanest scaled neocloud, the equity re-rates well above the late-June ~$256 highs.

## 6. Bear Case

**Core thesis (steel-manned):** Nebius is a superb business priced for flawless execution — the entire quality premium is in a ~17-19x forward-revenue multiple, its GAAP "profit" is a non-cash mark, and it is taking on the very concentration and circularity that make its own risk-anchor peer fragile, while betting $20-25B/yr that the buildout continues.

1. **Valuation leaves no margin for error.** ~17-19x EV/2026E revenue and ~7x EV/exit-ARR — roughly **3x CoreWeave's revenue multiple**. Any ramp slip, margin wobble, or AI-capex digestion de-rates a richly-priced stock hard.
2. **The profit is optics.** $621M net income is a $780.6M ClickHouse mark; the operating line is still **−$128M**. If the ClickHouse/AI-private-valuation cycle turns, the marks reverse.
3. **Concentration is converging toward the risk anchor.** As Microsoft + Meta ramp through 2027, Nebius inherits CoreWeave-style top-customer dependence — the opposite of the "diversified alternative" framing.
4. **Same NVIDIA circularity.** Supplier + shareholder overlap means Nebius's "demand" is also partly ecosystem-sponsored.
5. **Capex intensity is extreme and market-dependent.** $20-25B vs $3-3.4B revenue (~7x); the self-funding story needs prepayments, convertibles, and ABS markets to all stay open — a capital-markets air-pocket hits Nebius's ramp too.
6. **Dilution & complexity.** Convertibles, an up-to-25M-share ATM, dual-class control, aggressive M&A, and a sprawling multi-site/multi-asset footprint to integrate.

**Illustrative downside:** an AI-capex digestion scare plus a reversal of private-market marks could compress both the multiple and sentiment 40-60% from the highs, even with the balance sheet intact.

---

## 7. Key Uncertainties

Framed as the **cross-checks on CoreWeave** — what Nebius tells us about whether neocloud risk is financial or fundamental:

1. **Model vs balance sheet (the core cross-check).** If **both** Nebius (net cash) and CoreWeave (levered) keep converting backlog/ARR at high utilization, demand is real and CoreWeave's risk was mostly its *balance sheet*. If **Nebius's** utilization or pricing also cracks, the problem is *sector demand*, and the whole AI-infra long book should de-risk. *Watch:* ARR conversion, utilization, and rental pricing at both names.
2. **Concentration convergence.** Does Nebius's Microsoft+Meta revenue share climb toward CoreWeave's >60% single-customer profile as the mega-deals ramp in 2027? *Watch:* customer-concentration disclosures.
3. **Earnings quality.** How much of future "profit" is operating vs non-cash investment marks? *Watch:* operating income turning sustainably positive **ex-marks**; any reversal of the ClickHouse valuation.
4. **Funding durability.** Does the ">90% secured" 2026 capex claim survive a tighter capital market? *Watch:* ABS issuance against Microsoft/Meta, ATM usage, convertible terms, prepayment cadence.
5. **Optionality — crystallized or distraction?** Do Toloka/Avride/TripleTen/ClickHouse get monetized (proving hidden value) or absorb management attention? *Watch:* partner/stake-sale announcements.

**Thesis-breaking (either direction):** a Microsoft or Meta commitment cut, a private-market-mark reversal, or a funding stumble would each independently validate the bear; conversely, high-utilization ARR conversion with operating profit ex-marks and diversified demand would confirm Nebius as the durable, self-funding neocloud — and, by cross-check, reassure the whole book.

---

## 8. Valuation Context

> This is valuation "context," not a price target or a buy/sell recommendation. For a hyper-growth, near-net-cash name, the trailing multiple is meaningless; the operative lens is forward revenue/ARR against execution risk.

- **Forward multiples:** on ~$56-61B EV, Nebius trades at ~**17-19x** 2026E revenue ($3.0-3.4B) and ~**7-7.5x** exit-2026 ARR ($7-9B). Trailing P/S is not meaningful given +684% growth.
- **Quality premium, quantified.** CoreWeave trades at ~6x EV/2026E revenue **with** ~$23-33B of net obligations; Nebius at ~17-19x **with** near-net-cash. The market is paying roughly **3x the revenue multiple** for the cleaner balance sheet, positive cash generation, vertical integration, and optionality. That premium is rational in direction and demanding in size — it prices Nebius as *the* winning independent neocloud.
- **Optionality is partly free.** The ClickHouse/Toloka/Avride/TripleTen stakes carry value not captured in a cloud-only multiple (the ClickHouse mark alone was $780.6M in Q1) — a modest offset to the headline multiple.
- **Reading it:** Nebius is priced as the quality compounder of the neocloud group — which means the risk is not solvency (as at CoreWeave) but **expectations**. It works if the $7-9B ARR ramp and 40% group margins arrive on schedule; it de-rates sharply on any ramp/margin/AI-capex disappointment.

**Multi-method framing:**

| Method | Value / range | Key assumption | Confidence |
|--------|---------------|----------------|------------|
| EV / 2026E revenue | ~17-19x | Revenue $3.0-3.4B delivered | Medium |
| EV / exit-2026 ARR | ~7-7.5x | Exit ARR $7-9B on schedule | Medium |
| Balance-sheet floor | near-net-cash | Cash $9.3B vs ~$8.4B non-current debt | High |
| Sum-of-parts optionality | + non-core stakes | ClickHouse/Toloka/Avride/TripleTen monetized | Low |

**Scenario framing (illustrative, not a forecast):**
- **Bull (~30%):** ARR ramps to the high end, margins hit ~40%, marks hold; the premium multiple persists or expands and the equity re-rates above the ~$256 June highs.
- **Base (~45%):** strong growth but the stock churns as it grows into a rich multiple, hostage to AI-capex sentiment and quarterly ramp cadence.
- **Bear (~25%):** AI-capex digestion and/or a private-mark reversal compress multiple and sentiment 40-60% from the highs, balance sheet intact.

---

## 9. Catalysts & Monitoring Checklist

**Near-term (0-6 months):**
- Q2 2026 results (~Aug 2026): ARR and utilization, **operating income ex-marks**, Microsoft/Meta ramp cadence, capex funding mix, any ClickHouse mark changes.
- Nasdaq-100 passive flows post June-22 inclusion; any asset-backed financing (ABS) issuance against the Microsoft/Meta contracts; ATM usage.
- Customer-concentration and prepayment disclosures.

**Medium-term (6-18 months):**
- Meta **Vera Rubin** dedicated capacity starting early 2027; Pennsylvania (250-300 MW live by end-2027), Alabama, and Missouri sites coming online.
- Concentration trend as mega-deals ramp; progress toward sustained operating profit ex-marks.
- Any monetization of Toloka/Avride/TripleTen/ClickHouse stakes.

**Long-term (18+ months):**
- Whether independent neoclouds stay essential or are bypassed by hyperscaler self-build.
- The GPU credit/residual cycle (read across from CoreWeave).
- Path to durable GAAP operating profitability and genuine free cash flow after the capex peak.

**Metrics to monitor continuously:** ARR and utilization, operating income ex-marks, customer concentration, capex vs operating cash flow, cash and net-cash position, convertible/ATM dilution, prepayment cadence, and — as the cross-check — the same metrics at CoreWeave.

---

## 10. Conclusion

Nebius is the **control group** for this center's neocloud thesis. Where CoreWeave is a bear-led solvency test, Nebius is the demonstration that a neocloud **can** scale on a clean balance sheet: +684% revenue, positive adjusted EBITDA, +$2.3B operating cash flow, ~$9.3B cash, near-net-cash, vertical integration, and real optionality. That materially changes the read on the layer — **CoreWeave's fragility is at least partly a financing choice, not an inherent property of the model.**

But the cross-check cuts both ways, and this is the part a bull skips: Nebius is priced for perfection (~17-19x forward revenue, ~3x CoreWeave's multiple), its GAAP profit is a non-cash ClickHouse mark over a −$128M operating loss, its capex intensity is *higher* than CoreWeave's (~7x revenue), and it is accumulating the **same** hyperscaler concentration and the **same** NVIDIA supplier-shareholder circularity it is supposed to be the diversified answer to. So the risks the neocloud layer exists to test — real-vs-financed demand, concentration, circularity, AI-capex durability — are **shared**; only the *balance-sheet* fragility is CoreWeave-specific.

**Our posture is high-quality-but-high-expectations / high-risk (watch).** Nebius is the stronger business and the better-funded neocloud, and it earns a place in the book as the layer's **architecture check** on CoreWeave. But "better than the risk anchor" is a low bar for a stock priced as the category winner. Own it, if at all, as a small, high-beta, consciously-sized long on the AI buildout — and use the **pair** (Nebius clean + CoreWeave levered) as the single most useful tell in the whole center: if both keep converting demand, the buildout is real; if the *clean* one cracks too, the problem was never leverage — it was the demand.

---

## Appendix: Sources & Assumptions

**Primary & company sources:**
- [Nebius Q1 2026 press release / 6-K (SEC EX-99.2)](https://www.sec.gov/Archives/edgar/data/0001513845/000110465926064092/nbis-20260331xex99d2.htm) — quarter ended March 31, 2026, reported May 13, 2026 (revenue, AI-cloud revenue, adj EBITDA, operating loss, net income, investment-revaluation gain, cash, debt, convertibles, prefunded warrants, operating cash flow, capex, ARR, guidance)
- [Nebius Q1 2026 results (company newsroom)](https://nebius.com/newsroom/nebius-reports-first-quarter-2026-financial-results) — results announcement, 1.2 GW Pennsylvania site, shareholder letter
- [Nebius (NBIS) Q1 2026 earnings call transcript (Motley Fool)](https://www.fool.com/earnings/call-transcripts/2026/05/13/nebius-nbis-q1-2026-earnings-transcript/) — segment status (Toloka/Avride/TripleTen non-core), ClickHouse mark, concentration commentary, >90%-secured capex, data-center footprint, guidance cadence
- [Nebius–Microsoft AI infrastructure agreement](https://www.rcrwireless.com/20250910/ai-infrastructure/nebius-microsoft-ai) — up to ~$17.4B (up to ~$19.4B) to 2031, Vineland NJ (announced Sept 2025)
- [Meta–Nebius up to $27B agreement (CNBC)](https://www.cnbc.com/2026/03/16/meta-nebius-ai-infrastructure.html) and [Nebius newsroom](https://nebius.com/newsroom/nebius-signs-new-ai-infrastructure-agreement-with-meta) — $12B dedicated Vera Rubin capacity from early 2027 + up to $15B additional; prior $3B (Dec 2025)
- Quote/valuation references: [Yahoo Finance NBIS](https://finance.yahoo.com/quote/NBIS/), [StockAnalysis NBIS](https://stockanalysis.com/stocks/nbis/), [Macrotrends NBIS market cap](https://www.macrotrends.net/stocks/charts/NBIS/nebius-group/market-cap)

**Key assumptions & basis:**
- Price ~$240 = latest available 2026-07-01 quote; a high-beta name that printed ~$256 and ~$66B market cap around its June-22, 2026 Nasdaq-100 inclusion and is up roughly +165-185% YTD. Market cap ~$61B at ~$240 on ~252M shares (≈253.9M issued at Mar 31, 2026; verify against the latest 20-F/6-K — dual-class A/B, and convertibles/ATM are dilutive). Actual quoted price may differ intraday.
- Balance sheet (Mar 31, 2026): cash and equivalents ~$9,298M; non-current debt ~$8,432M, including a $4,337.5M convertible-notes placement ($2.59B 1.25% due 2031 + $1.75B 2.625% due 2033) and a ~$2,000M prefunded-warrant instrument (quasi-equity, associated with NVIDIA's $2B March-2026 strategic investment). Net position ranges from ~net-cash-neutral (~$0.9B net cash treating all non-current debt as debt) to ~$5B net cash (treating only convertibles as debt); EV ~$56-61B. Recompute against the filed statements.
- Q1 2026 (quarter ended Mar 31, 2026, reported May 13): revenue $399.0M (+684%), Nebius AI Cloud $389.7M (+841%), adjusted EBITDA +$129.5M (32% group; 45% cloud), **loss from operations −$128.0M**, net income from continuing operations +$621.2M driven by a **$780.6M non-cash gain on revaluation of equity investments** (chiefly ClickHouse), operating cash flow +$2,258M (prepayment-aided), capex $2,472.9M, core AI-cloud ARR $1.92B exiting Q1. "Adjusted EBITDA" excludes D&A, SBC and one-offs; the operating loss and cash flow are the conservative caliber.
- FY2026 guidance: revenue $3.0-3.4B, exit ARR $7-9B, group adjusted EBITDA margin ~40%, capex $20-25B (raised from $16-20B); contracted power ~3.5 GW targeting >4 GW by year-end, >75% owned; >90% of 2026 capex said to be secured by cash and contractual commitments — per company/CNBC/transcript.
- Contract figures (Microsoft up to ~$17.4B/$19.4B; Meta up to ~$27B + prior $3B; NVIDIA $2B investment) are multi-year ceilings/commitments, not booked revenue.
- This report is **initial coverage** and framed as the **cross-check ("architecture check") on the CoreWeave risk anchor**. Refresh price, ARR/utilization, operating income ex-marks, concentration, capex funding, and non-core marks at the next quarterly result.
