# Exercise 5: Supplier Invoice Reconciliation — Build It Yourself

## Goal

Write a custom Joule skill that a user can trigger by attaching a supplier invoice PDF and asking for an inconsistency check. The skill should extract data from the invoice, retrieve the matching purchase order from SAP S/4HANA, flag any discrepancies, and produce a plain-language summary and an Excel report.

The scaffold is in `invoice-po-reconciliation/`. Fill in the `<!-- TODO -->` sections, then import and test. The complete solution is in `solutions/` — check it only after your own attempt.

## Before You Start

1. Open **Explore Skills** and enable the SAP-published S/4HANA skill confirmed by your facilitator and the `xlsx` output skill.
2. Confirm both appear under **Active Skills**.
3. Select agentic thinking mode.

## The Scenario

A finance team member attaches a supplier invoice PDF to Joule and asks for an inconsistency check against the corresponding SAP purchase order. Your skill handles everything from there — no further prompts needed.

Open the sample invoice before writing the skill: `sample-data/Sample_INV-2023.pdf`

Note the differences between the invoice and the PO — your skill needs to detect and report them.

## Fill in the Scaffold

Open `invoice-po-reconciliation/SKILL.md` and `references/reconciliation-rules.md`. Each file has `<!-- TODO -->` comments with a short hint. Fill in every section, then zip the `invoice-po-reconciliation/` folder and import it.

## Test

Attach `sample-data/Sample_INV-2023.pdf` and run:

```
Please analyse this invoice for inconsistencies and give me a detailed report.
```

The skill should extract all data from the PDF without asking, detect any currency mismatch between the invoice and the PO, and ask how to proceed. Verify the Excel output once complete.

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
