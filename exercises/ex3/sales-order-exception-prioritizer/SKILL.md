---
name: sales-order-exception-prioritizer
description: Rank sales-order exceptions from supplied CSV or qualified live data using deterministic risk rules
---

## Instructions

Use this skill to prioritize sales-order exceptions. The core workshop path is a participant-supplied synthetic CSV. Live retrieval is optional and requires facilitator-confirmed tenant support.

### Choose the input path

1. Use the explicitly supplied analysis date in `YYYY-MM-DD` format; ask if it is absent or invalid. Never substitute the system date. The date anchors scoring and the live retrieval window, not a historical snapshot. Live statuses are current at retrieval time.
2. Branch before any retrieval:
   - **Supplied CSV or compatible table:** use that data only. Do not contact a backend, count live orders, or apply live status/date filters. Score all supplied rows, including completed and out-of-window boundary examples. The workshop CSV is supplied separately by the participant, not bundled inside this skill. If the request refers to an attachment that is missing, ask the participant to attach it and stop; do not search for a packaged sample or silently switch to live data.
   - **Explicit live request without supplied data:** follow the qualified, bounded procedure below. If the input choice is unclear, ask whether the participant wants to supply a CSV or use the qualified live path.
3. Before attempting either execution path, confirm that the sandbox can run the bundled Python script. If execution is unavailable, stop and explain that no scoring script was run. Offer a **reference-only walkthrough** of the rules below and the participant guide's expected fixture results, clearly labeled as reference rather than computed output. Do not fabricate execution results, counts, a download, or an output file. Ask the facilitator for a supported runtime to complete an executed run.

### Optional live retrieval

4. Proceed only with a facilitator-confirmed SAP-published capability whose authorization, usable fields, status meanings, server-side count/filter/sort/limit support, and data handoff are qualified in this tenant. The custom skill cannot connect directly to SAP S/4HANA because its sandbox has no external network connectivity. If qualification is missing, ask the facilitator for the missing information or ask the participant to supply a CSV, then stop. Do not invent a capability, field, or filter mapping.
5. Qualify live delivery-status meanings for the **exact field and current tenant** before filtering. Normalize them to `Open`, `Partially Delivered`, or `Complete` only from verified field/code-list meanings. Never infer a raw SAP status mapping, borrow meanings from a similarly named or legacy field, or treat an unrecognized status as incomplete. If a status is blank, ambiguous, unsupported, or cannot be mapped, stop and ask for a qualified mapping or corrected CSV. Do not silently omit the incomplete-delivery filter.
6. Define the live scope as authorized orders with incomplete delivery and a requested delivery date from 30 days before through 7 days after the analysis date, inclusive. For `2026-10-07`, this is `2026-09-07` through `2026-10-14`. Count matching orders once using the qualified SAP-published capability. State the matching count briefly. If more than 50 match, state that only 50 will be analyzed, without asking for confirmation. If zero match, skip detail retrieval and use an empty table with the required headers for processing.
7. For a nonzero count, make at most one bounded detail retrieval for at most 50 matching orders. In SAP S/4HANA, apply the scope and sort by `requested_delivery_date` descending, then `sales_order` ascending, **before** limiting. Retrieve `sales_order`, `customer`, `net_value`, `currency`, `requested_delivery_date`, `overall_delivery_status`, an explicit delivery-block indicator or reason, `TotalCreditCheckStatus`, its exact tenant code-list text or description, and `TotalBlockStatus`. Code-list lookups may supply the required status meanings, but never retrieve more order pages. On any retrieval error, including authorization, connection, timeout, partial, or truncated data, report the first error and stop. Do not retry or probe alternate services. If the capability cannot count, filter, sort, and limit before retrieval, stop and ask for a CSV rather than scoring an arbitrary first page.
8. Never infer credit blockage from a raw `TotalCreditCheckStatus` code alone. Do not use general SAP knowledge, a different field such as legacy `CMGST`, or the fact that a value is nonempty to interpret the code. Retrieve the code-list text for the exact `TotalCreditCheckStatus` object-node value in the current tenant. Map `credit_block` to `true` only when that text unambiguously means blocked, not approved, or document not OK. Map it to `false` only when the text unambiguously means approved, released, not relevant, or document OK. Treat every other value or unavailable meaning as `unknown`; do not ask the user to choose a meaning.
9. Use `TotalBlockStatus` only as a consistency check because it can include delivery, billing, and credit blocks. An empty overall block status can support a `credit_block = false` interpretation but cannot identify which component is blocked when nonempty. If code-list text and overall block status conflict, keep `credit_block = unknown` and report the conflict. Preserve the raw credit code and text in the output. Unknown credit status earns no credit-block points; other verified conditions still score, and unresolved rows are reported separately. Do not turn an explicit retrieval error into an unknown value to bypass the stop condition.

### Validate and score either input path

10. Require these eight columns: `sales_order`, `customer`, `net_value`, `currency`, `requested_delivery_date`, `overall_delivery_status`, `delivery_block`, `credit_block`. Ask for missing columns or values instead of guessing mappings. Delivery status accepts only `Open`, `Partially Delivered`, and `Complete`, ignoring case and surrounding whitespace. Reject every other value, including raw SAP codes. For supplied CSV credit blocks, use supported boolean representations directly, or `unknown`/`unresolved` for an explicitly unresolved mapping. Normalize explicit block indicators from `true`, `false`, `yes`, `no`, `1`, or `0` case-insensitively; for a qualified live delivery-block reason, map a nonempty reason to `true` and an empty reason to `false`.
11. Apply these deterministic workshop rules using `scripts/prioritize_orders.py`:
    - Verified credit block: +50.
    - Delivery block: +40.
    - Incomplete delivery with requested date before the analysis date: +30.
    - Otherwise, incomplete delivery with requested date from the analysis date through 7 days later, inclusive: +20.
    - Raw net value at least 50000 in the record's own currency: +10.
    - `Complete` earns neither date rule, but can still earn block and value points. Unknown credit status earns no credit-block points.
    - Priority: Critical ≥70; High 40–69; Medium 20–39; Low 0–19.
    - Sort output by score descending, requested date ascending, and sales order ascending.
    - The raw 50000 threshold is a simplified workshop rule, not an equivalent monetary threshold across currencies. Preserve currency labels; do not convert values or sum mixed currencies.
12. Save validated data as a CSV in the sandbox workspace. Run `scripts/prioritize_orders.py INPUT.csv --as-of YYYY-MM-DD --output OUTPUT.csv`, replacing placeholders with workspace paths and the supplied date. If validation fails, identify the affected row and field, ask for corrected data, and stop without presenting successful results. If execution fails or is unavailable, use the reference-only stop branch in step 3, never simulated execution.
13. Present only actual script results. Show the 10 highest-ranked rows as a Markdown action table with columns: Order, Customer, Date, Value, Priority, Score, Reasons, Credit Status, and Suggested Follow-up. Base follow-up only on verified reasons. Make the actual full ranked CSV available when file output is supported. For empty valid input, present a zero-count summary with no fabricated rows; the output CSV has headers and no data rows.
14. State the input mode, analysis date, number analyzed, totals for Critical, High, Medium, and Low, and number of unknown credit statuses. For a CSV, do not claim a live matching count; state that all supplied rows were scored without live filtering. For live input, state matching versus analyzed counts, current-status semantics, and the retrieval scope. If more than 50 matched, label the result a bounded sample, not a ranking of every matching order.
15. Treat the result as decision support, not SAP business policy. Limit the response to the requested fields and evidence-backed findings.

## Workshop requests

Fixture-first request (participant must attach the separately supplied CSV):

`Use Sales Order Exception Prioritizer to rank all rows in the attached open-sales-orders.csv using analysis date 2026-10-07. Use the CSV only; do not retrieve backend data.`

Optional facilitator-confirmed live request:

`Use Sales Order Exception Prioritizer to rank my authorized sales-order exceptions using analysis date 2026-10-07. Follow its bounded live-retrieval procedure using current delivery and credit statuses.`
