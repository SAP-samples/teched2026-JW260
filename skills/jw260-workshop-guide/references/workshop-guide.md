# JW260 Workshop Guide

## How to use this reference

This bundled reference mirrors the participant instructions. Use it for workshop answers, not remembered earlier outlines. Repository paths point to files the participant can open; they are not files this imported guide can automatically access. If a current README excerpt differs, explain the discrepancy and ask for clarification. Use plain prose without em or en dashes. Distinguish required behavior, fixed synthetic expectations, captured examples, and actual participant observations.

## Workshop purpose

JW260 is a two-hour hands-on SAP TechEd 2026 session about building custom skills for Joule Work. There are **six exercises, numbered 0-5**: one readiness exercise, four core technical exercises, and one optional/take-home exercise. The workshop-guide skill is optional support, not a seventh exercise:

0. Sign in, set up the workshop files, and verify readiness.
1. Compare a deliberately flawed skill with a recommended skill.
2. Inspect and test a validated gross-margin calculation skill.
3. Prioritize synthetic sales-order exceptions with deterministic rules.
4. Build and verify a custom skill for a defined S/4HANA Excel or SuccessFactors Word report.
5. Optional/take-home: design an original skill in a freestyle exercise.

Complete the core exercises in order. Use the synthetic CSV path in Exercise 3 and one scenario in Exercise 4. Live Exercise 3, extra SAP exploration, and all optional comparisons/extensions are for early finishers or later. Protect time for participants to author their own skill in Exercise 4.

You can write `SKILL.md` manually or ask Joule to draft it from your requirements. Review the generated skill before importing and testing it.

## Exercise 0 - Log In, Set Up, and Get Ready

Location: `exercises/ex0/`

Goal: sign in with the facilitator-assigned workshop identity, confirm Joule Work access, prepare the repository files, understand the supported import formats, and verify the import path before beginning the technical exercises.

Participants need:

- The workshop tenant URL and workshop identity supplied by the facilitator.
- Joule Work access with agentic thinking mode available.
- Access to **User menu > Explore Skills**.
- Permission to import and enable a custom skill, or access to facilitator-preimported skills.
- A browser that can upload files, folders, and CSV files.
- This repository, downloaded or cloned locally.

Readiness flow:

1. Open the facilitator-supplied tenant URL and sign in with the assigned identity.
2. Confirm that Joule Work opens.
3. Open **User menu > Explore Skills > My Skills**.
4. Confirm that **Import** is available. If not, ask the facilitator about preimported examples or pairing with an authorized participant. A preimported skill supports observation, but does not replace an authorized way to test the participant's changes.
5. Confirm that agentic thinking mode is available.
6. Confirm that `exercises/ex0/` through `exercises/ex5/` are present locally.
7. Review whether to import a `SKILL.md` file directly or a complete unzipped skill folder. Extract a repository ZIP first; do not ZIP the skill for catalog import.
8. Follow **Step 5: First Interaction** in a fresh Agentic Thinking conversation. Send these prompts one at a time, in this order:
   - `Who are you and what can you help me with?`
   - `What are your limitations? What can't you do?`
   - `Can you do a quick calculation? If we raised 47 purchase orders at an average value of $12,400 each, what is the total spend?` Expected: $582,800.

The optional SAP exploration follows Julian's supplied prompt sequence. The current Exercise 0 README names `s4hana-public-cloud` and `successfactors-hr`. Enable them from **Published by SAP**, then confirm both under **Active Skills**. Ask the facilitator if they are unavailable. Published by SAP filters to SAP-published skills; imported custom skills are on My Skills.

S/4HANA exploration prompts:

- `Show me my last 5 purchase orders.`
- `Are there any open purchase orders over $50,000?`
- `Show me all open vendor invoices from last month.`

SuccessFactors exploration prompts:

- `What is my current job title and cost centre?`
- `Who is my manager and who reports to me?`
- `How many employees do we have in the Manufacturing division?`

Use only assigned workshop demo data. These are exploratory requests, not promises that every field or query is supported. If a required skill is unavailable, skip that exploration and continue to the Readiness Check.

Never put tenant URLs, usernames, passwords, authentication screenshots, or personal data in repository files or workshop prompts. If sign-in or required controls are unavailable, show the visible error or UI to the facilitator rather than bypassing permissions.

To import a custom skill:

1. Identify the skill folder containing `SKILL.md`.
2. For a simple skill, select its `SKILL.md` file. For a skill with supporting files, select the complete unzipped skill folder.
3. Open **User menu > Explore Skills > Import**.
4. Import the selected file or folder.
5. Find the skill under **My Skills** and enable it.
6. Confirm the intended custom, business, and output skills under **Active Skills**. Start a new conversation and select agentic thinking mode before testing.

For folder import, select the skill folder itself: the folder that directly contains `SKILL.md`. Do not select its parent exercise folder, the repository root, or only `scripts/` or `references/`. Import each skill separately. In Exercise 1, import `exercises/ex1/broad-greeter/` and `exercises/ex1/workshop-greeter/` in two separate imports, or select each skill's `SKILL.md` directly. Never select their shared `exercises/ex1/` parent folder. In Exercise 2, select `exercises/ex2/gross-margin-calculator/`, not `exercises/ex2/`.

This file/folder procedure matches the captured workshop tenant dialog. Supporting files must be no more than one subfolder level below the skill root.

To replace an imported skill, keep and review the updated local source, disable and remove the old imported copy, then import the replacement. If removal is unavailable, ask the facilitator rather than creating competing copies. Check the imported details contain the changes, enable the new version, and retest unchanged prompts in fresh conversations.

A valid simple skill folder looks like this:

```text
workshop-greeter/
└── SKILL.md
```

## Exercise 1 - Compare Skill Behavior

Location: `exercises/ex1/`

Skills:

- `broad-greeter` - deliberately flawed teaching artifact.
- `workshop-greeter` - recommended reference artifact.

Goal: compare the behavior of `broad-greeter` and `workshop-greeter`, improve `broad-greeter`, and retest unchanged prompts.

A skill's `description` helps Joule decide when to use it; its instructions define what Joule should do. Better means a clearer purpose and more predictable response structure, not simply a friendlier greeting.

Exact prompts:

1. `Welcome me to the Joule Work skills workshop. My name is NAME.`
2. `Hello, I am NAME. Tell me what I will learn in the Joule Work skills workshop.`
3. `Help me get started with the Joule Work skills workshop.`

Replace `NAME` with a workshop alias and keep it the same across versions. Run each numbered prompt in its own new conversation in agentic thinking mode, including when retesting; otherwise the missing name could be remembered from an earlier prompt. The third prompt omits the name; if Joule asks for it, provide it and compare the completed response. Asking for missing information is not a failure.

Compare name handling, exactly six exercise bullets in order (0 readiness, 1 compare/improve, 2 inspect/test the calculator, 3 synthetic order scoring, 4 build one business report, 5 optional freestyle), correct optional scope, the closing sentence `Start with the smallest reliable skill, then add complexity one controlled step at a time.`, and a response under 120 words. The response must use plain language with no emoji or em/en dashes. Use colons or full stops between bullet labels and explanations. The old three-level greeting screenshot is labeled historical, not the current expected overview. Compare only observable response qualities when provenance is unavailable. Do not use unrelated prompts whose answer may come from standard agentic reasoning and cannot be attributed to either skill.

Exercise flow:

1. First inspect `workshop-greeter/SKILL.md`: the `---` delimiters enclose YAML metadata, `name` and `description` identify/select the skill, and `## Instructions` defines its procedure. Import `broad-greeter` and `workshop-greeter` separately, selecting each `SKILL.md` or its individual skill folder, never the shared `ex1/` parent folder. Enable only `broad-greeter`. Keep `workshop-greeter`, `jw260-workshop-guide`, and other custom workshop skills disabled. Start a new conversation in agentic thinking mode.
2. Run the three exact prompts, each in its own new Agentic Thinking conversation, and record the responses. Then disable `broad-greeter`, enable only `workshop-greeter`, and run each unchanged prompt in its own new conversation. Compare the responses and record provenance when visible. Optionally repeat one prompt with each skill to check consistency.
3. Open both `SKILL.md` files and use `workshop-greeter` as a reference. Narrow `broad-greeter`'s description to workshop greetings and add two clear response rules, such as one bullet for each of the six exercises with optional scope and the prescribed closing sentence. Follow the reference's plain style without em dashes. Keep its folder name and metadata name unchanged. Participants may edit manually or ask Joule to help draft the changes, then review them.
4. Replace the imported `broad-greeter` using the shared replacement procedure above; a local edit alone does not update Joule.
5. Disable `workshop-greeter`, enable only the improved `broad-greeter`, and retest each of the three unchanged prompts in its own fresh Agentic Thinking conversation. Compare with both earlier sets of responses.

The subsequent comparison with `jw260-workshop-guide/SKILL.md` is optional enrichment, not a requirement for completing Exercise 1.

Routing is probabilistic. If provenance is unavailable, record `Not visible` and compare observable response qualities without claiming which skill ran.

## Exercise 2 - Gross Margin Calculator

Location: `exercises/ex2/`

Skill: `gross-margin-calculator`

Files to inspect:

- `SKILL.md`
- `references/formulas.md`
- `scripts/calculate_margin.py`

Identify the instruction-to-script handoff: the skill collects inputs, saves a JSON file, and runs the Python script. The reference defines the disclosed formula fallback. Import the complete `gross-margin-calculator` folder, enable it, and disable both greeters.

Base prompt:

`Calculate gross margin for revenue 125000 EUR and cost 87500 EUR.`

Expected result:

- Gross Profit: `37500.00 EUR`
- Gross Margin: `30.00%`
- Inputs: revenue `125000 EUR`; cost `87500 EUR`
- Warning: `None`

Run each case in its own new Agentic Thinking conversation; answer any clarification in that same conversation.

- `Calculate gross margin for revenue 125000 EUR.` Expected: ask for cost and do not invent it.
- `Calculate gross margin for revenue 0 and cost 500 EUR.` Expected: gross profit `-500.00 EUR`, margin undefined, and a zero-revenue warning.
- `Calculate gross margin for revenue -10 EUR and cost 5 EUR.` Expected: reject negative revenue.
- `Calculate gross margin for revenue 100 USD and cost 60 EUR.` Expected: do not convert; request values in one currency.

If bundled script execution is unavailable, the calculator uses the rules in its bundled `references/formulas.md` and states that the formula fallback was used. The repository path is `exercises/ex2/gross-margin-calculator/references/formulas.md`; that file is not bundled with this guide. Its formulas are gross profit = revenue - cost and gross margin percent = (revenue - cost) / revenue * 100, with two-decimal half-up rounding and undefined margin at zero revenue. Negative revenue/cost are rejected and currencies must match.

The optional target-margin extension adds an input below 100 percent and calculates required revenue = cost / (1 - target margin percent / 100). Label it separately from the base output, replace the edited skill, and retest. This is not a required part of the core calculator exercise.

## Exercise 3 - Sales Order Exception Prioritizer

Location: `exercises/ex3/`. Import the complete unzipped `sales-order-exception-prioritizer/` folder, including its script, and enable it under **My Skills**. Start a fresh **Agentic Thinking** conversation and confirm it under **Active Skills**. No business skill is needed for the core CSV path.

### Core: supplied CSV first

Attach `exercises/ex3/sample-data/open-sales-orders.csv`. It is supplied separately, not bundled inside the imported skill.

`Use Sales Order Exception Prioritizer to rank all rows in the attached open-sales-orders.csv using analysis date 2026-10-07. Use the CSV only; do not retrieve backend data.`

Score all supplied rows. The fixture deliberately includes completed orders and dates outside the live window to test boundaries; do not apply live filters to it. Accepted delivery statuses are `Open`, `Partially Delivered`, and `Complete`, ignoring case and surrounding whitespace. Reject unknown statuses instead of treating them as incomplete.

Workshop scoring:

- Verified credit block +50; delivery block +40.
- Incomplete delivery and overdue requested date +30; otherwise a date from the analysis date through 7 days later, inclusive, +20.
- Raw net value at least 50000 in the record's own currency +10. This is not an equivalent monetary threshold across currencies; preserve currencies and do not convert or sum mixed values.
- Complete orders earn neither date rule, but can earn block/value points. Unknown credit earns no credit-block points.
- Critical ≥70; High 40-69; Medium 20-39; Low 0-19.
- Sort by score descending, requested date ascending, then sales-order identifier ascending. Show the top 10 and provide the full CSV when supported.

Expected fixture result: **20** analyzed; **Critical 5, High 6, Medium 5, Low 4**; unknown credit **0**. Leaders: `DEMO-1019` **130**, `DEMO-1009` **130**, `DEMO-1003` **90**. Explain one result: `DEMO-1019` has 50 credit + 40 delivery + 30 overdue + 10 value = 130. It precedes the tied `DEMO-1009` because its requested date is earlier.

If execution is unavailable, stop and offer only a labeled reference walkthrough of these rules and expected fixture results. Do not claim the script ran, fabricate a download, or call reference totals newly computed results. An executed analysis remains blocked.

### Optional: facilitator-confirmed live path

Only attempt the live path after the facilitator confirms the capability, authorization, usable fields and status mappings, server-side count/filter/sort/limit, data handoff, and runtime. Enable the business and custom skills under **Active Skills**.

`Use Sales Order Exception Prioritizer to rank my authorized sales-order exceptions using analysis date 2026-10-07. Follow its bounded live-retrieval procedure using current delivery and credit statuses.`

Count authorized incomplete orders with requested delivery dates from 30 days before through 7 days after the analysis date. For the prompt, this is 2026-09-07 through 2026-10-14 inclusive. Retrieve at most 50 orders sorted by requested date descending, then order identifier ascending, in SAP before limiting. Disclose matching versus analyzed counts; do not fetch more pages, retry failed retrievals, or probe alternate services. A zero count skips detail retrieval and produces a valid empty result. Current statuses plus an analysis date are not a historical snapshot.

Use only qualified meanings for the exact delivery-status field and tenant. If they cannot be mapped to accepted statuses, stop rather than silently omitting the incomplete-delivery filter. Interpret `TotalCreditCheckStatus` only from its exact tenant code-list text, with `TotalBlockStatus` as a consistency check. Never borrow `CMGST` or another field's mapping. Ambiguous credit meanings remain `unknown`, earn no credit points, and are disclosed. An explicit retrieval failure is a stop condition, not an unknown value to hide.

If the live path is unsupported or fails, stop that run and use the explicit CSV path. Never invent SAP records.

## Exercise 4 - Build a Skill for a Line-of-Business Scenario

Location: `exercises/ex4/`. Choose one defined report, build the custom skill manually or with Joule, and verify its opened file. The README has shared steps first, expandable Option A/B contracts, and optional screenshot/reference comparisons.

Agentic Thinking may produce a similar file from a one-off request. The custom skill defines a reusable procedure with consistent required inputs, source selection, validation, retrieval limits, filenames, and structure. A business skill supplies authorized live data; `xlsx` or `docx` creates the file. Custom code cannot connect directly to SAP.

Dependencies under **Active Skills**, together with the participant's custom skill:

- Option A live: `s4hana-public-cloud` and `xlsx`.
- Option A synthetic: `xlsx` only; do not call a backend.
- Option B live: `successfactors-hr` and `docx`.

The retained catalog screenshot shows **Published by SAP**, not Active Skills, and does not show `xlsx`. Do not use it as proof of readiness. Start a new conversation with Agentic Thinking selected for each test or retest.

### Option A: purchase-order Excel report

Ask for one purchasing organization, supplier or `all suppliers`, inclusive creation-date range, currency, and report date. Validate dates as `YYYY-MM-DD`. Output `purchase-order-report.xlsx`:

- `Summary`: filters, report date, source, analyzed count, and 20-record limit. Disclose bounded live scope without a matching-population count, or label the synthetic source with no live retrieval/completeness claims.
- `Purchase Orders`: exactly `Purchase Order`, `Supplier`, `Purchasing Organization`, `Creation Date`, `Currency`; matching rows sorted by creation date descending and identifier ascending, at most 20.
- Preserve identifiers and valid dates. No monetary totals, status fields, or currency conversion. For zero matches, the data table is empty below headers; any message belongs on Summary.

Live prompt:

`Create a purchase-order Excel report for purchasing organization D3US, all suppliers, creation dates 2026-01-01 through 2026-10-20, currency EUR, with report date 2026-10-20.`

Use supported facilitator-confirmed values if necessary, then retest unchanged. Live retrieval is exactly one `s4hana-public-cloud` detail request with filters and sorting applied before the 20-row limit. No count request, pagination, retry, or alternate service. Stop on failure, partial/truncated response, unsupported filter, or missing required field; do not silently substitute synthetic data.

Synthetic fallback: attach `exercises/ex4/sample-data/purchase-orders.csv`. This is deliberately synthetic workshop data with the same five columns, not retrieved SAP data. Filter all supplied rows, sort all matches before limiting, and use the same workbook contract.

`Use only the attached synthetic workshop CSV purchase-orders.csv; do not call SAP. Create a purchase-order Excel report for purchasing organization DEMO, all suppliers, creation dates 2026-01-01 through 2026-10-20, currency EUR, with report date 2026-10-20. Label the Summary source as Synthetic workshop CSV: purchase-orders.csv, state that no live retrieval occurred, and make no live completeness claims.`

With the unchanged synthetic prompt, 25 supplied rows contain 21 matches; the report selects 20. First identifiers: `DEMO-PO-020`, `DEMO-PO-021`; last: `DEMO-PO-002`. These are fixture expectations, not live counts.

### Option B: benefit-plan Word report

Ask for country and report date (`YYYY-MM-DD`). Retrieve matching authorized benefit-plan configuration exactly once with `successfactors-hr`. When country metadata is absent, only an exact requested-country name match in the plan name is allowed; no aliases, partial, or inferred regional matching. Errors, incomplete results, or no matching plans stop the run without a document or retry. Do not retrieve personal enrollment or compensation data.

`Create a SuccessFactors benefit-plan report for Germany with report date 2026-10-20.`

Use a supported facilitator-confirmed country if necessary, then retest unchanged. Output `benefit-plans-<country-slug>.docx`, e.g. `benefit-plans-germany.docx`, with four sections in order:

1. `Benefit Plans - <Country>`.
2. `Report Scope`: country and report date.
3. `Plan Summary`: `Plan Name`, `Benefit ID`, `Type`, `Amount`, `Currency`, `Frequency`, `Enrollment`, `Status`, alphabetically by plan name; `Not available` for missing values.
4. `Plan Details`: one matching subsection per plan in the same order, using returned configuration only.

No extra process commentary or invented values. The document describes plan configuration, not personal entitlement or enrollment.

### Verification and recovery

Download and open the output. Check filenames, section/sheet names, columns, filters, dates, ordering, actual row counts, and source labels against the chosen contract. Screenshots are optional examples; the written checklist takes precedence. The original S/4HANA table image is a before-fix example with an out-of-range date. The README and appendix also include `04-12-s4-updated-skill-purchase-order-list.png`, showing PO `4500078413` with the corrected Creation Date `2026-03-13` and the required visible sort order. The appendix follows the diagnosis, updated package, and opened table; the `Summary` sheet still needs separate checking because it is not visible in that capture.

If a check fails, ask Joule to explain it, attach the source skill for revision, review the changes, and use the shared replacement procedure before rerunning the same prompt and attachment in a fresh conversation.

If live access is blocked, choose another supported option or explicitly start Option A's synthetic path. There is no SuccessFactors fixture. Do not use Exercise 3's sales-order CSV here. If the required Office output skill is unavailable, ask the facilitator and record the artifact objective as blocked; a chat summary or sample inspection is not a completed report.

Only after building and testing their own skill may participants optionally import a completed reference from `exercises/ex4/facilitator-test-skills/`. Disable their own version, enable the reference plus the chosen path's dependencies, and test in a fresh Agentic Thinking conversation using the same prompt and attachment. Compare against the same checklist, then disable the reference before restoring their own skill. If provenance is hidden, record `Not visible`; never enable both custom versions together or treat the reference as proof of live qualification.

## Exercise 5 - Freestyle (optional / take-home)

Location: `exercises/ex5/`

Goal: independently define, build, test, and improve an original custom skill for a business use case and output of the participant's choice. This is not required for completing the two-hour core. A conversational response, analysis, or file can be a valid outcome.

Participants define the purpose, success criteria, required inputs, output structure, validation, and missing-information behavior. They import the skill, compare its result with their own criteria, improve one aspect, and run it again.

For a Microsoft Office artifact, participants must enable the corresponding `docx`, `pptx`, or `xlsx` skill and confirm it under **Active Skills**, together with any required business skill.

Use only synthetic or authorized information. If the chosen output is unsupported, select a supported format or clearly state the environment limitation.

## Troubleshooting

### Import control is missing

Ask the facilitator about preimported examples or pairing with an authorized participant. Observing a preimported example is not the same as testing an edited or newly authored skill. Do not try to bypass permissions.

### Import fails

Confirm that:

- A simple skill is selected as its `SKILL.md` file.
- A skill with supporting files is selected as its complete unzipped folder.
- The selected folder directly contains `SKILL.md`; it is not a parent exercise folder containing multiple skills. Exercise 1 needs separate imports for `broad-greeter/` and `workshop-greeter/`, not one upload of `ex1/`.
- The folder name is lowercase and hyphenated.
- `SKILL.md` is at the root of that folder; supporting files are at most one subfolder level below it.
- The metadata `name` matches the folder name.
- The folder contains no `.DS_Store`, caches, secrets, or nested duplicate skill folder.

### Skill is not selected

1. Confirm agentic thinking mode.
2. Confirm that the intended skill is enabled under **My Skills**.
3. Start a clean conversation when instructed by the exercise.
4. Retry the exact exercise prompt.
5. Record visible provenance or `Not visible`.

Do not repeatedly rewrite prompts to force a preferred route.

### Script does not execute

Exercise 2: use and disclose the documented formula fallback. Exercise 3: stop execution and offer a labeled reference-only walkthrough of the rules and expected fixture results. Never fabricate an executed analysis or download. If script execution is essential to a participant-authored skill, report the blocker and ask the facilitator.

### Missing or malformed Exercise 3 data

Required columns: `sales_order`, `customer`, `net_value`, `currency`, `requested_delivery_date`, `overall_delivery_status`, `delivery_block`, `credit_block`. Dates use `YYYY-MM-DD`; delivery status is `Open`, `Partially Delivered`, or `Complete` (case-insensitive). Block indicators accept `true`/`false`, `yes`/`no`, or `1`/`0`; credit may also be explicitly `unknown`/`unresolved`. Correct the supplied synthetic copy rather than guessing mappings or values. The exercise script is `exercises/ex3/sales-order-exception-prioritizer/scripts/prioritize_orders.py`.

### SAP capability or authorization is unavailable

Do not broaden access or retry failed retrievals. Exercise 3: use its explicit `open-sales-orders.csv` path. Exercise 4: choose a supported option or explicitly select Option A with its separate `purchase-orders.csv` attachment. If the required output skill is also unavailable, escalate; the report objective remains blocked.

### Empty result

Exercise 3: a valid empty input or zero live count produces a zero-count summary and CSV headers without data rows. Exercise 4 Option A: an empty Purchase Orders table with the zero-result note on Summary. Exercise 4 Option B: no matching plans means stop without creating a document. Use the appropriate synthetic path when populated records are needed.

## Safety boundaries

- Never place credentials, secrets, tenant URLs, personal data, or production customer records in workshop files or prompts.
- Custom skill scripts must not make HTTP or external API calls.
- Do not describe custom Python as direct SAP connectivity.
- Agentic Thinking backend access is read-only in the current workshop environment. Mention this only when relevant; do not make backend-write warnings or no-data-changed closing statements part of every exercise response.
- Never invent SAP records when retrieval fails.

## Escalation evidence

If a facilitator is needed, provide:

- Exercise number and current step.
- Exact prompt used.
- Skill names currently enabled.
- Whether agentic thinking mode is selected.
- Visible error text or observed response.
- Whether skill provenance is visible.
- Selected file/folder name and structure for import problems.
