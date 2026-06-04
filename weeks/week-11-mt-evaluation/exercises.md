# Week 11 Exercises

## A. Copy And Modify

Change the sorting line from:

```python
metric_summary.sort_values("chrf_pp", ascending=False)
```

to sort by `ter` ascending. Answer:

> Sorting by chrF++ chooses `___`, but sorting by TER chooses `___`.

## B. Guided Problem

Use `groupby()` to count simplified error labels:

```python
data.groupby(["mt_system", "simplified_error_label"]).size()
```

Answer: Which system has the most omission labels?

## C. Research-Style Task

Choose one segment where automatic metric and human label seem to tell different stories. Write 80-100 words explaining:

- the source sentence;
- the MT output;
- the reference;
- the metric or label;
- why a human reviewer is still needed.

## D. Caption Practice

> Figure 1 compares chrF++ across three synthetic MT systems for 12 segments. Higher chrF++ means greater overlap with the reference, but the figure does not prove overall translation quality.

## E. Source Note Practice

> Source checked: `___` (accessed `___`). It helps define `___`, but it does not prove that the best metric score is the best translation.
