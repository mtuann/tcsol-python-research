# Week 13 Data Dictionary

| Column | Type | Meaning | Week 13 Use |
|---|---|---|---|
| `coding_id` | text | one coded row ID | unit of analysis |
| `doc_id` | text | source document ID | group repeated rows from same source |
| `title` | text | source title | citation metadata |
| `issuing_body` | text | organization or institution | source credibility/context |
| `issue_date` | date string | source publication or access-relevant date | timeline |
| `date_basis` | text | whether `issue_date` is a publication date or an access-date placeholder | timeline caution |
| `source_type` | text | policy plan, bulletin, portal, model, report | evidence context |
| `policy_level` | text | national, global, international | comparison scope |
| `policy_area` | text | coded topic area | frequency table |
| `target_group` | text | affected group/system | interpretation |
| `theme_code` | text | more specific code | codebook practice |
| `evidence_type` | text | policy text, statistical indicator, metadata, method model, report | source-note language |
| `excerpt_paraphrase` | text | short paraphrase, not a copied quotation | coding evidence |
| `indicator_or_milestone` | text | relevant milestone/indicator family | timeline/caption detail |
| `url` | text | source URL | citation/source note |
| `access_date` | date string | date source was checked | reproducibility |
| `coder_note` | text | why/how the row was coded | audit trail |

Computed in notebook:

| Computed column | Meaning |
|---|---|
| `issue_date_parsed` | datetime parsed from `issue_date` |
| `issue_year` | year extracted from parsed date |
| `source_label` | short label for timeline plotting |
