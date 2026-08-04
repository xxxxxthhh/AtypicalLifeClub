# Palantir Technologies (PLTR) Deep Research Report

Coverage date: 2026-08-04
Last updated: 2026-08-04
Ticker: NASDAQ: PLTR
Disclaimer: This report is for informational and research purposes only. It does not constitute investment advice. Please conduct your own due diligence.

---

## Executive Summary

> **Framework note:** This report is an order-quality dashboard in the AI-infrastructure book's demand-risk layer, and it answers a question no existing report in this book can answer. Every other demand-layer name — Microsoft, Meta, Alphabet, Amazon, Oracle — is a **buyer** of AI infrastructure whose capex *is* the demand we are testing. CoreWeave and Nebius **rent** that infrastructure back out. MiniMax builds the **models**. None of them proves that the last mile works: that an end enterprise will write a large cheque for an AI application and that the vendor selling it earns a real margin doing so. Palantir is the purest listed instance of that last mile, and it publishes the most granular order-quality series in the entire book — TCV bookings, deals above $1M / $5M / $10M, remaining deal value, and net dollar retention, every quarter. Where Oracle and Amazon dashboard *infrastructure* order quality, Palantir dashboards *application-layer* order quality.

**One-line thesis:** Palantir's Q2 2026 (quarter ended June 30, 2026, reported August 3, 2026 after the close) is the strongest operating print in this entire coverage book — revenue $1.935B growing 93% and still accelerating, US commercial revenue +149%, a 47% *GAAP* operating margin, $1.22B of adjusted free cash flow at a 63% margin, and a Rule of 40 score of 155% — but the security is simultaneously the most expensive asset in the book by a wide margin, and its own price history over the last nine months is the proof that at these multiples the business result is not what determines the return.

**Current view:** **Cautious, medium conviction.** This is explicitly a valuation and multiple-risk call, not a business-quality call — a distinction that matters, because every other `cautious` verdict in this book (Oracle's −$23.7B FY2026 free cash flow, Nebius's leverage, MiniMax's model-layer commoditization) rests on something being wrong with the business. Nothing is wrong with this business: $9.2B of cash against $212M of debt, no external financing need, GAAP-profitable in every quarter, and accelerating at scale. The problem is the price. At the August 3 close of $125.65 the stock carried ~107x trailing GAAP earnings and ~49x trailing sales; at the $144.42 post-market indication that followed the release, ~123x and ~56x. Both anchors support the same verdict, which is the point. And between November 3, 2025 and June 25, 2026 the stock fell 48% — from $207.18 to $107.27 — while quarterly revenue growth *accelerated* from 63% to 85%. At this multiple, returns are governed by multiple compression, not by operating results.

**Quick stats:**

| Metric | Value |
|--------|-------|
| Share price | $125.65 (Aug 3, 2026 close, Yahoo/yfinance); Q2 released after the close, indicated $144.42 (+14.9%) in post-market trading |
| 52-week range | $107.27 (2026-06-25) – $207.18 (2025-11-03); the close sits ~39% below the November 2025 high |
| Market cap / shares | ~$301.2B at the close, ~$346.2B at the post-market indication; ~2.397B shares outstanding (+3.2% YoY), 2,568.7M weighted diluted |
| Latest reported period | Q2 2026, quarter ended 2026-06-30 (reported 2026-08-03 after the close) |
| Q2 revenue / YoY / QoQ | $1,935.464M, +93%, +19% |
| Q2 US revenue | $1,573M (81% of total), +115% YoY — US commercial $764M (+149%), US government $809M (+90%) |
| Q2 international revenue | ~$362M (~19% of total), ~+33% YoY (derived as total less US) — the one line not participating |
| Q2 GAAP operating income / margin | $912.004M / 47%; adjusted $1,194.472M / 62% (from 46% in Q2 2025) |
| Q2 GAAP net income / diluted EPS | $1,061.890M (55% margin) / $0.41 GAAP, $0.41 adjusted |
| Q2 OCF / adjusted FCF | $1,216.167M (63%) / $1,220.359M (63%) — adjusted FCF exceeds OCF; see the caliber note in §3 |
| Order book | Q2 TCV booked $3,373M (+49%); US commercial TCV $2,132M (+153%, a record); US commercial remaining deal value $6,238M (+124% YoY, +27% QoQ) |
| Deal count / customers | 220 deals ≥$1M, 98 ≥$5M, 73 ≥$10M; US commercial customer count +35% YoY; NDR 139% as of Q4 2025 |
| Balance sheet | $9.2B cash and short-term treasuries vs $212M total debt → ~$9.0B net cash; no external financing need |
| FY2026 guidance (raised) | Revenue $8,150–8,158M (+82%); US commercial ≥$3,424M (+134%); adjusted operating income $4,889–4,897M; adjusted FCF $4,500–4,700M |
| Rule of 40 / SBC | 155% (from 68% in Q3 2024); Q2 stock-based compensation $265.209M = 13.7% of revenue |
| Chain role | demand-risk order-quality dashboard: does AI spending convert into end-customer application revenue and margin |

## 1. Business Overview

Palantir sells operational software to organizations that need to act on data under real constraints — classification levels, regulatory regimes, physical supply chains, live military operations. It is not a data warehouse and not a model provider; it sits between them, and the layer it owns is the **ontology**: a semantic map of an organization's entities, relationships, and permitted actions, against which a language model can be pointed at a decision rather than at a document. That layer is why AIP converted so much faster than the market expected in 2024–2026, and it is the asset the bull case ultimately rests on.

| Product / line | Q2 2026 readout | Economic meaning | AI-infra relevance |
|----------------|-----------------|------------------|--------------------|
| US commercial (AIP / Foundry) | $764M, +149% YoY, +28% QoQ; customer count +35% YoY; TCV $2,132M (+153%, record) | The growth engine: AIP boot camps converting into production seats and expansions | The single cleanest public read that enterprises pay real money for AI applications |
| US government (Gotham / Apollo) | $809M, +90% YoY, +18% QoQ | Defense, intelligence, and civil agencies; multi-year, accredited, high-switching-cost | Demand that is budget-driven rather than AI-capex-driven — it does not co-move with hyperscaler spend |
| International commercial + government | ~$362M combined, ~+33% YoY | Europe and Asia; structurally slower, weighed down by European procurement and data regimes | The negative control: the same product growing at a third of the US rate |
| Ontology + forward-deployed engineering | Embedded in both segments | Deployment model that installs engineers inside the customer's operation | The moat and the scaling constraint at the same time |
| Adjusted operating margin | 62%, from 46% a year ago | 16 points of expansion in four quarters at 93% growth | Proves application-layer AI can carry software-grade economics |
| Balance sheet / funding | $9.2B cash, $212M debt, no financing need | Self-funded; adjusted FCF margin 63% | Palantir captures AI revenue without funding AI infrastructure |

Two structural points define this business relative to the rest of the demand-risk layer. First, **Palantir is asset-light in a layer of asset-heavy names.** Microsoft spent $41B on capex in a single quarter; Oracle burned $23.7B of free cash flow across FY2026; Meta's quarterly FCF fell 91% to $0.78B. Palantir's capex is immaterial, and it converted 63% of revenue into adjusted free cash flow in the same quarter. It participates in the AI economy purely as a value-capturer, never as a value-funder. Second, **the revenue base is bifurcated in a way the headline hides.** The 93% headline is US commercial at +149% and US government at +90% carrying a ~19% international base growing roughly a third as fast. Palantir is not a global AI-adoption story; it is a US AI-adoption story with an international attachment that has not inflected.

## 2. Industry & Competitive Position

Palantir competes on three maps, and its position is genuinely different on each.

In **US government**, the moat is the strongest and the least appreciated. Accreditation (FedRAMP High, IL5/IL6), classified-environment deployment via Apollo, and a decade of embedded operational history produce switching costs that no commercial software vendor enjoys. Competitors are the traditional integrators — Booz Allen, Leidos, CACI, SAIC — who sell labour hours rather than a product with software margins, which is precisely why Palantir's government revenue can grow 90% while carrying a 47% GAAP operating margin. The offsetting fact is that this demand is appropriated, not budgeted by a CFO responding to AI ROI: it moves with defense priorities and administration policy, and it carries political and reputational exposure that a pure enterprise vendor does not have.

In **US commercial**, the competitive set is crowded and rapidly capable: Databricks and Snowflake from the data-platform side, Microsoft Fabric and Azure AI Foundry, AWS Bedrock/SageMaker, and Google Vertex from the hyperscaler side, and the consultancies from the services side. Palantir's differentiation is that it sells a working outcome rather than a toolkit — the boot-camp motion compresses evaluation from quarters to days — and its 149% growth against that field is evidence the differentiation is currently real. The structural question is whether the ontology is a durable moat or a temporary head start: the model vendors themselves (OpenAI, Anthropic) are moving into enterprise deployment, and hyperscalers are building semantic layers into their own stacks.

The third map is the **AI-infrastructure chain**, where Palantir's role is unusual because it is barely a customer of it:

| Chain position | Palantir's role | Read-through to existing coverage |
|----------------|-----------------|-----------------------------------|
| Compute demand | Immaterial buyer; runs on hyperscaler and on-prem/classified capacity | Palantir does **not** validate GPU or capex demand directly — do not read it as a chip signal |
| Application monetization | The purest listed proof that AI applications carry software margins at scale | The core positive read for the `application-monetization` cross-check |
| Terminal demand | FY2026 revenue of ~$8.15B against ~$550B+ of annual hyperscaler capex | Scale caveat: the last mile is profitable but is still ~1.5% of the spend it must eventually justify |
| Model layer | Model-agnostic consumer of frontier and open models | Commoditizing models are a tailwind here — the opposite sign to Microsoft's OpenAI dependency |
| Enterprise software peers | Growing 93% while Salesforce-class incumbents grow single digits | The AI-native share shift inside enterprise software is real and is visible in this print |
| Government / defense tech | Adjacent to Anduril-class defense software; ahead of the integrators | Defense AI demand is a distinct, non-cyclical demand pool the rest of the book does not capture |

The most important sentence in this section is the scale caveat. Palantir demonstrates that the *unit economics* of application-layer AI are excellent where it works. It does not yet demonstrate that application-layer revenue is *large enough* to justify the infrastructure being built for it. Both statements are true, and conflating them is the most common analytical error made about this stock.

## 3. Financial Analysis

The Q2 2026 income statement is, on the numbers, the best in this coverage universe. There is no hedging required on the operating line.

| Metric | Current readout | Interpretation | Grade |
|--------|-----------------|----------------|-------|
| Revenue growth | Q2 $1,935M, +93% YoY, +19% QoQ; five straight quarters of acceleration (+48% → +63% → +70% → +85% → +93%) | Acceleration at a $6B+ trailing base is close to unprecedented in enterprise software | A+ |
| GAAP operating margin | 47% in Q2, from 26.8% in Q2 2025; adjusted 62% from 46% | Margin expanded 20 GAAP points in four quarters *while* growth accelerated — operating leverage, not cost cutting | A+ |
| Free cash flow | Q2 OCF $1,216.167M, adjusted FCF $1,220.359M (63% margin); FY2026 guided $4,500–4,700M | Cash conversion is real and guided to nearly double FY2025 | A |
| Balance sheet | $9.2B cash and short-term treasuries vs $212M total debt → ~$9.0B net cash | The cleanest balance sheet in the demand-risk layer; zero financing risk | A+ |
| Order book | TCV $3,373M (+49%); US commercial TCV $2,132M (+153%); US commercial RDV $6,238M (+124%) | Bookings growing faster than revenue in US commercial — forward growth is contracted, not hoped for | A |
| Earnings quality (tax) | TTM effective tax rate ~1.3%; full valuation allowance on US and UK deferred tax assets as of 2026-03-31; $2.618B NOL carryforwards, $3.452B valuation allowance (FY2025 disclosure) | GAAP EPS is essentially untaxed; at a normalized 21% rate TTM EPS falls from $1.17 to ~$0.94 | C |
| Dilution | Q2 SBC $265.209M = 13.7% of revenue; shares outstanding +3.2% YoY; 2,568.7M weighted diluted vs ~2,397M outstanding | Real and persistent economic cost that neither OCF nor adjusted FCF charges | C+ |
| Geographic concentration | US 81% of revenue and growing 115%; international ~19% growing ~33% | The thesis is a US thesis; international has not inflected | B− |

**Trailing-twelve-month frame (through 2026-06-30), reconciled from the four quarterly releases:** revenue $6,156M (+79%), GAAP operating income $2,635M (42.8% margin), GAAP net income $3,017M (49.0% margin), diluted EPS $1.17. The four quarters are Q3 2025 $1,181M, Q4 2025 $1,407M, Q1 2026 $1,633M, Q2 2026 $1,935M, and they sum exactly to the trailing figures used in §8. This matters because widely-quoted data feeds were still carrying a pre-Q2 window on the morning after the release — a trailing P/E computed against the older denominator overstates the multiple by roughly a third.

**Caliber note on adjusted free cash flow.** Q2 adjusted FCF of $1,220.359M *exceeds* operating cash flow of $1,216.167M. That is not an error: Palantir's non-GAAP definition adds back certain items alongside deducting its (immaterial) capex. The number to hold onto is that neither operating cash flow nor adjusted free cash flow charges the $265.209M of quarterly stock-based compensation, which is a genuine 13.7%-of-revenue economic cost borne by shareholders through the share count. Note also that §8 places a **GAAP** trailing P/E next to an **adjusted** forward FCF multiple; the denominators are not on the same basis and are labeled accordingly.

Cross-layer comparison — who captures AI revenue versus who funds it (each column at its own reported period; not restated):

| Metric | Palantir (Q2 2026) | Microsoft (FY26 Q4) | Oracle (FY26 Q4) | Meta (Q2 2026) |
|--------|--------------------|---------------------|-------------------|----------------|
| Revenue growth | +93% | +18% | — | — |
| GAAP operating margin | 47% | 45.1% | — | — |
| Quarterly capex | Immaterial (<1% of revenue) | $41B incl. leases (~35% of FY revenue) | FY2026 $55.66B | $31.078B |
| Free cash flow | $1.22B adjusted, 63% margin | ~$19.6B in Q4; ~$67.0B FY2026 | FY2026 −$23.69B | $0.784B (−91% YoY) |
| External financing need | None (~$9.0B net cash) | None (net cash) | ~$40B debt+equity planned | None |
| Sales multiple | ~42.5x FY2026E revenue | ~10.1x FY2026 revenue | — | — |

Red-flag check:

| Red flag | Current status | What to re-check |
|----------|----------------|------------------|
| Valuation multiple | ~107x trailing GAAP EPS at the close, ~123x at the post-market indication; ~49x/~56x trailing sales | Whether growth deceleration and multiple compression arrive in the same quarter |
| Near-zero tax rate | TTM effective rate ~1.3%; full US/UK valuation allowance still in place at 2026-03-31, with the company flagging a reasonable possibility of future release | A valuation-allowance release produces a large one-time non-cash GAAP gain *followed by* a structurally higher tax rate — GAAP EPS quality degrades from that point |
| SBC and dilution | $265.209M in Q2 (13.7% of revenue); share count +3.2% YoY; buybacks negligible relative to SBC | Whether SBC as a percentage of revenue falls as revenue scales, or holds and keeps diluting |
| Government concentration and politics | US government is 42% of Q2 revenue and grew 90%; contracts include politically contested civil-agency work | Budget cycles, administration change, procurement protest, reputational events affecting commercial sales |
| International stagnation | ~19% of revenue growing ~33% versus US at +115% | Whether Europe inflects or the company is permanently a US-plus-allies business |
| Insider selling | CEO Alex Karp and co-founder Peter Thiel have been persistent net sellers through 2026, largely under 10b5-1 plans | Direction and size of net insider activity around the post-earnings repricing |

## 4. Management & Governance

Alex Karp and the founding team have been operationally right about the thing that mattered most: they built the ontology and deployment layer before the model wave arrived, and when it arrived they monetized it faster than any incumbent. The boot-camp go-to-market was a genuine commercial innovation, the refusal to chase seat-count growth at the expense of margin has been vindicated by a 47% GAAP operating margin, and the guidance record is unusually strong — this quarter raised FY2026 revenue guidance to +82% growth, having entered the year guiding +61%. Karp's stated intention to hold US-commercial-class growth "for the next 18 months" is an aggressive public commitment that management has, so far, repeatedly beaten.

Governance carries three standing watch items. First, **founder control and communication style.** Palantir's dual-class structure concentrates control, and Karp's public commentary is deliberately provocative in a way that is inseparable from the brand but does create headline risk that a conventional enterprise-software vendor would not carry. Second, **persistent insider selling.** Karp and Thiel have been consistent net sellers through 2026; the great majority is executed under pre-arranged 10b5-1 plans and diversification by long-tenured founders at these price levels is entirely rational, so this is a data point rather than a signal — but the asymmetry between $265M of quarterly SBC issuance and negligible buybacks is a genuine, ongoing transfer from shareholders to employees. Third, **the political entanglement of the government book.** Palantir's civil-agency and defense work places it inside contested policy debates; management has chosen to lean into that positioning rather than manage it down. That is a defensible strategic choice with a real cost profile — commercial-customer reputational spillover and personnel-recruitment friction — that shareholders should price explicitly rather than ignore.

## 5. Bull Case

The bull case is that Palantir is the only company that has demonstrated, at scale and in public, that AI applications carry software economics — and that the market is still pricing it as a software company rather than as the category's monopolist.

1. **Acceleration at scale is nearly unprecedented.** Five consecutive quarters of accelerating growth — +48%, +63%, +70%, +85%, +93% — on a trailing base that has grown to $6.2B. Almost no enterprise software company has ever accelerated through this revenue level; the ones that did became far larger than the market expected at the time.
2. **The margin structure is the actual proof.** A 47% GAAP operating margin and a 62% adjusted margin, expanded from 26.8% and 46% respectively a year earlier, all while growing 93%. A Rule of 40 score of 155% is not a normal software outcome; it means the growth is not being bought.
3. **Forward growth is contracted, not projected.** US commercial TCV of $2,132M grew 153% — faster than the 149% revenue growth — and US commercial remaining deal value of $6,238M grew 124%. Bookings outrunning revenue at this scale is the healthiest possible composition.
4. **Two independent demand engines.** US commercial (+149%) is AI-adoption driven; US government (+90%) is budget-and-defense driven. They do not share a cycle, which is why a hyperscaler capex pause would not automatically transmit to Palantir revenue.
5. **Optionality the price does not obviously carry.** ~$9.0B of net cash with no financing need, a model-agnostic architecture that *benefits* from model commoditization, an international base that has not yet inflected, and a manufacturing/industrial franchise (Warp Speed) still early. If international inflects on the US pattern, the FY2027 revenue frame moves materially.

Upside frame: if FY2027 revenue approaches $14B on continued US commercial strength with international finally participating, and adjusted operating margin holds near 60%, the business would produce roughly $8B of adjusted operating income. At the ~35–40x forward sales the market has repeatedly paid for this franchise, that supports a $490–560B market cap, or roughly **$205–235 per share**. That requires the multiple to stop compressing — which is the entire question.

## 6. Bear Case

The bear case is not that the business disappoints. It is that at this multiple the business result is not what determines the return — and Palantir's own price history over the last nine months is the cleanest available proof.

1. **The stock has already demonstrated that growth cannot outrun de-rating.** On November 3, 2025 the shares closed at $207.18 on trailing revenue of ~$3.90B, a trailing sales multiple of roughly 123x. By June 25, 2026 they closed at $107.27 — a 48% drawdown — *while quarterly growth accelerated from 63% to 85%*. Decomposed against the post-market indication of $144.42: trailing sales grew 58%, the sales multiple compressed 54% (123x to ~56x), share count rose ~3%, and the net outcome was a ~30% price decline. Nothing about the business went wrong. The multiple simply left.
2. **Every valuation frame is extreme, and the tax-adjusted ones are worse.** ~123x trailing GAAP EPS and ~56x trailing sales at $144.42. Normalize the ~1.3% effective tax rate to 21% and trailing EPS falls from $1.17 to ~$0.94, taking the trailing P/E to ~154x. On forward-guided numbers it is still ~42.5x FY2026E sales and ~73x EV to FY2026E *adjusted* free cash flow — a 1.3% forward FCF yield on a non-GAAP denominator.
3. **The tax tailwind reverses, and reverses visibly.** The full valuation allowance on US and UK deferred tax assets is the reason GAAP EPS looks as good as it does. The company has flagged a reasonable possibility of release. Release produces a large one-time non-cash gain and then a permanently higher effective tax rate — GAAP earnings growth gets structurally harder from that quarter onward, at a moment when the multiple is priced off GAAP earnings.
4. **Dilution is a persistent, unpriced transfer.** $265.209M of SBC in one quarter — 13.7% of revenue — against negligible buybacks, with the share count up 3.2% YoY and weighted diluted shares 7% above shares outstanding. Neither the operating cash flow line nor the adjusted FCF line charges it.
5. **The concentration risks are real and correlated.** US government is 42% of revenue, exposed to appropriations, administration change, and procurement protest. International, at ~19% of revenue growing ~33%, is not currently a diversifier. And the political salience of the government book creates a channel through which a policy event could impair *commercial* growth — the two segments are less independent than the bull case assumes.

Downside frame: a de-rate to ~25x FY2026E sales — still an extreme premium in absolute terms, and above where the stock troughed in June 2026 — maps to roughly $204B of market cap, or about **$85 per share**. That is not a tail scenario constructed from a broken business; it is the multiple continuing the compression it has been in for nine months against guidance that is met.

## 7. Key Uncertainties

| Uncertainty | Why it matters | When we will know |
|-------------|----------------|-------------------|
| Does US commercial growth hold near triple digits? | The entire multiple rests on the +149% line; Karp has publicly committed to holding this pace for ~18 months | Q3 2026 results (early Nov 2026) against the $2,160–2,164M revenue guide |
| When does the valuation allowance release? | Converts an ~1.3% tax rate into a normal one; a one-time GAAP gain followed by structurally harder EPS growth | Quarterly 10-Q tax footnotes; management commentary on positive evidence |
| Does international inflect or stay stalled? | ~19% of revenue at ~33% growth; the difference between a US story and a global one is most of the bull case's upside frame | Quarterly segment disclosure; European commercial customer counts |
| Is the ontology a durable moat or a head start? | Determines whether 149% growth is a share shift that ends when hyperscalers and model vendors close the gap | Competitive win/loss commentary; NDR trend; hyperscaler semantic-layer launches |
| Does government demand survive a policy cycle? | 42% of revenue is appropriated, not budgeted against AI ROI | Appropriations cycles, contract awards and protests, administration policy changes |
| Does SBC intensity fall with scale? | 13.7% of revenue with negligible offsetting buyback is a permanent drag on per-share outcomes | Quarterly SBC as a percentage of revenue; buyback authorization changes |

Thesis-breaking conditions:

- **Bear case breaks:** US commercial growth holds above ~100% through FY2027 with international inflecting above ~50%, adjusted operating margin holds ≥60%, and the forward sales multiple stabilizes rather than continuing to compress — at which point growth is outrunning de-rating and the price becomes the lesser variable.
- **Bull case breaks:** US commercial growth decelerates below ~60% while the multiple is still above ~30x forward sales, or a valuation-allowance release plus a normalized tax rate exposes GAAP EPS growth as far slower than the headline, or a government-budget or policy event impairs the 42% government base.

## 8. Valuation Context

The following is valuation context, not a target price or recommendation. Two anchors are carried deliberately. The primary anchor is the **August 3, 2026 close of $125.65**, which is the last completed session and the auditable market price; because Q2 was released after that close, this price does not reflect the results. The secondary anchor is the **$144.42 post-market indication** on the same date — an indication, not a close. Share-count basis is ~2.397B shares outstanding for market capitalization and 2,568.7M weighted diluted shares for per-share earnings. Net cash of ~$9.0B is used for enterprise value.

| Method | At $125.65 close (primary) | At $144.42 post-market indication | Key assumptions |
|--------|----------------------------|-----------------------------------|-----------------|
| Market capitalization | ~$301.2B | ~$346.2B | ~2.397B shares outstanding |
| Enterprise value | ~$292.2B | ~$337.2B | Less ~$9.0B net cash ($9.2B cash, $212M debt) |
| Trailing P/E (GAAP) | ~107x | ~123x | TTM diluted EPS $1.17 through 2026-06-30 |
| Trailing P/E, tax-normalized | ~134x | ~154x | Restates the ~1.3% effective rate to 21%; TTM EPS ~$0.94 |
| Trailing P/S | ~48.9x | ~56.2x | TTM revenue $6,156M through 2026-06-30 |
| EV / trailing sales | ~47.5x | ~54.8x | Same denominator, net of cash |
| P/S on FY2026 guidance | ~36.9x | ~42.5x | FY2026 revenue guide midpoint $8,154M |
| EV / FY2026E adjusted FCF | ~63.5x | ~73.3x | Adjusted FCF guide midpoint $4.6B — a **non-GAAP** denominator, unlike the GAAP P/E rows above |
| FY2026E adjusted FCF yield | ~1.53% | ~1.33% | Same non-GAAP denominator |

**Scenario grid:**

| Scenario | Driver assumptions (US commercial growth / international / margin / multiple path) | Valuation implication vs the $144.42 indication | Subjective probability weight |
|----------|------------------------------------------------------------------------------------|--------------------------------------------------|-------------------------------|
| Bull | US commercial holds ≥100% through FY2027 and international inflects above ~50%; adjusted operating margin holds ~60%; FY2027 revenue approaches $14B; the forward sales multiple stabilizes at ~35–40x rather than compressing further | Cheap: ~$490–560B market cap, roughly $205–235 per share | 30% |
| Base | US commercial decelerates gradually toward 80–100% as comps harden; international stays a ~30–40% grower; margins hold; FY2027 revenue lands near $12–13B, but the forward multiple keeps drifting down toward ~30x sales as it has for nine months | Broadly fair to modestly rich: growth is delivered and largely offset by continued de-rating, leaving a low-single-digit to flat outcome | 40% |
| Bear | Growth decelerates below ~60% on US commercial, or a valuation-allowance release plus normalized tax exposes far slower GAAP EPS growth, or a government-budget/policy event impairs the 42% government revenue line; the multiple compresses to ~25x forward sales | ~$204B market cap, roughly $85 per share — the June 2026 trough repriced, not a broken business | 30% |

**What's priced in & the expectation gap:** At $144.42 the market is paying ~123x trailing GAAP earnings — ~154x if you tax it normally — and ~42.5x forward sales for a company that must sustain something close to 80%+ growth for several years merely to grow into the multiple. What is priced in: US commercial continuing near triple digits, margins holding near 60% adjusted, and the tax rate staying abnormal. What is not priced in: the valuation allowance releasing and permanently raising the tax rate; SBC continuing to run at 13.7% of revenue; international staying a ~33% grower; and — most importantly — the possibility that the multiple keeps compressing regardless of results, exactly as it did from November 2025 through June 2026. The 30% bull / 40% base / 30% bear grid reads the expectation gap as negative. **Both anchors produce the same verdict**, which is the strongest argument that this conclusion is not an artifact of anchor selection: at the $125.65 close the stock is ~107x trailing earnings and ~37x forward sales, and even that cheaper frame requires flawless multi-year execution to justify.

## 9. Catalysts & Timeline

| Catalyst | Timing | Impact |
|----------|--------|--------|
| Q3 2026 results against the $2,160–2,164M revenue guide | Early Nov 2026 | The direct test of whether the 93% acceleration holds; also the first read on Karp's 18-month growth commitment |
| Quarterly tax-footnote disclosure on the valuation allowance | Quarterly 10-Q, next early Nov 2026 | A release converts a ~1.3% tax rate to a normal one; the largest single GAAP EPS-quality event available |
| US commercial TCV and remaining deal value trend | Quarterly | Bookings currently outrun revenue (+153% vs +149%); the first quarter they invert is the leading indicator of deceleration |
| International commercial inflection or continued stall | Quarterly | Decides whether the bull case's upside frame is live; currently ~33% growth on ~19% of revenue |
| US federal appropriations and defense budget cycle | FY2027 budget process; event-driven | 42% of revenue is appropriated; policy or administration change transmits directly |
| Forward sales multiple behaviour through the next two prints | Ongoing | The governing variable for returns; the November 2025 – June 2026 compression is the base rate to beat |

The structured monitoring fields focus on five readouts: US commercial growth versus the guide, the valuation-allowance and tax-rate transition, SBC and dilution intensity, international inflection, and government concentration.

## 10. Conclusion

Palantir fills the last genuine hole in the demand-risk layer. This book has spent a year establishing that AI infrastructure is being bought at enormous scale — Microsoft's $41B quarterly capex, Meta's $31B, Alphabet's $44.9B — and testing whether that buying is real. What it could not test, until now, is whether anyone at the end of the chain makes money selling the applications that spending is supposed to enable. Palantir's Q2 2026 answers that decisively in the affirmative at the unit level: 93% growth, a 47% GAAP operating margin, 63% adjusted free-cash-flow margin, a 155% Rule of 40, and bookings growing faster than revenue. Nothing else in this book combines those numbers.

At the chain level, the answer comes with a scale caveat that must not be lost. Palantir's entire FY2026 revenue guide of ~$8.15B is roughly 1.5% of annual hyperscaler capex. The last mile is demonstrably profitable; it is not yet demonstrably large. This print is strong positive evidence for the `application-monetization` cross-check — revenue, margin, and operating cash flow are all improving together, which is exactly the confirmation that rule asks for — and it remains insufficient, on its own, to underwrite the terminal-demand assumption beneath $500B+ of annual infrastructure spending.

At the stock level the discipline is different, and this is where the verdict is set. The initiation stance is **cautious, medium conviction** — a valuation and multiple-risk call, explicitly not a business-quality call. The business is the best in the book; the security is the most expensive in the book. The decisive evidence is Palantir's own recent history: between November 3, 2025 and June 25, 2026 the shares lost 48% while quarterly revenue growth accelerated from 63% to 85%. Growth of that magnitude, delivered flawlessly, was not enough to produce a positive return, because the multiple was compressing faster than the business was compounding. At ~123x trailing GAAP earnings — ~154x tax-normalized — the same arithmetic still governs. Conviction is medium rather than high because the operating momentum is genuinely exceptional and a company beating raised guidance five quarters running can sustain an extreme multiple longer than the arithmetic suggests.

Upgrade trigger: US commercial growth holds above ~100% into FY2027 with international inflecting above ~50%, adjusted operating margin holds ≥60%, SBC falls below ~10% of revenue, and the forward sales multiple stabilizes rather than continuing to compress — upgrade to neutral-watch, and to constructive if a de-rate delivers those fundamentals below ~25x forward sales. Downgrade trigger: US commercial growth decelerates below ~60% while the multiple is still above ~30x forward sales, a valuation-allowance release plus normalized tax exposes materially slower GAAP EPS growth, bookings growth inverts below revenue growth for two consecutive quarters, or a government-budget or policy event impairs the 42% government base — downgrade to bearish-avoid.

## Appendix: Sources & Assumptions

- Q2 2026 revenue ($1,935.464M, +93% YoY, +19% QoQ), US revenue ($1,573M, +115%), US commercial revenue ($764M, +149%, +28% QoQ), US government revenue ($809M, +90%, +18% QoQ), GAAP net income ($1,061.890M, 55% margin), GAAP and adjusted diluted EPS ($0.41), GAAP income from operations ($912.004M, 47% margin), adjusted income from operations ($1,194.472M, 62% margin, versus 46% in Q2 2025), cash from operations ($1,216.167M, 63% margin), adjusted free cash flow ($1,220.359M, 63% margin), cash and short-term treasuries ($9.2B), TCV booked ($3,373M, +49%), US commercial TCV ($2,132M, +153%), US commercial remaining deal value ($6,238M, +124% YoY, +27% QoQ), deal counts (220 ≥$1M, 98 ≥$5M, 73 ≥$10M), US commercial customer count (+35% YoY), Rule of 40 (155%, from 68% in Q3 2024), Q2 stock-based compensation ($265.209M), weighted-average diluted shares (2,568,694 thousand), and the complete Q3 2026 and FY2026 guidance are from Palantir's Q2 2026 earnings release dated 2026-08-03: [Business Wire press release](https://www.businesswire.com/news/home/20260802523449/en/Palantir-Reports-Q2-2026-U.S.-Comm-Revenue-Growth-of-149-YY-and-Revenue-Growth-of-93-YY-Raises-FY-2026-Revenue-Guidance-to-82-YY-Growth-and-U.S.-Comm-Revenue-Guidance-to-134-YY-Crushing-Consensus-Expectations). The SEC EDGAR copy of this exhibit was not opened directly — gov-domain fetches are blocked in this environment — so figures were taken from the wire copy of the same release and cross-checked against investor-deck coverage: [Investing.com Q2 2026 slide coverage](https://ca.investing.com/news/company-news/palantir-q2-2026-slides-93-revenue-growth-155-rule-of-40-93CH-4772331).
- Alex Karp's "AI sovereignty" framing and his stated intention to hold US-commercial-class growth "for the next 18 months" are from the release and earnings-call coverage cited above; these are management statements, labeled as such, not company-reported metrics.
- International revenue of ~$362M and its ~+33% YoY growth are **derived, not disclosed**: total revenue less disclosed US revenue for Q2 2026 and for the prior-year quarter (US Q2 2025 implied at $731.6M from the disclosed +115% growth). Treat the growth rate as approximate.
- The trailing-twelve-month frame through 2026-06-30 (revenue $6,156M, GAAP operating income $2,635M, GAAP net income $3,017M, diluted EPS $1.17) is reconciled from the four component quarters — Q3 2025 $1,181M / $393.26M / $475.60M / $0.18, Q4 2025 $1,407M / $575.39M / $608.68M / $0.24, Q1 2026 $1,633M / $754M / $870.53M / $0.34, Q2 2026 $1,935M / $912M / $1,062M / $0.41 — which sum exactly to the stated totals, cross-checked against [stockanalysis.com](https://stockanalysis.com/stocks/pltr/financials/). Prior-quarter growth rates (Q2 2025 +48%, Q3 2025 +63%, Q4 2025 +70%, Q1 2026 +85%) and net dollar retention (134% in Q3 2025, 139% in Q4 2025) are from the corresponding Palantir quarterly releases and their coverage. Note that at the time of writing, several widely-used data feeds still reported a pre-Q2 trailing window (for example a trailing P/E of ~138–141x implying trailing EPS of ~$0.89–0.91); the reconciled post-Q2 denominator above is the one used throughout this report.
- The effective tax rate (~1.3% TTM, 1.4% for FY2025), the full valuation allowance on US and UK deferred tax assets as of 2026-03-31, the $2.618B of net operating loss carryforwards and $3.452B valuation allowance, and the company's own statement that there is a reasonable possibility of a future release are from Palantir's FY2025 and Q1 2026 tax disclosures as summarized by [stock-analysis-on.net](https://www.stock-analysis-on.net/NASDAQ/Company/Palantir-Technologies-Inc/Analysis/Income-Taxes) and [stockanalysis.com statistics](https://stockanalysis.com/stocks/pltr/statistics/). The 21% tax normalization in §8 is this report's own arithmetic, not a company figure: TTM pre-tax income of ~$3,055M taxed at 21% gives ~$2,414M, or ~$0.94 per weighted diluted share.
- Share price ($125.65, 2026-08-03 close; prior close $123.06 on 2026-07-31; post-market indication $144.42), the 52-week range ($107.27 on 2026-06-25 to $207.18 on 2025-11-03), shares outstanding (~2.397B, +3.24% YoY), total debt ($212M), and beta were pulled via Yahoo Finance/yfinance on 2026-08-04. The 2026-08-04 US session had not opened at the time of writing, so 2026-08-03 is the last completed close; Q2 2026 was released after that close, which is why the primary anchor does not reflect the results and a second labeled anchor is carried. The $144.42 figure is a post-market indication, not a close, and is labeled as such wherever it appears. Market capitalization, enterprise value, and all multiples are computed from these inputs. This market-data snapshot can be revised by the data provider and is subsequently maintained by `static/invest/research/update_prices.py`.
- The November 2025 multiple decomposition uses the 2025-11-03 close of $207.18 against trailing revenue of ~$3,896.5M (Q4 2024 $827.6M derived from Q4 2025's disclosed +70% growth, plus Q1–Q3 2025 actuals) and a then-share count of ~2.32B derived from today's ~2.397B less the disclosed +3.24% YoY change, giving a trailing sales multiple of ~123x. Both the share count and the Q4 2024 figure are derived rather than disclosed; the price and growth-rate facts underlying the argument (−48% from 2025-11-03 to 2026-06-25 while quarterly growth went from 63% to 85%) are direct and require no derivation.
- Insider-selling context for Alex Karp and Peter Thiel, competitive-landscape framing, and the bear-side valuation commentary are from secondary financial media and are labeled as sentiment and controversy inputs rather than as company disclosure. Microsoft, Oracle, and Meta comparison figures are from the `microsoft-2026`, `oracle-2026`, and `meta-2026` reports in this hub and each is stated at its own reported period without restatement. This report does not use non-public information.
