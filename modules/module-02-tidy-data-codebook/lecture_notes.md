# Module 02 Lecture Notes: Tidy Data and Codebook

Source check: 2026-06-09

## 1. Why This Module Matters

### Vietnamese

Học viên mới thường nghĩ một bảng CSV "có số" là đã có thể vẽ. Nhưng trong paper, bảng chỉ dùng được khi người viết biết:

- một dòng nghĩa là gì;
- mỗi cột là biến gì;
- biến đó là numeric, categorical, ordinal, date hay text;
- giá trị nào được phép;
- cột đó sẽ được giải thích trong Methods/caption như thế nào.

Module 02 nối Module 01 với các module cleaning và plotting sau này. Nếu codebook yếu, figure sau này sẽ dễ bị sai hoặc caption sẽ mơ hồ.

### English

A beginner may think that a CSV with numbers is already ready for plotting. In a paper, a table is usable only when the writer knows what one row means, what each column means, what type each variable has, what values are allowed, and how the variable will be described in Methods or captions.

## 2. Core Concepts

| Concept | Vietnamese explanation | English explanation |
|---|---|---|
| Wide table | Một observation có nhiều cột measure, ví dụ `pre_score` và `post_score`. | One observation has multiple measure columns, such as `pre_score` and `post_score`. |
| Long/tidy table | Mỗi dòng là một observation-measure-time rõ ràng. | Each row is a clear observation-measure-time record. |
| Identifier | Biến dùng để nhận diện đơn vị nhưng không phải outcome. | A variable that identifies units but is not an outcome. |
| Categorical | Nhóm không có thứ tự tự nhiên. | Groups without a natural order. |
| Ordinal | Nhóm có thứ tự nhưng khoảng cách không chắc bằng nhau. | Ordered categories where distances may not be equal. |
| Numeric | Biến định lượng có thể tính trung bình/tổng/hệ số. | Quantitative variable that can be averaged, summed, or modeled. |
| Date | Thời điểm, nên parse như date thay vì text. | Time point that should be parsed as date rather than plain text. |
| Codebook | Tài liệu giải thích từng cột. | Documentation explaining each column. |

## 3. Tidy Data Rule for This Module

The teaching rule:

> One row should represent one learner, one skill, and one time point.

Wide input:

```text
learner_id | pre_vocab_score | post_vocab_score | pre_speaking_score | post_speaking_score
```

Tidy output:

```text
learner_id | skill      | time | score
L001       | vocabulary | pre  | 42
L001       | vocabulary | post | 63
L001       | speaking   | pre  | 38
L001       | speaking   | post | 58
```

## 4. Practice Layers

### Lab A: Toy Learner Survey

File: `data/raw/module02_toy_learner_survey_wide.csv`

Purpose: teach wide-to-long reshaping with small learner data. The output table is `outputs/tables/module02_tidy_learner_scores_long.csv`.

### Lab B: Education Indicator Table

File: `data/raw/module02_education_indicator_wide.csv`

Purpose: show that public indicator data often starts with several measure columns. The tidy output is `country`, `year`, `school_level`, `indicator_name`, `indicator_value`.

### Lab C: Transfer Variable Bank

File: `data/raw/module02_transfer_variable_bank.csv`

Purpose: apply the same variable-design thinking to education policy, TCSOL, translation studies, contrastive linguistics, and academic writing.

## 5. Live Coding Flow

Key operations:

```python
wide = pd.read_csv("data/raw/module02_toy_learner_survey_wide.csv")
wide.shape
wide.head()
```

Then reshape:

```python
tidy = wide.melt(
    id_vars=["learner_id", "activity_group"],
    value_vars=["pre_vocab_score", "post_vocab_score"],
    var_name="measure_time",
    value_name="score"
)
```

The important teaching point is not only `melt()`. The important point is that `melt()` changes the unit of observation.

## 6. Codebook Minimum

Every important variable should have:

- variable name;
- variable type;
- role in analysis;
- unit of observation;
- allowed values;
- paper note.

Example:

| variable_name | variable_type | role | paper_note |
|---|---|---|---|
| `cefr_start` | ordinal | baseline proficiency | Do not average CEFR labels as if A1/A2/B1 were equally spaced numbers. |
| `time` | ordinal | measurement time | Created by reshaping pre/post columns. |
| `score` | numeric | outcome | Comparable within the same skill unless otherwise documented. |

## 7. Paper-Facing Output

By the end, the learner should have:

- one tidy learner-score table;
- one tidy education-indicator table;
- one codebook;
- one schema summary;
- one figure generated from tidy data;
- one caption that states the unit of observation after reshaping.

## 8. Teaching Notes

For a beginner, repeat these three questions:

1. What does one row mean before reshaping?
2. What does one row mean after reshaping?
3. What would the reader misunderstand if the codebook did not exist?

If the learner can answer those questions, Module 03 cleaning will make much more sense.
