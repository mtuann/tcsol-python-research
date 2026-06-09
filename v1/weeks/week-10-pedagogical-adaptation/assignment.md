# Week 10 Assignment: Short Lesson Adaptation

## Core Submit

Submit a notebook or folder containing:

1. `week10_activity_priority_table.csv`
2. `week10_phase_minutes.csv`
3. `week10_short_lesson_plan.csv`
4. `week10_adaptation_summary.csv`
5. `week10_activity_priority.png`
6. one figure caption;
7. one 2-3 sentence source note;
8. one 130-180 word pedagogical adaptation paragraph.

## Core Steps

1. Start with `live_coding.html` to read the completed workflow, then open `weeks/week-10-pedagogical-adaptation/live_coding.ipynb` from the repository root or use the Colab link when you are ready to run code.
2. Run the setup cell.
3. Load `data/raw/week10_pedagogical_adaptation_activities.csv`.
4. Calculate `adaptation_score`. Treat `learner_difficulty` as instructional need in this synthetic planning score, not as proof that harder items are always better to teach.
5. Use `sort_values()` to rank activities.
6. Use `groupby()` to summarize lesson minutes by phase.
7. Read the short lesson plan table and write the adaptation paragraph.

## Caption Frame

> Figure 1 ranks candidate teaching activities by `adaptation_score` for 25 synthetic activity rows. The unit is one candidate activity. The score is a planning heuristic for teacher review, not evidence that the activity is effective.

## Source Note Frame

> Source checked: `___` (accessed `___`). It supports `___`, but it does not prove this synthetic activity sequence works with real learners.

## Required Writing Move

> Based on the activity-priority table, I would adapt the short lesson by focusing on `___`. The first activity is `___`, which helps learners `___`. The lesson then moves to `___` and ends with `___`. This adaptation is reasonable for a short TCSOL lesson because `___`. However, it remains a design recommendation because the dataset is synthetic and should be tested with learner responses.

## Stretch

- Export `week10_lesson_phase_minutes.png` and write a second caption.
- Revise one activity for a 20-minute micro-lesson or for learners at a different proficiency level. Explain what you changed and why.
