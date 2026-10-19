# Cerebras Systems (CBRS) Deep Research Report

Coverage date: 2026-10-19
Last updated: 2026-10-19
Ticker: NASDAQ: CBRS
Disclaimer: This report is for informational and research purposes only. It does not constitute investment advice. Please conduct your own due diligence.

---

## Executive summary <!-- report-module:overview -->

**One-line thesis:** Cerebras has turned inference speed from its wafer-scale engine (WSE) into a sellable differentiation, and through a 750MW take-or-pay contract with OpenAI it is converting itself from a chip company selling systems into an inference cloud that owns compute and charges for capacity. At the **$127.21 regular-session close on 2026-10-16**, however, **34.11x EV/TTM GAAP revenue and 26.23x EV/the midpoint of the company's FY2026 core revenue guidance** require the $25.4B of remaining performance obligations (RPO) to convert on schedule and a customer base of similar scale to be built beyond OpenAI, while the company is still burning cash, still reports material weaknesses and is still working through a staged lock-up release.

**Current stance: cautious / low conviction.** Three-year bull/base/bear weights of 20%/50%/30% give 2029-10-19 per-share values of $289.67/$121.57/$25.70; the weighted terminal value is $126.43, or **-0.20%** annualized, below this report's 10% risk-adjusted hurdle and the 8% reference. The probability-weighted individual annualized returns equal **-6.83%**. Single favorable sensitivities (exit multiples +1x, revenue +20%, or weights of 30/50/20) give +5.52%/+5.50%/+6.30%, all below the hurdle. Conviction is low because the company has only two quarters of public reporting, has not yet filed its first post-IPO 10-K, and has RPO concentrated in a contract that can be partly terminated for missed delivery; both tails of the distribution are fat, at +127.7% in the bull case and -79.8% in the bear case.

**Key catalysts and window:** about 19.4M shares unlock on 2026-10-28; the lock-up ends entirely on the earlier of the second trading day after Q3 results or 2026-11-09; the Q3 results date had **not been announced** as of the report date. Over the next 6-18 months, test the Q4 recovery in core gross margin, tranche delivery of OpenAI capacity, AWS Bedrock (company-stated Q1 2027) and other hyperscalers (company-stated first revenue in mid-2027). The research role is an **architecture check** in the compute layer: it tests whether SRAM-based wafer-scale inference can win independent, durable, non-single-customer adoption in a compute layer dominated by GPUs and HBM.

| Key data | Current anchor and basis |
|---|---|
| Share price | $127.21, US regular-session close on 2026-10-16, the lowest close since listing; IPO price $185.00, first-day close $311.07 |
| Issued common shares / market cap | 237.564041M shares (A 112.247109M + B 111.601424M + N 13.715508M), 10-Q cover dated 2026-08-05; implies $30.221B, not a claimed October share count |
| Unrestricted cash + investments | $7.922B at 2026-06-30; a further $0.685B of restricted cash is limited to the OpenAI build-out |
| Adjusted net cash / EV | $7.003B / $23.217B; unrestricted cash and investments less the $0.918B OpenAI working capital loan, excluding restricted cash; leases and not-yet-commenced data-center leases listed separately |
| TTM revenue (to 2026-06-30) | GAAP $680.673M; company core basis $708.374M (adds back customer-warrant amortization, removes pass-through) |
| FY2026 company guidance | Core revenue $880M-$890M, core gross margin 41%-43%, core operating margin -19% to -17% (raised on 2026-08-12) |
| TTM cash flow | CFO $66.305M, capex $746.518M, FCF -$680.213M; Q2 alone FCF -$476.726M |
| RPO | $25.4B; about 22% within 24 months (to 2028-06-30), 43% in months 25-48; "a significant amount" attributable to the OpenAI MRA |
| Customer concentration | Q2 MBZUAI 34%, G42 9% (related parties of each other); OpenAI MRA revenue $56.8M, about 31.5% of Q2 GAAP revenue |
| Valuation | 34.11x EV/TTM GAAP revenue, 32.78x EV/TTM core revenue, 26.23x EV/FY2026 core guidance midpoint, 0.91x EV/RPO |
| Potential dilution | 76.0M anti-dilutive securities at 6/30 (unvested OpenAI warrant 23.4M, AWS warrant 2.7M, options 23.8M, RSUs 16.5M, PRSUs 9.0M); fully diluted proxy about 313.0M, +31.8% over issued shares |

Sources: [Q2 10-Q](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm), [Q2 results release](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056186/cbrsannouncesfinancialresu.htm), [Q1 10-Q](https://www.sec.gov/Archives/edgar/data/2021728/000162828026044981/cbrs-20260331.htm), [424B4 prospectus](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm), [CBRS price history](https://stockanalysis.com/stocks/cbrs/history/). All model forecasts are this report's assumptions, not company guidance or market consensus. TTM is computed as FY2025 + H1 2026 - H1 2025 and cross-foots line by line to the four quarters Q3 2025-Q2 2026.

## 1. Business overview and segment economics <!-- report-module:business -->

Cerebras is a fabless compute company: TSMC manufactures whole 5nm wafers, ASE deposits the redistribution layers, and final wafer packaging, assembly and test take place in Sunnyvale. The core is the WSE-3, a single 46,225mm² piece of silicon with 4 trillion transistors, 900,000 cores, 44GB of on-chip SRAM and 21PB/s of on-chip bandwidth. It does not depend on HBM or CoWoS, which the company presents as a supply advantage. Economically, the company historically sold CS-2/CS-3 systems to a few large customers; from 2026, revenue is shifting toward self-built or leased data centers selling inference as "Dedicated Capacity" (take-or-pay) and on-demand tokens. [424B4 Business](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm)

| Product / economic unit | Engineering position and verifiable scope | Commercial evidence and limits | Investment implication |
|---|---|---|---|
| WSE-3 / CS-3 systems | Whole-wafer single chip; on-chip SRAM instead of HBM; one reporting segment | FY2025 hardware revenue $358.4M; Q2 2026 hardware $54.1M after a $28.0M customer-warrant reduction | Point-in-time recognition, few customers, large tickets, volatile quarters |
| CS-4 (first Nexus platform system) | Launched 2026-08-18; three new WSEs, rack-scale; company claims up to 2x CS-3 speed and 10x throughput per watt | Company says first shipments begin that quarter; CS-5 planned for 2H 2027 | Generational change also brings old-generation inventory charges: $11.8M in Q2, $19.2M in H1 |
| Cerebras Cloud (dedicated + on-demand) | Own systems deployed in colocation/leased sites in California, Oklahoma, Canada and elsewhere | Q2 cloud and other services revenue $126.0M, +281% YoY | Shifting from selling equipment to owning assets moves capex, lease and utilization risk onto the company |
| OpenAI MRA | 750MW committed capacity in tranches over 2026-2028, each 3-4 years extendable to 5; option for 1.25GW more (up to 2GW by end-2030) | Q2 revenue $56.8M, H1 $74.4M (net of $2.5M/$3.3M warrant amortization); Q1 release valued the deal at "more than $20 billion" | High visibility, but the contract carries delivery-milestone and SLA termination rights, exclusivity, an approximately $1.0B customer loan and a 33.4M-share warrant |
| AWS commercial agreement | Global hardware leasing agreement signed June 2026 for deployment in AWS data centers; Trainium3 prefill + CS-3 decode | Not commenced and no revenue at 6/30; value not disclosed; AWS received a 2.7M-share warrant at $100 | Entry point for a second hyperscaler, including a minimum manufacturing-capacity guarantee from Cerebras to AWS |
| Partnerships and channels | AWS Marketplace, Microsoft Marketplace, IBM watsonx Model Gateway, OpenRouter, Hugging Face; AMD Helios disaggregated inference (company-stated production in Q4 2026) | Channel and partnership releases are not disclosed revenue | Evidence of broader adoption only, not valued separately |

Product basis: [424B4](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm), [CS-4 launch](https://www.cerebras.ai/press-release/cerebras-unveils-cs-4-up-to-30-times-faster-than-gpu-based-solutions-3347356), [AMD partnership](https://www.cerebras.ai/press-release/amd-and-cerebras-announce-industry-leading-ultra-low-latency-and-high-throughput-ai-inference). Speed and power multiples are issuer statements, not independent tests by this report.

| Auditable revenue structure, $M | FY2024 | FY2025 | H1 2026 | Q2 2026 |
|---|---:|---:|---:|---:|
| Hardware | 211.965 | 358.440 | 164.712 | 54.119 |
| Cloud and other services | 78.287 | 151.551 | 208.804 | 125.991 |
| GAAP total revenue | 290.252 | 509.991 | 373.516 | 180.110 |
| Less: pass-through revenue | — | — | -18.614 | -14.503 |
| Add: customer-warrant amortization (revenue reduction) | — | — | 46.315 | 44.262 |
| Company core revenue | — | — | 401.217 | 209.869 |
| GAAP gross margin | 42.3% | 39.0% | 29.9% | 14.2% |
| Core gross margin | — | — | 43.4% | 40.6% |

Sources: [424B4 financial statements](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm), [Q2 10-Q income statement and Note 3](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm), [Q2 reconciliation](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056186/cbrsannouncesfinancialresu.htm). 2025 had no warrant amortization or pass-through, so core and GAAP revenue match. FY2023 revenue was $78.7M; FY2024 grew about +269% and FY2025 +75.7%.

**Two accounting conventions determine the readings.** First, customer warrants are recorded as an asset at grant-date fair value and amortized against revenue over the contract: the balance was $1.128B at 6/30 (current portion $167.8M, about 24.6% of TTM GAAP revenue), amortizing through October 2031, and the asset will grow as the remaining 23.4M OpenAI shares vest with delivery. GAAP revenue is therefore depressed by design, and "more than triple revenue in 2027" is the CEO's statement about **core** revenue. Second, data-center rent, power and similar pass-through costs under the OpenAI contract are recognized gross, with nearly equal cost, inflating GAAP revenue without contributing gross profit; the core basis removes them. This report uses GAAP as the primary valuation basis and core as a labeled sensitivity.

| RPO reading | Balance | Recognized within 24 months | Months 25-48 | Source |
|---|---:|---|---|---|
| 2025-12-31 | $24.6B | About 15% (to 2027-12-31) | 43% | 424B4 Note 5 |
| 2026-03-31 | $25.0B | About 16% (to 2028-03-31) | 45% | Q1 10-Q Note 3 |
| 2026-06-30 | $25.4B | About 22% (to 2028-06-30), about $5.6B | 43%, about $10.9B | Q2 10-Q Note 3 |

RPO includes deferred revenue and future billings; "a significant amount" is attributable to OpenAI, but the OpenAI-only amount is not disclosed. Pass-through is included in RPO only for committed capacity whose leases are already recognized; pass-through for the remaining committed capacity is excluded, so RPO contains zero-margin dollars and is still not all future revenue. On the Q2 call (third-party transcript), the CEO said the $25.4B **does not include** AWS or any other hyperscaler business. The 12-month recognition percentage is not disclosed.

## 2. Industry, competition and architecture check <!-- report-module:competition -->

AI inference compute is not one market. GPUs (Nvidia, AMD) use HBM plus high-bandwidth interconnect for general-purpose throughput; custom ASICs (Broadcom/Google TPU, AWS Trainium) trade platform lock-in for cost; Cerebras trades on-chip SRAM for single-stream token speed, targeting low-latency, long-output inference such as coding agents, real-time voice and "fast modes" for reasoning models. Whether the speed premium is worth paying depends on whether end applications pay for lower latency and whether the gap persists as GPU and ASIC cost curves fall.

| Comparison | CBRS | GPU platforms (NVDA/AMD) | Neoclouds (CRWV/NBIS) | Constraint on the investment judgment |
|---|---|---|---|---|
| Core difference | Wafer-scale SRAM, single-stream speed; no HBM/CoWoS dependence | General ecosystem, CUDA/ROCm, HBM bandwidth and scale | Buy GPUs and rent them, earning a capital and operations spread | CBRS is both a chip company and a cloud operator and needs two moats |
| Revenue model | Cloud services lead from 2026, hardware secondary | Sell chips/systems at high margin | Lease contracts, long backlog | CBRS's 60%+ gross margin target sits between the two and must be proved |
| Latest quarterly margin | GAAP 14.2% / core 40.6% | Far higher than CBRS (not re-computed line by line here) | Asset-heavy, depreciation-driven | Core gross margin is still about 20 points below the long-term target |
| Customer structure | MBZUAI + G42 43%, OpenAI about 31.5% (Q2) | Broad | Also concentrated in a few AI labs | Concentration resembles a neocloud, not a typical chip vendor |
| Financing structure | Net cash, but the loan comes from a customer and warrants go to customers | Ample cash | CRWV net debt about $46B | CBRS's balance sheet is cleaner than CRWV's, at the cost of equity and revenue reductions |

| Same-date comparison, 2026-10-16 close | Close | Market cap | EV/TTM revenue |
|---|---:|---:|---:|
| CBRS (this report's basis) | $127.21 | $30.2B | 34.11x |
| NBIS | $165.47 | $45.4B | about 34.9x |
| CRWV | $61.39 | $33.9B | about 10.5x |
| AMD | $528.75 | $862B | about 20.6x |
| NVDA | $214.13 | $5.17T | about 17.0x |
| AVGO | $328.75 | $1.57T | about 17.9x |

Peer closes come from Nasdaq historical data; peer share counts, net debt and TTM revenue come from the [stockanalysis statistics pages](https://stockanalysis.com/stocks/crwv/statistics/) recalculated at the 10/16 close. They are derived approximations, not line-by-line filing checks by this report. CBRS and NBIS trade at similar multiples, but NBIS carries no chip R&D; CBRS is more than three times CRWV's multiple, but CRWV carries very large net debt. On the same day CRWV fell 11.9%, NBIS 12.2% and CBRS 10.5%, so the drop included sector-wide financing sentiment and cannot all be attributed to company events.

| Competitive / substitution path | Winning condition | CBRS risk and monitoring evidence |
|---|---|---|
| Nvidia low-latency inference | GPU-side inference optimization, disaggregated inference, dedicated fast modes | Media reports said an OpenAI "Ultrafast" workload moved to Nvidia (the CNBC original was not found, model names differ across sources and the company has not responded); **this report treats it as unconfirmed** and uses only actual OpenAI delivery and RPO changes as evidence |
| AMD and CBRS partnership | Helios GPUs do prefill, WSE does decode | Coopetition: if heterogeneous designs become mainstream, the WSE holds only one stage of the inference chain |
| Hyperscaler custom ASICs | Falling TPU/Trainium cost, first-party models first | The AWS agreement is both opportunity and test: if the Trainium3 + CS-3 combination does not scale, the speed premium is niche |
| Other SRAM/inference start-ups | Similar low-latency positioning at lower cost | Share is not disclosed; only new contracts and pricing readings can test it indirectly |
| Its own generational cadence | CS-4/CS-5 on time, yield and cost | Old-generation inventory charges have appeared; ramping new generations needs TSMC capacity without a long-term allocation commitment |

Observable moats are whole-wafer yield and packaging know-how, the compiler and inference software stack, more than 600MW of data-center capacity the company says is live or under contract by end-2027, and the customer endorsement of OpenAI and AWS. Unverifiable: independent market share, unit token cost at equal latency, and per-customer pricing. In the chain, this report classifies CBRS as an **architecture check** rather than a demand dashboard: it tests whether a non-GPU architecture can survive with an independent customer base, not the overall level of AI capex.

## 3. Financial health, cash quality and red flags <!-- report-module:financial -->

| Financial matrix, $M | FY2024 | FY2025 | Q1 2026 | Q2 2026 | TTM to 2026-06-30 |
|---|---:|---:|---:|---:|---:|
| GAAP revenue | 290.252 | 509.991 | 193.406 | 180.110 | 680.673 |
| YoY growth | about +269% | +75.7% | +94.4% | +74.3% | — |
| Hardware / cloud services | 211.965 / 78.287 | 358.440 / 151.551 | 110.593 / 82.813 | 54.119 / 125.991 | 383.183 / 297.490 |
| GAAP gross margin | 42.3% | 39.0% | 44.6% | 14.2% | 34.8% |
| GAAP operating loss | -101.438 | -145.862 | -15.037 | -477.233 | -552.480 |
| Core operating loss | — | -96.095 | -3.511 | -33.613 | -70.002 |
| GAAP net income / loss | -481.602 | 237.827 (incl. +363.336 one-off gain) | -14.006 | -450.528 | -512.352 |
| CFO | 451.978 | -10.050 | 12.335 | -59.823 | 66.305 |
| Capex | 23.435 | 382.739 | 131.970 | 416.903 | 746.518 |
| FCF (CFO - capex) | 428.543 | -392.789 | -119.635 | -476.726 | -680.213 |
| SBC | 58.564 | 49.767 | 9.593 | 377.008 | 413.933 |
| Customer deposits (period end) | 640.317 | 354.460 | 368.426 | 242.672 | — |
| Unrestricted cash + investments (period end) | 337.151 | 1,108.237 | 2,231.621 | 7,921.547 | — |

Sources: [424B4](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm), [Q1 10-Q](https://www.sec.gov/Archives/edgar/data/2021728/000162828026044981/cbrs-20260331.htm), [Q2 10-Q](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm). Q2 cash flows are H1 less Q1. FY2025 core operating loss is the sum of the prospectus's four quarterly non-GAAP operating losses (GAAP plus SBC); TTM core operating loss combines the prospectus basis for Q3/Q4 2025 with the company core basis for Q1/Q2 2026, a spliced calculation giving a TTM core operating margin of about -9.9%.

**FY2025 profit is not operating profit.** FY2025 GAAP net income of $237.8M came from a $363.3M non-operating gain on extinguishing the G42 forward-contract liability; the same year's operating loss was $145.9M. The forward contract arose from G42's 2024 preferred-share purchase, which after CFIUS review was moved to a non-voting structure, never closed and lapsed on 2025-04-15. FY2024's $481.6M net loss includes a $401.3M remeasurement loss on the same liability. No FY2024-to-FY2025 "turnaround" narrative based on net income is usable.

**The Q2 GAAP loss is mostly IPO one-offs, but not entirely.** Of Q2 SBC of $377.0M, about $273.6M was RSU catch-up once the IPO satisfied the liquidity condition and $34.2M was founder PRSU expense; IPO-related employer payroll tax added $22.8M. After removing these, the core operating loss was still $33.6M, a -16% core operating margin, with Q3 guided to -25% to -23% and the full year to -19% to -17%. The PRSUs have an aggregate fair value of $531.2M to be expensed over 3.4-5.9 years, and the company states that future SBC will be "significantly higher." [Q2 10-Q Note 13](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)

**Cash is flowing out, and it is flowing into assets.** H1 capex was $548.9M ($416.9M in Q2), which the company says was mainly its own systems for Cerebras Cloud; construction in progress was $604.0M at 6/30. H1 CFO was -$47.5M while customer deposits fell from $354.5M to $242.7M: the G42/MBZUAI prepayments that once supported cash are now being consumed. Unrestricted cash and investments of $7.922B at 6/30 include about $6.2B of IPO net proceeds; the $850M revolver (maturing 2031, SOFR + 2.25%, $150M minimum liquidity covenant) is undrawn. Management says liquidity covers at least the next 12 months and explicitly says it may raise equity, equity-linked or debt financing.

**Leases are the half of capital commitments that is off the balance sheet.** On-balance-sheet operating lease liabilities at 6/30 had a present value of $568.8M ($690.3M undiscounted, 5.5-year weighted remaining term, 7.2% discount rate). Off-balance-sheet disclosures of signed but not yet commenced data-center leases are: the Q1 10-Q reports $2.3B of Q1-signed leases not commenced; the Q2 10-Q reports $1.5B of Q2-signed leases not commenced and $753.4M signed after quarter end, with the MD&A combining them at about $2.3B. The Q2 10-Q does not explain what became of the Q1 $2.3B, and undiscounted on-balance-sheet rent rose only from $460.3M to $690.3M in the same period. **The two filings cannot be reconciled, and this report does not add them together.** Separately, the prospectus describes a March 2026 Canadian data-center lease with about $2.2B of minimum payments over ten years. Lease terms running longer than customer contracts are an explicit prospectus risk.

| Red-flag check | Current evidence | Judgment / to verify |
|---|---|---|
| Customer concentration | Q2 MBZUAI 34%, G42 9%, OpenAI MRA about 31.5%; two customers 76% of receivables at 6/30 | Major risk; three customers (two of them related parties) about 75% |
| Contract termination rights | OpenAI can terminate part or all for missed capacity delivery or SLA failure; the loan becomes due on termination | Delivery execution is a joint revenue and balance-sheet risk |
| Revenue quality | $1.128B warrant asset reduces revenue through 2031; pass-through recognized gross | The GAAP-core gap will persist; readings must be basis-consistent |
| Cash consumption | TTM FCF -$680.2M; Q2 -$476.7M | $7.9B cushion, but capex and lease scale depend on delivery pace |
| Internal control | Material weaknesses in FY2024 and FY2025, still present at 2026-06-30 (revenue recognition, inventory, data-center assets, equity administration, IT general controls) | Newly public, first 10-K not yet filed; no "risk-free" inference |
| Export controls | UAE customers rely on licenses; a July 2026 BIS rule (law-firm reading) lets G42/Core42 receive advanced computing items license-free if they become US companies by 2027-04-10 | Regulatory path improved but remains a variable until the condition is met |
| Supply | TSMC is the sole wafer foundry with no long-term allocation commitment; top three suppliers 13%/12%/10% in H1 | Company says it has secured wafers for growth; not a contractual guarantee |
| Litigation | October 2025 copyright class action (N.D. Cal.), no loss estimate | Not quantified for now |

## 4. Management, governance and capital allocation <!-- report-module:management -->

CEO Andrew Feldman (56) has led the company since April 2016; he previously founded SeaMicro (acquired by AMD in 2012) and was an AMD corporate vice president. Co-founder and CTO Sean Lie was AMD's chief architect; CFO Robert Komin joined in March 2024 after serving as Sunrun's CFO; COO Dhiraj Mallick joined in September 2023. The team made commercially viable a wafer-scale chip that was considered unmanufacturable for three decades and, in 2025-2026, switched the customer base from dependence on G42 to OpenAI and AWS, which is positive evidence of execution.

**Governance facts that must be stated.** The prospectus "Involvement in Certain Legal Proceedings" discloses that Feldman, in connection with improper revenue accounting at Riverstone Networks in 2001-2002, pled guilty in December 2007 to one count of circumventing an issuer's accounting controls and was sentenced to three years' probation and a $5,000 fine; in 2008 he settled with the SEC without admitting or denying, with a permanent injunction and payment of $289,507 plus interest. This happened nearly two decades ago, and this report does not infer current accounting problems from it; but alongside the company's not-yet-remediated material weaknesses, investors are entitled to ask for stronger evidence of disclosure quality. [424B4 Management](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm)

| Governance and incentive reading | Disclosure | Shareholder interpretation |
|---|---|---|
| Share structure | Class A 1 vote, Class B 20 votes, Class N non-voting; Class B held about 99.2% of votes after the IPO | Public Class A holders have almost no voting influence; the company says no single holder or group controls a majority |
| Sunset | Class B converts to A on transfer and 6 months after a founder leaves; **no time-based sunset** | The control structure can persist and may affect index inclusion |
| Board | Six members in three staggered classes; all independent except Feldman, three from Benchmark, Foundation and Eclipse | Early investors hold half the board and are distributing their stakes in tranches |
| Founder PRSUs | Feldman 5.7M and Lie 3.3M Class B shares across market-cap hurdles of $75B/$150B/$250B, measured as 90-day average price × **Class A shares only** | An incentive hurdle, not a forecast; measured on Class A shares, a given market cap requires a far higher per-share price than on the full share base |
| Founder ownership | Feldman 13G (event date 6/30) 10.397M shares, 9.2% on a Class A as-converted basis; about 4.6% of total shares on the prospectus basis | Economic exposure, but not a controlling stake |
| 2025 compensation | Feldman $11.75M, Lie $11.57M (mostly RSUs) | Grant-date accounting value, not cash |

**Insiders only sell.** Form 4s from 2026-08-14 to 10-07 show no open-market purchases (code P). Officers and a director's trust sold about 1.67M shares for about $345.9M under 10b5-1 plans: Lie 900,000 shares, about $187.4M; Mallick 396,000, about $80.8M; Feldman 275,000, about $55.2M; the Vishria trust 68,268, about $15.7M; Komin 32,500, about $6.6M. In addition, 91,364 shares were sold to cover taxes on the 8/18 RSU settlement (coded S rather than F, footnoted as non-discretionary), and the Vassallo family trust sold 100,000; all S-coded sales total about 1.86M shares and about $387.7M. Benchmark, Eclipse and Foundation distributed millions of shares in kind (J) to their limited partners, which is not selling, but those LPs become potential sellers. Plan sales do not prove motive, but "sell only, no buys" is the fact. Amounts are this report's weighted calculation from individual Form 4 transactions.

| Lock-up release (6:00 a.m. ET) | Approx. shares | Status |
|---|---:|---|
| First and second trading days (the second required a first-day close above $246.05, which was met) | about 2.5M each | Released |
| Second trading day after Q1 results | about 27.7M | Released |
| Second trading day after Q2 results (8/14) | about 36.4M | Released |
| 8/19, 9/2, 9/16 | about 14.6M each | Released |
| 9/30, 10/14 | about 19.4M each | Released |
| **10/28** | about 19.4M | Pending |
| Earlier of the second trading day after Q3 results or **11/9** | All remaining | Pending |

Source: [424B4 Shares Eligible for Future Sale](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm). The prospectus estimated about 171.1M shares released during the lock-up period. Media reports that "the lock-up expired on October 1" describe the 9/30 tranche, not full expiry.

**The central capital-allocation question is trading equity and revenue reductions for customers.** OpenAI received a 33.4M-share warrant at $0.00001 (10.03M vested and exercised, 23.4M vesting with delivery) and provided a $1.0B loan; two G42 warrants for 3.5M shares in total have been exercised; AWS received a 2.7M-share warrant at $100. At grant-date fair value, the accounting cost of these warrants already exceeds $1.1B and will reduce revenue. This prepays part of future shareholder value to customers in exchange for contracts; the return depends on whether contract gross profit covers it. IPO proceeds also funded about $416.1M of employee RSU tax withholding.

## 5. Bull case <!-- report-module:bullBear -->

**First, signed contracts give a chip start-up rare revenue visibility.** RPO of $25.4B is about 29 times the FY2026 core revenue guidance midpoint; about $5.6B is recognized before mid-2028 and about $10.9B over the following two years. OpenAI's committed capacity is take-or-pay, and the company says more than 600MW of data-center capacity is live or under contract. If delivery stays on schedule, existing RPO alone implies revenue on the order of $5B a year in 2028-2030, far above today's TTM of $0.68B.

**Second, real customers pay for the speed difference.** OpenAI publicly uses Cerebras for its "fast mode" (company release, 2026-08-13); Cognition, Lovable, CrowdStrike and others signed on with low latency as the selling point; AWS chose a Trainium3 + CS-3 combination, showing a hyperscaler willing to add the WSE for decode alongside its own chips. As inference's share of AI compute rises and coding agents and reasoning models produce longer outputs, the economic value of single-stream speed may be underestimated.

**Third, there is directional evidence of operating leverage, and the balance sheet can fund expansion.** Q2 core revenue of $209.9M beat the $194M guide by a wide margin, and the -16% core operating margin beat the -30% to -32% guide; the CFO says Q3 is the low point for core gross margin, which should improve "significantly" from Q4 as owned systems rise in the mix, with a long-term target of 60%+. $7.9B of unrestricted cash and investments, an undrawn $850M revolver and a supply chain independent of HBM/CoWoS mean the company does not need capital markets during the delivery window.

The bull case has FY2030E core revenue of $13.0B (four-year CAGR of 95.8% from the FY2026 guidance midpoint): OpenAI exercises part of its 1.25GW option, AWS and another hyperscaler ramp in 2027-2028, and CS-4/CS-5 external hardware sales recover. A 7x EV/forward revenue exit, $2.853B of adjusted net cash and 324M shares (including all unvested OpenAI warrants and the first PRSU tranche) give $289.67 per share in 2029, +127.7% versus $127.21. It needs delivery, customer expansion and the multiple to hold together, hence a 20% weight.

## 6. Bear case <!-- report-module:bullBear -->

**First, the biggest asset is also the biggest single point of failure.** OpenAI can terminate part or all of the MRA if capacity is not delivered on time or SLAs fail, and the $918M loan then becomes due; the contract also has exclusivity terms restricting service to named OpenAI competitors. Media have reported that an OpenAI fast-inference workload moved to Nvidia; this report treats that as unconfirmed, but it shows the buyer has alternatives and bargaining power. If OpenAI executes only the minimum commitment or delays tranches, the RPO schedule shifts later while the company's signed long-term leases do not.

**Second, the business model is getting heavier, and its returns are unproven.** Moving from selling systems to owning a cloud places capex, data-center leases, power costs and utilization risk on the company; TTM FCF is -$680M and Q2 core gross margin of 40.6% is far below the 60% target. Warrant amortization will reduce GAAP revenue through 2031, and pass-through dilutes gross margin. Even if revenue arrives, cash available to shareholders may lag what revenue growth implies for a long time.

**Third, pressure from share supply is not over.** About 19.4M shares unlock on 10/28 and all remaining shares are released no later than 11/9; the fully diluted proxy is about 313M, about 75M above issued shares; SBC will rise significantly; venture funds are distributing in kind and insiders keep selling. The multi-class structure and staggered board mean outside shareholders have little governance leverage over capital allocation.

**Fourth, even a growing business can suffer a large valuation compression.** The bear case has FY2030E core revenue of $3.0B, still 3.4 times the FY2026 guidance midpoint and not a business-disappears assumption; but if OpenAI partly terminates or does not renew, AWS and new customers ramp slowly and existing data centers sit partly idle, a 1.5x EV/forward revenue exit (an asset-heavy, under-utilized hosting business), $3.363B of adjusted net cash and 306M shares give $25.70 per share, -79.8% versus the current price. The bear case gets 30% rather than less because customer concentration, delivery termination rights, material weaknesses and share supply are disclosed facts, not imagination.

## 7. Key uncertainties and thesis-breaking conditions <!-- report-module:uncertainties -->

| Unknown | What we know now | Evidence needed / when to check |
|---|---|---|
| OpenAI's share of RPO and conversion pace | Only "a significant amount"; about 22% within 24 months | Quarterly RPO balance, 24-month percentage and OpenAI MRA revenue; Q3 10-Q (expected 2026-11) |
| Whether OpenAI executes only the minimum | 750MW committed, 1.25GW option; missed delivery allows termination | Tranche delivery announcements, changes in warrant vesting, loan amortization |
| Whether core gross margin can move toward 60% | Q2 40.6%, Q3 guide 38%-40%, full year 41%-43% | Whether Q4 core gross margin is at least 45%; quarterly trend in 2027 |
| True total of capex and leases | H1 capex $548.9M; not-commenced lease disclosures cannot be reconciled | Commitment table in the first 10-K; quarterly capex and new leases from Q3 |
| Whether a second large customer forms | AWS not commenced, no revenue; other hyperscalers first revenue company-stated mid-2027 | AWS commencement and revenue; new non-OpenAI contracts entering RPO |
| Internal control and first annual report quality | Material weaknesses still present at 6/30 | FY2026 10-K (expected March 2027) audit opinion and remediation status |
| UAE customers and export licenses | MBZUAI/G42 together 43% in Q2; conditional BIS easing | G42/Core42 progress toward US status before 2027-04-10; license changes |

These unknowns are large enough to change scenario weights, so low conviction means the "insufficient return" judgment is highly sensitive to two variables, OpenAI delivery and new customers, not a rejection of the company's technology. Conditions that trigger a downgrade review are: OpenAI partly terminates or lowers committed capacity, or RPO falls below $24.0B; Q3 core revenue below the $214M low end of guidance; FCF worse than -$1.0B for two consecutive quarters without new signed RPO to support it; or the fully diluted proxy above 330M. The thresholds are this report's discipline, not issuer commitments.

## 8. Valuation, reverse growth and scenario returns <!-- report-module:valuation -->

**Common price and share basis.** This report uses the 2026-10-16 regular-session close; the report date is October 19 Beijing time, before that day's US session completed. Market cap is $127.21 × 237.564041M = $30.221B. Adjusted net cash = 6/30 unrestricted cash $6.742B + investments $1.179B - OpenAI working capital loan $0.918B = $7.003B; restricted cash of $0.685B is the unspent portion of the same loan and is limited to the OpenAI build-out, so it is excluded and roughly offsets the loan. EV = $23.217B. Operating leases and not-commenced leases are not treated as financial debt. Cash is the 6/30 reading; Q3 cash consumption has not yet been disclosed, so the actual October EV is likely somewhat higher.

| Valuation method | Explicit inputs | Valuation meaning / limits |
|---|---|---|
| Current trading multiples | 34.11x EV/TTM GAAP revenue; 32.78x EV/TTM core revenue; 26.23x EV/FY2026 core guidance midpoint of $885M; market cap/book equity 3.30x | Loss-making, so only revenue multiples apply; core versus GAAP differs by about 1.3x |
| Forward scenario multiple | If 2027 core revenue is exactly 3x the FY2026 midpoint ($2.655B), EV/2027E is 8.74x | Only a mechanical conversion of management's "more than triple"; not this report's forecast |
| RPO coverage | EV/RPO 0.91x; market cap/RPO 1.19x | RPO is gross revenue, not profit, and includes zero-margin pass-through |
| Contracted cash check | RPO $25.4B × assumed post-capex cash rate of 15%-25% = $3.8B-$6.4B (undiscounted) | Existing contracts alone support only about 16%-27% of EV; the remaining roughly $17B-$19B pays for a future beyond the contracts |
| Three-year exit-multiple scenarios | FY2030E core revenue $3.0B-$13.0B, exit 1.5x-7x, shares 306M-324M | 2029 conditional per-share values $25.70-$289.67, not a price target today |

The contracted-cash check's 15%-25% is this report's assumption for revenue after delivery costs, operating expenses and the related capex, and does not contradict the company's 60%+ gross margin target: R&D, replacement of data-center equipment and warrant amortization still come after gross margin. It is not a DCF; it only shows what share of current EV is supported by signed contracts.

## 8.1 Valuation scenario grid <!-- report-module:valuation -->

Returns run from the 2026-10-19 report date to 2029-10-19, 1,096 days or 3.0007 years; exit uses FY2030E forward core revenue at that time. The 10% hurdle is this report's risk-return threshold; the extra 2 points over the 8% reference compensate for customer concentration, delivery termination rights, ongoing cash burn and dilution. The -0.20% annualized weighted terminal value is also below 8%; discounting the weighted terminal value at 8% gives a conditional entry line of $100.36, so the conclusion does not depend on the hurdle difference.

| Scenario | FY2030E core revenue / four-year CAGR | Exit EV/revenue | Exit shares / adjusted net cash | Per-share value / vs $127.21 / annualized | Weight |
|---|---|---|---|---|---|
| Bull case | $13.0B / 95.8%; OpenAI exercises part of its option, AWS and another hyperscaler ramp, hardware sales recover | 7x | 324M / $2.853B | $289.67 / +127.7% / +31.55% | 20% |
| Base case | $7.5B / 70.6%; OpenAI's 750MW delivered on time, 2027 core revenue about triples, AWS and other new customers contribute about $3B | 4.5x | 311M / $4.059B | $121.57 / -4.4% / -1.50% | 50% |
| Bear case | $3.0B / 35.7%; OpenAI partly terminates or delays, new customers ramp slowly, some data centers sit idle | 1.5x | 306M / $3.363B | $25.70 / -79.8% / -41.32% | 30% |

Four-year CAGR uses the $885M FY2026 core guidance midpoint as the base. Base-case 2030 revenue has two parts: existing RPO can recognize roughly $4B-$4.5B in 2030 (the back half of the months 25-48 bucket plus the start of the remaining 35%), plus about $3B outside RPO from AWS, other hyperscalers, on-demand and hardware. A 4.5x exit equals about 30x FCF at a mature free-cash-flow rate of about 15%, still a growth premium; the 1.5x bear multiple reflects asset-heavy, under-utilized hosting economics. The 20%/50%/30% weights are a research judgment; no objective frequency proves them.

## 8.2 Valuation cash bridge, reverse expectations and sensitivity <!-- report-module:valuation -->

| Exit share bridge, M | Bull | Base | Bear |
|---|---:|---:|---:|
| Issued at 2026-08-05 | 237.564 | 237.564 | 237.564 |
| Unvested OpenAI warrant (23.4M total, vesting with delivery/option) | 23.4 | 11.7 | 6.0 |
| Options (weighted exercise price about $5, counted in full) | 23.8 | 23.8 | 23.8 |
| Unvested RSUs | 16.5 | 16.5 | 16.5 |
| AWS warrant ($100 exercise price) | 2.7 | 2.7 | 0 |
| First founder PRSU tranche | 3.0 | 0 | 0 |
| Three years of new net grants (lower price, more shares) | 17 | 19 | 22 |
| Total (rounded) | 324 | 311 | 306 |

How the 23.4M unvested OpenAI shares split between committed capacity and the option is not disclosed; using half in the base case and about a quarter in the bear case is this report's assumption. Even so, base-case exit shares are about 31% above issued shares, and that dilution is the price of the base case's own delivery success.

| Exit cash bridge, $B | Bull | Base | Bear |
|---|---:|---:|---:|
| Starting adjusted net cash (2026-06-30) | 7.003 | 7.003 | 7.003 |
| Cumulative model-period core revenue (2026-07-01 to 2029-10-19) | 17.40 | 12.78 | 7.19 |
| Cumulative CFO rate / CFO | 25% / 4.350 | 20% / 2.556 | 5% / 0.360 |
| Cumulative capex | -8.500 | -5.500 | -3.500 |
| Lease exits, idle capacity and other | 0 | 0 | -0.500 |
| Exit adjusted net cash | 2.853 | 4.059 | 3.363 |

Model-period revenue by segment: bull 2H 2026 $0.50B / 2027 $3.2B / 2028 $6.5B / 2029 to 10/19 about 80% × $9.0B; base $0.48B / $2.7B / $4.8B / 80% × $6.0B; bear $0.45B / $2.0B / $2.5B / 80% × $2.8B. The base 2H 2026 matches the $479M-$489M H2 core revenue implied by company guidance, and base 2027 of $2.7B is about 3.05 times the FY2026 midpoint. The capex assumptions reflect owned systems and data-center fit-out, part of which OpenAI reimburses as pass-through; this report does not treat future financing as a cash source. Per-share value = (FY2030E core revenue × exit multiple + exit adjusted net cash) / exit shares; cumulative cash is added only once.

**What is priced in and the expectation gap:** holding the base 4.5x exit, 311M shares and $4.059B of net cash, FY2030E core revenue of **$7.89B** is needed to keep the stock at $127.21 in three years, a four-year CAGR of **72.8%** from the FY2026 guidance midpoint; a 10% annualized return needs **$10.80B, an 86.9% CAGR**. This report's base case of $7.5B / 70.6% sits slightly below break-even. In other words, even after a 59% decline from the first-day close, the market is still paying for "the OpenAI contract fully delivered, plus new customers of roughly AWS scale"; earning the hurdle requires customer expansion close to the bull case.

Weighted terminal value = 20% × $289.67 + 50% × $121.57 + 30% × $25.70 = **$126.43**; annualized -0.20%, with probability-weighted individual annualized returns of -6.83%, the latter reflecting the asymmetry from the depth of the bear case. Holding the scenarios fixed, the 10% hurdle corresponds to an entry price of about **$94.98**; monitoring uses $94 for rounding margin. It is a conditional observation line, not a buy instruction.

| Single sensitivity, all else fixed | Weighted terminal value | Annualized |
|---|---:|---:|
| Base weights and parameters | $126.43 | -0.20% |
| All exit multiples -1x / +1x | $103.41 / $149.45 | -6.67% / +5.52% |
| Each scenario's FY2030E revenue × 0.8 / × 1.2 | $103.46 / $149.40 | -6.65% / +5.50% |
| Bull/base/bear weights changed to 30%/50%/20% | $152.83 | +6.30% |
| Bull/base/bear weights changed to 25%/50%/25% | $139.63 | +3.15% |
| Exit net cash zero in all three scenarios | $114.84 | -3.35% |

The sensitivities hold all other variables fixed to isolate them; they are not a fully linked reforecast. Two favorable variables together (for example +1x multiples with 30/50/20 weights) can clear 10%, so "cautious" is a judgment about the current distribution, not a claim that every reasonable model loses money; low conviction reflects that such a combination is not far-fetched.

## 9. Catalysts, timeline and monitoring <!-- report-module:catalysts -->

| Catalyst / checkpoint | Timing | Testable impact |
|---|---|---|
| Lock-up tranches | About 19.4M shares on 2026-10-28; the rest no later than 2026-11-09 | Share supply; selling pace of insiders and LPs |
| Q3 2026 results and 10-Q | Quarter ended 2026-09-30; **date not announced** (third-party estimates of 11/11 or 11/19 not used) | Core revenue versus $214M-$216M guidance, core gross margin versus 38%-40%, RPO, capex, new leases |
| Q4 core gross margin recovery | Q4 2026, disclosed February-March 2027 | Company says "significantly" better; at least 45% is a positive reading |
| AMD disaggregated inference in production / first European capacity | Company-stated Q4 2026 / end-2026 | Broader adoption; not counted as revenue separately |
| FY2026 10-K | Expected March 2027 | First audited post-IPO annual report, material-weakness remediation status, full commitment table |
| AWS Bedrock general availability / first revenue from other hyperscalers | Company-stated Q1 2027 / mid-2027 | Whether a second revenue pillar forms and enters RPO |
| G42/Core42 US-status deadline | 2027-04-10 (BIS rule, law-firm reading) | Licensing path for UAE customers |
| CS-5 | Company-stated 2H 2027 | Generational cadence, old-generation inventory charges |

The five items below match the structured monitoring basis; thresholds are set by this report. Current readings are dated by filing or price as applicable.

| Monitoring ID / metric | Trigger | Latest reading | Next check |
|---|---|---|---|
| rpo-and-openai / RPO and OpenAI delivery | OpenAI partly terminates or lowers committed capacity, or RPO below $24.0B, is negative; new non-OpenAI contracts adding at least $3B to RPO are positive | 2026-06-30: RPO $25.4B; Q2 OpenAI MRA revenue $56.8M (about 31.5%); MBZUAI 34%, G42 9% | Q3 10-Q, expected 2026-11 |
| core-revenue-margin / Core revenue and gross margin | Q3 core revenue below $214M is negative; FY2026 core revenue at least $885M with Q4 core gross margin at least 45% is positive | 2026-06-30: Q2 core revenue $209.869M, core gross margin 40.6%; Q3 guide $214M-$216M, 38%-40% | Q3 results, date not announced; Q4/FY2026 |
| cash-burn-capex / Cash consumption and capex | FCF worse than -$1.0B for two consecutive quarters without new signed RPO is negative | 2026-06-30: Q2 FCF -$476.7M, H1 capex $548.9M; unrestricted cash and investments $7.922B; $850M revolver undrawn | Each 10-Q / 10-K |
| dilution-and-lockup / Dilution and lock-up | Fully diluted proxy (issued + anti-dilutive securities) above 330M is negative | 2026-08-05: issued 237.564M; anti-dilutive securities 76.0M at 6/30, proxy about 313M; about 19.4M shares unlock on 10/28, the rest no later than 11/9 | End of lock-up in 2026-11 and Q3 10-Q |
| valuation-hurdle-price / Price and return hurdle | With scenarios unchanged, a regular close at or below $94 triggers review for an upgrade to neutral-watch | 2026-10-16: $127.21; weighted terminal value $126.43, annualized -0.20%, 10% hurdle price $94.98 | Latest completed session; rebuild before relying on changed facts |

## 10. Conclusion <!-- report-module:conclusion -->

CBRS's chain task is to test whether, in a compute layer dominated by GPUs/HBM and hyperscaler ASICs, a non-GPU architecture can win independent, durable adoption not dependent on a single customer on the strength of inference speed. As of Q2 2026, the answer is "adopted by large customers, but not yet independent": about three-quarters of revenue comes from OpenAI and the related parties MBZUAI/G42, and the second hyperscaler has not commenced.

The expectation gap lies in what the price requires: at a 4.5x base exit, holding the current price needs FY2030E core revenue of $7.89B and a 10% annualized return needs $10.80B; this report's $7.5B base case already assumes OpenAI's 750MW delivered in full and on time plus about $3B of new-customer revenue, and still yields only -1.50% annualized. The fall from the $311.07 first-day close to $127.21 priced in part of the risk but did not create an adequate margin of safety.

The stance is therefore **cautious / low conviction**: the 20%/50%/30% grid gives a $126.43 weighted terminal value and -0.20% annualized, below the 10% hurdle; the best single favorable sensitivity is +6.30%, still below the hurdle; and the bear case can produce a -79.8% loss even with revenue more than tripling. The report keeps the technology and contract upside open while refusing to conflate "large contract value" with "adequate shareholder return."

**Upgrade triggers:** with scenarios unchanged, review an upgrade to neutral-watch after a regular close at or below $94; alternatively, rebuild the scenarios once all three of the following hold, and upgrade only if the rebuilt annualized return reaches 10%: FY2026 core revenue at least $885M with Q4 core gross margin at least 45%; new contracts with customers other than OpenAI and the UAE entities adding at least $3B to RPO; and a first 10-K that no longer reports material weaknesses. **Downgrade triggers:** review a downgrade to bearish-avoid if any one occurs: OpenAI partly terminates or lowers committed capacity, or RPO falls below $24.0B; Q3 core revenue below $214M; FCF worse than -$1.0B for two consecutive quarters without new signed RPO; or the fully diluted proxy above 330M. Every trigger requires the corresponding official filing and a full valuation rebuild; media reports and marketing announcements do not count as delivery.

## Appendix: sources, definitions and reproducible assumptions <!-- report-module:appendix -->

| Source | Date / scope | Use |
|---|---|---|
| [424B4 prospectus](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm) | Priced 2026-05-13, filed 05-14 | FY2024-2025 audited statements, quarterly history, business, customer history, G42/CFIUS, share structure, lock-up, management legal proceedings, compensation |
| [IPO closing 8-K](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035605/closing8-k.htm) | 2026-05-15 | 34.5M shares, greenshoe exercised in full, gross proceeds |
| [Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/2021728/000162828026044981/cbrs-20260331.htm) / [Q1 results release](https://www.sec.gov/Archives/edgar/data/2021728/000162828026044941/cbrsannouncesfinancialresu.htm) | Period ended 2026-03-31; 06-23/06-24 | Q1 statements, core reconciliation, "more than $20 billion" OpenAI statement, Q1 not-commenced leases |
| [Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm) | Period ended 2026-06-30, filed 08-12 | Statements, Note 3 RPO/OpenAI/concentration, Note 10 debt, Note 12 warrants, Note 13 SBC, Note 15 leases, material weaknesses, cover share count |
| [Q2 results release](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056186/cbrsannouncesfinancialresu.htm) | 2026-08-12 | Core reconciliation, Q3 and FY2026 guidance, 600MW capacity statement |
| [Q2 call transcript (third-party)](https://stockanalysis.com/stocks/cbrs/transcripts/686677-q2-2026/) | 2026-08-12 | Statements that 2027 core revenue will more than triple, Q3 margin low point, RPO excludes AWS |
| [Feldman 13G](https://www.sec.gov/Archives/edgar/data/2021728/000149315226038435/primary_doc.xml), Form 4s (2026-08-14 to 10-07, 37 filings) | Event date 2026-06-30; transactions to 10-05 | Founder ownership, insider sales, venture in-kind distributions |
| [CS-4](https://www.cerebras.ai/press-release/cerebras-unveils-cs-4-up-to-30-times-faster-than-gpu-based-solutions-3347356) / [AMD partnership](https://www.cerebras.ai/press-release/amd-and-cerebras-announce-industry-leading-ultra-low-latency-and-high-throughput-ai-inference) / [Gimlet](https://www.cerebras.ai/press-release/gimlet-labs-adds-cerebras-to-deliver-ultrafast-ai-inference-through-gimlet-cloud-deployment) | 2026-08-18 / 07-23 / 09-28 | Product and partnership stage; not a substitute for revenue evidence |
| [BIS UAE rule commentary (Skadden)](https://www.skadden.com/insights/publications/2026/07/bis-liberalizes-export) | 2026-07-16 | G42/Core42 license-free condition and 2027-04-10 deadline; law-firm reading, not the regulatory text |
| [CBRS prices](https://stockanalysis.com/stocks/cbrs/history/) / Nasdaq historical data | 2026-05-14 to 10-16 | Common $127.21 market anchor, IPO first day, highs and lows since listing; excludes after-hours |

**Definitions.** Core revenue/gross profit/operating loss are the company's non-GAAP basis: add back customer-warrant amortization, remove pass-through revenue and cost, and exclude SBC and IPO-related payroll tax. FCF = CFO - purchases of property and equipment. The fully diluted proxy = issued shares + 10-Q Note 5 anti-dilutive securities; it is not a company figure and mixes dates (8/5 and 6/30). TTM = FY2025 + H1 2026 - H1 2025. All revenue forecasts, exit multiples, share counts, cash rates and capex are this report's assumptions; this report does not use pre-IPO funding valuations (the prospectus discloses only per-share prices: Series G $36.2324, Series H $89.0156), unconfirmed media reports or third-party earnings-date estimates.
