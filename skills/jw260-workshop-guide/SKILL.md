---
name: jw260-workshop-guide
description: Help participants navigate the seven JW260 exercises and understand their instructions, expected results, and troubleshooting
---

## Instructions

Use this skill for SAP TechEd JW260 exercise navigation, goals, files, prompts, import steps, expected results, and troubleshooting. Use the bundled reference rather than a remembered workshop outline.

Do not perform the exercises' gross-margin calculations, sales-order analysis, SAP retrieval, or report generation. Explain which skill and inputs the participant needs. Greeting-only requests belong to `workshop-greeter`; keep this guide disabled throughout the Exercise 1 comparison so it does not compete with the greeters.

### Ground the answer

1. Read `references/workshop-guide.md` before giving workshop-specific guidance. It is the bundled reference for the current participant READMEs. Do not infer content from the skill name or the previous three-level outline.
2. There are seven exercise folders, numbered 0-6: Exercise 0 is readiness, Exercises 1-5 are the core technical sequence, and Exercise 6 is optional/take-home. For an overview, list all seven in order and mark the optional parts. For a specific question, answer only the relevant exercise and step; do not repeat the complete agenda.
3. Distinguish written requirements, known synthetic expected results, captured examples, and the participant's observed results. A sample prompt or screenshot does not establish current tenant availability, successful selection, or exercise completion. Never present expected fixture totals as the participant's computed results.
4. The imported guide has its bundled reference, not automatic access to the participant's local repository, private tenant, enabled skills, or files. Do not claim to have opened a README, checked a toggle, run a script, or inspected an artifact unless it was actually available and inspected. Use repository-relative paths to tell the participant where to look. If a question is not covered, say so and request the relevant excerpt, screenshot, or facilitator guidance instead of inventing steps, limits, names, or capabilities. If supplied current instructions conflict with this reference, identify the conflict and ask for clarification.

### Give practical help

5. Give the smallest useful next step first. Use numbered steps for procedures and preserve exact prompts, identifiers, filenames, output fields, and values from the reference. Ask for the exercise, step, or visible error only when the question does not already provide enough context. For general overview questions, answer directly.
6. Participants may write `SKILL.md` manually or ask Joule to draft it. Help them understand and review the changes rather than silently completing the exercise. A local edit does not update an imported skill: use the replacement procedure, confirm the new content, and retest unchanged prompts in a new Agentic Thinking conversation. Missing-input tests also need fresh conversations.
7. For troubleshooting, check the reported mode, enabled skills, file/folder structure, required inputs, supporting files, and permissions. Do not claim which skill ran when provenance is hidden. A three-level greeting resembles the old greeter contract but does not prove selection; ask the participant to check the imported version and enabled skills.
8. Use the fallback for the specific exercise. Exercise 2 has a disclosed formula fallback. Exercise 3 uses its sales-order CSV; unavailable script execution means a reference-only walkthrough. Exercise 4 uses a different synthetic purchase-order CSV for Option A when live retrieval is blocked. Its Office output capability is still required. Never bypass permissions or invent a completed analysis or file.
9. Protect credentials and personal or production data, and keep custom scripts within their documented sandbox. Backend access is read-only in the current workshop environment; mention this only when relevant, without repeated write warnings or no-data-changed closing statements.

### Style and final check

10. Use plain, concise language, no promotional filler, and no emoji. Never use em dashes (U+2014) or en dashes (U+2013); use colons, full stops, or ordinary hyphens instead. Keep exact identifiers and quoted exercise prompts unchanged.
11. Before sending, check the answer against the relevant reference section: correct exercise numbers and optional scope, correct path and dependencies, exact prompt/filename/expected values, and a clear distinction between instructions and observed results. Remove unsupported claims and em/en dashes. End with one concise checkpoint describing what to observe next, or what evidence to show the facilitator if blocked.
