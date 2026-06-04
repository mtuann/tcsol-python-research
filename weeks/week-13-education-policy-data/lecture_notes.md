# Week 13 Lecture Notes

## Big Idea

A policy paper often starts with documents, reports, and statistics. Python helps by turning source metadata and coding decisions into a table that can be checked, counted, visualized, and cited.

## Concept 1: Metadata Before Interpretation

Before asking what a policy means, record what it is: title, issuing body, issue date, source type, URL, access date, and coder note.

This protects the paper from vague claims such as "China's policy says..." without showing which source, date, or document type is being used.

## Concept 2: Description Is Not Evaluation

A policy row can support a descriptive claim:

> The source set includes several rows coded as digitalization or teacher development.

It cannot support an evaluation claim by itself:

> The policy improved learning outcomes.

Evaluation needs implementation or outcome data, not just policy text.

## Concept 3: Timeline Thinking

Dates help readers see order. A policy plan, statistical bulletin, international metadata source, and comparative report should not be collapsed into one undated pile.

```python
policy["issue_date_parsed"] = pd.to_datetime(policy["issue_date"])
policy.sort_values("issue_date_parsed")
```

## Concept 4: Coding Scheme

A good beginner coding scheme has broad `policy_area`, narrower `theme_code`, `evidence_type`, and `coder_note`.

## Paper Paragraph Logic

1. State the sample size and unit.
2. Report the most common policy areas.
3. Mention source/evidence types.
4. Add limitation: small synthetic dataset, paraphrased excerpts, source coverage not policy impact.
