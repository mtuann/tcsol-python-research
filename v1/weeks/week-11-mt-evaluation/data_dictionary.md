# Week 11 Data Dictionary

| Column | Type | Meaning | Week 11 Use |
|---|---|---|---|
| `segment_id` | text | source segment ID | identify repeated source rows |
| `domain` | text | topic domain | optional domain summary |
| `zh_source` | text | Chinese source sentence | source text |
| `vi_reference` | text | Vietnamese reference translation | metric reference |
| `mt_system` | text | neutral synthetic MT profile (`MT_A`, `MT_B`, `MT_C`) | grouping variable |
| `vi_mt_output` | text | Vietnamese MT output | metric hypothesis |
| `human_adequacy_1_5` | number | simplified adequacy score | human review summary |
| `human_fluency_1_5` | number | simplified fluency score | human review summary |
| `error_type` | text | simplified MQM-inspired type: `terminology`, `word_order`, `style`, `omission`, `no_error` | qualitative explanation |
| `severity` | text | `none`, `minor`, or `major` | revision-needed count |
| `review_decision` | text | `acceptable_variant`, `accept_with_minor_edit`, or `revise` | human review decision |
| `source_note` | text | provenance note | source note |

Important: `no_error` and `acceptable_variant` are not errors. They are included so the learner practices separating human labels from error counts.
