# Facilitator Test Skills for Exercise 4

These reference skills are for facilitator qualification before the workshop. Participants should build their own skill from the Exercise 4 requirements rather than import these finished versions.

## Required active skills

| Reference skill | Required SAP-published skills |
| --- | --- |
| `s4-purchase-order-excel-report` | facilitator-confirmed `s4hana-public-cloud` or `s4hana-private-cloud`, plus `xlsx` |
| `successfactors-benefit-plan-country-report` | `successfactors-hr`, plus `docx` |
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

`Create a SuccessFactors benefit-plan report for Germany with report date 2026-10-20.`

Expected artifact: `benefit-plans-germany.docx`. Verify it against Option B in `../README.md`.

The expected live behavior is exactly one `successfactors-hr` call for benefit plans whose country or region matches Germany. If country/region metadata is unavailable, an exact `Germany` name match is allowed; partial, alias, and inferred regional matches are not allowed. The Word document must contain only the title, requested-country/report-date scope, plan summary, and plan details—no Data Notes, matching-method explanation, disclaimers, or skill-execution information. The skill must retrieve only returned plan configuration fields, exclude personal enrollments and compensation data, and stop on the first error, partial or truncated result without retrying or switching services.

### SAP Ariba

`Create a requisition review PowerPoint for submissions from 2026-01-01 through 2026-10-20, minimum total value 1000 EUR, all authorized requesters, status Submitted, with report date 2026-10-20.`

Expected artifact: `requisition-review.pptx`. Verify it against Option C in `../README.md`.

## Qualification result

Record the exact business skill used, supported fields, authorization scope, whether business data was handed to the custom skill, whether the Office artifact opened successfully, and every deviation from the expected output. Do not describe an option as workshop-ready until the complete path succeeds with a clean participant identity.
