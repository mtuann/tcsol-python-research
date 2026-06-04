# Week 13: Education Policy Data, Metadata, Timeline, And Coding Scheme

Week 13 moves from translation workflows to education policy data. The learner practices turning policy documents, statistical bulletins, and international metadata sources into a small coding table that can support a paper without overclaiming.

## Research Frame

- Research area: education policy, applied linguistics policy context, and TCSOL-related policy interpretation.
- Small research question: Which policy areas appear in a small source set, and what kind of evidence supports each area?
- Why this matters: policy papers need source metadata, dates, issuing bodies, coding decisions, and cautious language before interpretation.
- Unit of analysis: one row, meaning one coded policy-source excerpt or metadata entry.
- Dataset: 12 synthetic coding rows based on official/source metadata, not scraped full policy text.
- Core learner output: policy coding table, timeline table, policy-area summary table, one timeline or bar figure, one caption, one source note, and one 130-180 word Results paragraph.
- Stretch output: theme-by-source crosstab and a short coding-scheme revision note.

## Python Skill

- Main skill: convert date text with `pd.to_datetime()` and sort policy rows into a timeline.
- Supporting skills: `value_counts()`, `groupby()`, `pd.crosstab()`, bar/timeline figures.
- Functions/libraries: `pandas`, `matplotlib`.

## Writing Support

- Paper section supported: Methods / Data Sources / Results.
- Writing output: one paragraph that separates policy description from policy evaluation.
- Sentence frame: "In this small policy-source set, `___` appears most often, while `___` appears in fewer rows. The evidence types include `___`. This pattern describes the coding sample; it does not prove policy impact."
- Common writing risk: treating a policy document or statistical bulletin as proof that implementation succeeded.

## Learning Objectives

By the end of this week, the learner can:

1. identify policy metadata fields: title, issuing body, date, source type, URL, and access date;
2. convert date strings to timeline-ready dates;
3. count coded policy areas and evidence types;
4. create a simple policy timeline figure;
5. write a cautious policy-data Results paragraph.

## Required Outputs

- [ ] Notebook runs from top to bottom.
- [ ] Raw policy coding dataset follows the schema in `data_dictionary.md`.
- [ ] `week13_policy_area_summary.csv` is exported.
- [ ] `week13_timeline.csv` is exported.
- [ ] `week13_policy_timeline.png` or `week13_policy_area_counts.png` is exported.
- [ ] Caption states rows, source types, and synthetic/paraphrased-data limitation.
- [ ] Results paragraph separates description, evidence type, and limitation.
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

## Data Provenance

- File: `data/raw/week13_policy_coding.csv`
- Type: synthetic policy-source coding dataset based on official/source metadata and paraphrased excerpts.
- SHA-256: `f2e45d989c7f4f10365dd9c5103ffd7c9cc264c5e4b2a866df5431f1e6827e58`
- Design basis: official Chinese education policy/statistics pages plus international policy metadata/coding sources.
- Copyright note: excerpts are short paraphrases for teaching; learners should consult original sources for quotation and citation.
