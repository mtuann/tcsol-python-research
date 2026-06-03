# Week 06 Lecture Notes: Intro Statistics for Results

## Learning Goals

By the end of Week 06, the learner should be able to:

1. compute `n`, `mean`, `SD`, `SE`, and `95% CI` from a cleaned pre/post dataset;
2. explain the difference between learner variation (`SD`) and estimate uncertainty (`SE`, `CI`);
3. create a simple confidence-interval figure;
4. write a short Results paragraph with a limitation.

## Why This Week Matters

Week 05 helped the learner make a figure. Week 06 teaches what to write around the figure. A Results paragraph should not only say which group is highest. It should report the estimate, tell the reader how uncertain that estimate is, and avoid causal claims when the design is descriptive.

## Concept Ladder

| Concept | Plain Meaning | Results Use |
|---|---|---|
| `n` | number of usable records | tells readers how much data supports the estimate |
| `mean` | sample average | the main descriptive estimate |
| `SD` | spread among learners | shows how different learner gains are |
| `SE` | uncertainty of the mean estimate | used to build a confidence interval |
| `95% CI` | interval around the estimated mean | supports cautious reporting |

Mental model: **SD describes learners; SE/CI describe the estimate.**

## Main Workflow

```python
usable = df[df["usable_pre_post"] == True].copy()

activity_stats = (
    usable
    .groupby("activity_focus")
    .agg(
        n=("gain_score", "count"),
        mean_gain=("gain_score", "mean"),
        sd_gain=("gain_score", "std"),
        se_gain=("gain_score", "sem"),
    )
)
```

Then add the 95% confidence interval:

```python
t_critical = stats.t.ppf(0.975, n - 1)
margin = t_critical * se_gain
ci95_low = mean_gain - margin
ci95_high = mean_gain + margin
```

## Reading The Week 06 Table

Start with:

1. Which rows were usable?
2. What is the mean gain?
3. How wide is the confidence interval?
4. What limitation must be stated?

Do not start with "Is it significant?" The learner should first learn to describe the evidence.

## Results Writing Frame

> In the usable Week 06 records (`N = 25`), learners gained an average of `[mean]` points from pre-test to post-test (`SD = [SD]`, `95% CI [low, high]`). By activity focus, `[highest group]` had the highest descriptive mean gain, while `[lowest group]` had the lowest. These estimates should be read cautiously because `[limitation]`.

## Weak vs Better Results

Weak:

> Result complements worked best because its score is highest.

Better:

> Result complements had the highest descriptive mean gain in the synthetic dataset (`M = 13.00`, `95% CI [12.06, 13.94]`). Because group assignment was not randomized and each group contained only 5-8 usable records, this should be treated as an observed pattern rather than evidence that the activity caused larger gains.

## Transfer Examples

| Track | Statistic Use | Safe Writing |
|---|---|---|
| TCSOL | mean pre/post gain + CI | "Learners gained an average of..." |
| Contrastive linguistics | mean difficulty rating by feature | "This feature was rated as more difficult..." |
| MT/MTPE | mean edit time or error count by system | "System A required more post-editing time..." |
| Education policy | mean coding score by policy period | "Documents in this period showed a higher average..." |

## Common Risks

- Treating a small synthetic dataset like real classroom evidence.
- Saying "proved" or "caused" when the design is descriptive.
- Reporting p-values without mean, interval, and limitation.
- Forgetting that missing data changed `raw_n` into `usable_n`.

