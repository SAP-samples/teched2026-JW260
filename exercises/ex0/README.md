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
