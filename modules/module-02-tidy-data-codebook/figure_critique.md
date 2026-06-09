# Module 02 Figure Critique

## Figure Under Review

Output: `outputs/figures/module02_tidy_prepost_example.png`

Claim it can support:

> After reshaping wide pre/post score columns into a tidy learner-skill-time table, plotting a pre/post pattern becomes straightforward.

## What Works

- The x-axis encodes measurement time.
- The y-axis encodes mean score.
- Color separates skill, not decoration.
- The caption can name the unit of observation after reshaping.
- The figure is exported as PNG, SVG, and PDF.

## What Must Be Explained

- The dataset is synthetic teaching data.
- Scores should be compared within skill unless scale comparability is documented.
- The figure is descriptive, not causal.
- The tidy table has a different unit of observation from the raw wide table.

## Common Bad Version

A weak version would:

- plot `pre_vocab_score` and `post_vocab_score` directly without explaining row meaning;
- average ordinal labels such as CEFR;
- omit the codebook;
- call the result "improvement caused by the activity" without design evidence;
- save only a screenshot.

## Revision Challenge

Create a second figure that separates `activity_group`.

Then write two sentences:

1. What becomes easier to compare?
2. What becomes visually more crowded?
