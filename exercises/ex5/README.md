# Exercise 5: Supplier Invoice Reconciliation — Build It Yourself

## Goal

Write a custom Joule skill that a user can trigger by attaching a supplier invoice PDF and asking for an inconsistency check. The skill should extract data from the invoice, retrieve the matching purchase order from SAP S/4HANA, flag any discrepancies, and produce a plain-language summary and an Excel report.

The scaffold is in `invoice-po-reconciliation/`. Fill in the `<!-- TODO -->` sections, then import and test. The complete solution is in `solutions/` — check it only after your own attempt.

## Timebox: 30 minutes

- Read the scenario and open the sample files: 5 minutes
- Fill in the scaffold: 15 minutes
- Import, test, and iterate: 10 minutes

## Before You Start

1. Open **Explore Skills** and enable the SAP-published S/4HANA skill confirmed by your facilitator and the `xlsx` output skill.
2. Confirm both appear under **Active Skills**.
3. Select agentic thinking mode.

## The Scenario

A finance team member attaches a supplier invoice PDF to Joule and asks for an inconsistency check against the corresponding SAP purchase order. Your skill handles everything from there — no further prompts needed.

Open both sample files before writing the skill:

| File | What it is |
|---|---|
| `sample-data/Invoice_INV-2023-08841_RookEquip.pdf` | The supplier invoice |
| `sample-data/PurchaseOrder_4500000000.pdf` | The SAP purchase order |
| `sample-data/po-4500000000-fixture.json` | PO fixture in USD (fallback if SAP is unavailable) |
| `sample-data/po-4500000000-eur-fixture.json` | PO fixture in EUR (use after the currency dialogue) |

Note the differences between the invoice and the PO — your skill needs to detect and report them.

## Fill in the Scaffold

Open `invoice-po-reconciliation/SKILL.md` and `references/reconciliation-rules.md`. Each file has `<!-- TODO -->` comments with a short hint. Fill in every section, then zip the `invoice-po-reconciliation/` folder and import it.

## Test

Attach `sample-data/Invoice_INV-2023-08841_RookEquip.pdf` and run:

```
Please analyse this invoice for inconsistencies and give me a detailed report.
```

The skill should extract all data from the PDF without asking, detect that the PO currency (USD) differs from the invoice currency (EUR), and ask how to proceed. Supply `sample-data/po-4500000000-eur-fixture.json` when prompted, then verify the Excel output.

Expected result: `invoice-reconciliation-INV-2023-08841.xlsx` with a `Summary` sheet and a `Line Items` sheet showing one `price_deviation` line and one `not_in_po` line.

## Fixture Fallback

If the SAP S/4HANA capability is unavailable, the skill will ask for a PO fixture. Attach `sample-data/po-4500000000-fixture.json` (USD) to trigger the currency dialogue, then supply `po-4500000000-eur-fixture.json` to continue.

## Troubleshooting

| Problem | Action |
|---|---|
| Skill asks for invoice number or PO upfront | Add the extraction step to `SKILL.md` — the skill should read these from the PDF. |
| Skill stops silently on currency mismatch | Add a currency-mismatch block that presents options to the user. |
| No plain-language analysis before the file | Add a step that presents findings before exporting. |
| `xlsx` skill is disabled | Enable it under **Explore Skills** and confirm it appears under **Active Skills**. |
| Generated file cannot be opened | Confirm the `xlsx` skill ran, check the filename, and regenerate. |

## Summary

You built a skill that reads an invoice PDF, detects discrepancies against a purchase order, and delivers a reconciliation report — with a governed read-only boundary throughout.

Continue to — [Exercise 6 - Freestyle](../ex6/README.md) or return to [JW260 Workshop Overview](../../README.md)
