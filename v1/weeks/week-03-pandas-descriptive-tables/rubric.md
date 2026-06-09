# Week 03 Rubric

Total: 100 points

| Criterion | Points | Strong work |
|---|---:|---|
| Code correctness | 25 | Notebook runs top to bottom; CSV loads correctly; filter, `gain_score`, `groupby`, and export all work. |
| Code clarity | 15 | Variables are readable; notebook sections are organized; no unnecessary code clutter. |
| Data handling | 15 | Raw data is preserved; completed rows are filtered intentionally; N is reported. |
| Table quality | 15 | Summary table has clear group labels, N, mean pre/post/gain, consistent rounding, and exported CSV. |
| Research writing and interpretation | 20 | Caption and paragraph connect to the research question, report main pattern, and include a limitation without causal overclaiming. |
| Reproducibility | 10 | Paths are stable; source/access date are recorded; output is produced by code, not manual editing. |

## Common Deductions

- -10 if the notebook only works after manual cell reordering.
- -10 if the table omits N.
- -10 if the interpretation claims causality.
- -5 if the exported table has inconsistent rounding.
- -5 if source/access date is missing.

## Track-Specific Bonus Awareness

The core dataset is TCSOL, but the learner can earn instructor feedback credit by explaining how the same `groupby` logic could later apply to:

- contrastive examples by `contrast_point`;
- MTPE segments by `error_label`;
- policy excerpts by `theme_code`.
