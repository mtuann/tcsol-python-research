# Module 02 Assignment

## Submission Package

Submit a folder named `module02_yourname/` with:

- `tidy_dataset.csv`
- `codebook.csv`
- `schema_summary.csv`
- `figure.png`
- `figure.svg`
- `caption.md`
- `methods_data_note.md`
- your edited notebook, if required by the instructor

## Part A: Inspect a Wide Table

Choose one of the provided raw datasets or your own small dataset.

Write:

1. What does one row mean now?
2. Which columns are identifiers?
3. Which columns are repeated measures?
4. Which columns are outcomes?
5. Which columns are context variables?

## Part B: Build a Codebook

Create a codebook with at least eight variables.

Minimum columns:

- `variable_name`
- `variable_type`
- `role`
- `unit_of_observation`
- `allowed_values`
- `paper_note`

## Part C: Reshape to Tidy Long Format

Use `pd.melt()` or an equivalent pandas operation to create one tidy analysis table.

Your output table must make the row meaning explicit. Example:

```text
learner_id | skill | time | score
```

## Part D: Create a Figure

Create one figure from the tidy table.

Export:

- PNG for web/slides;
- SVG for editable/vector use.

Optional:

- PDF for Overleaf or journal submission.

## Part E: Caption and Methods Note

Caption: 80-120 words.

Methods data note: 120-180 words explaining:

- raw unit of observation;
- tidy unit of observation;
- key variables;
- variable types;
- one limitation.

## Vietnamese Reminder

Đừng chỉ nói "dữ liệu đã clean". Hãy nói rõ: một dòng là gì, mỗi cột là biến loại gì, và biến đó được dùng vào claim nào.

## English Reminder

Do not only say "the data is clean." State what one row means, what type each column has, and which claim the variable supports.
