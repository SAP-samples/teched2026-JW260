# Exercise 5: Freestyle (Optional Stretch or Take-Home)

This is an optional extension after the core exercises. Use spare workshop time or return to it later; it is not required to complete the workshop.

> [!TIP]
> **Time left? Explore Joule Work Desktop.** Ask a facilitator to help you get it configured before you start. This is an optional exploration, not a requirement for completing the workshop.

## Goal

Design, build, and test an original custom Joule skill for a use case and outcome of your choice.

You can write `SKILL.md` manually or ask Joule to draft it from your requirements. Review the generated skill before importing and testing it.

## Choose your outcome

Choose a concrete business purpose and decide what the skill should return. Your result may be a conversational response, analysis, workflow, PowerPoint, Word document, Excel workbook, or another artifact supported by the workshop environment.

Unlike Exercise 4, this exercise does not prescribe the business scenario, input fields, transformation rules, or output format. You define the success criteria before you build the skill. Use supplied or authorized data and the capabilities available in the workshop environment.

If your outcome creates a Microsoft Office file, enable the corresponding SAP-published output skill in **Explore Skills** before testing: `Word Documents`, `PowerPoint`, or `Excel`. Confirm that it appears under **Active Skills** together with any business skill your scenario needs.

## Participant steps

1. Write one sentence that describes what your skill creates and for whom.
2. Decide which inputs the user must provide and which information must never be invented.
3. Define the expected response or artifact structure before writing the skill.
4. Create a lowercase, hyphenated skill folder containing a `SKILL.md`.
5. Add YAML metadata with a matching `name` and a precise `description`.
6. Write instructions that define:
   - when the skill should and should not be used;
   - required inputs and validation;
   - the exact output structure;
   - the output format and filename when a file is required;
   - the behavior when information is missing;
   - a final check before returning the response or file.
7. If your skill needs a script, reference, or other supporting file, add it in the appropriate subfolder and explain when Joule should use it.
8. Follow [Importing a skill](../../README.md#importing-a-skill). Enable your custom skill and every business or output skill it depends on, confirm they appear under **Active Skills**, and start a new **Agentic Thinking** conversation.
9. Run the skill and inspect the result. If it creates a file, download and open it; a successful download alone is not enough.
10. Compare the result with the success criteria you defined before building.
11. Improve one aspect of the source. Follow [Replacing an imported skill](../../README.md#replacing-an-imported-skill) and confirm the custom skill and dependencies under **Active Skills**. Retest the same request in a new **Agentic Thinking** conversation.

## Expected result

The skill achieves the outcome and success criteria you defined, uses only supplied or authorized information, and asks for missing required input instead of inventing it.

## Review questions

- Is the skill purpose narrow enough for reliable selection?
- Are all required inputs defined?
- Does the result follow the structure in `SKILL.md`?
- If a file is created, can it be opened and used without repair?
- Does the skill identify missing information rather than inventing it?
- Is the result free of credentials, personal data, and unauthorized business data?

## Troubleshooting

| Problem | Action |
| --- | --- |
| The skill is not selected | Narrow the description and confirm that the skill is enabled in agentic thinking mode. |
| Joule asks for information repeatedly | Make the required inputs and accepted formats explicit. |
| A requested artifact cannot be created | Use a supported format or clearly state the environment limitation. |
| A Word, PowerPoint, or Excel file is not created | Confirm that `Word Documents`, `PowerPoint`, or `Excel` is enabled under **Explore Skills** and appears under **Active Skills**. |
| The output structure changes between runs | Define the response, section, slide, sheet, or column order explicitly. |

## Summary

If you completed this optional extension, you designed, built, tested, and improved an original custom skill that produces a reusable conversational response, analysis, or supported artifact against your own success criteria.

Return to - [JW260 Workshop Overview](../../README.md)
