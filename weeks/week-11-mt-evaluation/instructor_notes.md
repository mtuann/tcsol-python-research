# Week 11 Instructor Notes

## Teaching Rhythm

1. Start by showing one row: source, reference, one MT output.
2. Ask: what can a metric see, and what can it miss?
3. Explain BLEU/chrF/TER as black-box summaries, not NLP theory.
4. Run the metric loop by system.
5. Compare the metric table with simplified human review labels.
6. End with a Results paragraph that includes a limitation.

## Instructor Answer Key

- Raw rows: 36.
- Source segments: 12.
- MT systems: 3.
- Highest chrF++ profile: `MT_B`.
- Lowest TER profile: `MT_B`.
- Highest revision-needed count: `MT_A` and `MT_C` are tied at 12 rows.

Important teaching note: `MT_A`, `MT_B`, and `MT_C` are neutral synthetic profiles. Do not describe them as real commercial systems, and do not tell the learner that `MT_B` is the "good" system before she reads the metric and human-review tables.

Keep the answer key as instructor support; learner-facing pages may show a worked example but the learner should explain the result in their own words.
