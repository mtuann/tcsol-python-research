# Week 09 Exercises

## A. Copy And Modify

Open `live_coding.ipynb`. Change the marker check from `"了"` to one of these:

- `"到"`
- `"完"`
- `"个"`
- `"在"`

Run the cell again. Write one sentence:

> The marker `___` appears in ___ usable contrastive examples.

## B. Guided Problem

Create a table with only high-risk examples:

```python
high_risk = analysis_rows[analysis_rows["teaching_risk"] == "high"]
high_risk[["example_id", "phenomenon", "chinese_example", "vietnamese_rendering"]]
```

Answer: which phenomenon has the most high-risk examples, which example is clearest for a beginner lesson, and what teaching note would you write?

## C. Research-Style Task

Choose one phenomenon and write 120-150 words with one definition, one example pair, one teaching implication, and one limitation.

## D. Figure Caption Practice

> Figure 1 shows the frequency of contrastive phenomena in the usable Week 09 synthetic example bank (`N = ___`). The figure is descriptive and should be used to select teaching examples, not to estimate population-level difficulty.
