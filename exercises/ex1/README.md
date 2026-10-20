# Exercise 1: Compare Skill Behavior

## Goal

Observe how skill descriptions and instructions affect routing and response reliability, then improve a flawed skill using evidence from Joule Work.

> [!warning] Teaching anti-pattern
> `broad-greeter` is an intentionally poor example created for this exercise. Do not copy it into production skills.

<!-- TEACHING ANTI-PATTERN: broad-greeter intentionally creates routing overlap. -->
<!-- TEACHING ANTI-PATTERN: broad-greeter intentionally leaves output behavior underspecified and inconsistent. -->

## Timebox: 18 minutes

- Observe: 6 minutes
- Diagnose: 4 minutes
- Improve: 4 minutes
- Retest: 4 minutes

## Before You Start

Create one ZIP for each top-level folder:

- `broad-greeter`
- `workshop-greeter`

Each archive must contain its named folder and that folder's `SKILL.md`. In Joule Work, use **Explore Skills > Import** to import both ZIPs, enable both skills on **My Skills**, and select agentic thinking mode.

## Observe - 6 Minutes

Run each exact prompt twice with both skills enabled:

1. `Welcome me to the Joule Work skills workshop. My name is NAME.`
2. `Hello, I am NAME. Tell me what I will learn in the Joule Work skills workshop.`
3. `Help me get started with the Joule Work skills workshop.`

After every run, record the routed skill shown by Joule and the visible response qualities. If your tenant does not expose the selected skill, enter `Not visible` and base the comparison on the response only.

### Observation Matrix

| Phase | Prompt | Run | Skill routed | Name used correctly | Three learning levels | Exact closing sentence | Concise and consistent | Other evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| All enabled | Welcome Priya | 1 |  |  |  |  |  |  |
| All enabled | Welcome Priya | 2 |  |  |  |  |  |  |
| All enabled | Mateo learning request | 1 |  |  |  |  |  |  |
| All enabled | Mateo learning request | 2 |  |  |  |  |  |  |
| All enabled | Getting started | 1 |  |  |  |  |  |  |
| All enabled | Getting started | 2 |  |  |  |  |  |  |
| Good only | Welcome Priya | 1 |  |  |  |  |  |  |
| Good only | Mateo learning request | 1 |  |  |  |  |  |  |
| Good only | Getting started | 1 |  |  |  |  |  |  |
| Improved skill | Assigned prompt | 1 |  |  |  |  |  |  |
| Improved skill | Assigned prompt | 2 |  |  |  |  |  |  |

The required closing sentence for comparison is: `Start with the smallest reliable skill, then add complexity one controlled step at a time.`

> [!note] Selection is not deterministic
> Skill selection can vary between runs, tenants, and surrounding conversation. A flawed skill is not guaranteed to fail on every prompt. Your evidence is the behavior observed across repeated prompts, not a promised routing result or guaranteed failure.

## Diagnose - 4 Minutes

Open both `SKILL.md` files and compare them with your observations.

- Identify description words that overlap with unrelated requests or with another skill.
- Identify instructions that leave the number, content, order, length, or closing of the response undefined.
- For each observed difference, cite one metadata or instruction line that could explain it.
- Decide whether your strongest evidence concerns routing, output reliability, or both.

## Improve - 4 Minutes

Improve `broad-greeter`.

Narrow its `description` and instructions to one distinct greeting use case that does not overlap with `workshop-greeter`. Add one explicit negative boundary. Define a reliable output contract covering name behavior, the exact number and content of learning items, maximum length, and closing sentence. Keep the folder name and metadata name unchanged.

Rebuild and re-import the `broad-greeter` ZIP, then enable it.

## Retest - 4 Minutes

1. Disable `broad-greeter` so only `workshop-greeter` remains enabled.
2. Run each of the three exact prompts once and complete the `Good only` rows.
3. Compare these results with the `All enabled` rows. Note what changed in routing and response qualities.
4. Disable `workshop-greeter` and enable only your improved `broad-greeter` skill.
5. Run the prompt most relevant to your change twice and complete the two `Improved skill` rows.
6. State one evidence-based improvement and one remaining uncertainty.

## Success Criteria

You have observed repeated behavior with competing skills, linked evidence to metadata or instructions, isolated the good skill for comparison, improved the flawed skill, and retested the change without treating routing as deterministic.

## Summary

You compared intentionally flawed and recommended skill designs, connected observed behavior to metadata and instructions, improved one skill, and retested it with the same prompts.

Continue to - [Exercise 2 - Gross Margin Calculator](../ex2/README.md)
