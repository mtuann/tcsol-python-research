# Week 13: Education Policy Data, Metadata, Timeline, And Coding Scheme

Week 13 moves from translation workflows to education policy data. The learner practices turning policy documents, statistical bulletins, and international metadata sources into a small coding table that can support a paper without overclaiming.

## Research Frame

- Research area: education policy, applied linguistics policy context, and TCSOL-related policy interpretation.
- Small research question: Which policy areas appear in a small source set, and what kind of evidence supports each area?
- Why this matters: policy papers need source metadata, dates, issuing bodies, coding decisions, and cautious language before interpretation.
- Unit of analysis: one row, meaning one coded policy-source excerpt or metadata entry.
- Dataset: 12 synthetic coding rows based on official/source metadata, not scraped full policy text.
- Core learner output: timeline table, policy-area summary table, source-type summary table, one timeline or bar figure, one caption, one source note, and one 130-180 word Data/Methods paragraph.
- Stretch output: theme-by-source crosstab and a short coding-scheme revision note.

## Python Skill

- Main skill: convert date text with `pd.to_datetime()` and sort policy rows into a timeline.
- Supporting skills: `value_counts()`, `groupby()`, `pd.crosstab()`, bar/timeline figures.
- Functions/libraries: `pandas`, `matplotlib`.

## Writing Support

- Paper section supported: Methods / Data Sources, with a bridge to Results.
- Writing output: one paragraph that explains unit of analysis, metadata fields, coding scheme, date basis, and limitation.
- Tool support: draft the paragraph in the notebook/exported `week13_submission_text.md`, then paste it into Word + Zotero; Quarto/Overleaf becomes optional practice in Week 14.
- Sentence frame: "The dataset contains `___` coded source rows from `___` source documents. Each row records `___`, and the coding scheme uses `___`. Some dates are `___`, so the timeline describes source coverage rather than policy impact."
- Common writing risk: treating a policy document or statistical bulletin as proof that implementation succeeded.

## Learning Objectives

By the end of this week, the learner can:

1. identify policy metadata fields: title, issuing body, date, source type, URL, and access date;
2. convert date strings to timeline-ready dates;
3. count coded policy areas and evidence types;
4. create a simple policy timeline figure;
5. write a cautious policy-data Methods paragraph.

## Required Outputs

- [ ] Notebook runs from top to bottom.
- [ ] Raw policy coding dataset follows the schema in `data_dictionary.md`.
- [ ] `week13_policy_area_summary.csv` is exported.
- [ ] `week13_source_type_summary.csv` is exported.
- [ ] `week13_timeline.csv` is exported.
- [ ] `week13_policy_timeline.png` or `week13_policy_area_counts.png` is exported.
- [ ] Caption states rows, source types, and synthetic/paraphrased-data limitation.
- [ ] Data/Methods paragraph separates unit, metadata/coding scheme, date basis, and limitation.
- [ ] Source note cites at least one official policy/statistics source and one metadata/coding model source with access date.

## Files

- Slides: `slides.html`
- Interactive demo: `interactive_demo.html`
- Lecture notes: `lecture_notes.md`
- Notebook: `live_coding.ipynb` and `live_coding.html`
- Exercises: `exercises.md`
- Assignment: `assignment.md`
- Data dictionary: `data_dictionary.md`
- Rubric: `rubric.md`
- Glossary: `glossary_week13.csv`
- Policy QA: `policy_qa.md`
- Translation QA: `translation_qa.md`

## Data Provenance

- File: `data/raw/week13_policy_coding.csv`
- Type: synthetic policy-source coding dataset based on official/source metadata and paraphrased excerpts.
- SHA-256: `cedbc768526aadf2ebfe41fdf08585ebe10963e5ba17adb1a78f93ca14d8aaa5`
- Design basis: official Chinese education policy/statistics pages plus international policy metadata/coding sources.
- Copyright note: excerpts are short paraphrases for teaching; learners should consult original sources for quotation and citation.
