# Module 01 Data Dictionary

Source check: 2026-06-09

## Dataset 1: `module01_toy_project_inventory.csv`

Teaching role: toy dataset for concept clarity.

Unit of observation: one possible paper project or data item.

| Column | Meaning |
|---|---|
| `project_id` | Short project identifier. |
| `paper_area` | Broad research area. |
| `paper_question` | Example question the paper might ask. |
| `data_item` | Data object needed for the question. |
| `data_role` | How the data supports the paper. |
| `unit_of_observation` | What one row would represent. |
| `format` | Expected file format. |
| `rows_expected` | Approximate row count for planning. |
| `source_owner` | Public provider, researcher, class corpus, or task platform. |
| `personal_data_risk` | Low/medium risk flag for ethics discussion. |
| `figure_candidate` | First possible figure type. |
| `readiness_note` | What must be checked before analysis. |

## Dataset 2: `module01_public_source_inventory.csv`

Teaching role: realistic academic source inventory.

Unit of observation: one candidate data source.

| Column | Meaning |
|---|---|
| `source_id` | Short source identifier used in figures. |
| `source_name` | Full source name. |
| `provider` | Organization or creator. |
| `research_track` | Track where the source is useful. |
| `access_mode` | How the learner accesses the data. |
| `format` | Likely data format. |
| `unit_of_observation` | Typical row meaning after download or extraction. |
| `typical_beginner_question` | Beginner-friendly research question. |
| `source_url` | Source or documentation URL. |
| `official_note` | Why this source is included. |
| `trust_score` | Teaching score from 1 to 5. Higher means more institutionally reliable. |
| `beginner_complexity` | Teaching score from 1 to 5. Higher means harder for a beginner. |
| `figure_candidate` | First plausible chart type. |
| `paper_risk` | Main interpretation, ethics, or citation risk. |
| `source_checked` | Date the source documentation was checked. |

Important: `trust_score`, `beginner_complexity`, and `readiness_score` are teaching heuristics. They are not formal measures of data quality.

## Dataset 3: `module01_transfer_question_bank.csv`

Teaching role: transfer dataset for applying the workflow to different domains.

Unit of observation: one research-question scenario.

| Column | Meaning |
|---|---|
| `track` | Application track. |
| `paper_question` | Example paper-facing question. |
| `needed_data` | Data needed to answer the question. |
| `unit_of_observation` | What one row should mean. |
| `first_python_action` | First operation a beginner should try. |
| `possible_chart` | Initial chart family. |
| `paper_output` | Writing product connected to the chart. |

## Output Tables

| File | Purpose |
|---|---|
| `outputs/tables/module01_data_inventory.csv` | Copy of the toy project inventory used as a paper planning artifact. |
| `outputs/tables/module01_source_readiness_summary.csv` | Ranked source inventory with computed readiness score. |
| `outputs/tables/module01_paper_question_map.csv` | Transfer question map exported from the notebook. |
| `outputs/tables/module01_caption_draft.md` | Caption draft for the readiness figure. |

## Output Figures

| File | Purpose |
|---|---|
| `outputs/figures/module01_source_readiness.png` | Raster figure for slides and web display. |
| `outputs/figures/module01_source_readiness.svg` | Vector figure for web or paper layout. |
| `outputs/figures/module01_source_readiness.pdf` | PDF figure for LaTeX/Overleaf workflows. |
| `outputs/figures/module01_workflow_map.png` | Visual workflow map for teaching. |
| `outputs/figures/module01_workflow_map.svg` | Vector workflow map. |

## Privacy and Ethics Note

The public repository uses no identifiable learner data. Any future real learner survey, learner corpus, translation task log, or classroom dataset should be anonymized and approved under the relevant institutional ethics process before publication or analysis.
