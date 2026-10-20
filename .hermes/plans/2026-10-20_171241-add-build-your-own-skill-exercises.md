# Plan: Add guided and freestyle “build your own skill” exercises

## Goal

Extend JW260 with a guided business-domain skill exercise and a freestyle document-generation challenge so participants have more work available without making completion of every task mandatory.

## Current context / assumptions

- The repository currently exposes Exercise 0 through Exercise 3 in `README.md`; the progression is readiness → compare/repair → deterministic calculation → read-only S/4 exception analysis.
- The working tree is already dirty on branch `db_exercises`, including an in-progress renumbering/move of exercises. Preserve those changes and review diffs before every commit; do not reset, restore, or stage unrelated files.
- Exercise 4 will satisfy “build your own skill based on a standard skill” through three selectable, read-only business goal cards: SAP SuccessFactors, SAP Ariba, or SAP S/4HANA. Participants choose one track rather than complete all three.
- Exact SAP-published capability names, supported fields, handoff behavior, and artifact-generation support are tenant-dependent and are not yet verified. Instructions must use visibly marked facilitator placeholders and a synthetic/manual fallback; they must not claim that a custom-skill script directly connects to an SAP backend.
- Exercise 5 will be an optional freestyle/early-finisher challenge. Participants choose one output: PowerPoint (`.pptx`), Word (`.docx`), or Excel (`.xlsx`). If the tenant cannot create the chosen binary format, the accepted fallback is the same structured content as Markdown for PowerPoint/Word or CSV for Excel.
- “More tasks rather than too few” should be implemented as a core path plus optional extensions. Do not lengthen the required workshop path until a timed rehearsal confirms capacity.
- Use synthetic data only. Keep all new scenarios read-only and do not introduce credentials, tenant URLs, production identifiers, personal data, or business-data write operations.

## Architecture / proposed approach

Add Exercise 4 as a scaffolded transfer exercise: participants start from a deliberately incomplete skill template, select a domain goal card, incorporate a facilitator-qualified SAP-published capability as the retrieval step, and define validation, output, safety, and fallback behavior themselves. Add Exercise 5 as a format-oriented capstone with a minimal blank template, three artifact briefs, and a common review rubric; update the root navigation and the `jw260-workshop-guide` support skill so all six exercises remain self-navigating.

Keep tenant-specific facts in one new facilitator qualification file rather than duplicating them across participant instructions. Add a small standard-library test suite that validates exercise navigation, required files, skill metadata, and the absence of unresolved placeholders from files intended to be importable.

## Step-by-step tasks

### 1. Protect the in-progress branch and capture the baseline

1. Run:

   ```bash
   git status --short --branch
   git diff -- README.md exercises skills
   ```

2. Confirm that the output still shows branch `db_exercises` and the pre-existing Exercise 0–3 move/renumber changes. Save the output outside the repository if needed; do not modify or stage anything.
3. Before each later commit, run `git diff --cached --name-only` and verify that only files named by that task are staged.

Expected result: the implementer understands which changes predate this plan and can avoid overwriting or accidentally committing them.

### 2. Add a failing structural test for the expanded workshop

Create `tests/test_workshop_structure.py` with this complete content:

```python
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class WorkshopStructureTests(unittest.TestCase):
    def test_root_readme_links_all_six_exercises(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        for number in range(6):
            with self.subTest(exercise=number):
                self.assertIn(f"exercises/ex{number}/", text)

    def test_each_exercise_has_readme_and_goal(self):
        for number in range(6):
            with self.subTest(exercise=number):
                path = ROOT / "exercises" / f"ex{number}" / "README.md"
                self.assertTrue(path.is_file(), path)
                self.assertIn("## Goal", path.read_text(encoding="utf-8"))

    def test_new_exercises_have_required_support_files(self):
        required = [
            "exercises/ex4/starter-template/SKILL.md",
            "exercises/ex4/references/domain-goal-cards.md",
            "exercises/ex4/sample-data/business-items.csv",
            "exercises/ex5/starter-template/SKILL.md",
            "exercises/ex5/references/artifact-briefs.md",
            "exercises/ex5/references/review-rubric.md",
            "skills/jw260-workshop-guide/references/facilitator-qualification.md",
        ]
        for relative_path in required:
            with self.subTest(path=relative_path):
                self.assertTrue((ROOT / relative_path).is_file(), relative_path)

    def test_importable_skills_have_matching_metadata_names(self):
        for path in ROOT.glob("exercises/ex*/**/SKILL.md"):
            if "starter-template" in path.parts:
                continue
            text = path.read_text(encoding="utf-8")
            match = re.search(r"(?m)^name:\s*([^\s]+)\s*$", text)
            self.assertIsNotNone(match, path)
            self.assertEqual(path.parent.name, match.group(1), path)

    def test_importable_skills_have_no_todo_placeholders(self):
        for path in ROOT.glob("exercises/ex*/**/SKILL.md"):
            if "starter-template" in path.parts:
                continue
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("TODO", text, path)
            self.assertNotIn("<CAPABILITY_NAME>", text, path)


if __name__ == "__main__":
    unittest.main()
```

Run:

```bash
python3 -m unittest tests/test_workshop_structure.py -v
```

Expected result: existing Exercise 0–3 assertions pass; tests fail for missing `exercises/ex4/`, `exercises/ex5/`, and their support files. Do not commit the failing test by itself unless the repository convention explicitly permits red commits.

### 3. Create Exercise 4: guided business-domain skill

Create these files:

- `exercises/ex4/README.md`
- `exercises/ex4/starter-template/SKILL.md`
- `exercises/ex4/references/domain-goal-cards.md`
- `exercises/ex4/sample-data/business-items.csv`

Use the following exercise contract in `exercises/ex4/README.md`:

1. Title: `Exercise 4: Build a Business Skill from a Standard Capability`.
2. Goal: choose one business outcome, use a facilitator-qualified SAP-published capability only for authorized retrieval, and build a custom skill that validates and transforms the handed-off data into a deterministic read-only result.
3. Timebox: 20 minutes core plus 10 minutes extensions.
4. Required flow:
   - Choose exactly one SuccessFactors, Ariba, or S/4HANA goal card.
   - Copy `starter-template/` to a lowercase, hyphenated folder with a meaningful name.
   - Replace every `TODO` and `<CAPABILITY_NAME>` placeholder.
   - Define in-scope and out-of-scope requests, required inputs, ordered steps, output contract, missing-data behavior, authorization boundary, and fallback.
   - Use the qualified SAP-published capability only if it exists in the workshop tenant; otherwise attach `sample-data/business-items.csv`.
   - Import, enable, and run one happy-path prompt, one missing-input prompt, and one boundary prompt from the selected goal card.
   - Exchange the skill with a partner and review it against five checks: discoverability, required inputs, deterministic output, safe failure, and no write-back.
5. Success criteria: all placeholders are replaced, the skill is importable, three prompt classes are tested, and the participant can explain which component retrieves data and which component transforms it.
6. End with `Continue to - [Exercise 5 - Build Your Own Skill](../ex5/README.md)`.

Put this complete starter in `exercises/ex4/starter-template/SKILL.md`:

```markdown
---
name: TODO-lowercase-hyphenated-name
description: TODO one sentence stating the exact business outcome and triggering request
---

## Instructions

Use this skill only to TODO. Do not use it to TODO.

1. Collect and validate these required inputs: TODO.
2. If authorized business data is not attached, ask Joule to use `<CAPABILITY_NAME>` to retrieve only TODO fields. This custom skill does not connect directly to an SAP backend.
3. If that capability, authorization, field set, or data handoff is unavailable, ask for the supplied synthetic CSV. Never invent business records.
4. Validate TODO. If validation fails, identify the field and request corrected input.
5. Apply these deterministic transformation rules in order: TODO.
6. Return exactly: TODO ordered output contract.
7. State the data scope, any omitted or unresolved records, and the analysis limitation.
8. Keep the workflow read-only. Do not create, update, approve, release, or delete business data.
```

Write `exercises/ex4/references/domain-goal-cards.md` with three parallel cards, each containing an outcome, required synthetic columns, a happy-path prompt, a missing-input prompt, a boundary prompt, deterministic output, and an optional extension:

- **SuccessFactors — Goal review planner:** summarize synthetic employee-goal items due in a participant-supplied date window into `Overdue`, `Due soon`, and `Later`; output counts and a manager discussion agenda. Required columns: `item_id,subject,due_date,status,owner_alias`. Never expose additional employee data or change goals.
- **Ariba — Requisition approval briefing:** group synthetic requisitions by age and amount into explicit priority bands; output counts, reasons, and a review list. Required columns: `item_id,subject,created_date,amount,currency,status`. Preserve currencies and do not approve requisitions.
- **S/4HANA — Delivery-risk briefing:** classify synthetic sales items by requested date and block indicators; output counts, reasons, and a customer-impact review list. Required columns: `item_id,subject,requested_date,delivery_block,credit_status,status`. Do not release blocks or update orders.

Use `<CAPABILITY_NAME>` in every live-path card and point to `skills/jw260-workshop-guide/references/facilitator-qualification.md`; do not invent product card names. Make each card’s prompts copy-pasteable and use a fixed analysis date so fallback results can be checked.

Create `exercises/ex4/sample-data/business-items.csv` as one neutral fixture usable by all tracks. Include 12 synthetic rows and a superset schema:

```csv
track,item_id,subject,reference_date,amount,currency,status,owner_alias,delivery_block,credit_status
successfactors,SF-DEMO-001,Synthetic goal A,2026-10-15,,,in-progress,USER-A,,
ariba,AR-DEMO-001,Synthetic requisition A,2026-09-15,12000,EUR,pending,USER-B,,
s4,S4-DEMO-001,Synthetic delivery A,2026-10-18,45000,EUR,incomplete,USER-C,true,blocked
```

Expand this pattern to four rows per track, covering one missing/ambiguous value, one date boundary, one low-priority case, and one high-priority case. Keep all identifiers visibly synthetic.

Run the structural tests. Expected result: Exercise 4 assertions pass; failures remain only for Exercise 5 and root/support-guide integration.

Stage only the four Exercise 4 files plus the test and commit:

```bash
git add tests/test_workshop_structure.py exercises/ex4
git diff --cached --check
git commit -m "Add guided business skill exercise"
```

Expected result: one commit with no unrelated Exercise 0–3 changes.

### 4. Create Exercise 5: freestyle skill with PPTX, DOCX, or XLSX output

Create:

- `exercises/ex5/README.md`
- `exercises/ex5/starter-template/SKILL.md`
- `exercises/ex5/references/artifact-briefs.md`
- `exercises/ex5/references/review-rubric.md`

`exercises/ex5/README.md` must make this an optional capstone/early-finisher exercise, not a guaranteed core deliverable. Use this flow:

1. Choose exactly one artifact brief: presentation, decision memo, or action register.
2. Choose a safe synthetic topic or reuse the supplied Exercise 4 fixture.
3. Copy and rename `starter-template/`.
4. Complete metadata, required inputs, artifact structure, validation, filename, and fallback behavior.
5. Import and run one complete-input prompt and one incomplete-input prompt.
6. Open the resulting artifact and review it against `references/review-rubric.md`; checking only that a file exists is insufficient.
7. If binary file creation is not available, produce the documented Markdown or CSV fallback and assess the same content contract.
8. Swap with a partner for one improvement cycle.

Put this complete starter in `exercises/ex5/starter-template/SKILL.md`:

```markdown
---
name: TODO-lowercase-hyphenated-name
description: TODO describe the exact artifact and business purpose
---

## Instructions

Use this skill only to create TODO from user-supplied or synthetic information. Do not retrieve or change business data.

1. Collect these required inputs before producing output: TODO.
2. Reject credentials, personal data, confidential production data, and unsupported file types. Do not invent missing facts.
3. Validate the input against this contract: TODO.
4. Create exactly one TODO artifact with this ordered structure: TODO.
5. Use the filename pattern `TODO-YYYY-MM-DD.EXT`, where the date is supplied by the user rather than inferred.
6. Verify the artifact against these checks before returning it: TODO.
7. If binary TODO generation is unavailable, return TODO fallback with the same sections, labels, and data.
8. State which input was used and identify any unresolved limitation.
```

Write three briefs in `exercises/ex5/references/artifact-briefs.md`:

- **PowerPoint:** a five-slide executive briefing (`Title`, `Situation`, `Evidence`, `Recommendation`, `Next steps`), maximum five bullets per slide, source note on evidence slides, Markdown slide-outline fallback.
- **Word:** a one-page decision memo (`Decision required`, `Context`, `Options`, `Recommendation`, `Risks`, `Next step`), explicit owner/date fields, Markdown memo fallback.
- **Excel:** an action register with columns `ID,Action,Owner,Due Date,Priority,Status,Source`, one frozen header row and filters if supported, CSV fallback. No macros, external links, hidden sheets, or formulas based on untrusted text.

For each brief include exact complete-input and missing-input prompts and a deterministic filename. Do not prescribe a specific library or claim that Joule can create the binary until facilitator qualification confirms it.

Write `exercises/ex5/references/review-rubric.md` as a 10-point rubric with five two-point dimensions: correct structure, factual grounding, deterministic formatting, safe handling of missing data, and usable/openable output. Define `8/10` as pass and require zero points for safety to fail the artifact regardless of total.

Run:

```bash
python3 -m unittest tests/test_workshop_structure.py -v
```

Expected result: all new-file assertions pass; failures remain only where root navigation or support-guide updates are not yet complete.

Stage only Exercise 5 and commit:

```bash
git add exercises/ex5
git diff --cached --check
git commit -m "Add freestyle artifact skill challenge"
```

### 5. Add one tenant-qualification source of truth

Create `skills/jw260-workshop-guide/references/facilitator-qualification.md` with a table containing these exact columns:

```markdown
| Track | SAP-published capability name | Confirmed fields | Handoff confirmed | Binary output confirmed | Test identity/date | Status/notes |
| --- | --- | --- | --- | --- | --- | --- |
| SuccessFactors | TBD | TBD | No | N/A | TBD | Use CSV fallback until qualified. |
| Ariba | TBD | TBD | No | N/A | TBD | Use CSV fallback until qualified. |
| S/4HANA | TBD | TBD | No | N/A | TBD | Use CSV fallback until qualified. |
| PowerPoint | N/A | N/A | N/A | No | TBD | Use Markdown outline fallback until qualified. |
| Word | N/A | N/A | N/A | No | TBD | Use Markdown memo fallback until qualified. |
| Excel | N/A | N/A | N/A | No | TBD | Use CSV fallback until qualified. |
```

Below it, add a qualification procedure requiring the facilitator to verify visible capability name, fields, authorization, same-conversation handoff, actual file generation, file download/opening, and fallback before replacing `TBD` or `No`. State that this file is facilitator-facing and must not contain tenant URLs, usernames, screenshots with identities, or credentials.

Run the tests; the required support-file assertion should now pass.

Commit only this file:

```bash
git add skills/jw260-workshop-guide/references/facilitator-qualification.md
git diff --cached --check
git commit -m "Add workshop capability qualification checklist"
```

### 6. Integrate Exercises 4 and 5 into root navigation

Update `README.md` in all of these places:

- Overview: change “three progressively more capable” to a progression ending in one guided build and one optional freestyle capstone.
- Learning outcomes: add “adapt a custom workflow around a qualified SAP-published capability without claiming direct connectivity” and “define and validate a PPTX, DOCX, or XLSX artifact contract with a documented fallback.”
- Exercises list: add links to `exercises/ex4/` and `exercises/ex5/` with two concise bullets each.
- Sequencing paragraph: identify Exercises 0–4 as the guided path and Exercise 5 as optional/early-finisher work until timing is validated.
- Workshop guide examples: change “four JW260 exercises” to “six JW260 exercises” and add one Exercise 4 and one Exercise 5 help prompt.
- Requirements and safety: state that binary artifact output depends on facilitator qualification and that fallback output is accepted.
- Troubleshooting table: add rows for unavailable standard capability/handoff and unavailable binary output.

Do not change existing Exercise 0–3 technical claims while making this navigation update.

Run:

```bash
python3 -m unittest tests/test_workshop_structure.py -v
```

Expected result: `test_root_readme_links_all_six_exercises` passes.

Commit only `README.md`:

```bash
git add README.md
git diff --cached --check
git commit -m "Link new JW260 build exercises"
```

If `README.md` contains pre-existing unstaged work that cannot be separated safely, use `git add -p README.md`; inspect every staged hunk and leave unrelated hunks unstaged.

### 7. Extend the optional `jw260-workshop-guide` support skill

Update `skills/jw260-workshop-guide/SKILL.md`:

- In step 1, change the exercise choice from `0, 1, 2, or 3` to `0 through 5`.
- In step 2, require reading `references/facilitator-qualification.md` before making claims about SAP-published capabilities, cross-skill data handoff, or PPTX/DOCX/XLSX output.
- Add a rule that the guide may explain and review a participant’s Exercise 4/5 design but must not silently choose the domain, outcome, or artifact on the participant’s behalf.
- Add a rule to recommend the documented fallback whenever qualification remains `TBD` or `No`.

Update `skills/jw260-workshop-guide/references/workshop-guide.md`:

- Change the workshop-purpose count to one readiness exercise plus five technical exercises.
- Add full sections for Exercise 4 and Exercise 5, using the goals, paths, timeboxes, test prompts, fallbacks, and success criteria from their READMEs.
- Update readiness checks from `ex0`–`ex3` to `ex0`–`ex5`.
- Add troubleshooting subsections for missing/unqualified SAP capabilities, failed data handoff, missing binary generation, and an artifact that downloads but does not open.
- Preserve the rule that custom skills have no external network access and do not directly connect to SAP backends.

Run the full test suite. Expected result: all tests pass.

Commit only the two support-skill files:

```bash
git add skills/jw260-workshop-guide/SKILL.md skills/jw260-workshop-guide/references/workshop-guide.md
git diff --cached --check
git commit -m "Extend JW260 workshop guide for capstone exercises"
```

Use interactive staging if either file contains pre-existing unrelated work.

### 8. Validate links, fixtures, placeholders, and participant flow

Run the automated tests and repository checks:

```bash
python3 -m unittest discover -s tests -v
git diff --check
git status --short
```

Expected result:

- All structural tests report `OK`.
- `git diff --check` prints nothing.
- `git status --short` contains no untracked Exercise 4/5 files; only intentional pre-existing work may remain.

Run this read-only Python link check from the repository root:

```bash
python3 - <<'PY'
import re
from pathlib import Path

root = Path('.')
missing = []
for md in root.rglob('*.md'):
    if '.git' in md.parts:
        continue
    text = md.read_text(encoding='utf-8')
    for target in re.findall(r'\[[^]]+\]\(([^)]+)\)', text):
        if target.startswith(('http://', 'https://', '#', 'mailto:')):
            continue
        path_text = target.split('#', 1)[0]
        if path_text and not (md.parent / path_text).resolve().exists():
            missing.append(f'{md}: {target}')
if missing:
    raise SystemExit('\n'.join(missing))
print('All local Markdown links resolve.')
PY
```

Expected output: `All local Markdown links resolve.`

Then perform two clean-reader walkthroughs using only repository instructions:

1. Exercise 4 fallback path: choose one goal card, copy the template, replace every placeholder, package it, and run all three prompt classes against the fixture.
2. Exercise 5 fallback path: choose one artifact brief, complete the template, produce the documented fallback, and score it against the rubric.

Record every question the reader must ask. Treat each as a documentation defect, fix it in the owning file, rerun tests, and commit fixes in small scoped commits.

### 9. Rehearse timing before promoting Exercise 5 to the core path

With a clean participant identity, rehearse:

- Exercise 4 live path if qualified, then its fixture fallback.
- Exercise 5 once for each of PPTX, DOCX, and XLSX when qualified, plus all three fallback formats.
- Partner review and one improvement cycle.

Record actual completion times and blocked-step recovery time in a temporary facilitator note outside the participant repository or in the existing organizer workspace. Keep Exercise 5 labeled optional unless the complete session, including setup and recovery margin, fits the allocated JW260 slot. If it does not fit, retain Exercise 5 as an early-finisher challenge rather than deleting it.

## Tests / validation summary

Follow red-green-refactor for the structural work:

1. Add `tests/test_workshop_structure.py` and observe failures for missing Exercises 4/5.
2. Add Exercise 4 minimally and verify only its failures disappear.
3. Add Exercise 5 minimally and verify its failures disappear.
4. Add qualification, root navigation, and support-guide integration until the suite passes.
5. Refactor duplicated wording into references only after all tests are green; rerun `python3 -m unittest discover -s tests -v` after every refactor.
6. Make one scoped commit per green increment. Never stage the whole dirty repository with `git add .`.

Final acceptance criteria:

- Root README and workshop-guide skill consistently describe Exercises 0–5.
- Exercise 4 offers exactly three selectable domain tracks and never implies direct SAP connectivity.
- Exercise 5 offers PPTX, DOCX, and XLSX contracts plus explicit Markdown/CSV fallbacks.
- Every new exercise has a goal, timebox, numbered procedure, exact test prompts, expected observations, troubleshooting/fallback, success criteria, and next/return navigation.
- All local Markdown links resolve.
- All importable skill folders have matching metadata names and no unresolved placeholders.
- Fixtures are synthetic and contain no credentials, tenant details, personal data, or production identifiers.
- A reviewer can complete both fallback paths using only the participant repository.
- Exercise 5 remains optional until a timed rehearsal demonstrates that it fits.

## Risks, tradeoffs, and open questions

- **Workshop duration:** Two additional exercises can overload the session. Mitigation: make Exercise 4 a choose-one track and Exercise 5 optional, with hard timeboxes and fallback artifacts.
- **Meaning of “standard skill”:** It may mean an SAP-published Joule capability, an existing workshop custom skill, or a template. This plan assumes an SAP-published capability combined with a custom workflow; confirm that interpretation with the feedback provider before freezing wording.
- **Tenant capability availability:** SuccessFactors, Ariba, or S/4HANA capabilities may not all exist in the workshop tenant. Do not publish capability names or live prompts until the facilitator qualification file is completed from observation.
- **Cross-skill handoff:** Even if a standard capability exists, its output may not be available to a custom skill in the same conversation. The CSV fallback is mandatory until this is observed.
- **PPTX/DOCX/XLSX generation:** The runtime may generate content but not an actual openable binary. Acceptance must distinguish “content contract passed” from “binary file generation qualified”; Markdown/CSV fallbacks prevent a blocked exercise.
- **Freestyle versus support:** Too much scaffolding defeats a freestyle exercise; too little causes blank-page delay. The proposed compromise supplies artifact briefs and a minimal TODO template but no finished skill.
- **Three Exercise 4 tracks increase maintenance:** One track would be simpler, but the feedback explicitly mentions SuccessFactors, Ariba, or S/4HANA. Keep one neutral fixture schema and one shared rubric to minimize duplication.
- **Existing dirty tree:** Current renumbering changes may overlap the same README and guide files. Use interactive staging and inspect cached diffs; do not assume every visible diff belongs to this implementation.
- **Open decision:** Should Exercise 4 participants be allowed to base their skill on the existing Exercise 2 or 3 custom skill instead when no SAP-published capability is available? The current plan uses the fixture fallback while preserving the SAP-published-capability architecture.
- **Open decision:** Should generated artifacts be retained as downloadable workshop outputs or discarded after review? Default to participant-local download only; do not commit generated binaries unless repository policy explicitly requests samples and licensing/size checks pass.
