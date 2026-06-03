# Week 01 Data Dictionary

## Dataset

- File: `data/raw/week01_research_tracks.csv`
- Source: instructor-created teaching dataset.
- Access date: 2026-06-03.
- License/reuse note: may be reused for this course.
- Unit of observation: one possible research project track.
- Row count: 4 synthetic instructor-created rows.
- Missing values: none expected; blank cells are not valid in this teaching dataset.
- Private data: no private or learner-identifiable data.

## Columns

| Column | Meaning | Example |
|---|---|---|
| `track_id` | Short stable ID for the research track. | `TCSOL_SHORT` |
| `track` | Name of the research direction. | `Short-term Chinese teaching` |
| `broad_interest` | A broad topic before it becomes researchable. | `Improving short-term Chinese classes...` |
| `small_research_question` | A narrower question that can be linked to data. | `How do learner answers change...` |
| `unit_of_observation` | What one row would represent in a future dataset. | `learner test item` |
| `starter_dataset` | A future dataset template for that track. | `pre_post_scores.csv` |
| `likely_output` | A table or figure that could appear in a paper. | `pre/post score table` |
| `beginner_python_task` | A very simple Python task for that dataset type. | `count learners...` |

## Why This Dataset Exists

Week 01 uses a small planning dataset instead of real classroom or translation data. This keeps the first lesson focused on the research workflow:

```text
topic -> question -> data unit -> Python task -> paper output
```

The learner should not worry yet about advanced analysis. The important question is: "What data would I need to answer this research question?"

## Mini Data Examples

Week 01 also includes:

- File: `data/raw/week01_mini_examples.csv`
- Purpose: show what one future row of research data may look like in each track.
- Required for learner: no, instructor demo only.

| Track | Example unit | Why it matters |
|---|---|---|
| TCSOL | one learner's answer to one test item | connects classroom teaching to measurable learner output |
| Contrastive analysis | one Chinese-Vietnamese sentence pair | connects grammar comparison to teaching notes |
| MTPE | one source-MT-postedit segment | connects machine output to human post-editing and error labels |
| Policy | one coded policy excerpt or document-theme pair | connects policy text to metadata and themes |

Do not add real learner names, emails, or identifiable classroom records to Week 01 data files.
