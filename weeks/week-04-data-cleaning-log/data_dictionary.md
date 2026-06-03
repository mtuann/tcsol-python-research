# Week 04 Data Dictionary

Dataset: `data/raw/week04_messy_tcsol_scores.csv`

Teaching purpose: beginner practice for cleaning a small TCSOL classroom dataset.

Unit of observation: one learner's pre/post score record for one short activity.

Important: this is synthetic teaching data, not real student data.

| Column | Type before cleaning | Intended cleaned type | Meaning | Known issue |
|---|---|---|---|---|
| `learner_id` | text | text | anonymized learner ID | none |
| `class_group` | text | category A-D | class section | inconsistent labels such as `a`, `Class A`, extra spaces |
| `activity_focus` | text | category | teaching focus | inconsistent spelling, spaces, hyphens, underscores |
| `pre_score` | text/number | numeric | score before activity, 0-100 | missing codes and invalid text |
| `post_score` | text/number | numeric | score after activity, 0-100 | missing codes |
| `attendance_hours` | text/number | numeric | attended hours during the activity | missing code `not recorded` |
| `completed` | text | yes/no/missing | whether the activity record is complete | variants such as `Y`, `YES`, `n`, blank |
| `self_confidence` | text/number | numeric | self-rating 1-5 | should be numeric |
| `gain_score` | derived | numeric | post_score minus pre_score | created only in cleaned data |

## Standard Labels

`class_group`: `A`, `B`, `C`, `D`

`activity_focus`:

- `measure_words`
- `result_complements`
- `word_order`
- `vocabulary_review`

`completed`:

- `yes`
- `no`
- missing when raw status is blank or unclear

## Cleaning Rules

1. Preserve the raw CSV.
2. Create a cleaned copy in code.
3. Treat blank cells, `NA`, `missing`, and `not recorded` as missing.
4. Convert numeric columns with `pd.to_numeric(..., errors="coerce")`.
5. Do not replace missing scores with zero.
6. Record every major decision in the cleaning log.
