# Week 07: TCSOL Short-Course Research

This week turns a short-term Chinese teaching activity into a small research design. The learner builds a rubric, maps classroom variables, summarizes learner-task evidence, and writes a Methods draft.

## Research Frame

- Question: In a short-term Chinese course on result complements in service dialogues, which activity focus shows higher descriptive rubric gain?
- Unit of analysis: one row, meaning one synthetic learner task record. `learner_id` is only the ID.
- Dataset: synthetic short-course TCSOL task data with one shared target structure, five rubric scores, and teacher notes.
- Core output: variable map, rubric gain table, activity summary table, two figures, and a 120-180 word Methods draft.
- Stretch output: one added qualitative difficulty code with a justification.

## Beginner Scope

Week 07 is not an experimental-design course. The core pattern is:

```text
teaching goal -> target structure -> learner task -> rubric -> classroom variables -> Methods draft
```

The learner should be able to explain:

- a `target_structure` is the language feature being taught;
- a rubric converts task evidence into consistent observations;
- `activity_focus` is a grouping variable, not proof of effectiveness;
- a Methods paragraph must define unit, variables, rubric, and limitation;
- source notes connect the design to proficiency/can-do frameworks.

## Weekly Materials

- `index.html`: learner-facing bilingual overview.
- `slides.html`: visual lecture deck with quick slide overview.
- `interactive_demo.html`: rubric + classroom variable explorer.
- `lecture_notes.md`: instructor and learner notes.
- `live_coding.ipynb`: runnable notebook source.
- `live_coding.html`: rendered notebook for GitHub Pages.
- `assignment.md`: weekly submission instructions.
- `rubric.md`: assessment criteria.
- `readings.md`: required course note and source references.

## Core Minimum

- [ ] Choose a realistic short-course `target_structure` such as result complements (`找到了`, `听懂了`, `写完了`).
- [ ] Read the five rubric criteria.
- [ ] Identify the unit of analysis and grouping variable.
- [ ] Write a 120-180 word Methods draft.

## Guided Core

- [ ] Load `week07_short_course_learner_tasks.csv`.
- [ ] Filter rows where `usable_task == True`.
- [ ] Export `week07_variable_map.csv`.
- [ ] Export `week07_rubric_gain_summary.csv`.
- [ ] Export `week07_activity_summary.csv`.
- [ ] Export `week07_total_gain_by_activity.png`.
- [ ] Export `week07_rubric_gain_by_criterion.png`.

## Stretch

- [ ] Add one new qualitative code for `main_difficulty`.
- [ ] Explain why the code is needed for the research question.
- [ ] Rewrite one rubric descriptor using an ACTFL/Can-Do, CEFR, or Chinese proficiency standard source note.

## Methods Frame

Vietnamese thinking frame:

> Nghiên cứu mini này dùng dữ liệu task synthetic từ một khóa Hán ngữ ngắn hạn. Đơn vị phân tích là một dòng learner task record; `learner_id` chỉ là mã định danh. Activity focus gồm `___`, `___`, và `___`; target structure là result complements trong service dialogues. Learner evidence được mã hóa bằng rubric 1-5 gồm task completion, accuracy, fluency, interaction strategy và confidence. Phân tích mô tả rubric gain theo activity focus và ghi lại learning difficulty phổ biến. Vì dữ liệu synthetic, sample nhỏ và không random assignment, kết quả chỉ dùng để luyện thiết kế nghiên cứu và viết Methods.

English paper frame:

> This mini study uses a synthetic short-course TCSOL task dataset. The unit of analysis is one row: one learner task record; `learner_id` is only the identifier. Activity focus is coded as `___`, `___`, and `___`, and the target structure is result complements in service dialogues. Learner task evidence is summarized with a 1-5 rubric covering task completion, accuracy, fluency, interaction strategy, and confidence. The analysis descriptively summarizes rubric gains by activity focus and records frequent learning difficulties. Because the dataset is synthetic, small, and not randomly assigned, the analysis supports research-design practice rather than causal claims.

## Data Provenance

- File: `data/raw/week07_short_course_learner_tasks.csv`
- Type: synthetic teaching dataset for workflow practice, not real student data.
- SHA-256: `d1cb69df35232bce0845394fe179c9ba4b1c3ecce15e7a2171f2397b6ca3fed6`
- Design basis: short-course TCSOL task evidence, aligned with proficiency/can-do thinking from ACTFL/NCSSFL-ACTFL, CEFR, and Chinese proficiency standards.
