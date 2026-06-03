# Week 01 Exercises

## Core Exercise A: Copy and Modify

Open `live_coding.ipynb`. Find the cell with these variables:

```python
my_name = "Your name"
my_research_area = "TCSOL"
my_topic = "short-term Chinese teaching"
```

Change them to fit your own interest.

Run the cell. Then write one sentence:

```text
My current research area is ..., and I want to study ...
```

## Core Exercise B: Guided Problem

Use the dataset `data/raw/week01_research_tracks.csv`.

Complete these tasks in the notebook:

1. Count how many research tracks are listed.
2. Print the name of each track.
3. Choose one track that feels closest to your future study.
4. Copy its small research question into your notebook.

The CSV-loading code is sample code. Your job is to run it and read the output, not to understand every symbol yet.

Checklist:

- [ ] I ran the CSV loading cell.
- [ ] I saw four rows.
- [ ] I can explain what one row means.
- [ ] I selected one track.

## Core Exercise C: Research-Style Task

This is the draft of the memo you will submit in the assignment. It is not a second separate memo.

Write a 100-150 word paragraph answering:

```text
Which research track seems most useful for your future Master's study, and what data would you need first?
```

Your paragraph should include:

- one research area;
- one small question;
- one possible dataset;
- one limitation.

## Stretch Exercise

Add one new row to a copy of the CSV file. The new row should describe a project you might actually want to do.

Suggested columns to fill:

- `track_id`
- `track`
- `broad_interest`
- `small_research_question`
- `unit_of_observation`
- `starter_dataset`
- `likely_output`
- `beginner_python_task`

Do not edit the original raw file. Save your copy as:

```text
data/processed/week01_my_research_track.csv
```
