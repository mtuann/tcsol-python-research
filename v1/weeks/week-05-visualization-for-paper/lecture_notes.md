# Week 05 Lecture Notes: Visualization for Papers

## Core Idea

Week 05 turns a cleaned table into a figure that can support a Results paragraph. The learner does not need many chart types yet. They need a reliable habit:

1. decide what the figure should help the reader compare;
2. choose a chart type that matches that comparison;
3. show enough context so the reader is not misled;
4. export the figure in a paper-ready format;
5. write a caption and interpretation that match the data.

## Exploratory Chart vs Paper Figure

An exploratory chart is for the researcher. It can be quick, messy, and temporary.

A paper figure is for the reader. It needs:

- one clear question;
- visible variables and units;
- labels that can be read without guessing;
- sample size;
- caption and limitation.

Week 05 uses the Week 04 cleaned TCSOL dataset so the technical focus is visualization.

## Tool Mental Model

Keep the tool roles simple:

| Tool | Job in Week 05 | Learner edits? |
|---|---|---|
| `pandas` | prepare `usable` rows and summary table | yes, lightly |
| `seaborn` | draw the chart from columns | yes, one line at a time |
| `matplotlib` | add labels and save the figure | mostly run-only |

The learner should understand the workflow before they understand every styling line. The polished axis labels, `n` annotations, layout settings, and SVG export can be treated as run-only scaffolding in the first pass.

## Figure Question

The figure question is:

> Which short-term activity focus shows the clearest descriptive gain pattern?

This is descriptive. It does not prove that one activity caused better learning. The dataset is small and synthetic, so the correct language is "shows", "suggests", or "is consistent with", not "proves".

## Bar Chart vs Dot Plot

Use a bar chart when the main question is a group summary.

Use a dot plot when the reader must see individual observations or small sample size.

For Week 05, both are useful:

- bar chart: mean gain by `activity_focus`;
- dot plot: every learner's `gain_score` by `activity_focus`;
- combined interpretation: result complements and measure words look higher on average, but the sample is small.

## Chart Anatomy

A paper figure should include:

- a title or caption that states what is shown;
- X axis: group variable;
- Y axis: measured outcome;
- readable labels;
- sample size note;
- exported file name;
- source note.

Avoid:

- unlabeled axes;
- decorative colors with no meaning;
- cropped axes that exaggerate differences;
- a legend that repeats what the axis already says;
- claims that are stronger than the design.

## Minimal Code Pattern

```python
usable = df[df["usable_pre_post"]].copy()
summary = usable.groupby("activity_focus").agg(
    n=("learner_id", "count"),
    mean_gain=("gain_score", "mean")
)
```

Then plot:

```python
sns.barplot(data=usable, x="activity_focus", y="gain_score", errorbar=None)
sns.stripplot(data=usable, x="activity_focus", y="gain_score", jitter=0.12)
```

Export:

```python
fig.savefig("outputs/figures/week05_mean_gain_by_activity.png", dpi=300, bbox_inches="tight")
fig.savefig("outputs/figures/week05_mean_gain_by_activity.svg", bbox_inches="tight")
```

## Caption Frame

```text
Figure 1. Gain score by activity focus in the synthetic Week 05 TCSOL dataset (N = [N] usable learner records). Panel A shows group mean gain; Panel B shows individual learner records with group means. The figure is descriptive and does not establish causal effects.
```

Weak caption:

```text
Figure 1. Scores by activity.
```

Better caption:

```text
Figure 1. Gain score by activity focus in the synthetic Week 05 TCSOL dataset (N = 25 usable learner records). Panel A shows group mean gain; Panel B shows individual learner records and mean lines. The figure is descriptive because activity groups were not randomly assigned.
```

## Interpretation Frame

```text
The figure suggests that [group] has the highest mean gain ([value]), followed by [group]. However, each group contains only [n range] usable records, so the pattern should be treated as descriptive. The individual-point plot shows [variation statement], which is important because mean bars alone can hide the number and spread of learner records.
```

## Transfer to Other Research Tracks

| Track | Figure question | Suitable first figure |
|---|---|---|
| TCSOL | Which activity focus shows stronger descriptive gains? | mean bar + individual dot plot |
| Contrastive analysis | Which error category appears more often in Chinese-Vietnamese examples? | frequency bar chart |
| MTPE | Which MT engine has more post-editing changes? | dot plot or box plot by engine |
| Education policy | How many policy documents appear by year or region? | bar chart or line chart, depending on time order |

Mini transfer frames:

- Contrastive analysis: "Figure 1 shows the frequency of selected Chinese-Vietnamese contrastive features in the coded example set (N = [examples]). Bars count examples, not learner difficulty; each claim still needs representative examples."
- MTPE: "Figure 1 shows post-editing time by MT system for [N] segments. Dots show segment-level variation, so the figure should be read with qualitative error examples rather than as an automatic quality ranking."
- Education policy: "Figure 1 shows the number of policy documents by year in the collected corpus (N = [documents]). The figure describes publication patterns, not policy effectiveness."

Week 05 prepares the learner to ask whether a figure helps the reader see the data, not whether it looks impressive.
