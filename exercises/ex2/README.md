# Exercise 2: Gross Margin Calculator

## Goal

Add required-input collection, validation, deterministic arithmetic, edge-case handling, and a supporting reference file.

## Base prompt

`Calculate gross margin for revenue 125000 EUR and cost 87500 EUR.`

Expected result:

- Inputs: revenue 125000 EUR; cost 87500 EUR
- Gross Profit: 37500.00 EUR
- Gross Margin: 30.00%
- Warning: None

![Gross margin result showing the supplied inputs, gross profit, and 30 percent gross margin](images/02-01-margin-base-result.png)

## Clarification and edge prompts

- `Calculate gross margin for revenue 125000 EUR.` Expected: ask for cost and do not invent it.
- `Calculate gross margin for revenue 0 and cost 500 EUR.` Expected: gross profit -500.00 EUR, undefined gross margin, and a zero-revenue warning.
- `Calculate gross margin for revenue -10 EUR and cost 5 EUR.` Expected: reject negative revenue.
- `Calculate gross margin for revenue 100 USD and cost 60 EUR.` Expected: do not convert currency; ask for values in one currency.

When a required input is missing, the skill asks for it instead of inventing a value:

![Gross margin skill asking for the missing cost input](images/02-02-margin-missing-input.png)

## Participant steps

1. Inspect `SKILL.md`, `references/formulas.md`, and `scripts/calculate_margin.py`.
2. Import the  `gross-margin-calculator` folder in Joule Work.
3. Enable the imported skill.
4. Select agentic thinking mode and run the base prompt.
5. Compare the result with the expected values.
6. Run every clarification and edge prompt and record the behavior.
7. If Python execution is unavailable, confirm that the skill uses and discloses the formula fallback.

## Extension: target margin

Add a target-margin input and use the reference formula to calculate required revenue at the current cost. Validate that the target is below 100 percent, keep decimal half-up rounding, and label the extension result separately from the base output.

## Summary

You created a skill with a complete input and output contract, deterministic calculation, validation, rounding, and fallback behavior.

Continue to - [Exercise 3 - Sales Order Exception Prioritizer](../ex3/README.md)
