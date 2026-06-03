# Week 06 Assignment: Results Paragraph With Confidence Interval

## Task

Use the Week 06 notebook to create a statistical Results package from the synthetic TCSOL pre/post dataset.

## Core Minimum

1. Load `data/raw/week06_tcsol_prepost_scores.csv`.
2. Keep only rows where `usable_pre_post == True`.
3. Read the overall summary:
   - `raw_n`
   - `usable_n`
   - `mean_gain`
   - `sd_gain`
   - `ci95_low`
   - `ci95_high`
4. Write a 120-160 word Results paragraph that reports the overall estimate, uncertainty, and one limitation.

## Guided Core

1. Compute an activity-level table with:
   - `n`
   - `pre_mean`
   - `post_mean`
   - `mean_gain`
   - `sd_gain`
   - `se_gain`
   - `ci95_low`
   - `ci95_high`
2. Export the overall table to `outputs/tables/week06_overall_gain_summary.csv`.
3. Export the activity table to `outputs/tables/week06_activity_statistics.csv`.
4. Export the confidence-interval figure to `outputs/figures/week06_mean_gain_ci_by_activity.png`.
5. Write one figure caption.

## Required Writing

Your Results paragraph must include:

- usable `N`;
- mean gain and SD for the overall dataset;
- 95% CI for the overall mean gain;
- one group-level comparison that includes group `n` and CI if you mention it;
- one limitation sentence;
- no causal claim such as "proved", "caused", or "more effective".

Your figure caption must include:

- figure number;
- outcome variable;
- grouping variable;
- usable `N`;
- what the error bars mean;
- one limitation phrase.

## Sentence Frames

Vietnamese thinking frame:

> Trong `___` bản ghi dùng được, chênh lệch post-test minus pre-test trung bình là `___` điểm (`SD = ___`, `95% CI [___, ___]`). Nhóm `___` có mean gain mô tả cao hơn nhóm `___`, nhưng mỗi nhóm chỉ có `n = ___` đến `___` bản ghi và khoảng tin cậy vẫn cần được đọc thận trọng. Vì vậy, kết quả này nên được hiểu như một pattern mô tả, không phải bằng chứng nhân quả.

English paper frame:

> In the usable Week 06 records (`N = ___`), learners showed a mean post-test minus pre-test difference of `___` points (`SD = ___`, `95% CI [___, ___]`). By activity focus, `___` had the highest descriptive mean gain, while `___` had the lowest. These estimates should be interpreted cautiously because `___`.

## Stretch

Add one optional paired t-test output and write two sentences:

1. What does the t-test compare?
2. Why should the Results paragraph still report mean, CI, and limitation?

## Submission

Submit:

- completed notebook;
- `week06_overall_gain_summary.csv`;
- `week06_activity_statistics.csv`;
- `week06_mean_gain_ci_by_activity.png`;
- CI figure caption;
- Results paragraph;
- source note for the dataset and methods.

Source note template:

> Dataset: synthetic Week 06 TCSOL pre/post dataset, `data/raw/week06_tcsol_prepost_scores.csv`, SHA-256 `175469cd9120b36a467d0e0b439f78859525841555c6a30bc5de0777edb9137a`. Method references: pandas GroupBy/SEM documentation and SciPy t distribution documentation. The dataset is for workflow practice and should not be treated as real classroom evidence.
