# JW260 - Build Your First Skill in Joule: A Developer's Guide to Skill Creation

## Description

This repository contains the material for the two-hour SAP TechEd 2026 hands-on session JW260 - Build Your First Skill in Joule: A Developer's Guide to Skill Creation.

## Overview

Start by improving a simple skill, inspect a validated calculation skill, and score synthetic sales-order exceptions. Then build your own skill for a defined business report.

You can write `SKILL.md` manually or ask Joule to draft it from your requirements. Review the generated skill before importing and testing it. You do not need to install Python locally; the calculation exercises use scripts bundled with the skills.

After the core exercises, you will be able to:

- Explain how skill metadata and instructions affect selection and behavior.
- Create a skill folder with `SKILL.md` and optional supporting files.
- Define required inputs, validation, output, and failure behavior.
- Use bundled references and scripts for repeatable processing.
- Distinguish authorized SAP data retrieval from custom processing without network access.
- Build and verify a custom skill that creates an Excel or Word report.

## Requirements

- Joule Work access with **Agentic Thinking** available.
- Access to **User menu > Explore Skills**, with permission to import and enable custom skills.
- A browser that supports file and folder uploads and file downloads.
- A plain-text editor if you want to edit `SKILL.md` manually.
- Only supplied synthetic data or authorized workshop demo data. Do not upload credentials, tenant URLs, personal data, or production customer records.

In the current workshop environment, Agentic Thinking provides read-only backend access; backend updates are not supported.

If import permission is missing, ask the facilitator about preimported skills or pairing with an authorized participant. A preimported example supports observation, but does not replace testing your own changes.

## Before You Start

1. Open the workshop tenant URL supplied by your facilitator and sign in with your assigned identity.
2. Download or clone this repository. Extract it first if you downloaded a repository ZIP.
3. Complete [Exercise 0 - Log In, Set Up, and Get Ready](exercises/ex0/).

## Exercises

**Core session:** Exercise 0 for readiness, followed by Exercises 1-4 in order. Use the synthetic CSV path in Exercise 3 and complete one scenario in Exercise 4. Optional sections are for early finishers or later exploration.

| Exercise | What you will do |
| --- | --- |
| [0 - Log In, Set Up, and Get Ready](exercises/ex0/) | Check access and prepare the files. |
| [1 - Compare Skill Behavior](exercises/ex1/) | Compare one vague skill with a reference, improve it, and retest. |
| [2 - Gross Margin Calculator](exercises/ex2/) | Inspect the instruction-to-script handoff and test input validation. |
| [3 - Sales Order Exception Prioritizer](exercises/ex3/) | Score synthetic orders and explain the result. Live retrieval is optional. |
| [4 - Build a Skill for a Line-of-Business Scenario](exercises/ex4/) | Choose an S/4HANA Excel report or SuccessFactors Word report, then build and verify your own skill. A synthetic purchase-order path is available if live retrieval is blocked. |
| [5 - Freestyle (optional / take-home)](exercises/ex5/) | Design an original skill and define your own success criteria. |

> [!NOTE]
> **Check content, not every pixel**
> Wording and formatting may differ from the screenshots. Required values, filenames, sections, sorting, and safety boundaries must still match the written checklist. Live records can differ by workshop identity; synthetic examples have fixed expected results.

## JW260 Workshop Guide skill

The optional [`jw260-workshop-guide`](skills/jw260-workshop-guide/) support skill explains navigation, exercise prompts, expected results, and troubleshooting. Import its complete folder and enable it when you need help. Keep it disabled during Exercise 1 so it does not compete with the greeters.

Try `Help me get started with Exercise 2.`, `How do I replace my imported skill?`, or `Which exercises are optional?`

The guide explains the next step; it does not perform the exercise's business work for you.

## Importing a skill

These instructions match the file/folder import dialog captured in the workshop tenant. Do not ZIP a skill for this import procedure.

1. Open **User menu > Explore Skills > Import**.
2. For a simple skill, choose its `SKILL.md` file. For a skill with supporting files, choose the complete unzipped skill folder.
3. Ensure `SKILL.md` is at the folder root. Keep supporting files in one level of subfolders, as required by the captured dialog.
4. Import, find the skill under **My Skills**, and enable it.
5. Confirm the custom skill and any required business/output skills under **Active Skills**.
6. Start a new conversation, select **Agentic Thinking**, and follow the exercise README.

> [!IMPORTANT]
> **Select one skill, not its parent exercise folder.** For folder import, select the folder that directly contains `SKILL.md`, including its supporting files. Do not select `exercises/`, `ex1/`, `ex2/`, the repository root, or only `scripts/` or `references/`. Import each skill separately. In Exercise 1, select `broad-greeter/` for one import and `workshop-greeter/` for the other, or select each skill's `SKILL.md` directly.

Example:

```text
exercises/ex1/                  <- Do not select this parent folder
├── broad-greeter/              <- Select this folder for the first import
│   └── SKILL.md
└── workshop-greeter/           <- Select this folder for the second import
    └── SKILL.md
```

## Replacing an imported skill

Editing a local file does not update the imported copy.

1. Save and review your updated local `SKILL.md` and supporting files. Keep this source copy.
2. Disable the old imported custom skill and remove that copy from the catalog before importing its replacement. If the removal action is unavailable, ask the facilitator rather than creating competing copies.
3. Import the updated file or complete folder using the procedure above. Open its details to check that the changes are present, then enable it.
4. Keep competing custom versions disabled. Start a new conversation in **Agentic Thinking**, rerun the same prompt, and verify the result.

## Troubleshooting

| Problem | Recovery |
| --- | --- |
| Import fails | Select one skill folder that directly contains `SKILL.md`, not its parent exercise folder. Import each skill separately; check supporting-file depth and absence of caches or `.DS_Store`. |
| Skill is not selected | Check mode and enabled status. Start a fresh conversation and retry the exercise prompt; do not assume which skill ran if provenance is hidden. |
| Script cannot run | Exercise 2 has a disclosed formula fallback. In Exercise 3, stop and inspect the rules and expected fixture results with the facilitator; do not call this an executed analysis. |
| Live SAP retrieval is unavailable | Exercise 3: use its sales-order CSV. Exercise 4: choose another supported option or its synthetic purchase-order path. Never substitute one exercise's dataset for another. |
| Office file cannot be created | Confirm `xlsx` or `docx` under **Active Skills**. If unavailable, ask the facilitator; do not claim the artifact was created. |

## Further reading

- [Joule Work Skills](https://help.sap.com/docs/joule/joule-work-621104a90a01407fbb2d1613db39a54d/skills?version=CLOUD&ai=true)
- [Skill Structure and Best Practices](https://help.sap.com/docs/joule/joule-work-621104a90a01407fbb2d1613db39a54d/skill-structure-and-best-practices?version=CLOUD&ai=true)

## Contributing

Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for the contribution guidelines.

## Code of Conduct

Please read the [SAP Open Source Code of Conduct](https://github.com/SAP-samples/.github/blob/main/CODE_OF_CONDUCT.md).

## How to obtain support

Support for this repository is available during the SAP TechEd session for which the content was designed. Otherwise, request support through the repository's [Issues](https://github.com/SAP-samples/teched2026-JW260/issues) tab.

## License

Copyright 2026 SAP SE or an SAP affiliate company and teched2026-JW260 contributors. Please see our [LICENSE](LICENSE) for copyright and license information. Detailed information, including third-party components and their licensing and copyright information, is available through the [REUSE tool](https://api.reuse.software/info/github.com/SAP-samples/teched2026-JW260).
