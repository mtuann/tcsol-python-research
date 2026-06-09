# Week 12 Lecture Notes: MTPE Workflow

## Plain-Language Concept

Machine translation post-editing (MTPE) begins after an MT output already exists. A post-editor reads the source, checks the MT output, and edits the target text until it is acceptable for the task.

Week 12 uses two beginner-friendly effort signals:

1. `pe_time_seconds`: how long the post-editing took in the synthetic classroom log.
2. `edit_distance`: how much the visible text changed from MT output to post-edited text.

These are related but not identical. A short edit can take a long time if the meaning is difficult. A long surface edit can be quick if the fix is obvious.

## Research Use

In a Translation Studies or MTPE paper, this workflow supports a Results subsection that says:

- which MT profile required less post-editing time;
- whether edit distance points in the same direction;
- what revision labels explain the effort;
- why the result is limited.

## Annotated Code

```python
from rapidfuzz.distance import Levenshtein

data["char_edit_distance"] = [
    Levenshtein.distance(mt, pe)
    for mt, pe in zip(data["vi_mt_output"], data["vi_postedit"])
]
```

The key idea is comparing two text columns row by row: before editing and after editing.

## Common Mistakes

1. Treating edit distance as mental effort. It is only visible text change.
2. Forgetting that time logs need context: editor, task, domain, and quality target.
3. Comparing MT profiles without checking whether each profile translated the same source segments.
4. Calling synthetic classroom data real productivity evidence.

## Mini Cheat Sheet

```python
Levenshtein.distance(a, b)
data["new_column"] = ...
data.groupby("mt_system")
.mean()
.to_csv(...)
plt.barh(...)
```

## Connection To Final Project

This week can support a small MTPE workflow study. It also prepares the learner to write a Methods note about how post-editing effort was operationalized.
