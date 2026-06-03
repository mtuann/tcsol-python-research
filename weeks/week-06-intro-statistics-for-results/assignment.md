# Week 06 Assignment: Results Paragraph With Confidence Interval

## Task

Use the Week 06 notebook to create a statistical Results package from the synthetic TCSOL pre/post dataset.

## Core Steps

1. Load `data/raw/week06_tcsol_prepost_scores.csv`.
2. Keep only rows where `usable_pre_post == True`.
3. Compute an activity-level table with:
   - `n`
   - `pre_mean`
   - `post_mean`
   - `mean_gain`
   - `sd_gain`
   - `se_gain`
   - `ci95_low`
   - `ci95_high`
4. Export the table to `outputs/tables/week06_activity_statistics.csv`.
5. Export the confidence-interval figure to `outputs/figures/week06_mean_gain_ci_by_activity.png`.
6. Write one figure caption and one 120-160 word Results paragraph.

## Required Writing

Your Results paragraph must include:

- usable `N`;
- mean gain and SD for the overall dataset;
- 95% CI for the overall mean gain;
- one group-level comparison;
- one limitation sentence;
- no causal claim such as "proved", "caused", or "more effective".

Your figure caption must include:

- figure number;
- outcome variable;
- grouping variable;
- usable `N`;
- what the error bars mean;
- one limitation phrase.

## Sentence Frame

> In the usable Week 06 records (`N = ___`), learners gained an average of `___` points from pre-test to post-test (`SD = ___`, `95% CI [___, ___]`). By activity focus, `___` had the highest descriptive mean gain, while `___` had the lowest. These estimates should be interpreted cautiously because `___`.

## Stretch

Add one optional paired t-test output and write two sentences:

1. What does the t-test compare?
2. Why should the Results paragraph still report mean, CI, and limitation?

## Submission

Submit:

- completed notebook;
- `week06_activity_statistics.csv`;
- `week06_mean_gain_ci_by_activity.png`;
- CI figure caption;
- Results paragraph;
- source note for the dataset and methods.
