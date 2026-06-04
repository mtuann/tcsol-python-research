# Week 11 Assignment: MT Evaluation Table

## Core Submission

Submit:

1. `week11_system_metric_summary.csv`
2. `week11_human_review_summary.csv`
3. `week11_chrf_by_system.png`
4. one figure caption;
5. one 2-3 sentence metric source note;
6. one 130-180 word Results paragraph.

## Core Steps

1. Open `live_coding.html` first to understand the workflow.
2. Run `live_coding.ipynb` in Colab or locally.
3. Load `data/raw/week11_mt_evaluation_segments.csv`.
4. Check that one source segment has three MT outputs and one reference.
5. Compute BLEU, chrF++, and TER by `mt_system`.
6. Export the metric table and human review table.
7. Create the chrF++ figure.
8. Write the Results paragraph with one limitation.

## Caption Frame

> Figure 1 compares chrF++ across three synthetic MT profiles for 12 Chinese-Vietnamese education-policy source segments (36 system-segment rows). Higher chrF++ means more surface overlap with the single Vietnamese reference, but it does not replace bilingual human review.

## Results Paragraph Frame

> In the synthetic Week 11 dataset, `___` had the highest `___` score, while `___` had the lowest TER. Human review showed that `___`. This suggests `___`. However, the dataset is small, synthetic, and uses one reference per source segment, so the result should be reported as a classroom evaluation example rather than a general claim about MT quality.

## Stretch

Use `week11_segment_review_sample.csv` to compare one segment where a metric score and human review label do not tell the same story. Explain the disagreement in 3-4 sentences.
