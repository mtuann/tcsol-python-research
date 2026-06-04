# Week 12 Exercises

## A. Before / After Check

Look at segment `P001`.

1. Copy `zh_source`, `vi_reference`, `vi_mt_output`, and `vi_postedit` for each profile.
2. Mark which two columns are compared for edit distance.
3. Mark which column is only a reference anchor for meaning.
4. Highlight one phrase that changed during post-editing.
5. Write one sentence explaining why the edit was needed.

## B. Edit Distance Direction

Fill in the blanks:

> Higher edit distance means more visible text changes. Lower normalized edit distance usually means less surface editing.

Then run:

```python
data.sort_values("normalized_edit_distance")[["segment_id", "mt_system", "normalized_edit_distance"]]
```

Answer:

> The lowest-edit row is `___`; the highest-edit row is `___`.

## C. Effort Table

Use `week12_mtpe_effort_summary.csv`.

Write 2 sentences:

1. Which MT profile has the lowest mean time?
2. Which MT profile has the highest mean time?

## D. Revision Labels

Use `week12_revision_type_summary.csv`.

Mini guide:

- `omission`: meaning was missing and had to be restored.
- `terminology`: a domain or policy term was repaired.
- `word_order`: Vietnamese sentence order was repaired.
- `style`: meaning was acceptable, but register or phrasing was polished.
- `no_error`: accepted variant; no post-edit was needed.

Write 2-3 sentences explaining whether the high-effort profile mostly needs omission, terminology, word-order, or style edits.

## E. Stretch: Time vs Edit Distance

Choose one segment from `week12_segment_edit_sample.csv`. Compare:

- `pe_time_seconds`
- `normalized_edit_distance`
- `revision_type`
- `post_editor_note`

Write 3-4 sentences explaining why MTPE effort needs both numbers and human notes.
