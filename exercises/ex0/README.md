# Exercise 0: Log In, Set Up, and Get Ready

## Goal

Sign in to the workshop environment, prepare the repository files, and confirm that Joule Work is ready before starting the technical exercises.

## What You Need

- The workshop tenant URL supplied by your facilitator.
- The workshop identity assigned to you by your facilitator.
- This repository, downloaded or cloned to your computer.

## Step 1: Sign In

1. Open the workshop tenant URL supplied by your facilitator.
2. Sign in with your assigned workshop identity.
3. Complete the authentication process if prompted.
4. Confirm that Joule Work opens successfully.

The empty conversation screen is your starting point. The exact greeting can vary by time of day.

If sign-in fails, stop and contact the facilitator. Do not use another participant's identity.

## Step 2: Check Joule Work Access

1. Confirm that agentic thinking mode is available. You will select it when testing skills in the exercises. You can test if it is there by opening a new conversation > +-icon > agentic thinking

![Joule Work new conversation screen with the message input ready](images/00-05-agentic-thinking.png)

2. Open **User menu > Explore Skills**.

   ![User menu with Explore Skills available](images/00-02-user-menu-explore-skills.png)

3. Confirm that you can open **My Skills**.
4. Look for the **Import** control.
   - If it is available, you will import the exercise skills yourself.

The Explore Skills page provides **My Skills**, **Active Skills**, and the **Import** control:

![Explore Skills page with tabs and Import control](images/00-03-explore-skills-import.png)

Selecting **Import** opens the skill import dialog. It also states the custom-skill sandbox boundary:

![Import Skill dialog with folder and file controls and the no-network security notice](images/00-04-import-skill-dialog.png)


## Step 3: Prepare the Workshop Files

1. Download or clone this repository.
2. Open the repository and locate the `exercises` folder.
3. Confirm that it contains `ex0`, `ex1`, `ex2`, `ex3`, `ex4`, and `ex5`.
4. Open `exercises/ex1/` and confirm that both `broad-greeter/` and `workshop-greeter/` contain a `SKILL.md` file.

## Step 4: Understand Import Formats

Joule Work imports either a `SKILL.md` file directly or an unzipped skill folder. Do not create a ZIP archive for this workshop.

For a simple skill, select its `SKILL.md` file:

```text
workshop-greeter/
└── SKILL.md
```

For a skill with supporting files, select the complete unzipped skill folder so its `SKILL.md` and referenced files stay together:

```text
gross-margin-calculator/
├── SKILL.md
├── references/
│   └── formulas.md
└── scripts/
    └── calculate_margin.py
```


## Step 5: First Interaction

Once the readiness check is complete, open a new conversation, enable agentic thinking mode, and send these prompts one at a time to get a feel for how Joule communicates.

1. `Who are you and what can you help me with?`

   Joule introduces itself and summarizes its capabilities.

2. `What are your limitations? What can't you do?`

   Knowing what Joule won't do is just as useful as knowing what it will.

3. `Can you do a quick calculation? If we raised 47 purchase orders at an average value of $12,400 each, what is the total spend?`

   Expected answer: **$582,800**. A quick way to confirm the conversation is live and responding correctly.

## Optional: Explore SAP-published Skills

The workshop exercises focus on custom skills you build yourself. Before you start, you can also explore what Joule's pre-shipped SAP skills can do on their own. These skills connect to live S/4HANA and SuccessFactors data in the workshop tenant.

### Enable the LOB skills

1. Open **User menu > Explore Skills**.
2. On the **Published by SAP** tab, find the SAP-published skills. They appear alongside any custom skills you have imported. SAP-published skills are marked with SAP as the publisher.
3. Enable `S4 HANA public` and `Successfactors HCM` using the toggle on each card.
4. Confirm that both appear under **Active Skills**.
5. Open a new conversation and enable agentic thinking mode.

### S/4HANA — purchasing and finance data

Try these prompts one at a time:

- `Show me my last 5 purchase orders.`
- `Are there any open purchase orders over $50,000?`
- `Show me all open vendor invoices from last month.`

Joule pulls data from S/4HANA without you naming a transaction code or Fiori app.

### SuccessFactors — HR and org data

Try these prompts one at a time:

- `What is my current job title and cost centre?`
- `Who is my manager and who reports to me?`
- `How many employees do we have in the Manufacturing division?`

Joule identifies your user account automatically and returns live data from SuccessFactors.

> [!note]
> The exact values you see depend on the workshop identity assigned to you. Counts and names will differ from the screenshots in JW160. If a skill toggle is not visible, the skill is not available in this tenant — skip that section and continue to the Readiness Check.

---

## Readiness Check

Before continuing, confirm all applicable items:

- [ ] I can sign in to the workshop tenant with my assigned identity.
- [ ] Joule Work opens successfully.
- [ ] I can open **User menu > Explore Skills > My Skills**.
- [ ] I can import skills, or the facilitator has confirmed the preimported-skill fallback.
- [ ] Agentic thinking mode is available.
- [ ] I have the repository and can locate all six exercise folders.
- [ ] I understand when to import a `SKILL.md` file or an unzipped skill folder.

Continue to - [Exercise 1: Compare Skill Behavior](../ex1/README.md)
