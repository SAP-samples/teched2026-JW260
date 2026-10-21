# JW260 Workshop Guide

## Workshop purpose

JW260 is a hands-on SAP TechEd 2026 session about building custom skills for Joule Work. Participants complete one readiness exercise followed by five progressive technical exercises:

0. Sign in, set up the workshop files, and verify readiness.
1. Compare a deliberately flawed skill with a recommended skill.
2. Build and test a validated gross-margin calculation skill.
3. Prioritize synthetic sales-order exceptions with deterministic, read-only rules.
4. Build and verify a custom skill for a defined S/4HANA, SuccessFactors, or Ariba outcome.
5. Design an original skill in a freestyle exercise.

Complete the exercises in order. Later exercises build on the metadata, validation, supporting-file, and safety concepts introduced earlier.

## Exercise 0 - Log In, Set Up, and Get Ready

Location: `exercises/ex0/`

Goal: sign in with the facilitator-assigned workshop identity, confirm Joule Work access, prepare the repository files, understand the required ZIP structure, and verify the import path before beginning the technical exercises.

Participants need:

- The workshop tenant URL and workshop identity supplied by the facilitator.
- Joule Work access with agentic thinking mode available.
- Access to **User menu > Explore Skills**.
- Permission to import and enable a custom skill, or access to facilitator-preimported skills.
- A browser that can upload ZIP and CSV files.
- This repository, downloaded or cloned locally.

Readiness flow:

1. Open the facilitator-supplied tenant URL and sign in with the assigned identity.
2. Confirm that Joule Work opens.
3. Open **User menu > Explore Skills > My Skills**.
4. Confirm that **Import** is available, or use facilitator-preimported skills.
5. Confirm that agentic thinking mode is available.
6. Confirm that `exercises/ex0/` through `exercises/ex5/` are present locally.
7. Review the required top-level-folder ZIP structure.

Never put tenant URLs, usernames, passwords, authentication screenshots, or personal data in repository files or workshop prompts. If sign-in or required controls are unavailable, show the visible error or UI to the facilitator rather than bypassing permissions.

To import a custom skill:

1. Identify the skill folder containing `SKILL.md`.
2. Create a ZIP containing the complete top-level skill folder, not only its contents.
3. Open **User menu > Explore Skills > Import**.
4. Import the ZIP.
5. Find the skill under **My Skills** and enable it.
6. Select agentic thinking mode before testing.

A valid simple archive looks like this:

```text
workshop-greeter.zip
└── workshop-greeter/
    └── SKILL.md
```

## Exercise 1 - Compare Skill Behavior

Location: `exercises/ex1/`

Skills:

- `broad-greeter` - deliberately flawed teaching artifact.
- `workshop-greeter` - recommended reference artifact.

Goal: observe how a broad description and vague instructions affect routing and output reliability, diagnose the defects, improve `broad-greeter`, and retest unchanged prompts.

Exact prompts:

1. `Welcome me to the Joule Work skills workshop. My name is NAME.`
2. `Hello, I am NAME. Tell me what I will learn in the Joule Work skills workshop.`
3. `Help me get started with the Joule Work skills workshop.`

The recommended skill should welcome the participant, list exactly three learning levels, use the prescribed closing sentence, and remain under 120 words. Compare only observable response qualities when provenance is unavailable. Do not use unrelated prompts whose answer may come from standard agentic reasoning and cannot be attributed to either skill.

Exercise flow:

1. Import and enable both skills.
2. Run each prompt twice and record visible behavior and provenance when available.
3. Compare both `SKILL.md` files.
4. Improve `broad-greeter` by narrowing its description, adding a negative boundary, and defining a reliable output contract.
5. Rebuild and re-import `broad-greeter`.
6. Isolate the recommended and improved skills in turn and retest unchanged prompts.

Routing is probabilistic. If provenance is unavailable, record `Not visible` and compare observable response qualities without claiming which skill ran.

## Exercise 2 - Gross Margin Calculator

Location: `exercises/ex2/`

Skill: `gross-margin-calculator`

Files to inspect:

- `SKILL.md`
- `references/formulas.md`
- `scripts/calculate_margin.py`

Base prompt:

`Calculate gross margin for revenue 125000 EUR and cost 87500 EUR.`

Expected result:

- Gross Profit: `37500.00 EUR`
- Gross Margin: `30.00%`
- Warning: none

Additional cases:

- Missing cost: ask for cost and do not invent it.
- Revenue zero and cost 500 EUR: gross profit `-500.00 EUR`, margin undefined, and a zero-revenue warning.
- Negative revenue or cost: reject the value.
- Mixed currencies: do not convert; request values in one currency.

If bundled script execution is unavailable, use the rules in `references/formulas.md` and state that the documented formula fallback was used.

## Exercise 3 - Sales Order Exception Prioritizer

Location: `exercises/ex3/`

Skill: `sales-order-exception-prioritizer`

Synthetic fixture: `exercises/ex3/sample-data/open-sales-orders.csv`

Live prompt:

`Use Sales Order Exception Prioritizer to rank my authorized sales-order exceptions as of 2026-10-07. Follow its bounded live-retrieval procedure and do not change any business data.`

For a live run, the skill counts authorized, incomplete orders in the window from 30 days before through 7 days after the analysis date. It reports the count briefly, retrieves at most 50 matching orders sorted by requested delivery date descending before limiting, and does not fetch additional pages. If more than 50 match, the result must disclose both the matching count and the analyzed count. If the capability cannot count, filter, sort, and limit before retrieval, use the synthetic fixture instead of an arbitrary first page.

For live credit status, do not interpret a raw `TotalCreditCheckStatus` code from memory. Retrieve its code-list text for the exact object-node value in the tenant and cross-check `TotalBlockStatus`. Map only unambiguous blocked/not-approved text to `true` and approved/released/not-relevant text to `false`. Keep missing, ambiguous, or conflicting values as `unknown`, award no credit-block points for them, and disclose the unknown count. Do not substitute a mapping from legacy `CMGST` or another status field.

Fallback prompt:

`Analyze the attached open-sales-orders.csv as of 2026-10-07 using Sales Order Exception Prioritizer. Do not change any business data.`

Expected result:

- Total records: `20`
- Critical: `5`
- High: `6`
- Medium: `5`
- Low: `4`
- Highest-ranked orders: `DEMO-1019` and `DEMO-1009`, score `130`, Critical
- Final statement: `No SAP business data was changed.`

The custom skill cannot connect directly to SAP S/4HANA. A tenant-confirmed SAP-published capability may retrieve data the signed-in user is authorized to access. If retrieval, authorization, handoff, or required fields are unavailable, use the synthetic CSV and never invent records.

## Exercise 4 - Build a Skill for a Line-of-Business Scenario

Location: `exercises/ex4/`

Goal: choose one predefined SAP S/4HANA, SAP SuccessFactors, or SAP Ariba outcome, build the custom skill manually or with Joule, and verify its generated report against the fixed output contract.

Agentic Thinking may complete a similar one-off request without a custom skill. The learning objective is to turn that ad hoc behavior into a reusable business procedure with consistent required inputs, safety boundaries, retrieval limits, filenames, and output structures. The SAP-published skill retrieves authorized data, the Office output skill creates the artifact, and the participant's custom skill defines how those capabilities are combined.

The S/4HANA option produces a filtered purchase-order Excel workbook, the SuccessFactors option produces a country-specific benefit-plan report in Word, and the Ariba option produces a five-slide requisition review PowerPoint. Each option defines required filters, report structure, sorting, and a verification checklist in `exercises/ex4/README.md`.

Before participants build or run the skill, they must enable the required business skill and output skill under **Explore Skills** and confirm both under **Active Skills**. Use `xlsx` for the S/4HANA option, `docx` for SuccessFactors, and `pptx` for Ariba. The S/4HANA option uses the facilitator-confirmed `s4hana-public-cloud` or `s4hana-private-cloud` skill; SuccessFactors uses `successfactors-hr`; the exact SAP Ariba skill must be confirmed in the workshop tenant.

The exact SAP-published skill name and fields depend on the workshop tenant. Do not invent a capability name or claim that the custom skill connects directly to an SAP backend. If the capability or data handoff is unavailable, choose another available scenario or use facilitator-approved synthetic data.

## Exercise 5 - Freestyle

Location: `exercises/ex5/`

Goal: independently define, build, test, and improve an original custom skill for a business use case and output of the participant's choice.

Participants define the purpose, success criteria, required inputs, output structure, validation, and missing-information behavior. They import the skill, compare its result with their own criteria, improve one aspect, and run it again.

For a Microsoft Office artifact, participants must enable the corresponding `docx`, `pptx`, or `xlsx` skill and confirm it under **Active Skills**, together with any required business skill.

Use only synthetic or authorized information. If the chosen output is unsupported, select a supported format or clearly state the environment limitation.

## Troubleshooting

### Import control is missing

Use a facilitator-preimported skill. Do not try to bypass permissions.

### ZIP is rejected

Confirm that:

- The ZIP contains one top-level folder.
- The folder name is lowercase and hyphenated.
- `SKILL.md` is at the root of that folder.
- The metadata `name` matches the folder name.
- The archive contains no `.DS_Store`, `__MACOSX`, caches, or nested duplicate folder.

### Skill is not selected

1. Confirm agentic thinking mode.
2. Confirm that the intended skill is enabled under **My Skills**.
3. Start a clean conversation when instructed by the exercise.
4. Retry the exact exercise prompt.
5. Record visible provenance or `Not visible`.

Do not repeatedly rewrite prompts to force a preferred route.

### Script does not execute

Treat runtime support as unavailable for that attempt. Use the exercise's formula, deterministic rules, or expected result fallback. Do not claim the script executed in Joule.

### Missing or malformed Exercise 3 data

Confirm all required columns exist and values use the expected format. Correct the supplied synthetic copy rather than guessing mappings or values.

### SAP capability or authorization is unavailable

Do not broaden access during the workshop. Use `open-sales-orders.csv`.

### Empty result

A valid zero-count result is acceptable. Use the synthetic fixture when records are needed to complete the scoring lesson.

## Safety boundaries

- Never place credentials, secrets, tenant URLs, personal data, or production customer records in workshop files or prompts.
- Custom skill scripts must not make HTTP or external API calls.
- Do not describe custom Python as direct SAP connectivity.
- Exercise 3 remains read-only. Do not create, update, release, or delete SAP business data.
- Never invent SAP records when retrieval fails.

## Escalation evidence

If a facilitator is needed, provide:

- Exercise number and current step.
- Exact prompt used.
- Skill names currently enabled.
- Whether agentic thinking mode is selected.
- Visible error text or observed response.
- Whether skill provenance is visible.
- File name and archive structure for import problems.
