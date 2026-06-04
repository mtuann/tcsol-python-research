# Week 13 Assignment: Education Policy Coding Table

## Core Submission

Submit:

1. `week13_policy_area_summary.csv`
2. `week13_timeline.csv`
3. one policy timeline or policy-area figure;
4. one figure caption;
5. one 2-3 sentence source note;
6. one 130-180 word Results paragraph.

The notebook exports `week13_submission_text.md` as a model text file. Edit it in your own words.

## Core Steps

1. Open `live_coding.html` first to understand the workflow.
2. Run `live_coding.ipynb` in Colab or locally.
3. Load `data/raw/week13_policy_coding.csv`.
4. Confirm the unit of analysis: one coded source row.
5. Convert `issue_date` to a datetime column.
6. Sort rows into a timeline and export `week13_timeline.csv`.
7. Count `policy_area`, `source_type`, and `evidence_type`.
8. Export one figure and write a caption.
9. Write a Results paragraph with one limitation.

## Caption Frame

> Figure 1 shows the timeline of 12 coded policy-source rows in the Week 13 classroom dataset. Rows are paraphrased and synthetic for practice; the figure describes source coverage rather than policy impact.

## Results Paragraph Frame

> In the Week 13 policy-source coding dataset, `___` appears most often. The evidence types include `___`, which means the table combines policy plans, statistical bulletins, metadata standards, and coding models. This pattern describes the source set; it does not prove that any policy has been implemented or caused an outcome.

## Stretch

Export `week13_theme_by_source_crosstab.csv` and write 3-4 sentences explaining whether your coding scheme needs a new theme or clearer theme definitions.
