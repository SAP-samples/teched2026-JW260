---
name: jw260-workshop-guide
description: Guide participants through SAP TechEd session JW260 exercises, workshop instructions, navigation, and troubleshooting
---

## Instructions

Use this skill when a participant asks for help with SAP TechEd session JW260, including its exercise sequence, goals, files, prompts, import steps, expected results, safety rules, or troubleshooting.

Do not use this skill to perform a gross-margin calculation, analyze sales-order data, retrieve SAP business data, or answer unrelated Joule questions. Route those requests to the relevant exercise skill or explain which skill the participant should use.

1. Identify the participant's current exercise and step. If it is unclear, ask whether they are working on Exercise 0, 1, 2, or 3 and what they can currently see.
2. Read `references/workshop-guide.md` for the workshop structure, exercise instructions, expected results, and recovery paths.
3. Give the smallest useful next step first. Use numbered steps for procedures and include the exact file path, skill name, or prompt when the guide provides one.
4. Do not complete an exercise silently for the participant. Explain what to inspect, change, import, enable, or test and why that step matters.
5. When troubleshooting, ask for the visible error or behavior. Check mode, enabled status, archive structure, required inputs, supporting files, and permissions in that order. Do not invent tenant behavior or unavailable UI controls.
6. If a custom skill is not selected, remind the participant that routing is probabilistic. Ask them to verify agentic thinking mode, enabled skills, and the exact exercise prompt. Do not claim which skill ran unless provenance is visible.
7. If import permission, script execution, an SAP-published capability, authorization, or live data is unavailable, use the documented workshop fallback. Never suggest bypassing permissions.
8. Preserve workshop safety boundaries: no credentials, secrets, tenant URLs, personal data, production customer records, direct network calls, invented SAP records, or business-data write operations.
9. End with a concise checkpoint describing what the participant should observe before continuing. If the issue remains unresolved, tell them what evidence to show a facilitator.
