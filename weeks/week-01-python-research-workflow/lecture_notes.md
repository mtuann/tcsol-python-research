# Week 01 Lecture Notes: Python as a Research Workflow

## Core Idea

Python is not the goal of this course. Python is the tool we use to make research work clearer, more repeatable, and easier to turn into paper evidence.

For this learner, Python will usually help with four kinds of work:

1. organizing data from a class, test, survey, translation task, or policy document;
2. checking the data instead of relying on memory or manual counting;
3. producing a table or figure;
4. writing a more transparent Methods and Results section.

## What Is a Notebook?

A Jupyter notebook has two important cell types.

| Cell type | Use |
|---|---|
| Markdown | Write explanations, headings, research questions, captions, and interpretation. |
| Code | Run Python commands. |

The best research notebook reads like a small paper draft:

```text
research question
data source
code
table or figure
interpretation
limitation
```

## The First Python Ideas

### 1. `print`

`print` shows a message or result.

```python
print("My research topic is short-term Chinese teaching.")
```

### 2. Variables

A variable is a name that stores a value.

```python
topic = "Chinese measure words"
research_area = "TCSOL"
```

Think of a variable as a labeled note. Python remembers the value so we can reuse it later.

### 3. Strings

Text in Python is usually written inside quotation marks.

```python
question = "How do learner answers change after a short measure-word lesson?"
```

### 4. Lists of rows

When we read a CSV file, Python can store the rows in a list.

```python
rows = [
    {"track": "TCSOL"},
    {"track": "MTPE"}
]
```

For Week 01, the learner only needs to know that:

- a list can contain several rows;
- `len(rows)` counts how many rows there are;
- `rows[0]` shows the first row.

## Research Skill: Topic vs Research Question

A broad topic is not yet ready for data analysis.

| Broad topic | Better research question |
|---|---|
| Teaching Chinese grammar | How do learner answers change before and after a short measure-word activity? |
| Chinese-Vietnamese comparison | Which ba-construction examples create word-order transfer problems for Vietnamese learners? |
| Machine translation | Which MT error type is most frequent in Chinese-Vietnamese policy sentences? |
| Education policy | How do recent policy excerpts discuss teacher development? |

A useful beginner research question should be:

- small enough for one project;
- connected to observable data;
- clear about the unit of observation;
- able to produce at least one table or figure.

## Worked Example

Broad interest:

```text
I care about short-term Chinese teaching.
```

Data-ready question:

```text
How do learner answers change before and after a two-week measure-word activity?
```

Possible data:

```text
one row = one learner's answer to one test item
```

Possible output:

```text
a descriptive table comparing pre-test and post-test answers
```

Important limitation:

```text
A pre/post change is descriptive. It does not prove causality by itself.
```

## Four Tiny Data Examples

These examples show what future research data might look like. They are for orientation only; the learner does not analyze them in Week 01.

| Track | One possible row |
|---|---|
| TCSOL | `learner_id=S001; item_id=Q03; pre_answer=一书; post_answer=一本书; target=measure_word` |
| Contrastive | `zh=我把书放在桌子上; vi=Tôi đặt sách lên bàn; predicted_difficulty=把 omitted` |
| MTPE | `zh_source=教育数字化推动资源共享; vi_mt=Giáo dục số thúc đẩy tài nguyên chia sẻ; vi_postedit=Giáo dục số thúc đẩy việc chia sẻ tài nguyên` |
| Policy | `title=教育强国建设规划纲要（2024-2035年）; theme=digitalization; excerpt=教育数字化` |

## Common Mistakes

### Mistake 1: Trying to learn everything at once

Do not try to learn pandas, statistics, MT metrics, and visualization in Week 01. The goal is only to run a notebook and understand the research workflow.

### Mistake 2: Choosing a question too broad for data

Too broad:

```text
How should Chinese be taught to Vietnamese students?
```

Better:

```text
Which three measure-word errors are most frequent in a beginner class after a short lesson?
```

### Mistake 3: Forgetting the unit of observation

Always ask:

```text
What does one row in my dataset represent?
```

Examples:

- one learner;
- one test answer;
- one sentence pair;
- one translation segment;
- one coded policy excerpt.

## Mini Cheat Sheet

```python
print("message")              # show a message
topic = "TCSOL"               # store text in a variable
len(rows)                     # count items
rows[0]                       # first item
row["track"]                  # value in the track column
```

## Connection to Final Projects

By the end of this course, the learner may choose one of these final project paths:

- TCSOL: pre-test/post-test and learner errors;
- Chinese-Vietnamese contrastive analysis: sentence pairs and teaching notes;
- MTPE: MT output, human post-editing, and error labels;
- education policy: policy excerpts, themes, metadata, and timelines.

Week 01 prepares the foundation: every project needs a clear question, a data unit, and a small output that can become part of a paper.
