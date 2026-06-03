# Week 03 Exercises: pandas Descriptive Tables

## Core Exercise A: Copy and Modify

Open the notebook and find this line:

```python
group_variable = "activity_focus"
```

Change it to:

```python
group_variable = "class_group"
```

Run the summary cell again.

Answer:

- How many groups appear?
- Which group has the highest `mean_gain`?
- Does this table answer the same research question as grouping by `activity_focus`?

## Core Exercise B: Guided Problem

Use the Week 03 dataset to create a table for completed learners only.

Checklist:

1. Load `week03_tcsol_scores.csv`.
2. Filter rows where `completed == "yes"`.
3. Create `gain_score = post_score - pre_score`.
4. Group by `activity_focus`.
5. Calculate:
   - `n_learners`;
   - `mean_pre`;
   - `mean_post`;
   - `mean_gain`.
6. Round averages to 1 decimal place.
7. Export the table.

Write one sentence:

> The largest descriptive average gain appears in...

## Core Exercise C: Research-Style Task

Write a 120-160 word interpretation of the table.

Your paragraph must include:

- the research question;
- the group with the largest average gain;
- N;
- one limitation;
- one next step for teaching or data collection.

Do not claim causality.

## Stretch Exercise

Create a second summary table grouped by both `class_group` and `activity_focus`.

Then answer:

- Is each class group linked to one activity focus in this teaching dataset?
- Why would this design make causal interpretation difficult?

## Reflection

In one sentence, explain why `groupby` is useful for paper writing.
