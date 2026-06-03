# Week 06: Intro Statistics for Results

This week turns the Week 05 cleaned pre/post dataset into cautious statistical writing. The learner computes `n`, `mean`, `SD`, `SE`, and `95% CI`, then writes a short Results paragraph that reports the estimate, uncertainty, and limitation.

## Research Frame

- Question: After a short-term Chinese learning activity, how large is the average gain, and how uncertain is the estimate?
- Unit of analysis: one usable learner record with numeric pre-test and post-test scores.
- Dataset: synthetic TCSOL pre/post data, reused from the cleaned Week 05 dataset.
- Core output: one activity-level statistics table, one CI figure with caption, one 120-160 word Results paragraph.
- Stretch output: paired t-test output and a short note explaining why p-values should not be the only evidence.

## Beginner Scope

Week 06 is intentionally not a full statistics course. The core lesson uses one repeated pattern:

```text
mean -> SD -> SE -> 95% CI -> cautious Results sentence
```

The learner should be able to explain:

- `mean` estimates the average gain in the sample;
- `SD` describes how spread out learner gains are;
- `SE` describes how stable the sample mean is as an estimate;
- `95% CI` gives an interval around the estimate under statistical assumptions;
- `p-value` is optional this week and should not replace estimate, interval, and limitation.

## Weekly Materials

- `index.html`: learner-facing bilingual overview.
- `slides.html`: visual lecture deck with quick slide overview.
- `interactive_demo.html`: CI explorer for changing sample size and variation.
- `lecture_notes.md`: instructor and learner notes.
- `live_coding.ipynb`: runnable notebook source.
- `live_coding.html`: rendered notebook for GitHub Pages.
- `assignment.md`: weekly submission instructions.
- `rubric.md`: assessment criteria.
- `readings.md`: required and optional readings.

## Core Checklist

- [ ] Load `week06_tcsol_prepost_scores.csv`.
- [ ] Filter rows where `usable_pre_post == True`.
- [ ] Compute `n`, `mean_gain`, `sd_gain`, `se_gain`, `ci95_low`, `ci95_high`.
- [ ] Export `outputs/tables/week06_activity_statistics.csv`.
- [ ] Export `outputs/figures/week06_mean_gain_ci_by_activity.png`.
- [ ] Write a CI figure caption that reports variable, groups, usable N, and limitation.
- [ ] Write a Results paragraph with estimate, interval, and limitation.

## Main Sentence Frame

> In the usable Week 06 records (`N = 25`), learners gained an average of `10.88` points from pre-test to post-test (`SD = 1.90`, `95% CI [10.10, 11.66]`). This descriptive result should be interpreted cautiously because the dataset is synthetic, activity groups were small, and activity focus was not randomly assigned.

Figure caption frame:

> Figure 1. Mean gain score by activity focus in the synthetic Week 06 TCSOL dataset (`N = 25` usable learner records). Error bars show 95% confidence intervals around group mean gains; the figure is descriptive and does not establish causal effects.

## Teaching Note

Keep the first pass descriptive. Do not ask the learner to decide whether the intervention "worked" from one p-value. The main research habit is to report the estimate and show uncertainty before making claims.
