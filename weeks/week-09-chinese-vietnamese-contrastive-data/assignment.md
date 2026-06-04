# Week 09 Assignment: Contrastive Analysis Table

## Submit

Submit a folder or notebook output containing:

1. the completed notebook or rendered notebook output;
2. one visible marker check result;
3. one filter/method note;
4. two figure captions in a notebook Markdown cell or `captions.md`;
5. one 120-170 word contrastive analysis paragraph.

The notebook can generate these files for reference: `week09_phenomenon_frequency.csv`, `week09_pattern_by_risk.csv`, `week09_teaching_priority_table.csv`, `week09_selected_contrastive_examples.csv`, `week09_phenomenon_frequency.png`, and `week09_risk_by_phenomenon_heatmap.png`.

## Core Steps

1. Open `weeks/week-09-chinese-vietnamese-contrastive-data/live_coding.ipynb` from the repository root, or use the Colab link on the website.
2. Run the setup cell.
3. Load `data/raw/week09_contrastive_examples.csv`.
4. Filter rows where `include_in_table == True`.
5. Use `str.contains()` to check one visible marker or pattern.
6. Export the four CSV tables and two figures.
7. Write a paragraph that includes count, one representative example, teaching implication, and limitation.
8. Add a one-sentence filter/method note: `66 raw rows; ___ included; ___ background/excluded rows removed because include_in_table == False.`

## Required Writing Move

> In the usable contrastive examples (`N = ___`), the highest-priority phenomenon was `___`. One representative example is `___`, where Chinese uses `___` while Vietnamese uses `___`. This contrast matters for teaching because `___`. Because the dataset is synthetic and small, this result should guide example selection rather than prove learner transfer.

## Caption Templates

Figure 1:

> Figure 1 shows the frequency of contrastive phenomena in the usable Week 09 synthetic example bank (`N = ___`). The figure is descriptive and should be used to select teaching examples, not to estimate population-level difficulty.

Figure 2:

> Figure 2 cross-tabulates phenomenon by teacher-assigned risk label in the usable Week 09 synthetic example bank (`N = ___`). The heatmap shows which examples may need more explicit explanation, but it does not measure actual learner errors.

## Stretch

Add one new row to a copy of the DataFrame, then explain the source, phenomenon label, and teaching value. Do not edit the original raw CSV for the required task.
