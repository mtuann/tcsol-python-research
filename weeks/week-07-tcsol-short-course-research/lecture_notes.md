# Week 07 Lecture Notes: TCSOL Short-Course Research

## Learning Goals

By the end of Week 07, the learner should be able to:

1. define a short-course TCSOL research question;
2. connect target structure, learner task, and rubric;
3. identify classroom variables in a small dataset;
4. summarize rubric gains without overclaiming;
5. write a Methods draft with source alignment.

## Why This Week Matters

Short-term teaching research often fails because the activity is interesting but the evidence is vague. Week 07 teaches the learner to design observable evidence before analyzing it. A paper-ready Methods section needs a clear unit of analysis, task, rubric, and limitation.

## Concept Ladder

| Concept | Plain Meaning | Methods Use |
|---|---|---|
| `target_structure` | language feature being taught | defines the teaching focus |
| learner task | what the learner does | creates observable evidence |
| rubric | consistent scoring guide | makes evidence comparable |
| `activity_focus` | teaching activity type | grouping variable |
| `main_difficulty` | coded learner problem | qualitative teaching insight |

## Main Workflow

```python
usable = df[df["usable_task"] == True].copy()

for stem, label in criteria:
    usable[f"{stem}_gain"] = usable[f"{stem}_post"] - usable[f"{stem}_pre"]

usable["total_gain"] = usable["total_post"] - usable["total_pre"]
```

## Rubric Design Rule

A beginner-friendly rubric should be:

- observable: teacher can see the behavior in a task;
- bounded: 1-5 means the same thing across learners;
- task-specific: it matches the target structure and activity;
- not moralizing: avoid vague labels like "weak student" or "good student".

## Reading The Week 07 Tables

Start with:

1. What is the unit of analysis?
2. Which rows are usable?
3. What does each rubric criterion measure?
4. Which activity has a higher descriptive gain?
5. Which difficulty appears most often?

Do not write "feedback cycle is best" from this small synthetic dataset. Write "feedback cycle showed the highest descriptive rubric gain in the usable synthetic records."

## Source Alignment

Use external frameworks as design support, not as decoration:

- ACTFL Proficiency Guidelines 2024: functional language ability across domains.
- NCSSFL-ACTFL Can-Do Statements 2026: learning targets and rubric-oriented performance evidence.
- CEFR Companion Volume 2020: action-oriented tasks and descriptors.
- Chinese Proficiency Grading Standards: Chinese-specific proficiency stages, levels, and linguistic dimensions.

## Methods Writing Frame

Vietnamese thinking frame:

> Đơn vị phân tích là một learner task record. Activity focus được mã hóa thành `[groups]`. Target structure là `[structure]`. Learner evidence được chấm bằng rubric 1-5 gồm `[criteria]`. Các bản ghi incomplete bị loại. Vì sample nhỏ và không random assignment, phân tích chỉ mô tả task evidence trong dữ liệu mẫu.

English paper frame:

> The unit of analysis is one learner task record. Activity focus is coded as `[groups]`. The target structure is `[structure]`. Learner task evidence is scored with a 1-5 rubric covering `[criteria]`. Incomplete records are excluded. Because the sample is small and not randomly assigned, the analysis descriptively summarizes task evidence in the synthetic dataset.

## Common Risks

- Starting with a chart before defining the task.
- Using a rubric criterion that cannot be observed.
- Treating activity groups as causal conditions.
- Forgetting to say why records were excluded.
- Citing proficiency frameworks without adapting them to the actual short-course task.
