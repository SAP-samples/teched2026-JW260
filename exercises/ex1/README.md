# Exercise 1: Compare Skill Behavior

## Goal

Compare a vague skill with a more clearly defined skill, then improve the vague skill and test it again.

A skill's `description` helps Joule decide when to use it. Its instructions define what Joule should do. Here, **better** means a clearer purpose and a response that consistently follows the intended structure, not simply a friendlier answer.

> [!WARNING]
> **Teaching anti-pattern**
> `broad-greeter` is an intentionally poor example created for this exercise. Do not copy it into production skills.

<!-- TEACHING ANTI-PATTERN: broad-greeter intentionally creates routing overlap. -->
<!-- TEACHING ANTI-PATTERN: broad-greeter intentionally leaves output behavior underspecified and inconsistent. -->

## Before You Start

Import each top-level skill folder unzipped:

- `broad-greeter`
- `workshop-greeter`

Each folder must contain its named `SKILL.md`. In Joule Work, use **Explore Skills > Import** to import both folders. Before testing, disable `jw260-workshop-guide` and any other custom workshop skills. Enable only `broad-greeter` on **My Skills** and leave `workshop-greeter` disabled. Start a new conversation and select agentic thinking mode.

> [!IMPORTANT]
> Keep `jw260-workshop-guide` disabled throughout Exercise 1. Re-enable it after completing the exercise when you need workshop navigation or troubleshooting help.

After import, both custom skills appear on **My Skills**:

![My Skills showing the imported broad-greeter and workshop-greeter cards](images/01-01-imported-skills.png)

Test one skill at a time: **broad-greeter first, then workshop-greeter**. A blue toggle indicates an enabled skill. Start a new conversation whenever you switch skills so the earlier responses do not influence the comparison.

## Observe

With only `broad-greeter` enabled, run these exact prompts. Replace `NAME` with your name and use the same name in both skill runs.

1. `Welcome me to the Joule Work skills workshop. My name is NAME.`
2. `Hello, I am NAME. Tell me what I will learn in the Joule Work skills workshop.`
3. `Help me get started with the Joule Work skills workshop.`

Record the responses. Then disable `broad-greeter`, enable only `workshop-greeter`, start a new conversation in agentic thinking mode, and run the same three prompts unchanged.

The third prompt does not provide a name. If Joule asks for your name, provide it and compare the completed response. Asking for missing information is not a failure.

Use this table to compare both skills:

| Check | What to look for |
| --- | --- |
| Name handling | Uses the supplied name and asks when it is missing. |
| Learning content | Exactly three bullets covering skill metadata and routing, validated business calculations, and SAP data analysis with a bundled Python script. |
| Ending | Uses the specified closing sentence below. |
| Length | Stays under 120 words. |

If Joule shows the selected skill, note it; otherwise record `Not visible` and compare the responses only. Optionally repeat one prompt with each skill to check consistency.

The required closing sentence for comparison is: `Start with the smallest reliable skill, then add complexity one controlled step at a time.`

The recommended skill should produce the three learning levels and exact closing sentence. Compare it with the earlier `broad-greeter` responses rather than relying on competition between enabled skills to expose a difference.

![Workshop greeting response with three learning levels and the required closing sentence](images/01-03-workshop-greeting-result.png)

> [!NOTE]
> **Selection is not deterministic**
> Enabling one custom skill at a time makes the comparison clearer, but does not guarantee that Joule selects it. A flawed skill may still produce a reasonable answer. Compare observed behavior without assuming a guaranteed failure or claiming selection when it is not visible.

## Improve

Open both `SKILL.md` files. Use `workshop-greeter` as a reference to improve `broad-greeter`:

1. Narrow its `description` to workshop greetings.
2. Add two clear response rules, for example, exactly three learning bullets and the required closing sentence.

Keep the folder name and metadata `name` unchanged. You can edit the file manually or ask Joule to help draft the changes, then review them.

Re-import the updated `broad-greeter` folder. Disable `workshop-greeter` before enabling the improved skill.

## Retest

1. Confirm that only your improved `broad-greeter` is enabled among the custom workshop skills.
2. Start a new conversation in agentic thinking mode and run the same three prompts.
3. Compare the results with the original `broad-greeter` responses and the `workshop-greeter` reference responses.
4. State one evidence-based improvement and one remaining uncertainty.

## Optional: Compare with the JW260 Workshop Guide

After completing the `broad-greeter` retest:

1. Re-enable `jw260-workshop-guide` if you want to use it for the remaining workshop exercises.
2. Open [`skills/jw260-workshop-guide/SKILL.md`](../../skills/jw260-workshop-guide/SKILL.md) in the repository.
3. Compare it with your `broad-greeter/SKILL.md`.
4. Identify how the workshop guide improves reliability through:
   - a narrower and more specific description;
   - explicit use and non-use boundaries;
   - ordered, detailed instructions;
   - troubleshooting and fallback behavior;
   - safety rules and a defined response ending.
5. Note one instruction from the workshop guide that you could adapt to make your improved `broad-greeter` clearer without broadening its purpose.

The workshop guide is a more complete example, but additional detail is useful only when it supports a clearly bounded purpose. More instructions do not compensate for an overly broad description.

## Success Criteria

You have tested `broad-greeter` first and `workshop-greeter` second in separate conversations, compared their responses, improved the vague skill, and retested the same prompts.

## Summary

You compared vague and clearly defined skill behavior, added clearer instructions, and retested the same prompts to see what improved.

Continue to - [Exercise 2 - Gross Margin Calculator](../ex2/README.md)
