# Week 11: Machine Translation Evaluation With BLEU, chrF, TER, And Human Error Labels

Week 11 introduces MT evaluation for Chinese-Vietnamese education-policy sentences. The learner treats automatic metrics as useful but limited evidence, then compares them with a small simplified human error table.

## Research Frame

- Research area: Translation Studies, MT evaluation, and MTPE preparation.
- Small research question: Which synthetic MT system is more reliable for short Chinese-Vietnamese education-policy sentences, and where do automatic metrics disagree with human review?
- Unit of analysis: one row, meaning one source segment translated by one MT system.
- Dataset: synthetic Chinese-to-Vietnamese MT outputs, references, simplified error labels, and 1-5 human adequacy/fluency scores.
- Core learner output: metric summary table, simplified error summary table, one figure, one caption, one source note, and one 130-180 word MT evaluation Results paragraph.
- Stretch output: compare BLEU/chrF/TER disagreement on one segment or prepare Week 12 MTPE notes.

## Python Skill

- Main skill: loop over grouped rows to compute one set of metrics per MT system.
- Supporting skills: `groupby()`, reading/exporting CSV, bar chart, cautious metric interpretation.
- Functions/libraries: `pandas`, `matplotlib`, `sacrebleu`.

## Writing Support

- Paper section supported: Results / Translation evaluation.
- Writing output: one paragraph reporting MT metric comparison and one human-review limitation.
- Tool support: use notebook output as the Results table; paste caption and paragraph into Word or Overleaf later.
- Sentence frame: "System `___` had the highest `___` score, while System(s) `___` had the highest/tied simplified human error-label count. This suggests `___`, but the conclusion is limited because automatic metrics compare outputs with one reference and do not replace bilingual human review."
- Common writing risk: reporting BLEU/chrF/TER as if they directly prove translation quality.

## Learning Objectives

By the end of this week, the learner can:

1. explain the difference between source, MT output, and reference translation;
2. compute BLEU, chrF++, and TER for each MT system using `sacrebleu`;
3. read higher-is-better metrics separately from lower-is-better TER;
4. summarize simplified human error labels by MT system;
5. write a cautious MT evaluation Results paragraph.

## Required Outputs

- [ ] Notebook runs from top to bottom.
- [ ] Raw MT evaluation dataset follows the schema in `data_dictionary.md`.
- [ ] `week11_system_metric_summary.csv` is exported.
- [ ] `week11_error_label_summary.csv` is exported.
- [ ] At least one figure is exported.
- [ ] Caption states systems, metric, N, direction of score, and limitation.
- [ ] Results paragraph separates automatic metrics, human review, and limitation.
- [ ] One short source note cites a metric or MQM/WMT source with link and access date.

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
- SHA-256: `b86c4ea84fcccba42c1a6dd8e6ac4112e42e59198ceb4b6c9e98dea0c810a939`
- Design basis: Chinese-Vietnamese education-policy examples with synthetic MT outputs and simplified MQM-inspired labels.
