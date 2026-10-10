# Lumentum (LITE) Deep Research Report

Coverage date: 2026-10-11
Last updated: 2026-10-11
Ticker: NASDAQ: LITE
Disclaimer: This report is for informational and research purposes only. It does not constitute investment advice. Please conduct your own due diligence.
Reporting basis: FY2026 Form 10-K (fiscal year ended 2026-06-27) and Q4 FY2026 earnings release; price anchor: $1,103.36 close on 2026-10-09; stance: cautious / low conviction. Financial data is taken from Lumentum's SEC filings and earnings releases unless stated otherwise. Forward figures such as OCS, ultra-high-power (UHP) lasers, the EML supply-demand gap and capacity targets exist only in the earnings calls and the OFC investor briefing and are labelled "(call)" and "(OFC briefing)" respectively — the call transcripts are third-party (Motley Fool), not company-hosted.

---

## Executive Summary <!-- report-module:overview -->

**One-line thesis:** Lumentum is one of the few component companies in AI optical connectivity that supplies all three architecture paths at once — EML and CW lasers for pluggable modules, ultra-high-power (UHP) lasers for co-packaged optics (CPO), and optical circuit switches (OCS) that replace electrical switching — with FY2026 revenue of $3,014.0M (+83.2% year over year), a Q4 non-GAAP operating margin of 36.6%, and a Q1 FY2027 guidance midpoint of $1.25B that delivers the first tier of the OFC target model more than a quarter early. The business evidence is ample; the issue is price: the 2026-10-09 close of $1,103.36 corresponds to a fully diluted market cap of about $112.5B, which requires FY2029 revenue of about $13.2B–$13.8B, an operating margin of 43%–44% and an exit multiple of 24–28x to hold at the same time, roughly equal to the company's entire disclosed capacity roadmap running full and sold out.

**Investment judgment:**
- **Stance:** cautious
- **Conviction:** low — demand, the long-term agreements (LTAs) and the margin inflection are all in primary documents, but the size of the negative skew depends on the FY2029 exit multiple and on a revenue path the company has delivered early three times in a row; with looser multiples and weights the weighted return comes close to the hurdle
- **Key catalysts:** Q1 FY2027 results (after the close on 2026-11-05, announced by the issuer), against guidance of revenue $1.225B–$1.275B, non-GAAP operating margin 39.5%–40.5% and non-GAAP EPS $4.05–$4.35; the first single OCS quarter above $100M (call) and the $400M framework for the second half of 2026; UHP lasers at about $50M per quarter by the end of 2026 (call); financial targets that may be updated at OFC 2027 (2027-03-09 to 03-11)
- **Monitoring window:** 12–18 months (through the OFC briefing's $2B per quarter target and first revenue from the Greensboro fab in early 2028)

### Key data (anchored on the 2026-10-09 close)

| Metric | Value | Basis |
|---|---:|---|
| Share price (2026-10-09 close) | $1,103.36 | Nasdaq historical endpoint, Nasdaq quote endpoint and CNBC, three endpoints agree (see appendix) |
| 52-week closing range | $149.61 (2025-10-10) – $1,133.40 (2026-10-06) | Current price -2.6% versus the closing high and 7.37x the closing low; intraday range $147.81–$1,143.00 |
| Share count, issued basis | 93,459,271 | Proxy statement record date 2026-09-24: 90,582,856 common shares + 2,876,415 Series A preferred shares held by NVIDIA (1:1 conversion) |
| Market cap, issued basis | $103.1B | $1,103.36 × 93,459,271 |
| Fully diluted share count | About 102.0M (range 102.0M–104.0M) | Adds 5.1M net new shares from the conversion value in excess of principal on the 2032 convertible notes, 0.4M from older convertible notes not yet submitted for conversion and 3.0M of unvested awards; the upper bound adds a further roughly 2.0M shares from conversions submitted but not yet settled (see Section 5) |
| Fully diluted market cap | $112.5B (upper bound $114.8B) | Valuation and the scenario grid use this basis |
| Net cash (convertible note principal treated as debt in full) | $1,091.3M | Cash and short-term investments of $2,738.4M, less convertible note principal of $1,554.3M and the Japan term loan of $92.8M (2026-06-27) |
| Enterprise value | $111.4B (upper bound $113.7B) | Fully diluted market cap less net cash |
| FY2026 revenue / Y/Y | $3,014.0M / +83.2% | 10-K |
| Q4 FY2026 revenue / Q/Q / Y/Y | $1,006.3M / +24.5% / +109.3% | Earnings release |
| Q4 non-GAAP gross margin / operating margin | 50.4% / 36.6% | Earnings release; GAAP is 47.4% / 27.8% |
| FY2026 GAAP net loss | $6,935.1M | Of which $7,756.6M is a non-cash extinguishment loss on the equitization of convertible notes (see Section 4) |
| FY2026 non-GAAP net income / EPS | $782.3M / $8.67 | Earnings release; non-GAAP tax rate 16.5% |
| Q1 FY2027 guidance | Revenue $1.225B–$1.275B; non-GAAP EPS $4.05–$4.35 | Earnings release; assumes about 102M diluted shares (earnings presentation) |
| EV / TTM revenue | 37.0x | $111.4B ÷ $3,014.0M |
| EV / annualized revenue at guidance midpoint | 22.3x | $111.4B ÷ ($1.25B × 4) |
| P/E (non-GAAP, TTM / annualized at guidance midpoint) | 127.3x / 65.7x | $1,103.36 ÷ $8.67; ÷ ($4.20 × 4). GAAP TTM EPS is negative, not applicable |
| FY2026 operating cash flow / capital expenditure / free cash flow | $751.4M / $451.3M / $300.1M | 10-K; a further $281.0M of cash paid for tax withholding on net-settled RSUs is recorded in financing activities |
| Customer concentration (FY2026) | Customer A 26.6%, Customer B 15.0% | 10-K; names not disclosed |

This report carries the `architecture-check` role for the optical layer. The question it answers is: **are CPO, NPO and optical switching cannibalizing pluggable modules, or stacking on top of them?** Lumentum sells into both sides, so its product-line dollar milestones are the most direct reading on this question. The 2026 evidence is **additive**: the EML supply-demand gap stayed above 30% without narrowing over the same period in which UHP lasers and OCS ramped (call). This does not duplicate the architecture check in innolight-2026 — Innolight tests which light source module makers buy, silicon photonics or EML, while this report tests which path an upstream device maker allocates its wafer capacity to.

---

## 1. Business Overview and Unit Economics <!-- report-module:business -->

Lumentum was spun off from JDSU in 2015 and has since acquired Oclaro (2018), NeoPhotonics and IPG's telecom transmission product lines (2022), and Cloud Light (2023). From Q1 FY2026 the company consolidated into a single reportable segment, with revenue disaggregated by product type into two categories, Components and Systems (10-K).

### Products and revenue mix (10-K)

| Category | Includes | FY2026 revenue | Share | Y/Y | FY2026 growth drivers (10-K MD&A) |
|---|---|---:|---:|---:|---|
| Components | Laser chips, laser assemblies, line subsystems, wavelength management | $2,005.6M | 66.5% | +79.7% | Laser chips and laser assemblies were 78% of the increase, spanning intra-data-center, data center interconnect and long-haul; 200G lane speeds drove a modest rise in laser chip ASPs. The remaining roughly 22% came from data transport products |
| Systems | Optical modules, optical circuit switches, industrial lasers | $1,008.4M | 33.5% | +90.7% | Cloud optical module revenue grew more than 173% on higher unit shipments and lower ASPs; OCS contributed more than $90.0M |
| Total | | $3,014.0M | 100.0% | +83.2% | |

### Revenue by product and quarter (earnings releases, $ millions)

| Quarter (period end) | Revenue | Components | Systems | Non-GAAP gross margin | Non-GAAP operating margin | Non-GAAP EPS |
|---|---:|---:|---:|---:|---:|---:|
| Q4 FY2025 (2025-06-28) | 480.7 | 320.4 | 160.3 | 37.8% | 15.0% | $0.88 |
| Q1 FY2026 (2025-09-27) | 533.8 | 379.2 | 154.6 | 39.4% | 18.7% | $1.10 |
| Q2 FY2026 (2025-12-27) | 665.5 | 443.7 | 221.8 | 42.5% | 25.2% | $1.67 |
| Q3 FY2026 (2026-03-28) | 808.4 | 533.3 | 275.1 | 47.9% | 32.2% | $2.37 |
| Q4 FY2026 (2026-06-27) | 1,006.3 | 649.4 | 356.9 | 50.4% | 36.6% | $3.23 |
| Q1 FY2027 guidance midpoint | 1,250.0 | — | — | — | 40.0% | $4.20 |

Over four quarters revenue rose to 2.1x, and non-GAAP operating income rose from $72.3M to $368.8M. The incremental operating margin from Q3 to Q4 was 54.6% ($108.1M ÷ $197.9M). The 10-K attributes about 54% of the dollar increase in gross margin to lower unit manufacturing costs from higher utilization at its own fabs, 29% to product mix and 17% to lower amortization of acquired intangibles.

### Four growth lines and how the milestones moved (calls and OFC briefing, third-party transcripts)

| Growth line | 2026-02 (Q2 call) | 2026-03 / 05 (OFC briefing, Q3 call) | 2026-08 (Q4 call) |
|---|---|---|---|
| Company revenue milestone | Original target of $750M per quarter by mid-2026, passed one quarter early | $1.25B per quarter, then $2B per quarter, in "less than 2 years" | Q1 FY2027 guidance midpoint of $1.25B, more than a quarter early |
| EML / CW laser chips | Supply-demand gap of about 25%–30%; all EML capacity locked up under LTAs through the end of 2027 | Gap above 30%; EML unit shipments in the December 2026 quarter to grow more than 50% year over year | Gap broadly unchanged; 200G EMLs already above 25% of EML revenue and expected to exceed 50% of unit shipments by mid-2027 |
| OCS | First $10M quarter reached one quarter early; backlog above $400M, three customers | Multi-year, multi-billion-dollar purchase agreement; 2027 run rate above $1B | Unit shipments doubled sequentially; the September quarter is the first quarter above $100M; "tracking to, not ahead of" the $400M framework |
| UHP lasers (CPO) | About $50M per quarter in Q4 2026; new orders worth hundreds of millions of dollars for delivery in the first half of 2027 | First scale-up CPO shipments at the end of 2027 | About $50M per quarter by the end of 2026, unchanged; first quarter above $100M set for the March 2027 quarter; the company says it is far behind demand |
| Cloud optical modules | Up about $50M sequentially; dropped its earlier notion of a ceiling of about $250M per quarter | Up more than 40% sequentially; module gap of about 30% | Record 800G shipments; 1.6T volume shipments have begun, some using in-house CW lasers |

Every cell in the table is management's account. Only three items can be checked against filings: OCS revenue above $90.0M in FY2026, cloud optical module growth above 173%, and a modest rise in laser chip ASPs (all 10-K MD&A).

### Customers, manufacturing and supply (10-K)

- **Customers:** In FY2026 two end customers each exceeded 10% of revenue — Customer A at 26.6% (FY2025 15.4%) and Customer B at 15.0% (FY2025 16.0%); the largest customer was 30.4% of accounts receivable. Neither is named. The only naming at company level came on the Q3 call, where the CEO called Google "certainly one of our largest customers" (third-party transcript). That statement does not mean Google is Customer A.
- **Ship-to locations:** United States 20.8%, Thailand 20.8%, Hong Kong 17.2%, Mexico 14.7%, China 9.4%. Ship-to locations are often where contract manufacturers are located and do not represent end customers.
- **Manufacturing:** Own wafer fabs plus assembly and test sites plus contract manufacturers; the main sites are in the United States, Thailand, China, the United Kingdom, Slovenia and Japan. Long-lived assets by country: Thailand $450.6M, Japan $232.1M, United States $153.0M, United Kingdom $139.1M, China $129.9M. Employees number 13,757, of whom 11,916 are in manufacturing. One contract manufacturer accounts for 18.2% of inventory purchases.
- **Supply:** The 10-K names no substrate supplier. The risk language new in FY2026 is: prepayments have been made to some suppliers to secure orders; China's export restrictions on Japan "affected our substrate supply chain globally"; and a new risk on China's restrictions on exports of indium, gallium and germanium. AXT's 8-K disclosed a 6-year indium phosphide substrate capacity reservation agreement signed with Lumentum on 2026-07-26 (two deposits of $43.5M each); on Lumentum's side it was confirmed only verbally on the Q4 call, with no press release, and AXT does not appear anywhere in the 10-K.

---

## 2. Industry and Competitive Position <!-- report-module:competition -->

Indium phosphide (InP) lasers are the light source for 800G/1.6T optical modules and the core of external light sources for CPO. The chain runs: substrates (axti-2026) → epitaxy and devices (Lumentum, Coherent, Broadcom, Mitsubishi Electric, Sumitomo Electric) → modules (innolight-2026, aaoi-2026, Coherent, Lumentum's own Cloud Light) → switches and GPU systems. Lumentum both sells laser chips to module makers and makes modules itself, and the competition section of the 10-K states directly that "some of these competitors are also our customers".

### Competitive landscape

| Segment | Main participants | Share or size basis | Source |
|---|---|---|---|
| EML | Lumentum, Broadcom, Mitsubishi Electric | The three together about 72% | TrendForce, 2026-06-03; no individual shares given |
| CW-DFB | Broadcom and Sumitomo Electric lead, followed by Coherent and LandMark / LuxNet | Together about 74% | TrendForce, 2026-06-03 |
| EML + CW-DFB | Broadcom, Lumentum, Sumitomo Electric | The three together about 55% | TrendForce, 2026-06-03; different basis from the row above |
| OCS | Lumentum, Coherent, HUBER+SUHNER; Google in-house | Market above $8B in 2030, 2026–2030 CAGR above 30% | Cignal AI, 2026-07-30 |
| CPO lasers | Lumentum, Coherent | NVIDIA invested $2B in each of the two on 2026-03-02 | The two companies' 8-Ks |
| China InP chain | Yunnan Germanium, San'an, Yuanjie, Accelink, Everbright Photonics | Yuanjie's 100G EML is in commercial use | TrendForce, 2026-08-06 |

- **Position as described by the company:** The OFC briefing says Lumentum has the industry's largest InP wafer fab footprint; the CEO estimates its pump laser share at about 70%–80% and says he sees no meaningful EML competition other than Broadcom (the latter statement is a second-hand report of the 2026-08-27 Deutsche Bank conference). These are all the company's account and have not been independently verified.
- **Peers are catching up:** In its 2026-08-12 results Coherent said its 6-inch InP lines in Texas and Sweden were already producing EMLs, CW lasers and photodiodes, that it plans to more than double internal InP output again by the end of 2027, and that it puts its OCS addressable opportunity at more than $4B (SDxCentral report). Lumentum's Greensboro fab conversion also uses 6-inch InP.
- **Market size:** The OFC briefing gives an optical AI market of $18B in 2025 and more than $90B in 2030 (about 40% CAGR; sources are LightCounting, 650 Group and company estimates), and cites LightCounting for InP's share of high-speed lanes in AI data centers rising from 79% in 2025 to 91% in 2030.
- **NVIDIA's parallel transaction:** On 2026-03-02, the same day, NVIDIA bought 7,788,161 common shares from Coherent ($256.80 per share, $2B in total) under an agreement that is likewise non-exclusive and includes a multi-billion-dollar purchase commitment and capacity rights. What Lumentum obtained is not an exclusive relationship.

### Position on the AI optical chain

Lumentum differs in that it sells three things at once: light sources for pluggable modules, light sources for CPO, and optical circuit switches that bypass optical-electrical conversion. Revenue at Innolight and AAOI can only show the strength of the pluggable path; AXT shows whether substrates are short; Coherent's revenue mix is broader but its disclosure is coarser. This report therefore uses Lumentum's product-line milestones as the reading for the architecture check, which the next section sets out separately.

---

## 3. Architecture Check: Pluggables, CPO / NPO and Optical Switching <!-- report-module:competition -->

Three questions, each mapped to milestones that can be checked.

### Test one: is CPO cannibalizing pluggable light sources

| Reading | Latest value | Meaning | Source level |
|---|---|---|---|
| EML supply-demand gap | Above 30%, broadly unchanged from the prior quarter | Pluggable light sources remain short even as UHP lasers ramp | Call |
| UHP laser run rate | About $50M per quarter by the end of 2026; first quarter above $100M in the March 2027 quarter | CPO light sources are still early in the ramp, at about 5% of Q4 revenue | Call |
| Scale-up CPO shipments | Volume ramp in the second half of 2027, customer deployment in 2028 | The bulk of in-rack optics revenue falls in 2028 | Call |
| First ELS module order | Received, for delivery in the second half of 2027, small initial volume | The external light source moves up from chip to module, with a higher unit price and a lower margin than chips | Call |

Conclusion: as of August 2026 it is additive, not substitutive. CPO light sources are still less than one-tenth of company revenue in dollar terms, so it is too early to call "cannibalization"; the real test point comes after scale-up shipments begin in the second half of 2027, when the question is whether the EML gap narrows with them.

### Test two: is silicon photonics displacing EML

Management acknowledges that silicon photonics plus CW lasers has taken significant share at 1.6T and expects EML to recover at 3.2T (call). A secondary report relays the CEO as saying that EML's share of 1.6T modules has fallen from about 70%–80% to about 40%–50% while unit shipments are still growing (stock3, 2026-08-28). Lumentum's response is to sell both: it is allocating the better-than-expected output of its Japan fab to 200G CW lasers, and says its CW pricing is above market and the margin gap to EML has narrowed markedly (call). The implication for the architecture check is that a win for the silicon photonics path does not directly reduce Lumentum's wafer demand, but it widens the competitor set from three EML makers to Broadcom, Sumitomo Electric, Coherent and Chinese CW vendors.

### Test three: is optical switching replacing electrical switching

OCS revenue exceeded $90.0M in FY2026 (10-K), and guidance for the September quarter includes the first quarter above $100M (call). Cignal AI notes that the only volume application today is scale-out (TPU clusters) and that revenue is concentrated at Google — Google has an in-house OCS and has also placed purchase orders with Lumentum, Coherent and HUBER+SUHNER; scale-up (GPU) applications add on from 2028. The CEO expects to become the largest supplier in early 2027 at the customer that has an in-house source (call). OCS currently tests one customer's architecture choice, not yet an industry choice.

---

## 4. Financial Health Analysis <!-- report-module:financial -->

### Quarterly results (earnings releases, $ millions)

| Item | Q4 FY2025 | Q1 FY2026 | Q2 FY2026 | Q3 FY2026 | Q4 FY2026 | FY2026 |
|---|---:|---:|---:|---:|---:|---:|
| Revenue | 480.7 | 533.8 | 665.5 | 808.4 | 1,006.3 | 3,014.0 |
| GAAP gross margin | 33.3% | 34.0% | 36.1% | 44.2% | 47.4% | 41.7% |
| GAAP operating income (loss) | (8.4) | 6.7 | 64.3 | 174.5 | 279.3 | 524.8 |
| Non-GAAP operating income | 72.3 | 99.8 | 167.7 | 260.7 | 368.8 | 897.0 |
| Stock-based compensation and related payroll taxes | 40.0 | 46.5 | 47.9 | 46.8 | 50.1 | 191.3 |
| GAAP net income (loss) | 213.3 | 4.2 | 78.2 | 144.2 | (7,161.7) | (6,935.1) |
| Non-GAAP net income | 63.3 | 86.4 | 143.9 | 225.7 | 326.3 | 782.3 |
| Non-GAAP diluted shares (millions) | 72.0 | 78.3 | 86.1 | 95.2 | 101.1 | 90.2 |
| Operating cash flow (differenced from year-to-date figures) | 64.0 | 57.9 | 126.7 | 203.8 | 363.0 | 751.4 |
| Capital expenditure (differenced from year-to-date figures) | 53.9 | 76.2 | 83.6 | 124.7 | 166.8 | 451.3 |
| Free cash flow (derived) | 10.1 | (18.3) | 43.1 | 79.1 | 196.2 | 300.1 |

### What the $6,935.1M GAAP net loss is

The FY2026 GAAP net loss is not an operating loss. On 2026-04-07 and 2026-05-29 the company, in privately negotiated transactions with certain holders, issued about 10.6M common shares in exchange for $1,124.9M aggregate principal of its 2026, 2028 and 2029 convertible notes. Because the conversion prices of these notes ($99.29, $131.03, $69.54) were far below the share price at the time, the market value of the shares handed over exceeded principal by $7,755.1M, which was recorded as a $7,756.6M loss on debt extinguishment. The loss involves no cash, is almost entirely non-deductible for tax, and corresponds to a move within shareholders' equity: additional paid-in capital rose from $1,986.8M to $12,430.1M, the accumulated deficit widened from $861.2M to $7,796.3M, and shareholders' equity actually rose from $1,134.7M to $4,643.9M. The economic cost is not in the income statement but in the share count — see Section 5.

Q4 also includes a $296.6M income tax benefit, mainly from the release of $236.3M of valuation allowance on US deferred tax assets. Both items are excluded from the non-GAAP basis.

### Financial health matrix (2026-06-27)

| Dimension | Value | Assessment |
|---|---|---|
| Liquidity | Cash and short-term investments $2,738.4M; $400.0M revolving credit facility undrawn | Ample; cash held offshore $417.9M |
| Interest-bearing debt | Convertible notes carrying value $1,544.6M (principal $1,554.3M) + Japan term loan $92.8M | All convertible notes are classified as current liabilities because holders may convert all of them in Q1 FY2027 |
| Fair value of convertible notes | $7,607.2M, 4.93x carrying value | The portion above principal is shares to be issued, not cash to be repaid |
| Cash conversion | Operating cash flow $751.4M, 24.9% of revenue; free cash flow $300.1M, 10.0% of revenue | Free cash flow is 38% of non-GAAP net income |
| Capital intensity | Capital expenditure $451.3M, 15.0% of revenue; $166.8M in Q4 alone | Construction in progress $377.4M; unpaid equipment payables $181.4M |
| Off-balance-sheet purchase obligations | $2,354.4M, of which $2,112.5M within one year | $875.3M three quarters earlier (2025-09-27); equal to 78.1% of FY2026 revenue |
| Working capital | Receivables $520.3M (about 47 days); inventory $691.6M (about 119 days) | Receivables up $270.3M in a year, inventory up $221.5M |
| Customer advances | Deferred revenue and customer deposits $15.4M (current) + $1.4M (non-current) | The narrative that customers fund capacity to offset capital expenditure does not yet show on the balance sheet |
| Stock-based compensation | $191.3M (including payroll taxes), 6.3% of revenue | A further $281.0M of tax withholding on net-settled RSUs was paid in cash |
| Tax | Non-GAAP tax rate 16.5%; cash taxes $46.7M | $81.4M of US valuation allowance still retained |

### Red-flag check

| Item | Conclusion | Note |
|---|---|---|
| Revenue recognition | No anomaly seen | Mainly product sales; Greensboro transition supply is recognized on a net basis |
| Non-GAAP adjustments | Watch | The largest recurring exclusions are stock-based compensation of $191.3M and amortization of intangibles of $135.7M; the company itself states that many of the adjustments are recurring |
| Stock-based compensation paid in cash | **Watch** | RSU tax withholding of $281.0M was paid within financing activities, versus $41.7M a year earlier. Free cash flow of $300.1M less this leaves only $19.1M |
| Purchase obligations | Watch | Up to 2.7x in three quarters; the 10-K changed its wording on order cancellability from "generally allow" to "may allow" |
| Going concern language | Eased | The Q2 10-Q stated that holders' conversion rights "raises a substantial doubt"; the Q3 10-Q (after NVIDIA's $2B arrived) removed it; the 10-K keeps only one risk-factor sentence |
| Export compliance | Unresolved | In August 2024 the company received an administrative subpoena from BIS and a related subpoena from DOJ concerning earlier shipments to Huawei; the outcome cannot be predicted. Non-routine legal fees in FY2026 were $9.6M |
| Quality and warranty | Watch | Warranty provision of $25.9M (FY2025 $10.2M), of which $9.8M relates to legacy Cloud Light products; separately received an escrow settlement payment of $27.5M |
| Inconsistencies across filings | Minor | Equitization shares of 10.7M (the two transactions added together) versus "about 10.6M"; cash paid on conversions of $520.0M versus principal of $519.4M; impairment of assets held for sale of $12.4M versus $7.7M |

---

## 5. Capital Structure and Share Bridge <!-- report-module:financial -->

This is the part of this report that is easiest to get wrong: depending on which share count is used for market cap, the result differs by about 15%.

### Convertible notes (10-K Note 10, 2026-06-27)

| Series | Principal | Conversion price | Shares if fully converted | Maturity | Status |
|---|---:|---:|---:|---|---|
| 0.50% 2026 convertible notes | $54.8M | $99.29 | 0.55M | 2026-12-15 | In FY2026: $581.1M repurchased, $149.3M converted, $264.8M equitized |
| 0.50% 2028 convertible notes | $179.6M | $131.03 | 1.37M | 2028-06-15 | In FY2026: $31.0M converted, $650.4M equitized |
| 1.50% 2029 convertible notes | $54.9M | $69.54 | 0.79M | 2029-12-15 | In FY2026: $339.1M converted, $209.7M equitized |
| 0.375% 2032 convertible notes | $1,265.0M | $187.77 | 6.74M | 2032-03-15 | Issued 2025-09-08; no holder had submitted a conversion request as of 2026-08-14; capped call cap price $268.24 |
| Total | $1,554.3M | | 9.45M | | Fair value $7,607.2M |

All four series settle the same way: principal must be paid in cash, and the conversion value in excess of principal is paid in cash, shares or a combination of the two, at the company's election. The FY2026 precedent is that the excess was paid entirely in shares (statement of changes in equity: 6.0M shares). The 10-K says that as of 2026-08-14 the company had received early conversion requests for a cumulative $757.8M of principal; $519.4M was settled within FY2026, so this report infers that about $238.4M of it is new since the fiscal year-end, with principal to be paid in cash in Q1 FY2027 — the 10-K does not state whether the figure is cumulative, and this is an inference.

### Share bridge

| Step | Shares | Source |
|---|---:|---|
| Common shares, 2025-06-28 | 69.8M | 10-K |
| Add: shares issued in the equitization | 10.6M | Statement of changes in equity |
| Add: conversion value in excess of principal settled in shares | 6.0M | Statement of changes in equity |
| Add: award vesting, options and ESPP, less shares withheld | 2.2M | Statement of changes in equity (2.4 − 0.8 + 0.4 + 0.2) |
| Common shares, 2026-06-27 | 88.6M | 10-K; +26.9% in a year |
| Common shares, 2026-08-14 | 89.7M | 10-K cover |
| Common shares, 2026-09-24 | 90,582,856 | Proxy statement record date |
| Add: Series A preferred shares (NVIDIA) | 2,876,415 | 1:1 conversion; participates in dividends and liquidation on an as-converted basis; no redemption right |
| **Issued basis** | **93,459,271** | +33.9% versus common shares at 2025-06-28 |
| Add: net new shares from the conversion value in excess of principal on the 2032 convertible notes | 5.10M | 6.74M less 1.15M shares equivalent to principal, less a further 0.49M capped call offset (at $1,103.36) |
| Add: conversion value in excess of principal on older convertible notes not yet submitted for conversion | 0.43M | Inferred principal of about $50.9M, pro rata |
| Add: unvested awards | 3.0M | Options 0.2M, RSUs 2.0M, PSUs 0.8M (2026-06-27) |
| **Fully diluted (primary basis)** | **About 102.0M** | Consistent with the roughly 102M diluted shares assumed in the company's Q1 FY2027 guidance |
| Add: conversion value in excess of principal on conversions submitted but not yet settled | About 2.0M | If these shares had not yet been issued at 2026-09-24 |
| **Fully diluted (upper bound)** | **About 104.0M** | The scenario grid's FY2029 share count of 107.5M starts from here |

Three notes. First, the roughly 2.0M shares between the primary basis and the upper bound cannot be resolved from disclosed documents and must wait for the Q1 FY2027 10-Q. Second, the enterprise value calculation has to match the share count: this report deducts the full $1,554.3M of convertible note principal from cash as debt and counts only the conversion value in excess of principal in the diluted share count; on the basis used in the peer-comparison table instead (issued shares, convertible notes as debt at carrying value), enterprise value is $102.0B, which would miss about $6B of excess conversion value on the convertible notes. Third, the capped call covers only the band from $187.77 to $268.24, is worth about $542.1M, and offsets about 0.49M shares at the current price.

### NVIDIA's preferred shares

On 2026-03-02, NVIDIA subscribed for 2,876,415 shares of Series A convertible preferred stock at $695.31 per share, $2.0B in total. Terms (8-K and 10-K Note 14): converts 1:1 into common stock, subject to expiry of the HSR waiting period; participates in dividends and liquidation on an as-converted basis; votes on an as-converted basis except in the election of directors; no preemptive rights and no redemption rights. The joint press release also says the agreement is non-exclusive and multi-year and includes a "multi-billion" purchase commitment from NVIDIA and future capacity rights for advanced laser components. **The amount, term, pricing and consequences of default of the purchase commitment are all undisclosed**; not a single 10-K risk factor mentions NVIDIA, the proxy statement does not mention NVIDIA anywhere (its as-converted holding is 3.08%, below the 5% disclosure threshold), and the related-party transactions section says "no transactions".

At the 2026-10-09 close this holding is worth about $3.17B, +58.7% versus cost. Economically it is common stock, and this report includes it in the issued basis.

---

## 6. Management, Governance and Capital Allocation <!-- report-module:management -->

- **Management:** Michael Hurlston has been President and CEO since February 2025; he was previously CEO of Synaptics (2019–2025) and CEO of Finisar (2018–2019), and worked at Broadcom (2001–2017). CFO Wajid Ali has held the role since February 2019 and was previously CFO of Synaptics. Wupen Yuen has been President, Global Business Units since September 2025 and came from NeoPhotonics.
- **Personnel changes:** Chief Accounting Officer Matthew Sepe stepped down on 2026-02-06 and was succeeded by Eric Chang (8-K, 2026-01-05). EVP Vincent Retort gave notice of retirement on 2026-07-27, effective 2026-10-02, after which he provides consulting services for two years, during which unvested awards continue to vest on the original schedule (8-K, 2026-07-30). Director Isaac Harris also served as interim Chief Procurement Officer from 2025-12-05 to 2026-05-31; the proxy statement's explanation is "the departure of certain key supply chain personnel".
- **Board:** At the record date 8 of 9 directors are independent; the independent chair and CEO roles are separate; all directors stand for election annually; majority voting (proxy statement). The 2026 annual meeting (2026-11-18) has only three routine proposals, with none to increase authorized shares, add to the equity plan or amend the charter.
- **Compensation:** CEO total compensation for FY2026 was $15,392,731 (FY2025: $27,670,076, including sign-on compensation); the pay ratio is 1,478:1; the last say-on-pay vote received 88.3% support. The annual bonus paid at 186.3% of target; the FY2024 PSUs and the FY2026 EPS PSUs both paid at the 200% cap — the FY2026 adjusted EPS target was $4.55 and the actual was $8.67. Hedging and pledging are prohibited.
- **Capital allocation:** No shares were repurchased in FY2026. Funding came from the NVIDIA preferred stock ($1,999.7M) and net proceeds of the 2032 convertible notes ($1,254.7M); uses were the repurchase of 2026 convertible notes ($843.1M), cash paid on conversions ($520.0M), the capped call ($102.0M), capital expenditure ($451.3M) and the acquisition of the Greensboro fab ($38.0M). In March 2026 it sold two San Jose properties for $43.0M with a short-term leaseback.

### Insider transactions since the start of 2026 (all 65 Form 4s, every transaction block parsed)

| Reporting person | Role | Open-market shares sold | Weighted average price | Amount | % of opening direct holdings | 10b5-1 |
|---|---|---:|---:|---:|---:|---|
| Vincent Retort | EVP (retired 2026-10-02) | 95,979 | $723.63 | $69.45M | 65.1% | Yes, plan dated 2025-11-13 |
| Wajid Ali | CFO | 32,331 | $982.62 | $31.77M | 43.5% | Yes, two plans |
| Wupen Yuen | President, Global Business Units | 21,174 | $854.29 | $18.09M | 22.3% | Yes, two plans |
| Jae Kim | General Counsel | 18,625 | $872.17 | $16.24M | 48.5% | Yes |
| Brian Lillie | Director | 12,000 | $981.73 | $11.78M | 46.3% | Yes |
| Penny Herscher | Board Chair | 8,849 | $563.42 | $4.99M | 81.1% of direct holdings | **No**; 39,378 shares held in trust untouched |
| Isaac Harris | Director | 5,416 | $896.62 | $4.86M | 49.0% | Yes, plan dated 2026-02-27 |
| Ian Small | Director | 3,500 | $911.17 | $3.19M | 11.9% | **No** |
| Pamela Fletcher | Director | 3,155 | $972.09 | $3.07M | 29.9% | Yes |
| Michael Hurlston | CEO | 548 | $958.66 | $0.53M | 0.4% | Checkbox not ticked; footnote says under a plan |
| **Total** | | **201,577** | **$813.38** | **$163.96M** | | Open-market purchases: 0 |

- **Sales only, no purchases:** From the start of 2026 through 2026-10-01, Section 16 insiders sold 201,577 shares for $163.96M in the open market and made no purchases at all (code P is zero). The shares sold are 0.22% of common shares at the record date. A further 216,951 shares, about $190.83M, were dispositions for tax withholding at vesting (code F), not market sales.
- **After the Q4 results:** Since 2026-08-11, 99,496 shares have been sold for $90.55M, all by five executives — Retort $37.91M, Ali $25.73M, Yuen $13.33M, Kim $13.05M, Hurlston $0.53M. Of these, Yuen sold 500 shares every day for 27 consecutive trading days starting 2026-08-21.
- **Inconsistencies to record, with no inference about motive:** The CEO's Form 4 of 2026-08-27 did not tick the 10b5-1 box, but the footnote and the same-day Form 144 both say the sale was under a plan adopted on 2026-05-28. The PSU certification of 2026-08-17 for five executives was not reported until 8 business days later, and the proxy statement's late-filing list includes only Harris's three reports. Former Chief Accounting Officer Sepe filed three Form 144s (10,429 shares, $7.95M) with no corresponding Form 4.
- **Adjacent dates, stated only:** Harris's plan adoption date and one of Ali's sales under a plan both fall on 2026-02-27, the trading day before the NVIDIA transaction 8-K (2026-03-02); Ali's plan was adopted on 2025-11-28.
- **Institutional holdings:** FMR went from 9,611,274 shares (13.5%) at 2025-12-31 to 3,611,652 shares (4.6%) at 2026-06-30, a 62% reduction in six months. The only holders above 5% listed in the proxy statement are Vanguard Capital Management and BlackRock, at 5.8% each.

---

## 7. Bull Case <!-- report-module:bullBear -->

1. **The constraint is real, and customers are paying for it.** All EML capacity is locked up under LTAs through the end of 2027, with room for price adjustments; pump laser agreements are mostly three-year and most carry take-or-pay terms; management mentioned price increases on some products on all three calls, Q2, Q3 and Q4 (call). The corroboration on the 10-K side is the rise in laser chip ASPs and purchase obligations rising to 2.7x in three quarters.
2. **The company has delivered its own targets early three times in a row.** $750M per quarter came one quarter early, $1.25B per quarter more than a quarter early, and the 50% non-GAAP gross margin originally tied to a $2B per quarter run rate was reached at $1.0B per quarter. The Q1 FY2027 operating margin guidance (39.5%–40.5%) is already above the top of the range for the $1.25B tier in the OFC model (33%–37%).
3. **Operating leverage is not yet used up.** Non-GAAP R&D and SG&A combined fell from 25.0% of revenue in FY2025 to 16.2% in FY2026; the incremental operating margin from Q3 to Q4 was 54.6%. The CFO said that at $2B per quarter, 42% should be seen as the midpoint of the range rather than the top (call).
4. **All three new growth lines are still early.** OCS was only $90M-plus in FY2026, against a management-stated 2027 run rate above $1B; UHP lasers are at about $50M per quarter by the end of 2026, and the bulk of scale-up CPO falls in 2028; 1.6T modules have only just entered volume production. The OFC briefing says the new growth lines are 60% of revenue at $2B per quarter, versus 25% at the Q3 FY2026 guidance midpoint.
5. **Greensboro is capacity outside the roadmap.** An existing fab bought from Qorvo for $38.0M in cash on 2026-03-17 and being converted to 6-inch InP; the OFC briefing puts its annual revenue capacity at $5B, with first revenue in early 2028 and full utilization from the end of 2028 into 2029 (call). It is not included in the $2B per quarter target.
6. **The balance sheet problem has been resolved.** Four quarters ago convertible notes were carried at $2,506.2M against cash and short-term investments of $877.1M; now convertible note principal is $1,554.3M against cash and short-term investments of $2,738.4M, and $1,265.0M does not mature until 2032 (holders can convert now, but none had submitted a request as of 2026-08-14). The going concern language has disappeared from the notes to the financial statements.
7. **The most important customer is also a shareholder.** NVIDIA subscribed for $2.0B at $695.31 and committed to purchases, and the Greensboro press release names NVIDIA as a customer of that fab.

The bull case in numbers is in Section 10: FY2029 revenue of $16.0B, a 46% operating margin and 28x give $1,654.86 per share, +16.0% annualized.

---

## 8. Bear Case <!-- report-module:bullBear -->

1. **The price has already paid for the whole roadmap.** For the current price to deliver an 8% annualized return over 2.72 years, it needs FY2029 revenue of about $13.8B, a 44% operating margin and a 28x exit; the framework the company has formally disclosed is $2B per quarter ($8B annualized) plus $5B from Greensboro at full utilization, about $13B in total. No margin of safety is left for delays, price cuts or multiple contraction.
2. **Share dilution is a real cost, and it is not over.** Common shares rose 26.9% in a year, or 33.9% including the preferred. The non-GAAP EPS denominator rose from 72.0M to 101.1M. On a fully diluted basis about 8.5M–10.5M shares are still to be issued. FY2026 free cash flow of $300.1M was almost entirely offset by RSU tax withholding of $281.0M.
3. **Customer concentration is rising, and customers will build their own.** Customer A rose from 15.4% to 26.6%, and the largest customer is 30.4% of accounts receivable. The 10-K explicitly says customers may develop products themselves; the main OCS buyer has its own in-house version (Cignal AI); the 1.6T ramp depends on one leading hyperscale customer's custom AI clusters (call).
4. **Supply is expanding across the whole industry at the same time.** Lumentum itself plans to grow EML unit shipments by more than 50% and add a fab with $5B of annual capacity; Coherent's 6-inch InP lines are in production and it plans to double again; TrendForce says combined monthly EML and CW-DFB capacity doubles in 2026 to about 50.7 million units. The last industry-wide capacity expansion in optical components was followed by the FY2023–FY2024 inventory digestion — the 10-K itself states that through FY2024 the company experienced large swings in demand and underutilized capacity.
5. **Silicon photonics weakens EML pricing power.** Management acknowledges that silicon photonics plus CW has taken significant share at 1.6T; CW has more competitors (Broadcom, Sumitomo Electric, Coherent and Chinese vendors). Whether Lumentum's CW premium is sustainable cannot be verified against any third-party price series.
6. **Key contract terms cannot be seen.** The amount and terms of NVIDIA's purchase commitment, the counterparty and terms of the "multi-year, multi-billion-dollar" OCS agreement, and the accounting treatment of the AXT agreement on Lumentum's side appear in no Lumentum filing. Customer advances on the balance sheet are only $16.8M.
7. **Insiders and a former 13.5% holder are selling.** Insiders sold a net $163.96M in 2026 with zero purchases; FMR cut its holding by 62% in six months; the average sell-side price target compiled by MarketBeat, $1,078.75, is already below the current price (second-hand data).
8. **The China supply chain is a two-way risk.** The 10-K adds two statements, one that China's export restrictions on Japan affected the substrate supply chain and one on export restrictions on indium, gallium and germanium; the newly signed AXT agreement places part of the substrate supply with a supplier that needs shipment-by-shipment licenses from China's Ministry of Commerce (see axti-2026); the Huawei business has stopped completely and the BIS / DOJ investigation is not closed.

The bear case in numbers: FY2029 revenue of $7.5B, a 33% operating margin and 18x give $378.36 per share, -32.5% annualized.

---

## 9. Key Uncertainties and Thesis-Breaking Events <!-- report-module:uncertainties -->

1. **Fully diluted share count.** Known: 93,459,271 shares at the record date (including the preferred); convertible note principal of $1,554.3M; cumulative conversion requests of $757.8M as of 2026-08-14. Unknown: how many of the shares for the conversion value in excess of principal had been issued before 2026-09-24. Confirmation: the convertible note balance and share count in the Q1 FY2027 10-Q.
2. **Who Customer A is, and whether it is the same customer for OCS and 1.6T.** Known: 26.6% of revenue and 30.4% of receivables. Unknown: its identity, and its relationship to NVIDIA's purchase commitment. There is no route to confirmation unless the company names it.
3. **The size and binding force of NVIDIA's purchase commitment.** Known: non-exclusive, multi-year, "multi-billion". Unknown: everything else. Confirmation: if the agreement is attached to a later filing as a material contract.
4. **FY2027 capital expenditure.** Known: $166.8M in Q4 alone, purchase obligations of $2,354.4M, and a Greensboro investment of "hundreds of millions of dollars" over several years. Unknown: the full-year figure — neither the call nor the 10-K gave one. Confirmation: the Q1 call.
5. **Whether the EML gap narrows once capacity comes online.** Known: the gap is above 30%, and the unit shipment target for the December 2026 quarter is +50%. Unknown: whether demand grows in step. Confirmation: the Q2 and Q3 FY2027 calls and gross margin.
6. **The CPO timetable.** Known: scale-up volume ramp in the second half of 2027 and deployment in 2028 (call). Unknown: whether it slips again; how much NPO takes as an intermediate path. Confirmation: whether UHP lasers pass $100M in the March 2027 quarter.
7. **OCS customer breadth.** Known: three customers, two of which account for most of it (call). Unknown: whether GPU-side scale-up applications appear on schedule in 2028.
8. **The outcome of the BIS / DOJ investigation.** Known: the August 2024 subpoenas and the company's voluntary disclosure. Unknown: the range of penalties; the 10-K says the worst case includes loss of export privileges.

**Thesis-breaking conditions (upside):** The company reaches $2B per quarter with an operating margin of at least 43% before the June 2027 quarter, and gives a formal model clearly above $8B annualized at OFC 2027 — this would turn the bull case into the base case.

**Thesis-breaking conditions (downside):**
- Q1 FY2027 revenue below $1.225B, or non-GAAP operating margin below 39.5%
- OCS revenue in the second half of 2026 clearly below the $400M framework, or the 2027 run-rate target withdrawn
- The first $100M UHP laser quarter pushed out beyond the June 2027 quarter
- Non-GAAP gross margin below 47% for two consecutive quarters, while management acknowledges EML price cuts or the gap disappearing
- Any customer above 10% of revenue seeing a significant fall in its share together with a sequential revenue decline

---

## 10. Valuation Context <!-- report-module:valuation -->

This section gives ranges and assumptions, not a price target.

### Multiples (2026-10-09 close of $1,103.36)

| Metric | Fully diluted basis (primary basis, 102.0M shares) | Peer-comparison basis (93.46M issued shares, convertible notes as debt at carrying value) | Denominator |
|---|---:|---:|---|
| Market cap | $112.5B | $103.1B | |
| Enterprise value | $111.4B | $102.0B | |
| EV / TTM revenue | 37.0x | 33.8x | FY2026 revenue $3,014.0M |
| EV / Q4 annualized revenue | 27.7x | 25.3x | $1,006.3M × 4 |
| EV / annualized revenue at guidance midpoint | 22.3x | 20.4x | $1.25B × 4 |
| EV / annualized non-GAAP operating income at guidance midpoint | 55.7x | 51.0x | $1.25B × 40% × 4 = $2.0B |
| P/E, TTM non-GAAP | 127.3x | 127.3x | EPS $8.67; GAAP EPS is negative |
| P/E, Q4 annualized non-GAAP | 85.4x | 85.4x | $3.23 × 4 |
| P/E, annualized non-GAAP at guidance midpoint | 65.7x | 65.7x | $4.20 × 4; guidance assumes about 102M shares |
| Free cash flow yield | 0.27% | 0.29% | FY2026 free cash flow $300.1M |

Two cautions. Non-GAAP EPS does not deduct stock-based compensation; FY2026 stock-based compensation and payroll taxes were $191.3M, equal to 21.3% of non-GAAP operating income. "Annualized" simply multiplies one quarter by 4; for a company growing 24% sequentially it understates the next 12 months, and for a company at a cycle peak it overstates them.

### Peer comparison (2026-10-09 closes; uniform basis: cover-page share counts, convertible notes as debt at carrying value)

| Company | Market cap | EV / TTM revenue | EV / guided annualized revenue | Latest-quarter revenue Y/Y | Non-GAAP operating margin | P/E, guided annualized |
|---|---:|---:|---:|---:|---:|---:|
| Lumentum (LITE) | $103.1B | 33.8x | 20.4x | +109.3% | 36.6% | 65.7x |
| Coherent (COHR) | $61.2B | 8.8x | 6.8x | +33.8% | 21.8% | 40.1x |
| AXT (AXTI) | $4.5B | 33.3x | No guidance | +164.8% | 23.5% | No guidance |
| Applied Optoelectronics (AAOI) | $9.3B | 15.0x | 8.2x | +86.4% | Not disclosed | 148.2x |
| Fabrinet (FN) | $17.4B | 3.6x | 3.0x | +44.6% | 10.9% | 29.1x |
| Ciena (CIEN) | $63.8B | 10.7x | 9.2x | +37.0% | 22.5% | No EPS guidance |
| Credo (CRDO) | $40.7B | 25.1x | 18.8x | +114.7% | 48.2% | No EPS guidance |
| Marvell (MRVL) | $241.4B | 26.3x | 19.7x | +36.5% | 36.6% | 62.6x |
| Broadcom (AVGO) | $1,725.9B | 19.8x | 12.7x | +85.5% | 67.9% | No EPS guidance |

On guided annualized revenue, Lumentum's 20.4x is 3.0x Coherent's and in line with Credo and Marvell. The market is giving it the multiple of "a semiconductor company growing more than 100% with an operating margin near 40%", not that of an optical components company. All peer figures are recomputed from each company's latest filings rather than carried over from the anchors in this site's older reports; AAOI's cover-page share count predates the at-the-market offering program it opened on 2026-08-21, so its market cap is understated.

### Scenario grid (FY2029; exit at 2029-06-30, 2.72 years from the price anchor)

| Scenario | FY2027 / FY2028 / FY2029 revenue | FY2029 operating margin | FY2029 EPS | Exit multiple | Net cash per share | Value per share | Versus current price | Annualized | Weight |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bull | $6.6B / $11.0B / $16.0B | 46% | $57.17 | 28x | $54.15 | $1,654.86 | +50.0% | +16.0% | 30% |
| Base | $6.2B / $9.0B / $12.0B | 43% | $40.08 | 24x | $43.95 | $1,005.87 | -8.8% | -3.3% | 40% |
| Bear | $5.8B / $7.5B / $7.5B | 33% | $19.22 | 18x | $32.32 | $378.36 | -65.7% | -32.5% | 30% |
| **Weighted** |  |  |  |  |  | **$1,012.32** | **-8.3%** | **-3.1%** | 100% |

- **Construction:** EPS = revenue × operating margin × (1 − 16.5% tax rate) ÷ 107.5M shares, excluding interest income; net cash per share = existing net cash of $1,091.3M plus 38% of cumulative FY2027–FY2029 net income (the actual ratio of FY2026 free cash flow to non-GAAP net income); the 107.5M shares are the fully diluted upper bound of 104.0M plus net issuance of about 1.2% a year.
- **What the base case implies:** revenue compounds at 58.5% over three years and reaches 4.0x FY2026 in FY2029; $2B per quarter is reached in the first half of FY2028, slightly earlier than the OFC briefing timetable; FY2029 revenue is equivalent to adding $4B on top of the $8B annualized level, i.e. most of the $5B full-utilization capacity claimed for Greensboro. The base case's FY2029 EPS of $40.08 is roughly the FY2028 figure of about $40 that secondary reports say the CEO called "achievable", arriving one year late.
- **The bear case is not a collapse:** revenue is still 2.5x FY2026; it simply stops growing after FY2028, and the operating margin returns to around the Q3 FY2026 level.
- **Result:** a weighted value of $1,012.32 per share, 8.3% below the current price, -3.1% annualized, 11.1 percentage points below the 8% required return.

### Sensitivity

| Adjustment | Weighted value per share | Annualized | Gap to 8% hurdle |
|---|---:|---:|---:|
| Main grid | $1,012.32 | -3.1% | -11.1 percentage points |
| Cash conversion raised from 38% to 50% | $1,022.85 | -2.7% | -10.7 |
| FY2029 share count of 105.5M (starting from the primary basis) | $1,031.51 | -2.4% | -10.4 |
| All three exit multiples raised by 4 turns | $1,168.12 | +2.1% | -5.9 |
| Weights changed to 40 / 40 / 20 | $1,139.97 | +1.2% | -6.8 |
| Multiples raised by 4 turns each and weights of 40 / 40 / 20 | $1,310.94 | +6.5% | -1.5 |
| Deeper downside (operating margin 30%, 15x) | $986.82 | -4.0% | -12.0 |

Relaxing either the multiples or the weights alone does not clear the hurdle; relaxing both together gives +6.5%, only 1.5 percentage points short of the hurdle. This shows the negative skew holds but is not large — which is why conviction is set at low.

### What is priced in, and the expectation gap

- **What the current price requires:** the 8% hurdle price at 2029-06-30 is $1,360.72. At a 28x exit and net cash of $43.95 per share, that needs FY2029 EPS of $47.03, i.e. revenue of about $13.8B at a 44% operating margin, which is 4.6x FY2026 revenue and 2.75x the current guided annualized level.
- **What merely breaking even requires:** at a 24x exit, the current price needs FY2029 EPS of $44.14, i.e. revenue of about $13.2B at a 43% operating margin.
- **Distance from the disclosed roadmap:** $2B per quarter ($8B annualized) plus $5B from Greensboro at full utilization comes to about $13B. In other words, the current price is roughly equal to "all disclosed capacity running full and sold out in FY2029, margins holding at the top of the target range, and the market still paying 24–28x at that point".
- **Where the expectation gap lies:** this report's base case differs from the market not on direction but on pace and multiple — base-case FY2029 revenue of $12.0B is about 9%–13% below what the current price implies, while the bull case's $16.0B is about 16%–21% above it.
- **Entry price consistent with the 8% hurdle:** the weighted value discounted back to today at 8% is about $820.85, which happens to be close to the $820.59 close on 2026-08-11, before the Q4 results were released. Of the 34.5% gain since then, the session after the results (2026-08-12) contributed 13.6%; the remaining 18.3% came with no new company-level financial disclosure, in a period of sell-side initiations and price target increases (second-hand data).

---

## 11. Catalysts and Monitoring Checklist <!-- report-module:catalysts -->

### Catalyst timeline

| When | Event | Check against |
|---|---|---|
| After the close on 2026-11-05 | Q1 FY2027 results and call (announced by the issuer) | Revenue $1.225B–$1.275B; non-GAAP operating margin 39.5%–40.5%; non-GAAP EPS $4.05–$4.35; first OCS quarter above $100M |
| November 2026 | Q1 FY2027 10-Q | Convertible note balance, share count, customer concentration, purchase obligations, whether supplier deposits appear |
| 2026-11-18 | Annual meeting of stockholders | Three routine proposals |
| 2026-12-15 | 2026 convertible notes mature | Balance of $54.8M at 2026-06-27 |
| Early February 2027 | Q2 FY2027 results | EML unit shipments +50% in the December 2026 quarter; UHP lasers at about $50M per quarter; OCS $400M in the second half of 2026 |
| 2027-03-09 to 03-11 | OFC 2027 | Management says it may give new financial targets |
| Early May 2027 | Q3 FY2027 results | First UHP laser quarter above $100M |
| Second half of 2027 | Scale-up CPO volume shipments; first ELS module delivery | The key window for the architecture check |
| Early 2028 | First Greensboro revenue | The claim of $5B of annual revenue capacity starts to be tested |

### Monitoring checklist

| Item | Latest reading | Trigger | Next check |
|---|---|---|---|
| Revenue and operating margin against the target model | Q4 revenue $1,006.3M, non-GAAP operating margin 36.6%; Q1 guidance midpoint $1.25B, 40.0% | Q1 revenue below $1.225B or operating margin below 39.5%; upside: $2B per quarter at no less than 43% before the June 2027 quarter | 2026-11-05 results |
| OCS ramp | Above $90.0M in FY2026; first quarter above $100M in the September quarter (call) | Second half of 2026 clearly below $400M, or the 2027 run rate above $1B withdrawn | Q1 and Q2 FY2027 calls |
| UHP lasers and CPO | About $50M per quarter by the end of 2026; first quarter above $100M in the March 2027 quarter (call) | First $100M quarter pushed out beyond the June 2027 quarter, or scale-up shipments pushed out to 2028 | Q2 and Q3 FY2027 calls |
| EML gap, pricing and gross margin | Gap above 30%; non-GAAP gross margin 50.4% | Non-GAAP gross margin below 47% for two consecutive quarters, with the gap disappearing or price cuts appearing | Each quarter's results |
| Customer concentration | Customer A 26.6%, Customer B 15.0%; largest customer 30.4% of receivables | Any 10% customer's share falls significantly together with a sequential revenue decline; or a single customer exceeds 35% | Q1 FY2027 10-Q |
| Share count and convertible note settlement | Issued basis 93,459,271 shares; fully diluted 102.0M–104.0M | Diluted shares clearly above the roughly 102M assumed in guidance; or large early conversions of the 2032 convertible notes | Q1 FY2027 10-Q |

---

## 12. Conclusion <!-- report-module:conclusion -->

**(1) Chain test role.** This report carries `architecture-check` for the optical layer: it uses Lumentum's product-line milestones to test whether CPO / NPO and optical switching substitute for pluggable modules or stack on top of them. The reading as of August 2026 is additive — the EML gap stayed above 30% while OCS and UHP lasers ramped. That is a positive reading for innolight-2026 and aaoi-2026 (light-source demand for pluggables has not been diverted), a same-direction confirmation for coherent-2026, and for axti-2026 it shows that substrate demand comes from more than one path. The decisive window for the test comes after scale-up CPO shipments in the second half of 2027.

**(2) Expectation gap.** The business is delivering, and faster than the company's own timetable. But $1,103.36 on 2026-10-09 corresponds to a fully diluted market cap of $112.5B, 22.3x guided annualized revenue and 65.7x guided annualized non-GAAP EPS; it requires FY2029 revenue of about $13.2B–$13.8B, an operating margin of 43%–44% and an exit multiple of 24–28x, roughly equal to the entire disclosed capacity roadmap running full and sold out. This report's base case is about 9%–13% below that.

**(3) Stance and conviction.** The 30% bull / 40% base / 30% bear scenario grid weights to $1,012.32 per share, 8.3% below the current price, -3.1% annualized over 2.72 years, 11.1 percentage points below the 8% required return. The weighted loss on the bear side (about $217 per share) exceeds the weighted gain on the bull side (about $165 per share), so the skew is negative and the stance is **cautious**. The bull case returns +16.0% annualized and there is nothing wrong with the quality of the business, so it is not bearish-avoid. Conviction is **low**: raising all multiples by 4 turns and changing the weights to 40 / 40 / 20 gives +6.5% annualized, only 1.5 percentage points short of the hurdle; and this company has delivered its targets early three times in a row, while the FY2029 revenue range ($7.5B–$16.0B) is itself wide. This is a judgment on price, not a rejection of the business.

**(4) Upgrade and downgrade conditions.** Upgrade to neutral-watch: with fundamentals unchanged, the share price falls back to about $820 (the price consistent with the 8% hurdle); or the company reaches $2B per quarter with a non-GAAP operating margin of at least 43% before the June 2027 quarter and gives a formal model clearly above $8B annualized at OFC 2027. Downgrade to bearish-avoid: Q1 FY2027 revenue below $1.225B or operating margin below 39.5%; OCS in the second half of 2026 clearly below $400M or the 2027 run-rate target withdrawn; the first $100M UHP laser quarter pushed out beyond the June 2027 quarter; non-GAAP gross margin below 47% for two consecutive quarters with the EML gap disappearing or price cuts appearing; or any 10% customer's share falling significantly together with a sequential revenue decline.

---

## Appendix: Sources and Assumptions <!-- report-module:appendix -->

### Primary sources

- [FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/1633978/000162828026057358/lite-20260627.htm) (filed 2026-08-17)
- [Q4 FY2026 earnings release](https://www.sec.gov/Archives/edgar/data/1633978/000162828026055726/lite_ex991xq4fy26.htm) (8-K Exhibit 99.1, 2026-08-11); [Q3 FY2026 earnings release](https://www.sec.gov/Archives/edgar/data/1633978/000162828026030530/lite_ex991xq3fy26.htm); [Q2 FY2026 earnings release](https://www.sec.gov/Archives/edgar/data/1633978/000162828026005005/lite_ex991xq2fy26.htm)
- [Q3 FY2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1633978/000162828026030777/lite-20260328.htm); [Q2 FY2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1633978/000162828026005129/lite-20251227.htm); [Q1 FY2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1633978/000162828025049073/lite-20250927.htm)
- [NVIDIA preferred stock 8-K](https://www.sec.gov/Archives/edgar/data/1633978/000119312526085412/d41019d8k.htm) and [joint press release](https://www.sec.gov/Archives/edgar/data/1633978/000119312526085412/d41019dex991.htm) (2026-03-02)
- Equitization 8-Ks: [2026-04-08](https://www.sec.gov/Archives/edgar/data/1633978/000119312526146256/d13152d8k.htm), [2026-06-01](https://www.sec.gov/Archives/edgar/data/1633978/000119312526249535/d112771d8k.htm); personnel 8-K: [2026-07-30](https://www.sec.gov/Archives/edgar/data/1633978/000162828026051078/lite-20260727.htm)
- [2026 proxy statement DEF 14A](https://www.sec.gov/Archives/edgar/data/1633978/000130817926000420/lite2026-def14a.htm) (filed 2026-10-06)
- [Form 4 and Form 144 list](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001633978&type=4) (65 Form 4s and 56 Form 144s in 2026, each parsed individually)
- [OFC 2026 investor briefing](https://s21.q4cdn.com/377324469/files/doc_presentations/2026/2026-Lumentum-at-OFC_final.pdf) (2026-03-17); [Q4 FY2026 earnings presentation](https://s21.q4cdn.com/377324469/files/doc_financials/2026/q4/Q4-FY26-Earnings-Presentation_final.pdf)
- [Q1 FY2027 results date announcement](https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-Reporting-Date-for-Fiscal-First-Quarter-2027-Financial-Results/default.aspx) (2026-10-05)
- [AXT 8-K on the Lumentum agreement](https://www.sec.gov/Archives/edgar/data/1051627/000143774926024883/axti20260715_8k.htm); [Coherent 8-K on the NVIDIA transaction](https://www.sec.gov/Archives/edgar/data/820318/000119312526084366/d42735d8k.htm)

### Call transcripts and secondary sources

- Motley Fool transcripts: [Q4 FY2026](https://www.fool.com/earnings/call-transcripts/2026/08/18/lumentum-lite-q4-2026-earnings-call-transcript/), [Q3 FY2026](https://www.fool.com/earnings/call-transcripts/2026/05/06/lumentum-lite-q3-2026-earnings-transcript/), [Q2 FY2026](https://www.fool.com/earnings/call-transcripts/2026/02/03/lumentum-lite-q2-2026-earnings-call-transcript/). The transcripts contain obvious mishearings, and the page dates are publication dates, not call dates.
- [TrendForce, 2026-06-03](https://www.trendforce.com/presscenter/news/20260603-13077.html); [TrendForce, 2026-08-06](https://trendforce.com/news/2026/08/06/news-inp-shortage-emerges-as-ai-optical-interconnect-bottleneck/); [Cignal AI, 2026-07-30](https://cignal.ai/2026/07/ocs-market-to-top-8-billion-by-2030/); [SDxCentral, 2026-08-14](https://www.sdxcentral.com/news/coherent-q4-financials-see-supply-chain-wins-and-scale-across-opportunity/)
- The content of the Deutsche Bank conference (2026-08-27) is available only as a second-hand report: [stock3, 2026-08-28](https://stock3.com/news/lumentum-kommt-mit-dem-ausbau-seiner-produktion-kaum-hinterher-17260929). Sell-side ratings and price targets come from the [MarketBeat](https://www.marketbeat.com/stocks/NASDAQ/LITE/forecast/) summary; no original sell-side report was opened.

### Price and share-count assumptions

- 2026-10-09 close: Nasdaq historical endpoint $1,103.355, Nasdaq quote endpoint $1,103.355, CNBC $1,103.36; this report uses $1,103.36. 2026-10-11 is a Sunday, with no trading day in between.
- The issued basis of 93,459,271 shares comes from the proxy statement record date (2026-09-24). The derivation of the fully diluted primary basis of 102.0M and the upper bound of 104.0M is in Section 5.
- "The $757.8M is cumulative" is this report's inference: the Q3 10-Q disclosed $500.8M as of 2026-04-30, $519.4M was settled in FY2026, and at 2026-06-27 only $289.3M of principal remained on the non-2032 convertible notes.

### Calculation assumptions

- Net cash $1,091.3M = $2,738.4M − $1,554.3M − $92.8M; equal to $10.70 per share (102.0M shares).
- Enterprise value $111.4B = $112.5B − $1.09B; upper bound $113.7B = $114.8B − $1.09B.
- Peer-comparison basis enterprise value $102.0B = $103.1B + debt at carrying value $1,637.4M − cash $2,738.4M.
- Capped call value = 6.74M × ($268.24 − $187.77) = $542.1M, equivalent to 0.49M shares.
- Holding period of 2.72 years = 2026-10-09 to 2029-06-30.
- Days sales outstanding and days of inventory are computed on Q4 revenue and Q4 cost of sales (including amortization of intangibles), times 91 days.

### Scenario grid detail

| Item | Bull | Base | Bear |
|---|---:|---:|---:|
| FY2027 revenue / operating margin | $6,600M / 41% | $6,200M / 40.5% | $5,800M / 39% |
| FY2028 revenue / operating margin | $11,000M / 44% | $9,000M / 42% | $7,500M / 37% |
| FY2029 revenue / operating margin | $16,000M / 46% | $12,000M / 43% | $7,500M / 33% |
| FY2029 operating income | $7,360M | $5,160M | $2,475M |
| FY2029 net income (16.5% tax rate) | $6,146M | $4,309M | $2,067M |
| FY2027–FY2029 cumulative net income | $12,447M | $9,562M | $6,273M |
| Ending net cash per share (38% conversion) | $54.15 | $43.95 | $32.32 |
| FY2029 EPS (107.5M shares) | $57.17 | $40.08 | $19.22 |
| Exit multiple | 28x | 24x | 18x |
| Value per share | $1,654.86 | $1,005.87 | $378.36 |
| FY2026–FY2029 revenue CAGR | 74.4% | 58.5% | 35.5% |

### Evidence limits

- All figures for OCS, UHP lasers, the EML gap, capacity and LTAs exist only at the level of the calls or the OFC briefing; all the 10-K can corroborate is OCS above $90.0M, cloud optical module growth above 173%, the rise in laser chip ASPs and purchase obligations.
- The identities of Customer A and Customer B are undisclosed; the naming of Google comes from the Q3 call transcript and cannot be equated with Customer A.
- The amount and terms of NVIDIA's purchase commitment, the counterparty to the OCS purchase agreement, and the treatment of the AXT agreement on Lumentum's side are all undisclosed.
- The statements that FY2028 EPS of about $40 is "achievable" and that consensus is $33 come only from second-hand reports; this report does not use them as fact, only to position the scenarios.
- The Greensboro facility's floor area differs between the press release (240,000 square feet) and the 10-K (148,000 square feet); the identification of Qorvo as the seller comes from the OFC briefing, while the 10-K says only "a third party".
- The fully diluted share count carries an unresolved range of about 2.0M shares, pending the Q1 FY2027 10-Q.
- Peer multiples are not aligned by fiscal quarter: Coherent, AAOI, AXT and Fabrinet are June quarters; the rest are quarters ending in early August.
- On the Q4 call the CEO placed the first UHP laser quarter above $100M in "the third quarter"; this report reads that as the fiscal quarter, the March 2027 quarter. If the calendar third quarter was meant, the milestone is two quarters later.
