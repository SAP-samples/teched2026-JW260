---
name: successfactors-benefit-plan-country-report
description: Retrieve authorized SuccessFactors benefit-plan configuration for one country and create a country-specific Word report
---

## Instructions

Create a SuccessFactors benefit-plan report for one requested country. Never retrieve personal enrollments, employee compensation, or another employee's data.

1. Get a country and report date in `YYYY-MM-DD` format. Ask only for a missing or invalid value. Country must be a non-empty country name; do not guess country codes, aliases, or regional mappings.
2. Make exactly one call to the enabled `successfactors-hr` skill. Retrieve only benefit plans whose configured country or region matches the requested country. If that metadata is unavailable, an exact country-name match in the returned plan name is an acceptable fallback. Do not use partial-name, alias, or inferred regional matches. Request only fields the service supports: plan name, benefit ID, type, status, effective date, entitlement amount and currency, payment frequency, payroll integration, enrollment requirement and method, enrollment window, opt-out, carry-forward enrollment, notification, eligibility rule, claims limit, dependent-specific rules, nominee requirement, and benefit schedule. Do not call SuccessFactors directly.
3. On any error, including authorization, connection, timeout, partial or truncated data, do not retry, switch services, or probe alternatives. Report the first error and stop.
4. If no matching plans are returned, state that no matching benefit plans were returned and stop. Do not create a document.
5. Use only fields returned with clear displayed meanings. Preserve returned wording. Do not infer missing plan amounts, enrollment conditions, eligibility, regional applicability, personal coverage, payment entitlement, or legal or tax advice. Use `Not available` only when an expected field was not returned.
6. Use the enabled `docx` skill to create `benefit-plans-<country-slug>.docx`, where `<country-slug>` is the requested country in lowercase hyphenated form. The document must contain exactly these sections in this order:
   1. `Benefit Plans - <Country>`
   2. `Report Scope` - requested country and report date
   3. `Plan Summary` - a table with `Plan Name`, `Benefit ID`, `Type`, `Amount`, `Currency`, `Frequency`, `Enrollment`, and `Status`; sort rows alphabetically by `Plan Name`
   4. `Plan Details` - one subsection per plan, in the same alphabetical order as the summary. Include only returned configuration fields.
7. The document contains only the report title, scope, summary, and plan-detail content. Do not add `Data Notes`, source descriptions, matching-method explanations, eligibility or enrollment disclaimers, payment-entitlement statements, legal or tax disclaimers, or other process or skill-execution information.
8. Check the four-section order, country match, alphabetical ordering, source grounding, privacy, and filename before returning the file.

If `successfactors-hr`, authorization, complete data handoff, or `docx` is unavailable, state what failed and stop. Do not fabricate data or claim that a document was created.
