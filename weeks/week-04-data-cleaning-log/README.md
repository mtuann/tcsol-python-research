# Week 04: Data Cleaning Log

## Research Frame

- Research area: short-term Chinese teaching and TCSOL, with transfer to contrastive, MTPE, and education policy datasets.
- Small research question: After cleaning messy classroom records, which activity focus has usable pre/post score evidence?
- Why this matters: beginner research data often comes from forms, spreadsheets, or manual notes. A table is not ready for analysis until labels, missing values, and numeric columns are checked and documented.

## Python Skill

- Main skill: build a small, reproducible data cleaning workflow.
- Supporting skills: inspect missing values, normalize text labels, convert score columns to numbers, create a cleaning log, export cleaned data.
- Functions/libraries: `pandas`, `read_csv`, `isna`, `str.strip`, `str.lower`, `replace`, `map`, `to_numeric`, `assign`, `to_csv`.

## Writing Support

- Paper section supported: Methods / Data preparation.
- Writing output: one cleaning decision note plus one before/after cleaning table.
- Tool support: write the cleaning note in the notebook, then paste it into Word. Zotero source notes continue; Overleaf is not needed.
- Sentence frame: "Before analysis, we standardized [labels], converted [columns] to numeric values, and treated [missing value rule] as missing. These decisions changed [before/after pattern] and were recorded in a cleaning log."
- Common writing risk: hiding cleaning decisions or presenting a cleaned dataset as if it were the original raw data.

## Learning Objectives

By the end of this week, the learner can:

1. Explain why raw data and cleaned data must be kept separate.
2. Detect missing values and inconsistent labels in a small dataset.
3. Normalize labels without manually editing the raw CSV.
4. Convert score columns to numeric values safely with `errors="coerce"`.
5. Export a cleaned dataset and a cleaning log.
6. Write a Methods-style cleaning note with clear limitations.

## Required Outputs

- [ ] Notebook runs from top to bottom.
- [ ] Raw dataset is loaded from `data/raw/week04_messy_tcsol_scores.csv`.
- [ ] Cleaned dataset is exported to `data/processed/week04_cleaned_tcsol_scores.csv`.
- [ ] Cleaning log is exported to `outputs/tables/week04_cleaning_log.csv`.
- [ ] Before/after issue table is exported to `outputs/tables/week04_cleaning_summary.csv`.
- [ ] Cleaning note explains label normalization, numeric conversion, missing values, and limitations.
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
| Pre-class | 25 min | Inspect the messy CSV and mark suspicious cells. |
| Lecture | 45 min | Explain raw vs cleaned data, missing values, label normalization, and cleaning logs. |
| Live coding | 45 min | Clean the TCSOL dataset and export cleaned files. |
| Guided practice | 35 min | Learner changes one mapping rule and checks the before/after table. |
| Writing bridge | 20 min | Draft a Methods-style cleaning decision note. |
| Homework | 90 min | Submit notebook, cleaned CSV, cleaning log, before/after table, and note. |

## Core vs Stretch

Core:

- keep raw data unchanged;
- normalize `class_group`, `activity_focus`, and `completed`;
- convert `pre_score`, `post_score`, `attendance_hours`, and `self_confidence`;
- create `gain_score`;
- export cleaned data and cleaning log;
- write one cleaning decision note.

Stretch:

- add a rule for a new label variant;
- compare summaries before and after cleaning;
- create a second cleaning log entry for a decision you would make differently with real data;
- explain how the same workflow would apply to MTPE or policy coding labels.

Instructor-only:

- discuss why cleaning is a research decision, not only a technical step;
- preview Week 05 visualization by showing that a figure should use cleaned labels;
- emphasize that real classroom data must be anonymized before publication.
