# Facilitator Test Skills for Exercise 4

These reference skills are for facilitator qualification before the workshop. Participants should build their own skill from the Exercise 4 requirements rather than import these finished versions.

## Required active skills

| Reference skill | Required SAP-published skills |
| --- | --- |
| `s4-purchase-order-excel-report` | facilitator-confirmed `s4hana-public-cloud` or `s4hana-private-cloud`, plus `xlsx` |
| `successfactors-learning-word-report` | `successfactors-learning`, plus `docx` |
| `ariba-requisition-powerpoint-review` | facilitator-confirmed SAP Ariba skill, plus `pptx` |

Enable the business skill, output skill, and imported reference skill. Confirm all three under **Active Skills** and select agentic thinking mode.

## Package and import

ZIP the complete named folder so that the archive contains one top-level folder and its `SKILL.md`. Ready-to-import archives may also be generated in this directory during facilitator preparation.

## Qualification requests

Replace the example filter values with values supported by the workshop tenant.

### SAP S/4HANA

`Create a purchase-order Excel report for purchasing organization D3US, all suppliers, creation dates 2026-01-01 through 2026-10-20, currency EUR, with report date 2026-10-20.`

Expected artifact: `purchase-order-report.xlsx`. Verify it against Option A in `../README.md`.

The expected live behavior is one detail request capped at 20 rows, with no status or net-value criterion, separate count, pagination, alternate-service probing, or retry. If that request fails, the skill must stop rather than trigger repeated backend calls.

### SAP SuccessFactors

`Create my learning due-date Word report for due dates 2026-01-01 through 2026-12-31, with report date 2026-10-20.`

Expected artifact: `learning-due-date-report.docx`. Verify it against Option B in `../README.md`.

### SAP Ariba

`Create a requisition review PowerPoint for submissions from 2026-01-01 through 2026-10-20, minimum total value 1000 EUR, all authorized requesters, status Submitted, with report date 2026-10-20.`

Expected artifact: `requisition-review.pptx`. Verify it against Option C in `../README.md`.

## Qualification result

Record the exact business skill used, supported fields, authorization scope, whether business data was handed to the custom skill, whether the Office artifact opened successfully, and every deviation from the expected output. Do not describe an option as workshop-ready until the complete path succeeds with a clean participant identity.
