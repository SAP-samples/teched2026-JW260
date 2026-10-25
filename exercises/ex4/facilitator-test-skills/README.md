# Facilitator Test Skills for Exercise 4

These completed references support facilitator qualification. Participants first build and test their own skill from the [Exercise 4 contracts](../README.md); comparison is optional. Disable the participant version while testing a reference so they do not compete for selection. These sources and captured examples do not establish qualification of the current tenant.

## Dependencies and import

| Reference and path | Required SAP-published skills |
| --- | --- |
| `s4-purchase-order-excel-report`, live | `s4hana-public-cloud`, plus `xlsx` |
| `s4-purchase-order-excel-report`, synthetic CSV | `xlsx` only; no backend call |
| `successfactors-benefit-plan-country-report`, live | `successfactors-hr`, plus `docx` |

Follow [Importing a skill](../../../README.md#importing-a-skill): import `SKILL.md` directly for a simple skill or the complete unzipped named folder when it contains supporting files. Do not create import archives here. For a replacement, disable and remove the old imported copy before importing the updated source. Enable the reference and every dependency for the chosen path, confirm them under **Active Skills**, and start a new conversation with **Agentic Thinking** explicitly selected before each qualification or retest.

## Qualification requests

Use facilitator-confirmed live values when the examples are unsupported, and keep prompts unchanged for comparisons. The participant exercise contains the same requests. Download and open each generated file; the written contract takes precedence over visual variation and captured counts.

### Option A: live SAP S/4HANA

```text
Create a purchase-order Excel report for purchasing organization D3US, all suppliers, creation dates 2026-01-01 through 2026-10-20, currency EUR, with report date 2026-10-20.
```

Expected artifact: `purchase-order-report.xlsx`; check the [Option A contract and checklist](../README.md#option-a-contract). Require exactly one `s4hana-public-cloud` detail call, with filters and sorting applied before the 20-row limit. No status/net-value criterion, count request, pagination, retry, or alternate service. An error, partial/truncated response, missing required field, or unsupported filter stops the run without a workbook. A successful zero-result response produces an empty table, not a message row. Live `Summary` must identify its source and bounded scope without a total matching count or completeness claim.

### Option A: explicit synthetic CSV fallback

Attach [`purchase-orders.csv`](../sample-data/purchase-orders.csv) and run:

```text
Use only the attached synthetic workshop CSV purchase-orders.csv; do not call SAP. Create a purchase-order Excel report for purchasing organization DEMO, all suppliers, creation dates 2026-01-01 through 2026-10-20, currency EUR, with report date 2026-10-20. Label the Summary source as Synthetic workshop CSV: purchase-orders.csv, state that no live retrieval occurred, and make no live completeness claims.
```

This is invented workshop data with five source columns: `Purchase Order`, `Supplier`, `Purchasing Organization`, `Creation Date`, `Currency`. It is not retrieved SAP data. Require no backend call, filtering over the supplied rows, sorting all matches before the local 20-row limit, and the same workbook filename, worksheets, and columns as the live contract. The `Summary` source must be synthetic and must not imply live retrieval or live completeness.

If live access fails, choose a supported option or explicitly start this synthetic path; never silently substitute data or keep retrying. If `xlsx` is unavailable, escalate and record the run as blocked, not complete. A local fixture check is not an end-to-end Joule or live-tenant qualification.

### Option B: live SAP SuccessFactors

```text
Create a SuccessFactors benefit-plan report for Germany with report date 2026-10-20.
```

Expected artifact: `benefit-plans-germany.docx`; check the [Option B contract and checklist](../README.md#option-b-contract). Require exactly one `successfactors-hr` call for plans matching the requested country or region. Only when metadata is unavailable may the returned plan name supply an exact country-name match; no partial, alias, or inferred regional matching. On the first error, partial/truncated result, or no matching plans, stop without a document, retry, or alternate service.

The Word file contains only title, country/report-date scope, plan summary, and plan details. No Data Notes, matching-method explanation, disclaimers, or skill-execution information. Use returned plan configuration, never personal enrollments or compensation. There is no SuccessFactors fixture; use a supported option or Option A's synthetic path if blocked.

## Qualification evidence

Record the actual source path, business skill used (none for synthetic), supported fields, authorization scope for live data, data handoff, whether the Office file opened, and every deviation from the contract. Inspect visible execution details for forbidden retries or alternate services; do not claim an exact observed backend-call count unless those details expose it. Do not describe a live option as workshop-ready until its complete path succeeds with a clean participant identity and representative non-empty data. Qualify the synthetic output path separately; neither static validation nor a synthetic report proves live access.
