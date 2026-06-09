# Week 10 Lecture Notes: Pedagogical Adaptation

## Learning Goals

By the end of Week 10, the learner should be able to:

1. distinguish a contrastive finding from a teaching activity;
2. read one activity row as a design decision;
3. calculate a simple adaptation score;
4. group lesson minutes by phase;
5. rank activity candidates;
6. write a pedagogical implication with a limitation.

## Why This Week Matters

A contrastive analysis is useful only when it becomes a teachable sequence: notice, compare, practice, communicate, and check. Week 10 is the bridge from analysis to classroom design.

## Concept Ladder

| Concept | Plain Meaning | Research Use |
|---|---|---|
| candidate activity | one possible teaching move | unit of analysis |
| lesson phase | review, notice, compare, practice, feedback, assessment | organize lesson flow |
| adaptation score | simple ranking heuristic | choose what to inspect first |
| phase minutes | time spent in each lesson phase | justify lesson design |
| pedagogical implication | what a teacher should do and why | Discussion section writing |

## Main Workflow

```python
activities = pd.read_csv(DATA_PATH)
activities["adaptation_score"] = activities["week09_priority_score"] + activities["learner_difficulty"] * 2 + activities["communicative_value"] - activities["preparation_load"]
priority = activities.sort_values("adaptation_score", ascending=False)
plan = activities[activities["include_in_short_lesson"]].copy()
phase_minutes = plan.groupby("lesson_phase")["minutes"].sum()
```

Tiny worked example:

```text
A001 = 28 + 3*2 + 2 - 1 = 35
```

In this synthetic score, `learner_difficulty` means instructional need: the teacher may need to design support. It does not mean that difficult items are automatically better to teach.

## Important Caution

A high adaptation score is not proof that an activity works. It is a transparent way to choose what to inspect first when planning a short lesson. Real effectiveness needs classroom evidence, learner work, or pre/post data.
