# Amazon.com (AMZN) Deep Research Report

Coverage date: 2026-02-11
Last updated: 2026-08-16
Ticker: NASDAQ: AMZN
Disclaimer: This report is for informational and research purposes only. It does not constitute investment advice. Please conduct your own due diligence.

---

## Executive Summary

> **Framework note:** This is the 2026H1 full-cycle rewrite that promotes Amazon from a standalone company file into the AI-infrastructure book's **demand-risk** layer, with the chain role of **dashboard**. The prior-cycle version is preserved unchanged at [`amzn-2026-pre-chain`](/invest/research/reports/view.html?id=amzn-2026-pre-chain). Amazon earns the dashboard role because it publishes the densest near-real-time instrument panel of any buyer in the layer: an AWS annualized run rate, a contracted backlog, a separately-quantified AI business and chips business, a mid-year capital-expenditure guide with an explicit input-cost attribution, and a trailing free-cash-flow line that has now gone negative. The core read-through is sharper than for any other demand-layer name: **AWS is simultaneously the largest single buyer of AI infrastructure and, through Trainium and Graviton, a direct competitor to the merchant silicon this book covers** — and it is funding that dual position with a trailing twelve-month free-cash-flow outflow of $7.604B against record segment profit.

**One-line thesis:** Amazon's Q2 2026 (quarter ended June 30, 2026, reported after the close on July 30, 2026) is the strongest operating print in the demand layer on every revenue and margin line — AWS $42.232B (+37%, fastest in 18 quarters) at a 39.4% segment margin, consolidated operating income $27.461B (+43%) at a record 13.7% margin, advertising +26% — and simultaneously the layer's sharpest capex-absorption warning, because trailing twelve-month free cash flow fell to **-$7.604B** while the full-year cash-capex guide was raised to about $220B with roughly $20B of the increase attributed to **higher memory prices rather than more capacity**.

**Current view:** **Constructive, medium conviction.** The valuation anchor for this report is the July 30, 2026 close of $235.50, which is the last completed US session — and it **predates the earnings release by hours**. Nothing in that price reflects the Q2 print, the $496B AWS backlog disclosure, or the raised capex guide. That is why the expectation gap in section 8 reads positive on fundamentals rather than on market reaction: this report deliberately makes no inference from after-hours or pre-market trading, which is not a completed session. Conviction is medium, not high, because three questions are genuinely unresolved: when trailing free cash flow troughs, how much of the capex step-up is input-cost inflation instead of capacity, and how to read $53.415B of Q2 other income booked on an investment in Anthropic that is simultaneously one of AWS's largest compute customers.

**2026-08-16 coverage-completeness update:** Amazon signed an agreement to acquire Globalstar on April 13, 2026. The August 13 S-4/A states that holders may elect $90 per share in cash, less the specified adjustment, or Amazon stock determined by a 20-day volume-weighted-average-price formula; support agreements cover about 57.6% of outstanding common shares and the HSR waiting period expired on July 17, 2026, while FCC, French and other international approvals and C-3-related authorisations remain pending. The transaction adds company-level satellite and spectrum optionality, but it does not currently map to an existing AI-chain crossCheck or monitoring trigger in this research book. The July 30 valuation anchor and constructive / medium-conviction stance in section 8 are unchanged.

**Quick stats:**

| Metric | Value |
|--------|-------|
| Share price | $235.50 (Jul 30, 2026 close, Nasdaq official / yfinance); **anchor predates the after-close earnings release** |
| July 2026 price path | $254.96 (Jul 15) → $226.65 (Jul 29), a -11.1% drawdown, then +3.9% to $235.50 on Jul 30 (100.9M shares, ~2.5x the month's typical volume) |
| 52-week closing range | $198.79 (2026-02-13) – $274.99 (2026-05-06); intraday range $196.00 – $278.56 |
| Market cap / shares | About $2.539T; 10.783B common shares outstanding at Jun 30, 2026 (Q2 diluted weighted average 10,903M) |
| Latest reported period | 2026 Q2, quarter ended 2026-06-30 (reported 2026-07-30, after the close) |
| Q2 revenue / YoY | $200.606B, +20% (+20% ex-FX; FX contributed $0.1B) |
| Q2 operating income / margin | $27.461B, 13.7% — a record quarterly operating margin, +43% YoY |
| Q2 net income / diluted EPS | $62.647B / $5.75, including **$53.415B of non-operating other income, primarily Anthropic investment marks** — not a clean operating-earnings measure |
| AWS | Q2 revenue $42.232B, +37% (+36.7% precisely), fastest in 18 quarters; $169B annualized run rate; operating income $16.621B at a 39.4% segment margin |
| AWS trailing twelve months | Revenue $148.404B (+28%); operating income $54.681B (+28%); TTM segment margin 36.8% |
| Advertising | Q2 $19.809B, +26% — the fastest advertising growth since Q1 2025; TTM $76.072B |
| TTM operating cash flow | $161.403B, +33% YoY |
| TTM PP&E purchases, net of proceeds and incentives | $169.007B, +64% YoY (a $66.1B year-over-year increase) |
| TTM free cash flow | **-$7.604B**, versus +$18.184B a year earlier and +$11.194B at FY2025 year end |
| Balance sheet | Cash $78.213B + marketable securities $44.775B = $122.988B; long-term debt $128.894B; long-term lease liabilities $94.338B |
| Q3 2026 guidance | Revenue $197.0B–$202.0B (+9% to +12%; nearly 400bp higher excluding Prime Day timing); operating income $22.5B–$26.5B |
| Chain role | demand-risk **dashboard**: buildout velocity, order quality, and input-cost mix read in near real time |

## 1. Business Overview

Amazon reports three segments, and in 2026 the gap between them has become the whole story: AWS is 21% of revenue and 61% of operating income, while the two retail segments supply the cash and the customer base that let Amazon fund an AI build no pure-play cloud vendor could carry.

| Segment | Q2 2026 revenue | YoY | Q2 operating income | Q2 margin | TTM revenue | TTM operating income | TTM margin |
|---------|-----------------|-----|---------------------|-----------|-------------|----------------------|-----------|
| North America | $116.177B | +16% | $9.123B | 7.9% | $453.670B | $33.651B | 7.4% |
| International | $42.197B | +15% | $1.717B | 4.1% | $173.606B | $5.380B | 3.1% |
| AWS | $42.232B | +37% | $16.621B | 39.4% | $148.404B | $54.681B | 36.8% |
| **Consolidated** | **$200.606B** | **+20%** | **$27.461B** | **13.7%** | **$775.680B** | **$93.712B** | **12.1%** |

Underneath the segments, the seven disclosed revenue lines show where growth actually came from. Every line accelerated in Q2, which is unusual and matters for the chain read: this was not an AWS-only quarter propped up by a weakening retail base.

| Revenue line | Q2 2026 | YoY (ex-FX) | Q1 2026 YoY | Comment |
|--------------|---------|-------------|-------------|---------|
| Online stores | $70.432B | +15% | +9% | Sharpest first-party retail acceleration in two years |
| Third-party seller services | $46.780B | +16% | +12% | Seller unit mix held at 61% of paid units |
| AWS | $42.232B | +37% | +28% | Fifth consecutive quarter of acceleration |
| Advertising services | $19.809B | +26% | +22% | Highest growth rate of the six disclosed quarters |
| Subscription services | $13.730B | +12% | +12% | Prime annuity, steady |
| Physical stores | $5.794B | +4% | +4% | Immaterial to the thesis |
| Other | $1.829B | +23% | +25% | Includes shipping and healthcare services |

Two structural points distinguish Amazon inside the demand-risk layer.

**First, the funding stack is retail-subsidised and now debt-assisted.** Trailing operating cash flow of $161.403B is the largest in the layer, but it no longer covers the build: net PP&E purchases of $169.007B exceeded it by $7.604B. The gap has been bridged with debt. Trailing twelve-month proceeds from long-term debt were $81.925B against $5.022B of repayments, and long-term debt roughly doubled from $65.648B at 2025 year end to $128.894B at June 30, 2026 — including the roughly $24.9B multi-tranche senior unsecured issuance completed on 2026-07-09, which the prospectus supplement designates for general corporate purposes rather than earmarking for AI infrastructure.

**Second, Amazon is the only demand-layer name that is also a supply-side substitute.** Per the release, the chips business exceeded a $25B annual revenue run rate growing at triple-digit percentages — up from the roughly $10B Trainium-plus-Graviton run rate disclosed in the prior cycle. Graviton5 reached general availability, is used by 98% of the top 1,000 EC2 customers, delivers up to 30–40% better price-performance than comparable instances and up to 25% better compute than Graviton4, and its revenue commitments rose nearly 3x quarter over quarter. On Trainium, the release states that Anthropic and OpenAI — the two largest model labs — have each made multi-year, multi-gigawatt commitments. That is the strongest own-silicon datapoint the book has recorded, and it cuts against the merchant-silicon layer at the same time as Amazon's capex validates it.

**Third, the pending Globalstar acquisition adds satellite and spectrum optionality but is not an existing AI-chain signal.** The August 13, 2026 S-4/A records an April 13 agreement under which holders may elect $90 per share in cash, less the specified adjustment, or Amazon stock determined by a 20-day VWAP formula, with stock consideration capped at $90 per share; support agreements cover 74,058,249 shares, about 57.6% of 128,598,125 outstanding common shares. The filing also says the maximum Apple C-3 milestone payment was reduced from $110M to about $97M. The HSR waiting period has expired, but FCC, ANFR, ARCEP and other approvals, C-3 authorisations and closing remain outstanding, leaving final consideration and timing conditional. No AI-infrastructure customer, procurement or capacity commitment is disclosed, so this report creates no crossCheck or monitoring item from the transaction.

## 2. Industry & Competitive Position

Amazon competes on three maps this book cares about, and its position on each moved in Q2.

**Hyperscale cloud.** AWS grew 36.7% to a $169B annualized run rate. That is a lower growth rate than Microsoft's Azure (+43% in the quarter ended June 30, 2026) but on a substantially larger base: AWS TTM revenue of $148.404B against Azure's fiscal-2026 revenue just above $100B. AWS's contracted backlog reached $496B growing at triple-digit percentages, per earnings-call coverage — roughly 3.3x TTM AWS revenue, versus Microsoft's commercial RPO of $678B at roughly 2x total company revenue and Oracle's RPO of $638B. Management said on the call that 2027 capacity is already largely reserved and that some 2028 capacity is spoken for, and that even at about $220B of 2026 capex Amazon expects to be short of capacity in both 2026 and 2027.

**AI-infrastructure chain position.** This is where the dashboard role earns its name. Amazon's disclosures map onto the book's layers more directly than any other buyer's:

| Chain layer | What Amazon's Q2 disclosure says | Read-through to existing coverage |
|-------------|----------------------------------|-----------------------------------|
| GPU / accelerators | Net PP&E of $53.076B in the quarter alone; AWS AI business above a $25B run rate | Supports NVIDIA/AMD demand, but see custom silicon below — the direction of the read is ambiguous for the first time |
| Custom silicon | Chips business above a $25B run rate at triple-digit growth; Trainium commitments reported above $225B; OpenAI committed to roughly 2 GW of Trainium ramping from 2027 and Anthropic to as much as 5 GW (call coverage) | Direct pressure on merchant-GPU share; the strongest architecture-substitution evidence in the book, and a cross-check on Broadcom's custom-ASIC thesis |
| Memory / HBM | The entire $20B capex raise ($200B to $220B) attributed to higher memory prices (call coverage); the release's guidance risk factors name "resource and supply volatility, including for memory chips", but that is standing language carried unchanged from the FY2025 10-K, so it corroborates nothing about this quarter | Confirms memory tightness for Micron/SK hynix/SanDisk — **and simultaneously shows that hyperscaler capex dollars can rise on price rather than volume** |
| Power / facilities | Capex guide about $220B for 2026; capacity short through 2027 | Supports Constellation, Vistra, GE Vernova, Vertiv, Equinix and Digital Realty demand reads |
| Networking / optical | AI cluster buildout at this scale drives Ethernet and optical volumes | Second-order support for Arista, Broadcom, Coherent, Corning |
| Neocloud | AWS capacity sold out through 2027 leaves headroom for third-party capacity | Reduces the bear case that hyperscalers dump capacity onto CoreWeave/Nebius |

**Retail and advertising.** Amazon holds roughly 37–40% of US e-commerce, and Q2 showed the retail flywheel re-accelerating rather than decaying: paid units +17%, online stores +15%, over 40% more items delivered same-day or overnight in the first half. Advertising at $19.809B (+26%) is now the third-largest US digital advertising platform behind Google and Meta and grew faster in Q2 than Meta's overall business. Worldwide shipping costs of $27.873B grew 19%, slightly above unit growth, which is the main retail-margin watch item.

Competitive risk is real but currently second-order: Azure grew faster in percentage terms, Alphabet's quarterly capex of $44.9B (logged in this hub's signal ledger on 2026-07-22) shows no retreat, and Google's TPU stack is the closest analogue to Trainium. Amazon's counter is scale of installed base plus the fact that it is the only one of the three selling its own silicon capacity to rival labs.

## 3. Financial Analysis

The income statement is the best in the layer. The cash-flow statement is the worst. Both are true, and the report is about the distance between them.

| Metric | Current readout | Interpretation | Grade |
|--------|-----------------|----------------|-------|
| Revenue growth | Q2 $200.606B, +20%; TTM $775.680B, +16% | Acceleration at a $775B base, with all seven revenue lines up | A |
| Operating margin | Q2 13.7% (record); TTM 12.1% vs 11.4% a year earlier | Margin expanded through the largest capex program in the company's history | A |
| AWS segment economics | Q2 margin 39.4%, operating income +64% YoY; TTM margin 36.8% | The margin recovered from the 32.9% trough of Q2 2025 — but D&A from the current build has not fully landed | A− |
| Net income quality | Q2 $62.647B / $5.75 diluted, of which $53.415B is non-operating other income; TTM net income $135.281B, TTM diluted EPS $12.44 | GAAP earnings are dominated by investment marks. Q2 operating income of $27.461B is the honest number; TTM GAAP P/E is not decision-useful | D |
| Free cash flow | TTM OCF $161.403B − net PP&E $169.007B = **-$7.604B**; a year earlier +$18.184B | The single most important negative datapoint in the demand layer. Capex is 2.25x trailing D&A of $75.200B | Caution |
| Capital expenditure | Q2 net $53.076B (+22.8% sequentially from $43.234B in Q1); TTM net $169.007B = 21.8% of revenue; 2026 cash-capex guide about $220B | Capex intensity has roughly doubled in two years; the guide raise is partly price, not capacity | Caution |
| Balance sheet | Cash + securities $122.988B; long-term debt $128.894B; long-term lease liabilities $94.338B | Narrow net debt $5.906B; including long-term leases, net debt is about $100.2B — a materially different funding picture | B− |
| Order book | AWS backlog $496B growing triple-digit percentages (call coverage) | Roughly 3.3x TTM AWS revenue; the visibility argument for the capex | A− |
| Shareholder returns | No dividend, no buyback; Q2 stock-based compensation $6.038B, TTM $19.314B (2.5% of revenue); shares outstanding +1% YoY | All cash goes to the build. Dilution is controlled but there is no return cushion | C+ |
| Headcount and unit economics | 1,595,000 employees (+3%); paid units +17%; shipping costs $27.873B (+19%) | Retail is levering: units grew 17% on 3% more people | A− |

**The cash bridge, stated precisely.** The $220B figure and the $169.007B figure are on **different bases** and must not be differenced:

| Cash line (release, TTM or period as marked) | Amount | Basis |
|---|---|---|
| Purchases of property and equipment, TTM | $173.028B | Gross |
| Proceeds from PP&E sales and incentives, TTM | $4.021B | Offset |
| **Purchases of PP&E, net — TTM** | **$169.007B** | The release's own free-cash-flow definition |
| Purchases of PP&E, net — six months 2026 | $96.310B | Of which Q1 $43.234B, Q2 $53.076B |
| Property and equipment acquired under finance leases, TTM | $4.048B | Non-cash, excluded above |
| Increase in PP&E acquired but not yet paid, TTM | $29.267B | Working-capital timing, excluded above |
| Full-year 2026 **cash capex** guide (call coverage) | about $220B, raised from about $200B | Company-defined cash capex; **not** the net-of-proceeds line |
| Depreciation and amortisation, TTM | $75.200B | Capex is 2.25x D&A |
| Acquisitions, non-marketable investments and other, net — TTM | $41.956B | Includes $24.359B in Q2 alone |

The last two rows carry the two forward risks. Capex running at 2.25x depreciation means reported AWS margin is being flattered by an asset base that has not yet been expensed; the 39.4% segment margin is a pre-wave number. And $41.956B of trailing non-marketable investment outflow — $24.359B of it in Q2 — is the cash side of the AI-lab stake complex whose paper gains dominate the income statement.

**The Anthropic complex: what is disclosed and what is inferred.** Disclosed: Q2 non-operating other income of $53.415B, which the release attributes as "primarily from our investments in Anthropic"; Q2 provision for income taxes of $18.199B and deferred income taxes of $17.691B, reflecting the tax on those marks; TTM non-operating income of $79.818B. Separately disclosed but **not attributed by the company**: an available-for-sale debt-securities unrealised gain of $41.988B net of $13.695B of tax inside other comprehensive income for Q2, and an increase in "Other assets" from $122.607B to $284.132B over six months. Our inference — labelled as inference — is that the OCI line cannot be the ordinary treasury book, since the entire marketable-securities balance is $44.775B, and that it belongs to the same non-marketable investment complex. We deliberately do **not** publish a summed "Anthropic gain" figure, because only the $53.415B carries company attribution.

The consequence is visible in equity: stockholders' equity rose from $411.065B to $551.620B in six months, of which $38.057B came from accumulated other comprehensive income rather than from operations. Book value and GAAP EPS are both being inflated by marks on private AI-lab positions.

**Demand-risk layer peer comparison** (each column at its own reported period; not restated):

| Metric | Amazon (Q2 2026, Jun-30) | Microsoft (FY26 Q4, Jun-30) | Meta (Q2 2026, Jun-30) | Oracle (FY26 Q4, May-31) | Alphabet (Q2 2026) |
|--------|--------------------------|------------------------------|------------------------|--------------------------|--------------------|
| Quarterly capex | $53.076B net PP&E | $41B incl. finance leases | $31.078B | FY2026 total $55.66B | $44.9B |
| Quarterly operating cash flow | $45.387B | $55.4B | $31.862B | — | — |
| Free cash flow | **TTM -$7.604B** | FY ~$67.0B | Q2 $0.784B (−91% YoY) | FY2026 −$23.69B | — |
| Order book | AWS backlog $496B (call) | Commercial RPO $678B | n/a | RPO $638B | n/a |
| Cloud/AI growth | AWS +37% | Azure +43% | n/a | OCI backlog-led | Cloud accelerating |
| External financing | TTM $81.925B long-term debt proceeds | None (net cash) | None | ~$40B debt+equity planned | None |

Amazon sits between Microsoft (absorption proven) and Oracle (absorption not proven, balance sheet strained): the largest absolute cash generation in the group, and the second-worst free-cash-flow line.

**Red-flag check:**

| Red flag | Current status | What to re-check |
|----------|----------------|------------------|
| Negative trailing free cash flow | -$7.604B TTM, from +$11.194B at FY2025 year end and +$25.925B at Q1 2025 | Whether the trough is Q2/Q3 2026 or extends into 2027; the Q3 and Q4 net PP&E lines |
| Capex raise driven by input price | About $20B of the 2026 raise attributed to higher memory prices (call coverage) | Any unit-versus-price split; whether 2027 guidance embeds further memory inflation |
| Earnings quality | $53.415B of Q2 net income is non-operating; TTM GAAP EPS $12.44 versus TTM operating income $93.712B | Direction of marks in Q3; these reverse as readily as they accrue |
| Counterparty circularity | Anthropic is simultaneously Amazon's largest investment mark and a Trainium customer committing up to 5 GW | Any disclosure of the carrying value, the commitment terms, or related-party revenue |
| Leverage understated by narrow definitions | Narrow net debt $5.906B versus about $100.2B including $94.338B of long-term lease liabilities | Lease growth: assets acquired under operating leases were $24.897B TTM |
| Depreciation wave | Net capex is 2.25x TTM D&A of $75.200B; PP&E net rose from $357.025B to $446.046B in six months | Whether AWS margin holds above 35% as the current build starts depreciating |
| Q3 revenue guide below Q2 | $197.0B–$202.0B midpoint $199.5B versus Q2's $200.606B | Prime Day timing explains it — growth is nearly 400bp higher excluding it; verify in the Q3 actuals |

## 4. Management & Governance

Andy Jassy's record is the AWS franchise itself, and Q2 is the strongest evidence yet that the 2026 capital plan is being executed rather than merely announced. The governance question is not competence; it is disclosure symmetry.

Three items warrant monitoring. **First, the capex guide's basis and attribution.** Management raised 2026 cash capex to about $220B from about $200B and attributed the increase to higher memory prices, per earnings-call coverage (CNBC, Seeking Alpha and Fortune independently report the figure and the attribution). Jassy's stated position is that "even at that amount, we will still not have enough capacity to meet all the demand we have in 2026, and I believe this dynamic will also be true in 2027 too," with 2028 demand described as striking. That is candid about capacity, but the release itself publishes neither the capex total nor the memory attribution — the shareholder who reads only the 8-K exhibit does not learn that the entire increase — roughly a tenth of the year's total investment — buys no incremental capacity. The release's guidance risk factors do name "resource and supply volatility, including for memory chips," but that is standing wording carried unchanged from the FY2025 10-K, so the primary document adds nothing about this quarter.

**Second, the Anthropic position.** Amazon books $53.415B of income from marking an investment in a company that has committed to as much as 5 GW of Trainium capacity. Both directions of that relationship are defensible individually; together they mean the largest single line in Q2 net income and one of the largest lines in the AWS backlog reference the same counterparty. The release does not disclose the carrying value, the ownership percentage, or any related-party revenue split. Compare Microsoft, which at least disclosed in January 2026 that roughly 45% of its then-$625B RPO was OpenAI-linked. Amazon has published no equivalent concentration figure for the $496B backlog.

**Third, capital returns remain zero** — no dividend, no buyback, for a third consecutive year — while long-term debt doubled in six months. That is internally consistent with a capacity-constrained build and is not a criticism, but it removes the shareholder-return cushion that Microsoft ($48.7B returned in FY2026) and Meta retain. Stock-based compensation of $19.314B TTM is 2.5% of revenue and diluted share count grew only 1%, so dilution discipline is intact.

## 5. Bull Case

The bull case is that Amazon is running the largest supply-constrained business in technology, and the market's July anchor was set before it could see the evidence.

1. **AWS acceleration is now five quarters long and is a market-share statement.** +17% → +20% → +24% → +28% → +37% across Q2 2025 to Q2 2026, at a base that reached a $169B annualized run rate. Segment operating income grew 64% year over year to $16.621B and the segment margin recovered from 32.9% to 39.4%. Nothing this large has re-accelerated this way.
2. **The backlog converts the capex into contracted revenue.** An AWS backlog of $496B growing triple-digit percentages (call coverage) is roughly 3.3x TTM AWS segment revenue, and management states 2027 capacity is largely reserved with some 2028 capacity spoken for. Capacity that is pre-sold is the strongest available answer to the overbuild objection.
3. **Own silicon is a margin lever the merchant buyers do not have.** A chips business above a $25B run rate at triple-digit growth, Trainium commitments reported above $225B, Graviton5 at 98% of the top 1,000 EC2 customers with 30–40% better price-performance: every unit of AI demand Amazon serves on its own silicon carries a structurally better gross margin than one served on purchased accelerators. This is why a 39.4% segment margin during a record build is plausible rather than suspicious.
4. **Retail is levering, not decaying.** Paid units +17% on 3% headcount growth, online stores +15%, third-party services +16%, North America margin at 7.9% and International at 4.1% — both segments contributed record or near-record profit while advertising grew 26%. The non-AWS business now produces $39.031B of TTM operating income, which funds a large share of the build without external capital.
5. **The anchor is stale by construction.** $235.50 was set in the session before the release, after an -11.1% July drawdown driven by AI-capex anxiety. Whatever the correct valuation of this print is, the price used in section 8 does not contain it.

Upside frame: if AWS sustains growth above 30% into 2027 while the segment margin holds in the high 30s, TTM AWS operating income approaches $75–80B and the sum-of-parts range in section 8.2 ($262–$338) becomes the relevant band rather than an aspiration. That requires free cash flow to trough in 2026 and turn up as the backlog converts.

## 6. Bear Case

The bear case does not dispute the growth. It disputes what the growth costs and how much of the reported profit is real.

1. **Free cash flow is negative and the capex line is still climbing.** -$7.604B TTM, down from +$25.925B at Q1 2025 — a $33.5B swing in five quarters. Net PP&E rose 22.8% sequentially in Q2 alone, and 2026 cash capex is guided about $220B. Amazon is now the second-worst free-cash-flow generator in the demand layer after Oracle, and unlike Oracle it is not a small company financing a pivot; it is the largest, meaning the absolute cash absorption is unprecedented.
2. **Part of the capex increase buys nothing.** About $20B of the raise is attributed to higher memory prices (call coverage). For a book that treats rising hyperscaler capex as evidence of rising buildout volume, this is a direct partial falsification: the same dollar figure now maps to fewer units. If memory inflation persists into 2027, capex guides across the layer will overstate physical demand.
3. **Reported profit is pre-depreciation and pre-wave.** Net capex at 2.25x trailing D&A means the 39.4% AWS margin reflects an asset base whose expense has not arrived. PP&E net grew from $357.025B to $446.046B in six months. As that depreciates, either AWS pricing rises or the segment margin compresses — and AWS's own price-performance messaging on Graviton argues against the former.
4. **Earnings quality is the weakest in the layer.** $53.415B of Q2's $62.647B net income is non-operating. Add the unattributed $41.988B after-tax OCI gain and the $161.5B six-month increase in "Other assets," and a large fraction of Amazon's reported book-value growth is marks on private positions that can reverse. TTM GAAP EPS of $12.44 makes the headline P/E of 18.9x look cheap; it is an artefact.
5. **Circularity.** Anthropic is the source of the largest income line and a counterparty committing up to 5 GW of Trainium capacity. Amazon has disclosed neither a concentration figure for the $496B backlog nor the carrying value of the stake. This is the same structural pattern the book flags at Oracle/OpenAI and Nebius, at a much larger absolute scale, with less disclosure.
6. **The valuation anchor cuts both ways.** $235.50 is stale in the direction of not knowing the print — but the July drawdown from $254.96 to $226.65 happened precisely because the market was already worried about capex, and the print confirmed capex is higher than feared.

Downside frame: if AWS decelerates toward the mid-20s while the segment margin falls below 35% under the depreciation wave, and free cash flow stays negative through 2027, a de-rate to roughly 2.6x EV/TTM sales maps to about $185–200 — near where the stock traded in February 2026, and about 15–20% below the anchor.

## 7. Key Uncertainties

| Uncertainty | Why it matters | When we will know |
|-------------|----------------|-------------------|
| When does trailing free cash flow trough? | -$7.604B with capex still rising sequentially; the trough date sets whether 2027 is a recovery or a second negative year | Q3 2026 results (late Oct 2026) and the Q4 cash-flow statement |
| How much of the capex raise is price versus capacity? | About $20B attributed to memory prices; determines whether the layer's capex-equals-volume inference holds | 2027 capex guidance and any unit disclosure; memory-vendor pricing commentary |
| Does the AWS segment margin survive the depreciation wave? | Capex is 2.25x D&A; the 39.4% margin is a pre-wave figure | Quarterly AWS segment margin through 2027 |
| What is the Anthropic position worth and how concentrated is the backlog? | $53.415B of Q2 income and up to 5 GW of committed capacity reference one counterparty | 10-Q/10-K disclosure of carrying value and any concentration figure |
| How fast does Trainium substitute for merchant accelerators? | Determines whether Amazon's capex is bullish or bearish for NVIDIA and AMD | Trainium deployment disclosures; OpenAI's roughly 2 GW ramp beginning 2027 |
| Does the $496B backlog convert on schedule? | Backlog is the answer to the overbuild objection; slippage would invert it | Quarterly backlog disclosure and AWS revenue conversion |
| Retail margin under 19% shipping-cost growth | Shipping costs grew faster than units; retail funds the build | Q3/Q4 North America segment margin |
| Globalstar closing and integration boundary | The cash / stock election and specified adjustment leave final consideration uncertain; FCC, French and other international approvals and C-3 authorisations remain outstanding | Regulatory approvals, C-3 authorisations and final closing filings |

Thesis-breaking conditions:

- **Bear case breaks:** trailing free cash flow troughs in 2026 and turns positive during 2027 while AWS holds growth above 30% and a segment margin above 37%, and backlog conversion is visible in reported AWS revenue.
- **Bull case breaks:** AWS growth decelerates toward the mid-20s while capex still rises, the AWS segment margin falls below 35%, trailing free cash flow stays below -$25B, or an Anthropic-related mark reverses materially.

## 8. Valuation Context

The following is valuation context, not a target price or a recommendation. All arithmetic uses the **July 30, 2026 close of $235.50** and the 10.783B common shares outstanding disclosed at June 30, 2026. The anchor predates the after-close earnings release; after-hours and pre-market trading are not completed sessions and are excluded.

### 8.1 Current multiples

| Metric | Value | Definition / caveat |
|--------|-------|---------------------|
| Share price | $235.50 | Jul 30, 2026 Nasdaq official close; release followed after the close |
| Market cap | ~$2.539T | $235.50 × 10.783B shares |
| Enterprise value (narrow) | ~$2.545T | Market cap + $128.894B long-term debt − $122.988B cash and securities; leases excluded |
| Enterprise value (incl. long-term leases) | ~$2.640T | Adds $94.338B of long-term lease liabilities; net debt about $100.2B |
| EV / TTM sales | ~3.28x narrow; ~3.40x lease-inclusive | TTM revenue $775.680B |
| EV / TTM operating income | ~27.2x | TTM operating income $93.712B |
| Price / TTM operating cash flow | ~15.7x | TTM OCF $161.403B |
| GAAP P/E (TTM) | ~18.9x — **not decision-useful** | TTM diluted EPS $12.44 is dominated by investment marks |
| Price / TTM free cash flow | Not meaningful | TTM FCF is -$7.604B |
| Implied AWS multiple, residual method | AWS carries ~$1.79T of EV if retail plus advertising is valued at 1.2x TTM revenue | Illustrative decomposition, not a valuation |
| Capex intensity | 21.8% of revenue | TTM net PP&E $169.007B / TTM revenue $775.680B |

**Sensitivity the narrow EV hides.** The narrow enterprise value implicitly values the non-operating investment complex at zero incremental adjustment while "Other assets" grew from $122.607B to $284.132B in six months. If $X of that increase is the AI-lab investment complex, operating enterprise value is $2.545T − $X: at $50B of attributed value the operating EV falls to about $2.495T and EV/TTM sales to about 3.21x; at $150B, to about $2.395T and 3.09x. Amazon does not break this out, so we present it as a sensitivity rather than asserting a figure.

### 8.2 Sum-of-parts on trailing twelve-month revenue

| Segment | TTM revenue | Multiple band | Implied value |
|---------|-------------|---------------|---------------|
| AWS | $148.404B | 12–15x revenue | $1.781T – $2.226T |
| Advertising | $76.072B | 8–10x revenue | $609B – $761B |
| Retail, subscriptions and other | $551.204B | 0.8–1.2x revenue | $441B – $661B |
| **Enterprise value** | | | **$2.831T – $3.648T** |
| Less narrow net debt | | | -$5.906B |
| **Equity value** | | | **$2.825T – $3.642T** |
| **Per share** | | | **$262 – $338** |

The multiple bands are carried forward unchanged from the prior cycle so that the comparison isolates the change in the fact base, not a change in method. At $235.50 the range implies roughly 11% to 43% above the anchor. Treat the upper half as conditional: it requires AWS growth and margin to persist while the negative-free-cash-flow build earns an adequate return.

### 8.3 Scenario grid

| Scenario | Driver assumptions (AWS growth / segment margin / FCF path / silicon mix) | Valuation implication versus the $235.50 anchor | Probability weight |
|----------|---------------------------------------------------------------------------|--------------------------------------------------|--------------------|
| Bull | AWS holds above 30% growth into 2027 with segment margin above 37% through the depreciation wave; the $496B backlog converts on schedule; trailing FCF troughs in 2026 and turns positive during 2027; Trainium mix lifts AWS gross margin | The anchor proves cheap: the sum-of-parts upper half becomes the relevant band, roughly $300–340 | 30 |
| Base | AWS decelerates gradually toward the low 30s as comps harden; segment margin settles at 35–38%; 2026 cash capex lands near $220B and 2027 grows again, keeping trailing FCF between -$15B and breakeven through 2027; memory inflation persists but is absorbed | The anchor is broadly fair, with the sum-of-parts lower half as the reference: roughly $250–275, a modest positive gap | 40 |
| Bear | AWS growth falls toward the mid-20s while capex still rises; the depreciation wave pushes segment margin below 35%; trailing FCF stays below -$25B into 2027; an Anthropic mark reverses materially and the earnings-quality discount widens | De-rate toward 2.6x EV/TTM sales: roughly $185–200, near the February 2026 level | 30 |

### 8.4 What is priced in, and the expectation gap

**The critical qualification first:** at $235.50 the market had not seen Q2. The last completed session closed hours before the release, at the end of a month in which the stock fell 11.1% from $254.96 on July 15 to $226.65 on July 29 on AI-capex anxiety, then rebounded 3.9% into the print on heavy volume. So this is not a "what did the market do with the news" analysis — it is a fundamental expectation gap measured at a pre-news anchor, and it will be superseded by the first completed post-release session.

What the anchor appears to have priced: AWS growth continuing but not accelerating to 37%; capex around the previously disclosed $200B; free cash flow weak but not the specific -$7.604B figure; and no knowledge of a $496B backlog or of capacity being reserved into 2027. What the anchor also appears to have priced, correctly, is a rising-capex risk premium — the July drawdown was that premium being applied.

Netting the grid: the positive surprises (AWS acceleration, segment margin recovery, backlog scale, sold-out capacity) are larger and more durable than the negative ones (the $20B capex raise, the FCF outflow), but the negatives are structurally worse than they look, because part of the capex increase buys no capacity and the reported margin is pre-depreciation. The 30/40/30 grid therefore reads a **modestly positive expectation gap** — enough for **constructive**, not enough for bullish, and explicitly conditional on an anchor that has an unusually short shelf life.

## 9. Catalysts & Timeline

| Catalyst | Timing | Impact |
|----------|--------|--------|
| First completed post-release session | 2026-07-31 | Re-anchors every multiple in this report; the current anchor is pre-news by construction |
| Q3 2026 results: FCF trough test, Q3 net PP&E, AWS margin | Late Oct 2026 | The single most important reading for the demand layer; guide is $197.0B–$202.0B revenue and $22.5B–$26.5B operating income |
| 2027 capex guidance and any unit-versus-price split | Q4 2026 results, early Feb 2027 | Determines whether the layer's capex-equals-volume inference survives memory inflation |
| 10-Q/10-K disclosure on the Anthropic position and backlog concentration | Filing cadence from Q3 2026 | Would resolve the largest earnings-quality and circularity question in the layer |
| OpenAI Trainium ramp, roughly 2 GW beginning 2027 | From 2027 | The clearest merchant-versus-custom silicon substitution reading available to the book |
| AWS backlog updates against the $496B base | Quarterly | Tests whether contracted demand keeps outrunning delivered capacity |
| Memory-price commentary from Micron, SK hynix and SanDisk | Their quarterly cycles | Cross-checks Amazon's attribution of the capex raise |
| Globalstar regulatory approvals and closing | No fixed date; depends on FCC, French and other international approvals and C-3 authorisations | Establishes when the satellite / spectrum assets actually enter Amazon, final consideration and the integration boundary; not an AI-chain trigger |

The structured monitoring fields track six readouts: AWS growth versus segment margin, the trailing free-cash-flow trough, the input-cost mix inside the capex raise, the Anthropic mark and circularity, AWS backlog conversion, and Trainium substitution against merchant silicon.

## 10. Conclusion

Amazon enters the chain book as the demand layer's dashboard, and the first reading it produces is uncomfortable in a useful way. On the revenue and margin lines it is the best print in the layer: AWS at $42.232B and +37%, its fastest in 18 quarters, at a 39.4% segment margin and a $169B annualized run rate, with a contracted backlog reported at $496B and capacity substantially reserved into 2027. Consolidated operating income of $27.461B at a record 13.7% margin, with advertising +26% and paid units +17%, shows this was not a one-segment quarter.

On the cash line it is the layer's clearest warning. Trailing free cash flow of -$7.604B against trailing operating cash flow of $161.403B says the build is now larger than the largest cash engine in the sector; net capex at 2.25x depreciation says the reported margin is a pre-wave figure; and the roughly $20B of the capex raise attributed to memory prices says something the book needs to internalise — a rising hyperscaler capex number is no longer automatically a rising volume signal.

The stance is **constructive, medium conviction**. Constructive because the operating evidence is strong, the backlog is contracted rather than hoped-for, own silicon is a real margin lever, and the $235.50 anchor was set in the session before any of that was public. Medium, not high, because the three variables that decide the thesis — the free-cash-flow trough, the price-versus-capacity mix of the capex, and the size and independence of the Anthropic position — are all outside the current disclosure window, and because the anchor itself will be superseded by the next completed session.

Upgrade trigger: trailing free cash flow troughs in 2026 and turns positive during 2027 while AWS holds growth above 30% with a segment margin above 37%, the $496B backlog converts visibly into reported AWS revenue, and 2027 capex guidance separates capacity from input-cost inflation — upgrade to bullish. Downgrade trigger: AWS growth decelerates toward the mid-20s while capex still rises, the AWS segment margin falls below 35%, trailing free cash flow stays below -$25B into 2027 with long-term debt still growing, or an Anthropic-related mark reverses materially without disclosure of the position's size — downgrade to neutral-watch.

## Appendix: Sources & Assumptions

- **Globalstar transaction primary source.** The agreement date, cash / stock election mechanics, $90 per-share cap, support agreements covering about 57.6% of outstanding common shares, July 17, 2026 HSR expiry, remaining regulatory approvals, C-3 authorisations, the roughly $97M milestone-payment cap and termination fees come from Globalstar's [Form S-4/A filed August 13, 2026](https://www.sec.gov/Archives/edgar/data/1366868/000110465926096195/tm2614482-11_s4a.htm). This report does not classify the transaction as an AI-chain signal and does not mechanically extrapolate the per-share cap into an issuer-disclosed transaction value.
- **Primary source.** All Q2 2026 income-statement, segment, balance-sheet, cash-flow and supplemental-metric figures in this report are taken directly from Amazon's official Q2 2026 earnings release / Form 8-K Exhibit 99.1, dated 2026-07-30 for the quarter ended 2026-06-30: [Amazon Q2 2026 earnings release (PDF)](https://s2.q4cdn.com/299287126/files/doc_earnings/2026/q2/earnings-result/AMZN-Q2-2026-Earnings-Release.pdf). This includes revenue $200.606B, operating income $27.461B, net income $62.647B, diluted EPS $5.75, other income $53.415B, segment revenue and operating income for North America ($116.177B / $9.123B), International ($42.197B / $1.717B) and AWS ($42.232B / $16.621B), the six disclosed revenue lines, TTM operating cash flow $161.403B, TTM purchases of PP&E net of proceeds and incentives $169.007B, TTM free cash flow -$7.604B, TTM D&A $75.200B, TTM stock-based compensation $19.314B, cash $78.213B, marketable securities $44.775B, long-term debt $128.894B, long-term lease liabilities $94.338B, total assets $1,095.689B, other assets $284.132B, stockholders' equity $551.620B, common shares outstanding 10.783B, employees 1,595,000, worldwide shipping costs $27.873B, paid-unit growth +17%, the Q3 2026 guidance range, the statements that the AWS AI business and the chips business each exceeded a $25B annual revenue run rate with triple-digit growth, the Graviton5 metrics, and the statement that Anthropic and OpenAI have each made multi-year, multi-gigawatt Trainium commitments. The release's guidance risk factors explicitly name "resource and supply volatility, including for memory chips."
- **Earnings-call coverage (labelled as such throughout).** The following figures are **not** in the official release and come from coverage of the 2026-07-30 earnings call: the full-year 2026 cash-capex guide of about $220B raised from about $200B and its attribution to higher memory prices; the AWS backlog of $496B growing at triple-digit percentages; Trainium revenue commitments reported above $225B; OpenAI committing to roughly 2 GW of Trainium capacity ramping from 2027 and Anthropic to as much as 5 GW; the statements that 2027 capacity is largely reserved with some 2028 capacity spoken for; and Andy Jassy's remark that "even at that amount, we will still not have enough capacity to meet all the demand we have in 2026, and I believe this dynamic will also be true in 2027 too." Sources: [CNBC](https://www.cnbc.com/2026/07/30/amazon-amzn-q2-earnings-report-2026.html), [Seeking Alpha](https://seekingalpha.com/news/4622393-amazon-outlines-q3-net-sales-of-197b-202b-while-lifting-2026-cash-capex-to-about-220b), [Fortune](https://fortune.com/2026/07/30/andy-jassy-amazon-capex-demand-aws-pga-tour/). Three independent outlets report the $220B figure and the memory attribution consistently. Note that this hub's cross-check signal entry `amazon-q2-2026-aws-capex-cash-conversion` deliberately scoped itself to release-only facts and therefore excludes these items; signal and report differ by evidence tier by design, and the signal ledger remains the stricter surface.
- **Basis warning.** The about-$220B guide is company-defined **cash capex**; the $169.007B TTM figure is **purchases of property and equipment net of proceeds from sales and incentives**, the basis the release itself uses for free cash flow. The two are not differenced anywhere in this report.
- **Attribution boundary on the Anthropic complex.** Only the $53.415B of Q2 other income carries company attribution ("primarily from our investments in Anthropic"). The $41.988B after-tax available-for-sale unrealised gain in other comprehensive income and the $161.5B six-month increase in "Other assets" are disclosed without attribution; the linkage stated in section 3 is our inference, supported by the size argument that total marketable securities are only $44.775B. No summed "Anthropic gain" figure is published here.
- **Market data.** The share price of $235.50 is the 2026-07-30 Nasdaq official close, retrieved via yfinance on 2026-07-31, and is the last completed US session at the time of writing; the earnings release followed after that close, so the anchor is pre-news by construction. The July path ($254.96 on 07-15, $226.65 on 07-29, $235.50 on 07-30 on 100.9M shares) and the 52-week closing range ($198.79 on 2026-02-13 to $274.99 on 2026-05-06, intraday $196.00–$278.56) are from the same source. Market cap, enterprise value and all multiples are computed from that price and the issuer's 10.783B share count and labelled with the anchor date. yfinance separately reports about 10.757B shares outstanding; the issuer figure is used. This snapshot is subsequently maintained by `static/invest/research/update_prices.py`.
- **Peer figures.** Microsoft, Meta, Oracle and Alphabet comparison figures are from the corresponding reports in this hub (`microsoft-2026`, `meta-2026`, `oracle-2026`) and from the verified signal-ledger entries `alphabet-q2-2026-capex` and the Meta Q2 2026 entries, each at its own reported period and not restated.
- **Version chain.** This is the 2026H1 full-cycle rewrite. The prior-cycle report, including its February 2026 fact base, its July 2026 incremental redlines and its older valuation anchors, is preserved unchanged at [`amzn-2026-pre-chain`](/invest/research/reports/view.html?id=amzn-2026-pre-chain) and is the diff baseline for this version. Historical valuation anchors from that version are intentionally not restated here; the archive is the audit trail.
- The sum-of-parts multiple bands (AWS 12–15x, advertising 8–10x, retail 0.8–1.2x) are carried forward unchanged from the prior cycle so the comparison isolates the fact base rather than the method. They are analytical bands, not targets. This report uses no non-public information.
