# Aehr Test Systems (AEHR) Deep Research Report

Coverage date: 2026-11-05
Last updated: 2026-11-05
Ticker: NASDAQ: AEHR
Disclaimer: This report is for informational and research purposes only. It does not constitute investment advice. Please conduct your own due diligence.

---

## Executive summary <!-- report-module:overview -->

**One-line thesis:** Effective backlog of $109.3M equals about 93% of remaining FY2027 revenue, so the debate is not about this year. At the 2026-11-04 close of $60.84, the stock needs about $310M of FY2028 revenue (2.07x the FY2027 guide) just to break even at the base-case multiple. That figure is reachable only if a customer that has not placed a production order moves to wafer-level burn-in.

**Stance derivation:** Net judgment: the business is improving and the stock is 58% below its August high. But the price still includes nearly 60% of the increment from full conversion by the evaluation customer (($310M - $213M) / $167M, see §8). The 30/40/30 grid (FY2028 revenue $380M / $230M / $110M) gives $97.65 / $36.08 / $15.80 per share, weighted $48.47, -12.8% annualized to 2028-06-30, 20.8 points below an 8% required return. The ruling is **cautious / low conviction**. This is a valuation call, not a business call. The bull case returns +33.1% annualized, so the ruling is not bearish-avoid; the evaluation decision is expected in 1H CY2027, so conviction can only be low.

**Chain job:** This report tests whether AI-processor burn-in moves from package level to wafer level (`architecture-check`). Test-platform names such as Teradyne and Advantest do not answer that question, and neither does KLA's process-control reading.

| Metric | Value | Basis |
|---|---:|---|
| Share price | $60.84 | 2026-11-04 close, second completed session after earnings |
| Market cap | $2.043B | Treasury-method diluted 33.584M shares; $1.987B on 32.663M basic |
| Net cash | $104.9M | 09-25 cash and equivalents; $0.15M restricted cash excluded; no financial debt |
| Enterprise value | $1.938B | $9.8M operating leases not treated as financial debt |
| EV / FY2027 revenue guide | 12.9x | $150M is guidance, not an actual |
| EV / Q1 annualized revenue | 14.7x | $33.007M × 4 |
| EV / spliced TTM revenue | 26.9x | $72.039M, skips the transition month, construction in §3 |
| Market cap / FY2027 non-GAAP net income floor | 68.1x | At least 20% × $150M = $30M, company basis, not tax-normalized |
| Market cap / Q1 annualized tax-normalized GAAP net income | 93.3x | $6.927M × 79% × 4 = $21.9M, derived here |
| Backlog | $100.9M / $109.3M | 09-25 / 11-01 effective |
| Bookings / book-to-bill | $46.7M / about 1.4 | Q1 FY2027 |
| Next hard node | 1H CY2027 | Evaluation customer's production decision (company framing) |

**The five facts that matter most:**

1. Q1 FY2027 (06-27 to 09-25) revenue was $33.007M, +200% YoY (against the quarter ended 2025-08-29, not a calendar-aligned quarter) and +75% QoQ (against the 05-29 quarter, skipping the transition month); GAAP gross margin 47.5%; net income $7.181M, including a $0.254M tax benefit. [Release](https://www.sec.gov/Archives/edgar/data/1040470/000165495426009385/aehr_ex991.htm)
2. Operating cash flow was -$3.054M, and RSU tax withholding took another $4.474M. Cash has fallen $11.456M since 05-29. FY2026 ATM sales raised $97.4M net; without that money, 09-25 cash and equivalents would be about $7.5M (derived). [10-K](https://www.sec.gov/Archives/edgar/data/1040470/000165495426006919/aehr_10k.htm)
3. The evaluation customer described as one of the largest opportunities has so far decided only to buy one fully configured FOX-XP test cell, to evaluate at a Taiwan OSAT, with installation in early 2027. This is not a production order.
4. The company has run a very similar script before: the FY2024 revenue guide went from at least $100M to $75-85M to above $65M, and the actual was $66.2M, with the largest customer at 67% of revenue. The stock fell from a $53.69 close on 2023-08-01 to $10.17 on 2024-06-26.
5. Since 2026-04, insiders have sold 677,349 shares for about $60.10M in the open market; the 10b5-1 box is unchecked on all 61 transaction lines, and purchases are zero. Sales were $11.15M on 08-12, the day the $22M order was announced.

**Open at publication:** The Q1 FY2027 10-Q had not been filed when this report was finalized. Customer concentration, product-line split, restricted-cash detail and the cover share count are `review-pending`; see §7.

## 1. Business overview and product economics <!-- report-module:business -->

Aehr makes semiconductor burn-in and reliability-screening equipment. Burn-in runs devices at high temperature and voltage to bring early failures forward. It can happen at wafer stage (the in-house FOX platform) or after packaging (Sonoma/Tahoe/Echo, acquired with Incal in July 2024). The company reports one segment and had 138 regular full-time employees at FY2026 year-end; headquarters and final assembly of wafer-level systems are in Fremont.

**Revenue structure (10-K, fiscal years ending around May 31):**

| Split | FY2024 | FY2025 | FY2026 | Read |
|---|---:|---:|---:|---|
| Total revenue | $66.218M | $58.968M | $50.001M | Down 24.5% over two years |
| Full-wafer contact product lines | $64.6M (98%) | $39.2M (66%) | $31.5M (63%) | The last cycle was almost entirely here |
| Package-level product lines | $1.6M (2%) | $19.8M (34%) | $18.5M (37%) | Incal consolidated |
| Systems (derived) | $24.169M | $21.978M | $28.669M | Total less contactors and services |
| Contactors | $37.560M | $30.848M | $14.887M | Fell hardest when silicon carbide weakened |
| Contactor share (derived) | 56.7% | 52.3% | 29.8% | Moves a lot within one cycle |
| Services | $4.489M | $6.142M | $6.445M | |
| EV and power semiconductor share | 92% | 41% | 17% | 10-K ESG section basis |
| Asia / US / Europe and Middle East | 87.7% / 5.3% / 7.0% | 62.9% / 30.0% / 7.1% | 45.6% / 41.3% / 13.1% | By ship-to location |

**New Q1 FY2027 readings (call):** Contactors and related products (WaferPaks, burn-in modules or BIMs, burn-in boards or BIBs) were $13.5M, 41% of revenue, against $2.6M a year earlier. Management expects about 35% for FY2027 and about 30% in the long-term model; for FY2026 the CFO's figures on the call varied, and the 10-K gives 29.8%. At 35%, FY2027 is about $52.5M (derived). The CEO also says it could reach 50% even in a good year; that is an expectation and should be read against the decline in the table above.

**Be clear about what the consumables are.** WaferPaks are custom per device with a typical life of two to seven years (10-K). The CEO says about one-third of each sale is WaferPaks, and customers buy another round when new devices launch (call). This is repurchase driven by capacity additions and new devices, not usage-based recurring revenue. Contactor revenue fell 60.4% from FY2024 to FY2026, which proves it shrinks with the cycle.

**The CEO's unit economics (call, company framing):** A 9-wafer FOX-XP with consumables sells for about $7M (transcripts differ, "$6.7-plus" and "$6 million, $7 million plus"; $35-70M over 5-10 systems implies $7M). Each million devices of annual output needs 5-10 systems, or $35-70M per million. He estimates about 25 million accelerators in 2027, with CPUs at double that.

Our read (inference): the $35-70M applies to **incremental** annual capacity, not to revenue that recurs each year. A system bought once runs for years, so equipment revenue follows the change in output rather than its level. That makes this company's revenue steeper than AI chip shipments, and more prone to drawdowns.

**Manufacturing is asset-light:** Q1 capex was just $0.049M. Sonoma is finally assembled and shipped directly by a Southeast Asian contract manufacturer; the CFO says this adds capacity of more than 20 systems per month. The CEO says more than a dozen per month are shipping and installing now, and that Fremont assembly hours per wafer-level system can fall to about one-third by year-end (call). Sonoma pricing, margin and contract terms are not disclosed and stay `review-pending`. The price above is on a FOX-XP basis and cannot be used to back into Sonoma revenue; "more than a dozen per month" is present tense in November and is not a Q1 average. This report does not estimate Sonoma revenue by multiplying units by price.

**Announced orders with amounts (company press releases, no 8-K):**

| Date | Product and customer | Amount | Delivery |
|---|---|---:|---|
| 2026-01-08 | Sonoma, multiple customers | over $5.5M | not itemized |
| 2026-02-26 | FOX-XP, first AI-processor production customer | $14M | see release |
| 2026-04-16 | Sonoma, lead hyperscale customer, largest in company history | $41M | from FY2027 |
| 2026-07-14 | Silicon carbide WaferPaks | over $8M | see release |
| 2026-08-12 | FOX-XP, first AI-processor production customer | $22M | next six months |
| 2026-10-07 | Sonoma, second processor | about $6M | next six months |

These announcements are only part of bookings and cannot be summed into backlog. The CFO says Q1 bookings came mainly from FOX systems, WaferPaks and aligners for AI processors and silicon photonics, not Sonoma (call).

## 2. Industry, competition and architecture check <!-- report-module:competition -->

**The architecture question:** AI processors put several compute dies, HBM and I/O chips into one expensive package. A bad die found after packaging scraps the whole package, and dies on one substrate heat differently, so package-level burn-in struggles to bring each one to its optimal screening temperature. The company says that is the case for wafer level (release, call). The opposing case is just as real: wafer level adds dedicated contactor and system spend, and the 10-K explicitly lists customers shortening burn-in times or moving to sampling as yields improve.

| Path | Participants (source) | Current evidence | Our read |
|---|---|---|---|
| Wafer-level burn-in | Aehr FOX (the company says only it can run this in volume today) | First AI-processor production customer added $22M in August, for its Taiwan manufacturing partner | One customer's production evidence: strong but narrow |
| Package-level burn-in | Aehr Sonoma; customer-built or affiliated suppliers (10-K, call) | Lead hyperscale customer ramping at more than a dozen per month | The revenue engine, and the concentration source |
| System-level test derivatives | Hon Precision (Cohu in one transcript), Chroma, AEM, Teradyne (CEO on the call) | CEO says package-level prospects are not raising SLT alternatives | Aehr's own account; the next two rows are contrary evidence |
| Teradyne Titan HP | [2026-10-06 announcement (trade-press reprint; the original page could not be retrieved)](https://iconnect007.com/article/151877/teradyne-introduces-titan-hp-platform-for-ai-data-center-devices/151874/ein) | Described as a "production-ready" enhanced burn-in system; says AI accelerators are entering the category needing burn-in | A large vendor targets the same budget. No production customer verified. AEHR -11.7% and SMH -0.2% that day; a date match only, causation unverified |
| AEM AMPS-BI | [2024-07-09 company release](https://aem.com.sg/news/aem-introduces-the-new-generation-of-automated-burn-in-systems-for-ai-and-high-performance-compute-chip-testing/) | Says it was selected as Plan-of-Record by an unnamed major fabless HPC and AI chip company | A rival already claims a production selection in package level |
| ATE plus prober | Advantest V93000, Teradyne UltraFLEX (CEO on the call) | Low parallelism but already on every line | Not burn-in, but may absorb some screening budget |
| Rack-level burn-in | Server makers (CEO on the call) | The earliest stopgap | Highest cost; the source of the demand |
| Chinese domestic rival | Suzhou Semight (10-K Note 9, patent suit) | Part of the claims upheld after two invalidation petitions | IP position in China is not fully secure |

**Evidence grading:**

| Claim | Evidence level | Basis |
|---|---|---|
| Wafer-level burn-in is in AI-processor production | Fact (company announcement) | 2026-08-12 $22M follow-on production order, nine 300mm wafer configuration |
| A second major customer will convert | Has not happened | Only the evaluation cell is bought; the company says the decision comes months after installation and validation |
| Second hyperscale processor out-volumes the first | Customer forecast, relayed by the company | October release: about $6M follow-on for initial production sampling and expected ramp |
| More than a dozen future customers | Management judgment | Release; no dollar split |
| Silicon carbide recovery | Partly fact | 17% of FY2026 (10-K EV and power basis); on the call the CEO said both "less than 10%" and "about $10 million", while 10% of $50M is $5M, so the figures do not reconcile; we use the 10-K; over $8M of new orders announced 07-14 |

**This report names no customer.** Company documents say only "lead hyperscale customer", "lead AI processor customer" and "a major supplier of AI accelerators, CPUs, and network processors". The CEO said on the call that the first wafer-level customer uses TSMC wafers, which is a process fact. Any naming is inference and is not written here.

**Peer valuation (2026-11-04 closes, SEC financial data, computed here):**

| Company | Market cap | Market cap / TTM revenue | Market cap / latest quarter annualized revenue | TTM GAAP P/E | Note |
|---|---:|---:|---:|---:|---|
| Teradyne (TER) | $39.19B | 7.8x | 7.5x | 28.5x | Platform test leader |
| FormFactor (FORM) | $6.68B | 6.8x | 6.0x | 38.5x | Probe cards; net income not adjusted for one-offs |
| Cohu (COHU) | $2.08B | not computed | 3.0x | n/a | Near break-even; TTM could not be spliced reliably |
| Aehr (AEHR) | $2.04B | 28.4x | 15.5x | n/a | Spliced TTM; FY2026 was a net loss |

Aehr's market cap is close to Cohu's, but Cohu's quarterly revenue of $173M is more than five times Aehr's. The difference is what is being paid for the architecture option.

**Direction of the cross-checks:** The ASE and Amkor reports address packaging ownership, Broadcom and Marvell address custom-silicon volume, and KLA addresses fab yield. This report asks whether one specific process step moves forward. Tool orders prove neither final yield nor customer identity.

## 3. Financial health, cash quality and red flags <!-- report-module:financial -->

**Fiscal-year change:** On 2026-04-02 the board moved the year-end from the Friday nearest May 31 to the Friday nearest June 30. FY2027 runs 2026-06-27 to 2027-06-25. The period 2026-05-30 to 06-26 is a separately reported 28-day transition period. Neither `fiscalYearEnd: 1231` in SEC metadata nor `--12-31` in the 10-K's XBRL is usable. [8-K](https://www.sec.gov/Archives/edgar/data/1040470/000165495426003310/aehr_8k.htm)

**Quarters and transition period ($ thousands):**

| Period | End date | Revenue | GAAP gross profit | Gross margin | Operating income | Net income | Bookings $M | Ending backlog $M |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Q1 FY26 | 2025-08-29 | 10,969 | 3,719 | 33.9% | (4,066) | (2,084) | 11.4 | 15.5 |
| Q2 FY26 | 2025-11-28 | 9,884 | 2,545 | 25.7% | (4,648) | (3,230) | 6.2 | 11.8 |
| Q3 FY26 | 2026-02-27 | 10,313 | 3,368 | 32.7% | (4,229) | (3,203) | 37.2 | 38.7 |
| Q4 FY26 | 2026-05-29 | 18,835 | 8,019 | 42.6% | (1,206) | 1,391 | 60.7 | 80.6 |
| Transition | 2026-06-26 | 638 | (1,012) | n/a | (3,995) | (2,743) | not disclosed | not disclosed |
| Q1 FY27 | 2026-09-25 | 33,007 | 15,663 | 47.5% | 6,047 | 7,181 | 46.7 | 100.9 |

Q2 FY26 net income is derived as the FY2026 total less the other three quarters. Backlog roll-forward: $80.6M + $46.7M - $33.007M - $0.638M = $93.655M, $7.245M short of the reported $100.9M, implying about $7.2M of transition-month bookings (derived; not disclosed by the company). The CFO's "up from $80.6 million" skips the transition month: without deducting transition revenue, $94.3M is $6.6M short of $100.9M. Backlog is defined as shipping within 12 months, which does not mean all of it lands in FY2027, so 93% is an upper bound on coverage; whether the evaluation cell is in backlog is also undisclosed.

**How the spliced TTM is built:** The company gives no continuous 52-week figure. This report uses Q2-Q4 FY26 plus Q1 FY27: $50.001M - $10.969M + $33.007M = **$72.039M**, skipping the transition month. Adding the transition month's $0.638M gives $72.677M, but that spans 56 weeks, not a year. Over the same window net income was +$2.139M and -$0.604M with the transition month, so **including the transition month flips the sign of net income**; operating cash flow was -$6.082M, or -$9.894M with the transition month. The $150M FY2027 figure excludes the transition month.

**Financial health matrix:**

| Item | Current | Comparison | Read | Grade |
|---|---|---|---|---|
| Growth | Q1 revenue +200% YoY | FY2026 -15.2% | Bottom turn on a low base | A- |
| Gross margin | GAAP 47.5%, non-GAAP 48.5% | FY2026 35.3%, FY2024 49.1% | Volume and mix; CFO says Q2 will be below Q1 on Sonoma mix | B+ |
| Operating leverage | Opex $9.616M, 29% of revenue | Q1 FY26 71% | Real, though the company says it will keep investing | B+ |
| Tax | Effective rate -3.7% | Statutory 21% | Lifts net income; see below | C |
| Cash conversion | Operating cash flow -$3.054M | Net income $7.181M | Receivables -$10.686M, inventory -$9.037M, payables +$6.230M | C |
| Inventory | $53.120M, about 279 days of cost | 05-29 $41.354M | CFO: long-lead parts for the AI ramp; 10-K warns of write-down risk | C+ |
| Receivables | $26.630M, about 73 days | 05-29 $17.473M | Shipments concentrated late in the quarter | B- |
| Balance sheet | Cash $104.902M, no financial debt | Equity $222.112M | Not short of money for a year, but the money came from shareholders | B+ |
| Dilution | 32.663M shares at 09-25 | 29.877M at 2025-05-30 | ATM added 1.943M; the rest about 0.66M a year | C+ |

**Red flags and explanations:**

- **Earnings quality.** Q1 pre-tax income was $6.927M and net income was higher at $7.181M. The CFO attributes the tax benefit mainly to disqualifying dispositions of options and excess RSU tax benefits (call), which track a high share price and will not persist. The non-GAAP measure does not normalize tax either: non-GAAP pre-tax $9.103M, net income $9.357M. Normalized at 21% that is $7.19M, 21.8% of revenue, not the reported 28.3% (derived).
- **The guide's implied fade.** The 07-14 guide was 18-22%; it is now at least 20%, or $30M. Q1 already supplied $9.357M, so the remaining three quarters need only $20.643M, 17.6% of $116.993M, below Q1's 28.3%. This is a floor, not a forecast, and Q1 includes a tax benefit. It may reflect tax normalization and Q2 mix, or simple conservatism; the CEO himself says "trying to be conservative" (call).
- **Deferred tax asset $25.120M.** This is 11.3% of equity. The 10-K says plainly that one basis for carrying no allowance is the expected return to profit in FY2027 and the backlog. If the forecast fails, an allowance is possible. Federal NOLs are $51.5M, of which $38.1M do not expire but carry an 80% limit. Near-term cash tax therefore runs below the book rate; this report does not add that to valuation (sensitivity in §8.2).
- **One-offs.** FY2026 other income includes a $1.3M employee retention credit refund; Q1 FY26 other income was $1.051M. Neither touches Q1 FY27.
- **Quarter-end revenue concentration.** The 10-K says a substantial portion of revenue is realized near quarter-end and that non-standard products defer revenue until customer specifications are met. Quarterly swings are structural.

**Incal's effect on EV:** Acquired 2024-07-31 for $22.153M fair value: $10.631M cash, 552,355 restricted shares at $9.381M, $2.381M escrow payable, -$0.240M working capital adjustment. The $2.5M escrow was released as $0.7M in FY2025 and $1.8M in FY2026, and the 10-K shows a zero escrow payable balance. The 10-K contains no acquisition-related contingent consideration. Incal is therefore not an EV adjustment. Q1 FY27 acquisition adjustments are $296K on both the operating and pre-tax lines, against $342K and $365K a year earlier, which shows escrow accretion has reached zero; the release's footnote wording is a leftover.

**Cash bridge (05-29 to 09-25, $ thousands):**

| Item | Transition | Q1 FY27 | Total |
|---|---:|---:|---:|
| Operating cash flow | (3,812) | (3,054) | (6,866) |
| Capex | (4) | (49) | (53) |
| RSU tax withholding | (71) | (4,474) | (4,545) |
| Issuance-related costs | (176) | (161) | (337) |
| Employee stock plan proceeds | 13 | 337 | 350 |
| FX | 0 | (5) | (5) |
| Change in cash, equivalents and restricted cash | (4,050) | (7,406) | (11,456) |

The company has no repurchase plan (10-K). The largest financing outflow in Q1 is RSU tax withholding, which is a cash cost of employee pay.

## 4. Management, governance and capital allocation <!-- report-module:management -->

**Guidance credibility (read both periods):**

| Period | What the company said | Outcome |
|---|---|---|
| FY2024 | At least $100M in 2023-07; cut to $75-85M in 2024-01; cut to above $65M in 2024-03 | Actual $66.2M, 34% below the first guide. Effective backlog of $39.7M in 2023-07 became backlog of $3.0M at 2023-11-30 in about 4.5 months, with bookings of $2.2M that quarter, as EV customers slowed |
| FY2025 | At least $70M in 2024-07; withdrawn in 2025-04 on tariffs; not reinstated by 2025-10 | FY2025 $59.0M, net loss $3.9M; FY2026 $50.0M |
| 2H FY2026 | In 2026-01, guided revenue $25-30M and bookings $60-80M | Revenue $29.1M in range; bookings $97.9M above the top |
| FY2027 | Guided $130-150M in 2026-07; moved to $150M in 2026-11 | To be tested; effective backlog equals about 93% of remaining revenue |

Our read: the latest record is clearly better than FY2024, and $100.9M of backlog is a different foundation from $3.0M. But both times management used customer forecasts to carry the narrative at a cycle turn. The difference this time is that orders have arrived; the FY2028 portion still rests on forecasts.

**Equity financing (fact):** This is where the FY2026 cash increase came from; operations did not produce it.

| Date | Item | Shares | Avg. price | Gross |
|---|---|---:|---:|---:|
| 2025-11 | $40M ATM | 384,380 | $25.89 | about $10.0M |
| 2026-02 | $40M ATM | 269,439 | $39.20 | about $10.5M |
| 2026-03 | $40M ATM | 476,649 | $40.88 | about $19.5M |
| 2026-04 | $60M ATM (William Blair, Craig-Hallum, commission up to 3%) | 812,185 | $73.87 | about $60.0M |
| Total | $100M shelf fully used | 1,942,653 | $51.48 | about $100M; FY2026 net $97.4M |

On 2026-07-27 the company filed an S-3ASR automatic shelf; the registration statement text lists no offering cap (the fee exhibit was not read). Per our 11-05 poll of SEC submissions, no 424B5 has been filed since 2026-04-08: **there is no ATM today, but the shelf is effective and one prospectus supplement can start one**. Authorized shares are 75 million against 32.66 million issued. On timing, management sold stock near $74, the shares then reached $145, and they are now back at $60.84. The financing was a rational response to cash needs and valuation, and it is also a precedent for future dilution.

**Insider transactions (parsed from Form 4s since 2026-03, excluding originals superseded by a 4/A, 213 transaction lines):**

| Month | Sales (code S) shares | Amount | Avg. price | Main sellers |
|---|---:|---:|---:|---|
| 2026-04 (9th to 22nd) | 512,991 | $40.22M | $78.40 | CEO $10.79M, director Scott $8.38M, chairman Posedel $7.20M |
| 2026-05 | 8,889 | $0.94M | $105.27 | Director Slayen, CFO Siu |
| 2026-07 | 20,000 | $1.64M | $82.13 | Director Scott |
| 2026-08 (4th to 17th) | 135,469 | $17.30M | $127.74 | CEO $5.23M, Slayen $2.92M, Scott $2.63M |
| Total | 677,349 | $60.10M | $88.73 | Purchases (code P): zero |

- The 10b5-1 box is unchecked on all 61 code S lines. Withholding (code F) is not a sale and is counted separately: 55,903 shares and $4,474,357 in the Q1 window, 682 shares and $70,811 in the transition month, matching the $4,474K and $71K in cash flow exactly.
- April sales overlap the company's ATM (04-08 to 04-17) in time: insiders averaged $78.40 in April, the company $73.87. Scott's 04-09 sale is counted at the 40,000 shares corrected by the 4/A.
- On 08-12 the company announced the $22M order, and code S sales that day totaled 85,130 shares and $11.15M: the CEO (indirect) 40,000 shares and $5.23M, Scott $2.63M, COO Engineer $1.97M, Posedel $1.09M, Oliphant $0.23M.
- On 04-16 the company announced the $41M order, and code S sales that day totaled 36,381 shares and $3.01M: Posedel, Danesh, Oliphant, Rogers, Sporck.
- These are date facts; we make no judgment about motive.
- There is no code S from 09-01 to 11-05: code F 15,854 shares and $1.47M, ESPP purchases (code J) 9,606 shares, Posedel's exercise and hold of 18,000 options, and a 2,169-share new-director grant.
- Proxy basis (08-27): all directors and executive officers beneficially held 1,488,042 shares, 4.6%.

**Large holders (13G, event-date basis):**

| Holder | Event date | Shares | Share | Read |
|---|---|---:|---:|---|
| Jane Street Group | 2026-07-24 | 1,648,523 | 5.1% | New; a market maker, so the position may include hedges or trading inventory (inference). The proxy shows 5.0% on a different denominator |
| FMR LLC | 2026-06-30 | 1,006,830 | 3.2% | Exit-type amendment below 5%; 2,142,639 shares and 7.0% at 2026-03-31 |
| AWM Investment | 2026-06-30 | 374,808 | 1.1% | Exit-type amendment below 5% |
| BlackRock | 2024-01 13G | 2,077,807 | 6.4% | The proxy reuses a nearly three-year-old 13G; not a current holding |

**Governance:** On 2026-10-24 the board went from six seats to seven. Narsing Vijayrao (formerly VP of Infrastructure at Meta, 2013-04 to 2026-08; before that at AMD) joined effective 10-28 and sits on the Compensation Committee; the 8-K reports no Item 404(a) transactions. At the 10-19 annual meeting, founder and chairman Posedel drew 13,494,820 votes for and 2,583,535 withheld, the most withheld of the six nominees. The auditor is BPM LLP. The company discloses manual-process risk in its SOX 404 work and is a non-accelerated filer (FY2026 10-K cover).

## 5. Bull case <!-- report-module:bullBear -->

1. **Orders have shown this is not just a story.** Three straight quarters of bookings at $37.2M / $60.7M / $46.7M total $144.6M, almost 3x FY2026 revenue. Backlog went from $11.8M to $100.9M.
2. **The evaluation customer alone could reshape the company.** On the CEO's $35-70M per million, if 3.3 million of this customer's units move to wafer level, about 13% of his 25 million accelerator estimate for 2027, that is about $167M at the $50M midpoint, more than all of FY2027 revenue.
3. **There is a physical reason for the step to move forward.** The CEO says dies in a multi-chip package heat differently, so package level cannot bring each to the same burn-in condition; the new DiTC contactor controls temperature per die on the wafer and will be used in the evaluation cell (call). If true, the Sonoma relationship becomes a sales channel for FOX.
4. **The second hyperscale processor buys time.** It has completed Sonoma qualification, about $6M of follow-on orders came in October, and the customer forecasts ultimately higher volume than the first device, at higher power.
5. **Operating leverage is visible.** Q1 revenue was 3x the prior year while opex rose only 24%, for an 18.3% GAAP operating margin.
6. **FY2027 looks conservative.** The remaining three quarters need $117M, effective backlog is $109.3M, and the CEO says supply is not the limit and orders can still ship this year.
7. **The price has already fallen hard.** $60.84 is 58% below the 08-17 close of $145.61.

**Valuation implication:** The bull case has FY2028 revenue of $380M and $97.65 per share, +60.5% from the price, +33.1% annualized (construction in §8.1). It requires the evaluation customer to decide on conversion in 1H CY2027 and take delivery of equipment for about 3.3 million units within FY2028.

## 6. Bear case <!-- report-module:bullBear -->

1. **What is priced is not this year.** At the base-case multiple, a zero return needs about $310M of FY2028 revenue and an 8% return about $337M, both above our $230M base case. Going from the roughly $168M annualized Q4 FY2027 run rate (derived) to $310M leaves a gap that essentially only the evaluation customer can fill.
2. **An evaluation is not an order.** Installation is in early 2027, with the decision months later; the company itself notes features still to be proven in a volume-production configuration. The CEO used the words "upside and risk". This customer's visibility at a Taiwan OSAT means failure would be just as public.
3. **Concentration changed names but did not leave.** FY2026 top five were 70%, with three at 26%/14%/11%; the largest was 67% in FY2024. The two main Q1 revenue contributors named are single-customer programs. "More than a dozen" is potential, not revenue.
4. **This is an incremental-capacity business.** AI chip output can keep rising at a slower rate and equipment revenue can still fall. The 10-K says most orders can be cancelled or rescheduled with limited penalties and that backlog does not assure revenue. The -60.4% in contactors from FY2024 to FY2026 is a real sample.
5. **Screening intensity can fall.** The 10-K says customers may shorten burn-in or move to sampling as yields improve. Burn-in is heaviest early in a device's ramp and may not stay there as it matures.
6. **Cash did not come from operations.** TTM operating cash flow is -$6.082M, and a revenue ramp consumes working capital first. A shelf is in place, and the company has sold stock when prices were strong.
7. **Insiders only sell.** About $60.10M sold, zero purchases; FMR went from 7.0% to 3.2%. It proves nothing by itself, but there is no offsetting signal.
8. **Its own product and large vendors compete for the same budget.** The CEO says the real competition to package level is FOX, so a wafer-level win would offset some Sonoma demand. Teradyne launched a burn-in offering in October, and AEM claims a Plan-of-Record customer.
9. **Volatility is its own risk.** Beta to SMH is about 2.5 (88 sessions since 07-01, correlation 0.73, computed here). The 2025-04-08 close of $6.78 put EV at about 2.9x FY2025 revenue.

**Valuation implication:** Base $36.08 (-40.7%), bear $15.80 (-74.0%, -55.8% annualized). The bear-case revenue of $110M is still 2.2x FY2026, so this is not a return to the trough.

## 7. Key uncertainties and thesis-breaking conditions <!-- report-module:uncertainties -->

| Uncertainty | Why it matters | When it can be confirmed | What it falsifies |
|---|---|---|---|
| Whether the evaluation customer converts | Decides $230M versus $380M | 1H CY2027; CEO framing is next steps after seeing data | A production order falsifies cautious; a rejection or no decision falsifies the bull case |
| Timing of the second processor | Main increment in the base case | Follow-on orders during CY2027 | Slipping past 2027 weakens the base case |
| FY2027 Q2 and Q3 bookings | Only new bookings can support FY2028 | Next two reports | Persistently under $40M points down; $60M or more points to an upgrade |
| Sonoma margin structure | Size of the Q2 gross margin dip | Q2 FY27 | Full-year non-GAAP gross margin under 47% weakens the base case |
| Whether a new ATM starts | Cash and dilution | Any time, watch 424B5 filings | See monitor `cash-and-dilution` |
| Normal tax rate | Valuation denominator | Pace of deferred tax use | A long-run rate under 21% helps cash |

**`review-pending` (waiting on the Q1 FY2027 10-Q; a non-accelerated filer's 45-day deadline implies about 2026-11-09, derived):**

- Latest cover share count; this report uses 32.663M at 09-25 as the floor and 33.584M diluted.
- Q1 customer concentration, geography and product split.
- Transition-month bookings and further detail.
- Purchase commitments and vendor prepayments.

**Other unknowns:** The company does not disclose AI-processor share of revenue, Sonoma pricing and product-level margins, the evaluation cell's value, payment terms and whether it is in backlog, or how much of the $22M order lands in FY2027. **Transcript-based figures:** call content comes from third-party transcripts; the company's IR webcast is the canonical source, and we did not compare against the audio word for word.

**Thesis-breaking conditions:** A production order from the evaluation customer large enough to support FY2028 revenue above $310M breaks this report's negative-skew conclusion. A cut in the FY2027 guide below $130M, or cancellation of the second processor, should reduce the bull weight.

## 8. Valuation context, reverse growth and scenario returns <!-- report-module:valuation -->

**Price and share basis:** $60.84 is the 2026-11-04 close (Nasdaq and CNBC agree). Results came after the 11-02 close, so 11-03 and 11-04 are both post-earnings closes and no price fork is needed. Shares use the treasury method: 32.663M (issued at 09-25) + 0.693M RSUs (07-23) + 0.228M options (0.252M × (1 - $5.81/$60.84)) = **33.584M**, market cap $2.043B. The quarter's diluted weighted average of 33.520M uses the quarter's average price and serves only as a check; 32.663M basic gives $1.987B. The RSU count is as of 07-23, includes the 07-01 grants, and overlaps slightly with 09-25 issued shares, an error under 0.05M. PRSU over-achievement (up to about 0.07M shares) and future grant capacity are not counted.

**Cash:** Cash and equivalents of $104.902M go into EV; the $105.1M figure includes $0.150M restricted cash and is not used. That $0.150M is identical at 05-29, 06-26 and 09-25, and the 10-K describes restricted cash as a manufacturing and office lease deposit (rounded to $0.2M), so we treat it as the same item (inference). No financial debt. Operating leases of $9.804M are excluded. Incal has no contingent consideration. EV = $2.043B - $104.9M = **$1.938B**.

| Valuation method | Input | Result | Meaning |
|---|---|---:|---|
| EV / FY2027 guide | $150M, guidance | 12.9x | About twice the TER and FORM market-cap multiples |
| EV / Q1 annualized | $132.0M | 14.7x | Q1 includes some pull-ins, per the CEO |
| EV / spliced TTM | $72.039M | 26.9x | Low denominator; not useful alone |
| Market cap / FY2027 non-GAAP net income floor | $30M | 68.1x | Company basis |
| Market cap / Q1 annualized tax-normalized GAAP net income | $21.9M | 93.3x | Derived here |
| Market cap / equity | $222.1M | 9.2x | Equity includes $25.1M deferred tax asset |
| Scenario grid | FY2028 | see §8.1 | Conditional values, not targets |

**FY2027 to FY2028 bridge (derived here; none of these are company targets):**

| Step | Amount | Basis |
|---|---:|---|
| FY2027 quarterly path | $33M / $36M / $39M / $42M = $150M | CEO: each remaining quarter grows a little, Q4 highest; the split is derived |
| Q4 annualized run rate | $168M | $42M × 4 |
| Second hyperscale processor increment | +$25M | Customer forecast; only about $6M ordered |
| Silicon photonics, SiC, GaN and other increment | +$20M | Multiple follow-on orders; no dollar guide |
| Subtotal excluding the evaluation customer | $213M | |
| Evaluation customer: partial or late conversion | +$17M | About 0.33 million units × $50M |
| Evaluation customer: converts 1H CY2027, delivers in FY2028 | +$167M | About 3.3 million units × $50M, about 13% of 25 million |
| Revenue drawdown path | $110M | 27% below FY2027; FY2024 to FY2026 was -24.5% |

## 8.1 Valuation scenario grid <!-- report-module:valuation -->

Returns run from 2026-11-04 to 2028-06-30, 604 days or 1.654 years. Exit uses full-year FY2028 figures, a trailing multiple; the market will be looking at FY2029 by then, so this setting leans conservative. GAAP basis, with opex including SBC. Tax is 21% throughout.

| Scenario | FY2028 revenue and driver | GAAP gross margin / opex / operating margin | After-tax operating income × exit multiple | Ending cash / shares | Per share / vs $60.84 / annualized | Probability weight |
|---|---|---|---|---|---|---:|
| Bull case | $380M: evaluation customer converts and ramps | 50% / $72M / 31.1% | $93.22M × 35 = $3,262.7M | $155M / 35.0M | $97.65 / +60.5% / +33.1% | 30% |
| Base case | $230M: existing programs continue, evaluation customer late and small | 48% / $60M / 21.9% | $39.82M × 28 = $1,114.8M | $130M / 34.5M | $36.08 / -40.7% / -27.1% | 40% |
| Bear case | $110M: evaluation customer stays out, hyperscale digestion after the ramp | 42% / $48M / -1.6% | Too little profit, so 4x revenue = $440.0M | $105M / 34.5M | $15.80 / -74.0% / -55.8% | 30% |

**Weighted $48.47, -20.3% from the price, -12.8% annualized, 20.8 points below the 8% hurdle.**

## 8.2 Valuation inputs, reverse expectations and sensitivity <!-- report-module:valuation -->

**The basis for each input:**

- **Gross margin.** The CFO gives about 48.5% non-GAAP for FY2027, plus or minus half a point; GAAP runs about 1 point lower. 50% needs a high consumables mix and scale, near FY2024's 49.1%. 42% sits between FY2025's 40.6% and today.
- **Opex.** Q1 annualizes to $38.5M. The company says it will add engineering, support and sales (call). $60M is 26% of revenue, below Q1's 29%.
- **Tax.** 21% is the federal statutory rate, unlike Q1's -3.7% and the company's non-GAAP treatment. State taxes push it up; R&D credits and FDII push it down. Near-term cash tax is below this, and NOLs are not in the valuation.
- **Exit multiples.** 28x is about TER's current 28.5x TTM P/E; 35x is below FORM's 38.5x, but for a smaller and more concentrated company the growth premium has to come from here. 4x revenue is above Cohu's 3.0x annualized and Aehr's roughly 2.9x at its 2025-04 low.
- **Ending cash.** From $104.9M, add two years of after-tax operating income and SBC, less working capital (about 25% of the revenue increase), capex and RSU withholding. The bear case assumes working capital release offsets inventory write-downs and withholding, so it stays flat.
- **Shares.** From 33.584M, using FY2026's non-ATM net increase of about 0.66M a year, 1.65 years adds about 0.9M to reach 34.5M. The 35.0M in the bull case reflects PRSU over-achievement and larger grants. No scenario assumes a new ATM. A raise at high prices would add cash and shares together, with little per-share effect.

**What is priced in (reverse):** Using the base-case structure (48%, $60M opex, 21% tax, 28x, $130M cash, 34.5M shares):

| Target | Exit per share | Required EV | Required operating income | Required FY2028 revenue | vs FY2027 guide |
|---|---:|---:|---:|---:|---:|
| Zero return | $60.84 | $1,969.0M | $89.0M | $310.4M | 2.07x |
| 8% annualized | $69.10 | $2,253.9M | $101.9M | $337.3M | 2.25x |

Expectation gap: at $60.84 the market prices about $310-337M; our base case is $230M. Against the $213M that excludes the evaluation customer, the $97M increment a zero return requires is about 58% of the $167M from full conversion.

**Balance price and balance multiple:**

- The $48.47 weighted value discounted at 8% is **$42.67**, the 8% balance price. The zero-return balance price is $48.47.
- Raising only the base-case multiple, reaching today's price takes 49.5x and an 8% return takes 56.6x.
- For the weighted value to return 8%: moving only the base case takes 72.7x; moving the bull and base cases together takes +16.4x each (51.4x / 44.4x).
- Weight reverse: with the bear weight fixed at 30%, the bull-case weight must reach **50.1%** for a zero return and 63.5% for 8%.

**In one sentence: the price is neutral only if the evaluation customer's conversion is more likely than not.** That can be falsified, and it is the core of this report's stance.

| Sensitivity | Change | Weighted per share | vs price | Annualized |
|---|---|---:|---:|---:|
| Multiples up | Bull 39x, base 32x | $53.51 | -12.0% | -7.5% |
| Multiples down | Bull 31x, base 24x | $43.42 | -28.6% | -18.4% |
| Mid-case revenue up | Base $260M, opex $62M, that case $44.03 | $51.65 | -15.1% | -9.4% |
| Upside revenue down | Bull $330M, that case $77.90 | $42.54 | -30.1% | -19.5% |
| Weights 40/40/20 | Conversion more likely | $56.65 | -6.9% | -4.2% |
| Weights 50/30/20 | Conversion above even | $62.81 | +3.2% | +1.9% |
| Weights 60/30/10 | Clearly optimistic | $70.99 | +16.7% | +9.8% |
| Weights 20/50/30 | Conversion less likely | $42.31 | -30.5% | -19.7% |
| Adding the deferred tax asset | +$0.73 per share | $49.19 | -19.1% | -12.1% |

No single favorable sensitivity brings the weighted return to 8%; only moving the bull weight to 60% does. Weights are research judgment, and no objective frequency proves them.

**Price action (no causal claim):** 11-03 was +26.5% on 8.75M shares with SMH +2.0%; 11-04 was -6.6% with SMH -2.7%. Facts: Q1 exceeded consensus (CFO; the specific consensus figure was not verified), and the guide moved to the top of its range; short interest on 10-15 was 5,622,469 shares, 17.2% of issued shares (not a free-float basis), about 2.0 days to cover, up about 29% from 08-14, and the 10-30 reading is not yet published; peers on 11-03 were TER +3.2%, FORM +10.9%, COHU +3.4%, and on 11-04 -6.8%, -11.9%, -12.1%; before earnings, from 10-12 to 11-02, the stock fell 34.2% and SMH 14.0%, a ratio of 2.4, close to the 2.5 beta. Inference: the 11-04 pullback coincides with a broad decline in test names and is close to what beta implies (about -6.8%), so it is not attributed to AEHR alone. The cause of the 11-03 gain is **undetermined**: results and guidance were a catalyst and covering is possible, but the split between re-rating and covering cannot be determined. From 08-17 to 08-28 the stock fell 44.5% against SMH -6.9%, far beyond beta, and we found no company-level cause; third-party articles call it profit-taking, unconfirmed. Insider sales of $17.30M from 08-04 to 08-17, before that fall, are a fact but cannot be used to attribute the move.

## 9. Catalysts, timeline and monitoring <!-- report-module:catalysts -->

| Date | Catalyst | What to watch | Impact |
|---|---|---|---|
| 2026-11 (by about 11-09, derived) | Q1 FY27 10-Q | Customer concentration, shares, contract terms | Clears `review-pending` |
| 2026-12-15 | NYC CEO Summit (mentioned on the call) | Any change in framing | Small |
| About late 2027-01 to early 02 (derived from past lags) | Q2 FY27 results | Revenue above Q1, gross margin below Q1, bookings | Bookings matter most |
| Early 2027 | Evaluation cell installed at Taiwan OSAT | On schedule or not | A delay is negative |
| 1H CY2027 | Production decision | The order amount, not the wording | Decides the bull and bear cases |
| CY2027 | Second processor ramp | Sonoma follow-on orders | Decides the base case |
| 2027-06-25 | FY2027 ends | Whether $150M and 20% are met | Delivery check |

**Structured monitoring items (matching `monitoring[]` in `reports.json`):**

| id | Metric | Trigger | Latest reading | Next check |
|---|---|---|---|---|
| `benchmark-wlbi-decision` | Evaluation customer's production decision | Rejection, or no production order by 2027-09-30 | Decided to buy one FOX-XP test cell, to install at a Taiwan OSAT in early 2027; no production order | Q3 FY27 results, about 2027-04/05 |
| `sonoma-second-processor` | Hyperscale customer's Sonoma cadence | Monthly shipments below a dozen with no follow-on for the second device, or second-device ramp slips past 2027 | More than a dozen per month (call); second device qualified, about $6M follow-on | Q2 FY27 results |
| `bookings-backlog` | Bookings and backlog | Book-to-bill below 1.0 in both FY27 Q2 and Q3, or backlog below $80M | Q1 bookings $46.7M, about 1.4; backlog $100.9M, effective $109.3M | Q2 FY27 results |
| `fy27-guide-margin` | FY2027 guide and gross margin | Revenue guide below $130M, or full-year non-GAAP gross margin below 47% | $150M; at least 20% (was 18-22%); Q1 non-GAAP 48.5%; CFO says about 48.5% for the year, plus or minus half a point | Q2 FY27 results |
| `cash-and-dilution` | Cash and dilution | Cash below $75M, or a new ATM or offering under the S-3ASR | Cash $104.902M; Q1 operating cash flow -$3.054M; the old $100M shelf is used up, the S-3ASR is effective, and with no new 424B5 since 04-08 there is no ATM today but one can start at any time | Each report and 424B filing |

## 10. Conclusion <!-- report-module:conclusion -->

**Chain-validation job:** `semicap-equipment` / `architecture-check`. We chose this role because what would most break the thesis is an architecture question: whether AI-processor burn-in moves from package level to wafer level. We chose it over `dashboard` because this company's orders sit in a few programs and cannot read overall AI buildout speed; one customer's shipment timing can change a quarter. The Sonoma cadence stays as a monitor to read custom AI-processor volume, but it is not this report's main job.

**Expectation gap:** $60.84 prices about $310-337M of FY2028 revenue; our base case is $230M.

**Stance and conviction:** The 30/40/30 grid gives $97.65 / $36.08 / $15.80 per share, weighted $48.47, -12.8% annualized, below the 8% required return. The bull-case weight needs to reach 50.1% for a zero return. The ruling is **cautious / low conviction**. It is not `bearish-avoid` because the bull case returns +33.1% annualized at a 30% weight, and the last three quarters of bookings are real. Low conviction has four sources: the conversion decision is binary and resolves within a year; customer identity and Sonoma economics are undisclosed; the 10-Q is not out; and with beta near 2.5, the stock can cross every price line in this report within weeks.

**Upgrade to neutral-watch (any one):**

- The evaluation customer places a production order of at least $30M, single or cumulative (the evaluation cell and small add-ons do not count).
- FY27 Q2 and Q3 bookings are each at least $60M, and the FY2027 revenue guide moves above $150M.
- The stock falls to about $46 or lower with fundamentals unchanged (weighted value then about +3.2% annualized).

**Downgrade to bearish-avoid (any one):**

- The evaluation customer clearly declines to convert, or there is no production order by 2027-09-30.
- The FY2027 revenue guide falls below $130M, or full-year non-GAAP gross margin falls below 47%.
- Book-to-bill is below 1.0 in both FY27 Q2 and Q3.
- The second-processor ramp slips past 2027.
- The stock rises to about $85 or higher with fundamentals unchanged (the bull case then returns only about +8.8% annualized).

## Appendix: sources, definitions and reproducible assumptions <!-- report-module:appendix -->

**Definitions:**

- **Backlog:** Per the 10-K, orders with confirmed purchase orders scheduled to ship within 12 months. **Effective backlog:** ending backlog plus bookings after period-end ($8.4M after period-end at 11-01).
- **WLBI / PLBI:** wafer-level / package-level burn-in. **SLT:** system-level test.
- **TTM (spliced):** Q2-Q4 FY26 + Q1 FY27, skipping the 2026-05-30 to 06-26 transition month.
- **Fiscal year:** FY2026 ended 2026-05-29; FY2027 runs 2026-06-27 to 2027-06-25; the 2028-06-30 exit date approximates FY2028 year-end (the company has not published the exact date).

**Company documents:**

- [Q1 FY2027 release (2026-11-02)](https://www.sec.gov/Archives/edgar/data/1040470/000165495426009385/aehr_ex991.htm): revenue, margin, cash flow, balance sheet, guidance, backlog.
- [FY2026 10-K (2026-07-27)](https://www.sec.gov/Archives/edgar/data/1040470/000165495426006919/aehr_10k.htm): product and geographic splits, customer concentration, backlog definition, ATM (Note 10), Incal, tax, risks.
- [S-3ASR (2026-07-27)](https://www.sec.gov/Archives/edgar/data/1040470/000165495426006922/aehr_s3asr.htm): 32,620,450 shares at 07-20; 252,489 options (average $5.81) and 692,905 RSUs at 07-23.
- [424B5 (2026-04-08)](https://www.sec.gov/Archives/edgar/data/1040470/000165495426003353/aehr_424b5.htm), [8-K ATM agreement (2026-04-08)](https://www.sec.gov/Archives/edgar/data/1040470/000165495426003355/aehr_8k.htm), [8-K ATM completed (2026-04-20)](https://www.sec.gov/Archives/edgar/data/1040470/000165495426003746/aehr_8k.htm).
- [8-K fiscal-year change (2026-04-07)](https://www.sec.gov/Archives/edgar/data/1040470/000165495426003310/aehr_8k.htm), [8-K new director (2026-10-29)](https://www.sec.gov/Archives/edgar/data/1040470/000165495426009242/aehr_8k.htm), [8-K annual meeting (2026-10-20)](https://www.sec.gov/Archives/edgar/data/1040470/000165495426009056/aehr_8k.htm), [Proxy statement (2026-09-09)](https://www.sec.gov/Archives/edgar/data/1040470/000165495426008222/aehr_def14a.htm).
- Earlier releases: [Q4 FY26](https://www.sec.gov/Archives/edgar/data/1040470/000165495426006655/aehr_ex991.htm), [Q3 FY26](https://www.sec.gov/Archives/edgar/data/1040470/000165495426003310/aehr_ex991.htm), [Q2 FY26](https://www.sec.gov/Archives/edgar/data/1040470/000165495426000197/aehr_ex991.htm), [Q1 FY26](https://www.sec.gov/Archives/edgar/data/1040470/000165495425011494/aehr_ex991.htm), [Q3 FY25 guidance withdrawal](https://www.sec.gov/Archives/edgar/data/1040470/000165495425004020/aehr_ex991.htm), [FY25 guide (2024-07-16)](https://www.sec.gov/Archives/edgar/data/1040470/000165495424009013/aehr_ex991.htm), [Q3 FY24](https://www.sec.gov/Archives/edgar/data/1040470/000165495424004414/aehr_ex991.htm), [Q2 FY24](https://www.sec.gov/Archives/edgar/data/1040470/000165495424000372/aehr_ex991.htm), [FY24 guide (2023-07-13)](https://www.sec.gov/Archives/edgar/data/1040470/000165495423009130/aehr_ex991.htm).
- Company announcements: [$14M order (2026-02-26)](https://www.aehr.com/2026/02/aehr-receives-14-million-order-from-lead-ai-processor-customer-for-multiple-new-fully-automated-fox-xp-wafer-level-burn-in-systems/), [$41M order (2026-04-16)](https://www.aehr.com/2026/04/aehr-receives-record-41-million-production-order-from-lead-hyperscale-ai-customer-second-half-bookings-exceed-92-million/), [over $8M silicon carbide orders (2026-07-14)](https://www.aehr.com/2026/07/aehr-receives-more-than-8-million-in-new-silicon-carbide-wafer-level-burn-in-orders-as-global-electric-vehicle-programs-accelerate/), [$22M follow-on order (2026-08-12)](https://www.aehr.com/2026/08/aehr-receives-22-million-follow-on-order-for-ai-processor-wafer-level-burn-in-systems/), [about $6M Sonoma follow-on orders (2026-10-07)](https://www.aehr.com/2026/10/aehr-receives-follow-on-sonoma-production-orders-for-lead-hyperscale-customer-s-next-generation-ai-processor/), [silicon photonics follow-on order (2026-08-04)](https://www.aehr.com/2026/08/aehr-test-systems-expands-silicon-photonics-production-momentum-with-follow-on-production-order-from-lead-customer/).
- [Form 4 filing list (SEC)](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1040470&type=4): XML parsed line by line, including codes F, S, M, J, G and A; Scott's 04-09 sale follows the [4/A](https://www.sec.gov/Archives/edgar/data/1040470/000165495426003553/).
- 13G: [Jane Street (2026-07-29)](https://www.sec.gov/Archives/edgar/data/1040470/000159588826000075/xslSCHEDULE_13G_X02/primary_doc.xml), [FMR (2026-08-06)](https://www.sec.gov/Archives/edgar/data/1040470/000031506626001938/xslSCHEDULE_13G_X02/primary_doc.xml), [FMR (2026-05-06)](https://www.sec.gov/Archives/edgar/data/1040470/000031506626001114/xslSCHEDULE_13G_X02/primary_doc.xml), [AWM (2026-08-14)](https://www.sec.gov/Archives/edgar/data/1040470/000153526426000048/xslSCHEDULE_13G_X02/primary_doc.xml).

**Figures sourced to the call (third-party transcript, [StockAnalysis/Quartr](https://stockanalysis.com/stocks/aehr/transcripts/708298-q1-2027/), compared with the [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/11/03/aehr-test-systems-aehr-q1-2027-earnings-call-transcript/)):** contactors and related $13.5M/41%, prior year $2.6M/24%; consumables about 35% in FY2027 and about 30% long term; 5-10 systems and $35-70M per million units, $6-7M or more per system, 25 million units in 2027; more than 20 per month in Southeast Asia; FY2027 non-GAAP gross margin about 48.5%, plus or minus half a point; prior-year Q1 bookings $11.4M (also in the release); tax explanation; FY2026 silicon carbide spoken figures.

**Transcript traps:** Some summaries say management guided Q2 revenue below Q1. In the original, that CFO line is an answer about gross margin ("Q2 would probably be lower"). On revenue, the CEO says each remaining quarter grows a little, with Q4 highest. This report follows the original. Transcripts also render the CFO as Chris Hsu (the 8-K signature is Chris P. Siu), present 163% as GAAP growth (the release says non-GAAP), turn "150" into "51", and give non-GAAP opex growth as +36% (the release shows $7,801K against $5,949K, about +31%). The Motley Fool page says parts were created with large language models, and its summary section is not cited.

**Market data:** [Nasdaq historical prices](https://www.nasdaq.com/market-activity/stocks/aehr/historical), [Nasdaq short interest](https://www.nasdaq.com/market-activity/stocks/aehr/short-interest); peer market caps use 11-04 closes times SEC cover shares, and TTM is spliced from SEC XBRL data without adjusting for non-recurring items.

**Signal log:** No entry was added to `signals.json` this time, because no existing cross-check rule's predicate matches.

**Disclaimer:** Scenario values are arithmetic under conditional assumptions. They are not price targets and are not investment advice.
