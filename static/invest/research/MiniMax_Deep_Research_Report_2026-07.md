# MiniMax Group Deep Research Report: Application-Layer Demand Validation and Valuation Stress Test

Coverage date: 2026-07-15
Last updated: 2026-07-15
Ticker: HKEX: 0100
Disclaimer: This report is for informational and research purposes only. It does not constitute investment advice. Please conduct your own due diligence.

---

## 1. Executive Summary and Current View <!-- report-module:overview -->

**One-sentence thesis:** MiniMax has shown that an independent Chinese foundation-model company can build global users, consumer-product revenue, and enterprise API revenue at the same time, but **FY2025 revenue of US$79.0M, a 25.4% gross margin, and US$279.6M of operating cash outflow** do not yet support the current **HK$91.2B market capitalization and 147.9x FY2025 price-to-sales ratio**. Initial coverage is **cautious / low conviction**.

MiniMax sits in the `demand-risk` layer as a `risk-anchor`. It does not validate GPU, network, or data-center supply. It tests whether upstream AI infrastructure can become paid users, API consumption, gross profit, and cash recovery at the application layer. If user and token growth do not improve unit economics, usage alone is not durable proof of returns on upstream capital expenditure.

### Current snapshot

| Metric | 2026-07-15 snapshot | Research implication |
|---|---:|---|
| Closing price | HK$261.00 | Yahoo Finance / `0100.HK` close on 2026-07-15 |
| Post-placement shares | 349.235M | 313.635M existing shares plus 35.600M new shares |
| Market capitalization | About HK$91.15B | Uses shares outstanding after placement completion |
| Estimated enterprise value | About HK$68.45B | Deducts about HK$22.70B of pro forma net cash; excludes the proposed convertible bond |
| FY2025 revenue | US$79.038M / about HK$616.5M | Up 158.9% year over year |
| FY2025 gross margin | 25.4% | Up from 12.2% in FY2024 |
| Price-to-sales / EV-to-sales | About 147.9x / 111.0x | Both use actual FY2025 revenue |
| Adjusted net loss | US$250.856M | About 3.17 times revenue |
| Operating cash flow | Negative US$279.641M | Commercialization does not yet fund R&D and compute |

Pro forma net cash adds the company-defined US$1.050B cash balance at FY2025 year end, HK$5.293B of IPO net proceeds, and HK$9.491B from the placement completed on 2026-07-14, then deducts US$35.5M of bank and other borrowings at an approximate 7.8 HKD/USD rate. This is an **upper-bound snapshot before 2026 operating burn and use of proceeds**, not an audited cash balance as of 2026-07-15.

**Current view: cautious / low conviction.** Business evidence is positive: revenue grew 158.9%, gross margin improved by 13.2 percentage points, international revenue was 73%, and paid consumer-product users reached 1.77M in the first nine months of 2025. Valuation, however, requires roughly **69% revenue CAGR over four years**, with sustained gross-margin expansion and lower cash burn. Recent equity financing removes near-term liquidity pressure but also shows that training, inference, and global commercialization remain externally funded.

## 2. Business Overview and Segment Economics <!-- report-module:business -->

Founded in 2022, MiniMax combines foundation models, first-party applications, and an open platform. Its models cover text and code, video, speech, and music. Main products include MiniMax Agent, Hailuo AI, MiniMax Audio, Talkie, and the developer and enterprise Open Platform. M3, launched on 2026-06-01, supports up to a one-million-token context window, native multimodality, coding and agent work, and computer use. The company has not yet disclosed audited M3 contributions to revenue, paid users, or inference unit cost.

### FY2025 revenue mix

| Revenue channel | FY2025 | Mix | YoY | Economic profile |
|---|---:|---:|---:|---|
| AI-native products | US$53.075M | 67.2% | +143.4% | Subscriptions, virtual items, top-ups, and online marketing; inference cost directly affects margin |
| Open Platform and other enterprise services | US$25.963M | 32.8% | +197.8% | API and enterprise services; materially higher margin in the first nine months of 2025 |
| Total | US$79.038M | 100% | +158.9% | Small commercial base but very rapid growth |

Mainland China generated US$21.375M, or 27.0% of FY2025 revenue, while international markets generated US$57.663M, or 73.0%. Geographic breadth reduces dependence on one domestic market but increases exposure to cross-border data rules, content regulation, payments, foreign exchange, and intellectual-property disputes.

### User and monetization funnel as of 2025-09-30

| Product or channel | Cumulative users or customers | Average MAU | Paying users in period | Key observation |
|---|---:|---:|---:|---|
| All AI-native products | 212.247M | 27.622M | 1.772M | Cumulative users are not necessarily unique individuals; a payer made at least one transaction |
| Talkie | 147.100M | 20.051M | 1.390M | Largest consumer product and primary source of paying users |
| Hailuo AI | 42.348M | 5.648M | 0.311M | Video generation is the second scaled product |
| MiniMax main product | 19.057M | 1.429M | 0.010M | Agent and text monetization remained early |
| Open Platform | 132K calling customers | 16K monthly active customers | 2.5K paying customers | Paying threshold was at least US$50 of API consumption during the period |

Consumer applications provide distribution and product feedback. API and enterprise services provide stronger gross-margin potential. The central question is whether MiniMax can convert its large free audience into durable paid demand while the higher-margin platform business absorbs training and inference costs.

## 3. Industry, Competition, and Moat <!-- report-module:competition -->

The prospectus cites CIC estimates that the global foundation-model market, measured by model-related revenue, could expand from US$10.7B in 2024 to US$206.5B in 2029, an implied 80.7% CAGR. It also places MiniMax tenth globally with roughly 0.3% share in 2024. Because this work was commissioned by the issuer, it is best treated as a market scenario rather than a settled fact.

### Competitive position

| Dimension | MiniMax | Z.ai, HKEX: 2513 | Large platforms and private frontier labs |
|---|---|---|---|
| FY2025 revenue | US$79.0M, +158.9% | RMB724.3M, +131.9% | Often stronger scale, compute, and distribution, but disclosure is inconsistent |
| FY2025 gross margin | 25.4% | 41.0% | Mature cloud and API businesses can be higher; consumer generation is inference-heavy |
| R&D as percentage of revenue | About 320% | About 439% | Frontier competition requires high spending and absolute capital capacity |
| Commercial mix | Consumer products 67.2%; platform and enterprise 32.8% | API 26.3%; enterprise agents 22.9%; enterprise models 50.4% | Large platforms cross-distribute through search, cloud, productivity, or advertising |
| Main differentiation | Integrated text, video, speech, and music plus global consumer distribution | Enterprise deployment, GLM APIs, and agent engineering | Closed-model capability, ecosystem, channels, chip access, and capital |

### Competitive scenarios and valuation mapping

| Scenario | Competitive outcome | Valuation implication | Weight |
|---|---|---|---:|
| Bull | Multimodal products and the platform gain share together | 70%-80% revenue CAGR can absorb the current high multiple | 20% |
| Base | MiniMax retains an independent position, but platforms constrain acquisition and API pricing | 50%-60% CAGR falls short of the market-implied 69% requirement | 50% |
| Bear | Open models and platform distribution weaken differentiation while litigation limits products | Revenue and valuation multiple reset together | 30% |

MiniMax has three possible moat layers. Multimodal model work can be reused across Hailuo, Audio, Talkie, and Agent. Distribution across more than 200 countries and regions provides product feedback. Consumer products, APIs, and enterprise services offer multiple monetization paths. None is yet validated by profit: model capabilities change rapidly, open weights compress API prices, switching costs are limited, and large platforms acquire users and compute more efficiently.

The supply side is not independent. The prospectus reports about US$58.3M of Alibaba Cloud purchases in the first nine months of 2025 and proposed related-party cloud-service caps of US$115M, US$125M, and US$135M for 2026, 2027, and 2028. Reliable compute access is useful, but supplier concentration, related-party governance, and inference costs constrain margins.

## 4. Financial Health, Cash Burn, and Red Flags <!-- report-module:financial -->

### Financial health matrix

| Metric | FY2025 | FY2024 | Change and interpretation |
|---|---:|---:|---|
| Revenue | US$79.038M | US$30.523M | Up 158.9%; strong scale growth |
| Gross profit | US$20.079M | US$3.738M | Up 437.2%; faster than revenue |
| Gross margin | 25.4% | 12.2% | Up 13.2 percentage points but below mature software and API economics |
| Selling and distribution expense | US$51.896M | US$86.995M | Down 40.3% as organic discovery and recommendations reduced acquisition spend |
| R&D expense | US$252.771M | US$188.979M | Up 33.8%; about 3.20 times revenue |
| Adjusted net loss | US$250.856M | US$244.243M | Absolute loss barely narrowed, although loss margin improved |
| Operating cash flow | Negative US$279.641M | Negative US$258.483M | Cash burn increased 8.2% |
| Year-end cash balance | US$1.050B | US$0.881B | Includes cash, restricted cash, time deposits, and FVTPL financial assets |

The IFRS net loss of US$1.872B mainly reflected a US$1.590B fair-value loss on redeemable preferred shares, which converted to ordinary shares at the IPO. Adjusted loss and cash flow are more useful for operating analysis. Even on that basis, FY2025 operating cash outflow was US$279.6M and R&D spending was more than three times revenue.

### Financing and dilution timeline

| Date | Event | Scale | Shareholder implication |
|---|---|---:|---|
| 2026-01-09 | Hong Kong IPO | About HK$5.293B net including over-allotment | Extended runway; 313.635M shares after listing |
| 2026-06-23 | Post-IPO awards | 1.169M awards | No purchase price and staged vesting create future dilution |
| 2026-07-14 | Share placement completed | 35.600M shares at HK$268; about HK$9.491B net | Share count rose to 349.235M, or 11.35% above the pre-placement total |
| Pending | Zero-coupon convertible bond | HK$6.500B principal; initial conversion price HK$335 | Full conversion would add about 19.403M shares; issuance is independent of the placement |

### Red-flag review

- **Cash burn: severe, but not a near-term solvency crisis.** External financing provides substantial liquidity; self-funded operations do not yet exist.
- **Dilution: material.** The July placement is complete, while awards and the convertible bond may expand fully diluted shares further.
- **Supplier concentration: monitor.** Training and inference rely on a small number of large cloud providers.
- **Intellectual property litigation: monitor.** Major US film studios have sued over Hailuo AI. MiniMax recorded no provision at FY2025 year end because outcome and loss could not be estimated reliably.
- **Audit and controls: no major qualification identified.** Ernst & Young audited FY2025, and this review found no auditor change or going-concern qualification.

## 5. Management, Governance, and Capital Allocation <!-- report-module:management -->

Founder Yan Junjie serves as chairman and chief executive. A single product and research roadmap can improve execution speed, and FY2025 revenue and gross-margin gains are evidence of rapid delivery. Releases including M2.7, M3, and agent-team products also show a sustained cadence. The next test is whether technical releases become paid demand, gross profit, and cash rather than only benchmark scores or token throughput.

MiniMax uses a weighted-voting-rights structure. Class A shares carry one vote and Class B shares carry ten votes. The FY2025 annual report disclosed 81.103M Class B shares, allowing the founder to retain voting control without majority economic ownership. This can protect long-horizon research but weakens external shareholder influence over capital allocation, dilution, and related-party transactions.

Capital priorities are explicit. Ninety percent of IPO net proceeds was allocated to R&D: 50% for model research and AI infrastructure, 20% for model talent, and 20% for product development and global expansion. July placement proceeds were also designated for AI infrastructure, model development, global commercialization, and Harness products. The priorities fit the strategy, but repeated financing makes capital efficiency a central governance question.

The preliminary management assessment is **B / awaiting validation**. Technology and growth execution are strong and gross-margin improvement is credible. Cash consumption, WVR control, related cloud procurement, IP litigation, and a large placement within six months of listing reduce governance visibility.

## 6. Bull and Bear Cases <!-- report-module:bullBear -->

### Bull case

1. FY2025 revenue grew 158.9%, and both AI-native products and Open Platform or enterprise services grew more than 140%, reducing dependence on a single product.
2. Gross margin improved from 12.2% to 25.4%. Open Platform and enterprise gross margin reached 69.4% in the first nine months of 2025, showing possible operating leverage.
3. AI-native products averaged 27.6M MAU and 1.77M paying users in the first nine months of 2025, while international revenue reached 73%.
4. The IPO and completed placement provided about HK$14.8B of net proceeds for M3, agents, video, speech, music, and global distribution.
5. If open-weight M3, its long context window, and multimodal agents create developer adoption, Open Platform mix and consolidated gross margin could rise quickly.

### Bear case

1. US$79.0M of revenue supports about HK$91.2B of market capitalization, a 147.9x historical price-to-sales ratio with little room for commercial execution errors.
2. Adjusted net loss was US$250.9M and operating cash outflow was US$279.6M, both more than three times revenue. Growth remains externally funded.
3. AI-native product gross margin was only 4.7% in the first nine months of 2025. Free-user scale can amplify token cost rather than profit.
4. The share price fell about 49% from HK$515 on 2026-06-23 to HK$261.00 on 2026-07-15, showing extreme sensitivity to financing and risk appetite.
5. Open models and large platforms can compress API pricing, while IP, content safety, cross-border data, and technology regulation affect both products and valuation.

| Thesis | Evidence required | Disconfirming signal |
|---|---|---|
| Consumer products achieve scale economics | AI-native gross margin stays above 20% and paid conversion and ARPU rise together | MAU grows while margin stalls and marketing expense rebounds |
| Platform becomes the profit engine | Open Platform reaches more than 40% of revenue and keeps gross margin above 60% | API price competition pushes margin below 50% |
| Financing creates long-duration compounding | Revenue grows faster than cash burn and runway extends | Another large equity raise within two years without better unit economics |

## 7. Key Uncertainties and Thesis-Breaking Conditions <!-- report-module:uncertainties -->

| Uncertainty | Current reading | Upgrade condition | Failure or downgrade condition |
|---|---|---|---|
| Revenue quality | FY2025 +158.9%; products 67.2%, platform 32.8% | Both platform and paid consumer revenue grow above 80% in 2026 | Growth falls below 50% and relies on promotion or one product |
| Unit economics | FY2025 gross margin 25.4%; CFO negative US$279.6M | Gross margin above 40% and cash burn below 100% of revenue | Gross margin below 25% or burn remains above 200% of revenue |
| User monetization | 9M25 average MAU 27.6M; paying users 1.77M | Paying users and ARPU grow faster than MAU | MAU rises while paid conversion or retention declines |
| Product capability | M3 launched on 2026-06-01 | Third-party adoption, API usage, and paid disclosures rise together | Benchmarks improve without commercial KPI response |
| Capital and dilution | July placement added 11.35%; bond remains pending | Proceeds accelerate revenue and margin, with no large equity raise for 24 months | Bond conversion is followed by more placement or award expansion |
| Legal and regulatory | Hailuo US IP litigation has no provision | Litigation remains controlled and content governance improves | Injunction, material damages, or restrictions in a key market |

The thesis does not fail because one model temporarily trails a benchmark. It fails if **at least two of revenue growth, gross margin, and cash burn deteriorate for two consecutive reporting periods**. A model release or a higher share price alone is not an upgrade trigger.

## 8. Valuation and Expectation Gap <!-- report-module:valuation -->

MiniMax is loss-making, so P/E, free-cash-flow yield, and a conventional DCF are not decision-useful. A more transparent framework calculates market capitalization using post-placement shares, deducts reported financial assets and completed financing, and uses EV to FY2025 sales to expose the growth demanded by the market price.

### Current valuation bridge

| Item | Estimate | Method |
|---|---:|---|
| Price multiplied by post-placement shares | HK$261.00 x 349.235M | About HK$91.15B market capitalization |
| Pro forma cash and financial assets | About HK$22.98B | FY2025 cash balance plus IPO and completed placement net proceeds |
| Bank and other borrowings | About HK$0.28B | US$35.5M at 7.8 HKD/USD; excludes the pending bond |
| Estimated enterprise value | About HK$68.45B | Upper-bound pro forma snapshot before 2026 cash use |
| FY2025 revenue | About HK$0.616B | US$79.038M at 7.8 HKD/USD |
| Price-to-sales / EV-to-sales | About 147.9x / 111.0x | Historical revenue multiples, not target prices |

### Market-implied requirement

If EV-to-sales normalizes from about 111.0x to 20x over four years and investors require a 10% annual return:

`Implied revenue CAGR = (111.0 / 20)^(1/4) x 1.10 - 1 = approximately 68.8%`

The price therefore requires close to 69% FY2025-FY2029 revenue CAGR alongside significant gross-margin expansion, declining cash burn, and controlled dilution. The base case assumes 50%-60% CAGR, below the market-implied requirement, so the expectation gap is negative.

| Scenario | FY2025-FY2029 revenue CAGR | FY2029 margin and cash profile | Valuation interpretation | Weight |
|---|---:|---|---|---:|
| Bull | 70%-80% | Gross margin 45%-55%; near operating cash-flow breakeven | Platform and API scale can absorb the current multiple | 20% |
| Base | 50%-60% | Gross margin 35%-45%; burn rate falls but investment continues | Business succeeds but falls short of approximately 69% implied growth | 50% |
| Bear | 25%-40% | Gross margin below 35%; continued financing and dilution | Revenue and valuation multiple reset together | 30% |

This report does not issue a target price. The valuation exercise measures the tolerance for growth, margin, and financing errors rather than pretending to estimate a precise fair value.

## 9. Catalysts and Monitoring Checklist <!-- report-module:catalysts -->

| Timing or event | Catalyst or risk | Auditable reading to monitor |
|---|---|---|
| 2026 interim results | First listed interim operating update | Segment revenue, gross margin, R&D, operating cash flow, and cash balance |
| M3 commercialization | Model capability becomes platform demand | Paying API customers, token consumption, enterprise adoption, and inference unit cost |
| Hailuo and Talkie updates | Consumer conversion and retention | MAU, paying users, ARPU, and AI-native gross margin |
| Placement proceeds | Financing becomes growth | Use of HK$9.491B net proceeds, compute purchases, and R&D efficiency |
| Bond closing or conversion | Potential financing and dilution | Completion, conversion-price adjustment, and the potential 19.403M shares |
| IP and regulatory developments | Downside tail risk | Hailuo litigation, content governance, cross-border data, and product restrictions |

The next formal review should follow the 2026 interim results and update three trends together: FY2025 revenue growth versus 2026 growth, 25.4% gross margin versus the new margin, and US$279.6M operating cash outflow versus new burn. Updating product releases without refreshing valuation and cash consumption would create false freshness.

## 10. Conclusion and Review Rules <!-- report-module:conclusion -->

**Conclusion: cautious / low conviction.** MiniMax is a rare listed pure-play foundation-model and application company. Its global users, consumer revenue, API revenue, and gross-margin improvement are real positive evidence. The problem is not an absence of product-market fit. The problem is that about 111.0x EV to FY2025 sales demands close to 69% revenue CAGR while high R&D spending, low consumer-product margins, IP risk, and dilution all improve at once.

**Upgrade rule:** Move toward `neutral-watch` or `constructive` if an interim or later report shows revenue growth above 80%, consolidated gross margin above 40%, continued Open Platform mix and paying-customer gains, operating cash burn below 100% of revenue, and at least 24 months of funding without another large equity raise.

**Downgrade rule:** Move to `bearish-avoid` if revenue growth falls below 50%, consolidated gross margin remains near 25%, operating cash burn stays above 200% of revenue, or further large placements follow the bond and awards. A material IP injunction, damages award, or restriction in a key market would also trigger a downgrade.

MiniMax is the application-layer risk anchor for the broader AI-infrastructure research book: **token growth becomes high-quality validation of upstream compute demand only when paid demand, gross margin, and cash recovery improve together.**

## 11. Appendix, Assumptions, and Sources <!-- report-module:appendix -->

### Key assumptions

- Market price is the `0100.HK` close of HK$261.00 on 2026-07-15, obtained through the Yahoo Finance price ledger.
- Market capitalization uses 349,235,308 shares after placement completion, not the stale 313,635,308 shares still shown by some market-data services.
- A 7.8 HKD/USD approximation is used only for the valuation bridge; foreign-exchange precision does not drive the conclusion.
- Pro forma cash does not deduct 2026 operating burn or deployment of proceeds, so enterprise value may be understated. The proposed bond is excluded from cash, debt, and conversion shares.
- Scenarios are growth and unit-economics stress tests, not earnings forecasts or target prices.

### Primary sources

1. [MiniMax FY2025 Annual Report, HKEX, 2026-04-22](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0422/2026042202118.pdf)
2. [MiniMax Prospectus, HKEX, 2025-12-31](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/1231/2025123100025.pdf)
3. [IPO Final Offer Price and Allotment Results, HKEX, 2026-01-08](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0108/2026010801342.pdf)
4. [35.6M Share Placement and HK$6.5B Convertible Bond Announcement, HKEX, 2026-07-10](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0710/2026071000027.pdf)
5. [Next Day Disclosure Return after Placement Completion, HKEX, 2026-07-14](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0714/2026071400331.pdf)
6. [MiniMax M3 Official Release, 2026-06-01](https://www.minimax.io/blog/minimax-m3)
7. [Z.ai FY2025 Annual Results, HKEX, 2026-03-31](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0331/2026033101549.pdf)
8. [Yahoo Finance 0100.HK Historical Data](https://finance.yahoo.com/quote/0100.HK/history/)

---

This report is for informational and research purposes only and does not constitute investment advice. MiniMax has a short listing history, volatile market pricing, and a rapidly changing financing structure. Reconfirm price, share count, bond status, and the latest financial disclosures before making any decision.
