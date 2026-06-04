# Week 09 Assignment: Contrastive Analysis Table

## Submit

Submit a folder or notebook output containing:

1. `week09_phenomenon_frequency.csv`
2. `week09_pattern_by_risk.csv`
3. `week09_teaching_priority_table.csv`
4. `week09_selected_contrastive_examples.csv`
5. `week09_phenomenon_frequency.png`
6. `week09_risk_by_phenomenon_heatmap.png`
7. two figure captions;
8. one 120-170 word contrastive analysis paragraph.

## Core Steps

1. Open `weeks/week-09-chinese-vietnamese-contrastive-data/live_coding.ipynb`.
2. Run the setup cell.
3. Load `data/raw/week09_contrastive_examples.csv`.
4. Filter rows where `include_in_table == True`.
5. Use `str.contains()` to check one visible marker or pattern.
6. Export the four CSV tables and two figures.
7. Write a paragraph that includes count, one representative example, teaching implication, and limitation.

## Required Writing Move

> In the usable contrastive examples (`N = ___`), the highest-priority phenomenon was `___`. One representative example is `___`, where Chinese uses `___` while Vietnamese uses `___`. This contrast matters for teaching because `___`. Because the dataset is synthetic and small, this result should guide example selection rather than prove learner transfer.

## Stretch

Add one new row to a copy of the DataFrame, then explain the source, phenomenon label, and teaching value. Do not edit the original raw CSV for the required task.
