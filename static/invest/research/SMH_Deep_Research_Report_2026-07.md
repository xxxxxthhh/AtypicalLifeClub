# SMH VanEck Semiconductor ETF Deep Research Report - Benchmark Sleeve For The AI Semiconductor Chain

Coverage date: 2026-07-06
Last updated: 2026-10-02
Ticker: NASDAQ: SMH
Disclaimer: This report is for informational and research purposes only. It does not constitute investment advice. Please conduct your own due diligence.

---

## Executive Summary

SMH is the benchmark ETF for the semiconductor side of the AI-infrastructure book. It is not a chain node like ASML, TSMC, NVIDIA, Micron, or Arista. It is a liquid, issuer-defined semiconductor basket that lets the research hub compare single-name thesis risk against broad semis beta.

As of the VanEck issuer page on July 2, 2026, ~~SMH had NAV of $592.26, total net assets of $68.82B~~, a 0.35% total expense ratio, and a December 20, 2011 inception date. **Update (2026-10-02)**: VanEck's page now shows NAV of $617.90, total net assets of $75.75B and YTD NAV return of 71.59%, all as of October 1, 2026; the expense ratio is unchanged at 0.35%. VanEck says the fund seeks to track the MVIS US Listed Semiconductor 25 Index, which covers companies involved in semiconductor production and equipment. Daily holdings as of July 1, 2026 showed 26 holdings, led by NVIDIA 18.41%, TSMC 9.18%, AMD 5.57%, Applied Materials 5.49%, Broadcom 5.49%, Micron 5.39%, KLA 5.10%, Lam Research 4.97%, ASML 4.96%, and Intel 4.92%. **Update (2026-10-02)**: daily holdings as of October 1, 2026 still number 26, led by NVIDIA 19.27%, TSMC 9.16%, AMD 5.52%, Broadcom 5.01% and Micron 4.98%; SK hynix (Nasdaq-listed ADS, SKHY) now sits at 4.55% (see §2).

> ~~**2026-07-31 price check.** SMH closed at **$504.22** on **2026-07-29** (last completed session) versus the **$592.29** anchor dated below, a **-14.9%** move. As the benchmark sleeve this is the control reading for the July 2026 chain-wide repricing: the single-name reports in this coverage fell **far more** than the benchmark, so their drawdowns are not explained by semis beta alone. The dated NAV, assets and holdings figures below remain accurate as of their stated dates; the benchmark framing is unchanged.~~
>
> **Update (2026-10-02)**: the price anchor is now the **2026-10-01 regular-session close of $617.81** (Nasdaq historical; CNBC cross-check). That is +4.31% versus the old $592.29 anchor, +22.53% from the 2026-07-29 close of $504.22, +71.55% year to date (from the 2025-12-31 close of $360.13), and −7.64% below the 52-week closing high of $668.91 (2026-06-22).

~~The current view is **benchmark / neutral control sleeve**.~~ **Update (2026-10-02)**: the current view is **stance: neutral-watch, conviction: low**, at $617.81. Because SMH is the default benchmark the chain reports are scored against, **a stance on SMH is an absolute call on the semiconductor basket, not a relative one**: it says whether owning the benchmark itself clears an 8-10% annual hurdle from today's price. It does not say whether SMH will beat or lag any single name. The benchmark/control-sleeve job described below is unchanged.

- **Valuation at the anchor (fund data plus estimates):** VanEck's fund-level trailing P/E was 37.21x as of 2026-08-31, about 41.3x when rescaled to the 2026-10-01 price (estimate). A holdings-weighted aggregation of Nasdaq consensus (estimate, §3) gives 40.2x trailing, **22.4x next-twelve-months**, 27.5x CY2026E, 19.4x CY2027E and 15.6x CY2028E earnings.
- **Probability-weighted result:** a 30/40/30 bull/base/bear grid on CY2028 fund earnings weights to **$758.33 per unit, +22.7%, or +9.5% annualized** over 2.248 years. That is 1.5 points above the 8% hurdle and 0.5 points below 10%. The skew is balanced: +75.9% in the bull case against −36.0% in the bear case.
- **Why conviction is low:** the neutral reading itself is not robust. Three turns lower on every exit multiple take the weighted return to +2.9%, three turns higher take it to +15.8%, and a 10% cut to CY2028 earnings takes it to +4.5%. The Street's own memory consensus already turns down in 2029, inside the holding window.
- **Monitoring window:** 3-15 months, keyed to the Q3 2026 reporting season, consensus revisions and the next index review (cadence not verified in this backfill).

SMH is useful because it captures the whole semis complex in one liquid benchmark, but it should not be treated as proof that any one bottleneck is tight. If a single-name report strongly outperforms or underperforms SMH, that spread becomes a research question: did the company validate a real layer-specific constraint, or did it simply ride the same semiconductor beta?

## 1. ETF Role And Benchmark Job

SMH's job is to provide a control line for the semiconductor reports. The ETF spans designers, foundry, equipment, memory, analog, and semiconductor-adjacent architecture names. That breadth makes it a benchmark, not a direct falsification node.

| Benchmark job | Why it matters | How to use it |
|---|---|---|
| Semis beta control | Separates single-name thesis alpha from broad AI-chip momentum | Compare each semis report's rerun return against SMH over the same window |
| Concentration check | NVIDIA and TSMC dominate enough to shape ETF returns | Avoid calling SMH a diversified supply-chain proof point |
| Layer sanity check | Equipment, foundry, memory, and design names all sit in one basket | Use dispersion among holdings to locate the real bottleneck |
| Risk sleeve | Captures ETF-level drawdown, inflow, and sentiment risk | Compare single-name volatility against the benchmark |

SMH therefore follows the IGV precedent: it is a report in `reports.json`, tagged as an ETF, but it does not carry a `chainLayer` and does not render as a coverage-map node.

## 2. Holdings And Concentration

The ETF is market-cap weighted and concentrated in the largest AI semiconductor winners. As of VanEck's July 1, 2026 holdings snapshot:

| Rank | Holding | Ticker | Weight |
|---:|---|---|---:|
| 1 | NVIDIA | NVDA | 18.41% |
| 2 | Taiwan Semiconductor Manufacturing | TSM | 9.18% |
| 3 | Advanced Micro Devices | AMD | 5.57% |
| 4 | Applied Materials | AMAT | 5.49% |
| 5 | Broadcom | AVGO | 5.49% |
| 6 | Micron Technology | MU | 5.39% |
| 7 | KLA | KLAC | 5.10% |
| 8 | Lam Research | LRCX | 4.97% |
| 9 | ASML Holding | ASML | 4.96% |
| 10 | Intel | INTC | 4.92% |

The top ten holdings total roughly 69.5% by the listed weights above. That is useful for benchmark power, but it means SMH can behave more like a concentrated AI-semiconductor momentum sleeve than a broad industrial ETF.

**Update (2026-10-02)**: **holdings as of October 1, 2026 (VanEck daily holdings, 26 holdings plus cash).** An index change between 2026-08-31 and 2026-10-01 altered the mix. NVIDIA's weight was 22.82% in the 2026-08-31 factsheet and is 19.27% in the 2026-10-01 daily file. SK hynix entered through its Nasdaq-listed ADS (SKHY) at 4.55%; the 2026-08-31 country breakdown showed no Korean exposure. Texas Instruments (4.51%) sits just outside the top ten, behind Lam Research by market value.

| Rank | Holding | Ticker | Weight (2026-10-01) |
|---:|---|---|---:|
| 1 | NVIDIA | NVDA | 19.27% |
| 2 | Taiwan Semiconductor Manufacturing | TSM | 9.16% |
| 3 | Advanced Micro Devices | AMD | 5.52% |
| 4 | Broadcom | AVGO | 5.01% |
| 5 | Micron Technology | MU | 4.98% |
| 6 | Intel | INTC | 4.73% |
| 7 | Applied Materials | AMAT | 4.73% |
| 8 | KLA | KLAC | 4.59% |
| 9 | SK hynix (ADS) | SKHY | 4.55% |
| 10 | Lam Research | LRCX | 4.51% |

The top ten now total 67.05%, and NVIDIA plus TSMC total 28.43%. Memory (Micron plus SK hynix) is now 9.53% of the fund, up from 5.39% (Micron alone) on July 1.

## 3. Performance And Risk Snapshot

| Metric | Issuer snapshot |
|---|---:|
| NAV | ~~$592.26 as of July 2, 2026~~ **Update (2026-10-02)**: $617.90 as of October 1, 2026 |
| Total net assets | ~~$68.82B as of July 2, 2026~~ **Update (2026-10-02)**: $75.75B as of October 1, 2026 |
| Total expense ratio | 0.35% |
| Inception date | December 20, 2011 |
| Total holdings | 26 as of July 1, 2026 (26 as of October 1, 2026) |
| YTD return shown on issuer page | ~~64.47% as of July 2, 2026~~ **Update (2026-10-02)**: 71.59% as of October 1, 2026 |

The YTD return shows how much of the 2026 tape has become semiconductor-led. That makes SMH a good benchmark for AI-semiconductor exposure, but it also means the ETF is vulnerable to a group de-rating if AI-capex expectations, GPU supply, memory pricing, or export-control assumptions reset together.

### 3.1 Current Multiples At The New Anchor (Update 2026-10-02)

**Method.** VanEck publishes a fund-level trailing P/E but no forward P/E. The forward figures below are this report's estimate. Fund earnings per unit is the sum, over the 25 equity holdings, of each holding's weight × ($617.81 ÷ its 2026-10-01 close) × its EPS. EPS is Nasdaq's street (adjusted) basis: the last four reported quarters for trailing, the next four consensus quarters for NTM, and fiscal-year consensus calendarized to CY2027 and CY2028. The holdings-based trailing figure (40.2x) reconciles with VanEck's own 37.21x at the 2026-08-31 close of $556.63, rescaled to today's price (about 41.3x). That reconciliation is why the aggregation is treated as a usable estimate rather than a black box.

| Metric | Value | Basis | Source / label |
|---|---:|---|---|
| Price (2026-10-01 close) | $617.81 | Regular session | Nasdaq historical; CNBC cross-check |
| NAV / total net assets | $617.90 / $75.75B | 2026-10-01 | VanEck (fund data) |
| 52-week closing range | $325.10 (2025-11-20) - $668.91 (2026-06-22) | Closes | Nasdaq historical |
| 1-year price change | +85.14% | From the 2025-10-01 close of $333.69 | Nasdaq historical |
| Trailing P/E (fund) | 37.21x | 2026-08-31 | VanEck factsheet (fund data) |
| Trailing P/E rescaled to 2026-10-01 | about 41.3x | 37.21x × $617.81 / $556.63 | Estimate |
| Holdings-based trailing P/E | 40.2x (fund EPS $15.37) | 95.4% of weight (SK hynix excluded) | Estimate (Nasdaq data) |
| Holdings-based NTM P/E | **22.4x** (fund EPS $27.58) | Next four consensus quarters | Estimate (Nasdaq consensus) |
| P/E on CY2026E | 27.5x (fund EPS $22.46) | Calendarized consensus | Estimate |
| P/E on CY2027E | 19.4x (fund EPS $31.84) | Calendarized consensus | Estimate |
| P/E on CY2028E | 15.6x (fund EPS $39.69) | Calendarized consensus | Estimate |
| Consensus fund EPS growth | CY2027 +41.8%, CY2028 +24.7%; CY2026-28 CAGR 32.9% | From the rows above | Estimate |
| Price/book (fund) | 11.12x | 2026-08-31 | VanEck factsheet (fund data) |
| Weighted average market cap | $1,766,184M | 2026-08-31 | VanEck factsheet (fund data) |
| Distribution yield / 30-day SEC yield | 0.18% / 0.15% | 2026-10-01 | VanEck (fund data) |

**What the consensus path assumes.** Street consensus has fund earnings per unit rising about 77% from CY2026 to CY2028. The memory names already show the Street expecting a cycle turn inside the holding window. Micron's fiscal-year consensus EPS is $164.16 for FY Aug-2028 and $139.33 for FY Aug-2029. SK hynix's is $37.38 per ADS for CY2028 and $26.97 for CY2029 (Nasdaq consensus, 2026-10-01). Together these two names are 9.53% of the fund.

### 3.2 Scenario Grid (Update 2026-10-02)

**Mechanics.**
- **Holding period:** 2026-10-02 to 2028-12-31, 821 days = 2.248 years. Weights are multiples of 10 summing to 100.
- **Exit value:** value per unit at the end of 2028 = CY2028 fund EPS × the exit P/E. The exit P/E is a trailing multiple on CY2028 earnings, since CY2029 consensus is too sparse to use.
- **Price-only:** distributions (0.18% yield) are excluded, and the 0.35% expense ratio is not separately deducted. The net bias is under 0.2 points a year.
- **No balance sheet:** an ETF has no net cash or share count of its own. Per-unit earnings is the only path variable.
- **Exit-multiple anchors:** today's structure, 40.2x trailing and 22.4x NTM. A 22x trailing exit is consistent with a market paying about 20x forward for low-teens growth at the end of 2028. These multiples are assumptions, not historical averages.

| Scenario | CY2027 fund EPS | CY2028 growth | CY2028 fund EPS (CY2026-28 CAGR) | Exit trailing P/E | Value per unit | Versus $617.81 | Annualized | Weight |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Bull: AI capex broadens through 2028, consensus beaten | $33.43 (consensus +5%) | +25% | $41.79 (36.4%) | 26x | $1,086.54 | +75.9% | +28.6% | 30% |
| Base: 2027 consensus delivered, 2028 growth half of consensus | $31.84 (consensus) | +12% | $35.66 (26.0%) | 22x | $784.54 | +27.0% | +11.2% | 40% |
| Bear: memory/WFE digestion arrives a year before the Street's 2029 turn | $25.83 (CY2026 +15%) | −15% | $21.95 (−1.1%) | 18x | $395.18 | −36.0% | −18.0% | 30% |
| **Weighted** | - | - | - | - | **$758.33** | **+22.7%** | **+9.5%** | **100%** |

**The probability-weighted annualized return of +9.5% is 1.5 points above the 8% hurdle and 0.5 points below 10%.**

### 3.3 Sensitivity Test (Update 2026-10-02)

| Test | Setting | Weighted value per unit | Weighted annualized return | Clears 8%? |
|---|---|---:|---:|---|
| Base | Exits 26x / 22x / 18x; paths as above; weights 30/40/30 | $758.33 | +9.5% | Yes (just) |
| Exit multiples −3 turns | 23x / 19x / 15x | $658.17 | +2.9% | **No** |
| Exit multiples +3 turns | 29x / 25x / 21x | $858.50 | +15.8% | Yes |
| Exit multiples −5 turns | 21x / 17x / 13x | $591.39 | −1.9% | **No** |
| Slower growth | CY2028 fund EPS −10% in every scenario | $682.50 | +4.5% | **No** |
| Both | −3 turns and −10% EPS | $592.35 | −1.9% | **No** |
| Re-weighted toward bear | 20/40/40 | $689.20 | +5.0% | **No** |
| Heavily bear-weighted | 10/40/50 | $620.06 | +0.2% | **No** |
| Re-weighted toward bull | 40/40/20 | $827.47 | +13.9% | Yes |

**The balanced reading is real at central assumptions but not robust in either direction.** Three turns of multiple, a 10% earnings shortfall or one notch of weight is enough to move the result out of the 8-10% band, toward either side. That is why the stance is neutral-watch and conviction is low.

### 3.4 Reverse Test: What The Price Requires (Update 2026-10-02)

To earn 8% (10%) a year, SMH must be worth $734.49 ($765.41) per unit at the end of 2028; holding today's price requires $617.81. For each exit P/E, the table solves for the CY2028 fund EPS that produces that value. It then shows the implied CY2026-28 CAGR from the $22.46 CY2026 base and the gap to the $39.69 consensus. **ETF adaptation:** the brief's rule that cash and share count move with the path has no ETF analogue, so per-unit earnings is the only variable that moves.

| Exit trailing P/E | Break-even (0%): CY2028 EPS / CAGR / vs consensus | 8%: CY2028 EPS needed | 8%: implied CAGR / vs consensus | 10%: CY2028 EPS needed | 10%: implied CAGR / vs consensus |
|---:|---|---:|---|---:|---|
| 16x | $38.61 / 31.1% / −2.7% | $45.91 | **43.0%** / +15.7% | $47.84 | 45.9% / +20.5% |
| 18.5x | $33.40 / 21.9% / −15.9% | $39.70 | **33.0%** / +0.0% | $41.37 | 35.7% / +4.2% |
| 20x | $30.89 / 17.3% / −22.2% | $36.72 | **27.9%** / −7.5% | $38.27 | 30.5% / −3.6% |
| 22x | $28.08 / 11.8% / −29.3% | $33.39 | **21.9%** / −15.9% | $34.79 | 24.5% / −12.3% |
| 26x | $23.76 / 2.9% / −40.1% | $28.25 | **12.2%** / −28.8% | $29.44 | 14.5% / −25.8% |

Holding the base-case earnings path fixed ($35.66) and varying only the exit multiple: 20x gives $713.20 (+6.6% annualized) and 18x gives $641.88 (+1.7%).

**The expectations gap in one sentence:** at $617.81, earning 8% requires either the full Street CY2028 fund EPS of $39.69 at an 18.5x trailing exit, or CY2028 EPS 15.9% below consensus ($33.39) at a 22x exit. Our base case sits between the two ($35.66 at 22x), so the price already pays for most of the consensus supercycle and leaves little margin if the 2029 memory turn arrives early.

## 4. Bull Case

The bull case is that SMH remains the cleanest liquid way to own the AI semiconductor cycle without choosing one exact bottleneck.

1. AI infrastructure spending still has to flow through GPUs, foundry, memory, equipment, networking silicon, and EDA.
2. The ETF holds several covered research-hub names in one basket, including NVDA, TSM, AMAT, AVGO, MU, KLAC, LRCX, ASML, CDNS, SNPS, MRVL, and ALAB.
3. Large AUM and long operating history make it practical as a benchmark and trading sleeve.
4. If the AI capex cycle remains broad, SMH can participate even when the winning layer rotates.

Upside context is not a target price. The constructive read is that SMH should keep working if the research hub's semicap, foundry, memory, networking, and custom-silicon monitors confirm each other rather than diverge.

**Update (2026-10-02)**: in numbers, the bull case (30% weight, §3.2) requires CY2027 fund EPS about 5% above the $31.84 consensus and another +25% in 2028, valued at 26x trailing. That gives $1,086.54 per unit, +28.6% annualized.

## 5. Bear Case

The bear case is concentration and cyclicality. SMH can look diversified while still being dominated by a few high-expectation names and by one macro narrative.

1. NVIDIA and TSMC together were about 27.6% of the July 1 holdings snapshot. **Update (2026-10-02)**: 28.43% on October 1, after peaking at 32.36% in the 2026-08-31 factsheet before the index change that took effect by 2026-10-01.
2. Equipment names are sensitive to order digestion, China restrictions, and WFE cyclicality.
3. Memory and foundry can re-rate quickly if AI demand turns into inventory digestion.
4. The ETF's strong 2026 YTD return raises the hurdle for future confirmation.
5. ETF ownership does not remove semiconductor-cycle risk; it mostly spreads single-name execution risk.

The thesis-breaking condition is broad divergence: if chip designers stay strong but equipment, memory, foundry, and packaging reports fail to confirm, SMH is no longer a clean AI-capex confirmation signal.

**Update (2026-10-02)**: in numbers, the bear case (30% weight, §3.2) has the digestion that the Street already pencils in for memory in 2029 arriving a year early. CY2027 fund EPS reaches only $25.83 and CY2028 falls 15% to $21.95, at 18x trailing. That gives $395.18 per unit, −18.0% annualized.

## 6. Monitoring Checklist

| Monitor | Trigger | Interpretation |
|---|---|---|
| Top-holding concentration | NVDA/TSM weight keeps rising | ETF becomes less useful as broad semis beta |
| Equipment confirmation | ASML/AMAT/LRCX/KLAC order and backlog reads weaken | AI capex may not be converting into tool demand |
| Foundry and memory confirmation | TSM/MU/SK hynix reports diverge from designer strength | Supply-chain bottleneck may be narrower than the ETF suggests |
| ETF flows / AUM | AUM changes faster than NAV movement | Sentiment and allocation flows may be driving price action |
| Export-control sensitivity | China restrictions hit equipment or advanced chips | ETF can de-rate at basket level even without a single-name miss |

**Update (2026-10-02)**: **current checklist (corresponds one-to-one with `monitoring[]` in reports.json; the table above is the historical July version).**

| # | id | Metric | Trigger | Latest reading | Next check |
|---:|---|---|---|---|---|
| 1 | top-holding-concentration | NVIDIA plus TSMC weight | NVDA + TSM combined weight above 33% in VanEck daily holdings | 28.43% on 2026-10-01 (NVDA 19.27%, TSM 9.16%) after the index change between 2026-08-31 and 2026-10-01; 32.36% in the 2026-08-31 factsheet (22.82% / 9.54%); 27.59% on 2026-07-01 | Next index review (cadence not verified in this backfill) |
| 2 | equipment-confirmation | Semicap guidance and consensus growth | Two or more of ASML/AMAT/LRCX/KLAC guide next-quarter revenue below the prior quarter, or consensus CY2027 EPS growth for the four falls below +15% | Nasdaq consensus (2026-10-01): CY2027 EPS growth AMAT +31.2%, KLAC +32.9%, LRCX +34.0%, ASML +32.9%. AMAT Q3 FY2026 revenue was $9,115M (+25% y/y), with Q4 guided at $10,250M ± $500M (8-K, 2026-08-13) | ASML Q3 2026 results, mid-October 2026 (estimated) |
| 3 | foundry-memory-confirmation | Memory and foundry consensus | CY2028 consensus EPS for Micron or SK hynix cut by more than 15% from the 2026-10-01 levels ($155.88 / $37.38, calendarized) | Micron reported FQ4 FY2026 (August quarter) EPS of $33.19 on 2026-09-30. Consensus is $164.16 for FY Aug-2028 and $139.33 for FY Aug-2029; SK hynix is $37.38 for CY2028 and $26.97 for CY2029 per ADS; TSMC is $16.56 / $21.33 / $25.92 per ADR for CY2026-28. TSMC monthly revenue was not fetched in this backfill | TSMC Q3 2026 results, October 2026 (estimated) |
| 4 | etf-flows-aum | Total net assets versus NAV | Over any calendar quarter, AUM growth exceeds NAV growth by more than 10 percentage points, or implied units outstanding fall by more than 5% | From 2026-07-02 to 2026-10-01, total net assets rose 10.1% to $75.75B against NAV +4.3% to $617.90, implying about +5.5% units (estimate) | Year-end 2026 issuer snapshot |
| 5 | export-control-sensitivity | U.S./China chip and tool restrictions | A new U.S. or Chinese rule restricting advanced chips, HBM or fabrication tools that any top-10 holding describes as material in a filing or results release | No new rule identified in this backfill (2026-10-02; not a full regulatory sweep). AMAT's Q3 FY2026 release (2026-08-13) listed China as the only region declining year over year | Continuous; Q3 2026 filings in October-November 2026 |
| 6 | fund-forward-valuation | Holdings-based NTM P/E | NTM P/E above 26x, or below 19x while CY2027 consensus fund EPS stays at or above $30.25 | 22.4x NTM and 40.2x trailing at $617.81 on 2026-10-01 (estimate); VanEck fund trailing P/E 37.21x at 2026-08-31, about 41.3x rescaled | Monthly; next after Nvidia's Q3 FY2027 results, November 2026 (estimated) |
| 7 | consensus-revisions | Holdings-weighted consensus fund EPS | CY2027 consensus fund EPS below $28.66 (−10% versus $31.84), or CY2028 above $43.66 (+10% versus $39.69) | 2026-10-01: CY2026 / CY2027 / CY2028 fund EPS of $22.46 / $31.84 / $39.69 per unit (Nasdaq consensus aggregation, estimate) | After the Q3 2026 reporting season, November 2026 |

## 7. Conclusion

SMH belongs in the research hub as a benchmark ETF, not as a coverage-map node. It answers a different question from the single-name reports: what did broad semiconductor exposure do while the chain-specific thesis was being tested?

Use SMH as the control sleeve for semis. When a covered name beats SMH, ask whether its layer-specific bottleneck strengthened. When it lags SMH, ask whether the company failed to convert broad AI beta into its own financial evidence. ~~The current classification is **lite benchmark / neutral control sleeve**.~~

**Update (2026-10-02)**: **stance conclusion.**

**(1) The expectations gap in one sentence.** At $617.81, earning the 8% hurdle requires either the full Street CY2028 fund EPS of $39.69 at an 18.5x trailing exit, or EPS 15.9% below consensus ($33.39) at 22x. Our base case ($35.66 at 22x) sits between the two, so the price already pays for most of the consensus supercycle.

**(2) Stance and conviction.**
- **The grid:** the 30/40/30 grid (bull $1,086.54 / base $784.54 / bear $395.18) weights to **$758.33 per unit, +22.7% against $617.81, or +9.5% annualized** over 2.248 years. That is 1.5 points above the 8% hurdle and 0.5 points below 10%, with +75.9% in the bull case against −36.0% in the bear case. Hence **stance: neutral-watch**.
- **This is an absolute call on the benchmark, not a relative one.** It does not rank SMH against any covered single name. The control-sleeve job above is unchanged.
- **Why not constructive:** the weighted result sits inside the hurdle band rather than clearly above it. A 3-turn multiple cut (+2.9%), a 10% earnings shortfall (+4.5%) or a 20/40/40 weighting (+5.0%) each fail the hurdle. The Street already models memory earnings falling in 2029.
- **Why not cautious:** at central assumptions the weighted return still clears 8%. The base case assumes CY2028 earnings 10% below consensus. Three turns of multiple expansion take the result to +15.8%.
- **Why conviction is low:** the neutral reading moves out of the band under modest shocks in either direction. Out-year consensus has few estimates. Two inputs carry data caveats: the currency basis of ASML's EPS and the single reported quarter for SK hynix.

**(3) Upgrade and downgrade triggers (identical clause by clause to `stanceTriggers` in reports.json).**
- **Upgrade to constructive** if either of the following holds:
  - The holdings-based NTM P/E falls below 19x while CY2027 consensus fund EPS stays at or above $30.25 (no more than 5% below the 2026-10-01 $31.84).
  - CY2028 consensus fund EPS rises above $43.66 (+10% versus $39.69) while the NTM P/E stays at or below 24x.
- **Downgrade to cautious** if any one of the following holds:
  - The holdings-based NTM P/E rises above 26x.
  - CY2027 consensus fund EPS falls below $28.66 (−10% versus $31.84).
  - CY2028 consensus EPS for Micron or SK hynix is cut by more than 15% from the 2026-10-01 levels ($155.88 / $37.38, calendarized).
  - A new U.S. or Chinese export-control rule restricting advanced chips, HBM or fabrication tools is described as material by a top-10 holding.

## Appendix: Sources And Assumptions

- VanEck SMH issuer page, accessed July 6, 2026: https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/
- NAV, net assets, expense ratio, inception date, YTD return, total holdings, and daily holdings are from VanEck's issuer page snapshots dated July 1-2, 2026.
- This ETF report intentionally has no `chainLayer`: SMH spans multiple semiconductor layers and is used as a benchmark/control sleeve rather than a single bottleneck report.

**Update (2026-10-02)**: **sources, method and data gaps for the stance backfill.**
- **Price anchor:** the 2026-10-01 close of $617.81 is from the Nasdaq historical-quotes API (assetclass=etf), cross-checked against the CNBC quote service (last $617.81, dated 2026-10-01). The same Nasdaq series supplies the 52-week range and the YTD and 1-year changes.
- **VanEck fund data:**
  - The issuer page (accessed 2026-10-02) gives NAV $617.90, total net assets $75.75B, YTD 71.59% and 0.35% total expense ratio, all as of 2026-10-01.
  - The daily holdings file is dated 2026-10-01: 26 holdings plus cash.
  - Fund details as of 2026-10-01: 0.18% distribution yield and 0.15% 30-day SEC yield.
  - The SMH factsheet (https://www.vaneck.com/us/en/investments/semiconductor-etf-smh-fact-sheet.pdf) is as of 2026-08-31: P/E 37.21, P/B 11.12, weighted average market cap $1,766,184M, top-10 and country weights.
- **Consensus and EPS:** per-holding EPS comes from the Nasdaq earnings-surprise API (last four reported quarters) and the earnings-forecast API (quarterly and fiscal-year consensus), fetched 2026-10-02. Per-holding closes are the 2026-10-01 closes from Nasdaq historical.
- **Calendarization:** CY2026 uses fiscal-year consensus for December year-ends and mapped actual-plus-forecast quarters for the others. CY2027 and CY2028 blend fiscal years by months of overlap. Broadcom, Qualcomm and Synopsys FY2029 are held flat at FY2028 where needed.
- **Data gaps (estimates and limits):**
  - SK hynix has only one reported quarter on Nasdaq, so it is excluded from the trailing figure (95.4% weight coverage).
  - The currency basis of ASML's EPS against its USD ADR price is unverified (4.39% weight); if the EPS is in euros, ASML's multiples are understated.
  - Qualcomm's trailing EPS exceeds its NTM consensus.
  - Out-year consensus has few estimates.
  - Weights are frozen at 2026-10-01, although the index composition changes over time (rebalance cadence not verified in this backfill).
  - The fund-level forward P/Es, the scenario values and the exit multiples are this report's estimates, not VanEck data.
  - TSMC monthly revenue and ASML bookings were not fetched in this backfill.
  - The AMAT Q3 FY2026 figures in the equipment-confirmation row ($9,115M revenue, +25% y/y, Q4 guide $10,250M ± $500M) are taken from the research hub's signal log entry `amat-q3-fy2026-record-revenue-dram-mix`, which cites AMAT's 2026-08-13 8-K and Exhibit 99.1; they were not re-fetched in this backfill.
