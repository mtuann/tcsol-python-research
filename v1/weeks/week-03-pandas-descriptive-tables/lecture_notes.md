# Week 03 Lecture Notes: pandas Basics and Descriptive Tables

## Core Idea

`pandas` helps turn a table into research evidence. In Week 03, the learner does not need to memorize the whole library. The goal is to use a few stable moves:

1. load a CSV;
2. look at the rows and columns;
3. select only useful columns;
4. filter rows;
5. create a simple derived column;
6. summarize groups;
7. export a descriptive table.

The research habit is more important than the syntax: every summary table must answer a small question and be accompanied by a cautious caption.

## What Is a DataFrame?

A `DataFrame` is a table that Python can work with. For this course, explain it like this:

> A DataFrame is a research table in memory. Rows are observations; columns are variables; Python can summarize them without changing the raw CSV.

This beginner definition is enough. Avoid explaining indexes deeply in Week 03.

## The Dataset

File: `data/raw/week03_tcsol_scores.csv`

Unit of observation: one learner's pre/post score record for one short learning activity.

Main columns:

- `learner_id`: anonymized learner ID.
- `class_group`: class section A-D.
- `activity_focus`: teaching focus.
- `pre_score`: score before activity, 0-100.
- `post_score`: score after activity, 0-100.
- `attendance_hours`: hours attended during the short activity.
- `completed`: whether the learner completed the activity record.

The dataset is intentionally small and clean. Week 04 will introduce cleaning.

## Code Pattern

```python
import pandas as pd

df = pd.read_csv("weeks/week-03-pandas-descriptive-tables/data/raw/week03_tcsol_scores.csv")
df.head()
```

Read this as:

- `pd` is the short name for pandas.
- `read_csv` opens the table.
- `head()` shows the first rows, like a quick safety check.

## Select Columns

```python
score_columns = ["learner_id", "class_group", "activity_focus", "pre_score", "post_score"]
scores = df[score_columns]
```

Selection is useful because papers rarely need every raw column. The learner should ask:

- Which columns answer the research question?
- Which columns are metadata?
- Which columns should stay in the raw data but not appear in the paper table?

## Filter Rows

```python
complete = df[df["completed"] == "yes"]
```

Read this as:

> Keep only rows where `completed` is `yes`.

This is not "deleting data." It is creating a new table for the summary. The raw CSV remains unchanged.

## Create a Derived Column

```python
complete = complete.assign(gain_score=complete["post_score"] - complete["pre_score"])
```

`gain_score` is a derived variable. It is not in the raw file, but it helps answer the research question.

Writing note:

- Say "gain score was calculated as post-test minus pre-test."
- Do not say "improvement was caused by the activity."

## Group and Summarize

```python
summary = (
    complete
    .groupby("activity_focus")
    .agg(
        n_learners=("learner_id", "count"),
        mean_pre=("pre_score", "mean"),
        mean_post=("post_score", "mean"),
        mean_gain=("gain_score", "mean")
    )
    .reset_index()
)
```

Plain-language explanation:

- Split rows by `activity_focus`.
- Calculate one set of numbers for each group.
- Return a new summary table.

This is the core Week 03 skill.

## Export the Table

```python
summary.to_csv("weeks/week-03-pandas-descriptive-tables/outputs/tables/week03_group_summary.csv", index=False)
```

The exported table is the artifact that can move into a paper draft.

## Caption Formula

Use this formula:

```text
Table 1. [Main pattern]. Data are from [source], N = [sample size].
Scores are on a [scale]. The table reports [method/statistic].
This descriptive table does not establish [limitation].
```

Example:

> Table 1. The measure-word group shows the largest descriptive average gain (12.1 points), closely followed by result-complement activities (12.0 points). Data are from an instructor-created Week 03 teaching dataset, N = 31 completed learner records. Scores are classroom scores on a 0-100 scale; gain is calculated as post-test minus pre-test. The table is descriptive: activity focus is linked to class section in this toy dataset, so the result does not establish a causal effect.

## Common Mistakes

Mistake 1: Treating `groupby` as magic.

Fix: Always say "group rows by X, calculate Y."

Mistake 2: Forgetting N.

Fix: Include `n_learners` in the table and caption.

Mistake 3: Claiming causality.

Fix: Use "shows", "suggests descriptively", "in this dataset" instead of "proves" or "caused".

Mistake 4: Editing the output manually.

Fix: Change the code and re-run the notebook.

## Transfer to Other Research Tracks

The same pattern works later:

| Track | Group by | Summarize |
|---|---|---|
| TCSOL | `activity_focus` | mean score gain |
| Contrastive analysis | `contrast_point` | number of examples |
| MTPE | `error_label` | count and severity |
| Education policy | `theme_code` | number of excerpts |

Week 03 uses TCSOL because the numeric table is easy. The habit transfers.
