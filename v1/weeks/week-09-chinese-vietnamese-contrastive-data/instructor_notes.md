# Week 09 Instructor Notes

## Teaching Rhythm

1. Start from Week 08: an error category can suggest a contrastive hypothesis, but it does not prove transfer.
2. Show one pair: `我在学校学习汉语。` vs `Tôi học tiếng Trung ở trường.`
3. Ask what the row is: one example pair, not one learner and not one translation system.
4. Run the notebook and pause after the filter cell.
5. Make the learner explain `str.contains()` in plain language: "find rows whose text visibly contains this marker".
6. Spend time on the writing frame; the point is not the table alone, but the sentence that uses it responsibly.

## Suggested Timing

- 15 min: contrastive example as unit of analysis.
- 20 min: dataset columns and filtering.
- 20 min: `str.contains()`, frequency, crosstab.
- 20 min: representative examples.
- 20 min: figure caption and analysis paragraph.
- 15 min: assignment setup.

## Instructor Answer Key

- Raw rows: 66.
- Included rows after `include_in_table == True`: 60.
- Background/excluded rows: 6.
- Highest teaching-priority phenomenon in the current synthetic data: `result_complement`.
- Top priority details: `n = 11`, mean risk = 2.55, priority score = 28.0.
- Suggested representative example: C030 `我找到票了。` / `Tôi tìm thấy vé rồi.`

Keep these numbers out of the first learner-facing writing frame until after the learner has read the table.
