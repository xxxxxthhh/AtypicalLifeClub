# Alphabet (GOOG) Deep Research Report

Coverage date: 2026-07-31
Last updated: 2026-11-27
Ticker: NASDAQ: GOOG
Disclaimer: This report is for informational and research purposes only. It does not constitute investment advice. Please conduct your own due diligence.

---

> **2026-11-27 re-anchor.** The latest completed GOOG close was $270.98 on November 25 (New York time). The Q3 ATM draw meets the July downgrade condition. The stance moves from ~~neutral-watch / medium conviction~~ to **cautious / medium conviction**. The November 5 €6B and November 24 C$6B senior notes are separate debt principals in their respective currencies. [Q3 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm) · [Euro notes 8-K](https://www.sec.gov/Archives/edgar/data/1652044/000119312526449835/d174184d8k.htm) · [Canadian notes 8-K](https://www.sec.gov/Archives/edgar/data/1652044/000119312526475973/d91615d8k.htm)



## Executive Summary



> **Framework note:** This report joins the AI-infrastructure book's demand-risk layer as an **architecture check**. The layer already carries two common-constraint reports (Microsoft, Meta) whose job is to prove that hyperscaler capex is real, and one dashboard (Oracle) tracking order quality. Alphabet does not need to repeat that job. What only Alphabet can do is test the **buyer-side architecture question**: the largest own-silicon program in the world has just started selling TPU systems to third parties, which makes Alphabet simultaneously a top-two merchant-silicon customer and a merchant-silicon competitor. That is a different architecture axis from the one nebius-2026 carries in this layer (neocloud versus hyperscaler economics), and it is the demand-side mirror of broadcom-2026's supply-side architecture check. Together the two form a two-sided test of whether custom accelerators are genuinely displacing merchant GPUs or merely riding alongside them.

**One-line thesis.** Search and Cloud grew strongly in Q3, while infrastructure spending took quarterly free cash flow to −$9.065B and Alphabet raised $12.4B of common equity through its ATM program.

**Current view. Cautious / medium conviction.** At $270.98, class-weighted common equity is about $3.346T and EV is about $3.305T after stripping restricted SpaceX stock and including finance leases and preferred equity. That is 21.05x TTM operating income and 167.36x TTM free cash flow. The 20% / 50% / 30% grid weights to $287.08 and +2.8% annualized price return against an 8% research hurdle.

**Quick stats:**

| Metric | Value |
|--------|-------|
| Share price | $270.98 at the 2026-11-25 GOOG close; GOOGL $273.10 |
| First post-results close | $282.32 on 2026-10-29; −4.0% from then to the new anchor |
| Common market cap / shares | About $3.346T; 12,294M Class A / B / C shares at 2026-10-21 |
| Latest report | Q3 2026, ended September 30 and released October 28 |
| Q3 revenue | $127.577B, +25% YoY |
| Q3 operating income / margin | $40.576B, +30% YoY; 31.8% margin |
| Q3 diluted EPS | GAAP $2.12; quarterly net equity securities loss $8.664B |
| Search & other | $63.350B, +12% YoY |
| YouTube ads / subscriptions, platforms and devices | $11.207B / $14.290B |
| Google Cloud | $30.709B, +103%; operating income $11.121B, margin 36.2% |
| Revenue backlog | $567.7B total, $560.8B Cloud; just over 55% of total expected within 24 months |
| Q3 capex / OCF / FCF | $51.355B / $42.290B / −$9.065B |
| TTM OCF / capex / FCF | $179.551B / $159.804B / $19.747B |
| Cash capex through nine months | $131.953B; quantified 2027 capital budget awaits issuer disclosure |
| Cash and securities / carrying debt | $265.098B (including $75.2B of restricted SpaceX) / $126.118B including current debt |
| Capital returns | Buybacks $0 in 9M 2026; $0.22 quarterly common dividend |
| Financing | $12.4B net Q3 ATM proceeds, $28.7B net Q3 senior unsecured notes; $27.6B ATM capacity left |
| Chain role | demand-risk **architecture check**: TPU externalization vs merchant silicon, plus Search resilience and capex funding quality |

## 1. Business Overview

> Q3 2026 update. Services earned $39.157B on $96.302B of revenue (40.7% margin). Cloud earned $11.121B on $30.709B (36.2%). Other Bets reported $0.372B of revenue and a $2.047B operating loss. Search contributed $63.350B, YouTube ads $11.207B, Network $7.455B, and subscriptions, platforms and devices $14.290B. The segment table and initiation analysis below provide the historical Q2 comparison.

Alphabet reports three segments, and Q2 2026 is the first quarter in which all three are visibly reorganized around one asset — the AI compute estate. Consolidated revenue was $119.796B (+24%, +23% constant currency) with operating income of $40.770B, a 34.0% margin that expanded two points while the company spent $44.924B of capex in a single quarter.

| Segment / line | Q2 2026 readout | Economic meaning | AI-infra relevance |
|----------------|-----------------|------------------|--------------------|
| Google Search & other | $63.271B, +17% (Q1 2026 was +19%) | The cash cow, still compounding two years into AI answers | The single most important falsification test for "AI destroys Search economics" |
| YouTube ads | $11.055B, +13% | Second-largest ad property; 1.7B+ unique viewers on World Cup content | Content moat; minor chain relevance |
| Google Network | $7.303B, −0.7% | The declining third-party ad business | Also the business exposed to the ad-tech remedy |
| Subscriptions, platforms & devices | $12.911B, +15% | YouTube Premium/TV, Google One, Pixel | Consumer AI monetization via Google One AI tiers |
| Google Services total | $94.540B, +15%; operating income $39.544B (41.8% margin, from 40.1%) | The funding engine for the entire build | Generates the cash that becomes GPU, TPU, and power purchase orders |
| Google Cloud | $24.768B, +82%; operating income $8.814B (35.6% margin, from 20.7%) | The AI revenue engine; now includes **product revenue from TPU system sales** | The direct landing zone for AI capex and the layer's cleanest demand read |
| Other Bets | $382M revenue; operating loss $1.799B | Waymo, Wing, Isomorphic; Waymo took $16.0B of funding in Feb 2026, the significant majority from Alphabet | Option value, not chain evidence |
| Alphabet-level activities | Operating loss $5.789B (from $3.372B) | Unallocated shared AI R&D — the frontier-model cost centre | The real cost of Gemini is here, not in Cloud's 35.6% margin |

Three structural points matter for this book.

**First, the segment definition changed in substance.** The Q2 10-Q now states that Google Cloud "generates product revenues primarily from the sale of TPU systems." Alphabet has crossed from consuming its own silicon to selling it. Inventory on the balance sheet went from $2.439B at December 31, 2025 to **$9.991B** at June 30, 2026, and the 10-Q defines that inventory as "primarily hardware related to TPU systems for sale to enterprise customers and devices." Section 3 treats this as the report's core question.

**Second, the order book is now comparable to Microsoft's.** Total revenue backlog is $519.5B, of which $513.9B is Google Cloud — roughly 5.2x the annualized Q2 Cloud run-rate — with just over half expected to convert within 24 months. Alphabet changed its backlog definition in Q1 2026 to include contracts with an original expected term of one year or less, so the year-over-year comparison is not like-for-like; the sequential increase of more than $50B is.

**Third, the funding stack inverted.** Alphabet historically returned more cash than any company in this layer. In H1 2026 it repurchased **nothing** (H1 2025: $28.306B), raised $49.6B of equity in June, issued $56.226B net of debt, and let share count rise from 12,088M to 12,230M. Long-term debt roughly doubled, from $46.547B to $98.165B. This is the first time in this book that a company with an unlimited-looking balance sheet has chosen dilution over buybacks to fund compute.

## 2. Industry & Competitive Position

> Q3 2026 update. Search grew about 12%, above the 10% monitoring threshold, with no comparative per-query AI monetization disclosed. Cloud grew 103% and cash capex was $51.355B, about 2.14 times the year-ago quarter. Spend cannot be attributed to individual suppliers. The peer and infrastructure comparisons below retain their Q2 frame.

**Search.** The bear case that AI assistants would strip Google's query monetization has now had two years to show up in the numbers and has not. Search & other grew 17% to $63.271B, decelerating only modestly from Q1 2026's +19%. Management's account is that AI features expand rather than cannibalize: AI Mode passed 1 billion monthly active users after a global rollout last October, AI Overviews and AI Mode were merged into one Search experience, and Gemini's query understanding lets Google monetize longer queries that were previously hard to match to ads. That claim is self-reported and unverifiable from outside, but the revenue line is not — and the revenue line is intact. The Gemini App reports 950M monthly active users and API throughput of roughly 22 billion tokens per minute, up from 16 billion a quarter earlier.

**Cloud.** Google Cloud's +82% is the fastest growth of the big three at meaningful scale — Microsoft's Azure and other cloud services grew 43% in its own June quarter, per the microsoft-2026 report in this hub; AWS is not in this coverage and no figure is asserted for it here. More important is the margin path: 20.7% to 35.6% in four quarters, at a moment when the segment is absorbing the largest infrastructure program in its history. Management flagged that Q3 will bring "modest margin pressure" because Alphabet plans to rent third-party capacity as a bridge while its own build catches up — an admission that it is supply-constrained, and a small piece of demand that flows to the neocloud layer.

**The AI-infrastructure chain.** Alphabet's capex is the demand this book scores:

| Chain position | Alphabet's role | Read-through to existing coverage |
|----------------|-----------------|-----------------------------------|
| GPUs / accelerators | Large NVIDIA buyer and GPU reseller on GCP, while running the industry's only at-scale alternative architecture | Two-sided: supports NVDA volume today, erodes the merchant TAM narrative over time |
| Custom / merchant silicon | TPU is the reference custom-ASIC program; Broadcom is the long-standing co-design partner | Higher TPU volume is directly supportive of the AVGO custom-ASIC thesis |
| HBM / memory | TPU and GPU clusters both consume HBM and datacenter DRAM/NAND | Supports MU, SK hynix, SNDK demand reads regardless of which accelerator wins |
| Networking / optical | ~40% of capex is data centers and networking equipment | Supports ANET, AVGO, GLW, COHR reads |
| Power / facilities | Bought Intersect (renewable developer) for $5.9B in March 2026 to accelerate energy and datacenter capacity | Supports CEG, VST, GEV, VRT, EQIX, DLR reads; also evidence that power, not silicon, is the binding constraint |
| Neocloud | Renting third-party capacity in Q3 2026 as a bridge | Marginally supportive of CRWV/NBIS utilization, and evidence against the "hyperscalers will dump capacity" bear case |
| Foundry | TPU volume feeds TSMC advanced nodes and advanced packaging | Second-order support for the TSM thesis |

**Regulatory.** In Note 10 of its Q3 10-Q, Alphabet reports that the Eastern District of Virginia denied the DOJ’s requested structural divestitures in September 2026 and ordered behavioral remedies covering interoperability, data access and auction conduct. Alphabet plans to appeal the adverse portion after final judgment. Search cross-appeals remained pending per the same filing. Short-term accrued legal and regulatory fines and settlements stood at $13.8B at September 30. Subsequent docket activity remains unverified here. [Q3 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm)

## 3. The TPU Counterfactual: Own Silicon Against Merchant Silicon

> Q3 2026 update. Inventory reached $13.308B, up about 33.2% from $9.991B at June 30. The 10-Q still expects most signed TPU-system agreement revenue in 2027, and the earnings release identifies TPU systems as a meaningful contributor to Cloud growth. The total backlog includes a $16.8B related-party agreement with Crux AI. No TPU-specific revenue, unit or backlog split was disclosed. The architecture comparison below retains the Q2 disclosure frame.

This is the section that justifies Alphabet's place in this book, and the reason its chain role is architecture check rather than common constraint.

Every merchant-silicon thesis in this coverage — NVIDIA's pricing power, Broadcom's custom-ASIC ramp, AMD's second-source case — rests on an assumption about how much accelerator demand hyperscalers will buy versus build. Until this quarter that assumption could not be tested from the buyer's side, because no hyperscaler's internal silicon was a disclosed financial object. Microsoft's Maia is immaterial. Amazon discloses no Trainium economics. Alphabet's Q2 2026 filings changed that.

**What is newly disclosed, and what is not:**

| Observable | Q2 2026 disclosure | What it does and does not prove |
|------------|--------------------|---------------------------------|
| Segment definition | Google Cloud "generates product revenues primarily from the sale of TPU systems" (10-Q) | TPU is now a product line sold to third parties, not only an internal cost centre. It does not size that line. |
| Inventory | $2.439B → $9.991B in six months; "primarily hardware related to TPU systems for sale to enterprise customers and devices" (10-Q) | A ~$7.6B six-month hardware build-ahead. It does not tell us how much is TPU versus Pixel, nor the sell-through. |
| Cost of revenues | Other cost of revenues $29.8B, +22%, driven by depreciation, "inventory costs, primarily from the sales of TPU systems to customers," and YouTube content (call) | TPU sales are already a P&L item and carry hardware-like gross margins. It does not isolate the amount. |
| Revenue recognition | A "small amount" of existing TPU-system agreements recognized in 2026; the "vast majority" in 2027 (call) | The externalization is contracted, not hypothetical — but 2026 financials barely reflect it. |
| Backlog | TPU system sales sit inside the $513.9B Cloud backlog (call) | The commitments are counted. They are not separable from cloud-services backlog. |
| Deployment model | TPUs are being placed in customers' own data centers and in third-party facilities, including a project with Blackstone (call) | Alphabet is willing to ship silicon outside its own estate — the defining merchant behaviour. |
| Allocation policy | Pichai: TPUs are prioritized for frontier-model development; both TPUs and GPUs are used for serving (call) | Internal demand has first call, which caps near-term external supply — and confirms GPUs remain in the serving mix. |

**The read-through is asymmetric, and it is not the same for every supplier.**

For NVIDIA, this is a marginal negative to the *long-run* addressable market rather than to current revenue. Alphabet remains a large GPU buyer and resells NVIDIA capacity on GCP, and its own statement that it serves models on "TPUs and GPUs" is a direct contradiction of the strong substitution thesis. But a hyperscaler that ships accelerators into other people's data centers is no longer only a customer; it is a competitor with a cost structure no merchant vendor can match, because it does not need to earn a margin on the silicon to earn a return on the workload.

For Broadcom, this is a marginal positive. Broadcom is the long-standing TPU co-design and networking partner, and external TPU volume is incremental to the internal roadmap it already ships against. If Alphabet's 2027 recognition guidance is met, it should be visible in AVGO's custom-ASIC line before it is separable in Alphabet's.

For the memory, optical, power, and facility layers this is close to neutral. A TPU rack consumes HBM, optics, and megawatts on the same order as a GPU rack. Substitution at the accelerator layer does not reduce demand at those layers; it only changes whose logo is on the board.

**The evidence limit, stated plainly:** Alphabet discloses no TPU unit volume, no TPU revenue line, and no TPU backlog split. Inventory and the Cloud backlog are the only observables, and neither is attributable to any covered supplier. Anyone reading this quarter as proof that custom silicon is displacing merchant silicon is reading past the disclosure. What the quarter proves is narrower and still important: the option is now real, contracted, and on the balance sheet, and 2027 is when it becomes measurable.

## 4. Financial Analysis

Q3 revenue and operating income grew strongly while operating cash flow trailed cash capital spending.

| Metric | Q3 2026 / September reading | Interpretation | Grade |
|---|---|---|---|
| Revenue growth | $127.577B, +25%; TTM $471.098B | Sustained double-digit growth | A |
| Operating margin | 31.8%, $40.576B of quarterly profit (+30%); TTM $156.976B | Down sequentially from Q2’s 34.0% | B+ |
| Segment quality | Services 40.7%, Cloud 36.2%; Alphabet-level costs $7.655B | Shared AI R&D affects segment comparability | B+ |
| Earnings quality | Diluted EPS $2.12 with $8.664B net equity-securities loss | Investment marks can lift or lower earnings | Caution |
| Free cash flow | $42.290B − $51.355B = −$9.065B; TTM +$19.747B | Quarterly deficit deepens, TTM still positive | Caution |
| Depreciation | PP&E depreciation of $8.369B, 16.3% of cash capex; net PP&E $372.827B | Incoming asset spend leads depreciation | Caution |
| Balance sheet | $265.098B cash and securities, $126.118B carrying debt, plus $3.705B finance leases | After excluding $75.2B of restricted stock, net cash after borrowing is $63.780B | B |
| Capital returns | Nine-month buybacks $0, quarterly common dividend $0.22 | About 0.32% annualized dividend yield | Caution |
| Dilution and financing | 36M ATM shares raised $12.4B net; Q3 senior unsecured notes $28.7B net | October 21 share count already includes Q3 issuance | Caution |
| Order book | Total $567.7B, Cloud $560.8B; just over 55% of total within 24 months | Cloud +9.1% sequentially; total includes $16.8B related-party contract | B+ |
| Off-balance-sheet | $924.4B purchase commitments, $213.4B due within 12 months; $75.7B data center backstops, $48.0B executed / $27.7B future | Distinguish contingent exposure from carrying debt | Caution |

Peer columns retain the initiation comparison dates and their own reporting bases.

| Metric | Alphabet (Q3 2026) | Microsoft (FY26 Q4) | Meta (Q2 2026) | Oracle (FY26 Q4 / full year) |
|---|---|---|---|---|
| Capex | $51.355B cash | $41B incl. finance leases | $31.078B | FY2026 $55.66B |
| OCF | $42.290B | $55.4B | $31.862B | — |
| FCF | −$9.065B | ~$19.6B | $0.784B | FY2026 −$23.69B |
| Order book | $567.7B total | Commercial RPO $678B | — | RPO $638B |
| Repurchases / financing | No buybacks through nine months; Q3 ATM and senior notes | $22.3B of FY26 buybacks | Ongoing in Q2 | Initiation comparison assumed planned debt and equity |

| Red flag | Verified position | Next evidence |
|---|---|---|
| Inventory and monetization | $13.308B inventory and no stand-alone TPU revenue | Signed contract recognition and inventory turnover in 2027 |
| Financing pace | €6B and C$6B notes closed separately in November after the balance sheet date | Actual deployment, debt and cash balances in the next quarter |
| Regulatory implementation | Issuer reports no divestiture ordered in September, but conduct measures apply | Implementation and appeal outcomes |

## 5. Management & Governance

> Q3 2026 update. There were no buybacks through September. The October 21 cover count shows 5,888M / 827M / 5,579M Class A / B / C shares, with Class C non-voting. Alphabet has a conditional commitment for up to $10B of infrastructure and energy backstops for related-party equity-method venture Crux AI. Waymo entered a $5B secured loan in October without an Alphabet guarantee. The Q2 governance and deal background below is historical.

Sundar Pichai's record as CEO now includes the two largest capital decisions in Alphabet's history taken within four months of each other: a capex program guided to $195-205B for FY2026 and "significantly" higher in 2027, and the abandonment of a buyback program that returned $28.306B in H1 2025 alone. CFO Anat Ashkenazi raised FY2026 guidance mid-year and attributed it to "acceleration in the delivery of capacity to meet growing demand" — an honest framing, and the same one Microsoft and Meta used in the same fortnight.

The capital-allocation decision deserves to be named precisely, because it is the most consequential thing in this quarter that management did not explain. Alphabet repurchased nothing in Q1 or Q2 2026 while $69.5B of the April 2025 $70.0B authorization sat unused, and simultaneously raised $49.6B of equity and $56.226B of net debt. Buying back stock and issuing stock in the same six months are not contradictory if the second is cheaper capital for a higher-return use — but the Q2 call did not address the pause, and the release did not either. Investors are left to infer the reasoning from the cash-flow statement.

Governance context sharpens that point. Alphabet's dual-class structure means Class B shares (835M at June 30, 2026) carry super-voting rights concentrated with the founders, while GOOG — the Class C line this report anchors to, 5,527M shares — carries no vote at all. The decision to fund compute by diluting shareholders rather than by returning less is therefore not contestable by the holders being diluted. That is not new, and it is not a scandal; it is a standing discount factor that becomes more relevant the moment the company starts issuing equity.

Capital deployment beyond capex was equally aggressive and, on the whole, coherent. Wiz closed in March 2026 for $29.5B — the largest acquisition in Alphabet's history and a direct bet on multicloud security as a Cloud attach motion, with $22.705B of the price booked as Google Cloud goodwill. Intersect closed the day before for $5.9B, bringing a renewable-energy developer in-house to accelerate datacenter and power capacity; that is vertical integration into the constraint this book has repeatedly identified as binding. Waymo took a $16.0B funding round in February 2026, the significant majority funded by Alphabet, and GFiber is being contributed out for $1.5B in cash, a $2.0B note, and a retained 49.99%. The pattern is consistent: buy into the infrastructure stack, push non-core Other Bets toward outside capital.

Disclosure quality is genuinely mixed, and this report's confidence is calibrated to that:

| Disclosure | Assessment |
|------------|------------|
| Revenue backlog ($519.5B total, $513.9B Cloud, just over 50% within 24 months) | Strong and voluntary; comparable to Microsoft's RPO disclosure |
| SpaceX position ($94.0B fair value, ~4.9% ownership, restriction periods) | Strong; the 10-Q quantifies both the mark and the lock-up |
| EPS effect of the equity gain ($6.26 per diluted share, in a release footnote) | Good practice — management flagged the distortion rather than letting the headline stand |
| TPU system economics | Weak. No unit volume, no revenue line, no backlog split. The report's core question is deliberately unmeasurable from outside |
| GCP within Google Cloud | Weak. Cloud's +82% mixes GCP, Workspace, and now TPU hardware, which have very different margin structures |
| Frontier-model R&D | Parked in the unallocated −$5.789B Alphabet-level line, which flatters Google Cloud's reported 35.6% margin |
| 2027 capex | "Significantly" higher, unquantified, with details deferred |

Two governance watch items follow. First, GAAP net income is now dominated by unrealized marks — $99.031B in Q2 on top of $36.915B in Q1 — which triples reported EPS without a dollar of cash. Management de-emphasized it correctly on the call; any metric, internal or compensation-linked, that keys off GAAP EPS this year is measuring the wrong thing. Second, the off-balance-sheet support has grown into a governance question of its own: $43.8B of maximum potential payments under credit derivatives, $7.6B of financial guarantees, and an agreement to provide an estimated $24.1B of future backstops for third-party build-outs are commitments to other companies' capital structures, disclosed in aggregate and without counterparty detail.

## 6. Bull Case

1. **Search can fund a meaningful part of the build.** It grew about 12% to $63.350B. The ad line is resilient while per-query economics remain unreported.
2. **Cloud is profitable at scale.** Revenue grew 103% at a 36.2% segment margin and backlog rose 9.1% sequentially. Timely delivery would help operating cash growth catch up with spending.
3. **TPU sales already contribute to growth.** Alphabet still expects most revenue under the limited set of signed system agreements in 2027. The March Wiz acquisition adds scope for security attach, with incremental profit still to be observed.
4. **The direct divestiture tail has narrowed.** The issuer reports behavioral remedies in September. Quarterly Network revenue of $7.455B is an exposure indicator, with the scope and cost of compliance still uncertain.
5. **Assets and financing allow adjustment.** Restriction-adjusted cash and securities exceed borrowings by $63.780B, and capital spending can be paced. The optimistic case assumes positive FCF in 2027 and a 34% operating margin in 2028. Section 9 prices that path.

## 7. Bear Case

1. **The ATM has been used.** Q3 FCF was −$9.065B, TTM FCF fell to $19.747B and buybacks stayed at zero. The ATM raised $12.4B net with $27.6B remaining. The issuer intends to use ATM proceeds primarily for employee-equity-related tax obligations, with construction relying on operating cash and other financing sources.
2. **Shareholders face depreciation and dilution.** Quarterly PP&E depreciation was $8.369B against $51.355B of cash capex. Consolidated operating margin fell from Q2’s 34.0% to 31.8%. Newly installed assets and energy costs will test how much margin can hold.
3. **Headline P/E overstates earnings power.** TTM common net income of $235.310B includes estimated pre-tax net equity-securities gains of $129.584B. The adjusted estimate implies 25.17x earnings, and cash return metrics are weaker.
4. **Backlog quality varies.** The $567.7B total includes a $16.8B related-party contract. Executed and future backstops total $75.7B, with payments dependent on contractual conditions.
5. **Regulatory and financing tails remain.** September’s decision reduces immediate divestiture risk, while behavioral effects, Search appeals and the separate Texas case still matter. If Cloud falls below 40% with conversion delays or dilution deepens as cash stays weak, the adverse 2028 case uses a 24% operating margin and 14x EV/EBIT.

## 8. Key Uncertainties

| Uncertainty | Why it matters | When we will know |
|-------------|----------------|-------------------|
| Where does free cash flow trough? | Q3 −$9.065B, TTM +$19.747B and common equity already issued | Quarterly cash flows, ATM and new common-share disclosures |
| Does Cloud backlog convert on schedule? | $560.8B with just over 55% of total backlog guided inside 24 months is the layer's largest single demand claim | Quarterly backlog disclosure and Cloud revenue |
| Does TPU external revenue land in 2027? | The "vast majority" of existing agreements is guided to 2027; slippage would deflate the architecture-check thesis | FY2026 10-K disclosure and 2027 quarterly Cloud product revenue |
| How steep is the depreciation wave? | Tests whether the Q3 consolidated margin of 31.8% holds as depreciation rises | Quarterly cost-of-revenues and margin path through 2027 |
| What changes in implementation or appeal? | The issuer reports behavioral U.S. ad-tech remedies in September and pending Search appeals | Final judgment, implementation terms and appeals dockets |
| Do buybacks resume? | Zero through nine months, $0.22 quarterly dividend | Quarterly financing activities |
| Does Search decelerate again? | About +12% after Q2’s +17%, without an AI query monetization split | Search & other revenue and any per-query disclosure |

Thesis-breaking conditions:

- **July bear-case invalidation test:** quarterly FCF turns positive during 2027 while Cloud holds 50%+ growth, TPU revenue recognizes as guided, buybacks resume, and consolidated operating margin stays above 32% as depreciation ramps. Section 11 uses a separate 30% floor as one condition for returning to neutral-watch.
- **July financing trigger met.** The Q3 ATM issuance met the original downgrade clause. Section 11 retains each of the original operating, financing and regulatory triggers for further review.

## 9. Valuation Context

~~Historical 2026-07-30 anchor: $333.68, about $4.081T of market cap, 26.7x EV/TTM operating income and 73.9x EV/TTM free cash flow.~~

**2026-11-27 update, anchored to the 2026-11-25 close as of the November 27 premarket cut-off.** GOOG closed at $270.98 and GOOGL at $273.10. The October 21 cover lists 5.888 / 0.827 / 5.579B Class A / B / C shares. Class A proxies non-traded Class B. Common equity value = (5.888 + 0.827) × $273.10 + 5.579 × $270.98 = $3.346T. Using GOOG for every class as a sensitivity gives $3.331T.

At September 30, $56.334B of cash plus $208.764B of marketable securities gives $265.098B. Current debt of $1.016B plus $125.102B non-current gives $126.118B of borrowings. Commercial paper was zero. Reported net cash after borrowings is $138.980B. Excluding $75.2B in restricted SpaceX shares leaves $189.898B of cash and securities and $63.780B of net cash. Add separately recorded finance leases of $3.705B and the $19.250B liquidation preference (385M depositary shares × $50) on unconverted preferred shares for $3.305T of EV. Using all reported cash and securities instead gives $3.230T. Operating lease expense stays in EBIT, so operating lease liabilities are excluded from EV. Private investment assets do not offset EV. The post-quarter Waymo loan and two November bond deals are separate disclosures, with September net debt kept on its reported date.

| Measure | Calculation and reading | Interpretation |
|---|---|---|
| TTM revenue / operating income | FY2025 − 9M25 + 9M26 = $471.098B / $156.976B | Both through September 30 |
| P/sales and EV/sales | $3.346T / $471.098B = 7.10x; on EV 7.02x | Capital-structure cross-check |
| EV / TTM operating income | $3.305T / $156.976B = 21.05x | Includes depreciation and central R&D expense |
| GAAP P/E reference | $270.98 / approx. $19.15 = 14.15x | EPS approximated as $10.81 − $7.99 + $16.33, with changing weighted shares |
| Equity-gain adjustment | $235.310B − $129.584B × (1 − 21%) = $132.939B; market cap / adjusted income = 25.17x | Illustrative flat tax rate, strips realized and unrealized net equity-securities gains, retains other nonoperating items |
| EV / TTM FCF and FCF yield | $179.551B − $159.804B = $19.747B; EV / FCF 167.36x; FCF / common market cap 0.59% | Issuer cash-capex definition, with stock compensation and lease principal considered separately |
| Cash capex intensity / common dividend yield | $159.804B / $471.098B = 33.9%; $0.88 / $270.98 = 0.32% | Annualized dividend uses the current quarterly $0.22 |
| Backlog coverage | $560.8B / ($30.709B × 4) = 4.57x | Capacity, consumption and contract duration set timing |

**End-2028 scenario grid.** These are research assumptions, with USD and share counts in billions. Terminal price = (revenue × operating margin × EV/EBIT + terminal available net cash after finance leases and senior preferred claims) ÷ diluted common shares. Dilution assumptions cover net new common shares. Preferred remains a separate claim to avoid counting both conversion shares and preference. The exit multiples reflect different returns on investment, regulatory tails and Cloud growth.

| Scenario | Operating and funding assumptions | Sales / margin / EBIT | Multiple / net bridge / shares | Price / return from anchor | Weight |
|---|---|---|---|---|---|
| Bull | Cloud ≥55% in 2027, TPU monetizes on schedule, FCF turns positive and financing needs fall | 730 / 34% / 248.20 | 23x / +70 / 12.35 | $467.90 / +72.7% | 20% |
| Base | Cloud gradually cools to 40%–55%, TPU recognition remains unbroken out, FCF recovery is slow and behavioral remedies apply | 645 / 30% / 193.50 | 19x / +45 / 12.45 | $298.92 / +10.3% | 50% |
| Bear | Cloud falls below 40% with delayed conversion, depreciation squeezes margins, more capital is needed and enforcement tightens | 555 / 24% / 133.20 | 14x / −15 / 12.60 | $146.81 / −45.8% | 30% |

The 767 days to 2028-12-31 are about 2.100 years. Weighted terminal price is $287.08, or +5.9% total and +2.8% annualized price return. Excluding dividends, 8% annualized requires $318.51 at exit, or a $244.24 entry at the same weights. Moving 10 points from the pessimistic to the optimistic case gives $319.19 and +8.1% annualized. Moving 10 points the other way gives $254.97 and −2.9%. Relative to July, executed equity issuance and lower TTM FCF raise the adverse weight, while the September behavioral decision and continued Cloud growth support the central case. The adverse price and low cash yield support cautious. Medium conviction reflects the sensitivity to weights and limited data on TPU and remedy economics.

## 10. Catalysts & Timeline

| Catalyst | Timing | Impact |
|----------|--------|--------|
| Q3 2026 results | Reported October 28 | Cloud growth, quarterly FCF deficit and actual ATM issuance |
| EDVA behavioral remedies | September decision as reported by issuer | Final judgment, appeal, compliance cost and auction effects are still to be checked |
| FY2026 10-K and next capex outlook | Early 2027 | Look for separate TPU economics and a quantified FY2027 capex plan |
| Search appeals | Pending in the Q3 10-Q | Await the court’s schedule and decisions |
| 2027 capex | Next quantified issuer outlook | Compare with revenue, depreciation and external financing |
| Further ATM sales or buyback resumption | Event-driven | Track fresh financing beyond already executed Q3 issuance |
| GFiber close | Late 2026 per the Q3 10-Q | $1.5B cash, $2.0B note and 49.99% retained; verify actual closing |

The structured monitoring fields focus on six readouts: Search resilience against AI answers, Cloud backlog conversion, the free-cash-flow and funding mix, TPU external monetization, the depreciation wave, and the ad-tech remedy outcome.

## 11. Conclusion

Alphabet still provides the buyer-side test of how custom and merchant silicon coexist. Q3 Cloud grew 103%, with most revenue under current TPU systems agreements still expected in 2027. Search grew about 12%, while cash capex exceeded operating cash flow by $9.065B and the ATM raised $12.4B net, meeting an independently sufficient July downgrade clause. The Q3 cash-flow data, the November notes and the September remedies decision each have separate evidence.

**Current view is cautious / medium conviction, at the 2026-11-25 close of $270.98.** EV/TTM operating income is 21.05x, FCF is 0.59% of common market capitalization, weighted annualized price return is +2.8%, and the adverse case implies −45.8%. That leaves limited tolerance for further capital intensity and dilution.

Upgrade to neutral-watch after two consecutive quarters of positive free cash flow, no new financing-related common issuance during that period, and consolidated operating margin of at least 30% in both quarters, with Cloud backlog conversion and TPU milestones checked. The July bear-case invalidation test in Section 8 separately retains its above-32% margin requirement.

Q3 ATM issuance satisfied the original neutral-watch to cautious trigger. From cautious, promptly reassess for a further downgrade if any of the original alternatives occurs: TTM free cash flow turns negative, Alphabet makes a new draw under the $40B ATM program or issues further equity after Q3, Cloud growth drops below about 40% while backlog conversion slips, consolidated operating margin falls below about 30% as depreciation ramps, external TPU revenue slips out of 2027, or a structural ad-tech remedy is ordered. Each remains an independent trigger for a new decision. A bearish-avoid stance requires an explicit review of the evidence and valuation. The completed Q3 issuance is logged in stance history.

## Appendix: Sources & Assumptions

- Current sources: [Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm) (capital, operations and legal note), [Q3 earnings release](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000080/googexhibit991q32026.htm) (cash-flow reconciliation), [FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm) (TTM roll-forward), [November 5 euro notes 8-K](https://www.sec.gov/Archives/edgar/data/1652044/000119312526449835/d174184d8k.htm), [November 24 Canadian notes 8-K](https://www.sec.gov/Archives/edgar/data/1652044/000119312526475973/d91615d8k.htm), [Nasdaq GOOG closes](https://api.nasdaq.com/api/quote/GOOG/historical?assetclass=stocks&fromdate=2026-10-29&todate=2026-11-27&limit=30), [Nasdaq GOOGL closes](https://api.nasdaq.com/api/quote/GOOGL/historical?assetclass=stocks&fromdate=2026-11-24&todate=2026-11-27&limit=10), and the [Nasdaq trading calendar](https://www.nasdaq.com/market-activity/stock-market-holiday-schedule). The valuation cut-off was November 27 at 09:11 ET, before the 09:30 ET regular-session open. Nasdaq was closed on November 26 and scheduled a 13:00 ET close on November 27. The November bond principals are denominated in their own currencies and excluded from the September USD borrowing balance.


- Q2 2026 consolidated revenue ($119,796M), revenue by line (Google Search & other $63,271M, YouTube ads $11,055M, Google Network $7,303M, Google advertising $81,629M, Google subscriptions/platforms/devices $12,911M), segment revenue and operating income (Google Services $94,540M / $39,544M; Google Cloud $24,768M / $8,814M; Other Bets $382M / −$1,799M; Alphabet-level activities −$5,789M), total operating income ($40,770M) and 34% margin, other income (expense) net ($97,983M including a $99,031M net gain on equity securities), net income ($112,193M), diluted EPS ($9.11), TAC ($16,179M), employees (198,933), the balance sheet (cash and marketable securities $242,474M, inventory $9,991M vs $2,439M at 2025-12-31, property and equipment net $321,212M vs $246,597M, long-term debt $98,165M vs $46,547M, goodwill $57,828M, total assets $921,983M, stockholders' equity $640,480M, 12,230M Class A+B+C shares outstanding), the cash-flow statement (Q2 operating cash flow $39,069M, purchases of property and equipment $44,924M, H1 capex $80,598M, repurchases of stock $0, dividend payments $2,689M, proceeds from common stock $30,499M and mandatory convertible preferred $19,063M, debt issuance $56,226M net for H1), the TTM free-cash-flow reconciliation (OCF $185,675M, capex $132,402M, FCF $53,273M; Q2 FCF −$5,855M), the June 2026 $49.6B equity raise and $40B ATM Program, the Q2 senior unsecured note issuance of $20.3B net, the July 2026 declared dividends ($0.22 per common share; $12.15 per preferred share), and the footnote that the $99.0B equity gain increased the tax provision by $21.9B, net income by $77.1B, and diluted EPS by $6.26 are all from Alphabet's official Q2 2026 earnings release (Exhibit 99.1 to the Form 8-K, dated 2026-07-22): [Q2 2026 earnings release](https://s206.q4cdn.com/479360582/files/doc_financials/2026/q2/2026q2-alphabet-earnings-release.pdf) and the [Alphabet investor news page](https://abc.xyz/investor/news/news-details/2026/Alphabet-Announces-Second-Quarter-2026-Results-2026-Y3uQ6H4ZJa/default.aspx).
- The revenue backlog ($519.5B total, $513.9B Google Cloud, just over 50% expected within 24 months, and the Q1 2026 election to include contracts with an original expected term of one year or less), the inventory definition ("primarily hardware related to TPU systems for sale to enterprise customers and devices"), the Google Cloud segment description ("generates product revenues primarily from the sale of TPU systems"), the share-repurchase disclosure (no repurchases in the three and six months ended 2026-06-30; $69.5B remaining of the April 2025 $70.0B authorization), purchase commitments and other contractual obligations of $811.0B ($200.7B short-term), backstops of $7.6B in financial guarantees and $43.8B in credit derivatives plus an estimated $24.1B of future backstops, short-term accrued legal and regulatory fines and settlements of $17.4B, the Wiz acquisition ($29.5B closed 2026-03-11; $22,705M goodwill to Google Cloud, $8,300M intangibles), the Intersect acquisition ($5.9B closed 2026-03-10), the pending GFiber contribution ($1.5B cash, $2.0B note receivable, 49.99% retained interest, expected to close late 2026), the SpaceX position (total fair value $94.0B at 2026-06-30, ~4.9% effective ownership, of which $80.0B is subject to short-term sale restrictions and $14.1B to restrictions through Q3 2027), and the antitrust status of the DOJ Search case (final judgment December 2025; Google appeal January 2026; DOJ/state appeal February 2026) and the ad-tech case (April 2025 EDVA mixed ruling; remedies proceeding September 2025; closing arguments November 2025; final judgment pending; DOJ structural proposal that "could have a material adverse effect on our business") are from Alphabet's Form 10-Q for the quarter ended 2026-06-30: [Alphabet Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000071/goog-20260630.htm). The Q1 2026 equity-securities gain of $36,915M, the Q1 2026 effective tax rate of 19.2%, and the February 2026 Waymo funding round of $16.0B are from the Form 10-Q for the quarter ended 2026-03-31: [Alphabet Q1 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000048/goog-20260331.htm).
- **Earnings-call figures (not in the press release), labelled as such:** the FY2026 capex guidance raise to $195-205B from $180-190B; the ~60% servers / ~40% data centers and networking split; the statement that capex will increase "significantly" in 2027; the TPU revenue-recognition commentary (a small amount in 2026 with the vast majority of existing agreements in 2027, TPU sales included in the Cloud backlog, TPU placement in customer and third-party data centers including a project with Blackstone, and the build-ahead inventory rationale); the plan to expand third-party capacity in Q3 2026 as a bridging strategy with "modest margin pressure"; the statement that infrastructure investment "will continue to put pressure on the P&L in the form of higher depreciation expense"; other cost of revenues of $29.8B (+22%) and its drivers; and the Gemini/AI Mode metrics (AI Mode 1B+ MAU, Gemini App 950M MAU, ~22B API tokens per minute up from 16B, 9M+ monthly developers, ~90% of the Fortune 100 on Gemini Enterprise) are from the Q2 2026 earnings-call coverage: [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-alphabet-beats-q2-2026-estimates-shares-fall-on-capex-surge-93CH-4807140). Where the call and the filings differ in rounding (for example the call's "$514 billion" Cloud backlog), this report uses the 10-Q figure of $513.9B.
- FY2025 comparatives used to derive trailing-twelve-month figures (revenue $402,836M, operating income $129,039M, diluted EPS $10.81) are from Alphabet's Q4 and fiscal-year 2025 results; H1 2025 comparatives (revenue $186,662M, operating income $61,877M, diluted EPS $5.12) are from the Q2 2026 press release's own year-to-date columns. TTM revenue ($445.9B) and TTM operating income ($147.6B) are computed as FY2025 minus H1 2025 plus H1 2026; TTM GAAP diluted EPS (~$19.9) is computed the same way and is approximate because per-share amounts are not strictly additive across periods.
- The attribution of the $99.0B equity gain to Anthropic and SpaceX specifically is media inference, not company disclosure: the press release says only that the gain was "primarily the result of net unrealized gains on our equity securities," while the 10-Q discloses the SpaceX position directly. The Anthropic valuation mark is from press coverage: [Fortune](https://fortune.com/2026/07/22/anthropic-spacex-investments-google-earnings-biggest-ever-profit-quarter/).
- ~~The historical market anchor was the 2026-07-30 close of $333.68 and about $4.081T in common equity.~~
- The FY2026 revenue estimate of roughly $493B used only for the forward capex-intensity figure is our own annualization (H1 2026 actual $229.692B plus H2 2025 grown at approximately the current rate) and is not company guidance. Peer figures for Microsoft, Meta, and Oracle are from the microsoft-2026, meta-2026, and oracle-2026 reports in this hub and this hub's verified signal ledger entry `alphabet-q2-2026-capex-raise`; each is stated at its own reported period and is not restated to a common calendar. This report does not use non-public information.
