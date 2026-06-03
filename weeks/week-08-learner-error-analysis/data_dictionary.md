# Week 08 Data Dictionary

| Column | Type | Meaning | Week 08 Use |
|---|---|---|---|
| `response_id` | text | synthetic response identifier | row identifier |
| `learner_id` | text | synthetic learner identifier | ID only; the unit is the response row |
| `class_group` | text | class label | context variable |
| `activity_focus` | text | teaching activity category | optional grouping/context |
| `activity_label` | text | display label | figure/table label |
| `item_id` | text | prompt/item identifier | item context |
| `target_structure` | text | Chinese target structure | crosstab row |
| `prompt_vi` | text | Vietnamese prompt for learner task | example interpretation |
| `expected_answer` | text | target-like Chinese/Pinyin answer | representative example |
| `learner_answer` | text | synthetic learner response | representative example |
| `has_error` | boolean | whether the usable response contains a coded error | filter for error tables |
| `error_category` | text | human-coded error category | frequency table and crosstab |
| `error_feature` | text | plain description of the error | teaching interpretation |
| `severity` | numeric | simple 1-3 severity rating; 0 for no-error rows | teaching priority score |
| `possible_vi_transfer` | text | possible Vietnamese transfer hypothesis | discussion note, not proof |
| `correction_note` | text | short teaching note | teaching implication |
| `usable_error` | boolean | row can be analyzed | required filter |

Important: this is a synthetic teaching dataset for learning workflow, not real student data.

## Provenance

- Source role: synthetic learner-error coding dataset.
- Privacy: contains no real learner records.
- SHA-256: `a96e92a6fa3d746e77e0b6bb97a5ee01bf55f15c6690e23bac0b240feedd6fc0`
- Unit of analysis: one row, meaning one learner response to one item.
- Required filter: use rows where `usable_error == True`; count error patterns with `has_error == True`.
