# Exercise 2: Gross Margin Calculator

## Goal

Inspect and test a supplied skill that collects required inputs, validates them, and uses a bundled script for deterministic arithmetic. Notice what belongs in the instructions, script, and reference file.

## Before You Start: Import and Enable the Skill

1. Open **User menu > Explore Skills > Import**.
2. Select the complete unzipped `exercises/ex2/gross-margin-calculator/` folder, including `SKILL.md`, `references/formulas.md`, and `scripts/calculate_margin.py`.
3. Find `gross-margin-calculator` under **My Skills** and enable it. Disable both greeters from Exercise 1 and any competing custom skills. Confirm `gross-margin-calculator` under **Active Skills**.
4. Start a new conversation and select **+ > Agentic Thinking** before running the base prompt below.

> [!IMPORTANT]
> **Select `gross-margin-calculator/`, not its parent `ex2/` folder.** The selected folder must directly contain `SKILL.md`. Import the complete folder, not only `SKILL.md`, `scripts/`, or `references/`, so the bundled script and reference are included. Do not ZIP the skill for import.

## Base prompt

`Calculate gross margin for revenue 125000 EUR and cost 87500 EUR.`

Expected result:

- Inputs: revenue 125000 EUR; cost 87500 EUR
- Gross Profit: 37500.00 EUR
- Gross Margin: 30.00%
- Warning: None

![Gross margin result showing the supplied inputs, gross profit, and 30 percent gross margin](images/02-01-margin-base-result.png)

## Clarification and edge prompts

Start a **new conversation in agentic thinking mode for each prompt**, so values from the base calculation are not reused. Answer any clarification in that same conversation.

- `Calculate gross margin for revenue 125000 EUR.` Expected: ask for cost and do not invent it.
- `Calculate gross margin for revenue 0 and cost 500 EUR.` Expected: gross profit -500.00 EUR, undefined gross margin, and a zero-revenue warning.
- `Calculate gross margin for revenue -10 EUR and cost 5 EUR.` Expected: reject negative revenue.
- `Calculate gross margin for revenue 100 USD and cost 60 EUR.` Expected: do not convert currency; ask for values in one currency.

When a required input is missing, the skill asks for it instead of inventing a value:

![Gross margin skill asking for the missing cost input](images/02-02-margin-missing-input.png)

## Participant steps

1. Open `gross-margin-calculator/SKILL.md`, then its `references/formulas.md` and `scripts/calculate_margin.py`. Find the instruction that saves the inputs as JSON and calls the script. Notice how the reference provides the fallback rules; you do not need to understand every line of Python.
2. Complete **Before You Start** above, then run the base prompt in a new **Agentic Thinking** conversation.
3. Compare the result with the expected values.
4. Run each clarification and edge prompt in its own fresh conversation and record the behavior.
5. If Python execution is unavailable, confirm that the skill uses and discloses the formula fallback.

## Optional extension: target margin

**Quick challenge:** how much revenue would you need for a 35% gross margin, keeping cost unchanged? No Python changes are needed.

1. **Edit `gross-margin-calculator/SKILL.md`.** Add target-margin planning to its `description` and opening sentence. Replace the sentence beginning `The only additional text permitted` with:

   ```text
   Keep the base result and fallback disclosure. When target-margin planning is requested, ask for a missing target percentage; accept only numbers from 0% to below 100%. Use the target-revenue formula in references/formulas.md, rounding to two decimals (half-up). Add a Target Margin Planning section with target, unchanged cost, and required revenue. State that this uses the reference formula, not the base script.
   ```

2. **Save, [replace the imported copy](../../README.md#replacing-an-imported-skill), and enable it.** Import the complete `gross-margin-calculator/` folder.
3. **Test in a new Agentic Thinking conversation:**

   `Calculate gross margin for revenue 125000 EUR and cost 87500 EUR. Also calculate required revenue for a 35% target gross margin at the same cost.`

   **Check:** current margin stays **30.00%**; target required revenue is **134615.38 EUR** in a separate section.

## Summary

You inspected and tested an input/output contract, traced the instruction-to-script handoff, and checked validation, rounding, and disclosed fallback behavior.

Continue to - [Exercise 3 - Sales Order Exception Prioritizer](../ex3/README.md)
