# Bài nộp Week 03: Bảng mô tả với pandas

## Goal

- Python skill: use `pandas` to summarize a CSV with `groupby`.
- Research skill: create a descriptive table that answers a small teaching question.
- Paper section supported: Results.
- Writing output: table caption and 120-160 word interpretation.

## Data

- File: `data/raw/week03_tcsol_scores.csv`
- Unit of observation: one learner pre/post score record.
- Raw variables: `activity_focus`, `pre_score`, `post_score`, `completed`, `class_group`.
- Derived variable to create: `gain_score = post_score - pre_score`.

## Start Here

1. Open `live_coding.ipynb` in Colab or Jupyter.
2. Run all cells once without editing.
3. In the practice cell, change only `group_variable` if instructed.
4. Keep the raw CSV unchanged.
5. Write the caption and interpretation in a Markdown cell or in Word.

## Tasks

1. Load and inspect the dataset.
2. Select the columns needed for the research question.
3. Filter to completed records.
4. Create `gain_score`.
5. Produce one descriptive table grouped by `activity_focus`.
6. Export the table as `outputs/tables/week03_group_summary.csv`.
7. Write a caption for the table.
8. Write a 120-160 word interpretation.
9. Record one limitation and one short debugging note.
10. Add one transfer sentence for your track.

## Submission

Submit:

- completed `.ipynb` notebook;
- exported CSV table;
- caption, 2-4 sentences;
- interpretation paragraph, 120-160 words;
- source note with access date;
- one limitation;
- one debugging note, 1-2 sentences;
- one transfer sentence.

## Writing Frame

Use this frame:

```text
Table 1. The [activity_focus] group shows the largest descriptive average gain ([mean_gain] points), closely followed by [comparison group] ([comparison_gain] points). Data are from an instructor-created Week 03 teaching dataset, N = [n] completed learner records; scores are on a 0-100 scale, and gain is post_score minus pre_score. Because activity focus is linked to class section in this toy dataset, the result should be read as a descriptive pattern, not causal evidence.
```

## Interpretation Frame

Use 4-5 sentences:

```text
This table answers [research question] using [metric]. The main pattern is [pattern] with N = [n]. The top two groups are close/far apart because [comparison]. The main limitation is [limitation]. A next step is [data cleaning / data collection / visualization].
```

## Source and Debugging Note Templates

Source note:

```text
Dataset source: instructor-created synthetic Week 03 dataset, accessed 2026-06-03.
```

Debugging note:

```text
When I changed [cell/line], I checked [shape/N/output] to confirm the table still used completed records only.
```

## Checklist Before Submitting

- [ ] Notebook runs from top to bottom.
- [ ] The raw CSV is not manually edited.
- [ ] The summary table includes N.
- [ ] Averages are rounded consistently.
- [ ] Caption includes source, N, score scale, statistic, and limitation.
- [ ] Interpretation does not use "prove", "cause", or "effective" without caution.
- [ ] Transfer sentence says: in my track, `groupby` would group by ___ and summarize ___.
