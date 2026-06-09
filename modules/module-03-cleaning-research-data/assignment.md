# Module 03 Assignment

## Submission Package

Submit a small paper-facing cleaning package:

1. cleaned learner-survey dataset;
2. cleaning log;
3. before/after data-quality figure;
4. label-normalization map;
5. 120-180 word Methods data-preparation note.

## Part A - Inspect

Open `module03_messy_learner_survey.csv`.

Write short answers:

- What is one row before cleaning?
- Which columns define a duplicate record?
- Which variables have missing, invalid, or mixed-type values?
- Which issue would most distort a figure?

## Part B - Clean

Using the notebook:

- remove the duplicate learner-date record;
- normalize `activity_group`;
- convert score, minutes, satisfaction, and date columns;
- set impossible values to missing instead of inventing replacements;
- preserve raw audit columns.

## Part C - Visualize Data Quality

Create or regenerate a before/after quality figure.

The figure must show:

- issue count before cleaning;
- unresolved issue count after cleaning;
- readable labels;
- exported PNG and SVG or PDF.

## Part D - Write

Write a Methods note that includes:

- source and synthetic teaching limitation;
- duplicate key;
- label normalization rule;
- type conversion rule;
- missing/out-of-range handling;
- which records are included in gain-score analysis.

## Optional Transfer

Choose one row from `module03_transfer_cleaning_bank.csv` and write how the same cleaning logic would apply to your own research area.
