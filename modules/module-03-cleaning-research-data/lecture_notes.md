# Module 03 Lecture Notes

## Instructor Goal

Teach data cleaning as a research decision, not as a cosmetic coding step. The learner should leave with a repeatable pattern:

1. inspect;
2. decide;
3. clean;
4. log;
5. write.

## Learning Objectives

By the end of the module, learners can:

- identify missing values, duplicate observation keys, label variants, invalid ranges, and failed type conversions;
- explain why each issue can distort a research figure;
- clean a small dataset with pandas while preserving audit columns;
- export a cleaned dataset and cleaning log;
- draft a Methods note from the cleaning log.

## Timing

| Segment | Time | Activity |
|---|---:|---|
| Warm-up | 10 min | Show two figures: one from messy labels and one after normalization. Ask which one is trustworthy. |
| Concept | 20 min | Missing values, duplicates, labels, types, ranges. |
| Live coding | 45 min | Run `live_coding.ipynb` from raw CSV to outputs. |
| Interactive demo | 15 min | Explore `interactive_demo.html` and filter issue types. |
| Paper writing | 20 min | Turn cleaning log rows into Methods sentences. |
| Transfer | 20 min | Apply the same checks to education-policy or translation-studies data. |

## Teaching Script

Start with the question: "If I plot this table immediately, what might be false?"

Use the learner survey:

- `activity_group` has label variants: `Task-Based`, `task based`, `Task_based`.
- `L012` appears twice for the same date, so duplicate detection should use the observation key, not all columns.
- `post_vocab_score` includes `105` and `sixty-five`.
- `minutes_on_task` includes `-3`.
- one date cannot be parsed.

When students ask "Should we drop the row?", redirect to:

- What is the unit of observation?
- Is the value impossible, unknown, or merely unusual?
- Does the row still contain usable information for another variable?
- Can the paper explain this decision transparently?

## Common Misconceptions

| Misconception | Correction |
|---|---|
| "Cleaning means deleting bad rows." | Cleaning means making an accountable decision. Sometimes keep the row and set one invalid value to missing. |
| "Missing values should be filled so charts work." | Filling values creates evidence. Only impute when the method is justified. |
| "Duplicate rows are always exact duplicate rows." | Research duplicates often depend on an observation key, such as learner-date or country-year. |
| "`errors='coerce'` solves type problems." | It reveals type problems by turning failed conversions into missing values; you still need an audit. |

## Board Prompts

- What is one row in this dataset?
- Which columns define a duplicate record?
- Which values are impossible by measurement design?
- Which values are missing but still informative?
- What would a reader need to know before trusting the final figure?

## Exit Ticket

Ask each learner to write three sentences:

1. The observation key in my dataset is...
2. The most risky dirty-data issue is...
3. My Methods note will report...
