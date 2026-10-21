---
name: s4-purchase-order-excel-report
description: Retrieve a bounded set of authorized SAP S/4HANA purchase orders for one purchasing organization and create an Excel report
---

## Instructions

Use this skill only to create a read-only Excel report of purchase orders that the signed-in user is authorized to view in SAP S/4HANA. Do not use it to create, change, approve, release, or delete purchase orders.

1. Collect all required filters before retrieval:
   - one specific purchasing organization; do not accept `all purchasing organizations` for the live path;
   - supplier, or the explicit value `all suppliers`;
   - purchase-order creation date range with inclusive start and end dates in `YYYY-MM-DD` format;
   - currency;
   - report date in `YYYY-MM-DD` format.
2. Ask for every missing or ambiguous filter. Do not infer dates, currency, supplier, organization, or report date. If the user requests all purchasing organizations, ask for one organization to keep the live retrieval narrowly bounded.
3. Use the enabled SAP-published `s4hana-public-cloud` or `s4hana-private-cloud` skill, as confirmed by the facilitator, to retrieve only purchase orders the signed-in user is authorized to view. This custom skill does not connect directly to SAP S/4HANA.
4. Apply the purchasing organization, supplier, creation-date range, and currency filters in SAP before retrieval. Retrieve only these fields:
   - purchase-order number;
   - supplier name or identifier returned by the SAP skill;
   - purchasing organization;
   - creation date;
   - currency.
5. Make one bounded detail-retrieval request for at most 20 purchase orders. Sort by creation date descending and purchase-order number ascending and apply the 20-record limit in SAP before retrieval. Do not request, filter, sort, or report purchase-order status or net value; the qualified workshop service did not return meaningful values for those fields. Do not make a separate count request or fetch additional pages.
6. Use only the facilitator-confirmed purchase-order service selected by the enabled S/4HANA skill. Do not probe alternative services and do not retry the detail request. If the single detail request fails, stop immediately, report that live retrieval is unavailable for this run, and ask for a facilitator-approved CSV fallback. Do not diagnose the backend, recommend SICF changes, or claim a temporary suspension unless the service explicitly returns that information.
7. Validate every returned row against the requested filters. Preserve values exactly as returned. Do not invent missing values. Mark unavailable optional display text as `Not available`.
8. Use the enabled `xlsx` skill to create `purchase-order-report.xlsx` with exactly two worksheets:
   - `Summary`: show report date, every applied filter, analyzed row count, the fixed 20-record live limit, whether 20 rows were returned, and any retrieval limitation. Do not claim a total matching count because no separate count request is made. Do not show a net-value total.
   - `Purchase Orders`: use these columns in this exact order: `Purchase Order`, `Supplier`, `Purchasing Organization`, `Creation Date`, `Currency`.
9. In `Purchase Orders`, include one row per retrieved purchase order and sort rows by creation date descending, then purchase-order number ascending. Use a header row, filters, and an appropriate date format. If no records are returned, leave the table empty below the header and put the zero-result note only on `Summary`. Do not add formulas, macros, hidden worksheets, or external links.
10. Before returning the file, verify that both worksheets exist, the headers and ordering are correct, each row satisfies the filters, the rows follow the required sorting, no status or net-value field appears, and the workbook opens successfully.
11. Return the workbook and state the analyzed row count, that the live result is bounded to at most 20 rows, and: `No SAP business data was changed.` If fewer than 20 rows are returned, describe only the analyzed result; do not claim it is the complete matching population unless the SAP service explicitly establishes that fact in the same detail response.
12. If the required S/4HANA skill, authorization, data handoff, required fields, `xlsx` skill, or single detail request is unavailable, explain exactly what is unavailable and stop. Do not invent a report, repeatedly retry, switch services, or claim that a workbook was created.
