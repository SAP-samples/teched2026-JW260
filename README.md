# JW260 - Build Your First Skill in Joule: A Developer's Guide to Skill Creation

## Description

This repository contains the material for the SAP TechEd 2026 session JW260 - Build Your First Skill in Joule: A Developer's Guide to Skill Creation.

## Overview

In this hands-on session, you build progressively more capable Joule Work custom skills. You start by comparing skill descriptions and instructions, add validated deterministic calculation, prioritize synthetic sales-order exceptions, and then design your own business and document-generation skills.

After completing the exercises, you will be able to:

- Explain how skill metadata and instructions affect discovery and behavior.
- Create the required skill folder and `SKILL.md` structure.
- Define required inputs, validation, output, and failure behavior.
- Use bundled references and scripts for deterministic processing.
- Keep custom skills within no-network, authorization, and read-only boundaries.
- Build a custom skill around an available SAP-published skill.
- Create a PowerPoint, Word, or Excel artifact with an original skill.

## Requirements

- Joule Work access with agentic thinking mode available.
- Access to **User menu > Explore Skills**.
- Permission to import and enable a custom skill, or access to skills preimported by the facilitator.
- A browser that can upload ZIP and CSV files.
- No credentials, tenant URLs, personal data, production identifiers, or real customer records in workshop files.

## Before You Start

1. Open the workshop tenant URL supplied by your facilitator.
2. Sign in with your assigned workshop identity.
3. Confirm that you can access **User menu > Explore Skills**.
4. Download or clone this repository.
5. Complete [Exercise 0 - Log In, Set Up, and Get Ready](exercises/ex0/) before beginning the technical exercises.


## Exercises

- [Exercise 0 - Log In, Set Up, and Get Ready](exercises/ex0/)
  - Sign in with the assigned workshop identity.
  - Verify access, import options, and workshop files.
- [Exercise 1 - Compare Skill Behavior](exercises/ex1/)
  - Compare intentionally flawed skills with a recommended skill.
  - Improve one skill and retest the same prompts.
- [Exercise 2 - Gross Margin Calculator](exercises/ex2/)
  - Validate inputs and perform deterministic calculations.
  - Handle missing, invalid, and zero-revenue cases.
- [Exercise 3 - Sales Order Exception Prioritizer](exercises/ex3/)
  - Analyze supplied synthetic sales-order data.
  - Apply deterministic read-only prioritization rules.
- [Exercise 4 - Build a Skill for a Line-of-Business Scenario](exercises/ex4/)
  - Choose a defined S/4HANA, SuccessFactors, or Ariba outcome.
  - Build the skill and verify its Excel, Word, or PowerPoint report.
- [Exercise 5 - Freestyle](exercises/ex5/)
  - Design an original skill for a business use case of your choice.
  - Define, build, test, and improve the result independently.

Complete the exercises in order. Later exercises build on the metadata, validation, supporting-file, and safety concepts introduced earlier.

## JW260 Workshop Guide skill

The repository also includes the optional [`jw260-workshop-guide`](skills/jw260-workshop-guide/) support skill. It is not a separate exercise. Import and enable it if you want to ask Joule questions such as:

- `What are the six JW260 exercises?`
- `Help me get ready with Exercise 0.`
- `Help me get started with Exercise 2.`
- `How do I import my skill?`
- `What should I check when a skill is not selected?`
- `What is the fallback for Exercise 3?`
- `How do I choose a scenario for Exercise 4?`
- `How do I get started with Exercise 5?`

The guide explains workshop navigation, exercise goals, exact prompts, expected results, troubleshooting, and safety boundaries. It does not perform the calculation or sales-order analysis for you.

## Importing a skill

1. Open the exercise folder and identify the skill folder containing `SKILL.md`.
2. For a simple skill, select its `SKILL.md` file. For a skill with supporting files, select the complete unzipped skill folder.
3. Open **User menu > Explore Skills > Import** in Joule Work.
4. Import the selected file or folder.
5. Find the skill under **My Skills** and enable it.
6. Select agentic thinking mode.
7. Follow the prompts and expected results in the exercise README.

Example skill folder layout:

```text
workshop-greeter/
└── SKILL.md
```


## Troubleshooting

| Problem | Recovery |
| --- | --- |
| Import fails | Import a `SKILL.md` file directly for a simple skill, or import the complete unzipped skill folder when it has supporting files. |
| Skill is not selected | Confirm agentic thinking mode and enabled status, then retry the exact exercise prompt. |
| Bundled script cannot run | Use the formulas or expected behavior documented in the exercise. |
| SAP capability or authorization is unavailable | Use the synthetic CSV in Exercise 3. |

## Contributing

Please read the [CONTRIBUTING.md](./CONTRIBUTING.md) to understand the contribution guidelines.

## Code of Conduct

Please read the [SAP Open Source Code of Conduct](https://github.com/SAP-samples/.github/blob/main/CODE_OF_CONDUCT.md).

## How to obtain support

Support for this repository is available during the SAP TechEd session for which the content was designed. Otherwise, request support through the repository's [Issues](https://github.com/SAP-samples/teched2026-JW260/issues) tab.

## License

Copyright 2026 SAP SE or an SAP affiliate company and teched2026-JW260 contributors. Please see our [LICENSE](LICENSE) for copyright and license information. Detailed information, including third-party components and their licensing and copyright information, is available through the [REUSE tool](https://api.reuse.software/info/github.com/SAP-samples/teched2026-JW260).
