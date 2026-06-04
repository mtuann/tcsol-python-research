# Week 11 Assignment: MT Evaluation Table

## Core Submit

Submit a notebook or folder containing:

1. `week11_system_metric_summary.csv`
2. `week11_error_label_summary.csv`
3. `week11_chrf_by_system.png`
4. one figure caption;
5. one 2-3 sentence metric source note;
6. one 130-180 word MT evaluation Results paragraph.

## Core Steps

1. Start with `live_coding.html`, then run `live_coding.ipynb` from the repository root or in Colab.
2. Load `data/raw/week11_mt_evaluation_segments.csv`.
3. Check that one row means one source segment translated by one MT system.
4. Compute BLEU, chrF++, and TER by `mt_system`.
5. Summarize simplified error labels by `mt_system`.
6. Export the metric table and one figure.
7. Write a Results paragraph that separates metric evidence from human review.

## Caption Frame

> Figure 1 compares chrF++ across three synthetic MT systems for 12 Chinese-Vietnamese education-policy segments. Higher chrF++ means more surface overlap with the single Vietnamese reference, but it does not replace bilingual human review.

## Results Frame

> In the synthetic Week 11 dataset, `___` had the highest `___` score, while `___` had the lowest TER. Human review showed that `___` had the highest or tied highest count of `___` labels. This suggests `___`. However, the dataset is small and uses one reference per segment, so the result should be reported as a classroom evaluation example rather than a general claim about MT quality.

## Stretch

Export `week11_error_count_by_system.png` and write a second caption explaining why human error labels can disagree with automatic metrics.
