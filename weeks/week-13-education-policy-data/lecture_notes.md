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
policy["issue_date_parsed"] = pd.to_datetime(policy["issue_date"], errors="coerce")
policy.sort_values("issue_date_parsed")
```

Tiny worked example:

| source type | issue_date | date_basis | how to read it |
|---|---|---|---|
| policy plan | 2025-01-19 | publication_date | the policy source was published/announced on this date |
| data portal | 2026-06-04 | access_date_placeholder | the page is dynamic, so this is when the learner checked it |

Common mistake: sorting date strings without parsing them, then treating every date as a publication date.

Debugging signs:

- `NaT` means Python could not parse at least one date.
- A timeline that places all dynamic portals on the access date is not wrong, but the caption must say so.
- A sentence like "policy implementation increased in 2026" is too strong if the row is only an access-date placeholder.

## Concept 4: Coding Scheme

A good beginner coding scheme has broad `policy_area`, narrower `theme_code`, `evidence_type`, and `coder_note`.

## Paper Paragraph Logic

1. State the sample size and unit.
2. List the metadata and coding fields.
3. Explain date basis, especially access-date placeholders.
4. Mention source/evidence types.
5. Add limitation: small synthetic dataset, paraphrased excerpts, source coverage not policy impact.
