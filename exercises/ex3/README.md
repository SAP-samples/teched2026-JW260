# Exercise 3: Sales Order Exception Prioritizer

## Goal

Run deterministic scoring on a supplied synthetic CSV, then explain one result. Explore and test this skill to see how it makes use of business data.

## 1. Set up the skill

1. In **Explore Skills**, choose **Import** and select the complete unzipped folder `exercises/ex3/sales-order-exception-prioritizer/`, including its `SKILL.md` and `scripts/` folder. Do not import just `SKILL.md` for this exercise.
2. Enable **Sales Order Exception Prioritizer** under **My Skills**.
3. Start a new conversation, select **Agentic Thinking**, and confirm the custom skill appears under **Active Skills**. No SAP-published retrieval skill is needed for the CSV path.

The CSV is supplied separately from the skill package. Its repository path is `exercises/ex3/sample-data/open-sales-orders.csv`.

## 2. Run the fixture first

1. Attach `sample-data/open-sales-orders.csv` from this exercise folder.

   ![The synthetic open-sales-orders CSV attached to the Joule conversation](images/03-01-attach-fixture.png)

2. Run this prompt:

   `Use Sales Order Exception Prioritizer to rank all rows in the attached open-sales-orders.csv using analysis date 2026-10-07. Use the CSV only; do not retrieve backend data.`

   The captured request uses earlier wording for the same CSV-only path:

   ![CSV fallback request using the attached open-sales-orders.csv instead of backend connectivity](images/03-06-fixture-request.png)

3. Confirm that the ranked table is sorted by score descending, requested date ascending, and sales order ascending. It should show the top 10 rows.

   ![CSV fallback ranked results showing DEMO-1019 and DEMO-1009 as Critical with scores of 130](images/03-07-fixture-ranked-results.png)

4. Confirm these totals: **Critical 5, High 6, Medium 5, Low 4, total 20**, with zero unknown credit statuses.

   ![CSV fallback summary showing 20 analyzed orders, priority totals, zero unknown credit statuses, and the ranked CSV download](images/03-08-fixture-summary-and-download.png)

5. When a download is available, open the full ranked CSV and compare its leading results:
   - `DEMO-1019`: score 130, Critical.
   - `DEMO-1009`: score 130, Critical.
   - `DEMO-1003`: score 90, Critical.

The fixture intentionally includes **completed orders and dates outside the live retrieval window** to exercise boundary rules. Score all 20 rows without applying the live filters. `Open`, `Partially Delivered`, and `Complete` are the only accepted delivery statuses, case-insensitively; an unrecognized status must produce a validation error, not be treated as incomplete.

## 3. Explain the score

These are simplified workshop rules, not SAP business policy:

| Verified condition | Points |
| --- | ---: |
| Credit block | +50 |
| Delivery block | +40 |
| Incomplete delivery and requested date before the analysis date | +30 |
| Incomplete delivery and requested date from the analysis date through 7 days later, inclusive | +20 |
| Raw net value at least 50000 in the record's own currency | +10 |

The two date rules are mutually exclusive. `Complete` orders receive neither date rule, but can still receive block or value points. Unknown credit status adds no credit-block points.

Priority thresholds: **Critical ≥70; High 40–69; Medium 20–39; Low 0–19**.

For `DEMO-1019`, the verified credit block contributes 50, delivery block 40, overdue incomplete delivery 30, and net value 125000 EUR contributes 10: **50 + 40 + 30 + 10 = 130 (Critical)**. Its earlier requested date places it before the tied `DEMO-1009`.

The raw **50000** threshold is applied separately in each record's currency. This is a simplified workshop rule, **not an equivalent monetary threshold across currencies**. Preserve currency labels; do not convert or sum mixed-currency values.

If script execution is unavailable, stop the execution path and use the rules and expected fixture results above for a **reference-only walkthrough**. Do not claim the script ran, fabricate a ranked CSV, or present the reference totals as newly computed results. Ask the facilitator for a supported runtime if you want to complete an executed run.

## Optional: Use the skill with live S/4HANA Data

<details>
<summary>Explore live retrieval after completing the core CSV path</summary>

For this exercise,enable `SAP S/4HANA Cloud Public Edition` as well as the custom skill and confirm both under **Active Skills** in **Agentic Thinking**.

Prompt:

`Use Sales Order Exception Prioritizer to rank my authorized sales-order exceptions using analysis date 2026-10-07. Follow its bounded live-retrieval procedure using current delivery and credit statuses.`

The skill first counts authorized, incomplete orders with requested delivery dates from **2026-09-07 through 2026-10-14**, inclusive. It retrieves at most **50** matching orders, sorted by requested delivery date descending and sales order ascending **before** the limit is applied. If more than 50 match, Joule should state that briefly and continue without asking for confirmation. It shows the 10 highest-ranked results and discloses matching versus analyzed counts. Do not retrieve more pages or retry after a retrieval error.


### Example live result

These retained captures illustrate a previous live run, not fixture expectations or a historical snapshot. Live records and counts may differ; use the written scope and rules above to verify your run.

Joule states the matching count and the bounded analysis scope before presenting the results:

![Live prioritization response showing 144 matching orders and a bounded analysis of 50](images/03-02-live-scope-and-results.png)

The ranked table highlights the highest-priority orders:

![Live ranked table showing the first Critical and High priority sales-order exceptions](images/03-03-live-ranked-orders.png)

The summary shows priority totals, unknown credit statuses, and the credit-code meanings retrieved for this tenant. Do not copy these mappings into your skill as universal SAP rules.

![Live analysis summary showing priority totals, verified credit-status mappings, and the ranked CSV download](images/03-04-live-summary-and-credit-status.png)

When a ranked CSV is available, download and open it to inspect the full analyzed sample, scores, and reasons:

![Opened ranked CSV showing sales-order scores, priorities, credit-status resolution, and reasons](images/03-05-ranked-csv-preview.png)

</details>


## Summary

An executed fixture run should match the totals and leading results above and explain a score of 130. If runtime was unavailable, record that you completed only the reference walkthrough. The live path is optional and tenant-dependent.

Continue to - [Exercise 4 - Build a Skill for a Line-of-Business Scenario](../ex4/README.md)
