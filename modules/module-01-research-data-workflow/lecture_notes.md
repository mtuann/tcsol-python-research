# Module 01 Lecture Notes: Research Data Workflow

Source check: 2026-06-09

## 1. Why This Module Matters

### Vietnamese

Một người mới học Python thường muốn hỏi ngay: "Dùng lệnh nào để vẽ chart?" Trong research paper, câu hỏi đúng hơn là:

> Figure này sẽ hỗ trợ claim nào, và dữ liệu phía sau nó có đủ rõ để người đọc tin không?

Module 01 vì vậy chưa cố dạy nhiều cú pháp. Nó dạy cách nghĩ: data source -> raw table -> analysis table -> figure -> caption -> limitation. Nếu học viên hiểu chuỗi này, các module sau về cleaning, transform, chart type và writing sẽ có chỗ đứng.

### English

A beginner often asks: "What command draws the chart?" In an academic paper, the better question is:

> What claim will this figure support, and is the data behind it clear enough for readers to trust?

Module 01 therefore does not overload syntax. It teaches the workflow: data source -> raw table -> analysis table -> figure -> caption -> limitation.

## 2. Core Concepts

| Concept | Vietnamese explanation | English explanation |
|---|---|---|
| Paper question | Câu hỏi nghiên cứu mà figure cần phục vụ. | The research question that the figure supports. |
| Data source | Nơi dữ liệu đến từ đâu: public database, survey, task log, coding sheet. | Where the data comes from: public database, survey, task log, coding sheet. |
| Unit of observation | Một dòng trong bảng đại diện cho cái gì. | What one row in the table represents. |
| Raw data | Bảng ban đầu, thường còn nhiều cột, missing values, hoặc metadata. | The original table, often with many columns, missing values, or metadata. |
| Analysis table | Bảng đã đủ gọn để plot hoặc model. | A prepared table that is ready for plotting or modeling. |
| Figure output | File PNG, SVG, hoặc PDF có thể đưa vào paper. | A PNG, SVG, or PDF file that can be used in a paper. |
| Caption | Đoạn văn giải thích figure, nguồn, mẫu, measure, pattern và limitation. | Text explaining the figure, source, sample, measure, pattern, and limitation. |

## 3. The Beginner Workflow

1. Write one paper question.
2. Identify one possible dataset.
3. State what one row means.
4. Check whether the source is official, reproducible, and ethical.
5. Read the CSV in Python.
6. Inspect shape, columns, and first rows.
7. Create a simple summary table.
8. Draw one honest figure.
9. Export the figure.
10. Write a caption and one limitation.

## 4. Practice Layers

### Lab A: Toy Data

File: `data/raw/module01_toy_project_inventory.csv`

Purpose: make the workflow visible without forcing the learner into a large dataset. Each row is a possible paper project. The learner practices reading the table and identifying `paper_area`, `unit_of_observation`, `data_role`, and `figure_candidate`.

### Lab B: Academic Source Inventory

File: `data/raw/module01_public_source_inventory.csv`

Purpose: compare realistic data sources before downloading huge files. The learner sees that trusted public data sources can still be difficult for beginners because they have metadata, licensing, survey design, missingness, and citation requirements.

### Lab C: Transfer Question Bank

File: `data/raw/module01_transfer_question_bank.csv`

Purpose: transfer the same workflow to education policy, TCSOL, contrastive linguistics, translation studies, and academic writing.

## 5. Live Coding Flow

The notebook intentionally uses only three beginner patterns:

```python
pd.read_csv("file.csv")
df.shape
df.head()
```

Then it adds one gentle transformation:

```python
sources["readiness_score"] = sources["trust_score"] * 20 - sources["beginner_complexity"] * 8
```

This creates a meaningful figure without requiring advanced statistics. The point is not that this score is "true"; the point is that every figure needs an explicit rule that can be inspected.

## 6. Paper-Facing Output

By the end, the learner should have:

- one data inventory table;
- one source readiness table;
- one source readiness figure;
- one caption draft;
- one limitation sentence.

Suggested caption pattern:

> Figure X shows [measure] for [sample/source]. The figure indicates [main visible pattern]. Because [limitation], the figure should be interpreted as [appropriate scope], not as [overclaim].

## 7. Common Mistakes

| Mistake | Why it hurts the paper | Repair |
|---|---|---|
| Starting from a chart type | The figure may not match the research claim. | Start from a paper question and unit of observation. |
| Linking a data source without reading metadata | Reader cannot assess measurement validity. | Record source, access date, definitions, and limitations. |
| Treating raw data as analysis-ready | Missingness or duplicated units may distort the figure. | Inspect shape, columns, missing values, and row meaning. |
| Writing a decorative caption | Caption does not explain evidence. | Mention source, sample, measure, pattern, and limitation. |

## 8. Teaching Notes

For a learner with no programming background, keep the live coding slow:

- type one command at a time;
- ask "what do we expect to see?" before running;
- read the output aloud;
- connect every line of code to the paper workflow;
- avoid explaining Python internals unless the learner asks.

The most important question to repeat is:

> What does one row mean?

If the learner can answer this, they are ready for Module 02.
