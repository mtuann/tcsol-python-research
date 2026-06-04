# Week 11 Lecture Notes: MT Evaluation

## Learning Goals

By the end of Week 11, the learner should be able to:

1. identify source, MT output, reference, and human review columns;
2. explain BLEU, chrF++, and TER in plain language;
3. compute one metric table by MT system;
4. read simplified human error labels alongside automatic metrics;
5. write a cautious MT evaluation Results paragraph.

## Concept Ladder

| Concept | Plain Meaning | Research Use |
|---|---|---|
| source segment | original Chinese sentence | input being translated |
| MT output | Vietnamese sentence from a system | object being evaluated |
| reference | human-written Vietnamese comparison sentence | automatic metric target |
| BLEU | word/n-gram overlap with reference | rough corpus-level comparison |
| chrF++ | character + word n-gram overlap | helpful for surface similarity |
| TER | edit rate to reference | lower is better |
| simplified error label | human review code | explains what metric cannot show |

## Main Workflow

```python
for system, rows in data.groupby("mt_system"):
    metrics = compute_bleu_chrf_ter(rows["vi_mt_output"], rows["vi_reference"])
```

## Important Caution

Automatic metrics are not bilingual judgment. They compare one output with one reference and can miss meaning, register, omission, or acceptable alternative translations. Use metrics as a reproducible summary, then pair them with human review.
