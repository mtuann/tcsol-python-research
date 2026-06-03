# Week 05: Visualization for Papers

## Research Frame

- Research area: short-term Chinese teaching and TCSOL, with transfer to contrastive, MTPE, and education policy datasets.
- Small research question: Which short-term activity focus shows the clearest descriptive gain pattern, and how can we visualize it without overclaiming?
- Why this matters: a paper figure is not decoration. It is an argument about data that must show the pattern, the unit of analysis, sample size, and limitation clearly.

## Python Skill

- Main skill: create one paper-ready figure package with `seaborn` and `matplotlib`.
- Supporting skills: filter analysis-ready rows, choose bar vs dot plot, label axes, annotate `n`, use color intentionally, export `.png`, and inspect a companion dot plot.
- Functions/libraries: `pandas`, `seaborn`, `matplotlib.pyplot`, `barplot`, `stripplot`, `savefig`.

## Writing Support

- Paper section supported: Results / Figure caption.
- Writing output: one figure caption plus one 120-160 word interpretation paragraph.
- Tool support: create figures in the notebook, export figures to `outputs/figures`, then paste the PNG and caption into Word or Google Docs. LaTeX tools stay outside the Week 05 core workflow.
- Sentence frame: "Figure 1A shows [summary pattern] and Figure 1B shows [individual records] for [N] usable learner records. The pattern suggests [descriptive pattern], but the figure should not be read as causal because [limitation]."
- Common writing risk: using a clean-looking bar chart to hide small `n`, individual variation, or a non-causal design.

## Learning Objectives

By the end of this week, the learner can:

1. Explain the difference between an exploratory chart and a paper figure.
2. Choose a figure type that matches a research question.
3. Use a bar chart for a group summary and read a dot plot for individual observations.
4. Add axis labels, title, sample-size note, and caption.
5. Export a primary figure as `.png`.
6. Interpret a figure descriptively without claiming causality.

## Required Outputs

Core:

- [ ] Notebook runs from top to bottom.
- [ ] Visualization dataset is loaded from `data/raw/week05_cleaned_tcsol_scores.csv`.
- [ ] Figure summary table is exported to `outputs/tables/week05_figure_summary.csv`.
- [ ] Mean-gain bar figure is exported to `outputs/figures/week05_mean_gain_by_activity.png`.
- [ ] Figure 1A/1B caption reports variable, groups, usable N, source, and limitation.
- [ ] Interpretation paragraph avoids causal language and explains why the dot plot matters.

Stretch:

- [ ] Individual-gain dot figure is exported to `outputs/figures/week05_gain_distribution_by_activity.png`.
- [ ] `.svg` copies are exported for both figures.

## Files

- Slides: `slides.html`
- Interactive demo: `interactive_demo.html`
- Lecture notes: `lecture_notes.md`
- Notebook: `live_coding.html`, source `live_coding.ipynb`
- Exercises: `exercises.md`
- Assignment: `assignment.md`
- Data dictionary: `data_dictionary.md`
- Rubric: `rubric.md`
- Readings: `readings.md`

## Weekly Rhythm

| Stage | Time | Plan |
|---|---:|---|
| Pre-class | 25 min | Inspect two example figures and decide which one supports a paper claim better. |
| Lecture | 45 min | Explain figure choice, chart anatomy, small-N caution, and caption logic. |
| Live coding | 50 min | Create the primary bar figure and inspect the companion dot plot from the cleaned TCSOL dataset. |
| Guided practice | 35 min | Learner changes labels and caption language while preserving the claim. |
| Writing bridge | 25 min | Draft a figure caption and a descriptive interpretation paragraph. |
| Homework | 90 min | Submit notebook, figures, summary table, caption, and interpretation. |

## Core vs Stretch

Core:

- filter to `usable_pre_post == True`;
- compute mean gain and `n` by `activity_focus`;
- make one mean bar figure;
- inspect the companion dot plot produced by the notebook;
- export the primary `.png`;
- write one Figure 1A/1B caption and one interpretation paragraph.

Stretch:

- export `.svg` copies;
- edit the companion dot plot style;
- add confidence intervals only after explaining what they represent;
- make a second figure for `class_group`;
- compare a bar-only figure with a dot-plus-summary figure;
- write a transfer caption for MTPE or policy data.

Instructor-only:

- emphasize that visualization is a research decision, not a style exercise;
- show how hiding individual points can make small datasets look more certain than they are;
- preview Week 06: mean, SD, standard error, and confidence interval for a cautious Results paragraph.
