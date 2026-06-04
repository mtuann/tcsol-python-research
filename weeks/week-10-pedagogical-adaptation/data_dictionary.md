# Week 10 Data Dictionary

| Column | Type | Meaning | Week 10 Use |
|---|---|---|---|
| `activity_id` | text | synthetic activity identifier | row identifier |
| `phenomenon` | text | Week 09 contrastive phenomenon | grouping and ranking |
| `activity_title` | text | short name of the activity | lesson plan table |
| `lesson_phase` | text | exact CSV values: `review`, `notice`, `compare`, `controlled_practice`, `communicative_practice`, `feedback`, `assessment` | phase-minutes table |
| `target_level` | text | approximate learner level | scope check |
| `target_form` | text | Chinese form or pattern | teaching focus |
| `vietnamese_bridge` | text | Vietnamese support/contrast | contrastive explanation |
| `contrastive_focus` | text | what learners notice or practice | activity rationale |
| `activity_type` | text | activity format | design description |
| `minutes` | numeric | planned minutes | pacing figure |
| `preparation_load` | numeric | 1 low to 3 high | adaptation score |
| `learner_difficulty` | numeric | 1 low to 3 high; used here as instructional need, not proof that harder is always better | adaptation score |
| `communicative_value` | numeric | 1 low to 3 high | adaptation score |
| `week09_priority_score` | numeric | Week 09 phenomenon priority score | cross-week bridge |
| `include_in_short_lesson` | boolean | selected for the model lesson plan | required filter |
| `activity_goal` | text | learner-facing goal | pedagogical paragraph |
| `teacher_move` | text | what the teacher does | lesson plan detail |
| `learner_output` | text | what the learner produces | assessment link |
| `assessment_evidence` | text | what counts as evidence | evaluation note |
| `caution_note` | text | limitation or teaching warning | writing limitation |

Important: this is a synthetic lesson-design dataset, not evidence that an activity is effective.

## Provenance

- Source role: synthetic pedagogical adaptation dataset.
- Privacy: contains no real learner records.
- SHA-256: `03ecb6c201417f55a0c33b0a78ac9641461d3d591589de3f0f9dbd37e6ff1e97`
- Unit of analysis: one row, meaning one candidate teaching activity.
