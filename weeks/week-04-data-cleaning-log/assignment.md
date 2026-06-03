# Assignment: Cleaned Dataset and Cleaning Note

## Goal

- Python skill: use pandas to clean a small messy dataset.
- Research skill: make data preparation decisions visible.
- Paper section supported: Methods / Data preparation.
- Writing output: cleaning decision note plus a before/after cleaning table.

## Data

- File: `data/raw/week04_messy_tcsol_scores.csv`
- Unit of observation: one learner pre/post score record.
- Key variables: `class_group`, `activity_focus`, `pre_score`, `post_score`, `attendance_hours`, `completed`, `self_confidence`.

## Tasks

1. Load and inspect the raw dataset.
2. Create a cleaning log table.
3. Normalize class labels.
4. Normalize activity focus labels.
5. Normalize completed status.
6. Convert numeric columns safely.
7. Create `gain_score`.
8. Export cleaned CSV.
9. Export cleaning log CSV.
10. Export one before/after cleaning summary.
11. Write a 100-150 word cleaning decision note.

## Submission

Submit:

- completed `.ipynb` notebook;
- cleaned dataset CSV;
- cleaning log CSV;
- before/after cleaning summary table;
- cleaning decision note;
- one limitation;
- source note with access date.

## Writing Frame

Use this frame:

```text
Before analysis, the raw dataset was preserved and a cleaned copy was created in pandas. Labels in [columns] were standardized using a predefined mapping. Numeric columns were converted with [method], and invalid entries were treated as missing rather than replaced with zero. After cleaning, [N] records had complete pre/post scores for the descriptive summary. The main limitation is [limitation].
```

## Checklist Before Submitting

- [ ] Raw CSV is not manually edited.
- [ ] Cleaned CSV is exported to `data/processed`.
- [ ] Cleaning log has step, column, problem, and decision.
- [ ] Missing values are not silently replaced with zero.
- [ ] Label mappings are visible in the notebook.
- [ ] Cleaning decision note avoids saying the data are perfect.
