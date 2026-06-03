# Tuần 02: Dữ liệu nghiên cứu dưới dạng bảng

English option: public HTML pages include a Tiếng Việt / English language switcher. Markdown files are Vietnamese-first authoring sources.

## Research Frame

- Research area: TCSOL, đối chiếu Hán-Việt, MTPE, hoặc chính sách giáo dục.
- Small research question: Dataset đầu tiên của paper cần những dòng và cột nào?
- Why this matters: nếu không định nghĩa rõ row/column, Python có thể chạy được nhưng kết quả không dùng được trong paper.

## Python Skill

- Main skill: đọc và hiểu dữ liệu dạng bảng bằng list/dictionary/CSV.
- Supporting skills: phân biệt row, column, value, schema, required/optional column.
- Functions/libraries: `csv.DictReader`, list of dictionaries, `print`, simple loops.

## Writing Support

- Paper section supported: Data/Materials description.
- Writing output: một data description 120-160 từ cho dataset đầu tiên.
- Tool support: notebook Markdown; Word optional; Zotero chưa bắt buộc; Overleaf chưa cần.
- Sentence frame: "The dataset is organized at the level of [unit of observation]. Each row contains [required columns], which allows the study to [paper purpose]."
- Common writing risk: mô tả dataset bằng tên file nhưng không nói rõ một dòng đại diện cho điều gì.

## Learning Objectives

By the end of this week, the learner can:

1. explain row, column, value, and schema in plain language;
2. read a small CSV as a list of dictionaries;
3. choose required vs optional columns for one research track;
4. write a short data description suitable for a paper draft.

## Required Outputs

- [ ] `live_coding.ipynb` runs from top to bottom.
- [ ] One research track is selected.
- [ ] One row unit is stated clearly.
- [ ] Required and optional columns are listed.
- [ ] A small table plan is exported to `outputs/tables/week02_selected_table_plan.csv`.
- [ ] A 120-160 word data description is written.
- [ ] Source/access date and privacy risks are recorded.

## Luồng học trên lớp

| Giai đoạn | Thời lượng | Hoạt động |
|---|---:|---|
| Warm-up | 10 phút | Nhìn một file CSV và hỏi: một dòng là gì? |
| Slides | 20 phút | Row, column, value, schema, source note. |
| Demo | 10 phút | Mở `interactive_demo.html` để chọn track và xem cột bắt buộc. |
| Live coding | 35 phút | Chạy notebook, đọc CSV bằng `csv.DictReader`, chọn table plan. |
| Guided practice | 25 phút | Làm Exercise A/B. |
| Writing bridge | 10 phút | Viết data description bằng sentence frame. |
| Wrap-up | 10 phút | Kiểm tra privacy risk và source note. |

## Core vs Stretch

Core:

- chạy notebook;
- chọn một track;
- đọc danh sách cột bắt buộc;
- xuất một table plan nhỏ;
- viết data description 120-160 từ.

Stretch:

- thêm một optional column và giải thích vì sao cần;
- so sánh hai track xem track nào có privacy risk cao hơn;
- phác thảo một data dictionary 5 dòng cho project tương lai.

Instructor-only:

- nhấn mạnh Week 2 chưa học pandas;
- tránh biến bài học thành thiết kế database nâng cao;
- preview Week 3: cùng schema này sẽ vào `pandas.DataFrame`.

## Files

- Week overview HTML: `index.html`
- Slides HTML: `slides.html`
- Interactive demo HTML: `interactive_demo.html`
- Rendered notebook HTML: `live_coding.html`
- Notebook source/download: `live_coding.ipynb`
- Data: `data/raw/week02_research_table_examples.csv`
- Column template: `data/raw/week02_column_planning_template.csv`
- Exercises: `exercises.md`
- Assignment: `assignment.md`
- Data dictionary: `data_dictionary.md`
- Rubric: `rubric.md`
- Readings: `readings.md`
