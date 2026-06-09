# Week 11: Machine Translation Evaluation With BLEU, chrF++, TER, And Human Review Labels

Week 11 introduces MT evaluation for Chinese-Vietnamese education-policy sentences. The learner treats automatic metrics as useful but limited evidence, then compares them with a small simplified human review table.

## Research Frame

- Research area: Translation Studies, MT evaluation, and MTPE preparation.
- Small research question: Which synthetic MT output profile shows stronger evidence for Chinese-Vietnamese education-policy sentences, and where do automatic metrics need human review?
- Unit of analysis: one row, meaning one source segment translated by one synthetic MT profile.
- Dataset: 12 source segments, 3 synthetic MT profiles, 36 system-segment rows.
- Core learner output: metric summary table, human review summary table, one chrF++ figure, one caption, one source note, and one 130-180 word Results paragraph.
- Stretch output: segment-level chrF++/TER comparison for selected rows and a second human-review figure.

## Python Skill

- Main skill: loop over grouped rows to compute one metric set per `mt_system`.
- Supporting skills: `groupby()`, reading/exporting CSV, bar chart, cautious metric interpretation.
- Functions/libraries: `pandas`, `matplotlib`, `sacrebleu`.

## Writing Support

- Paper section supported: Results / Translation evaluation.
- Writing output: one paragraph reporting automatic metric comparison, human review summary, and limitation.
- Tool support: use notebook output as the Results table; paste caption, source note, and paragraph into Word or Overleaf later.
- Sentence frame: "System `___` had the highest `___` score, while human review showed `___`. This suggests `___`, but the conclusion is limited because automatic metrics compare outputs with one reference and do not replace bilingual human review."
- Common writing risk: reporting BLEU/chrF++/TER as if they directly prove translation quality.

## Learning Objectives

By the end of this week, the learner can:

1. explain the difference between source, MT output, and reference translation;
2. compute BLEU, chrF++, and TER for each MT profile using `sacrebleu`;
3. read higher-is-better metrics separately from lower-is-better TER;
4. summarize human review labels by MT profile without treating `no_error` as an error;
5. write a cautious MT evaluation Results paragraph.

## Required Outputs

- [ ] Notebook runs from top to bottom.
- [ ] Raw MT evaluation dataset follows the schema in `data_dictionary.md`.
- [ ] `week11_system_metric_summary.csv` is exported.
- [ ] `week11_human_review_summary.csv` is exported.
- [ ] `week11_severity_summary.csv` is exported.
- [ ] `week11_metric_settings.csv` is exported.
- [ ] At least one figure is exported.
- [ ] Caption states systems, metric, N, direction of score, and limitation.
- [ ] Results paragraph separates automatic metrics, human review, and limitation.
- [ ] One short source note cites metric/MQM sources with link and access date.

## Files

- Slides: `slides.html`
- Interactive demo: `interactive_demo.html`
- Lecture notes: `lecture_notes.md`
- Notebook: `live_coding.ipynb` and `live_coding.html`
- Exercises: `exercises.md`
- Assignment: `assignment.md`
- Data dictionary: `data_dictionary.md`
- Rubric: `rubric.md`
- Glossary: `glossary_week11.csv`

## Data Provenance

- File: `data/raw/week11_mt_evaluation_segments.csv`
- Type: synthetic MT evaluation dataset, not output from named commercial systems.
- SHA-256: `2b87763883f56fe746262cb7be8b1b363922cde8b2ec31b1121139e97388268c`
- Design basis: Chinese-Vietnamese education-policy examples with synthetic MT outputs and simplified MQM-inspired review labels.
