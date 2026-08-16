# Reddit, Inc. (RDDT) Deep Research Report

Coverage date: 2026-08-01
Last updated: 2026-08-01
Ticker: NYSE: RDDT
Disclaimer: This report is for informational and research purposes only. It does not constitute investment advice. Please conduct your own due diligence.

---

## 1. Executive Summary and Current View <!-- report-module:overview -->

**One-line thesis:** Reddit delivered a nearly flawless Q2 2026 on the financials, but the composition of that growth has changed — the primary source of revenue growth has shifted from user acquisition to per-user monetization, while the U.S. daily-active base that generates roughly 78% of revenue went flat-to-slightly-down. At the same time, a single Google contract bundles both licensing revenue and search distribution, and it expires in the first half of 2027. The market erased 21% of the company's value in one session after the print; what it repriced was not the quarter, but visibility into the top of the funnel.

**Investment judgment:**

- **Stance:** Neutral-to-constructive (on valuation) / low conviction (on visibility)
- **Confidence:** Low. The positive skew comes from valuation arithmetic, while the variable that decides the thesis — search referral traffic — is one management itself describes as having "low visibility." Any higher confidence would be false precision.
- **Key catalysts:** Q3 2026 results in late October 2026 (the first independent test of U.S. DAU and ad growth), the outcome of the Google data-licensing renewal (expires H1 2027), and any new AI licensing agreement
- **Monitoring window:** 3–12 months

**Key data (price anchor: 2026-07-31 close):**

| Metric | Value |
|--------|-------|
| Share price (2026-07-31 close, Friday) | $140.67 |
| Prior close (2026-07-30) | $178.04 |
| One-day decline on the print | -21.0% (largest single-day drop since IPO) |
| Market cap (192.40M shares outstanding) | ~$27.06B |
| Market cap (on ~203M TTM diluted shares) | ~$28.6B |
| Enterprise value | ~$24.30B |
| Cash and marketable securities (2026-06-30) | $2,786M |
| Total debt (2026-06-30) | $20.87M (negligible) |
| 52-week range | $119.27 - $282.95 |
| TTM P/E | 32.8x |
| Forward P/E (data-provider consensus) | 23.7x |
| P/S (TTM revenue $2,779M) | 9.7x |
| EV/Sales (TTM) | 8.7x |
| EV/EBITDA (TTM) | 30.3x |
| Beta (provider labels it 5Y; the company has traded only ~2.4 years, so it is computed on the available window) | 1.94 |
| Short interest as % of shares outstanding | 8.83% (16.99M shares; roughly 12.2% of the 139.6M float) |
| Q2 2026 revenue | $804.91M (+61% YoY) |
| Q2 2026 net income | $252.85M (31.4% net margin) |
| Q2 2026 diluted EPS | $1.25 (+178% YoY) |
| Q2 2026 adjusted EBITDA | $343M (43% margin, +106% YoY) |
| Q2 2026 free cash flow | $260.74M |
| TTM operating cash flow | $1,026M |
| Q2 2026 global DAUq | 130.3M (+18% YoY) |
| Q2 2026 U.S. DAUq | 53.2M (+6% YoY) |
| Q2 2026 international DAUq | 77.1M (+28% YoY) |
| Q2 2026 global ARPU | $6.18 (+36% YoY) |
| Q2 2026 U.S. ARPU | $11.85 (+51% YoY) |
| Q3 2026 revenue guidance | $860-870M (+47% to +49% YoY) |
| Q3 2026 adjusted EBITDA guidance | $385-395M (~45% margin) |

**The central tension of this print, stated as arithmetic:**

| Measure | Q1 2026 | Q2 2026 | Change |
|---------|---------|---------|--------|
| U.S. DAUq | 53.5M | 53.2M | **-0.3M (-0.6%)** |
| U.S. ARPU (quarterly) | $9.63 | $11.85 | **+23.1%** |
| U.S. revenue (derived = DAUq × ARPU) | ~$515M | ~$630M | **+22.3%** |
| International DAUq | 73.3M | 77.1M | +5.2% |
| International ARPU (quarterly) | $2.02 | $2.26 | +11.9% |
| International revenue (derived) | ~$148M | ~$174M | +17.7% |
| Derived total | ~$663M | ~$805M | — |
| Company-reported total revenue | $663.41M | $804.91M | — |

The derived totals reconcile to reported revenue within 0.05% (a $0.1M gap in Q1 and $0.3M in Q2), which confirms the decomposition above is internally consistent and auditable. **Conclusion: essentially all of the quarter's U.S. revenue growth came from per-user monetization, not from users.**

A caliber note on the U.S. DAU figure: the -0.6% sequential move sits on a metric rounded to 0.1M and spans the Q1→Q2 boundary, which is a genuine seasonal inflection in digital advertising (Q1 is the seasonal trough). **This report therefore reads it as "flat to slightly down," not as a structural break** — a directional signal that requires independent confirmation in Q3, not a conclusion on its own. The more robust series is the year-over-year one: U.S. DAU growth decelerated from +7% in Q1 to +6% in Q2, while U.S. ARPU rose 51% year over year.

**Three judgments at initiation:**

1. **The growth engine has switched tracks, but switching tracks is not the same as stalling.** The 51% YoY increase in U.S. ARPU has verifiable drivers: active advertisers up 70% YoY, automated-buying platform Reddit Max revenue up 150% sequentially, and dynamic product ads and app-install ads each more than doubling year over year. This is product and sales execution landing, not a one-time price increase.
2. **The largest single-point risk is not the "AI is taking our traffic" narrative — it is a specific contract expiry date.** The Google data-licensing agreement (roughly $60M/year, signed February 2024) expires in H1 2027, and renewal negotiations are reported to be ongoing and not straightforward.
3. **At the current price, the market's implied requirement for 2027 is not demanding.** As derived in §8: applying a mature ad-platform multiple of 6x EV/Sales, the current $24.30B enterprise value requires only about $4.05B of FY2027 revenue, implying roughly +22% growth from this report's FY2026E — a bar that sits below the midpoint of our base-case range.

## 2. Business Overview and Segment Economics <!-- report-module:business -->

Reddit was founded in 2005 and listed on the NYSE in March 2024 at $34 per share. It is a network of user-created, user-moderated interest communities (subreddits). Its core asset is twenty years of human-written discussion ranked by community voting — this is simultaneously its advertising inventory and the corpus it licenses to AI labs.

**Revenue is heavily concentrated in advertising:**

| Revenue line | Q2 2026 | Share | YoY | Notes |
|--------------|---------|-------|-----|-------|
| Advertising revenue | $762M | 94.7% | +64% | Driven by both impressions and pricing |
| Other revenue (mainly data licensing) | $43M | 5.3% | +24% | AI training-data licensing to Google, OpenAI and others |
| **Total** | **$804.91M** | 100% | **+61%** | — |

**This structure is itself an analytical starting point:** data licensing is only 5.3% of revenue, so AI licensing contributes very little to current earnings. Its real importance is **signal value and distribution coupling**, not revenue scale. Conversely, even a complete non-renewal of the Google agreement would hit revenue by only about $60M/year (roughly 2.2% of TTM revenue) — the genuine risk sits on the traffic side (see §7).

**Geographic segment economics (Q2 2026):**

| Region | DAUq | YoY | Quarterly ARPU | YoY | Derived quarterly revenue | Share |
|--------|------|-----|----------------|-----|---------------------------|-------|
| United States | 53.2M | +6% | $11.85 | +51% | ~$630M | ~78% |
| International | 77.1M | +28% | $2.26 | +31% | ~$174M | ~22% |
| Global | 130.3M | +18% | $6.18 | +36% | $804.91M | 100% |

**Structural implication:** U.S. users are 41% of global DAU but generate roughly 78% of revenue — U.S. ARPU is 5.2x the international level. This means the +28% international user growth carries very weak revenue leverage and cannot offset a flat U.S. base. It is precisely why the market gave no credit for the headline "+18% global DAU."

**User metrics and one disclosure change:**

| Measure | Q1 2026 | YoY | Notes |
|---------|---------|-----|-------|
| Global DAUq | 126.8M | +17% | — |
| of which: logged-in | 52.0M | +7% | High-engagement, monetizable core |
| of which: logged-out | 74.8M | +26% | Predominantly search-referred, weakly monetizable |
| Global WAUq | 493.1M | +23% | — |

Q2 2026 global WAUq reached 514.6M (+24% YoY), crossing 500 million for the first time.

**A point that must be recorded: the company will stop disclosing the logged-in / logged-out split beginning in Q3 2026**, retaining only U.S. and international daily and weekly actives. Management's stated rationale is that the change better reflects how the business is actually run. This report's observation: **logged-out users are the most direct carrier of search-referred traffic and the exact locus of the market's current concern; discontinuing that split removes the only public metric by which outside investors could gauge the extent of any search-referral damage.** This is a factual statement plus an observation about timing, not an allegation about management's motives — but it does raise the difficulty of verifying the thesis going forward, and §7 tracks it as a standalone uncertainty.

**Core business lines and product progress (Q2 2026, per management disclosure):**

1. **Advertising platform:** active advertisers +70% YoY; Reddit Max (automated buying) revenue +150% sequentially; dynamic product ads (DPA) and app-install ads each more than doubled year over year. Advertiser-count growth outpacing ARPU growth is the most verifiable support for the monetization ramp.
2. **Data licensing:** agreements with Google (roughly $60M/year, signed February 2024) and OpenAI. Management indicated future deal structures could introduce dynamic pricing, noting these agreements "aren't binary."
3. **Product and retention:** management stated that new app-user retention improved roughly 50% year over year (on a relative basis), and named converting web users into higher-engagement app users as a core priority, with a long-term goal of 1 billion global daily users.
4. **AI products:** on-platform AI answering features such as Reddit Answers. The strategic intent is to convert "users googling for Reddit content" into "users asking Reddit directly" — that is, to reclaim the top of the funnel from a third party.

## 3. Industry, Competition and Moat <!-- report-module:competition -->

Reddit competes in digital advertising, but its competitive position has one unusual feature: **its user acquisition depends heavily on a platform that is also its largest competitor (Google).** No other social advertising peer has this structure.

**Peer landscape (data as of 2026-07-31):**

| Company | Market cap | TTM revenue | Net margin | Position relative to Reddit |
|---------|-----------|-------------|------------|------------------------------|
| Meta | $1.42T | $228.25B | 29.84% | The default destination for ad budgets; owns its traffic loop, no search-referral dependency |
| Snap | $7.89B | $6.10B | -6.72% | Young user base, never reached scaled profitability — the counterexample that social advertising need not be profitable |
| Pinterest | $13.45B | $4.37B | 7.64% | High commercial intent, low engagement; the closest "second-tier ad platform" comparable |
| **Reddit** | **$27.06B** | **$2.78B** | **31.35%** | Smallest revenue base, but the highest growth rate and highest net margin of the four |

**A contrast worth noting:** Reddit's TTM revenue is only 64% of Pinterest's and 46% of Snap's, yet its market cap is 2.0x and 3.4x theirs respectively. What the market is paying for is 66.6% revenue growth and a 31.35% net margin — both first among the four. The premium has a fundamental basis, but it also means valuation support disappears quickly if growth converges toward Pinterest's level.

**Strong moat elements:**

1. **A corpus that cannot be replicated:** twenty years of human-written discussion ranked by community consensus. This is the "authentic human opinion" corpus that both search engines and AI labs need, and capital cannot recreate it quickly. It is the fundamental reason the AI licensing agreements exist at all.
2. **High-commercial-intent long-tail queries:** users searching Reddit for "which product is actually better" carry very high purchase intent, giving a theoretical ARPU ceiling well above generic social.
3. **An extraordinary gross-margin structure:** 91.44% TTM gross margin, with content produced free by users and moderated free by volunteers. This is why Reddit achieves a 31% net margin at just $2.78B of revenue, while Pinterest earns 7.64% on $4.37B.
4. **Community governance and the moderator system:** free content-moderation labor that also constitutes an operational barrier competitors find hard to replicate.

**Weak moat / structural fragility:**

1. **The top of the funnel is controlled by a third party.** A large share of logged-out users arrive via Google search. Google algorithm changes, or AI Overviews answering questions directly on the results page, alter Reddit's user inflow with no ability for Reddit to intervene. Management confirmed on the Q2 call that search referrals "were choppy in the quarter and traffic was more volatile later in the quarter," and that visibility "continues to remain low."
2. **A three-way conflict of interest.** Google is simultaneously Reddit's largest traffic source, the payer under its data-licensing agreement, and the party substituting AI Overviews for clicks. These three roles mean no negotiation is a purely commercial one.
3. **Single-channel monetization dependency:** 94.7% of revenue is advertising, which is sensitive to macro budget cycles.
4. **A monetization gap in the user base:** international users are 59% of DAU but contribute only 22% of revenue.

**Overall moat rating: moderate.** The content asset itself is a strong moat (near-impossible to replicate), but **the distribution channel is a weak moat** (subject to Google). Reddit's core strategy — converting users from "passers-by arriving via search" into "regulars who open the app" — is precisely an attempt to strengthen that weak link. Management's framing that they are "not building for drive-by traffic" but for "a daily destination" is a direct response to the problem; new app-user retention up 50% YoY is the strongest evidence yet for that path, but it remains a single quarter of a relative-basis figure.

## 4. Financial Health, Cash Flow and Red-Flag Check <!-- report-module:financial -->

Reddit completed a transition from persistent losses to high-quality profitability during 2025, and both the magnitude and the speed of that shift are unusual.

**Annual financial trajectory:**

| Metric | FY2022 | FY2023 | FY2024 | FY2025 | TTM (to 2026-06-30) |
|--------|--------|--------|--------|--------|---------------------|
| Revenue | $666.7M | $804.0M | $1,300M | $2,203M | $2,779M |
| Revenue YoY | +37.5% | +20.6% | +61.7% | +69.4% | +66.6% |
| Gross margin | 84.28% | 86.19% | 90.49% | 91.18% | 91.44% |
| Operating income | -$172.2M | -$140.2M | -$560.6M | +$442.0M | +$785M |
| Net income | -$158.6M | -$90.8M | -$484.3M | +$529.7M | +$871.1M |
| Diluted EPS | -$2.77 | -$1.54 | -$3.33 | +$2.62 | +$4.29 |

Note: the large FY2024 loss was driven mainly by stock-based compensation recognized at the IPO and does not reflect operating losses.

**Quarterly sequence (the key evidence on whether the "track switch" has damaged the growth rate):**

| Quarter | Revenue | QoQ | Net income | Diluted EPS | SBC | Free cash flow |
|---------|---------|-----|------------|-------------|-----|----------------|
| Q2 2025 | $499.63M | — | $89.30M | $0.45 | $89.07M | $110.83M |
| Q3 2025 | $584.91M | +17.1% | $162.66M | $0.80 | $83.52M | $183.10M |
| Q4 2025 | $725.61M | +24.1% | $251.60M | $1.24 | $85.18M | $263.64M |
| Q1 2026 | $663.41M | -8.6% | $203.98M | $1.01 | $68.34M | $311.16M |
| Q2 2026 | $804.91M | +21.3% | $252.85M | $1.25 | $100.95M | $260.74M |

The Q1 sequential decline is normal digital-advertising seasonality (Q4 is peak spending season) and is not a basis for trend judgment.

**Financial health matrix:**

| Metric | Current (Q2/TTM 2026) | Prior (FY2024) | Trend | Rating |
|--------|----------------------|----------------|-------|--------|
| Revenue growth | +61% (Q2 YoY) | +61.7% | Sustained at a high level | A |
| Gross margin | 91.44% (TTM) | 90.49% | Slowly rising | A |
| Operating margin | 28.8% (Q2) | -43.1% | Turned positive, expanding fast | A- |
| Adjusted EBITDA margin | 43% (Q2) | — | Expanding fast | A |
| Net margin | 31.4% (Q2) | -37.3% | Turned positive | A- (flattered by tax rate and interest income, see below) |
| Free cash flow | $1,018M (TTM) | Negative | Strong | A |
| Cash and marketable securities | $2,786M | $1,841M | Compounding | A |
| Total debt | $20.87M | $26.7M | Effectively unlevered | A |
| Shareholders' equity | $3,286M | $2,131M | Building | A |
| SBC as % of revenue | 12.5% (Q2) | — | Falling (guidance cut from high teens to low-to-mid teens) | B+ |
| User growth (U.S.) | +6% YoY, -0.6% QoQ | — | Flat to slightly down | C+ |

**One detail on capital efficiency:** Q2 capital expenditure was just $1.13M, and TTM capex is roughly $7.4M. Reddit sustains 66% revenue growth with essentially no asset intensity — free cash flow and operating cash flow are nearly identical (TTM OCF $1,026M vs FCF $1,018M). That is a sharp contrast with technology peers spending heavily on AI infrastructure over the same period.

**Red-flag check:**

| Check | Conclusion | Detail |
|-------|-----------|--------|
| Earnings quality | **Flag for labeling** | Q2 net income of $252.85M **exceeds** operating income of $231.72M. The gap comes from interest income on $2.8B of cash and a modest effective tax rate (the CFO described the effective rate as remaining modest). This means EPS growth will decelerate materially versus operating-income growth once the tax rate normalizes. This is not manipulation, but the TTM P/E of 32.8x must be adjusted for it in cross-company comparison |
| Stock-based compensation | Ordinary watch item | Q2 $100.95M, or 12.5% of revenue; TTM roughly $338M, or 12.2% of TTM revenue. Not a small absolute level, but full-year guidance was cut from "high teens" to "low-to-mid teens" — the direction is right |
| Leverage | No risk | Total debt $20.87M against $2.77B net cash |
| Cash flow vs earnings divergence | No anomaly | TTM OCF $1,026M vs net income $871M — cash flow exceeds earnings |
| Disclosure quality | **New watch item** | Logged-in / logged-out split discontinued beginning Q3 2026 (see §2) |
| Goodwill / M&A | No anomaly | No material acquisitions; management ranks "opportunistic M&A" second among capital-allocation priorities |
| Customer concentration | Ordinary watch item | Advertisers are diversified (active advertisers +70% YoY), but data-licensing revenue is highly concentrated in Google and OpenAI |

## 5. Management, Governance and Capital Allocation <!-- report-module:management -->

**Core team (as of the Q2 2026 earnings call):**

| Name | Role | Notes |
|------|------|-------|
| Steve Huffman | Co-founder and CEO | Co-founded Reddit in 2005; returned as CEO in 2015 |
| Jennifer Wong | Chief Operating Officer | Leads advertising commercialization |
| Andrew (Drew) Vollero | Chief Financial Officer | — |
| Jesse Rose | Head of Investor Relations | — |

**Execution track record:** within two years of the 2024 IPO, management moved the company from a FY2024 operating loss of $560.6M to TTM operating income of $785M, while growing revenue from $1.30B to $2.78B TTM. That is a strong record. Q2 also validated expense discipline: full-year SBC guidance was cut and operating margin expanded to 28.8%.

**Governance — the lowest-rated section of this report:**

Reddit uses a dual-class structure. Class A carries one vote per share; Class B carries ten votes per share and converts 1:1 into Class A.

| Governance item | Data | Source and date |
|-----------------|------|-----------------|
| Advance Magazine Publishers holding | 16,182 Class A shares + 42,191,092 Class B shares, roughly 22% of combined Class A and Class B outstanding | DEF 14A (filed 2026-04-23), holdings as of 2026-03-31 |
| Total voting power controlled by Huffman | Approximately 70.7% (including Class B conversion, equity awards, and the irrevocable proxy under the Advance voting agreement) | Same |
| Class B voting multiple | 10 votes per share | Same |

**Implication:** one individual controls roughly 70% of voting power, and public Class A holders have no practical influence on any matter requiring a shareholder vote. Advance Publications (parent of Condé Nast), the largest institutional holder, has assigned its voting power to Huffman under the voting agreement. **This means: hostile acquisition is impossible, there is no channel for activist pressure, and strategic course-correction depends entirely on management correcting itself.** For a company facing an external shock to its business model, this structure is simultaneously a stabilizer (it cannot be forced into bad decisions by short-horizon shareholders) and a risk (there is no external corrective mechanism if management misjudges).

**Capital allocation:** on the Q2 call, management gave three priorities — first, investing in the business; second, opportunistic M&A; third, share repurchases, while maintaining a high level of profitability.

| Buyback progress | Data |
|------------------|------|
| Total authorization | $1 billion (approved by the board 2026-02-04, announced 2026-02-05, no expiration) |
| Q1 2026 executed | 34,690 shares / $5.0M (roughly $995M remaining as of 2026-03-31) |
| Q2 2026 executed | Approximately 1.5 million shares / roughly $235M, average price $157.57 |
| Remaining authorization | Approximately $760M |

**A neutral observation on the repurchase price:** against this report's frozen July 31, 2026 valuation anchor of $140.67, the Q2 average repurchase price of $157.57 was about 12% higher. This is an explicitly dated historical comparison that does not update with later market prices, so subsequent trading cannot support describing the repurchase as “currently underwater” or “currently profitable.” It neither proves management misjudged (the buying occurred before the print, at a normal pace) nor should it be read as a confirming “management is confident” signal. What is genuinely worth watching is Q3: after the 21% post-print one-day decline, the pace at which the remaining $760M authorization is deployed will be management's real statement about its own valuation view.

**Management rating: B+.** A combination of operational execution (A) and governance structure (C). The execution record is solid, cost discipline is verifiable, and the capital-allocation framework is clear; the deductions come entirely from the accountability gap under dual-class control and from the disclosure narrowing recorded in §2.

## 6. Bull and Bear Cases <!-- report-module:bullBear -->

### 6.1 Bull Case

**Core argument:** the market has wrongly equated "user growth is slowing" with "the business is deteriorating." Reddit's monetization penetration is still early, ARPU expansion has clear product drivers and verifiable intermediate indicators, and the current price already discounts a growth slowdown.

**Supporting evidence:**

1. **The ARPU ramp has product support and is not a one-time price hike.** U.S. ARPU rose 51% YoY while active advertisers rose 70% YoY, Reddit Max revenue rose 150% sequentially, and dynamic product ads and app-install ads each more than doubled. Advertiser count growing faster than ARPU indicates pricing is coming from demand-side competition in the auction, not unilateral increases.
2. **Margins are still expanding rapidly.** Q2 adjusted EBITDA margin was 43% (+106% YoY), with Q3 guided to roughly 45%. Margins expanding while revenue grows 61% YoY indicates operating leverage is not yet exhausted.
3. **An exceptionally clean balance sheet.** Net cash of $2.77B ($14.37 per share, or 10.2% of the share price), essentially no debt, TTM free cash flow of $1,018M, and near-zero capex. The company can keep investing in product and repurchasing stock through a traffic headwind.
4. **International monetization has not started.** International DAU is 77.1M (+28% YoY) at an ARPU just 1/5.2 of the U.S. level. Even closing to one-third of U.S. ARPU (from $2.26 to roughly $3.95) on the current user base would imply roughly $130M of incremental quarterly revenue (77.1M × $1.69). This engine has not been switched on.
5. **AI licensing is an unpriced option.** It contributes just 5.3% of revenue today. If renewals land with the dynamic-pricing structure management has hinted at (Reddit earning more as its data becomes more valuable to AI-generated answers), the shape of this revenue line changes from a fixed annual fee to a take rate on AI usage. The market prices essentially none of this today.
6. **There is already evidence of the funnel being reclaimed.** New app-user retention improved roughly 50% YoY (relative basis), and WAUq crossed 500 million. If app conversion persists, the structural importance of search referrals declines.

**Key assumptions:** U.S. DAU stays flat rather than entering sustained decline; advertiser-count growth continues; and even absent a Google renewal, the traffic impact is gradual rather than a cliff.

**Valuation implication of the bull scenario:** if FY2027 revenue growth holds at 30%-35% with adjusted EBITDA margins of 46%-48%, then on a mature-platform 6x EV/Sales frame the current $24.30B enterprise value sits well below the scenario's fair range (derivation in §8). In that scenario the current price is cheap.

### 6.2 Bear Case

**Core argument:** Reddit's user growth depends on a channel it does not control and which is actively eroding it. The current high growth is a one-time catch-up in monetization rate; once that is spent, an advertising platform with no user growth is not worth 9.7x sales.

**Supporting evidence:**

1. **The most valuable user cohort has stopped growing.** U.S. DAU growth decelerated from +7% in Q1 to +6% in Q2, with the sequential figure moving 53.5M → 53.2M. U.S. users generate roughly 78% of revenue; once that leg goes from slow growth to zero growth, the entire growth burden shifts to ARPU.
2. **ARPU has a ceiling, and it is closer to its limit than user growth is.** Monetization-rate gains are a converging process: ad load, price per impression, and advertiser penetration all have physical limits. U.S. ARPU has already risen 51% in a year; a second increase of the same magnitude is mathematically harder. When ARPU growth decays while user count is flat, revenue growth loses both of its sources at once.
3. **The Google agreement creates a dual dependency with a hard expiry.** The roughly $60M/year agreement expires in H1 2027, renewal talks are reported to be ongoing, and Reddit is reported to be considering restricting Google's structured AI data access. **Fact must be separated from inference here:** the facts are the contract value, the February 2024 signing, the expiry, and that negotiations are underway. **The inference — this report's judgment, not company disclosure — is that the licensing relationship and search distribution may be coupled, i.e. that Reddit content's prominence in Google search and AI Overviews may derive in part from that contractual arrangement. If the inference holds, a non-renewal would hit licensing revenue and referral traffic simultaneously; if it does not, the damage is limited to roughly $60M/year (about 2.2% of TTM revenue).** Whether this inference is true is the single most important open question in this report.
4. **Structural substitution by AI Overviews.** Google's AI summaries answer questions directly on the results page, reducing the need to click through to Reddit. This is not a negotiable commercial term but the direction of search product evolution — the trend does not reverse even if the contract renews.
5. **Management itself says it cannot see.** Huffman's words on the call were that search referrals "were choppy in the quarter and traffic was more volatile later in the quarter," and that "visibility on search continues to remain low, and we expect it to probably continue to be volatile." When management cannot offer visibility on the most important forward variable, any extrapolation-based valuation deserves a discount.
6. **Net margin is flattered by non-operating factors.** Q2 net income exceeded operating income, with the gap coming from interest income and a modest effective tax rate. Once taxes normalize, the same operating income produces lower EPS, and the apparent "cheapness" of a 32.8x TTM P/E degrades.
7. **The verification metric is about to disappear.** Beginning in Q3 2026, the logged-in / logged-out split is discontinued, removing the only public metric by which outside investors could directly measure search-referral damage (see §2).

**Valuation implication of the bear scenario:** if the Google agreement is not renewed and logged-out traffic decline transmits into U.S. DAU and ad inventory, FY2027 revenue growth falls to 8%-15% with adjusted EBITDA margins of 38%-42%, and the market would most likely compress the multiple toward the Pinterest-to-Snap band (3x-4.5x EV/Sales). In that scenario the current 8.7x EV/Sales is clearly expensive.

## 7. Key Uncertainties and Thesis-Breaking Conditions <!-- report-module:uncertainties -->

**What we do not know:**

| Uncertainty | Current state | When it can be confirmed |
|-------------|---------------|--------------------------|
| **The true extent of search-referral damage** | Management calls visibility "low" and traffic "choppy"; no quantification | Q3 2026 results (late October 2026): U.S. DAU and ad growth. Note the logged-in/logged-out split ends at the same time, raising verification difficulty |
| **Whether licensing and distribution are coupled** (the inference in §6.2, point 3) | No public contract terms exist to confirm or falsify it | When the Google renewal outcome is announced (before H1 2027), or if related language appears in Reddit's 10-K risk factors |
| **Whether U.S. DAU is flat or beginning to decline** | A single quarter at -0.6% QoQ, inside rounding and seasonal noise | Requires two consecutive quarters (Q3 and Q4 2026) to establish direction |
| **How much ARPU headroom remains** | U.S. quarterly ARPU $11.85, +51% YoY; no public ceiling reference | Watch the second derivative of U.S. ARPU YoY growth: two consecutive quarters of deceleration signals convergence |
| **Timing and magnitude of tax-rate normalization** | CFO says only that the rate "remains modest," with no normalization path given | 10-K deferred-tax and valuation-allowance disclosure, or a quarter in which the rate jumps |
| **Whether international monetization can start** | International ARPU $2.26, just 1/5.2 of the U.S. level | Watch whether international ARPU YoY growth stays above 30% |

**Thesis-breaking conditions:**

- **Bull case breaks:** U.S. DAU declines sequentially for two consecutive quarters; or U.S. ARPU YoY growth falls below +25% (signaling the monetization dividend is converging); or Q4 2026 revenue guidance implies less than +35% YoY.
- **Bear case breaks:** the Google agreement renews on flat or better terms and U.S. DAU returns to sequential growth in Q3 and Q4; or a new AI licensing agreement of comparable scale is signed, proving the data asset has competing buyers.
- **Whole framework breaks (report requires a rewrite):** the Google agreement is confirmed not to renew and the company simultaneously discloses a sharp decline in search referrals; or the company narrows user-metric disclosure further such that external verification becomes impossible; or a major content-regulation event (such as a change to platform liability law) alters the business model's foundation.

## 8. Valuation and Expectations Gap <!-- report-module:valuation -->

**Current anchor (2026-07-31 close):** share price $140.67 on 192.40M shares outstanding gives a market cap of roughly $27.06B; net of $2.77B of net cash, enterprise value is roughly $24.30B. On TTM diluted shares (approximately 203M, derived from TTM net income of $871.1M ÷ diluted EPS of $4.29), the diluted market cap is roughly $28.6B. Unless noted otherwise, multiples below use $27.06B market cap and $24.30B EV.

**Multi-method valuation:**

| Method | Value / range | Key assumptions | Confidence |
|--------|---------------|-----------------|------------|
| TTM P/E | 32.8x | TTM EPS $4.29; **includes interest income and low-tax-rate benefit — must be adjusted for cross-company comparison** | Medium |
| Forward P/E (data-provider consensus) | 23.7x | Third-party basis implying EPS of roughly $5.94, most likely NTM (next twelve months) rather than FY2026; the gap versus the next row's derivation reflects differing bases and assumptions, not a contradiction | Medium |
| Forward P/E (this report's derivation) | ~26.5x | FY2026E EPS of roughly $5.30. Derivation: H1 actual $2.26 + Q3 ~$1.41 (guided EBITDA midpoint $390M × Q2's actual 73.8% net-income conversion) + Q4 ~$1.63 (**this report's assumption**: Q4 adjusted EBITDA of roughly $450M) | Medium-low |
| P/S (TTM) | 9.7x | TTM revenue $2,779M | High (no assumptions) |
| EV/Sales (TTM) | 8.7x | Same | High (no assumptions) |
| EV/Sales (FY2026E) | ~7.3x | FY2026E revenue of roughly $3,308M (H1 actual $1,468M + Q3 guidance midpoint $865M + **this report's assumption** of roughly $975M in Q4, implying +12.7% QoQ versus the +24.1% seasonal step in Q4 2025) | Medium |
| EV/EBITDA (TTM) | 30.3x | **Data-provider basis with a GAAP-EBITDA denominator (~$0.80B, roughly operating income of $785M plus D&A); the next row uses an adjusted-EBITDA denominator, so the two rows are not directly comparable** | High (no assumptions) |
| EV/EBITDA (FY2026E, adjusted basis) | ~16.8x | FY2026E adjusted EBITDA of roughly $1,449M (H1 actual $609M + Q3 guidance midpoint $390M + **this report's assumption** of roughly $450M in Q4); the adjusted basis excludes SBC and similar items, so its denominator is inherently larger than the GAAP basis in the row above | Medium |
| Net cash support | $14.37 per share | 10.2% of the July 31, 2026 valuation anchor of $140.67, providing a hard floor for that historical valuation snapshot | High |
| Sell-side target range (**market-sentiment reference only, not this report's conclusion**) | $170 / $200 / $200 / $221 | Cantor / Deutsche Bank / Oppenheimer / Wedbush, post-print reductions | — |

**Peer multiple comparison (2026-07-31):**

| Metric | Reddit | Pinterest | Snap | Meta |
|--------|--------|-----------|------|------|
| Market cap | $27.06B | $13.45B | $7.89B | $1.42T |
| TTM revenue | $2.78B | $4.37B | $6.10B | $228.25B |
| TTM revenue growth | +66.6% | — | — | — |
| Net margin | 31.35% | 7.64% | -6.72% | 29.84% |
| TTM P/E | 32.8x | 48.5x | n/a (loss-making) | 21.0x |
| Forward P/E | 23.7x | 12.7x | 7.3x | 17.3x |
| P/S | 9.7x | 3.1x | 1.3x | 6.2x |
| EV/Sales | 8.7x | 3.1x | 1.5x | 6.3x |
| EV/EBITDA | 30.3x | 44.1x | n/a | 13.1x |

**Scenario grid:**

| Scenario | Driver assumptions (FY2027 revenue growth / adjusted EBITDA margin / multiple range) | Valuation implication (vs 2026-07-31 close of $140.67) | Probability weight |
|----------|--------------------------------------------------------------------------------------|--------------------------------------------------------|--------------------|
| Bull scenario | Revenue +30% to +35%; margin 46%-48%; EV/Sales 7x-9x. Requires: search referrals stabilize + at least one new or improved AI licensing agreement + international monetization begins | **Cheap** — FY2027 revenue of roughly $4.30B-$4.47B at 7x-9x implies EV of $30B-$40B, well above the current $24.30B | 30% |
| Base scenario | Revenue +22% to +28%; margin 44%-46%; EV/Sales 5.5x-7x. Requires: U.S. DAU flat, ARPU growth converging down from +51%, Google agreement renewed on neutral terms | **Fair** — FY2027 revenue of roughly $4.04B-$4.23B at 5.5x-7x implies EV of $22B-$30B; the current $24.30B sits in the lower part of that range | 50% |
| Bear scenario | Revenue +8% to +15%; margin 38%-42%; EV/Sales 3x-4.5x. Requires: Google agreement not renewed and referral decline transmits into U.S. DAU and ad inventory | **Expensive** — FY2027 revenue of roughly $3.57B-$3.80B at 3x-4.5x implies EV of $11B-$17B, well below the current $24.30B | 20% |

(All three scenarios derive FY2027 revenue from this report's FY2026E of roughly $3,308M; the composition and assumptions behind FY2026E are itemized in the valuation table above.)

**What is priced in, and the expectations gap:**

An auditable reverse-derivation anchors the market's current requirement. Meta, as a mature high-margin advertising platform, trades at 6.3x EV/Sales. Assuming Reddit eventually converges to a **6x EV/Sales** mature-platform valuation, supporting the current $24.30B enterprise value requires revenue of **$4.05B**. Against this report's FY2026E of $3,308M, that implies **FY2027 revenue growth of only about +22%**.

**The expectations gap:** at $140.67 the market implicitly requires roughly 22% FY2027 revenue growth (under a mature-platform multiple assumption). This report's base case is **+22% to +28%** — **landing right at or above that bar**. Put differently, the current price pays for nothing beyond the base case: international monetization, dynamic pricing on AI licensing, and further operating-leverage release are all free options, while downside protection comes from $14.37 per share of net cash (10.2% of the price) and essentially zero debt.

The fragility of this derivation must be stated alongside it: it assumes Reddit can sustain mature-platform margins and ultimately earn a 6x multiple. The bear scenario denies exactly that assumption — if revenue growth falls below 15%, the market will not pay 6x but the 3x-4.5x that sits between Pinterest and Snap. **The positive skew in this report therefore does not come from "growth will be good"; it comes from "the current price already discounts a growth slowdown, but does not discount a collapse."**

## 9. Catalysts and Monitoring Checklist <!-- report-module:catalysts -->

| Catalyst | Timing | Impact |
|----------|--------|--------|
| **Q3 2026 results** | Late October 2026 (estimated) | **The single most important event this year.** Tests: whether U.S. DAU returns to sequential growth, whether U.S. ARPU YoY growth holds, delivery against the $860-870M revenue guide, and the Q4 guide |
| Google data-licensing renewal | Before H1 2027 (contract expiry); announcement timing uncertain | Dual impact (revenue plus the distribution inference, see §6.2). Any leaked terms or company confirmation would reprice the stock materially |
| A new AI licensing agreement | Event-driven, no fixed date | The strongest single catalyst for the bull case: it would simultaneously prove competing demand for the data asset and the viability of a dynamic-pricing structure |
| Pace of the remaining $760M buyback authorization | Ongoing; disclosed with Q3 results | Repurchase intensity after a 21% decline is management's real statement on its own valuation view |
| Discontinuation of the logged-in / logged-out split | Effective from Q3 2026 | Already confirmed; the effect is reduced external verifiability and a longer time to thesis confirmation |
| Q4 2026 results and FY2027 guidance | February 2027 (estimated) | The first FY2027 framework, testing the base-case assumptions in the §8 scenario grid directly |
| Third-party traffic monitoring data | Ongoing (monthly) | Independent readings on Reddit's search referrals from services such as Similarweb — the only high-frequency verification source between prints |
| Effective tax-rate normalization | Timing unknown | A one-time depression of EPS growth that could trigger an earnings-quality re-rating |

**Key monitoring metrics (in priority order):**

1. **Sequential direction of U.S. DAUq** — the single most important metric. Two consecutive quarters of sequential decline breaks the bull case.
2. **U.S. quarterly ARPU YoY growth** — the rate of convergence down from +51%. Falling below +25% signals the monetization dividend has peaked.
3. **Advertising revenue YoY growth** — Q3 guidance implies +47% to +49% total revenue growth; watch whether ad growth keeps pace.
4. **Active advertiser count growth** — currently +70% YoY, a leading indicator for ARPU sustainability.
5. **Other revenue (data licensing), YoY and absolute** — currently $43M per quarter. Renewal outcomes will show up in this line first.
6. **Adjusted EBITDA margin** — Q3 guided to roughly 45%. If margins retreat while revenue decelerates, operating leverage has topped out.
7. **Buyback execution** — the quarterly burn rate against the remaining $760M authorization.

## 10. Conclusion <!-- report-module:conclusion -->

**The question this report answers:** when AI answer engines begin substituting for search clicks, is the business model of a content platform that acquires users through search referrals, monetizes through advertising, and licenses its corpus to AI labs being eroded or re-rated? Reddit is the purest available sample for this question — it is simultaneously a victim of AI (traffic) and a beneficiary of it (licensing).

**The expectations gap in one sentence:** at $140.67 the market implicitly requires roughly 22% FY2027 revenue growth (on a mature-platform 6x EV/Sales basis); this report's base case is +22% to +28%, landing right at or above that bar — the current price pays for a growth slowdown, but not for a collapse, and not for the international-monetization and AI-licensing-dynamic-pricing options.

**Stance and conviction: neutral-to-constructive, low conviction.** Scenario weights of 30/50/20 — bull (cheap) 30%, base (fair) 50%, bear (expensive) 20% — produce a positive weighted skew. Conviction is set at low because the variable that determines that skew, search referral traffic, is the one management itself describes as having "low visibility" with continued volatility expected, and because the most direct public metric for verifying it (the logged-in / logged-out split) is discontinued starting next quarter. **The positive skew comes from valuation arithmetic, not from high confidence in the fundamentals; the two should not be conflated.**

One point should be stated plainly: this report does not view the post-print -21% as a mispricing. Q2 did expose a real structural change — the growth engine switched from users to monetization, and monetization has a ceiling. Repricing for that is rational. This report's judgment is narrower: after the repricing, the price is not expensive for the base case.

**Upgrade triggers (toward a more constructive stance):**
- U.S. DAUq returns to sequential growth for two consecutive quarters in Q3 and Q4 2026; or
- the Google agreement renews on flat or better terms; or
- a new AI licensing agreement of comparable scale is signed.

**Downgrade triggers (toward caution or avoidance):**
- U.S. DAUq declines sequentially for two consecutive quarters; or
- U.S. ARPU YoY growth falls below +25%; or
- Q4 2026 revenue guidance implies less than +35% YoY growth; or
- the Google agreement is confirmed not to renew and the company simultaneously discloses a sharp decline in search referrals.

This is a monitoring perspective, not an allocation recommendation: a beta of 1.94, short interest at 8.83% of shares outstanding, and a 52-week range of $119.27-$282.95 (the high is 2.4x the low) describe an extremely volatile stock, and the next meaningful verification point (Q3 results) is roughly three months away. Any position should sit within a risk budget appropriate to a high-volatility asset, and the Q3 U.S. DAU reading should be treated as a more important signal than the price action.

## 11. Appendix: Assumptions and Sources <!-- report-module:appendix -->

**Key assumptions used in this report (and the boundary with disclosed fact):**

| Item | Nature | Notes |
|------|--------|-------|
| Q4 2026 revenue of roughly $975M | **This report's assumption** | Implies +12.7% QoQ, below the +24.1% seasonal step in Q4 2025 — a conservative setting |
| Q4 2026 adjusted EBITDA of roughly $450M | **This report's assumption** | Implies a margin of roughly 46%, slightly above the roughly 45% guided for Q3 |
| Q3 net-income conversion of 73.8% | **This report's assumption** | Taken from Q2 actuals (net income $253M ÷ adjusted EBITDA $343M) |
| Mature-platform 6x EV/Sales | **This report's assumption** | Referenced to Meta's current 6.3x; used for the implied-growth derivation in §8 |
| U.S. / international revenue split | **This report's derivation** | = DAUq × ARPU, both company-disclosed; derived total reconciles to reported revenue within 0.05% |
| Coupling between the licensing agreement and search distribution | **This report's inference** | No public contract terms support it; an open question, explicitly labeled in §6.2 and §7 |
| Google agreement at roughly $60M/year, expiring H1 2027 | Media reporting | Not company-disclosed; sources below |
| All other financial and operating figures | Company disclosure | Earnings releases, earnings call, SEC filings |

**Peer comparison table (repeated for auditability, data as of 2026-07-31):**

| Metric | Reddit | Pinterest | Snap | Meta |
|--------|--------|-----------|------|------|
| Market cap | $27.06B | $13.45B | $7.89B | $1.42T |
| Enterprise value | $24.30B | — | $9.27B | — |
| TTM revenue | $2.78B | $4.37B | $6.10B | $228.25B |
| Net margin | 31.35% | 7.64% | -6.72% | 29.84% |
| P/S | 9.7x | 3.1x | 1.3x | 6.2x |
| EV/Sales | 8.7x | 3.1x | 1.5x | 6.3x |
| Forward P/E | 23.7x | 12.7x | 7.3x | 17.3x |

**Sources:**

- Reddit Q2 2026 earnings release and financial statements (published after market close on 2026-07-30): revenue split, net income, EPS, adjusted EBITDA, DAUq/WAUq, ARPU, cash balances, Q3 guidance.
- Reddit Q2 2026 earnings call (2026-07-30): Huffman's remarks that search referrals were "choppy" and that visibility "continues to remain low"; buyback execution detail (approximately 1.5 million shares / roughly $235M / average price $157.57 / roughly $760M remaining); the three capital-allocation priorities; the SBC guidance reduction; active advertisers +70%; Reddit Max revenue +150% sequentially; new app-user retention +50% YoY; discontinuation of the logged-in/logged-out split from Q3; and the CFO's comment that the effective tax rate "remains modest."
- Reddit Q1 2026 earnings release (published 2026-04-30): Q1 revenue $663.41M, advertising revenue $625M, net income $203.98M, adjusted EBITDA $265.97M, DAUq 126.8M (logged-in 52.0M / logged-out 74.8M), WAUq 493.1M, ARPU (global $5.23 / U.S. $9.63 / international $2.02).
- Reddit Form 8-K (2026-02-05, document `rddt-20260205.htm`): the $1 billion Class A repurchase authorization approved by the board on 2026-02-04.
- Reddit Form 10-Q (period ended 2026-03-31, document `rddt-20260331.htm`): Q1 repurchases of 34,690 shares / $5.0M, with $995.0M remaining.
- Reddit Form DEF 14A (filed 2026-04-23, document `rddt-20260423.htm`): Advance Magazine Publishers' holdings (16,182 Class A + 42,191,092 Class B, roughly 22% of combined Class A and B, as of 2026-03-31); Huffman's approximately 70.7% of total voting power; the dual-class structure and the Advance voting agreement.
- Annual and quarterly financial series (FY2022-FY2025, TTM, and the last five quarters of revenue / earnings / SBC / cash flow / balance sheet): stockanalysis.com Reddit financial statement pages (`stockanalysis.com/stocks/rddt/`), retrieved 2026-07-31.
- Market data (share price $140.67, prior close $178.04, market cap, enterprise value, 192.40M shares outstanding, 52-week range, multiples, beta, short interest, net cash per share, free cash flow per share): stockanalysis.com, 2026-07-31 close.
- Peer multiples (Meta, Pinterest, Snap): stockanalysis.com company statistics pages, 2026-07-31.
- The Google data-licensing agreement (roughly $60M/year, signed February 2024, expiring H1 2027, renewal talks ongoing, Reddit reported to be weighing tighter structured AI data access): multiple financial media reports (Bloomberg, 2025-09-17, on Reddit seeking its next AI content pact, and follow-up reporting in July 2026 on the renewal negotiations). **Media reporting, not company disclosure.**
- Post-print sell-side target changes (Cantor $170, Deutsche Bank $200, Oppenheimer $200, Wedbush $221): TipRanks and Benzinga compilations, 2026-07-31. **Market-sentiment reference only.**

**Caliber notes and limitations:**

1. This report's price anchor is the **2026-07-31 (Friday) closing price of $140.67**, a completed-session close rather than an intraday snapshot. The publication date of 2026-08-01 is a Saturday, with no new trading data.
2. This report was unable to read the Q2 2026 SEC Form 10-Q directly (the SEC website returned access restrictions during this work), so the Q2 operating-expense detail (research and development, sales and marketing, and general and administrative line items) is missing. The financial analysis is therefore based on aggregate revenue, gross profit, operating income, net income, cash flow, and balance-sheet measures. This is a known data gap in this report.
3. Two market-cap conventions exist: $27.06B on 192.40M shares outstanding, and roughly $28.6B on approximately 203M TTM diluted shares. All multiples in this report use the former; readers comparing against third-party diluted-basis data should note the difference.
4. This is an initial coverage report; no prior-cycle version exists for comparison.
