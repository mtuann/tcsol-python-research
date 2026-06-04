# Week 14 Data Dictionary

## `week14_paper_package_inventory.csv`

| Column | Type | Meaning | Week 14 Use |
|---|---|---|---|
| `artifact_id` | text | short package item ID | row label |
| `paper_area` | text | package area such as Data, Figure, References | grouping variable |
| `artifact_name` | text | human-readable item name | audit table |
| `source_week` | text | course week where item comes from | traceability |
| `source_path` | text | expected file path | `Path.exists()` check |
| `default_tool` | text | likely writing/tool route | tool choice |
| `required_core` | yes/no | whether item is core for the final mini paper | missing-action filter |
| `status` | text | ready, revise, missing | readiness figure |
| `quality_check` | text | what makes the artifact acceptable | assignment checklist |
| `learner_action` | text | next action for the learner | missing-action table |
| `notes` | text | caution or teaching note | interpretation |

## `week14_reference_checklist.csv`

| Column | Type | Meaning | Week 14 Use |
|---|---|---|---|
| `source_id` | text | source row ID | row label |
| `source_title` | text | source title | reference list |
| `source_type` | text | official technical doc, method protocol, etc. | source note |
| `where_used` | text | where the source supports the paper/package | citation decision |
| `required_metadata` | text | metadata fields to check | Zotero check |
| `zotero_status` | text | add_to_zotero, optional_bib, etc. | reference workflow |
| `bibtex_key` | text | suggested `.bib` key | Quarto/Overleaf option |
| `citation_risk` | text | low/medium/high citation risk | caution |
| `next_action` | text | what the learner should do next | assignment checklist |

Computed in notebook:

| Computed column/table | Meaning |
|---|---|
| `file_exists` | whether `source_path` exists in the repo/workspace |
| `needs_action` | core item is missing, not ready, or path does not exist |
| `week14_package_audit.csv` | full inventory with audit columns |
| `week14_missing_actions.csv` | core items that need action before submission |
| `week14_reference_status.csv` | reference status summary |
