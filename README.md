# JW260 - Build Your First Skill in Joule: A Developer's Guide to Skill Creation

## Description

This repository contains the material for the SAP TechEd 2026 session JW260 - Build Your First Skill in Joule: A Developer's Guide to Skill Creation.

## Overview

In this hands-on session, you build progressively more capable Joule Work custom skills. You start by comparing skill descriptions and instructions, then add validated deterministic calculation, and finally prioritize synthetic sales-order exceptions with a read-only skill.

After completing the exercises, you will be able to:

- Explain how skill metadata and instructions affect discovery and behavior.
- Create the required skill folder and `SKILL.md` structure.
- Define required inputs, validation, output, and failure behavior.
- Use bundled references and scripts for deterministic processing.
- Keep custom skills within no-network, authorization, and read-only boundaries.

## Requirements

- Joule Work access with agentic thinking mode available.
- Access to **User menu > Explore Skills**.
- Permission to import and enable a custom skill, or access to skills preimported by the facilitator.
- A browser that can upload ZIP and CSV files.
- No credentials, tenant URLs, personal data, production identifiers, or real customer records in workshop files.

## Exercises

- [Getting Started and Exercise 1 - Compare Skill Behavior](exercises/ex0/)
  - Compare intentionally flawed skills with a recommended skill.
  - Improve one skill and retest the same prompts.
- [Exercise 2 - Gross Margin Calculator](exercises/ex1/)
  - Validate inputs and perform deterministic calculations.
  - Handle missing, invalid, and zero-revenue cases.
- [Exercise 3 - Sales Order Exception Prioritizer](exercises/ex2/)
  - Analyze supplied synthetic sales-order data.
  - Apply deterministic read-only prioritization rules.

Complete the exercises in order. Later exercises build on the metadata, validation, supporting-file, and safety concepts introduced earlier.

## JW260 Workshop Guide skill

The repository also includes the optional [`jw260-workshop-guide`](skills/jw260-workshop-guide/) support skill. It is not a separate exercise. Import and enable it if you want to ask Joule questions such as:

- `What are the three JW260 exercises?`
- `Help me get started with Exercise 2.`
- `Why is my skill ZIP rejected?`
- `What should I check when a skill is not selected?`
- `What is the fallback for Exercise 3?`

The guide explains workshop navigation, exercise goals, exact prompts, expected results, troubleshooting, and safety boundaries. It does not perform the calculation or sales-order analysis for you.

## Importing a skill

1. Open the exercise folder and identify the skill folder containing `SKILL.md`.
2. Create a ZIP containing the complete top-level skill folder, not only the files inside it.
3. Open **User menu > Explore Skills > Import** in Joule Work.
4. Import the ZIP.
5. Find the skill under **My Skills** and enable it.
6. Select agentic thinking mode.
7. Follow the prompts and expected results in the exercise README.

Example archive layout:

```text
workshop-greeter.zip
└── workshop-greeter/
    └── SKILL.md
```

## Safety boundaries

- Use only supplied synthetic data or data your workshop identity is authorized to read.
- Never add credentials, secrets, tenant URLs, personal data, or production customer records to a skill.
- Custom skills run without external network connectivity. Do not add HTTP or API calls.
- A custom skill does not connect directly to SAP S/4HANA. SAP data retrieval requires an available SAP-published capability and the signed-in user's authorization.
- Exercise 3 is read-only. Do not create, update, release, or delete SAP business data.
- If live retrieval is unavailable, use the supplied `open-sales-orders.csv` fixture. Never invent business records.

## Troubleshooting

| Problem | Recovery |
| --- | --- |
| Import control is missing | Use a facilitator-preimported skill. |
| ZIP is rejected | Confirm the archive contains one top-level skill folder with `SKILL.md` at its root. |
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
