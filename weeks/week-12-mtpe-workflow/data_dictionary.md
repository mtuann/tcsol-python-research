# Week 12 Data Dictionary

| Column | Type | Meaning | Week 12 Use |
|---|---|---|---|
| `segment_id` | text | source segment ID | identify repeated source rows |
| `domain` | text | topic domain | optional domain summary |
| `zh_source` | text | Chinese source sentence | source text |
| `vi_reference` | text | Vietnamese reference translation | comparison anchor, not the main MTPE target |
| `mt_system` | text | neutral synthetic MT profile (`MT_A`, `MT_B`, `MT_C`) | grouping variable |
| `vi_mt_output` | text | Vietnamese MT output before editing | input to edit distance |
| `vi_postedit` | text | Vietnamese post-edited text | output after human editing |
| `pe_time_seconds` | integer | synthetic post-editing time | effort measure |
| `revision_type` | text | `no_error`, `style`, `terminology`, `word_order`, or `omission` | reason for editing |
| `severity` | text | `none`, `minor`, or `major` | revision-needed count |
| `review_decision` | text | `accept`, `minor_edit`, or `major_revision` | workflow decision |
| `post_editor_note` | text | short note explaining edit | qualitative evidence |
| `source_note` | text | provenance note | source note |

Computed in notebook:

| Computed column | Meaning |
|---|---|
| `char_edit_distance` | Levenshtein character edits between `vi_mt_output` and `vi_postedit` |
| `normalized_edit_distance` | edit distance divided by the longer text length |
| `revision_needed` | `True` when severity is not `none` |
