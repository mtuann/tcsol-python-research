# Week 04 Rubric

Total: 100 points

| Criterion | Points | Strong work |
|---|---:|---|
| Code correctness | 25 | Notebook runs top to bottom; raw CSV loads; label normalization, numeric conversion, gain score, and exports all work. |
| Data cleaning decisions | 20 | Cleaning rules are explicit; raw data is preserved; missing values are treated cautiously. |
| Cleaning log quality | 15 | Log includes step, column, problem, decision, and reason. |
| Before/after table | 15 | Table clearly shows issue counts or label counts before and after cleaning. |
| Research writing | 15 | Cleaning note explains method, N, and limitation without claiming the data are perfect. |
| Reproducibility | 10 | Paths are stable; outputs are produced by code; source/access date are recorded. |

## Common Deductions

- -15 if the raw CSV is edited manually.
- -10 if missing scores are replaced with zero without justification.
- -10 if label mappings are hidden or undocumented.
- -10 if cleaned CSV or cleaning log is not exported.
- -5 if the cleaning note omits a limitation.

## Track-Specific Bonus Awareness

The core dataset is TCSOL, but the learner can earn instructor feedback credit by explaining how the same cleaning log idea applies to:

- contrastive categories in a codebook;
- MTPE error labels;
- education policy source names or date fields.
