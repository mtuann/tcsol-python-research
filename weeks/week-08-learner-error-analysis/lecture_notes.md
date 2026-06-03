# Week 08 Lecture Notes: Learner Error Analysis

## Learning Goals

By the end of Week 08, the learner should be able to:

1. define the unit of analysis for learner-error data;
2. distinguish usable response rows from coded-error rows;
3. compute an error frequency table;
4. build and read a target-structure by error-category crosstab;
5. select representative examples for a Results paragraph;
6. write a cautious learner-error Results paragraph.

## Why This Week Matters

Error analysis is useful for TCSOL only when it connects learner responses to teaching decisions. A frequency table shows which coded problems are visible. A crosstab shows where the problems appear. Representative examples make the pattern understandable to a reader.

## Concept Ladder

| Concept | Plain Meaning | Research Use |
|---|---|---|
| learner response | one answer to one prompt | unit of analysis |
| `error_category` | human coding label | countable pattern |
| `target_structure` | language feature being practiced | crosstab row |
| `severity` | simple 1-3 seriousness rating | teaching priority heuristic |
| representative example | one clear learner/expected pair | evidence in Results writing |

## Main Workflow

```python
usable = df[df["usable_error"] == True].copy()
error_rows = usable[usable["has_error"] == True].copy()
error_frequency = error_rows["error_category"].value_counts()
error_by_target = pd.crosstab(error_rows["target_structure"], error_rows["error_category"])
```

## Codebook Rule

A beginner-friendly error code should be:

- observable in the learner answer;
- specific enough to guide teaching;
- stable enough that another coder can understand it;
- separated from blame or learner ability labels;
- paired with examples.

## Reading The Week 08 Tables

Start with:

1. How many response rows are usable?
2. How many usable rows contain coded errors?
3. Which error category is most frequent?
4. Which target structures show the top error?
5. Which examples best explain the pattern?

Do not write "Vietnamese learners have word-order problems" from this dataset. Write "In the synthetic usable responses, `word_order` was the most frequent coded error and appeared across multiple target structures."

## Results Writing Frame

Vietnamese thinking frame:

> Trong `N = ___` usable response rows, `___` dòng có coded learner error. Error category xuất hiện nhiều nhất là `___` (`n = ___`), tiếp theo là `___`. Bảng chéo cho thấy `___` xuất hiện ở `___`. Vì dữ liệu synthetic và sample nhỏ, kết quả nên dùng để chọn teaching priority, không dùng để chẩn đoán cá nhân hoặc khái quát rộng.

English paper frame:

> In the usable learner-response records (`N = ___`), `___` rows contained a coded learner error. The most frequent error category was `___` (`n = ___`), followed by `___`. The crosstab suggests that `___` appeared in `___`. Because the dataset is synthetic and small, the result should be used to identify teaching priorities rather than diagnose individual learners.

## Common Risks

- Counting `no_error` as an error category.
- Treating possible Vietnamese transfer as proven transfer.
- Forgetting that severity is a simple teaching heuristic.
- Choosing examples that are unclear or too idiosyncratic.
- Writing a general claim from a small synthetic dataset.
