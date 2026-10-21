---
name: ariba-requisition-powerpoint-review
description: Retrieve authorized SAP Ariba requisitions using user-supplied filters and create a five-slide PowerPoint review
---

## Instructions

Use this skill only to create a read-only PowerPoint review of requisitions that the signed-in user is authorized to view in SAP Ariba. Do not use it to create, change, submit, withdraw, approve, deny, or otherwise act on requisitions.

1. Collect all required filters before retrieval:
   - requisition submission date range with inclusive start and end dates in `YYYY-MM-DD` format;
   - minimum total value as a nonnegative number;
   - currency;
   - requester, or the explicit value `all authorized requesters`;
   - requisition status;
   - report date in `YYYY-MM-DD` format.
2. Ask for every missing or ambiguous filter. Do not infer dates, currency, requester, status, or minimum value.
3. Use the facilitator-confirmed and enabled SAP-published Ariba skill to retrieve only requisitions the signed-in user is authorized to view. This custom skill does not connect directly to SAP Ariba. Do not invent the name of an unavailable Ariba skill.
4. Apply the date, minimum-value, currency, requester, and status filters in SAP Ariba when the enabled skill supports them. Retrieve only:
   - requisition identifier;
   - requester display name or identifier returned by the Ariba skill;
   - total value;
   - currency;
   - submission date;
   - status and its displayed text when available.
5. Count matches before retrieving details when supported. Sort by total value descending and requisition identifier ascending before applying any retrieval limit. Retrieve no more than 50 requisitions. If counting, server-side filtering, sorting, or bounded retrieval is unsupported, state the limitation instead of presenting an arbitrary page as complete.
6. Validate every returned record against the requested filters. Preserve values and currencies exactly as returned. Do not convert currencies, invent missing values, or guess status-code meanings. Omit records missing a required field and disclose the omitted count.
7. Use the enabled `pptx` skill to create `requisition-review.pptx` containing exactly five slides in this order:
   1. `Requisition Review` — title, applied submission-date range, and report date.
   2. `Scope and Filters` — all requested filters, matching count when known, analyzed count, omitted-invalid-record count, and any retrieval limitation.
   3. `Summary` — number of analyzed requisitions and total value grouped separately by currency. Do not combine or convert currencies.
   4. `Highest-Value Requisitions` — up to five records sorted by numeric value descending and requisition identifier ascending. Show requisition ID, requester, value, currency, submission date, and status.
   5. `Review Points` — concise factual observations supported by the retrieved records and items for human review. Do not make or imply an automated approval decision.
8. Keep slide content readable. Use no more than five principal bullets per slide; a compact table is allowed on slide 4. Do not add macros, external links, hidden slides, or unsupported branding claims.
9. Before returning the file, verify the exact slide count, title order, filter completeness, summary calculations, slide-4 sorting and maximum of five records, factual support for every review point, and that the presentation opens successfully.
10. Return the presentation and state the matching count when known, analyzed count, whether the review is complete or bounded, and: `No SAP Ariba data was changed.`
11. If the facilitator-confirmed Ariba skill, authorization, data handoff, required fields, or `pptx` is unavailable, explain exactly what is unavailable and stop. Do not invent requisitions or claim that a presentation was created.
