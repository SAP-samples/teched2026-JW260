---
name: gross-margin-calculator
description: Calculate gross profit and gross margin from revenue and cost
---

## Instructions

Use this skill only to calculate gross profit and gross margin from revenue and cost stated in one currency.

1. Collect `revenue`, `cost`, and `currency` before calculating. If any input is missing, ask for it. Do not infer missing numbers.
2. Reject negative revenue or cost and ask the user to provide nonnegative values.
3. Do not convert currency. Confirm that revenue and cost use the same currency if the request is ambiguous.
4. Save one JSON object containing `revenue`, `cost`, and `currency` to an input file in the sandbox workspace.
5. Run `scripts/calculate_margin.py` with the JSON input file path as its only argument.
6. If the script reports a validation error, explain the error and request corrected input. Do not calculate with invalid input.
7. Present the result using these fixed fields::
   - Inputs: revenue, cost, and currency
   - Gross Profit: amount and currency
   - Gross Margin: percentage, or `undefined` when the script returns null
   - Warning: every warning returned by the script, or `None`
   Before responding, verify that the displayed inputs match the supplied values and the results match the selected calculation path. The only additional text permitted is the formula-fallback disclosure required by step 8.
8. If script execution is unavailable, follow `references/formulas.md` exactly. State that the formula fallback was used and apply the documented validation, rounding, and zero-revenue rules.
