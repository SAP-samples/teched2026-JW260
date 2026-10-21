---
name: successfactors-learning-word-report
description: Retrieve the signed-in user's authorized SuccessFactors learning assignments and create a due-date Word report
---

## Instructions

Create a read-only Word report for the signed-in user's learning assignments. Never request another employee's data or change a learning assignment.

1. Get an inclusive due-date range and a report date, all in `YYYY-MM-DD` format. Ask only for values that are missing or invalid.
2. Use the enabled `successfactors-learning` skill once to retrieve the signed-in user's authorized learning assignments. Request only title, due date, and displayed status. Do not call SuccessFactors directly.
3. Keep assignments whose due dates fall inside the requested range. Prefer server-side date filtering when the published skill supports it; otherwise filter the complete returned result. If the result is explicitly partial, truncated, or unavailable, stop and explain the limitation.
4. Do not invent missing values or interpret an unknown status code. Omit records without a title, valid due date, or displayed status, and count them as omitted.
5. Put each included assignment in exactly one category:
   - `Completed`: status explicitly says completed.
   - `Overdue`: not completed and due before the report date.
   - `Due in Range`: not completed and due on or after the report date.
6. Use the enabled `docx` skill to create `learning-due-date-report.docx` with exactly these sections in this order:
   1. `Learning Due-Date Report`
   2. `Report Scope` - signed-in user, due-date range, report date, and any retrieval limitation
   3. `Summary` - total included, Overdue, Due in Range, Completed, and omitted counts
   4. `Overdue Assignments` - table with `Title`, `Due Date`, and `Status`
   5. `Assignments Due in Range` - table with the same columns
   6. `Recommended Next Steps` - brief factual actions based only on overdue and due-in-range assignments
7. Sort both assignment tables by due date ascending, then title ascending. Keep an empty section and write `None` when a table has no rows. Do not add a completed-assignment section.
8. Check the section order, counts, sorting, and privacy before returning the file. State: `No SAP SuccessFactors data was changed.`

If `successfactors-learning`, authorization, required fields, complete data handoff, or `docx` is unavailable, state what failed and stop. Do not fabricate data or claim that a document was created.
