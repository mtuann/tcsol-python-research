# Week 11 Data Dictionary

| Column | Type | Meaning | Week 11 Use |
|---|---|---|---|
| `segment_id` | text | source sentence identifier | grouping and review |
| `domain` | text | education-policy topic | source description |
| `zh_source` | text | Chinese source sentence | translation input |
| `vi_reference` | text | human-written Vietnamese reference | metric comparison |
| `mt_system` | text | synthetic system label, not a commercial name | system grouping |
| `vi_mt_output` | text | Vietnamese MT output | metric hypothesis |
| `human_adequacy_1_5` | numeric | simplified human meaning score | human review comparison |
| `human_fluency_1_5` | numeric | simplified human readability score | human review comparison |
| `simplified_error_label` | text | simplified MQM-inspired label | error summary |
| `severity` | text | `none`, `minor`, or `major` | error count |
| `source_note` | text | provenance warning | limitation writing |

Important: this is a synthetic MT evaluation dataset. The system names are anonymized classroom labels and do not identify real services.

## Provenance

- Source role: synthetic Chinese-Vietnamese education-policy MT evaluation dataset.
- Privacy: contains no client text and no real learner records.
- SHA-256: `b86c4ea84fcccba42c1a6dd8e6ac4112e42e59198ceb4b6c9e98dea0c810a939`
- Unit of analysis: one row, meaning one source segment translated by one MT system.
