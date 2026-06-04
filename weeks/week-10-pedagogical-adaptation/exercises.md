# Week 10 Exercises

## A. Copy And Modify

Change the ranking line from:

```python
priority = activities.sort_values("adaptation_score", ascending=False)
```

to rank by `minutes` instead. Answer:

> Ranking by `adaptation_score` chooses `___`, but ranking by `minutes` chooses `___`.

## B. Guided Problem

Use `groupby()` to calculate total minutes by lesson phase in the selected model plan:

```python
plan.groupby("lesson_phase")["minutes"].sum()
```

Answer: Which phase receives the most minutes? Does that automatically mean it is the most important phase?

Stretch check:

```python
activities.groupby("phenomenon")["minutes"].sum().sort_values(ascending=False)
```

Answer: Which phenomenon has the most candidate activity time, and why is this not the same as lesson priority?

## C. Research-Style Task

Choose one activity in the short lesson plan. Write 80-100 words explaining:

- what learners do;
- which contrastive phenomenon it supports;
- why it fits the lesson phase;
- one limitation.

## D. Caption Practice

> Figure 1 ranks candidate teaching activities by adaptation score. The score is a transparent planning heuristic, not evidence of classroom effectiveness.

> Figure 2 shows minutes by lesson phase in the selected short lesson plan. The figure helps justify lesson pacing, but the plan still needs classroom testing.

## E. Source Note Practice

> Source checked: `___` (accessed `___`). It supports `___`, but it does not prove that this synthetic activity sequence works with real learners.
