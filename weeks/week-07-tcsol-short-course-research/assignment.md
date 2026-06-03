# Week 07 Assignment: Mini TCSOL Teaching-Study Design

## Task

Use the Week 07 notebook to create a small research-design package for a short-term Chinese teaching activity.

## Core Minimum

1. Choose one `target_structure` that could be taught in a short course, for example result complements such as `找到了`, `听懂了`, or `写完了`.
2. Identify the unit of analysis.
3. Identify the grouping variable.
4. Read the five rubric criteria.
5. Write a 120-180 word Methods draft.

## Guided Core

1. Load `data/raw/week07_short_course_learner_tasks.csv`.
2. Keep only rows where `usable_task == True`.
3. Export:
   - `week07_variable_map.csv`
   - `week07_rubric_gain_summary.csv`
   - `week07_activity_summary.csv`
4. Export:
   - `week07_total_gain_by_activity.png`
   - `week07_rubric_gain_by_criterion.png`
5. Write one figure caption for each figure.

## Minimum Path

Follow this order if programming still feels new:

1. Run the setup cell and check that it prints the Week 07 folder and SHA-256.
2. Run all notebook cells from top to bottom.
3. Open the 3 exported CSV files.
4. Inspect the 2 exported figures.
5. Write 2 captions.
6. Write the Methods draft.

Caption frame for Figure 1:

> Figure 1. Mean rubric gain by activity focus in the synthetic Week 07 TCSOL task dataset (`N = ___` usable records). The figure is descriptive because activity groups are small and not randomly assigned.

Caption frame for Figure 2:

> Figure 2. Mean gain by rubric criterion across usable learner task records. The figure shows where task evidence is strongest, not which teaching activity caused improvement.

## Required Writing

Your Methods draft must include:

- course context;
- unit of analysis;
- activity focus;
- target structure;
- rubric criteria;
- what counts as usable data;
- one limitation sentence;
- no causal claim such as "proved", "caused", or "most effective".

Write the unit clearly: one row is one learner task record. `learner_id` is only the identifier.

## Sentence Frames

Vietnamese thinking frame:

> Nghiên cứu mini này dùng dữ liệu task synthetic từ một khóa Hán ngữ ngắn hạn. Đơn vị phân tích là `___`. Activity focus gồm `___`, `___`, và `___`; target structure là `___`. Learner evidence được mã hóa bằng rubric 1-5 gồm `___`. Các bản ghi incomplete bị loại khỏi phân tích. Vì `___`, kết quả chỉ dùng để mô tả design và evidence, không dùng để kết luận nhân quả.

English paper frame:

> This mini study uses a synthetic short-course TCSOL task dataset. The unit of analysis is `___`. Activity focus is coded as `___`, `___`, and `___`, and the target structure is `___`. Learner task evidence is summarized with a 1-5 rubric covering `___`. Incomplete task records are excluded from the analysis. Because `___`, the analysis supports descriptive design practice rather than causal claims.

## Stretch

Add one qualitative code to `main_difficulty` in a copied DataFrame, not in the raw CSV. The notebook checks the raw-data hash for reproducibility, so editing the raw CSV will trigger an error.

```python
usable_stretch = usable.copy()
usable_stretch.loc[usable_stretch["learner_id"] == "L003", "main_difficulty"] = "needs result-complement contrast"
```

Then write two sentences:

1. What learning difficulty does this code capture?
2. Which source or teaching framework makes the code meaningful?

## Submission

Submit:

- completed notebook;
- `week07_variable_map.csv`;
- `week07_rubric_gain_summary.csv`;
- `week07_activity_summary.csv`;
- two figures;
- two figure captions;
- Methods draft;
- source note for proficiency/can-do or Chinese proficiency standard alignment.

Source note template:

> I used [source name] to frame learning outcomes because it describes what learners can do through communicative tasks. I adapted the source to this short-course TCSOL setting by focusing on `[target structure]`, `[task type]`, and `[rubric criterion]`.
