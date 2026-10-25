---
name: invoice-po-reconciliation
description: <!-- TODO: One sentence — what does this skill do, for which document, and against which SAP object? -->
---

## Instructions

<!-- TODO: When should Joule use this skill? What is it not allowed to do (think: read-only)? -->

### Step 1 — Extract data from the invoice

<!-- TODO: Which fields should Joule read from the PDF before asking the user anything?
     What should it do if a required field is missing? -->

### Step 2 — Retrieve the purchase order and check for mismatches

<!-- TODO: How does Joule get the PO — and what is the fallback if the SAP capability is unavailable?
     What should it do when the PO currency differs from the invoice currency?
     (Hint: don't convert — ask the user how to proceed.) -->

### Step 3 — Reconcile and report

<!-- TODO: How should Joule match invoice lines to PO lines?
     What counts as a match, a price deviation, or a line not on the PO?
     What should the plain-language summary contain before any file is exported?
     Describe the Excel output: filename, worksheets, and the columns you want. -->
