# Week 03 Instructor Notes

## Teaching Goal

Week 03 is the first real pandas week. Keep the learner's cognitive load low:

- one small dataset;
- one research question;
- one new library;
- one paper-facing table.

Do not introduce data cleaning deeply. If learners notice `completed == "no"`, frame it as a simple filter. Missing values, type conversion, and label normalization belong to Week 04.

## Key Explanation

Use this phrase repeatedly:

> `groupby` means: group rows by one column, then calculate a statistic for each group.

Then map it to research:

> A paper table usually compares groups, themes, labels, or time points. `groupby` is how Python makes that comparison reproducible.

## Likely Confusions

1. Learner thinks `df["column"]` is a file path.
   - Explain: square brackets select a column inside a table.

2. Learner thinks filtering deletes rows.
   - Explain: filtering creates a new table; the raw CSV remains unchanged.

3. Learner thinks higher mean gain proves activity effectiveness.
   - Explain: this is descriptive classroom data. There is no random assignment or control group.

4. Learner wants to memorize syntax.
   - Redirect to pattern: load, inspect, select, filter, create, summarize, export, write.

## Timing

- 10 min: recap Week 02 row/column/schema.
- 15 min: DataFrame concept and `read_csv`.
- 15 min: select/filter/create `gain_score`.
- 20 min: `groupby` and summary table.
- 15 min: caption writing and causality caution.
- 20 min: guided practice.

## Transfer Examples

Use these only after the core TCSOL example works:

- Contrastive analysis: group examples by `contrast_point`.
- MTPE: group segments by `error_label`.
- Education policy: group excerpts by `theme_code`.

## Source Audit

Checked on 2026-06-03:

- pandas Getting Started and GroupBy documentation.
- JupyterLab User Guide.
- Zotero Word Processor Plugin documentation.
- Tidy Data paper page.

## Overleaf Boundary

Do not teach Overleaf in Week 03. Word + Zotero setup may begin as a light preview because captions and source notes now exist.
