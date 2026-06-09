# Week 13 Assignment: Education Policy Coding Table

## Core Submission

Submit:

1. `week13_policy_area_summary.csv`
2. `week13_source_type_summary.csv`
3. `week13_timeline.csv`
4. one policy timeline or policy-area figure;
5. one figure caption;
6. one 2-3 sentence source note;
7. one 130-180 word Data/Methods paragraph.

The notebook exports `week13_submission_text.md` as a model text file. Edit it in your own words.

## Core Steps

1. Open `live_coding.html` first to understand the workflow.
2. Run `live_coding.ipynb` in Colab or locally.
3. Load `data/raw/week13_policy_coding.csv`.
4. Confirm the unit of analysis: one coded source row.
5. Convert `issue_date` to a datetime column and check `date_basis`.
6. Sort rows into a timeline and export `week13_timeline.csv`.
7. Count `policy_area`, `source_type`, and `evidence_type`.
8. Export one figure and write a caption.
9. Write a Data/Methods paragraph with one limitation.

## Caption Frame

> Figure 1 shows the timeline of 12 coded policy-source rows in the Week 13 classroom dataset. Rows are paraphrased and synthetic for practice; the figure describes source coverage rather than policy impact.

If you use the bar figure instead:

> Figure 2 shows policy-area counts in the Week 13 classroom dataset. Counts describe the small synthetic coding sample and should not be interpreted as policy importance or implementation quality.

## Data/Methods Paragraph Frame

> The Week 13 classroom dataset contains `___` coded rows from `___` source documents. The unit of analysis is one coded source entry, not one learner, school, or full policy corpus. Each row records source metadata such as `___`, and analytic fields such as `___`. Dates were parsed with `pd.to_datetime`; rows marked as access-date placeholders should be read as dynamic source checks rather than publication chronology. Therefore, the table supports a transparent source map, not a claim about implementation quality or causal policy effects.

## Stretch

Export `week13_theme_by_source_crosstab.csv` and write 3-4 sentences explaining whether your coding scheme needs a new theme or clearer theme definitions.
