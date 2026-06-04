# Week 10: Pedagogical Adaptation From Contrastive Evidence

Week 10 turns Week 09 contrastive findings into a short, teachable classroom adaptation. The learner uses `groupby()` and `sort_values()` to rank candidate activities, group minutes by lesson phase, read a model short lesson plan, and write a cautious pedagogical adaptation paragraph.

## Research Frame

- Research area: Applied Linguistics and TCSOL.
- Small research question: Which Week 09 contrastive phenomena should become priority teaching activities in a short Chinese lesson for Vietnamese learners?
- Unit of analysis: one row, meaning one candidate teaching activity, not one learner and not one class session.
- Dataset: synthetic activity-design dataset connected to Week 09 phenomena and priority scores.
- Core learner output: read the priority table, inspect a phase-minutes table, write one caption, one short source note, and a 130-180 word pedagogical adaptation paragraph.
- Guided notebook output: activity priority table, phase-minutes table, short lesson plan table, adaptation summary table, and one paper-ready figure.
- Stretch output: export the second figure or revise one activity for a different learner level or time limit.

## Python Skill

- Main skill: `groupby()` and `sort_values()`.
- Supporting skills: filtering, simple score calculation, reading/exporting CSV, bar charts.
- Functions/libraries: `pandas`, `matplotlib`.

## Writing Support

- Paper section supported: Discussion / Pedagogical implications.
- Writing output: one paragraph explaining how evidence becomes a short lesson adaptation.
- Tool support: write in notebook Markdown first, then paste into Word/Zotero draft.
- Sentence frame: "Based on the activity-priority table, I would adapt the short lesson by focusing on `___` because `___`. The lesson sequence begins with `___`, then moves to `___`, and ends with `___`. This recommendation is limited because the dataset is synthetic and should be tested with real learner responses."
- Common writing risk: claiming that a ranked activity is automatically effective without classroom evidence.

## Learning Objectives

By the end of this week, the learner can:

1. explain why a high-priority contrastive phenomenon still needs a teachable activity sequence;
2. calculate and interpret `adaptation_score` as a planning heuristic, not proof of effectiveness;
3. use `groupby()` to summarize minutes by lesson phase;
4. use `sort_values()` to rank candidate activities;
5. read a short lesson plan table as a pedagogical argument;
6. write a bounded pedagogical implication paragraph.

## Required Outputs

- [ ] Notebook runs from top to bottom.
- [ ] Activity dataset follows the schema in `data_dictionary.md`.
- [ ] Activity priority table is exported.
- [ ] Phase-minutes table is exported.
- [ ] Short lesson plan table is exported.
- [ ] Adaptation summary table is exported.
- [ ] At least one figure is exported.
- [ ] One core caption explains variables, unit, 45-minute time frame, and limitation.
- [ ] Pedagogical adaptation paragraph avoids causal overclaim.
- [ ] One short source note cites a teaching-design or grammar source with link and access date.

## Files

- Slides: `slides.html`
- Interactive demo: `interactive_demo.html`
- Lecture notes: `lecture_notes.md`
- Notebook: `live_coding.ipynb` and `live_coding.html`
- Exercises: `exercises.md`
- Assignment: `assignment.md`
- Data dictionary: `data_dictionary.md`
- Rubric: `rubric.md`
- Glossary: `glossary_week10.csv`

## Data Provenance

- File: `data/raw/week10_pedagogical_adaptation_activities.csv`
- Type: synthetic activity-design dataset, not real classroom observation data.
- SHA-256: `03ecb6c201417f55a0c33b0a78ac9641461d3d591589de3f0f9dbd37e6ff1e97`
- Design basis: Week 09 teaching-priority scores plus beginner-friendly lesson-planning principles.
