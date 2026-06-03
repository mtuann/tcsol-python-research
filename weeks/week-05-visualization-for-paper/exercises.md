# Week 05 Exercises: Visualization for Papers

## Core Exercise A: Copy and Modify

Open the notebook and find the label map:

```python
activity_labels = {
    "result_complements": "Result complements",
    "measure_words": "Measure words",
    "vocabulary_review": "Vocabulary review",
    "word_order": "Word order",
}
```

Change one display label, for example:

```python
"measure_words": "Measure words / lượng từ"
```

Run the notebook again.

Answer:

- Did the data values change?
- Did the figure interpretation change?
- Why is it safer to change display labels in code than to edit the CSV?

## Core Exercise B: Guided Problem

Create two figures from the Week 05 dataset.

Checklist:

1. Load `week05_cleaned_tcsol_scores.csv`.
2. Filter to `usable_pre_post == True`.
3. Create a summary table with `n`, `mean_gain`, `median_gain`, `min_gain`, and `max_gain`.
4. Make a bar chart of mean `gain_score` by `activity_focus`.
5. Make a dot plot showing individual `gain_score` values.
6. Add axis labels and a sample-size note.
7. Export both figures as `.png` and `.svg`.

Expected checks:

| Check | Expected result |
|---|---:|
| Usable records | 25 |
| Activity groups | 4 |
| Highest mean gain | `result_complements` |
| Lowest mean gain | `word_order` |

## Core Exercise C: Research-Style Task

Write a 120-160 word figure interpretation.

Your paragraph must include:

- which figure you are interpreting;
- the strongest descriptive pattern;
- usable N;
- why the dot plot matters;
- one limitation.

Do not use causal verbs such as "caused", "proved", or "led to" unless the study design supports them.

## Stretch Exercise

Create a second figure grouped by `class_group`.

Answer:

- Does `class_group` answer the same research question as `activity_focus`?
- Which figure would you put in the paper first?
- What information belongs in the caption but not on the plot itself?

## Reflection

In one sentence, explain why a paper figure should show sample size or individual points when the dataset is small.
