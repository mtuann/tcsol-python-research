# Week 04 Exercises: Data Cleaning Log

## Core Exercise A: Copy and Modify

Open the notebook and find the activity mapping:

```python
activity_map = {
    "measure words": "measure_words",
    "result complements": "result_complements",
    "word order": "word_order",
    "vocab review": "vocabulary_review",
    "vocabulary review": "vocabulary_review",
}
```

Add one new variant:

```python
"measure word": "measure_words"
```

Run the notebook again.

Answer:

- Did the number of unmapped activity labels change?
- Why is it safer to change the mapping rule than to edit the CSV by hand?

## Core Exercise B: Guided Problem

Create a cleaned version of the Week 04 dataset.

Checklist:

1. Load `week04_messy_tcsol_scores.csv`.
2. Inspect missing values with `isna().sum()`.
3. Normalize `class_group`.
4. Normalize `activity_focus`.
5. Normalize `completed`.
6. Convert score columns with `pd.to_numeric(..., errors="coerce")`.
7. Create `gain_score`.
8. Export cleaned data.
9. Export a cleaning log.

Write one sentence:

> After cleaning, the main remaining limitation is...

## Core Exercise C: Research-Style Task

Write a 100-150 word cleaning decision note.

Your note must include:

- raw data was preserved;
- which labels were standardized;
- which numeric columns were converted;
- what happened to invalid or missing values;
- how many rows are usable for a pre/post summary;
- one limitation.

Do not say the data became perfect.

## Stretch Exercise

Create a before/after table for `activity_focus`.

Answer:

- How many raw label variants appeared before cleaning?
- How many standard labels remain after cleaning?
- What would happen to a Week 03 `groupby` table if these labels were not cleaned?

## Reflection

In one sentence, explain why data cleaning belongs in the Methods section of a paper.
