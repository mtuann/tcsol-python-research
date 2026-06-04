# Week 12: MTPE Workflow With Time Logs And Edit Distance

Week 12 moves from evaluating raw MT outputs to analyzing post-editing effort. The learner compares synthetic Chinese-Vietnamese MT profiles using post-edited text, post-editing time, edit distance, and simplified revision labels.

## Research Frame

- Research area: Translation Studies, MTPE workflow, and Chinese-Vietnamese education-policy translation.
- Small research question: Which synthetic MT output profile requires less post-editing effort, and what revision types explain that effort?
- Why this matters: MTPE papers should not only say which system scores higher; they should explain what editors actually changed and how much effort the workflow required.
- Unit of analysis: one row, meaning one source segment translated by one synthetic MT profile and then post-edited.
- Dataset: 10 source segments, 3 synthetic MT profiles, 30 system-segment rows.
- Core learner output: MTPE effort summary table, revision-type table, one time figure, one caption, one source note, and one 130-180 word Results paragraph.
- Stretch output: normalized edit-distance figure and segment-level before/after discussion.

## Python Skill

- Main skill: create new columns from existing text columns using `rapidfuzz.distance.Levenshtein.distance`.
- Supporting skills: `groupby()`, summary tables, bar charts, source notes.
- Functions/libraries: `pandas`, `matplotlib`, `rapidfuzz`.

## Writing Support

- Paper section supported: Results / MTPE workflow analysis.
- Writing output: one paragraph reporting time, edit distance, revision labels, and limitation.
- Tool support: use the effort table and time figure as Results evidence; paste caption and source note into Word, Quarto, or Overleaf later.
- Sentence frame: "Profile `___` had the lowest observed mean post-editing time, while profile `___` had the highest. The revision labels suggest `___`. However, edit distance is only a surface proxy, and the time logs are synthetic classroom values."
- Common writing risk: treating edit distance as the same thing as human cognitive effort.

## Learning Objectives

By the end of this week, the learner can:

1. explain the difference between MT output, post-edited text, and reference translation;
2. compute character-level edit distance between MT output and post-edited text;
3. summarize post-editing time by MT profile;
4. connect revision labels to effort patterns;
5. write a cautious MTPE Results paragraph.

## Required Outputs

- [ ] Notebook runs from top to bottom.
- [ ] Raw MTPE dataset follows the schema in `data_dictionary.md`.
- [ ] `week12_mtpe_effort_summary.csv` is exported.
- [ ] `week12_revision_type_summary.csv` is exported.
- [ ] `week12_time_by_system.png` is exported.
- [ ] `week12_submission_text.md` is exported or copied from notebook output.
- [ ] Caption states systems, N, unit, and lower-is-less-effort direction.
- [ ] Results paragraph separates time, edit distance/revision labels, and limitation.
- [ ] Source note cites RapidFuzz and MTPE source with access date.

## Files

- Slides: `slides.html`
- Interactive demo: `interactive_demo.html`
- Lecture notes: `lecture_notes.md`
- Notebook: `live_coding.ipynb` and `live_coding.html`
- Exercises: `exercises.md`
- Assignment: `assignment.md`
- Data dictionary: `data_dictionary.md`
- Rubric: `rubric.md`
- Glossary: `glossary_week12.csv`

## Data Provenance

- File: `data/raw/week12_mtpe_segments.csv`
- Type: synthetic MTPE workflow dataset, not output from named commercial systems and not real translator productivity data.
- SHA-256: `f4a22aed428056220b9617dd4259dbe7efa27a6f9308b525a4bd0032b19e3363`
- Design basis: Chinese-Vietnamese education-policy examples with synthetic MT outputs, post-edited text, time logs, and simplified revision labels.
