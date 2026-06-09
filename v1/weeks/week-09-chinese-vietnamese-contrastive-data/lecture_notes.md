# Week 09 Lecture Notes: Chinese-Vietnamese Contrastive Data

## Learning Goals

By the end of Week 09, the learner should be able to:

1. define a contrastive example as the unit of analysis;
2. distinguish translation equivalence from contrastive evidence;
3. use `str.contains()` for a small visible pattern check;
4. compute a phenomenon frequency table;
5. build and read a phenomenon-by-risk crosstab;
6. select representative examples for an analysis paragraph;
7. write a cautious Chinese-Vietnamese contrastive note.

## Why This Week Matters

Contrastive analysis is useful for TCSOL when it helps the teacher choose explanations, examples, and follow-up tasks. It is also useful for translation and policy-text reading because it prevents the writer from treating similar-looking forms as perfect equivalents.

## Concept Ladder

| Concept | Plain Meaning | Research Use |
|---|---|---|
| contrastive example | one Chinese form plus one Vietnamese rendering | unit of analysis |
| `phenomenon` | human code for the contrastive point | countable category |
| `similarity_level` | similar, partial, different | interpretation caution |
| `teaching_risk` | low, medium, high | priority for explanation |
| representative example | one clear pair to discuss | evidence in analysis writing |

## Main Workflow

```python
df = pd.read_csv(DATA_PATH)
analysis_rows = df[df["include_in_table"] == True].copy()
analysis_rows["has_le"] = analysis_rows["chinese_example"].str.contains("了", regex=False)
frequency = analysis_rows["phenomenon"].value_counts()
risk_table = pd.crosstab(analysis_rows["phenomenon"], analysis_rows["teaching_risk"])
```

## Codebook Rule

A beginner-friendly contrastive code should be:

- visible in the Chinese example or Vietnamese rendering;
- specific enough to support a teaching note;
- broad enough to count across several examples;
- separated from claims about learner ability;
- paired with a representative example and limitation.

## Reading The Week 09 Tables

Start with:

1. How many rows are included in the main contrastive table?
2. Which phenomenon appears most often?
3. Which phenomenon has the highest teaching-priority score?
4. Which examples are high-risk because Chinese and Vietnamese do not map one-to-one?
5. Which single example would make the clearest paper paragraph?

Do not write "Vietnamese learners cannot learn result complements." Write "In this synthetic teaching example bank, `result_complement` had the highest priority score and should receive explicit contrastive explanation."

## Common Risks

- Treating every Vietnamese rendering as a direct translation equivalent.
- Treating `str.contains()` as linguistic analysis by itself.
- Mixing too many phenomena in one row.
- Claiming L1 transfer without learner evidence.
- Choosing examples that are too advanced for beginner TCSOL.
- Forgetting to state that the dataset is synthetic.
