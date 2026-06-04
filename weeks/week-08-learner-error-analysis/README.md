# Week 08: Learner Error Analysis

This week turns learner responses into a small error-analysis Results package. The learner codes response-level errors, counts error categories, cross-tabulates errors by target structure, chooses representative examples, and writes a cautious Results paragraph.

## Research Frame

- Question: In usable short-course Chinese learner responses, which error categories appear most often, and which target structures do they connect to?
- Unit of analysis: one row, meaning one learner response to one item. `learner_id` is only the ID.
- Dataset: synthetic learner-error coding data with prompts, expected answers, learner answers, on-prompt status, error categories, severity, and correction notes.
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
- [ ] Filter rows where `usable_error == True` and `on_prompt == True`.
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

> Trong 68 response rows dùng được và đúng prompt, 57 dòng có coded learner error. Lỗi xuất hiện nhiều nhất là `tone_marking` (`n = 13`, 22.8% coded errors), tiếp theo là `result_complement`, `measure_word`, `aspect_marker`, và `word_order` (`n = 11` mỗi nhóm). Vì dữ liệu synthetic, sample nhỏ và các off-prompt responses đã bị loại khỏi bảng chính, kết quả chỉ dùng để chọn teaching priority và ví dụ dạy lại, không dùng để khái quát về toàn bộ learner Việt Nam học tiếng Trung.

English paper frame:

> In the on-prompt usable Week 08 learner-response records (`N = 68`), 57 rows contained a coded learner error. The most frequent category was `tone_marking` (`n = 13`, 22.8% of coded errors), followed by `result_complement`, `measure_word`, `aspect_marker`, and `word_order` (`n = 11` each). Because the dataset is synthetic and small, and off-prompt responses were excluded from the main table, the pattern should guide follow-up teaching design rather than support broad claims about Vietnamese learners of Chinese.

## Data Provenance

- File: `data/raw/week08_learner_error_coding.csv`
- Type: synthetic learner-response dataset for workflow practice, not real student data.
- SHA-256: `0f17314ecc223b8a0228f46212949ba0bc4b56aeca6848b891e9c00cc263d3d4`
- Design basis: learner error analysis for TCSOL, connected to Week 07's target-structure/rubric habit and to proficiency/can-do sources.
