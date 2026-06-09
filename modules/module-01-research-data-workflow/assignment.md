# Module 01 Assignment

## Submission Package

Submit a folder named `module01_yourname/` with:

- `research_data_inventory.csv`
- `source_readiness_figure.png`
- `source_readiness_figure.svg`
- `caption.md`
- `reflection.md`
- your edited notebook, if required by the instructor

## Part A: Copy and Modify

1. Open `live_coding.ipynb`.
2. Run the notebook once without changing anything.
3. Choose one row from `module01_transfer_question_bank.csv`.
4. Write your own paper question in one sentence.
5. Create a three-row data inventory for that question.

Minimum columns:

- `data_item`
- `source_or_owner`
- `unit_of_observation`
- `format`
- `personal_data_risk`
- `first_possible_figure`
- `readiness_note`

## Part B: Source Readiness

Choose three possible sources for your paper idea.

For each source, assign:

- `trust_score` from 1 to 5;
- `beginner_complexity` from 1 to 5;
- a one-sentence reason for each score.

Then compute:

```python
readiness_score = trust_score * 20 - beginner_complexity * 8
```

## Part C: Figure Export

Create one horizontal bar chart showing the readiness scores.

Export at least:

- PNG for web/slides;
- SVG for editable/vector use.

Optional:

- PDF for Overleaf or journal submission.

## Part D: Caption and Limitation

Write a caption of 80-120 words.

The caption must include:

- what the figure shows;
- what the unit of observation is;
- how the score was calculated;
- what the main pattern is;
- one limitation.

## Part E: Reflection

Write 120-180 words answering:

1. Which source would you start with, and why?
2. Which source looks useful but too complex right now?
3. What must be checked before this data can appear in a real paper?

## Vietnamese Reminder

Đừng cố chọn dataset "xịn nhất". Ở Module 01, mục tiêu là chọn dataset đủ nhỏ, đủ rõ, và đủ đáng tin để học được workflow nghiên cứu bằng Python.

## English Reminder

Do not try to choose the most impressive dataset. In Module 01, the goal is to choose a dataset that is small enough, clear enough, and trustworthy enough to learn the Python research workflow.
