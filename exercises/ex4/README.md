# Exercise 4: Build a Skill for a Line-of-Business Scenario

## Goal

Choose one defined SAP S/4HANA or SAP SuccessFactors outcome, create the custom skill manually or with Joule, and verify the generated business document. Your custom skill defines the required inputs, safe data handoff, and repeatable report structure; the SAP-published business and output skills supply the live data and file-generation capabilities.

Agentic Thinking may already produce a similar file from a one-off request. Your goal is to turn that request into a reusable procedure with predictable inputs, boundaries, and output, not merely to generate a file once.

## Build, run, and verify

1. Choose **Option A** (purchase-order Excel report) or **Option B** (benefit-plan Word report) below. The outcome is fixed; you design the skill.
2. In **Explore Skills**, enable the dependencies for your chosen path:

   | Path | Business skill | Output skill |
   | --- | --- | --- |
   | Option A, live | `SAP S/4HANA Cloud Public Edition` | `Excel` |
   | Option A, synthetic CSV | None; use the attached sample data only | `Excel` |
   | Option B, live | `SAP SuccessFactors HCM` | `Word Documents` |

3. Create a lowercase, hyphenated folder containing `SKILL.md`. Write it manually or ask Joule to draft it, then review the required inputs, data source, validation, output structure, sorting, and failure behavior.
4. Follow [Importing a skill](../../README.md#importing-a-skill). Enable your custom skill and confirm it and **every required dependency** under **Active Skills**. Start a new conversation and explicitly select **Agentic Thinking**.
5. Run the sample prompt for your chosen path. Download and open the file, then check the option's written output contract and checklist. Screenshots are optional examples, not proof that your run succeeded.
6. If a check fails, improve the source and follow [Replacing an imported skill](../../README.md#replacing-an-imported-skill). Recheck **Active Skills**, start a new **Agentic Thinking** conversation, and rerun the unchanged prompt and attachment.

A custom skill cannot connect directly to an SAP backend. Live retrieval uses the named SAP-published skill and your authorized access; the synthetic path makes no backend call. If live access or retrieval is unavailable, ask the facilitator for a supported option or use **Option A's synthetic CSV**. Do not retry failed backend calls or switch services. If `Excel` is unavailable, escalate to the facilitator; inspecting sample data or describing a workbook does **not** complete Option A.

<details>
<summary>Optional: catalog screenshot</summary>

This capture shows **Published by SAP**, not **Active Skills**. It shows `SAP S/4HANA Cloud Public Edition`, `SAP SuccessFactors HCM`, and `Word Documents` enabled; `Excel` is not visible. Enable the output skill your option needs and use **Active Skills** for the final readiness check, including your imported custom skill.

![Published by SAP catalog showing enabled business skills and Word Documents; Excel is not visible](images/04-01-active-skills.png)

</details>

## Choose one scenario

<details open>
<summary>Option A: SAP S/4HANA - Filtered Purchase Order Excel Report</summary>

### Option A contract

Ask for one specific purchasing organization, supplier or `all suppliers`, an inclusive purchase-order creation date range, currency, and report date. Use `YYYY-MM-DD` dates and ask for missing or invalid inputs.

For the live path, make **exactly one** `SAP S/4HANA Cloud Public Edition` detail request, filtered and sorted before retrieval, capped at 20 purchase orders. No separate count, pagination, retry, or alternate service. On an error, partial/truncated result, unsupported filter, or missing required field, explain the first problem and stop without a workbook. Do not silently switch to synthetic data.

Create `purchase-order-report.xlsx` with exactly these worksheets:

1. **`Summary`**: applied filters, report date, source, analyzed purchase-order count, and the 20-record limit. For live data, state that the result is bounded and may not represent all matches; do not claim a total matching count. For synthetic data, identify `Synthetic workshop CSV: purchase-orders.csv`, state that no live retrieval occurred, and make no SAP population or completeness claims.
2. **`Purchase Orders`**: exactly `Purchase Order`, `Supplier`, `Purchasing Organization`, `Creation Date`, `Currency`, in that order. One row per selected purchase order, sorted by creation date descending, then purchase-order identifier ascending, with at most 20 rows.

Keep identifiers unchanged and dates valid. Do not add monetary totals, status fields, or currency conversion. For zero matches, leave the table empty below its headers and put the zero-result note only on `Summary`.

### Live sample prompt

```text
Create a purchase-order Excel report for purchasing organization D3US, all suppliers, creation dates 2026-01-01 through 2026-10-20, currency EUR, with report date 2026-10-20.
```

Use facilitator-confirmed values if these are unsupported, then keep the request unchanged when retesting. A sample prompt is not evidence that your tenant is qualified.

### Synthetic fallback

Attach [purchase-orders.csv](sample-data/purchase-orders.csv) in a new conversation and use the prompt below. This is **invented workshop data**, not retrieved SAP data. Teach your skill to use the explicitly requested attached CSV instead of a business skill, apply the same filters, sort **all matching rows before taking at most 20**, and produce the same workbook contract with the synthetic source label in `Summary`. Only your custom skill and `Excel` are required under **Active Skills**.

```text
Use only the attached synthetic workshop CSV purchase-orders.csv; do not call SAP. Create a purchase-order Excel report for purchasing organization DEMO, all suppliers, creation dates 2026-01-01 through 2026-10-20, currency EUR, with report date 2026-10-20. Label the Summary source as Synthetic workshop CSV: purchase-orders.csv, state that no live retrieval occurred, and make no live completeness claims.
```

For this unchanged synthetic prompt, expect **20 report rows** from 21 matching rows in the 25-row file. The first identifiers are `DEMO-PO-020` and `DEMO-PO-021`; the last is `DEMO-PO-002`. This checks filtering and sorting before the limit, not live retrieval.

### Option A checklist

Open `purchase-order-report.xlsx` and confirm:

- the two worksheet names and five columns match the contract exactly;
- `Summary` matches the requested filters, report date, source, and actual analyzed row count;
- every row matches the filters, dates are valid, and sorting is correct;
- at most 20 purchase-order rows appear, with no message row in an empty table;
- no monetary totals, status fields, or currency conversions appear;
- live output discloses its bounded scope, or synthetic output is clearly labeled with no live-data claims.

<details>
<summary>Optional: compare with captured live examples</summary>

Wording, colors, and table widths may vary. Live records and counts also vary by identity and tenant. Required filenames, fields, dates, and sorting must still match the written contract.

![Captured S/4HANA response to the purchase-order report sample prompt](images/04-02-s4-purchase-order-response.png)

![Purchase-order workbook summary showing report filters and bounded retrieval limit](images/04-03-s4-purchase-order-summary.png)

![Before-fix purchase-order table with five columns and an incorrect date](images/04-04-s4-purchase-order-list.png)

The table above is a **before-fix** example: PO `4500078413` displays `1970-01-21`, outside the requested range. The [date-fix appendix](appendix-date-fix.md) shows the diagnosis, skill update, and retest. The captured count of 14 is illustrative, not an expected synthetic or live result.

The updated workbook below shows PO `4500078413` with Creation Date **`2026-03-13`**. The visible rows follow the required date-descending, purchase-order-ascending sort order. Use the checklist to verify your own workbook, including its `Summary` sheet.

![Updated purchase-order table showing PO 4500078413 with corrected Creation Date 2026-03-13](images/04-12-s4-updated-skill-purchase-order-list.png)

</details>
</details>

<details>
<summary>Option B: SAP SuccessFactors - Benefit-Plan Country Report</summary>

### Option B contract

Ask for a **country** and **report date** (`YYYY-MM-DD`). Retrieve authorized benefit-plan configuration with `SAP SuccessFactors HCM` and use `Word Documents` to create `benefit-plans-<country-slug>.docx`, for example `benefit-plans-germany.docx`.

- Ask for missing or invalid inputs. Include only plans matching the requested country; if country metadata is unavailable, use an exact country-name match in the plan name, not a partial, alias, or inferred regional match.
- Make exactly one retrieval call. If it fails, is incomplete, or returns no matching plans, explain the result and stop **without creating a document**. Do not retry or switch services.
- Use returned plan configuration only. Do not retrieve personal enrollments or compensation, or invent values.

Include exactly these four sections in order:

1. **Title:** `Benefit Plans - <Country>`.
2. **Report Scope:** country and report date.
3. **Plan Summary:** a table with `Plan Name`, `Benefit ID`, `Type`, `Amount`, `Currency`, `Frequency`, `Enrollment`, and `Status`, sorted alphabetically by plan name. Use `Not available` for missing values.
4. **Plan Details:** one subsection per plan in the same order, using available configuration details such as effective date, enrollment settings, or eligibility rules.

Do not add process commentary to the document.

### Option B sample prompt

```text
Create a SuccessFactors benefit-plan report for Germany with report date 2026-10-20.
```

Use a facilitator-confirmed country if Germany is unsupported, then keep your request unchanged when retesting. If no matching plans are returned, stop without a file; choose a supported option or Option A's synthetic path for the report-building exercise.

### Option B checklist

Open the generated Word file and confirm:

- the filename, country, and report date match your request;
- the four sections appear in order without extra process commentary;
- the summary has the specified columns and alphabetical plan order;
- each plan has a matching detail subsection using returned information only;
- all plans match the requested country, with no personal enrollment or compensation data.

<details>
<summary>Optional: compare with captured live examples</summary>

![SuccessFactors response showing the Germany benefit-plan summary](images/04-05-successfactors-benefit-plan-response.png)

![SuccessFactors response showing the Word download and report structure](images/04-06-successfactors-benefit-plan-download.png)

![Word report showing the Germany report scope and plan summary](images/04-07-successfactors-benefit-plan-summary.png)

![Word report showing the Car Allowance Germany plan details](images/04-08-successfactors-benefit-plan-details.png)

The captured run contains six plans. Your authorized data may differ; verify sections, columns, ordering, and returned values rather than copying that count or those amounts. Include only available fields in `Plan Details`, even where the screenshot displays an unavailable field. The written contract takes precedence.

</details>
</details>

<details>
<summary>Optional: improve with Joule or compare a reference skill</summary>

For a defect, ask Joule to explain it, attach your own `SKILL.md` or package, and ask for an update. Download, extract, and review the result before replacing the imported copy and retesting. The [date-fix appendix](appendix-date-fix.md) illustrates this process.

After testing your own skill, you may compare the completed [facilitator reference](facilitator-test-skills/README.md):

1. Choose [`s4-purchase-order-excel-report`](facilitator-test-skills/s4-purchase-order-excel-report/) or [`successfactors-benefit-plan-country-report`](facilitator-test-skills/successfactors-benefit-plan-country-report/) and follow [Importing a skill](../../README.md#importing-a-skill).
2. Disable your own version and enable only the reference plus the dependencies for your path. Confirm them under **Active Skills**.
3. Start a new **Agentic Thinking** conversation and run the same request and, for synthetic data, the same attachment. Download and check the reference file against the written contract.
4. Disable the reference before re-enabling and retesting your own version in another new conversation.

Do not enable both custom versions at once. If provenance is not visible, record `Not visible` and compare only observable behavior. A reference is not proof of live tenant qualification or a substitute for checking the file.

</details>

## Expected result

You built one custom skill and opened a report that meets its chosen contract. A labeled Option A synthetic report is a valid exercise result, but does not demonstrate SAP retrieval. If a required output capability is unavailable, ask the facilitator for help and do not claim the exercise complete.

Continue optionally to [Exercise 5 - Freestyle (stretch or take-home)](../ex5/README.md), or [return to the workshop overview](../../README.md).
