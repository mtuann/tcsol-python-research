# Module 03 Data Dictionary

All datasets are synthetic teaching data. They contain no real participant information.

## `module03_messy_learner_survey.csv`

Unit before cleaning: one learner activity record.

Recommended duplicate key: `learner_id + survey_date`.

| Variable | Type before cleaning | Clean type | Meaning | Cleaning note |
|---|---|---|---|---|
| `learner_id` | text | identifier | learner code | synthetic ID only |
| `research_track` | text | categorical | learner's paper track | strip and standardize labels |
| `activity_group` | text | categorical | short teaching activity condition | normalize case, spaces, underscores, and hyphens |
| `cefr_start` | text | ordinal | starting proficiency band | keep as ordered label, do not average |
| `survey_date` | text | date | activity survey date | parse with `pd.to_datetime(..., errors="coerce", format="mixed")` |
| `pre_vocab_score` | text/numeric | numeric | vocabulary score before activity | convert with `pd.to_numeric(..., errors="coerce")`; valid range 0-100 |
| `post_vocab_score` | text/numeric | numeric | vocabulary score after activity | convert with audit; valid range 0-100 |
| `minutes_on_task` | text/numeric | numeric | approximate activity time | valid range is non-negative |
| `satisfaction_1_5` | text/numeric | ordinal numeric | 1-5 satisfaction rating | valid values 1, 2, 3, 4, 5 |
| `notes` | text | text | audit note for teaching | not used as evidence |

## `module03_cleaned_learner_survey.csv`

Additional audit columns:

| Variable | Meaning |
|---|---|
| `gain_vocab_score` | `post_vocab_score - pre_vocab_score`, calculated only when both scores exist |
| `complete_vocab_pair` | `True` when pre and post vocabulary scores are both available |
| `score_issue` | `True` when a score violated the valid range before cleaning |
| `*_raw` columns | original raw values preserved for audit |

## `module03_messy_education_indicators.csv`

Unit before cleaning: one country-year-school-level record.

| Variable | Type before cleaning | Clean type | Meaning | Cleaning note |
|---|---|---|---|---|
| `country_raw` | text | categorical | country label | normalize variants such as `Viet Nam` and `Vietnam` |
| `year` | text/numeric | integer | indicator year | convert to nullable integer |
| `school_level` | text | categorical | school level | normalize spaces and underscores |
| `completion_rate` | text percent | numeric | completion rate percentage | remove `%`; treat `--` and `n/a` as missing |
| `student_teacher_ratio` | text/numeric | numeric | students per teacher | convert to numeric |
| `policy_note` | text | text | teaching context note | not a measured outcome |

## Cleaning Policy

- Do not overwrite raw input files.
- Preserve audit columns for any value that was changed or coerced.
- Use `NA` for unknown or invalid values instead of inventing replacements.
- Log every cleaning decision that affects row count, group labels, numeric conversion, or figure interpretation.
- Caption and Methods notes should report the observation key, row count after cleaning, and any exclusions from analysis.
