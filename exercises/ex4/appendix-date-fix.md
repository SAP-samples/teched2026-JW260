# Exercise 4 Appendix: Improve a Skill with Joule

If you find a defect, ask Joule to explain it and suggest how to improve your skill. This optional example shows the process for an incorrect purchase-order date.

## 1. Identify the defect

The Excel report showed `1970-01-21` for PO `4500078413`, outside the requested date range. Joule traced it to a timestamp-conversion mistake and showed the corrected date, `2026-03-13`.

![Joule explaining the timestamp error and showing the corrected date](images/04-09-s4-date-error-diagnosis.png)

## 2. Ask for an improvement

Joule suggested preserving the returned data, checking timestamp units, validating dates against the requested range, and cross-checking the summary against the data sheet.

![Joule suggesting improvements to prevent the date error](images/04-10-s4-date-prevention-advice.png)

## 3. Update your source skill

Attach your own `SKILL.md` or source package and ask Joule to incorporate the improvements. In this example, the source was attached as a ZIP.

![The source skill attached to the update request](images/04-11-s4-source-skill-attachment.png)

Joule returned an updated skill package for download.

![The updated skill ZIP and summary of changes](images/04-12-s4-updated-skill-download.png)

## 4. Reimport and verify

Download and extract the package, review the changes, remove the old imported custom skill, and import and enable the replacement. Keep the required business and output skills enabled.

Run the same sample prompt in a new conversation, open the new workbook, and check the corrected date, sorting, and the rest of the [Option A checklist](README.md#verify-the-output).

[Return to Exercise 4](README.md) · [Continue to Exercise 5](../ex5/README.md)
