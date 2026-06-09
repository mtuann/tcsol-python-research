# Week 12 Assignment: MTPE Effort Analysis

## Core Submission

Submit:

1. `week12_mtpe_effort_summary.csv`
2. `week12_revision_type_summary.csv`
3. `week12_time_by_system.png`
4. one figure caption;
5. one 2-3 sentence source note;
6. one 130-180 word Results paragraph.

The notebook also exports `week12_submission_text.md` as a model text file. You may edit that text instead of copying from output cells.

## Core Steps

1. Open `live_coding.html` first to understand the workflow.
2. Run `live_coding.ipynb` in Colab or locally.
3. Load `data/raw/week12_mtpe_segments.csv`.
4. Confirm that one source segment has an MT output and a post-edited text.
5. Confirm which column is the reference anchor and which two columns are compared for edit distance.
6. Run the edit-distance cell and read `char_edit_distance` plus `normalized_edit_distance`.
7. Summarize post-editing time by `mt_system`.
8. Export the effort table, revision-type table, time figure, caption, source note, and Results paragraph.
9. Write the Results paragraph with one limitation.

## Caption Frame

> Figure 1 compares mean post-editing time across three synthetic MT profiles for 10 Chinese-Vietnamese education-policy source segments (30 system-segment rows). Lower time indicates less observed post-editing effort in this classroom dataset.

## Results Paragraph Frame

> In the synthetic Week 12 MTPE dataset, `___` required the lowest mean post-editing time, while `___` required the highest. The edit-distance and revision-type tables suggest that `___`. However, the dataset is synthetic and edit distance captures visible text change rather than all cognitive effort, so the result should be interpreted as a workflow illustration.

## Stretch

Export `week12_edit_distance_by_system.png` and write a second caption explaining why edit distance and time might not always rank systems identically.
