# Week 09 Data Dictionary

| Column | Type | Meaning | Week 09 Use |
|---|---|---|---|
| `example_id` | text | synthetic example identifier | row identifier |
| `teaching_track` | text | broad use case for the example | context variable |
| `phenomenon` | text | contrastive phenomenon code | frequency table and priority table |
| `chinese_example` | text | Chinese sentence, phrase, or pair | visible evidence |
| `pinyin` | text | pinyin or pronunciation note | learner support |
| `vietnamese_rendering` | text | Vietnamese rendering/equivalent | contrastive comparison |
| `literal_gloss` | text | simple English gloss | helps non-specialist reading |
| `focus_token_zh` | text | Chinese marker or focus form | example interpretation |
| `focus_token_vi` | text | Vietnamese focus rendering | example interpretation |
| `chinese_pattern` | text | simplified Chinese pattern label | Methods/data description |
| `vietnamese_pattern` | text | simplified Vietnamese pattern label | Methods/data description |
| `similarity_level` | text | similar, partial, different, or background | caution for interpretation |
| `teaching_risk` | text | low, medium, high, or exclude; teacher-assigned priority heuristic, not measured learner difficulty | crosstab columns |
| `risk_score` | nullable numeric | 1 low, 2 medium, 3 high; blank for excluded rows | priority score |
| `learner_error_link` | text | Week 08 category this may connect to | cross-week bridge |
| `evidence_note` | text | short analytic/teaching note | paragraph evidence |
| `source_type` | text | synthetic teaching example or background note | provenance note |
| `include_in_table` | boolean | whether row belongs in main table | required filter |

Important: this is a synthetic teaching dataset for learning workflow, not a corpus and not real learner data.

## Provenance

- Source role: synthetic Chinese-Vietnamese contrastive example dataset.
- Privacy: contains no real learner records.
- SHA-256: `b80e88ea2cfa12e88cab9198a5aafa22aca669264d8683098c3935e0c55f9686`
- Unit of analysis: one row, meaning one contrastive example pair.
- Required filter: use rows where `include_in_table == True`; excluded rows are kept only to teach filtering and documentation.
