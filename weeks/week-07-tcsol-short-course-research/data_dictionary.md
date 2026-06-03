# Week 07 Data Dictionary

| Column | Type | Meaning | Week 07 Use |
|---|---|---|---|
| `learner_id` | text | synthetic learner identifier | ID only; the unit is the whole row |
| `class_group` | text | class label | optional grouping |
| `activity_focus` | text | teaching activity category | grouping variable |
| `activity_label` | text | display label | figure/table label |
| `target_structure` | text | Chinese target structure | shared teaching focus: result complements in service dialogues |
| `attendance_hours` | numeric | synthetic attendance hours | context variable |
| `task_completion_pre/post` | numeric | 1-5 rubric score | task evidence |
| `accuracy_pre/post` | numeric | 1-5 rubric score | language accuracy |
| `fluency_pre/post` | numeric | 1-5 rubric score | task fluency |
| `interaction_strategy_pre/post` | numeric | 1-5 rubric score | interaction behavior |
| `confidence_pre/post` | numeric | 1-5 rubric score | observed confidence or learner self-rating |
| `main_difficulty` | text | teacher-coded difficulty | qualitative code |
| `teacher_feedback` | text | short observation note | qualitative evidence |
| `completed_task` | boolean | task completion flag | cleaning check |
| `usable_task` | boolean | row can be analyzed | required filter |

Important: this is a synthetic teaching dataset for learning workflow, not real student data.

## Provenance

- Source role: synthetic short-course TCSOL task dataset.
- Privacy: contains no real learner records.
- SHA-256: `d1cb69df35232bce0845394fe179c9ba4b1c3ecce15e7a2171f2397b6ca3fed6`
- Unit of analysis: one row, meaning one synthetic learner task record.
- Required filter: use rows where `completed_task == True` and `usable_task == True` before computing Week 07 summaries. In this dataset, `L010` and `L019` are excluded because they do not have usable post-task rubric scores.
