# Module 02 Data Dictionary

Source check: 2026-06-09

## Dataset 1: `module02_toy_learner_survey_wide.csv`

Teaching role: toy dataset for wide-to-long reshaping.

Unit of observation before reshaping: one learner.

| Column | Meaning |
|---|---|
| `learner_id` | Anonymous learner identifier. |
| `research_track` | Application track: TCSOL or translation. |
| `activity_group` | Teaching or workflow activity group. |
| `course_start_date` | Start date of the short course. |
| `native_language` | Broad language-background category. |
| `cefr_start` | Baseline CEFR-like proficiency category. |
| `pre_vocab_score` | Vocabulary score before activity. |
| `post_vocab_score` | Vocabulary score after activity. |
| `pre_speaking_score` | Speaking score before activity. |
| `post_speaking_score` | Speaking score after activity. |
| `confidence_pre` | Self-reported confidence before activity, 1-5. |
| `confidence_post` | Self-reported confidence after activity, 1-5. |
| `minutes_on_task` | Minutes spent on the assigned activity. |

## Dataset 2: `module02_education_indicator_wide.csv`

Teaching role: academic indicator table for showing that public data also needs schema thinking.

Unit of observation before reshaping: one country-year-school-level.

| Column | Meaning |
|---|---|
| `country` | Country name. |
| `year` | Year. |
| `school_level` | School level. |
| `gross_enrollment_rate` | Teaching extract indicator. |
| `completion_rate` | Teaching extract indicator. |
| `student_teacher_ratio` | Teaching extract indicator. |
| `source_note` | Short source note for the teaching extract. |

Important: this is a synthetic teaching extract inspired by public education indicators. It is not a real official indicator download.

## Dataset 3: `module02_transfer_variable_bank.csv`

Teaching role: transfer scenarios for applying codebook thinking.

Unit of observation: one research-question scenario.

| Column | Meaning |
|---|---|
| `track` | Application track. |
| `paper_question` | Example paper-facing question. |
| `unit_of_observation` | Proposed row meaning. |
| `key_variables` | Variables likely needed. |
| `variable_types` | Expected variable type mix. |
| `tidy_action` | First data-structuring action. |
| `paper_output` | Writing or output artifact. |

## Output Tables

| File | Purpose |
|---|---|
| `outputs/tables/module02_tidy_learner_scores_long.csv` | Tidy learner-score table where one row is one learner-skill-time. |
| `outputs/tables/module02_tidy_education_indicators_long.csv` | Tidy indicator table where one row is one country-year-indicator. |
| `outputs/tables/module02_codebook.csv` | Codebook for learner-score analysis. |
| `outputs/tables/module02_schema_summary.csv` | Count of variable types by role. |
| `outputs/tables/module02_variable_map.csv` | Variable map for paper-relevant variables. |
| `outputs/tables/module02_caption_draft.md` | Caption draft for the tidy pre/post figure. |

## Output Figures

| File | Purpose |
|---|---|
| `outputs/figures/module02_tidy_prepost_example.png` | Main teaching figure generated from tidy data. |
| `outputs/figures/module02_tidy_prepost_example.svg` | Vector version for editing/web. |
| `outputs/figures/module02_tidy_prepost_example.pdf` | PDF version for paper/Overleaf workflow. |
| `outputs/figures/module02_variable_type_map.png` | Variable type map. |
| `outputs/figures/module02_tidy_codebook_workflow.png` | Workflow map from wide table to figure. |
