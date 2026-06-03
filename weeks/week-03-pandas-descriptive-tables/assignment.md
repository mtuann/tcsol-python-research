# Assignment: Descriptive Table With pandas

## Goal

- Python skill: use `pandas` to summarize a CSV with `groupby`.
- Research skill: create a descriptive table that answers a small teaching question.
- Paper section supported: Results.
- Writing output: table caption and 120-160 word interpretation.

## Data

- File: `data/raw/week03_tcsol_scores.csv`
- Unit of observation: one learner pre/post score record.
- Key variables: `activity_focus`, `pre_score`, `post_score`, `gain_score`, `completed`.

## Tasks

1. Load and inspect the dataset.
2. Select the columns needed for the research question.
3. Filter to completed records.
4. Create `gain_score`.
5. Produce one descriptive table grouped by `activity_focus`.
6. Export the table as `outputs/tables/week03_group_summary.csv`.
7. Write a caption for the table.
8. Write a 120-160 word interpretation.
9. Record one limitation and one debugging note.

## Submission

Submit:

- completed `.ipynb` notebook;
- exported CSV table;
- caption;
- interpretation paragraph;
- source note with access date;
- one limitation.

## Writing Frame

Use this frame:

```text
Table 1 shows that [activity_focus] had the highest average gain ([mean_gain] points), while [comparison group] had [comparison result]. The table includes N = [n] completed learner records from a short teaching dataset. Because the data are descriptive and groups are not randomly assigned, the result should be read as [careful interpretation], not causal evidence.
```

## Checklist Before Submitting

- [ ] Notebook runs from top to bottom.
- [ ] The raw CSV is not manually edited.
- [ ] The summary table includes N.
- [ ] Averages are rounded consistently.
- [ ] Caption includes source, N, score scale, statistic, and limitation.
- [ ] Interpretation does not use "prove", "cause", or "effective" without caution.
