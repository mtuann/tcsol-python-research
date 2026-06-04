# Week 09: Chinese-Vietnamese Contrastive Data

This week turns Chinese-Vietnamese examples into a small contrastive analysis package. The learner builds a bilingual example table, uses simple string matching to inspect visible patterns, counts contrastive phenomena, reads a risk crosstab, chooses representative examples, and writes a cautious analysis paragraph.

## Research Frame

- Question: In a small teaching-oriented Chinese-Vietnamese contrastive example bank, which phenomena carry higher teaching risk for beginner Vietnamese learners of Chinese?
- Unit of analysis: one row, meaning one contrastive example pair. It is not one learner and not one translation system output.
- Dataset: synthetic contrastive examples with Chinese sentence/phrase, pinyin, Vietnamese rendering, pattern labels, similarity level, teaching risk, and a Week 08 learner-error link.
- Core output: phenomenon frequency table, phenomenon-by-risk crosstab, teaching priority table, selected examples table, two figures, and a 120-170 word contrastive analysis paragraph.
- Stretch output: one added example with a checked source note and a short explanation of why it should or should not become a teaching point.

## Beginner Scope

Week 09 is not NLP, automatic parsing, or a full theory course in contrastive linguistics. The core pattern is:

```text
Chinese example + Vietnamese rendering -> contrastive code -> frequency/risk table -> representative examples -> analysis paragraph
```

The learner should be able to explain:

- a contrastive example row compares one Chinese pattern with one Vietnamese rendering;
- `phenomenon` is a human coding label, not an automatic linguistic truth;
- `str.contains()` can find visible text patterns, but interpretation still needs human checking;
- `pd.crosstab()` can show which phenomena have more low/medium/high teaching-risk examples;
- representative examples help an analysis paragraph stay concrete;
- contrastive evidence can guide teaching notes, but it should not overgeneralize about all Vietnamese learners.

## Weekly Materials

- `index.html`: learner-facing bilingual overview.
- `slides.html`: visual lecture deck with quick slide overview.
- `interactive_demo.html`: contrastive phenomenon + teaching-risk explorer.
- `lecture_notes.md`: instructor and learner notes.
- `live_coding.ipynb`: runnable notebook source.
- `live_coding.html`: rendered notebook for GitHub Pages.
- `assignment.md`: weekly submission instructions.
- `rubric.md`: assessment criteria.
- `readings.md`: required course note and source references.

## Core Minimum

- [ ] Load `week09_contrastive_examples.csv`.
- [ ] Filter rows where `include_in_table == True`.
- [ ] Read the unit of analysis and the top teaching-priority phenomenon.
- [ ] Use one `str.contains()` check for a visible Chinese pattern such as `了`, `到`, `完`, or `个`.
- [ ] Write a 120-170 word contrastive analysis paragraph.

## Guided Core

- [ ] Export `week09_phenomenon_frequency.csv`.
- [ ] Export `week09_pattern_by_risk.csv`.
- [ ] Export `week09_teaching_priority_table.csv`.
- [ ] Export `week09_selected_contrastive_examples.csv`.
- [ ] Export `week09_phenomenon_frequency.png`.
- [ ] Export `week09_risk_by_phenomenon_heatmap.png`.
- [ ] Write one caption for each figure.

## Stretch

- [ ] Add one new contrastive example row.
- [ ] Decide whether it belongs in the main table.
- [ ] Add a source note from a dictionary, grammar, textbook, corpus, paper, or official standard.
- [ ] Explain why the example is useful for teaching, translation, or policy-text reading.

## Analysis Frame

Vietnamese thinking frame:

> Trong `N = 60` contrastive examples dùng được, hiện tượng có teaching-priority score cao nhất là `result_complement` (`n = 11`, mean risk = 2.55). Bảng risk cho thấy các ví dụ high-risk tập trung ở những pattern mà Chinese và Vietnamese không tương ứng một-một. Vì dữ liệu synthetic và được thiết kế để luyện workflow, kết quả chỉ nên dùng để chọn ví dụ dạy học và viết contrastive note, không dùng để khẳng định mọi learner Việt Nam sẽ mắc lỗi như nhau.

English paper frame:

> In the usable Week 09 contrastive example records (`N = 60`), `result_complement` received the highest teaching-priority score (`n = 11`, mean risk = 2.55). The risk table suggests that higher-risk examples cluster around patterns where Chinese and Vietnamese do not map one-to-one. Because the dataset is synthetic and designed for workflow practice, the results should guide example selection and contrastive teaching notes rather than support broad claims about all Vietnamese learners of Chinese.

## Data Provenance

- File: `data/raw/week09_contrastive_examples.csv`
- Type: synthetic contrastive teaching dataset, not real learner data and not a corpus sample.
- SHA-256: `78cbedef8cdd1eb5d093864ee4e4c1c75aeb963b9537b540b49c4a251faba3a8`
- Design basis: contrastive analysis for TCSOL examples, connected to Week 08 learner-error categories and to official/reference resources listed in `readings.md`.
