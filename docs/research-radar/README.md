# Research Radar — run receipts

Daily receipts from the `research-radar-weekday-scan` task. Every run commits one, including runs that find nothing.

These are **branch-only process artifacts**. They are not merged to `main`: the reviewer absorbs the data into `main` and discards the receipt with the branch. Nothing may be derived from a receipt, and a receipt must never contradict `reports.json`, `signals.json` or the report Markdown.

**Why older rows are not links.** A receipt lives only on its own dated branch. Once that branch has been reviewed and consumed, housekeeping deletes it and the receipt file goes with it — by design. Rows for consumed runs are kept below as a rolling record of what happened, without links, because the files they named no longer exist on any branch. To read an older receipt, open it on its branch *before* that branch is housekept.

| Date | Commit shape | Qualifying events | Proposals filed | Open items carried |
|---|---|---|---|---|
| 2026-08-18 *(branch consumed & deleted 2026-08-20)* | data commit | 1 — NVIDIA 8-K 2026-08-17: residual value guaranties on ~4.25 GW IT load at PORTS-Pike, payment obligation capped at US$105B, OpenAI affiliate as tenant | P-4 (chain-wide price-anchor staleness) | O-3, O-5, P-2, P-3, P-4, U-2 |
| 2026-08-19 *(branch consumed & deleted 2026-08-20)* | receipt only — no data updates | 0 | none new (P-4 figures corrected in receipt §4) | O-3, O-5, P-2, P-3, P-4, U-2 |
| 2026-08-20 *(branch consumed & deleted 2026-08-21)* | data commit | 2 — Nebius 6-K 2026-08-19: proposed US$4.50B convertible senior notes, proceeds naming data-center build-out and GPU procurement; Marvell 8-K 2026-08-18: warrant to Google over up to 58,970,907 shares at $206.58, vesting on discretionary Custom Products purchases | P-3 (re-raised — reviewer's named maturity condition fired), P-5 (new — `customer-warrant-linked-revenue`) | O-3, O-5, P-2, P-3, P-4, U-2, P-5 |
| [2026-08-21](2026-08-21.md) | data commit | 2 — Jinpan 2026 Semi-Annual Report 2026-08-21: data-center new orders RMB 3.869B (+336.25% YoY) and backlog RMB 5.092B, with operating cash flow turning negative to RMB -23.76M (-110.12% YoY); Nebius 6-K furnished 2026-08-20: convertible offering priced and upsized to US$5.0B (0.50% 2030 / 4.50% 2034), settlement expected 2026-08-24 | P-6 (new — `jinpan-2026:receivables-cash-quality` should read `breached`, stance-coupled and fail-closed), P-7 (new — `jinpan-2026` valuation denominator superseded by H1 actuals) | O-3, O-5, P-2, P-3, P-4, U-2, P-5, P-6, P-7 |

## Reviewer dispositions consumed by this task

The reviewer writes `YYYY-MM-DD-review.md` back onto the same dated branch. Housekeeping reads it before deleting the branch, and folds every still-live disposition into memory. Standing instructions adopted so far:

- **Contingent guarantees** (2026-08-19): state the condition, the cap, counterparty recourse, and the missing agreement text; never translate a cap into spend, revenue, backlog or capex.
- **Structural classification** (2026-08-19): buyer equity, neocloud backstop and developer/tenant credit support are three different structures and must not be forced into one cross-check rule.
- **Cross-contamination claims** (2026-08-20): open the cited primary filing and match filer name and CIK to the covered issuer before alleging that figures belong to another company.
- **Unpriced financings** (2026-08-20): treat a proposed, unpriced offering as `unclear` for funding durability until pricing, settlement or other binding primary evidence establishes actual capital access and cost.
