---
name: s4-purchase-order-excel-report
description: Create a filtered purchase-order Excel report from one bounded authorized SAP S/4HANA retrieval or an explicitly requested attached synthetic workshop CSV
---

## Instructions

Create a purchase-order Excel report. Choose exactly one source path per request: authorized live data or explicitly supplied synthetic workshop CSV. Never silently substitute one for the other.

1. Collect one specific purchasing organization, supplier or the explicit value `all suppliers`, an inclusive creation-date start and end, currency, and report date. Require valid `YYYY-MM-DD` dates with start no later than end. Ask for missing, invalid, or ambiguous values; never infer them. Do not accept `all purchasing organizations`.
2. Check that `Excel` is enabled before proceeding. If unavailable, explain the blocker, ask for facilitator help, and stop without claiming to have created a workbook or completed the exercise.
3. Select the source:
   - **Attached synthetic CSV path:** Use this path only when the user explicitly requests the attached synthetic workshop CSV. Require the attachment; if missing, ask for it and stop. Do not call any SAP business skill, even if enabled. Validate and process the supplied rows as described below.
   - **Live path:** Use only the enabled SAP-published `SAP S/4HANA Cloud Public Edition` skill for authorized purchase-order retrieval. This custom skill cannot connect directly to SAP. Follow the single-request boundary below.

### Live source: exactly one bounded detail request

Make exactly one call to `SAP S/4HANA Cloud Public Edition` for purchase-order details. Apply purchasing organization, supplier (unless `all suppliers`), inclusive creation-date range, and currency filters in SAP before retrieval. Sort by creation date descending, then purchase-order number ascending, and apply a maximum of 20 records before retrieval. Retrieve only purchase-order number, supplier name or identifier, purchasing organization, creation date, and currency.

Do not make a separate count request, paginate, retry, probe alternate services, or switch business skills. Do not request, filter, sort, or report status or net value. On any error, including authorization, connection, timeout, partial or truncated data, report the first error and stop without a workbook. An explicitly bounded top-20 result is allowed; an error or response flagged partial/truncated is not. If a required filter, sort, limit, field, or complete data handoff cannot be supported, stop rather than silently omitting it. Explain that the user can start a new request with the supplied synthetic workshop CSV or ask the facilitator for a supported option; never generate fallback data yourself.

Validate every returned row against the requested filters. Require all five fields, preserve identifiers and meaningful returned values, and reject missing or ambiguous required values rather than inventing them. Preserve valid calendar dates; convert a timestamp only with known format and units, then validate the date against the requested range. Stop on invalid or out-of-range rows. A successful zero-row response proceeds to an empty workbook table.

### Synthetic source: supplied CSV only, no backend

Require exactly these five headers in order: `Purchase Order`, `Supplier`, `Purchasing Organization`, `Creation Date`, `Currency`. Treat identifiers as text and preserve them unchanged. Require non-empty values, unique purchase-order identifiers, and valid `YYYY-MM-DD` creation dates. On malformed input, ask for a corrected attachment and stop; never invent or repair records silently.

Filter the supplied rows by exact purchasing organization, exact supplier unless `all suppliers`, inclusive creation-date range, and exact currency. Sort all matching rows by creation date descending and purchase-order identifier ascending, then select at most 20. Out-of-filter fixture rows are intentionally excluded, not retrieval errors. Use only the attachment; do not consult live data, claim SAP authorization or retrieval, or infer that the fixture represents any live population. The workshop fixture uses invented `DEMO-PO-` and `DEMO-SUP-` identifiers. Zero matches proceeds to an empty workbook table.

### Shared workbook contract

Use the enabled `Excel` skill to create `purchase-order-report.xlsx` with exactly two worksheets:

1. `Summary`: report date, every applied filter, source, analyzed row count, and the 20-record limit. No monetary totals.
   - Live source: identify `SAP S/4HANA Cloud Public Edition`, whether 20 rows were returned, and the bounded retrieval limitation. State that the result may not represent all matching records. Do not claim a total matching count or complete matching population; there is no separate count request.
   - Synthetic source: identify `Synthetic workshop CSV: purchase-orders.csv` for the supplied workshop file, state `No live retrieval occurred`, and describe the 20-record output limit as a local selection from supplied synthetic data, not a live retrieval limit. Do not make SAP population or live completeness claims. If a differently named synthetic attachment was explicitly supplied, use its actual filename in the source label.
2. `Purchase Orders`: exactly `Purchase Order`, `Supplier`, `Purchasing Organization`, `Creation Date`, `Currency`, in that order. Include one row per selected purchase order, sorted by creation date descending and purchase-order identifier ascending, with at most 20 rows. Use headers, table filters, and a valid date display. For zero matches, leave the table empty below the headers and put the zero-result note only on `Summary`.

Do not convert currencies or add formulas, macros, hidden worksheets, or external links. Before returning the workbook, verify it opens, both worksheet names and the five headers are exact, all rows match the filters, dates and sorting are correct, analyzed count matches the data rows, the 20-row limit holds, and source labeling is accurate. If file creation or validation fails, report the failure without claiming success.

Return the workbook and analyzed row count. For live data, disclose the bounded scope; for synthetic data, explicitly identify the synthetic source and absence of live retrieval.
