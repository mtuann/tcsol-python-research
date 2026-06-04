# Week 08 Exercises

## A. Copy And Modify

Add or change one display label in a copied output table, for example:

```python
display_labels = {"word_order": "Word order"}
error_frequency["display_label"] = error_frequency["error_category"].map(display_labels).fillna(error_frequency["error_category"])
```

to:

```python
display_labels = {"word_order": "Trật tự từ"}
error_frequency["display_label"] = error_frequency["error_category"].map(display_labels).fillna(error_frequency["error_category"])
```

Rerun the frequency table and confirm the raw `error_category` keys are unchanged.

## B. Read The Frequency Table

Answer in short phrases:

1. How many on-prompt coded error rows are there?
2. Which category is most frequent?
3. What percentage of coded errors does it represent?
4. Why should `no_error` rows not be counted as errors?

## C. Read The Crosstab

Choose one row in `outputs/tables/week08_error_by_target_structure.csv` and explain one high cell.

## D. Representative Example

Choose one row from `outputs/tables/week08_representative_examples.csv` and write:

- learner answer;
- expected answer;
- error category;
- one teaching note.

## E. Results Draft

Write 120-160 words using the frame in `assignment.md`. Mark:

- N;
- top category;
- crosstab pattern;
- teaching implication;
- limitation.
- one source note.

## F. Stretch

Recode one example in a copied DataFrame and explain why the new code is clearer. Do not edit the raw CSV.
