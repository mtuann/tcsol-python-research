# Module 03 Rubric

Total: 100 points.

| Category | Points | Strong submission |
|---|---:|---|
| Problem inspection | 15 | Identifies missing values, duplicate key, label variants, type failures, and invalid ranges. |
| Cleaning decisions | 25 | Cleans one rule at a time, preserves audit columns, and avoids unjustified filling. |
| Cleaning log | 20 | Each row states issue type, detected count, decision, affected rows, risk, and paper note. |
| Figure quality | 15 | Before/after quality figure is readable, labeled, exported, and linked to the cleaning log. |
| Methods writing | 20 | Methods note explains observation key, row exclusions, conversion rules, and limitation. |
| Reproducibility | 5 | Notebook runs from raw data to outputs without manual edits. |

## Automatic Deductions

- Minus 10 if raw files are overwritten.
- Minus 10 if missing scores are filled without justification.
- Minus 10 if duplicate logic is not tied to an observation key.
- Minus 5 if the figure has no caption or cannot be regenerated.
