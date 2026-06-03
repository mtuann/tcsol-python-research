# Week 03: pandas Basics and Descriptive Tables

## Research Frame

- Research area: short-term Chinese teaching and TCSOL.
- Small research question: Which activity group shows the largest descriptive score gain after a short Chinese learning activity?
- Why this matters: a beginner teaching study often starts with a modest classroom table. Before using statistics, the learner must know how to summarize rows into a clear table that can support a cautious caption.

## Python Skill

- Main skill: use `pandas` to create a descriptive table.
- Supporting skills: load a CSV, inspect rows, select columns, filter rows, create a new column, use `groupby`, export a table.
- Functions/libraries: `pandas`, `read_csv`, `head`, column selection, boolean filtering, `assign`, `groupby`, `agg`, `round`, `to_csv`.

## Writing Support

- Paper section supported: Results.
- Writing output: one descriptive table caption plus a 120-160 word interpretation.
- Tool support: write in the notebook first, then paste the caption into Word; Zotero setup can begin with source metadata, but citation insertion is optional this week.
- Sentence frame: "Table 1 shows that [group] had the highest average gain ([number] points), but this result is descriptive because [limitation]."
- Common writing risk: claiming that the activity caused improvement when the table only describes a small teaching dataset.

## Learning Objectives

By the end of this week, the learner can:

1. Explain what a `DataFrame` is in plain research language.
2. Select columns and filter rows without changing the original raw CSV.
3. Use `groupby` to summarize a classroom dataset by activity group.
4. Export a descriptive table as CSV.
5. Write a caption that reports N, variables, method, main pattern, and limitation.

## Required Outputs

- [ ] Notebook runs from top to bottom.
- [ ] Raw dataset is loaded from `data/raw/week03_tcsol_scores.csv`.
- [ ] A filtered complete-case table is created.
- [ ] A descriptive table is exported to `outputs/tables/week03_group_summary.csv`.
- [ ] Caption explains N, variables, units, method, and main finding.
- [ ] Interpretation paragraph separates description, inference, and limitation.
- [ ] Writing output is ready to paste into Word or the final paper draft.
- [ ] Sources are cited with links and access date.

## Files

- Slides: `slides.html`
- Interactive demo: `interactive_demo.html`
- Lecture notes: `lecture_notes.md`
- Notebook: `live_coding.html`, source `live_coding.ipynb`
- Exercises: `exercises.md`
- Assignment: `assignment.md`
- Data dictionary: `data_dictionary.md`
- Rubric: `rubric.md`
- Readings: `readings.md`

## Weekly Rhythm

| Stage | Time | Plan |
|---|---:|---|
| Pre-class | 30 min | Read notes and inspect the CSV columns. |
| Lecture | 45 min | Explain DataFrame, select, filter, groupby, and table captions. |
| Live coding | 40 min | Build the descriptive table from the raw CSV. |
| Guided practice | 35 min | Learner changes the grouping variable and interprets the output. |
| Writing bridge | 15 min | Draft a caption and one cautious Results sentence. |
| Homework | 90 min | Submit notebook, exported table, caption, interpretation, and limitation. |

## Core vs Stretch

Core:

- load the CSV;
- select columns;
- filter `completed == "yes"`;
- compute `gain_score`;
- group by `activity_focus`;
- write one caption.

Stretch:

- group by both `class_group` and `activity_focus`;
- sort the table by `mean_gain`;
- export both a CSV and Markdown table;
- draft a Word/Zotero source note.

Instructor-only:

- explain why descriptive summaries do not establish causality;
- preview Week 04 cleaning issues: missing values, labels, type conversion;
- show how the same `groupby` pattern can later summarize contrastive examples, MTPE error labels, or policy themes.
