# Week 11 Lecture Notes: MT Evaluation

## Plain-Language Concept

Machine translation evaluation compares an MT output with a reference translation and with human review notes. A metric is useful because it gives a consistent number. It is limited because many translations can be acceptable even when they do not match one reference exactly.

Week 11 uses three automatic metrics:

- BLEU: word and n-gram overlap; higher is usually better.
- chrF++: character plus word overlap; higher is usually better.
- TER: edits needed to match a reference; lower is usually better.

TER should not be described as actual MTPE effort. It is a reference-matching edit metric. Week 12 introduces post-edited text and time logs for MTPE effort.

## Research Use

In a Translation Studies paper, this workflow supports a small Results subsection:

1. report automatic metric comparison;
2. report human review labels;
3. show one figure;
4. explain why the conclusion is bounded.

## Annotated Code

```python
for system, rows in data.groupby("mt_system"):
    hypotheses = rows["vi_mt_output"].tolist()
    references = [rows["vi_reference"].tolist()]
    score = chrf.corpus_score(hypotheses, references).score
```

The important idea is `groupby("mt_system")`: each system profile is evaluated on the same set of source segments.

## Common Mistakes

1. Reading TER in the wrong direction. Lower TER is usually better.
2. Saying “BLEU proves quality.” Say “BLEU suggests stronger overlap with the reference.”
3. Treating `no_error` as an error. It is a review label, not a problem.
4. Forgetting the source note. Metric settings and dataset provenance must be recorded.

## Mini Cheat Sheet

```python
BLEU(effective_order=True)
CHRF(word_order=2)
TER()
data.groupby("mt_system")
metric_summary.to_csv(...)
plt.barh(...)
```

## Connection To Final Project

This week can support a small MT evaluation section in a translation workflow paper. It also prepares Week 12, where the learner asks whether a system that looks good by metric also requires less post-editing effort.
