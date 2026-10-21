# Exercise 4: Build a Skill for a Line-of-Business Scenario

## Goal

Choose one defined SAP S/4HANA, SAP SuccessFactors, or SAP Ariba outcome, create the custom skill manually or with Joule, and verify the generated business document against the expected output.

## Choose one scenario

Complete one of the following three scenarios. The business outcome and output format are fixed; you design the skill that achieves them.

The exact SAP-published skill names can differ by workshop tenant. Before starting, confirm in **Explore Skills** that your chosen scenario has an available capability and that your workshop identity can access the required data. A custom skill cannot connect directly to an SAP backend; an available SAP-published skill retrieves authorized data and the custom skill prepares the report.

## Why build a custom skill?

Agentic Thinking may be able to complete a similar request without your custom skill, but its retrieval strategy and output can vary between conversations. Your custom skill turns the request into a reusable business procedure: it asks for the same required inputs, applies the same safety boundaries and retrieval limit, and produces a report with a predictable filename and structure.

The SAP-published business skill supplies authorized business data, the `xlsx`, `docx`, or `pptx` skill creates the file, and your custom skill defines how those capabilities are combined. The goal is therefore not merely to generate a file once, but to make the result repeatable, governed, and easy to verify.

## Enable the required skills

Before building or running your custom skill, open **Explore Skills** and enable both the business skill and the output skill required by your option:

| Option | Business skill | Output skill |
| --- | --- | --- |
| SAP S/4HANA purchase-order report | The facilitator-confirmed `s4hana-public-cloud` or `s4hana-private-cloud` skill | `xlsx` |
| SAP SuccessFactors learning report | `successfactors-learning` | `docx` |
| SAP Ariba requisition review | The facilitator-confirmed SAP Ariba skill | `pptx` |

Use the exact skill names shown in the workshop catalog. Confirm that each required toggle is on and that both skills appear under **Active Skills**. If the required business or output skill is missing, stop and ask the facilitator which option is supported; enabling only your custom skill is not sufficient.

## Option A: SAP S/4HANA — Filtered Purchase Order Excel Report

### Target outcome

Create a custom skill that asks for these filters:

- one specific purchasing organization;
- supplier, or `all suppliers`;
- purchase-order creation date range;
- currency.

The skill uses an available SAP S/4HANA capability to retrieve matching purchase orders and creates `purchase-order-report.xlsx`.

The workbook must contain:

1. A worksheet named `Summary` with the applied filters, report date, number of analyzed purchase orders, and the 20-record live limit. The live path does not make a separate count request.
2. A worksheet named `Purchase Orders` with these columns in this order:
   - Purchase Order
   - Supplier
   - Purchasing Organization
   - Creation Date
   - Currency
3. One row per retrieved purchase order, sorted by creation date descending and then purchase-order number ascending, with at most 20 rows.
4. A clear note that the live result is bounded and may not represent all matching records.

The qualified workshop service did not return a meaningful header-level net-value field. The live skill therefore must not request, filter, sort, or total by net value. It must make one narrowly filtered detail request and must not make a separate count request, fetch additional pages, probe alternative services, or retry after a failed detail request. On the first retrieval failure, it stops and asks for a facilitator-approved CSV fallback.

### Verify the output

Open `purchase-order-report.xlsx` and confirm:

- both worksheets exist with the exact names;
- the `Summary` values match the filters used in the request;
- the `Purchase Orders` columns are in the required order;
- every visible row matches the filters;
- the rows follow the required sort order;
- no more than 20 purchase-order rows are present;
- a zero-result workbook has an empty table below the headers rather than a message row;
- values are not converted between currencies;
- no purchase order was created, changed, approved, or released.

## Option B: SAP SuccessFactors — Learning Due-Date Word Report

### Target outcome

Create a custom skill that asks for a due-date range and report date, retrieves the signed-in participant's authorized learning assignments with `successfactors-learning`, and creates `learning-due-date-report.docx` with the `docx` skill.

Use one retrieval. If server-side date filtering is unavailable, the custom skill may filter a complete returned result locally. It must stop if the result is partial, truncated, or unavailable.

The document must contain these sections in this order:

1. `Learning Due-Date Report`
2. `Report Scope` — signed-in user, selected due-date range, and report date.
3. `Summary` — total assignments and counts for overdue, due within the selected range, and completed.
4. `Overdue Assignments` — title, due date, and status, sorted by due date ascending.
5. `Assignments Due in Range` — title, due date, and status, sorted by due date ascending.
6. `Recommended Next Steps` — a short, factual list based only on the retrieved assignments.

The report must not include learning data for another employee and must not invent completion status, due dates, or recommendations based on unavailable data.

### Verify the output

Open `learning-due-date-report.docx` and confirm:

- all six sections exist in the required order;
- the report scope shows the requested date range;
- the summary counts agree with the listed assignments;
- overdue and due-in-range assignments appear under the correct headings;
- assignments are sorted by due date ascending;
- no unsupported employee or personal information appears;
- no learning assignment was created, changed, or completed.

## Option C: SAP Ariba — Requisition Review PowerPoint

### Target outcome

Create a custom skill that asks for these filters:

- requisition submission date range;
- minimum total value;
- currency;
- requester, or `all authorized requesters`;
- requisition status.

The skill uses an available SAP Ariba capability to retrieve matching requisitions and creates `requisition-review.pptx`.

The presentation must contain exactly five slides:

1. `Requisition Review` — title and applied date range.
2. `Scope and Filters` — all filters used and the report date.
3. `Summary` — number of matching requisitions and total value by currency.
4. `Highest-Value Requisitions` — up to five requisitions sorted by value descending, showing requisition ID, requester, value, currency, submission date, and status.
5. `Review Points` — factual observations and items requiring human review; no approval recommendation may be presented as an automated decision.

### Verify the output

Open `requisition-review.pptx` and confirm:

- it contains exactly five slides with the required titles and order;
- the scope slide contains every filter from the request;
- the summary agrees with the retrieved data;
- slide 4 contains no more than five requisitions and uses the required sort order and fields;
- observations are supported by the retrieved data;
- currencies remain separate and are not converted;
- no requisition was created, changed, submitted, or approved.

## Build and run your skill

1. Choose Option A, B, or C.
2. In **Explore Skills**, enable the required business skill and `xlsx`, `docx`, or `pptx` output skill shown in the table above. Confirm that both appear under **Active Skills**.
3. Create a lowercase, hyphenated skill folder containing `SKILL.md`.
4. Build the skill manually or ask Joule to help draft it.
5. Ensure the skill defines its purpose, required filters, retrieval handoff, validation, exact output structure, sorting, missing-data behavior, and read-only boundary.
6. ZIP the complete skill folder, import it, enable it, and select agentic thinking mode.
7. Run the skill with filter values supported by the workshop data.
8. Download and open the generated file.
9. Verify it against the checklist for your selected option.
10. If a check fails, improve the skill, reimport it, and run the same request again.

## Troubleshooting

| Problem | Action |
| --- | --- |
| The required SAP-published capability is unavailable | Choose another option or ask the facilitator which scenario is supported by the tenant. |
| The `xlsx`, `docx`, or `pptx` skill is disabled | Enable the output skill for your option under **Explore Skills**, then confirm it appears under **Active Skills**. |
| A required field cannot be retrieved | Do not invent it. Ask the facilitator whether another option is supported. |
| Retrieved data cannot be handed to the custom skill | State the limitation and use facilitator-approved synthetic data if available. |
| The S/4HANA detail request fails | Stop after the first failure. Do not retry or probe other services; use a facilitator-approved CSV fallback if available. |
| The generated file cannot be opened | Check the requested format, filename, and generation instructions, then regenerate it. |
| The environment cannot generate the required file type | Preserve the same content and structure in a facilitator-approved fallback; do not claim that the target file was created. |
| The request would change business data | Stop and revise the skill so it remains read-only. |

## Expected result

You created one custom skill that meets a predefined line-of-business outcome and generated a report that passes every applicable verification check.

## Summary

You translated a defined SAP business outcome into a custom skill, combined it with authorized data retrieval, generated a business file, and verified the result against a fixed contract.

Continue to - [Exercise 5 - Freestyle](../ex5/README.md)
