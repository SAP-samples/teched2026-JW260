---
name: ariba-buying-requisition-item-review
description: Review authorized purchase requisition items from SAP Ariba Buying and create a five-slide PowerPoint
---

## Instructions

Use this skill only to create a read-only PowerPoint review of purchase requisition items that the signed-in user is authorized to view through SAP Ariba Buying. Do not create, change, submit, withdraw, approve, deny, or otherwise act on requisitions. Do not use SAP Ariba Sourcing.

1. Collect these required inputs before retrieval:
   - plant code or the explicit value `all authorized plants`;
   - fixed vendor code or the explicit value `all authorized vendors`;
   - delivery-date range with inclusive start and end dates in `YYYY-MM-DD` format;
   - report date in `YYYY-MM-DD` format.
2. Ask for every missing or ambiguous input. Do not infer dates, plant, or vendor.
3. Make exactly one request to the enabled SAP-published SAP Ariba Buying capability that finds or displays purchase requisition items. Retrieve at most 20 items the signed-in user is authorized to view. Request only fields the observed Buying result can provide:
   - purchase requisition number;
   - item number;
   - item description;
   - quantity and unit;
   - price, currency, and price basis;
   - purchasing group;
   - plant;
   - fixed vendor;
   - purchasing organization;
   - delivery date.
4. Apply plant, fixed-vendor, and delivery-date filters during retrieval when supported. Otherwise, apply them locally only if the Buying response is complete for the requested scope. If the response is partial, truncated, or an arbitrary page, stop instead of presenting it as a complete review.
5. On any retrieval error, including authorization, connection, timeout, unavailable fields, partial data, or truncation, do not retry, switch to SAP Ariba Sourcing, probe another service, or make an alternate request. Report the first error and stop.
6. Validate each returned item against the requested filters. Preserve requisition and item identifiers, leading zeros, codes, descriptions, quantities, units, prices, currencies, price bases, and dates exactly as returned. Do not invent unavailable fields or convert currencies. Omit an item that cannot be validated and disclose the omitted count in the chat response.
7. Sort validated items by delivery date ascending, then purchase requisition number ascending, then item number ascending. Keep at most 20 validated items.
8. Use the enabled `pptx` skill to create `requisition-item-review.pptx` with exactly five slides in this order:
   1. `Purchase Requisition Item Review` — title, applied delivery-date range, and report date.
   2. `Scope and Filters` — plant, fixed vendor, inclusive delivery-date range, analyzed-item count, omitted-invalid-item count, 20-item limit, and any supported retrieval limitation.
   3. `Item Summary` — analyzed-item count, total price grouped separately by currency, and counts grouped by plant and fixed vendor. Label price totals as sums of returned item prices; do not claim they are requisition totals.
   4. `Upcoming Requisition Items` — up to five items in the required sort order, showing requisition and item number, description, quantity and unit, price and currency, plant, fixed vendor, and delivery date.
   5. `Review Points` — concise factual observations supported by the returned items and items requiring human review. Do not make or imply an automated approval decision.
9. Keep slide content readable. Use no more than five principal bullets per slide; a compact table is allowed on slide 4. Do not add macros, external links, hidden slides, or unsupported branding claims.
10. Before returning the file, verify that it opens, has exactly five slides in the required order, includes every requested filter, preserves item-level identifiers and currencies, uses no more than five records on slide 4, follows the required sorting, and supports every review point with returned data.
11. Return the presentation and state the analyzed-item count, omitted-invalid-item count, whether the result is complete or bounded, and: `No SAP Ariba data was changed.` If SAP Ariba Buying, authorization, data handoff, required fields, or `pptx` is unavailable, explain exactly what is unavailable and do not claim that a presentation was created.