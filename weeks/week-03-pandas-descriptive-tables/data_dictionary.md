# Week 03 Data Dictionary

Dataset: `data/raw/week03_tcsol_scores.csv`

Teaching purpose: beginner pandas practice for descriptive summaries.

Unit of observation: one anonymized learner's pre/post score record for one short Chinese learning activity.

Source: instructor-created synthetic teaching dataset.

Access date for course site: 2026-06-03.

License/reuse note: use for this course and teaching demonstrations; do not treat it as empirical classroom evidence.

Missing value codes: none in the raw Week 03 CSV. The row with `completed = no` is complete as a row but excluded from the main Week 03 completed-record summary.

| Column | Type | Meaning | Example | Notes |
|---|---|---|---|---|
| `learner_id` | string | anonymized learner ID | `S001` | No real names. |
| `class_group` | string | class section | `A` | Used for optional grouping. |
| `activity_focus` | string | short teaching focus | `measure_words` | Main grouping variable. |
| `pre_score` | integer | score before activity | `58` | 0-100 classroom score. |
| `post_score` | integer | score after activity | `72` | 0-100 classroom score. |
| `attendance_hours` | float | hours attended | `5.5` | Used as context, not main analysis. |
| `completed` | string | completed record flag | `yes` | Core filter for summary. |

Derived variable:

| Column | Formula | Meaning |
|---|---|---|
| `gain_score` | `post_score - pre_score` | descriptive score change |

Privacy note:

- IDs are synthetic.
- No legal names, contact details, or identifiable learner information appear in this dataset.

Interpretation note:

- The dataset is for teaching.
- It can support descriptive practice only.
- It cannot establish causal effects.
