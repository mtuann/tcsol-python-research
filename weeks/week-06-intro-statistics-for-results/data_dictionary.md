# Week 06 Data Dictionary

| Column | Type | Meaning | Week 06 Use |
|---|---|---|---|
| `learner_id` | text | synthetic learner identifier | row identifier |
| `class_group` | text | class label | optional grouping |
| `activity_focus` | text | teaching activity focus | group for statistics |
| `pre_score` | numeric | pre-test score | baseline score |
| `post_score` | numeric | post-test score | post-activity score |
| `attendance_hours` | numeric | synthetic attendance hours | optional covariate |
| `completed` | boolean | completed activity flag | cleaning check |
| `self_confidence` | numeric | learner confidence rating | optional future analysis |
| `gain_score` | numeric | `post_score - pre_score` | main Week 06 outcome |
| `usable_pre_post` | boolean | row has usable pre/post scores and completed status | required filter |

Important: this is a synthetic teaching dataset for learning workflow, not real student data.

## Provenance

- Source role: synthetic classroom-style dataset for Week 05 cleaning and Week 06 statistics practice.
- Privacy: contains no real learner records.
- SHA-256: `175469cd9120b36a467d0e0b439f78859525841555c6a30bc5de0777edb9137a`
- Required filter: use rows where `usable_pre_post == True` before computing Week 06 statistics.
