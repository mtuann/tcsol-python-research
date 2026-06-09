# Module 03 Figure Critique

## Critique Target

A common weak figure shows average vocabulary gain by activity group before label cleaning.

## What Goes Wrong

| Problem | What the reader sees | Why it is misleading |
|---|---|---|
| Label variants | `Task-Based`, `task based`, and `Task_based` appear as separate groups | One teaching condition is split into several bars |
| Duplicate key | one learner-date record appears twice | One learner receives extra weight in the mean |
| Invalid score | `105` is included as a post score | The post mean becomes too high |
| Missing score | missing pre/post values disappear without explanation | The sample size changes invisibly |
| Type failure | `sixty-five` cannot be averaged | The figure may silently exclude or fail on that row |

## Better Critique Questions

- What is the unit of observation behind each bar?
- Which rows were excluded from the gain calculation?
- Were labels normalized before grouping?
- Were impossible values set to missing or treated as real scores?
- Does the caption say what was cleaned?

## Redesign Requirement

A better figure should include:

- canonical labels;
- duplicate-key rule;
- complete-pair count;
- a caption that says missing or invalid scores were documented rather than filled;
- a cleaning log link or table.

## Sample Critique Paragraph

The original figure is not trustworthy because the group labels are not canonicalized: variants of `task-based` appear as separate groups. The figure also does not state whether duplicate learner-date records were removed or how invalid scores were handled. A revised figure should be generated only after label normalization, duplicate-key cleaning, numeric conversion audit, and valid-range checks; the caption should report the complete-pair sample used for gain scores.
