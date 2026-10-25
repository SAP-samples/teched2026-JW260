---
name: invoice-po-reconciliation
description: Analyse a supplier invoice PDF for inconsistencies against an SAP S/4HANA purchase order and produce a detailed reconciliation report in Excel
---

## Instructions

Use this skill when a user attaches a supplier invoice and asks for an inconsistency check, reconciliation analysis, or comparison against a purchase order. Do not use this skill for general invoice queries, payment processing, or any write-back operation.

Do not approve, post, release, or change any invoice or purchase order. This skill is read-only.

### Step 1 — Extract all data from the invoice

Read the attached invoice PDF and extract the following header fields:

- `invoice_number`: exactly as printed.
- `vendor_name`: supplier name as printed.
- `vendor_id`: SAP vendor account number if present; note as `Not stated on invoice` if absent.
- `po_number`: the purchase order reference as printed.
- `invoice_date`: converted to `YYYY-MM-DD`.
- `currency`: the invoice currency code (for example, `EUR`, `USD`).

Extract each line item:

- `line_item`: item number exactly as printed (for example, `10`, `20`).
- `description`: item description text.
- `quantity`: numeric quantity.
- `unit`: unit of measure.
- `unit_price`: numeric unit price in the invoice currency.
- `line_total`: numeric line total in the invoice currency.

Validate that each `line_total` equals `quantity × unit_price` within a 0.01 rounding tolerance. If any line total does not match, report the specific line and ask the user to confirm or correct it before continuing.

If a required header field (`invoice_number`, `po_number`, `invoice_date`, `currency`) cannot be read from the document, ask the user for it. Do not invent values.

### Step 2 — Retrieve the purchase order from SAP S/4HANA

This custom skill cannot connect directly to SAP S/4HANA. Use an available SAP-published skill for SAP S/4HANA to retrieve the PO referenced on the invoice.

Retrieve for the PO header: `PurchaseOrder`, `Supplier`, `PurchasingOrganization`, `DocumentCurrency`, `CreationDate`.

Retrieve for each PO line: `PurchaseOrderItem`, `PurchaseOrderItemText`, `OrderQuantity`, `OrderQuantityUnit`, `NetPriceAmount`, `NetPriceQuantity`, `DocumentCurrency`.

If the SAP-published capability is unavailable, tell the user and ask them to attach a PO JSON fixture in the format described in `references/reconciliation-rules.md`. Never invent SAP data.

Once retrieved or supplied, check the following:

**PO number mismatch:** if the returned `PurchaseOrder` does not match the invoice PO reference, stop and ask the user to confirm the correct reference.

**Supplier mismatch:** if `vendor_id` is stated on the invoice and does not match the returned `Supplier`, report both values and ask the user whether to continue.

**Currency mismatch:** if the PO `DocumentCurrency` differs from the invoice `currency`, do not convert and do not stop silently. Present:
- The invoice currency extracted from the document.
- The PO currency from SAP S/4HANA.
- The likely reasons: amended PO, wrong PO reference on the invoice, or incorrect invoice currency.
- Three options:
  1. Provide a different PO number to retrieve.
  2. Attach a PO fixture in the invoice currency to proceed.
  3. Cancel and resolve the discrepancy outside this skill.

Wait for the user's choice. If the user supplies a fixture, validate and continue. If the user cancels, summarise the discrepancy and end with: `No SAP business data was changed.`

### Step 3 — Reconcile invoice lines against PO lines

Apply the rules from `references/reconciliation-rules.md` to each invoice line:

**Matching:** match by description (case-insensitive). A line that matches no PO item is `not_in_po`. A PO item matched by no invoice line is `not_invoiced`.

**Price deviation:** calculate `abs(invoiced_unit_price - po_unit_price) / po_unit_price × 100`, rounded to two decimal places. If the result exceeds 2.00%, status is `price_deviation`.

**Quantity deviation:** if invoiced quantity differs from PO quantity and price is within tolerance, status is `quantity_deviation`. If both price and quantity differ, status is `price_deviation` with the quantity difference noted.

**Match:** price within 2.00% tolerance and quantity equal.

Compute for each line: status, price deviation %, invoiced total, PO line value (`NetPriceAmount / NetPriceQuantity × OrderQuantity`), and amount deviation (invoiced total minus PO line value).

Compute totals: total invoiced, total PO value, net deviation.

Overall status is `MATCH` only when net deviation is 0.00 and no lines have any deviation or mismatch status. Otherwise `REVIEW REQUIRED`.

### Step 4 — Present a plain-language analysis

Present findings conversationally before generating the file:

1. State the overall result — match or review required.
2. For each `price_deviation` or `quantity_deviation` line: name the item, state invoiced and PO values, deviation percentage and amount, and one suggested action.
3. For each `not_in_po` line: name the item and state that it has no PO line. Suggest confirming whether a separate PO covers it.
4. For each `not_invoiced` PO line: name the item and note it was not invoiced.
5. State the net deviation.

Do not recommend payment approval or rejection. Present as decision support only.

### Step 5 — Export the reconciliation report to Excel

Use the available `xlsx` skill to create `invoice-reconciliation-<invoice_number>.xlsx`, replacing spaces, slashes, and special characters in the invoice number with hyphens.

**Worksheet 1 — `Summary`** (one label–value row per field, in this order):

| Field | Value |
|---|---|
| Invoice Number | as extracted |
| Vendor Name | as extracted |
| Vendor ID | as extracted, or `Not stated on invoice` |
| Purchase Order | as extracted |
| Invoice Date | `YYYY-MM-DD` |
| Currency | as extracted |
| Report Date | today's date in `YYYY-MM-DD` |
| Lines Invoiced | count of invoice lines |
| Lines in PO | count of PO lines |
| Total Invoiced | two decimal places |
| Total PO Value | two decimal places |
| Net Deviation | two decimal places |
| Lines Matched | count |
| Lines with Deviation | count of `price_deviation` + `quantity_deviation` |
| Lines Not in PO | count |
| Lines Not Invoiced | count |
| Overall Status | `MATCH` or `REVIEW REQUIRED` |

**Worksheet 2 — `Line Items`** (one row per reconciliation line, columns in this exact order):

`Invoice Line` · `PO Item` · `Description` · `Invoiced Qty` · `PO Qty` · `Unit` · `Invoiced Unit Price` · `PO Unit Price` · `Price Deviation %` · `Invoiced Total` · `PO Line Value` · `Amount Deviation` · `Status` · `Note`

Sort: matched and deviation rows first by invoice line number ascending, then `not_invoiced` PO rows by PO item ascending, then `not_in_po` invoice rows by invoice line ascending.

### Step 6 — Final check

Before returning the file, verify:

- Both worksheets exist with the exact names `Summary` and `Line Items`.
- `Overall Status` correctly reflects the `Line Items` data.
- No SAP data was created, changed, posted, released, or approved.
- End every response with: `No SAP business data was changed.`

### Boundaries

Do not use this skill for:
- Posting, releasing, or approving invoices or purchase orders.
- Currency conversion.
- Requests involving personal employee data.
- Any write-back to SAP S/4HANA.
