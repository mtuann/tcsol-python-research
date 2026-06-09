# Week 08 Assignment: Learner Error Report

## Task

Use the Week 08 notebook to create a small learner-error Results package for short-course Chinese teaching.

## Core Minimum

1. Load `data/raw/week08_learner_error_coding.csv`.
2. Identify the unit of analysis.
3. Filter `usable_error == True` and `on_prompt == True`.
4. Count only rows where `has_error == True`.
5. Identify the top error category.
6. Write a 120-160 word Results paragraph.

## Guided Core

1. Export:
   - `week08_error_frequency.csv`
   - `week08_error_by_target_structure.csv`
   - `week08_teaching_priority_table.csv`
   - `week08_representative_examples.csv`
2. Export:
   - `week08_error_category_frequency.png`
   - `week08_error_by_target_heatmap.png`
3. Write two captions.
4. Write the Results paragraph.

## Minimum Path

Follow this order if programming still feels new:

1. Run the setup cell and check the SHA-256.
2. Run all notebook cells from top to bottom.
3. Open `outputs/tables/week08_error_frequency.csv`.
4. Open `outputs/tables/week08_error_by_target_structure.csv`.
5. Open `outputs/tables/week08_representative_examples.csv`.
6. Write captions.
7. Write the Results paragraph.

Caption frame for Figure 1:

> Figure 1. Frequency of coded learner-error categories in the synthetic Week 08 dataset (`N = 57` coded error rows). The figure is descriptive and excludes target-like, unusable, and off-prompt rows.

Caption frame for Figure 2:

> Figure 2. Coded error categories by target structure in the synthetic Week 08 dataset (`N = 57` coded error rows). Cell values show counts of on-prompt coded error rows; the heatmap supports teaching-priority discussion rather than learner diagnosis.

## Required Writing

Your Results paragraph must include:

- usable response N;
- coded-error row N;
- top error category with count;
- one crosstab pattern;
- one teaching implication;
- one limitation sentence;
- no broad claim about all Vietnamese learners.

## Sentence Frames

Vietnamese thinking frame:

> Trong `N = ___` on-prompt usable response rows, `___` dòng có coded learner error. Error category xuất hiện nhiều nhất là `___` (`n = ___`), tiếp theo là `___`. Bảng chéo cho thấy `___`. Teaching priority tiếp theo là `___`. Vì `___`, kết quả chỉ nên dùng để thiết kế follow-up activity, không để khái quát rộng.

English paper frame:

> In the on-prompt usable learner-response records (`N = ___`), `___` rows contained a coded learner error. The most frequent category was `___` (`n = ___`), followed by `___`. The crosstab suggests that `___`. The next teaching priority is `___`. Because `___`, the result should guide follow-up activity design rather than broad generalization.

## Stretch

Create a copied DataFrame, not a raw CSV edit:

```python
error_rows_stretch = error_rows.copy()
error_rows_stretch.loc[error_rows_stretch["response_id"] == "R004", "error_category"] = "word_order_target_frame"
```

Then write two sentences:

1. Why is the recoded category clearer?
2. What extra evidence would be needed before claiming Vietnamese transfer?

## Submission

Submit:

- completed notebook;
- 4 CSV tables;
- 2 figures;
- 2 figure captions;
- 120-160 word Results paragraph;
- one note about transfer as hypothesis, not proof.
- one source note linking an error category to a teaching target or reading.
