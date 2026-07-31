# Astera Labs (ALAB) Deep Research Report

Coverage date: 2026-07-31
Last updated: 2026-07-31
Ticker: NASDAQ: ALAB
Disclaimer: This report is for informational and research purposes only. It does not constitute investment advice. Please conduct your own due diligence.

---

## Executive Summary

> **Framework note:** This report opens the AI-infrastructure book's **interconnect** layer, which until now had zero nodes, and it opens it as an **architecture check**. The queue label that commissioned it asks a specific question: does rack-level fan-out - PCIe/CXL retimers, PCIe smart fabric switches, active Ethernet cable modules - behave as a bottleneck *distinct* from the optical layer (coherent-2026, corning-2026, aaoi-2026) and the networking layer (arista-2026), or is it merely a component of them? Section 3 answers that question with the evidence, and the answer is not the flattering one. The chain role is deliberately `architecture-check` rather than `common-constraint`: the role names the **job** - testing which scale-up path (NVLink Fusion, open PCIe/Scorpio, UALink, Ethernet) actually gets adopted and who gets paid for it - and that job survives whichever way the distinctness question resolves. Labelling this layer a common constraint would have been falsified by the report's own finding. On the supply side it pairs with broadcom-2026 and marvell-2026, which sell the merchant switch and SerDes silicon that could absorb ALAB's function.

**One-line thesis:** Astera Labs is the purest listed expression of connectivity content inside the AI rack - Q1 2026 revenue of $308.4M grew 93% year over year at a 76.3% gross margin, PCIe Gen 6 products crossed one-third of revenue, and management claims over $1,000 of Astera silicon content per accelerator - but at the July 30, 2026 close of $299.69 the market still pays roughly **50x trailing-twelve-month revenue** and about **33x our own CY2026 revenue estimate**, which requires roughly 40-50% compound revenue growth sustained for five years just to earn a normal return, from a fabless company of 756 full-time employees whose top five direct customers were 90% of Q1 revenue and whose largest one holds a warrant for 3.26M shares that is recognized as contra-revenue as it buys more.

**Current view:** **Cautious, medium conviction.** This is not a quality objection. The operating evidence is among the best in the entire book: 93% growth, 76% gross margin, 36.2% non-GAAP operating margin, net cash of about $1.18B, no debt, and a genuinely new switch socket (Scorpio X-Series, 320 lanes) that did not exist in the rack two years ago. The objection is skew at the price. The July 2026 AI-infrastructure repricing took ALAB from a $432.74 close on July 6 to $249.74 on July 29 (-42.3%) and then back up 20.0% in a single session on July 30 - and even after that round trip the multiple is the richest in this coverage by a wide margin. Conviction is medium rather than low because no single quarter closes a gap this size, and medium rather than high because the two things that would settle the thesis - 2027 NVLink Fusion and UALink revenue, and whether the retimer function survives integration - are outside the current disclosure window.

**Timing note, stated up front:** the latest *reported* period is **Q1 2026 (quarter ended 2026-03-31, reported 2026-05-05)**. Astera Labs is scheduled to report Q2 2026 on **2026-08-05**, five days after this initiation's price anchor. The fact base here is therefore roughly three months old while the price is one day old, and that asymmetry is deliberate: the price anchor must be the latest completed close, and the last completed US session at the time of writing was 2026-07-30.

**Quick stats:**

| Metric | Value |
|--------|-------|
| Share price | $299.69 (Jul 30, 2026 close, Yahoo/yfinance); +20.0% on the session, from $249.74 |
| Trailing-year close range | $100.27 (2026-03-30) - $483.02 (2026-06-30); today is ~38.0% below the June closing high and ~199% above the March closing low |
| Market cap / shares | About $51.37B; 171,407,939 shares outstanding at 2026-04-30 (10-Q cover) |
| Net cash / enterprise value | About $1.18B (cash $148.3M + marketable securities $1,036.2M, no meaningful debt) / about $50.19B |
| Latest reported period | Q1 2026, quarter ended 2026-03-31 (reported 2026-05-05); next print 2026-08-05 |
| Q1 revenue / YoY / QoQ | $308.4M, +93% / +14% |
| Q1 gross margin (GAAP / non-GAAP) | 76.3% / 76.4% |
| Q1 operating income / margin (GAAP / non-GAAP) | $61.8M, 20.1% / $111.7M, 36.2% |
| Q1 net income / diluted EPS (GAAP / non-GAAP) | $80.3M, $0.44 / $110.1M, $0.61 |
| Q1 stock-based compensation | $48.9M, 15.9% of revenue - essentially the whole GAAP-to-non-GAAP gap |
| Q2 2026 guidance | Revenue $355-365M (+15-18% QoQ); gross margin ~73%; non-GAAP diluted EPS $0.68-0.70 |
| FY2025 / TTM revenue | $852.5M (+115%) / $1,001.4M |
| TTM operating income / net income / FCF | $224.0M / $267.6M / $342.8M (OCF $383.4M less capex $40.6M) |
| Customer concentration (Q1) | Five direct customers at 29% / 21% / 16% / 12% / 12% - about 90% combined |
| Valuation | ~51.3x P/TTM revenue; ~50.1x EV/TTM revenue; ~33x EV/CY2026E revenue; ~192x trailing GAAP P/E; ~146x EV/TTM FCF |
| Chain role | interconnect **architecture check**: which scale-up fabric wins, and whether merchant fan-out silicon survives integration |

## 1. Business Overview

Astera Labs is a fabless semiconductor company that sells connectivity silicon and the software that manages it. It does not make accelerators, systems, or optics. Its product is the plumbing between accelerators, CPUs, memory, and the network inside and immediately around an AI rack - a market that essentially did not exist as a separate merchant category before PCIe Gen 5 and that the company has so far led.

The company does not report segments and does not disclose revenue by product line. What follows is the qualitative product structure with the quantitative anchors management provided on the Q1 2026 call, labelled accordingly.

| Product line | What it does | Q1 2026 readout | Chain relevance |
|--------------|--------------|-----------------|-----------------|
| Aries (PCIe/CXL Smart DSP Retimers) | Restores PCIe signal integrity over the reach a modern rack needs; deployed in volume on NVIDIA HGX and hyperscaler rack platforms | Growing on early adoption of PCIe 6 for both scale-out and scale-up; roadmap extends to PCIe 7 | The original franchise; per-accelerator attach, on copper, inside the rack |
| Scorpio (Smart Fabric Switches) | P-Series: PCIe 6 switching, 32-320 lanes for scale-out. X-Series: 320-lane scale-up fabric switch with in-network compute | X-Series shipping since 2026-05-05 with production ramp guided to H2 2026; two additional major hyperscalers expected to start receiving P-Series in late 2026 | The new socket; the reason this layer is an architecture question rather than a component question |
| Taurus (Smart Cable Modules) | Active electrical cable modules for Ethernet scale-out, moving to 1.6T | Solid results on broad adoption across AI and general-purpose compute | Overlaps the networking layer's copper reach problem, adjacent to arista-2026 |
| Leo (CXL Memory Controllers) | CXL memory expansion and pooling; KV-cache offload for inference | On track for an early ramp with Microsoft Azure M-series; a new custom KV-cache design win guided to ship in 2027 | The only product tied to a memory-tier architecture bet rather than accelerator volume |
| COSMOS (software) | Fleet-wide link management, diagnostics and telemetry across all four silicon families | Not separately monetized; cited as the stickiness layer | The claimed switching cost; unverifiable from outside |

Three structural points frame everything below.

**First, the business is an attach rate, not an end market.** Astera Labs sells content per accelerator. Management's own framing on the Q1 call was "over $1,000 worth of content per accelerator" within AI racks, growing as optical-enabled switches mature. That is a powerful multiplier while accelerator units grow, and it is also the whole story: there is no installed base to service, no subscription, and no independent replacement cycle. Revenue is accelerator shipments times attach times price.

**Second, PCIe Gen 6 is the current price event.** Management said on the Q1 call that PCIe Gen 6 products contributed more than one-third of total company revenue, spanning both signal conditioning (Aries) and fabric (Scorpio). Each PCIe generation shortens the electrical reach at which a signal survives, which is what creates retimer demand in the first place; each generation therefore resets both content and ASP. The bull case and the bear case are both downstream of how many generations that keeps working.

**Third, the customer list is short and it holds equity.** In Q1 2026 five direct customers were individually 10% or more of revenue - 29%, 21%, 16%, 12% and 12%, roughly 90% combined. The 10-Q notes that certain of these are manufacturing partners buying on behalf of end customers, so the direct-customer percentages move with production allocation rather than with end demand. Separately, one customer (the "Holder") has held warrants since 2022, and in February 2026 received a new warrant for up to 3,262,299 shares at $142.82, with a maximum grant-date fair value of $280.0M, vesting in tranches as it purchases more product. Those warrants are recognized as **contra-revenue**: $2.1M in Q1 2026, and management attributed roughly 200 basis points of the Q2 gross-margin step-down to a non-cash warrant impact.

## 2. Industry & Competitive Position

**The market Astera created.** Merchant PCIe retiming became a real category with PCIe Gen 5 in AI servers, and Astera Labs took it early with Aries. Its position in PCIe Gen 5/6 signal conditioning for AI platforms is the strongest in the industry, evidenced by 76% gross margins that have not eroded through three years of scaling. What is far less settled is the newer, larger prize: scale-up fabric switching, where Astera is a challenger rather than an incumbent.

| Competitor | Where it overlaps | Read-through to existing coverage |
|------------|-------------------|-----------------------------------|
| Broadcom (AVGO) | PCIe switching, SerDes IP, Ethernet switching and custom XPU design; owns the SerDes that could absorb retiming into the endpoint | The most direct absorption risk. broadcom-2026 already sells the accelerator, the switch and the SerDes into the same rack |
| Marvell (MRVL) | Custom ASIC, optical DSP, and - after the Celestial AI acquisition - optical interconnect; also an NVLink Fusion participant | marvell-2026 is the closest structural analogue: an interconnect-adjacent name whose thesis is socket conversion it has not yet proven |
| Credo (CRDO) | Active electrical cables and PCIe retimers; the clearest head-on competitor in Taurus's market and a declared entrant in Aries's | Not in this coverage; named here as the price-competition vector on cable modules |
| NVIDIA | NVLink and NVLink Fusion define the scale-up fabric on the largest installed base of accelerators; Astera participates by NVIDIA's invitation | nvidia-2026 is simultaneously the demand driver and the party that decides how much of the rack stays merchant |
| Arista (ANET) | Scale-out Ethernet fabric at the system level, one tier out from the rack | arista-2026 and this report do not compete for BOM dollars; they sit in series |
| Coherent / AAOI / Corning | Optical modules, lasers, fiber and cable, from the rack outward | coherent-2026, aaoi-2026 and corning-2026 own the optical BOM; Astera's content is copper and silicon inside the rack |

**The scale-up fabric race is the actual contest.** Three architectures are competing to connect accelerators to each other inside a rack: NVIDIA's NVLink and its licensable NVLink Fusion variant; the open UALink standard, backed by AMD, Amazon and others; and PCIe-native scale-up, which is where Astera's Scorpio X-Series sits. Astera has chosen to be present in all three - the same posture Marvell has taken - which maximizes optionality and minimizes leverage. Management guided initial NVLink Fusion custom-solution revenue to 2027, and initial UALink revenue also to 2027 as hyperscaler ASICs and GPUs supporting it launch. Astera cites a merchant scale-up switch silicon market projected to reach $20 billion by 2030; that is a company-cited third-party projection, not a company forecast, and this report does not build on it.

**Where the competitive position is genuinely strong:** volume PCIe 6 signal conditioning at hyperscalers today, a shipping 320-lane scale-up switch with in-network compute ahead of the merchant field, and a software layer (COSMOS) that is deployed across the fleet and is the kind of asset that decides re-designs. **Where it is not:** every one of those positions is contested by companies with 20 to 70 times its revenue, and in fabric switching the incumbent competence belongs to Broadcom.

## 3. Is Rack Fan-Out a Distinct Bottleneck?

This is the question the coverage queue commissioned, it is the reason the `interconnect` layer exists in the book's schema, and it deserves a direct answer rather than a hedge. The answer this report reaches is: **rack-scale fan-out is a distinct socket, but it is not a distinct bottleneck.** Those are different claims and the difference decides what this layer is for.

**The case that it is distinct (the socket argument), which holds:**

| Test | Evidence | Verdict |
|------|----------|---------|
| Does it have its own BOM line? | Retimers, PCIe fabric switches and active cable modules are separate silicon bought separately from optics, switches and accelerators; management claims over $1,000 of content per accelerator | Yes - it does not overlap the optical or system-switch BOM |
| Is it a new socket or a rebadged old one? | Scorpio X-Series, a 320-lane scale-up fabric switch with in-network compute, did not exist in the rack two years ago; PCIe Gen 6 crossed one-third of revenue in its first full year | Yes - genuinely new content, not reallocated spend |
| Is it commoditized? | 76.3% GAAP gross margin in Q1 2026, up sequentially, three years into scaling | No - pricing power is real today |
| Is it a different physical problem? | Copper reach inside and immediately around the rack, not fiber between racks; signal integrity, not switching capacity | Yes - it is a distinct engineering domain from optical or Ethernet switching |

**The case that it is not a bottleneck, which also holds and matters more:**

1. **Nobody is waiting on it.** On the Q1 2026 call management said it has supply in place through the end of the year, described the back-end supply chain as diversified against pockets of supply challenge, and reported 75 days of inventory as a comfortable position. There is no allocation, no lead-time extension, no customer queuing. Contrast that with the layers this book has verified as genuinely gating: interconnect power (constellation-energy-2026, vistra-2026, gevernova-2026), where megawatts arrive years late, and HBM (micron-2026, sk-hynix-2026), where supply is sold out ahead. A cluster is late because it has no power or no HBM. No cluster is late because it has no retimers.
2. **It has no independent cycle.** Revenue is accelerator units times attach times price. There is no separate capital-expenditure decision that could fund fan-out ahead of or behind accelerators, no separate permitting or construction lead time, and no separate depreciation schedule. When the accelerator layer slows, this layer slows in the same quarter with no lag and no buffer.
3. **It shares the same channel and the same signal.** Q1 revenue by region was Taiwan $93.2M, Singapore $91.1M, China $89.6M, United States $15.0M - the ODM and manufacturing-partner channel that already carries every other rack component. There is nothing here to observe that is not already observable one tier up.

**Therefore:** the `interconnect` layer's value to this book is an **architecture read, not a constraint read.** It tells us which scale-up fabric hyperscalers are actually buying and how much of the rack stays merchant - which is exactly what the `architecture-check` role is for. It does not add a new gating variable to the buildout model, and it should not be scored as one. Anyone using ALAB revenue as an early warning on AI capex is reading a coincident indicator, not a leading one; nvidia-2026 and the demand-risk layer get there first and with more signal.

**The structural risk that follows directly: absorption.** The reason a merchant retimer exists is that the accelerator and switch vendors have not integrated the function. That is a choice, not a law.

- **Broadcom** already ships the SerDes IP, the PCIe switches and the custom XPUs into the same rack. If it decides that retiming belongs inside its own endpoint silicon, the merchant socket narrows to the platforms Broadcom does not touch.
- **NVIDIA** decides the scale-up fabric on the largest installed base. Astera's NVLink Fusion participation, announced May 2025 and expanded to custom solutions in December 2025, is genuine business - and it is also the tell: Astera is inside that architecture because NVIDIA invited it, on terms NVIDIA sets, with revenue guided no earlier than 2027.
- **The customers themselves** are the counterparties on the warrants. A customer with 29% of your revenue and a 3.26M-share warrant struck at $142.82 has both the incentive and the leverage to negotiate price, and the option value rises with your success.

Astera's honest defense is the treadmill: every PCIe generation shortens electrical reach, so the retiming problem regenerates faster than integration can absorb it, and each generation lifts content. That defense has worked from Gen 4 through Gen 6. It is a bet on physics staying ahead of integration economics, and it is unfalsifiable until a generation arrives where it does not.

## 4. Financial Analysis

Q1 2026 is an unusually clean operating quarter attached to an unusually noisy earnings statement.

| Metric | Current readout | Interpretation | Grade |
|--------|-----------------|----------------|-------|
| Revenue growth | Q1 $308.4M, +93% YoY and +14% QoQ; FY2025 $852.5M, +115%; TTM $1,001.4M | The fastest growth in this coverage at a $1B scale | A |
| Gross margin | 76.3% GAAP / 76.4% non-GAAP, up ~70bps sequentially on a lower mix of hardware within signal conditioning | Fabless semiconductor margins with no erosion through three years of scaling | A |
| Operating margin | GAAP 20.1% / non-GAAP 36.2% | The gap is stock-based compensation, not adjustments of judgment | B+ |
| Stock-based compensation | $48.9M in Q1, 15.9% of revenue; $457.6M unrecognized on RSUs over ~1.9 years plus $43.1M on PSUs over ~2.4 years | Real dilution, not a one-time item; the non-GAAP margin is not a cash margin | C |
| Earnings quality | GAAP net income $80.3M exceeded pre-tax income of $73.4M because of a $6.9M income-tax **benefit**; interest income contributed $11.6M | GAAP net income is flattered by a tax benefit and by interest on the IPO cash - neither is operating | C+ |
| Free cash flow | TTM OCF $383.4M less capex $40.6M = $342.8M; Q1 OCF $74.6M | Genuine cash conversion; asset-light by construction | A- |
| Balance sheet | Cash $148.3M + marketable securities $1,036.2M = ~$1.18B; no meaningful financial debt; equity $1,493.9M | Fortress relative to size; funds R&D through any plausible downturn | A |
| R&D intensity | Q1 R&D $125.6M, 40.7% of revenue; FY2025 $304.0M | Spending like a company that believes the treadmill defense | B+ |
| Customer concentration | Five customers at 29% / 21% / 16% / 12% / 12% of Q1 revenue; the same customers were 25% / 20% / 16% / 17% / 13% of receivables | The single largest structural risk; the top customer nearly tripled its share from 12% a year ago | D |
| Customer warrants | February 2026 warrant for up to 3,262,299 shares at $142.82, max grant-date fair value $280.0M, vesting on purchase tranches; $2.1M of contra-revenue in Q1 | Reported revenue is net of an equity give-back to the largest customer, and the give-back scales with success | C- |
| Inventory / commitments | Inventory $60.2M (75 days per management); purchase commitments $79.6M total, $29.6M in the rest of 2026 | Small and short; consistent with no supply constraint | B |
| M&A | Feb 9, 2026: certain assets of a private data-center acceleration company for $74.0M, of which $68.4M is goodwill and the rest immaterial intangibles | An acqui-hire in substance; small enough not to change the thesis | B |

**Interconnect and adjacent-layer comparison** (each column at its own latest reported period; not restated to a common calendar):

| Metric | Astera Labs (Q1 2026, Mar-31) | Broadcom (Q2 FY2026) | Marvell (Q1 FY2027, Apr-30) | Coherent (Q3 FY2026, Mar-31) |
|--------|-------------------------------|-----------------------------|------------------------------|-------------------------------|
| Quarterly revenue | $308.4M | $22.19B | $2.42B | $1.81B |
| Revenue growth YoY | +93% | +48% | n/a in that report | +21% |
| Gross margin | 76.3% GAAP | 69.4% GAAP / 77.1% non-GAAP | ~52% | 39.6% non-GAAP |
| Operating margin | 20.1% GAAP / 36.2% non-GAAP | 48.6% GAAP / 67.3% non-GAAP | ~14% GAAP | n/a |
| EV / TTM revenue at each report's anchor | **~50.1x** | ~24-25x | ~14.1x on the FY2027 outlook | ~7.5x |
| Net cash / (net debt) | +$1.18B | -$45B | -$1.1B | -$1.0B |

Astera Labs has the best growth and the best gross margin in that table and the highest multiple by a factor of two against the next-richest name. That is the entire investment question in one row.

**Red-flag check:**

| Red flag | Current status | What to re-check |
|----------|----------------|------------------|
| Customer concentration | Top customer 29% of Q1 revenue, up from 12% a year earlier; top five ~90% | Whether Customer A keeps rising; whether any 10%+ customer disappears from the table |
| Equity given to a customer | Warrants for up to 3.26M shares at $142.82 (Feb 2026), plus 1.48M (2022) and 0.83M (2023); recognized as contra-revenue | Quarterly contra-revenue and any new warrant to a second customer |
| Non-GAAP distance from GAAP | $48.9M of quarterly SBC, 15.9% of revenue, is essentially the entire GAAP-to-non-GAAP bridge | Whether SBC as a percentage of revenue falls as revenue scales |
| Tax-benefit-flattered net income | Q1 GAAP net income above pre-tax income on a $6.9M tax benefit | Whether an effective tax rate normalizes toward a statutory level in FY2027 |
| Geographic exposure | 89% of Q1 revenue billed to Taiwan, Singapore and China; the 10-Q flags China trade restrictions and export controls among its risk factors | Any export-control change touching the ODM channel |
| Insider selling | Frequent Form 4 and Rule 144 filings through June and July 2026 as the stock ran from ~$110 to ~$483 | Whether selling continues after the July drawdown |
| Valuation | ~50.1x EV/TTM revenue after a 38% drawdown from the June closing high | Whether the multiple compresses through growth or through price |

## 5. Management & Governance

Astera Labs is run by its co-founders - Jitendra Mohan, Chief Executive Officer and a director since November 2017, and Sanjay Gajendra, President, Chief Operating Officer and a director - alongside Desmond Lynch, who has been Chief Financial Officer since March 2026, and Philip Mazzara, General Counsel since 2022. The company had 756 full-time employees at 2025 year-end (527 in North America, 208 in Asia, 21 in Europe). The operating record is the strongest argument for the team: from $79.9M of revenue in 2022 to $852.5M in 2025 and a $1.4B+ annualized run rate on the Q2 2026 guide, with gross margin never breaking below the mid-70s and GAAP operating income turning positive in 2025 after a $116.1M loss in 2024. Product execution has been on time and on the standards curve - Aries through PCIe Gen 6 with Gen 7 announced, Scorpio P-Series and then a 320-lane X-Series inside eighteen months.

Four governance items deserve to be named precisely, because they are where the interests diverge.

**The CFO transition.** Michael Tate, who took the company public, retired as Chief Financial Officer on March 2, 2026 and is providing transition services as a Strategic Advisor to the CEO until September 1, 2026. Desmond Lynch, previously Chief Financial Officer of Rambus from August 2022 to February 2026, took the role in March 2026 and signed the Q1 2026 Form 10-Q. The handover is orderly, well disclosed, and into a strong resume - and it is still a change in the officer who owns guidance quality at a company whose entire valuation rests on one quarter of guidance at a time, with the Q1 2026 call his first. It is noted here, not scored against the thesis.

**The customer warrants.** Since 2022 Astera has issued one customer warrants over 1,484,230 shares, amended and extended by 831,945 shares in 2023, and then in February 2026 a further 3,262,299 shares at a $142.82 exercise price with a maximum grant-date fair value of $280.0M. All vest against purchase tranches and are booked as contra-revenue. This is a legitimate and increasingly common structure for locking in an anchor customer, and it is also an admission of where the bargaining power sits: the company is paying its largest customer, in equity, to keep buying, and the payment scales with the customer's purchases. Investors should read reported revenue as already net of that transfer, and read the ~200bps of Q2 gross-margin guidance attributed to a non-cash warrant impact as the first quarter in which it is material.

**Stock-based compensation.** $48.9M in Q1 alone - 15.9% of revenue, and larger than the $61.8M of GAAP operating income by two-thirds. Unrecognized RSU expense is $457.6M over roughly 1.9 years, with $43.1M more on PSUs over 2.4 years. Non-GAAP operating margin of 36.2% is what the business looks like if that cost is treated as zero; GAAP's 20.1% is what it looks like if it is treated as real. It is real.

**Insider selling and disclosure.** EDGAR shows a steady stream of Form 4 and Rule 144 filings through June and July 2026, the period in which the stock traded between roughly $280 and $483. Most of this is presumptively scheduled 10b5-1 activity by founders and early holders and it is not by itself a signal; it is noted because press coverage of the late-July decline cited insider liquidations among the drivers, and because a reader should know the flow exists rather than infer it from the price.

Disclosure quality is mixed in a specific and consequential way:

| Disclosure | Assessment |
|------------|------------|
| Customer concentration (percent of revenue and of receivables, plus the manufacturing-partner caveat) | Strong. The caveat that direct-customer percentages move with production allocation is the kind of qualification most companies omit |
| Warrant terms (share counts, strike, maximum fair value, vesting mechanic, contra-revenue treatment) | Strong in the filing; management's call framing of "a recently executed warrant agreement" without naming the instrument is weaker |
| Revenue by product line | **Absent.** Aries, Scorpio, Taurus and Leo have no disclosed revenue, so the single most important mix question - how fast Scorpio is displacing Aries - is only answerable through call commentary |
| Revenue by end customer versus manufacturing partner | Absent. The company discloses direct customers only, which it says is not representative of end demand |
| Content per accelerator | Call-only, unaudited, and the load-bearing number in the bull case |
| Backlog or bookings | Not disclosed at all. There is no order-book visibility of the kind broadcom-2026 and arista-2026 provide |

That last row is why this report's conviction is capped. A company with no segment revenue, no backlog and no end-customer disclosure is asking to be valued at 50x sales on the strength of quarterly call commentary.

## 6. Bull Case

The bull case is that Astera Labs is the toll booth on a road that gets longer with every accelerator generation, and that content per accelerator compounds faster than unit growth decelerates.

1. **The attach rate is rising, not flat.** Over $1,000 of content per accelerator today, per management, versus a retimer-only business three years ago. Scorpio adds a switch socket on top of the retimer socket, Taurus adds cable modules, Leo adds a memory-tier socket. Each is incremental content on the same unit.
2. **PCIe Gen 6 is doing what Gen 5 did, only bigger.** It crossed one-third of total revenue in Q1 2026 across both signal conditioning and fabric, and Gen 7 is already on the Aries roadmap. Every generation shortens electrical reach, regenerating the problem Astera solves and lifting ASPs with it.
3. **Scorpio is a real second act.** The X-Series 320-lane scale-up fabric switch with in-network compute is shipping, with production ramp guided to H2 2026 and two additional major hyperscalers expected to begin taking P-Series in late 2026. Management expects Scorpio to become the largest product line by the end of 2026, surpassing Aries and Taurus.
4. **2027 has three separate call options.** NVLink Fusion custom solutions, UALink switches as hyperscaler ASICs and GPUs launch, and Leo KV-cache offload each have a design win and each is guided to start contributing revenue in 2027. None is in the current run rate.
5. **The financial profile is rare.** 76% gross margin, 36% non-GAAP operating margin, $342.8M of trailing free cash flow, $1.18B of net cash and no debt, at 93% growth. Very few companies in this book combine growth and margin at this level, and none combines them with this balance sheet.

Upside frame: if revenue compounds at 50%+ through 2029 as content per accelerator rises and Scorpio, UALink and NVLink Fusion all convert, CY2029 revenue in the $4-5B range at a mature high-margin connectivity multiple of 15-18x sales supports an enterprise value materially above today's $50.19B, and the current price will have proved to be a discount to a company that simply kept executing.

## 7. Bear Case

The bear case is not that the business is bad. It is that at this price the business has to be extraordinary for five consecutive years, while three separate parties hold the option to make it ordinary.

1. **The multiple requires a five-year sprint.** At ~$50.19B of enterprise value on $1,001.4M of trailing revenue, an 8% annual required return to a generous terminal multiple of 12x sales implies roughly $6.1B of revenue by 2030 - about a 44% compound annual growth rate sustained for five straight years. At a still-generous 15x terminal it is about 38%. Current growth is 93% and the Q2 guide implies about +88%, so the bar is not absurd - but it allows no deceleration below the high 30s at any point, and semiconductor content cycles do not usually behave that way.
2. **Absorption is a live option held by others.** Broadcom ships SerDes, PCIe switches and custom accelerators into the same rack and could integrate retiming into its endpoints. NVIDIA controls the scale-up fabric on the largest accelerator base and admits Astera into NVLink Fusion on its own terms and timing. The merchant socket exists because integration has not happened yet, not because it cannot.
3. **The customer is a counterparty, not just a buyer.** One customer is 29% of revenue and holds warrants over up to 5.6M shares across three tranches, the newest struck at $142.82 with a $280.0M maximum fair value, vesting as it buys more. Reported revenue is already net of that. Five customers are roughly 90% of the total, and 89% of revenue is billed into Taiwan, Singapore and China.
4. **Non-GAAP flatters the economics twice.** Stock-based compensation of $48.9M a quarter is 15.9% of revenue and is the whole GAAP-to-non-GAAP bridge; separately, GAAP net income exceeded pre-tax income on a tax benefit and includes $11.6M of interest income. The ~109x forward non-GAAP P/E implied by the Q2 guide is the *flattering* earnings multiple. The trailing GAAP one is about 192x.
5. **There is no order book to fall back on.** No backlog, no RPO, no segment revenue, no end-customer disclosure. When the growth rate is questioned, there is nothing in the disclosure to answer with except the next quarter's guide.
6. **The July 2026 tape is itself evidence about ownership.** ALAB closed at $432.74 on July 6, $249.74 on July 29, and $299.69 on July 30 - a 42% drawdown and then a 20% single-session bounce, with no company news in between. A shareholder base that reprices a company by a fifth in a session on sector flow is not a base that will underwrite a five-year compounding story through a disappointing quarter.

Downside frame: if growth normalizes toward 40% in 2027 as PCIe 6 laps itself, if Scorpio's ramp is respectable rather than transformative, and if the multiple compresses to a still-rich 15x forward sales on roughly $2.2B of CY2027 revenue, enterprise value lands near $33B - roughly $200 per share on today's share count, about 33% below the $299.69 anchor and still above where the stock traded as recently as April 2026.

## 8. Key Uncertainties

| Uncertainty | Why it matters | When we will know |
|-------------|----------------|-------------------|
| Does the Q2 print sustain the growth rate? | The guide implies about +88% YoY; a miss or a soft Q3 guide breaks the compounding premise directly | 2026-08-05 |
| Does Scorpio actually become the largest product line? | It is the difference between a retimer company and a fabric company, and management staked the year on it | Q3 and Q4 2026 calls; no product-line revenue is disclosed, so only commentary will answer |
| How much contra-revenue do the warrants absorb? | ~200bps of Q2 gross margin is the first material quarter; the maximum fair value outstanding is $280.0M | Quarterly gross margin and the contra-revenue line in the cash-flow statement |
| Does NVLink Fusion or UALink revenue land in 2027? | Both are guided to 2027 and neither is in the run rate; both are also outside Astera's control | FY2026 10-K and the 2027 quarterly calls |
| Does any accelerator or switch vendor integrate the retiming function? | The single structural risk to the merchant socket | Platform announcements at each accelerator generation; no fixed date |
| Does the top customer's share keep rising? | 12% to 29% in four quarters is the wrong direction for a company at 50x sales | Quarterly 10-Q concentration table |
| Does fan-out ever become supply-constrained? | It would upgrade this layer from an architecture read to a constraint read and change how the book scores it | Quarterly supply commentary from Astera and its competitors |

Thesis-breaking conditions:

- **Bear case breaks:** revenue growth holds above 60% through 2027 while Scorpio becomes the largest product line and NVLink Fusion or UALink revenue arrives on schedule, gross margin returns above 75% once the warrant impact laps, the top customer's share falls back below ~25%, and the multiple compresses through growth rather than through price.
- **Bull case breaks:** revenue growth decelerates below ~40% year over year, gross margin settles below ~70% on warrant and mix effects, a major customer's next platform drops discrete retiming or PCIe switching in favor of integrated silicon, or the top customer exceeds ~35% of revenue.

## 9. Valuation Context

The following is valuation context, not a target price or recommendation. All arithmetic uses the 2026-07-30 close of $299.69 and 171,407,939 shares outstanding as of 2026-04-30, giving a market cap of about $51.37B. Net cash is about $1.18B (cash $148.3M plus marketable securities $1,036.2M, with no meaningful financial debt), giving an enterprise value of about $50.19B. Trailing-twelve-month figures are the four quarters ended 2026-03-31: revenue $1,001.4M, operating income $224.0M, net income $267.6M, operating cash flow $383.4M, capital expenditure $40.6M.

| Method | Current readout | Key inputs | Interpretation |
|--------|-----------------|------------|----------------|
| P / TTM revenue | $51.37B / $1,001.4M = ~51.3x | Four quarters ended 2026-03-31 | The richest sales multiple in this coverage by roughly 2x |
| EV / TTM revenue | $50.19B / $1,001.4M = ~50.1x | Net cash ~$1.18B | Against Broadcom at ~24-25x, Marvell at ~14.1x forward, Coherent at ~7.5x |
| EV / CY2026E revenue | $50.19B / ~$1.5B = **~33x** | Our own estimate: Q1 actual $308.4M plus the Q2 guide midpoint $360M, with H2 growing at a decelerating sequential rate. Not company guidance | Still roughly 1.4x Broadcom's trailing multiple on a company 1/20th the size |
| EV / CY2027E revenue | $50.19B / ~$2.25B = ~22x | Assumes 50% growth on the CY2026 estimate; our assumption, not guidance | Two years of flawless execution gets to a multiple that is merely expensive |
| Trailing P/E (GAAP) | $51.37B / $267.6M = **~192x** | TTM net income; per-share sums are not strictly additive across periods | Flattered by a tax benefit and interest income |
| Forward P/E (non-GAAP, annualized) | $299.69 / ~$2.76 = ~109x | Q2 non-GAAP EPS guide midpoint $0.69 annualized; excludes ~15.9%-of-revenue stock compensation | The most generous earnings framing available, and it is still triple digits |
| EV / TTM free cash flow | $50.19B / $342.8M = ~146x | OCF $383.4M less capex $40.6M | Real cash, priced for a decade of it |
| Free-cash-flow yield | $342.8M / $51.37B = ~0.67% | Same | Effectively an option premium, not a yield |
| EV / TTM operating income | $50.19B / $224.0M = ~224x | GAAP operating income | Applying Q1's 36.2% non-GAAP margin to trailing revenue implies roughly $362M and ~139x - our own derivation, not a company-reported trailing figure |
| Net cash cushion | ~$1.18B, about 2.3% of market cap | Cash plus marketable securities, no debt | Protects the company; does not protect the multiple |
| Reverse test | To earn 8% a year to a terminal 12x revenue, ~$6.1B of revenue is needed by 2030 - roughly a 44% five-year compound growth rate; at 15x terminal, roughly 38% | Enterprise value grown at 8% from $50.19B | This is the number that decides the stance |
| Drawdown context | $299.69 versus the $483.02 close on 2026-06-30 (-38.0%) and the $100.27 close on 2026-03-30 (+198.9%) | Closing basis, trailing year | The drawdown removed the excess, not the premium |

**Scenario grid:**

| Scenario | Driver assumptions (growth / Scorpio mix / 2027 options / competitive structure) | Valuation implication versus today | Subjective probability weight |
|----------|--------------------------------------------------------------------------------|-------------------------------------|-------------------------------|
| Bull | Revenue compounds above 50% through 2029 as content per accelerator keeps rising; Scorpio becomes the largest product line and holds share against merchant switch silicon; NVLink Fusion and UALink both convert in 2027; gross margin recovers above 75% after the warrant effect laps | $299.69 proves cheap: CY2029 revenue of $4-5B at 15-18x sales for a franchise with no integration threat realized | 20% |
| Base | Growth decelerates through the 60s and into the 40s by 2028 as PCIe 6 laps itself; Scorpio ramps well but shares the scale-up socket with Broadcom; one of the two 2027 options converts and the other slips; gross margin settles in the low 70s on warrant and mix effects | Broadly fair to slightly rich: ~22x CY2027E revenue is defensible for this growth and margin, leaving return roughly equal to execution with no multiple help | 50% |
| Bear | Growth normalizes to ~40% in 2027; an accelerator or switch vendor integrates retiming on a major platform; the top customer pushes past 35% of revenue and extracts more price and warrant coverage; multiple compresses to 15x forward sales | De-rates toward ~$33B of enterprise value on ~$2.2B of CY2027 revenue, roughly $200 per share, about 33% below the anchor | 30% |

**What's priced in & the expectation gap:** at ~50.1x trailing and ~33x our CY2026 estimate, the price already contains: PCIe Gen 6 running its full course, Scorpio winning a durable share of scale-up switching, content per accelerator rising rather than plateauing, and no integration by Broadcom, NVIDIA or the customers themselves. What is *not* priced either way is the 2027 option stack - NVLink Fusion, UALink and Leo KV-cache are guided as revenue events but nothing in the disclosure lets an outsider size them.

The 20/50/30 grid carries a negative skew, and the asymmetry is in magnitude as well as probability: at 50x trailing revenue the downside from a normalizing growth rate is violent and mechanical, while the upside requires three separate things to go right in sequence. That is why this initiation opens **cautious** rather than neutral. It is emphatically not a quality judgment - on operating evidence this is one of the strongest companies in the book - it is a statement about what the July 30 price already pays for.

## 10. Catalysts & Timeline

| Catalyst | Timing | Impact |
|----------|--------|--------|
| Q2 2026 results and Q3 guidance | 2026-08-05 | The immediate test: does the ~+88% implied growth land, and does gross margin hold near 73% with the warrant impact |
| Scorpio X-Series production ramp | H2 2026 | Whether the scale-up switch socket is real revenue or a demonstration |
| Two additional hyperscalers taking Scorpio P-Series | Late 2026 | Direct evidence on customer diversification, which is the highest-value fix available to the thesis |
| Scorpio becoming the largest product line | By end-2026, per management | The single clearest test of the second-act claim; only observable through commentary |
| FY2026 10-K | Early 2027 | Full-year concentration table, warrant vesting to date, and any first disclosure of product-line detail |
| NVLink Fusion and UALink initial revenue | 2027 | The architecture verdict this layer exists to record |
| Leo KV-cache design win shipping | 2027 | Whether the memory-tier socket is a real fourth leg |
| A competitor or customer integrating retiming or PCIe switching | Event-driven, no fixed date | The thesis-breaking event for the whole merchant category |

The structured monitoring fields track seven readouts: revenue growth and Scorpio mix, gross-margin trajectory under the warrant effect, customer concentration, the customer-warrant contra-revenue mechanic, scale-up socket absorption, whether fan-out ever becomes supply-constrained, and the valuation multiple against the growth rate.

## 11. Conclusion

Astera Labs enters this book as the first and only node in the `interconnect` layer, and it earns that place by answering the question the layer was created to ask - just not in the affirmative. Rack-scale fan-out is a genuinely distinct **socket**: separate silicon, a separate physical problem, over $1,000 of claimed content per accelerator, 76% gross margins, and in Scorpio X-Series a switch that did not exist in the rack two years ago. It is not a distinct **bottleneck**: Astera has supply in place through the year with 75 days of inventory and no allocation, it has no independent cycle because its revenue is accelerator units times attach times price, and it ships through the same Taiwan/Singapore/China channel as everything else in the rack. Nothing is late because of retimers. The honest consequence is that this layer should be read as an architecture indicator - which scale-up fabric wins, and how much of the rack stays merchant - and not added to the book's list of gating constraints. That is precisely the `architecture-check` job, and it is why the role was chosen over `common-constraint`.

At the company level the operating evidence is close to the best in this coverage. Revenue grew 93% to $308.4M in Q1 2026 at a 76.3% gross margin and a 36.2% non-GAAP operating margin, PCIe Gen 6 crossed a third of revenue, free cash flow was $342.8M on a trailing basis, and the balance sheet carries $1.18B of net cash against no debt. Very little in this book combines those four facts.

At the stock level the discipline point is arithmetic. After a 38% drawdown from the June 30 closing high and a 20% single-session bounce on July 30, ALAB still trades at about 50.1x trailing revenue, about 33x our own CY2026 estimate, about 192x trailing GAAP earnings and about 109x the most generous forward non-GAAP framing. Earning 8% a year from here to a terminal 12x revenue requires roughly 44% compound revenue growth for five straight years. That is a demand that permits no deceleration below the high 30s, made of a company whose top five customers are 90% of revenue, whose largest customer holds a warrant over 3.26M shares that reduces reported revenue as it buys more, and whose merchant socket exists only for as long as Broadcom, NVIDIA and the hyperscalers choose not to absorb it.

The initiation stance is **cautious, medium conviction**, from a 20% bull / 50% base / 30% bear grid. Cautious because the skew at this price is negative in both probability and magnitude, not because the company is weak. Medium rather than low because no single quarter closes a gap of this size, so the 2026-08-05 print is unlikely to change the arithmetic. Medium rather than high because the two variables that settle the thesis - whether 2027 NVLink Fusion and UALink revenue arrives, and whether the retimer function survives integration - are both outside the current disclosure window.

Upgrade trigger: revenue growth holds above 60% through 2027 with Scorpio confirmed as the largest product line, NVLink Fusion or UALink revenue arriving on schedule, gross margin returning above 75% once the warrant impact laps, the top customer's share falling back below ~25%, and EV/forward revenue compressing below ~20x through growth rather than through price - upgrade to neutral-watch. Downgrade trigger: revenue growth decelerating below ~40% year over year, gross margin settling below ~70%, a major customer's next platform dropping discrete retiming or PCIe switching for integrated silicon, or the top customer exceeding ~35% of revenue - downgrade to bearish-avoid.

## Appendix: Sources & Assumptions

- Q1 2026 revenue ($308.4M, +93% YoY, +14% QoQ), GAAP gross margin (76.3%) and non-GAAP gross margin (76.4%), GAAP operating income ($61.8M, 20.1%) and non-GAAP operating income ($111.7M, 36.2%), GAAP net income ($80.3M) and diluted EPS ($0.44), non-GAAP net income ($110.1M) and diluted EPS ($0.61), cash ($148.3M) and marketable securities ($1,036.2M), Q1 operating cash flow ($74.6M), diluted share count (181.2M), and the Q2 2026 guidance (revenue $355-365M, gross margin ~73%, GAAP operating expenses $188-191M, non-GAAP operating expenses $128-131M, GAAP diluted EPS $0.44-0.46, non-GAAP diluted EPS $0.68-0.70) are from Astera Labs' official Q1 2026 earnings release dated 2026-05-05: [Astera Labs Q1 2026 results](https://ir.asteralabs.com/news-releases/news-release-details/astera-labs-reports-first-quarter-2026-financial-results).
- Customer concentration (Customer A 29%, B 21%, C 16%, D 12%, E 12% of Q1 2026 revenue, against 12%/26%/-/23%/- a year earlier, and the note that certain listed customers are manufacturing partners purchasing on behalf of end customers), accounts-receivable concentration (25%/20%/16%/17%/13%), revenue by geography (Taiwan $93,155K, Singapore $91,138K, China $89,571K, United States $14,967K, other $19,530K), stock-based compensation ($48,913K in Q1 2026, with $457.6M unrecognized on RSUs over ~1.9 years and $43.1M on PSUs over ~2.4 years), the warrant disclosures (the October 2022 Customer Warrant over 1,484,230 shares, the October 2023 amendment adding 831,945 shares, and the February 2026 warrant over up to 3,262,299 shares at a $142.82 exercise price with a $85.83 per-share grant-date fair value and $280.0M maximum total fair value, all vesting on purchase tranches and recognized as contra-revenue of $2,097K in Q1 2026), the income-tax benefit ($6,896K) against pre-tax income ($73,414K), interest income ($11,581K), inventory ($60,156K), purchase commitments ($79,615K total, $29,594K in the remainder of 2026), the February 9, 2026 acquisition of certain assets of a privately held data-center acceleration company for $74.0M consideration with $68.4M of goodwill, the shares outstanding on the cover (171,407,939 as of 2026-04-30) and at the balance-sheet date (171,277K at 2026-03-31), and the China trade-restriction and export-control risk language are all from Astera Labs' Form 10-Q for the quarter ended 2026-03-31, filed 2026-05-06: [Astera Labs Q1 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1736297/000173629726000020/alab-20260331.htm). The absence of material news between that filing and this report's anchor date was checked against the company's EDGAR filing index; the only subsequent 8-K, filed 2026-06-08, reports the results of the 2026 annual stockholders meeting: [Astera Labs EDGAR filings](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001736297&type=10-Q&dateb=&owner=include&count=40).
- Governance facts are from the proxy and the annual report: the executive-officer table (Desmond Lynch, Chief Financial Officer, officer since 2026; Philip Mazzara, General Counsel and Secretary, officer since 2022), Lynch's biography (Chief Financial Officer of Rambus from August 2022 to February 2026), the disclosure that Michael Tate retired as Chief Financial Officer on March 2, 2026 and intends to provide transition services as a Strategic Advisor to the CEO until September 1, 2026, and the board composition and director classes are from the definitive proxy statement filed 2026-04-23: [Astera Labs 2026 DEF 14A](https://www.sec.gov/Archives/edgar/data/1736297/000114036126016359/ny20065212x1_def14a.htm). Desmond Lynch's signature as Chief Financial Officer appears on the Q1 2026 Form 10-Q cited above. The headcount of 756 full-time employees at 2025 year-end (527 in North America, 208 in Asia, 21 in Europe) is from the Human Capital section of the FY2025 Form 10-K, filed 2026-02-20: [Astera Labs FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1736297/000173629726000010/alab-20251231.htm).
- **Earnings-call figures (not in the press release or the filings), labelled as such:** PCIe Gen 6 contributing more than one-third of total revenue; over $1,000 of content per accelerator; the expectation that Scorpio becomes the largest product line by the end of 2026, surpassing Aries and Taurus; two additional major hyperscalers expected to begin receiving Scorpio P-Series in late 2026; Leo on track for an early ramp with Microsoft Azure M-series plus a custom KV-cache design win shipping in 2027; Taurus expanding to 1.6T Ethernet and Aries to PCIe 7; the statement that supply is in place through the end of the year with a diversified back-end supply chain and 75 days of inventory; the attribution of roughly 200 basis points of the Q2 gross-margin step-down to a non-cash impact from a recently executed warrant agreement with a customer; and the guidance that NVLink Fusion custom solutions and UALink switches both start contributing revenue in 2027. These come from Q1 2026 earnings-call coverage: [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/05/05/astera-labs-alab-q1-2026-earnings-transcript/) and [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-astera-labs-beats-q1-2026-estimates-shares-rise-93CH-4677421). Where the two transcripts differ on a product name, the filing-consistent spelling (Taurus) is used. This report does not assert that the warrant referenced on the call is the same instrument as the February 2026 warrant disclosed in the 10-Q; the company has not said so.
- Product and market claims from company announcements: the Scorpio X-Series 320-lane scale-up fabric switch with Hypercast and in-network compute engines, shipping as of 2026-05-05 with production ramp in H2 2026, and the company-cited third-party projection of a merchant scale-up switch silicon market reaching $20 billion by 2030, are from [the Scorpio X-Series announcement](https://www.globenewswire.com/news-release/2026/05/05/3288226/0/en/Astera-Labs-Extends-Leadership-in-Open-AI-Scale-Up-Networking-with-New-320-Lane-Scorpio-X-Series-Smart-Fabric-Switch.html). The NVLink Fusion relationship is from [the May 2025 collaboration announcement](https://www.asteralabs.com/news/astera-labs-expands-collaboration-with-nvidia-to-advance-nvlink-fusion-ecosystem/) and [the December 2025 custom-solutions announcement](https://www.asteralabs.com/news/astera-labs-expands-connectivity-portfolio-with-custom-solutions/). No revenue, design-win value or purchase commitment is disclosed in any of them. The $20 billion market projection is reported for context only and no figure in this report is derived from it.
- Historical financials used for trailing-twelve-month and multi-year figures - FY2022 revenue $79.9M, FY2023 $115.8M, FY2024 $396.3M with a $116.1M operating loss, FY2025 revenue $852.5M with $173.4M of operating income and $219.1M of net income, and the quarterly series for the four quarters ended 2026-03-31 (revenue $191.9M / $230.6M / $270.6M / $308.4M; operating cash flow $135.4M / $78.2M / $95.3M / $74.6M; capital expenditure $2.0M / $12.3M / $18.7M / $7.6M) - were pulled from Yahoo Finance/yfinance on 2026-07-31 and reconcile to the company's own Q1 2026 release for the overlapping quarter. Trailing-twelve-month revenue ($1,001.4M), operating income ($224.0M), net income ($267.6M) and free cash flow ($342.8M) are computed as the sum of those four quarters; trailing per-share figures are not used because per-share amounts are not strictly additive across periods.
- Share price ($299.69, the 2026-07-30 close), the July 2026 price path (2026-07-06 close $432.74, then $382.89, $393.16, $417.45, $412.97, $362.05, $361.78, $350.62, $319.74, $303.62, $309.09, $319.79, $330.89, $326.97, $291.58, $282.52, $260.23, $249.74 on 07-29 and $299.69 on 07-30), and the trailing-year closing range ($100.27 on 2026-03-30 to $483.02 on 2026-06-30) were pulled via Yahoo Finance/yfinance on 2026-07-31; on an intraday basis the trailing-year high was $499.48 on 2026-06-30 and the low $97.89 on 2026-03-30. No stock split or other corporate action occurred in the period, which was checked directly. US markets had not completed the 2026-07-31 session at the time of writing, so the last completed close is 2026-07-30. Market cap (~$51.37B), enterprise value (~$50.19B) and every multiple are computed from that verified close and the 171,407,939 share count on the 10-Q cover, and are labelled with the 2026-07-30 anchor date. This market-data snapshot can be revised by the data provider and is subsequently maintained by `static/invest/research/update_prices.py`.
- The CY2026 revenue estimate of roughly $1.5B and the CY2027 estimate of roughly $2.25B are this report's own arithmetic (Q1 actual plus the Q2 guide midpoint, then decelerating sequential growth through H2 2026, and 50% growth in 2027) and are not company guidance; Astera Labs gives one quarter of guidance at a time. The reverse test (roughly 44% five-year compound growth to earn 8% a year to a terminal 12x revenue) is likewise this report's own arithmetic. Peer figures for Broadcom, Marvell and Coherent are from the broadcom-2026, marvell-2026 and coherent-2026 reports in this hub, each stated at its own reported period and its own price anchor and not restated to a common calendar. Insider Form 4 and Rule 144 activity in June and July 2026 is stated qualitatively from the EDGAR filing index and is not quantified here. This report does not use non-public information.
