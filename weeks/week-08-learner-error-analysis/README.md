# Week 08: Learner Error Analysis

This week turns learner responses into a small error-analysis Results package. The learner codes response-level errors, counts error categories, cross-tabulates errors by target structure, chooses representative examples, and writes a cautious Results paragraph.

## Research Frame

- Question: In usable short-course Chinese learner responses, which error categories appear most often, and which target structures do they connect to?
- Unit of analysis: one row, meaning one learner response to one item. `learner_id` is only the ID.
- Dataset: synthetic learner-error coding data with prompts, expected answers, learner answers, error categories, severity, and correction notes.
- Core output: error frequency table, error-by-target crosstab, teaching priority table, representative examples table, two figures, and a 120-160 word Results paragraph.
- Stretch output: one recoded example with a justification and a short note about how the code improves teaching interpretation.

## Beginner Scope

Week 08 is not corpus linguistics, NLP, or automatic error detection. The core pattern is:

```text
learner response -> error code -> frequency table -> crosstab -> examples -> Results paragraph
```

The learner should be able to explain:

- a response row is one answer to one item;
- `error_category` is a human coding label, not a machine diagnosis;
- `value_counts()` answers “which code appears most often?”;
- `pd.crosstab()` answers “which code appears with which target structure?”;
- representative examples help a Results paragraph stay concrete;
- small synthetic data can suggest teaching priorities but cannot diagnose all learners.

## Weekly Materials

- `index.html`: learner-facing bilingual overview.
- `slides.html`: visual lecture deck with quick slide overview.
- `interactive_demo.html`: error category + teaching priority explorer.
- `lecture_notes.md`: instructor and learner notes.
- `live_coding.ipynb`: runnable notebook source.
- `live_coding.html`: rendered notebook for GitHub Pages.
- `assignment.md`: weekly submission instructions.
- `rubric.md`: assessment criteria.
- `readings.md`: required course note and source references.

## Core Minimum

- [ ] Load `week08_learner_error_coding.csv`.
- [ ] Filter rows where `usable_error == True`.
- [ ] Separate rows where `has_error == True`.
- [ ] Read the top error category and its count.
- [ ] Write a 120-160 word Results paragraph.

## Guided Core

- [ ] Export `week08_error_frequency.csv`.
- [ ] Export `week08_error_by_target_structure.csv`.
- [ ] Export `week08_teaching_priority_table.csv`.
- [ ] Export `week08_representative_examples.csv`.
- [ ] Export `week08_error_category_frequency.png`.
- [ ] Export `week08_error_by_target_heatmap.png`.
- [ ] Write one caption for each figure.

## Stretch

- [ ] Create `error_rows_stretch = error_rows.copy()`.
- [ ] Recode one learner answer into a clearer error category.
- [ ] Explain why the new code is better for teaching.
- [ ] Add one sentence on whether a possible Vietnamese transfer explanation is plausible or only a hypothesis.

## Results Frame

Vietnamese thinking frame:

> Trong 76 response rows dùng được, 66 dòng có coded learner error. Lỗi xuất hiện nhiều nhất là `word_order` (`n = 17`, 25.8% coded errors), tiếp theo là `measure_word` (`n = 13`). Bảng chéo cho thấy `word_order` xuất hiện ở nhiều target structures, không chỉ một item. Vì dữ liệu synthetic và sample nhỏ, kết quả nên dùng để chọn teaching priority và ví dụ dạy lại, không dùng để khái quát về toàn bộ learner Việt Nam học tiếng Trung.

English paper frame:

> In the usable Week 08 learner-response records (`N = 76`), 66 rows contained a coded learner error. The most frequent category was `word_order` (`n = 17`, 25.8% of coded errors), followed by `measure_word` (`n = 13`). The crosstab suggests that `word_order` appeared across multiple target structures. Because the dataset is synthetic and small, the pattern should guide follow-up teaching design rather than support broad claims about Vietnamese learners of Chinese.

## Data Provenance

- File: `data/raw/week08_learner_error_coding.csv`
- Type: synthetic learner-response dataset for workflow practice, not real student data.
- SHA-256: `a96e92a6fa3d746e77e0b6bb97a5ee01bf55f15c6690e23bac0b240feedd6fc0`
- Design basis: learner error analysis for TCSOL, connected to Week 07's target-structure/rubric habit and to proficiency/can-do sources.
