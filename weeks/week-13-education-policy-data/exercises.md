# Week 13 Exercises

## A. Metadata Check

Choose row `C001`.

1. Copy `title`, `issuing_body`, `issue_date`, `url`, and `access_date`.
2. Explain why each field matters for a paper.
3. Mark which fields help readers find the source again.

## B. Timeline Direction

Run:

```python
policy.sort_values("issue_date_parsed")[["coding_id", "title", "issue_date_parsed"]]
```

Answer:

> The earliest source date is `___`; the latest source date is `___`.

## C. Coding Counts

Use `week13_policy_area_summary.csv`.

Write 2 sentences:

1. Which policy area appears most often?
2. Which areas appear only once?

## D. Evidence-Type Caution

Use `week13_source_type_summary.csv` and `week13_theme_by_source_crosstab.csv`.

Mini guide:

- `policy_text`: a policy source says something should happen.
- `statistical_indicator`: a bulletin reports a descriptive number or indicator family.
- `metadata`: a source defines how indicators should be understood.
- `method_model`: a source models how policy coding can be organized.
- `report`: a comparative source summarizes policy patterns.

Write 2-3 sentences explaining why these evidence types should not be mixed as if they were the same kind of proof.

## E. Stretch: Revise One Code

Pick one row and propose a better `theme_code`. Explain why the new code is clearer, and whether the change affects the policy-area summary.
