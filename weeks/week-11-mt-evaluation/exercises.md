# Week 11 Exercises

## A. Source / MT / Reference Check

Look at segment `S001`.

1. Copy the Chinese source.
2. Copy the three Vietnamese MT outputs.
3. Copy the Vietnamese reference.
4. In one sentence, explain why the same source appears three times.

## B. Metric Direction

Fill in the blanks:

> BLEU and chrF++ are usually read as higher is better. TER is usually read as lower is better because it measures edits needed to match a reference.

Then answer:

```python
metric_summary.sort_values("chrf_pp", ascending=False)
metric_summary.sort_values("ter")
```

> Sorting by chrF++ chooses `___`, while sorting by TER chooses `___`.

## C. Human Review Labels

Use:

```python
human_review
severity_summary
```

Write 2 sentences:

1. Which MT profile needs revision most often?
2. Which labels are not errors?

## D. Segment-Level Stretch

Use `week11_segment_review_sample.csv`.

Pick one segment and compare:

- `segment_chrf_pp`
- `segment_ter`
- `error_type`
- `severity`
- `review_decision`

Write 3-4 sentences explaining why automatic metrics are helpful but incomplete.

## E. Caption Practice

Use this frame:

> Figure 1 compares `___` across `___` synthetic MT profiles for `___` source segments. Higher `___` means `___`, but the figure does not prove `___`.
