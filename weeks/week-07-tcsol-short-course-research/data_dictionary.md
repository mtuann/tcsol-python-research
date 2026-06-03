# Week 07 Data Dictionary

| Column | Type | Meaning | Week 07 Use |
|---|---|---|---|
| `learner_id` | text | synthetic learner identifier | row identifier |
| `class_group` | text | class label | optional grouping |
| `activity_focus` | text | teaching activity category | grouping variable |
| `activity_label` | text | display label | figure/table label |
| `target_structure` | text | Chinese target structure | teaching focus |
| `attendance_hours` | numeric | synthetic attendance hours | context variable |
| `task_completion_pre/post` | numeric | 1-5 rubric score | task evidence |
| `accuracy_pre/post` | numeric | 1-5 rubric score | language accuracy |
| `fluency_pre/post` | numeric | 1-5 rubric score | task fluency |
| `interaction_strategy_pre/post` | numeric | 1-5 rubric score | interaction behavior |
| `confidence_pre/post` | numeric | 1-5 rubric score | learner confidence |
| `main_difficulty` | text | teacher-coded difficulty | qualitative code |
| `teacher_feedback` | text | short observation note | qualitative evidence |
| `completed_task` | boolean | task completion flag | cleaning check |
| `usable_task` | boolean | row can be analyzed | required filter |

Important: this is a synthetic teaching dataset for learning workflow, not real student data.

## Provenance

- Source role: synthetic short-course TCSOL task dataset.
- Privacy: contains no real learner records.
- SHA-256: `5071470f422fb53651c8ceae8d400d51414054cab62a048a7e70e225a913c62b`
- Required filter: use rows where `usable_task == True` before computing Week 07 summaries.
