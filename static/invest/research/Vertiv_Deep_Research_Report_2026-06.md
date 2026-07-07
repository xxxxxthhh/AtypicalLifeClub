# Vertiv (VRT) Deep Research Report

Coverage date: 2026-06-30
Last updated: 2026-07-07
Ticker: NYSE: VRT
Disclaimer: This report is for informational and research purposes only. It does not constitute investment advice. Please conduct your own due diligence. All prices and market caps are point-in-time snapshots; financial figures are per company disclosure unless noted otherwise.

> **Background note:** Vertiv Holdings (formerly Emerson Network Power) provides the power, thermal/cooling, and IT-infrastructure hardware and services that sit *inside* the data center — UPS, switchgear/busbar, air and liquid cooling, integrated racks, prefabricated modules, and lifecycle services. It went public in 2020 via a SPAC led by David Cote (ex-Honeywell CEO). This report is **initial coverage**, and it is framed deliberately as a **demand "dashboard"** for this center's AI-infrastructure chain: read alongside NVIDIA, Broadcom, Corning, GE Vernova, Bloom Energy and SanDisk. Vertiv answers "how does power and heat actually get into the room and the rack" — and its orders/backlog are among the most real-time, hardest-to-fake reads on whether the AI data-center buildout is genuinely proceeding versus merely being announced.

---

## Executive Summary

**One-line thesis:** Vertiv is the picks-and-shovels supplier of data-center power and thermal management — the layer between "where the electricity comes from" (GE Vernova / Bloom / Oklo) and "the chips that consume it" (NVIDIA / Broadcom). As AI racks jump from ~10kW to 100kW+ and force the industry from air to liquid cooling, Vertiv's Q1 2026 print shows the pull: revenue **+30% to $2.65B** (+23% organic, Americas +44% organic), adjusted operating margin **20.8%** (+430bps), adjusted EPS **$1.17** (+83%); the latest disclosed backlog was **$15.0B** at Q4 2025 (+109% Y/Y, reported February 2026). The order book is the tell, but its date matters: this is the most recent backlog anchor, not a Q1 2026 balance.

**Verdict:** **Cautious / medium conviction: high-quality franchise, but the price implies a near-perfect buildout pace.** Vertiv is arguably the cleanest single barometer of AI-capex *velocity*, and execution (margin, FCF, backlog) is excellent. But the stock has roughly **tripled in a year** to **$306.97** (~**$117.9B** market cap, ~**48x** FY2026E adjusted EPS, ~**80x** trailing GAAP), so it already prices in years of sustained buildout. The debate is not whether AI data-center demand is real (the latest disclosed backlog supports it) but whether the *pace* holds — because Vertiv's high-beta order book cuts both ways.

**Current market read (latest market-data snapshot, 2026-06-29 close):** VRT closed **$306.97** on 2026-06-29, below quote-source/IBD references to a 52-week/all-time high near **$379.94** in May 2026. On ~**384M** shares, market cap is ~**$117.9B** (~$146B at the ~$379.94 high); with ~$3.26B debt securities and finance-lease obligations and ~$2.50B cash (net debt ~**$0.76B**, excluding operating lease liabilities), enterprise value is ~**$118.7B**. The stock is up roughly **100% YTD** and about 3x over the past year. Financial source: [Vertiv Q1 2026 8-K (SEC)](https://www.sec.gov/Archives/edgar/data/0001674101/000162828026026379/q12026exhibit991vrt04222026.htm); quote references: [Yahoo Finance VRT](https://finance.yahoo.com/quote/VRT/), [StockAnalysis VRT](https://stockanalysis.com/stocks/vrt/), [Investor's Business Daily VRT profile](https://www.investors.com/stock-lists/sector-leaders/vertiv-vrt-stock-ai/).

**Key data:**

| Metric | Value |
|--------|-------|
| Price (2026-06-29 close) | $306.97 (below a quote-source/IBD high near $379.94) |
| Market cap | ~$117.9B (~384M shares; ~$146B at the ~$379.94 high) |
| Net debt / EV | ~$0.76B net debt ($3.26B debt securities + finance leases − $2.50B cash); EV ~$118.7B |
| Forward P/E | ~48x (FY2026E adj EPS $6.30-6.40); ~54x (FY2026E GAAP $5.60-5.70) |
| Trailing P/E (GAAP) | ~80x |
| EV/EBITDA (FY2026E, est.) | ~34x; EV/Sales ~8.6x |
| Q1 2026 net sales | $2,650M (+30% Y/Y; +23% organic, +4% M&A, +3% FX) |
| Q1 2026 Americas organic | +44% |
| Q1 2026 adj operating margin | 20.8% (+430bps Y/Y) |
| Q1 2026 adj diluted EPS | $1.17 (+83%); GAAP net income $390M (+137%) |
| Q1 2026 adj free cash flow | $653M (+147%) |
| Backlog | $15.0B (Q4 2025, +109% Y/Y); book-to-bill well above 1x |
| FY2026 guidance (raised) | revenue $13.5-14.0B (organic +29-31%); adj EPS $6.30-6.40 (+51% mid); adj op margin ~23.3% |
| Liquid-cooling position | Directionally a leading vendor; public share/TAM estimates vary and are treated as industry estimates, not audited company disclosure |
| Primary competitors | Schneider Electric, Eaton, Modine, Rittal, Stulz |
| CEO / Exec Chairman | Giordano "Gio" Albertazzi / David Cote |

---

## 1. Business Overview

Vertiv designs, manufactures and services the **critical digital infrastructure** inside data centers, communication networks, and commercial/industrial facilities. Its offerings span four functional areas, sold globally and reported in three geographic segments (**Americas, Asia Pacific, EMEA**):

- **Power management:** UPS systems, switchgear, busbar/busway, power distribution, DC power — the equipment that conditions and routes electricity from the building feed to the rack. Bolstered by recent acquisitions in switchgear/busbar (e.g., E&I/Powerbar).
- **Thermal management (the growth engine):** air cooling (CRAC/CRAH, chillers) and, increasingly, **liquid cooling** — the CoolChip CDU family (70kW–1,350kW), direct-to-chip cold plates, and immersion. This is where AI density (100kW+ racks) is forcing a generational shift.
- **Integrated rack & modular solutions:** prefabricated, factory-integrated power+cooling modules that compress data-center construction time — increasingly valued as hyperscalers race to energize capacity.
- **Services & spares:** installation, monitoring, maintenance, lifecycle management — a recurring, higher-margin annuity attached to the installed base.

**The business model:** Vertiv sells mission-critical hardware where downtime is catastrophic, then attaches multi-year service. Revenue is **order-driven and increasingly long-cycle**: large hyperscale projects are booked into backlog and recognized as built, so **orders and backlog lead revenue by several quarters** — which is exactly what makes Vertiv a forward read on the buildout. Q1 2026 adjusted FCF of $653M (+147%) shows the model converts growth to cash as it scales.

---

## 2. Industry & Competitive Position

### 2.1 The AI density shift: air → liquid, the key inflection

AI accelerators have pushed rack power density from ~10–15kW (traditional) toward **100kW+** (GB200/GB300-class racks), beyond what air cooling can dissipate. This forces **liquid cooling** (direct-to-chip today, immersion emerging) from a niche into a default design path for AI halls. Public market-size and share estimates vary materially by definition, so this report treats exact liquid-cooling TAM/share numbers as directional industry estimates rather than company-disclosed facts. The investable point is simpler: Vertiv has a full portfolio (CDUs, direct-to-chip, immersion) and the power+thermal+integration breadth to sell the whole "grey space." This is the structural tailwind beneath the +30% Q1 revenue growth and the Q4 2025 backlog.

### 2.2 Competitive landscape: a two-horse race, with diversified giants closing in

| Player | Position | Note |
|--------|----------|------|
| **Vertiv** | Directionally one of the leading DC power+thermal/liquid-cooling vendors | Most AI-data-center-pure of the majors |
| **Schneider Electric** | Close peer/leader in broader electrical + data-center infrastructure | Larger, more diversified (electrification) |
| **Eaton** | Closing in; bought Boyd Thermal (Mar 2026) | Diversified electrical; grid + DC |
| **Others** | Rittal, Stulz, Modine, Boyd | Fragmented specialist set; share estimates are directional |

Industry press and research summaries generally frame Vertiv and Schneider as top-tier competitors, but the precise share split is less audit-ready than the company financials. Vertiv's edge is focus and portfolio breadth (power + thermal + integrated modular + services under one roof); the risk is that diversified giants (Schneider, Eaton) with deeper electrical franchises and balance sheets press hard, and that cooling hardware faces price competition as capacity expands.

### 2.3 Why Vertiv is the chain's "dashboard"

Vertiv sits at a chokepoint where AI-capex intentions become physical commitments: a hyperscaler cannot energize GPUs without power and cooling gear, and that gear is **ordered before the chips ship**. So Vertiv's **orders, book-to-bill and backlog are a leading, hard-to-fake indicator** of buildout velocity — cross-validating the demand assumptions embedded in this center's NVIDIA, Broadcom, Corning, GE Vernova and Bloom reports. The latest disclosed backlog anchor is Q4 2025: $15.0B (+109%) and book-to-bill ~2.9x, meaning the pipeline was filling faster than it drained at that point. The corollary: a sharp deceleration in Vertiv orders would be one of the **earliest warnings** for the entire AI-infrastructure chain.

---

## 3. Financial Health

### 3.1 Q1 2026: growth, margin and cash all inflecting up

| Metric | Q1 2026 | Q1 2025 | Change |
|--------|---------|---------|--------|
| Net sales | $2,650M | ~$2,036M | +30% (+23% organic) |
| Adj operating profit | $551M | ~$336M | +64% |
| Adj operating margin | 20.8% | ~16.5% | +430bps |
| GAAP operating profit | $440M | — | — |
| GAAP net income | $390M | ~$165M | +137% |
| Adj diluted EPS | $1.17 | $0.64 | +83% |
| Adj free cash flow | $653M | ~$264M | +147% |

The print is high quality: growth is **mostly organic** (+23%), margin expansion is structural (operating leverage + mix toward higher-value thermal/integrated), and cash conversion is strong (adj FCF $653M). Americas organic +44% reflects the U.S. hyperscale buildout directly.

### 3.2 Balance sheet & cash: modest leverage, self-funding growth

- **Cash ~$2.50B; total debt ~$3.26B; net debt ~$0.76B** — light leverage (net debt < 0.3x FY2026E EBITDA), a meaningful contrast to the heavier balance sheets elsewhere in the chain.
- **Adjusted FCF $653M in Q1** (+147%), funding capacity expansion, bolt-on M&A (switchgear/busbar, thermal) and buybacks/dividend without balance-sheet strain.
- Capital intensity is moderate (assembly/integration, not fabs), so incremental AI demand drops through to cash efficiently.

### 3.3 Guidance: raised, and implying sustained momentum

| Metric | FY2026 guidance (raised) |
|--------|--------------------------|
| Net sales | $13.5B – $14.0B (organic +29–31%) |
| Adj operating margin | ~23.3% |
| GAAP diluted EPS | $5.60 – $5.70 |
| Adj diluted EPS | $6.30 – $6.40 (+51% at midpoint) |

Management *raised* full-year guidance on the Q1 print, implying ~30% organic growth and continued margin expansion to ~23%. The raise — following the record Q4 2025 backlog — is the clearest signal that order momentum is being converted, not just promised.

---

## 4. Management & Governance

**CEO Giordano "Gio" Albertazzi** (CEO since Jan 2023, long-time Vertiv/Emerson operator) leads execution; **Executive Chairman David Cote** (ex-Honeywell CEO, who took Vertiv public) anchors capital allocation and discipline; **CFO Craig Chamberlin** signed the Q1 2026 10-Q. Observations:

- **Operating execution:** margin +430bps Y/Y and adj FCF +147% show the team is converting the AI surge into profit and cash, not just revenue — the key test for a hardware scaler.
- **Capital allocation:** bolt-on M&A into adjacent high-value areas (switchgear/busbar, thermal) plus buybacks and a dividend; net debt kept light through a hyper-growth phase.
- **Cyclical memory:** this management has run Vertiv through the slower pre-AI cycle, which matters — the franchise is not a pure-play startup riding one wave.
- **Watch item:** the gap between GAAP and adjusted figures (GAAP EPS $5.60-5.70 vs adj $6.30-6.40) — track what "adjusted" excludes (amortization, stock comp, restructuring) over time.

**Management grade: A- (excellent operating conversion of the AI surge, disciplined balance sheet, experienced through-cycle leadership; the test ahead is sustaining margin and order quality as competition and scale intensify).**

---

## 5. Bull Case

**Core thesis:** Vertiv is a high-quality, well-run beneficiary of a multi-year, density-driven shift in data-center power and cooling, with Q1 guidance and the Q4 2025 backlog showing that demand is contracted, not merely hoped-for.

1. **The Q4 2025 backlog is the proof point.** $15.0B (+109% Y/Y) and book-to-bill ~2.9x meant demand was being booked faster than shipped — multi-quarter forward visibility no ordinary capital-goods firm has.
2. **Liquid cooling is a generational inflection.** 100kW+ AI racks force air→liquid; Vertiv has the full portfolio (CDU 70kW-1,350kW, direct-to-chip, immersion), while exact share/TAM estimates should be treated as directional industry inputs.
3. **Margins and cash are inflecting structurally.** Adj op margin 20.8% (+430bps) heading to ~23.3%; adj FCF +147% — operating leverage plus mix, self-funding growth on light leverage.
4. **Breadth = wallet share.** Power + thermal + integrated modular + services under one roof lets Vertiv sell the whole grey space and attach recurring service — stickier than point-product rivals.
5. **Cleanest AI-capex velocity read.** As a chokepoint between power and chips, Vertiv's order book is a leading indicator the rest of the chain lacks — and right now it is accelerating.

---

## 6. Bear Case

**Core thesis:** at ~$117.9B and ~48x forward adjusted EPS after a ~3x year, Vertiv prices in years of uninterrupted hyperscale buildout — and its high-beta order book means any deceleration hits hard and early.

1. **Valuation leaves no slack.** ~48x FY2026E adj EPS, ~54x GAAP, ~80x trailing, ~8.6x EV/Sales — priced for sustained ~30% growth; any wobble in AI-capex pace de-rates it fast.
2. **High beta to AI capex — both ways.** The same order book that signals strength would signal weakness first: a hyperscaler digestion phase, project delays, or capex reprioritization show up in Vertiv orders before almost anywhere else.
3. **Order lumpiness & book-to-bill optics.** A book-to-bill near ~2.9x in a standout quarter is not a run-rate; large lumpy hyperscale orders make quarter-to-quarter order growth volatile and easy to misread.
4. **Competition from diversified giants.** Schneider (≈ tied) and Eaton (Boyd Thermal, Mar 2026) have deeper electrical franchises and balance sheets; cooling hardware can face pricing pressure as capacity floods in.
5. **Customer concentration / cyclicality.** Hyperscaler demand is concentrated; data-center capex has historically been cyclical, and Vertiv carries some net debt into any downturn (less than peers, but not net cash).

---

## 7. Key Uncertainties

1. **Durability of order momentum.** Is book-to-bill sustainably >1x, or did a few mega-orders flatter recent quarters? When we'll know: quarterly orders/book-to-bill and backlog conversion.
2. **Liquid-cooling position & margin under competition.** Can Vertiv hold top-tier competitive position and ~23% margin as Schneider/Eaton press and cooling capacity expands? Watch segment margin and competitive design wins.
3. **AI-capex cycle.** The whole thesis rests on hyperscaler capex staying elevated; a digestion phase is the single biggest swing factor (this is exactly what the **CoreWeave / neocloud** coverage is meant to stress-test).
4. **Mix & margin ceiling.** How much further can adjusted margin expand before mix/competition cap it? Track incremental margins.
5. **M&A integration.** Bolt-ons (switchgear/busbar, thermal) must integrate without diluting returns.

**Thesis-breaking events:**
- If **book-to-bill falls below 1x** for two consecutive quarters, the buildout-velocity thesis is challenged (and it is an early warning for the whole chain).
- If a **major hyperscaler pauses or stretches** data-center capex, Vertiv orders decelerate first.
- If **liquid-cooling pricing/margin compresses** as competitors add capacity, the margin-expansion leg breaks.

---

## 8. Valuation Context

> The following is valuation "context," not a price target or a buy/sell recommendation.

- **Forward P/E ~48x (FY2026E adjusted) / ~54x (GAAP):** on guidance of adj EPS $6.30-6.40 and GAAP $5.60-5.70 at $306.97. Richer than the compute names (NVIDIA ~25x, Broadcom ~33x forward) but below Corning's ~71x — reasonable *if* ~30% growth persists, demanding if it doesn't.
- **Trailing P/E ~80x:** reflects how far earnings still are from the forward run-rate; the multiple only "works" on the forward ramp.
- **EV/EBITDA ~34x (FY2026E, est.) / EV/Sales ~8.6x:** EV ~$118.7B (market cap ~$117.9B + net debt ~$0.76B) on ~$13.75B revenue and ~$3.4-3.5B est. adj EBITDA. Premium capital-goods multiples that embed continued double-digit growth and margin expansion.
- **Reading the multiple:** Vertiv's valuation is a bet on **the duration and pace of the AI data-center buildout.** The backlog de-risks the next several quarters; the multiple is underwritten by the years *after* that. If buildout velocity holds, EPS grows into the multiple; if it digests, both earnings cadence and the multiple compress — a high-beta double.

**Scenario grid:**

| Scenario | Driver assumptions (backlog / liquid cooling and power equipment / margin / multiple) | Valuation implication (rich / fair / cheap vs today) | Probability weight |
|----------|---------------------------------------------------------|------------------------------------------------------|--------------------|
| Bull | Q2/Q3 orders and book-to-bill stay above 1.5x, the $15.0B backlog keeps growing and converts cleanly into revenue; 100kW+ AI racks lift liquid cooling, CDU, direct-to-chip, and power-equipment share; adjusted operating margin beats the 23% guide path and expands toward 24-25%; forward P/E can hold a 35-40x range | Current price looks fair-to-slightly cheap only if backlog, liquid-cooling share, and margin all beat expectations together | 20% |
| Base | AI buildout remains strong through 2027, but order growth normalizes from the Q4 2025 high; backlog conversion supports high-teens to low-20s EPS CAGR after FY2026; liquid-cooling adoption continues but competition intensifies; adjusted operating margin is about 23-24%; forward P/E normalizes toward about 32x | Current price already discounts the optimistic side of base, and Vertiv needs continued execution to grow into the valuation | 50% |
| Bear | Hyperscaler capex digests, orders/book-to-bill approaches or falls below 1x, and backlog starts rolling over; Schneider/Eaton and others pressure liquid-cooling and power-equipment price or share; margin expansion stops, EPS CAGR falls to low-teens or worse; forward P/E returns to the 20s | Current price is rich; earnings cadence and multiple can compress together, turning the high-beta order book into a downside warning | 30% |

**What's priced in & the expectation gap:** At the $306.97 close on Jun 29, 2026 and about 48x FY2026E adjusted EPS, if forward P/E normalizes toward about 32x over three years with an 8% required return, the reverse-multiple frame implies about `(48 / 32)^(1/3) x 1.08 - 1`, or roughly **24% EPS CAGR**. Our base case needs backlog, liquid-cooling share, and 23%+ margins to keep delivering just to approach that hurdle; the 20% bull / 50% base / 30% bear blend says business quality is high, but the expectation gap is negative at the current price and the skew turns cautious. This is an expectations frame, not a target price.

---

## 9. Catalysts & Monitoring Checklist

**Near-term (0-6 months):**
- Q2 2026 results (~late July 2026): organic growth, **orders/book-to-bill**, backlog trend, margin, guidance.
- Hyperscaler capex guidance (MSFT, META, GOOG, AMZN) — Vertiv demand is derivative of total AI-infrastructure spend.
- Liquid-cooling design wins / new CDU/immersion product traction.

**Medium-term (6-18 months):**
- Backlog conversion to revenue and the path to ~23%+ margin; incremental margins.
- Competitive share vs Schneider/Eaton (esp. post-Boyd Thermal integration).
- Free-cash-flow trajectory and capital-return cadence.

**Long-term (18+ months):**
- Whether liquid cooling becomes the default AI standard and Vertiv holds share.
- The next data-center capex cycle phase — still expanding, stabilizing, or digesting?
- Mix shift toward services/recurring and its margin effect.

**Metrics to monitor continuously:** orders & book-to-bill, backlog, organic growth by region, adj operating margin, adj FCF, net debt, hyperscaler capex, liquid-cooling share.

---

## 10. Conclusion

Vertiv is the most direct, real-time read on whether the AI data-center buildout is actually happening: power and cooling gear is ordered before the chips ship, and the latest disclosed order book was filling faster than it emptied at Q4 2025 — a $15.0B backlog (+109%), followed by +30% Q1 revenue, +430bps margin, and a *raised* full-year guide. As a franchise it is high quality: experienced through-cycle management, structural margin expansion, strong cash conversion, and light leverage. Within this center's chain it plays a unique double role — both a beneficiary *and* the **dashboard** that cross-checks the demand assumptions in NVIDIA, Broadcom, Corning, GE Vernova and Bloom.

**The quality is largely in the price.** At $306.97 — roughly triple a year ago — Vertiv trades at ~48x FY2026E adjusted EPS (~80x trailing) and ~$117.9B, pricing in years of sustained ~30% growth. The bet is on the *pace* of the buildout, and Vertiv's high-beta order book is the same instrument on the way down as on the way up: it would flash the warning first.

The expectation gap is negative: at $306.97 and about 48x FY2026E adjusted EPS, if the multiple normalizes toward about 32x over three years with an 8% required return, the market implies roughly 24% EPS CAGR; our 20% bull / 50% base / 30% bear grid needs backlog, liquid-cooling share, and 23%+ margins to keep delivering just to approach that hurdle.

The current stance is **cautious, medium conviction**. Cautious does not deny Vertiv's business quality; it recognizes that the price bundles multiple years of fast buildout, order durability, and margin expansion into one assumption. Medium conviction comes from strong Q1 growth, margin, FCF, and Q4 2025 backlog evidence, while Q2/Q3 orders, book-to-bill, and liquid-cooling competition will decide whether Vertiv can sustain the implied EPS hurdle. Use Vertiv as the chain's velocity gauge — and pair it with the CoreWeave / neocloud risk anchor, which tests whether that velocity is real economic demand or leverage-fueled.

Upgrade trigger: Move to neutral-watch or constructive if Q2/Q3 orders/book-to-bill stays above 1.5x, backlog keeps growing, liquid-cooling/power-equipment share improves, and adjusted operating margin runs above the 23% guide path without further forward-multiple expansion. Downgrade trigger: Move to bearish-avoid if orders/book-to-bill approaches or falls below 1x, backlog starts rolling over, liquid-cooling competition compresses gross or incremental margin, or hyperscaler capex guidance enters a digestion phase.

---

## Appendix: Sources & Assumptions

**Primary sources:**
- [Vertiv Q1 2026 results 8-K / press release (SEC)](https://www.sec.gov/Archives/edgar/data/0001674101/000162828026026379/q12026exhibit991vrt04222026.htm) — quarter ended March 31, 2026, reported April 22, 2026
- [Vertiv Q1 2026 results (IR)](https://investors.vertiv.com/news/news-details/2026/Vertiv-Reports-Strong-First-Quarter-with-Diluted-EPS-Growth-of-136-Adjusted-Diluted-EPS-Growth-of-83-Raises-Full-Year-Guidance/default.aspx) — revenue, margin, EPS, raised FY2026 guidance
- [Vertiv Q4 2025 results 8-K (SEC)](https://www.sec.gov/Archives/edgar/data/0001674101/000167410126000006/exhibit991vrt02112026.htm) — $15.0B backlog (+109%), book-to-bill
- [Vertiv Q1 2026 10-Q (SEC)](https://www.sec.gov/Archives/edgar/data/0001674101/000162828026026556/vrt-20260331.htm) — balance sheet (debt, cash)
- Quote/valuation references: [Yahoo Finance VRT](https://finance.yahoo.com/quote/VRT/), [StockAnalysis VRT](https://stockanalysis.com/stocks/vrt/)
- AI/liquid-cooling and high-water-mark context: [Investor's Business Daily VRT profile](https://www.investors.com/stock-lists/sector-leaders/vertiv-vrt-stock-ai/)
- Liquid-cooling market/share: directional industry estimates (Dell'Oro Group / MarketsandMarkets as cited by industry press), treated as non-company-disclosed and not audited

**Key assumptions & basis:**
- Price $306.97 = 2026-06-29 U.S. close; ~384M shares → market cap ~$117.9B (~$146B at a ~$379.94 high). Actual quoted price may differ intraday.
- Net debt ~$0.76B = ~$3.26B debt securities and finance-lease obligations − ~$2.50B cash; operating lease liabilities are excluded from this shorthand EV bridge.
- Q1 2026 (quarter ended Mar 31, 2026): net sales $2,650M (+30%, +23% organic), adj operating margin 20.8%, adj diluted EPS $1.17, GAAP net income $390M, adj FCF $653M — per the April 22, 2026 8-K. "Adjusted" excludes amortization of intangibles, stock comp, restructuring and certain items; track the GAAP-vs-adjusted gap.
- Backlog $15.0B (+109% Y/Y) and book-to-bill are Q4 2025 figures (reported Feb 2026); reconcile to the latest quarter as reported. A single-quarter book-to-bill near ~2.9x reflects lumpy large orders and is not a run-rate.
- Forward multiples use FY2026E guidance: adj EPS $6.30-6.40, GAAP EPS $5.60-5.70, revenue $13.5-14.0B, adj op margin ~23.3%; EV/EBITDA uses an estimated ~$3.4-3.5B FY2026E adj EBITDA (revenue × ~24% + D&A) and is approximate.
- Liquid-cooling share/TAM estimates are directional and vary by source definition; the report relies on them to frame the competitive field, not as audited valuation inputs.
- The 2026-07-07 v5 scenario grid and priced-in paragraph use the same 2026-06-29 price-ledger anchor. The reverse P/E math frames market-implied expectations only; it is not a target price.
- This report is **initial coverage**; refresh price, orders/backlog, margin and guidance at the next quarterly result.
