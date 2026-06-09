# Week 04 Lecture Notes: Data Cleaning Log

## Core Idea

Week 04 turns "the CSV opened successfully" into "the CSV is ready to support a paper claim." The learner already knows the Week 03 pandas pattern. This week adds one research workflow:

1. diagnose the raw data;
2. make cleaning decisions;
3. apply those decisions with code;
4. export cleaned data;
5. write down what changed.

The core habit is not memorizing every pandas cleaning function. The core habit is keeping raw data untouched and making every cleaning decision visible.

## Raw Data vs Cleaned Data

Explain the distinction plainly:

> Raw data is the table as collected. Cleaned data is a derived table made by code. A paper can analyze cleaned data, but it should be honest about the cleaning rules.

Week 04 uses an instructor-created TCSOL score dataset with common beginner-friendly problems:

- the same label written several ways, such as `Measure Words`, `measure words`, and `measure_words`;
- missing score values written as blank cells, `NA`, `missing`, or `not recorded`;
- numeric columns stored as text;
- completed status written as `yes`, `Y`, `n`, or blank.

## Diagnose Before Cleaning

Use the first pass to ask:

- Which columns have missing values?
- Which columns should be numeric?
- Which columns have labels that should be standardized?
- Which rows are still usable for the Week 03 summary?

```python
df.isna().sum()
df["activity_focus"].value_counts(dropna=False)
df.dtypes
```

The learner should read this as a data-quality inspection, not as a test they are failing.

## Cleaning Log

A cleaning log is a small table of decisions.

| Step | Column | Problem | Decision |
|---|---|---|---|
| 1 | `activity_focus` | several spellings | map to four standard labels |
| 2 | `pre_score` | text and missing codes | convert to numeric, invalid values become missing |
| 3 | `completed` | yes/no variants | map to `yes`, `no`, or missing |

The log is useful because a future reader can see what happened between raw CSV and analysis table.

## Normalize Labels

```python
clean["activity_focus_raw"] = clean["activity_focus"]
clean["activity_focus"] = (
    clean["activity_focus"]
    .astype("string")
    .str.strip()
    .str.lower()
    .str.replace("-", " ", regex=False)
    .str.replace("_", " ", regex=False)
    .map(activity_map)
)
```

Read this as:

- keep a raw label column if the decision may need checking;
- remove accidental spaces;
- lower-case text;
- convert hyphen/underscore variants into a shared pattern;
- map variants to standard labels.

## Convert Numeric Columns

```python
score_columns = ["pre_score", "post_score", "attendance_hours", "self_confidence"]
for column in score_columns:
    clean[column] = pd.to_numeric(clean[column], errors="coerce")
```

`errors="coerce"` means invalid values become missing. This is safer than pretending `eighty` or `not recorded` is a number.

## Missing Values Are Decisions

Missing values are not automatically bad. The paper needs to say how they were handled.

In Week 04, use a conservative beginner rule:

- keep missing values as missing;
- do not invent scores;
- calculate `gain_score` only when both pre and post are present;
- report how many rows are usable for the summary.

Do not teach imputation yet.

## Export Cleaned Data

```python
clean.to_csv("weeks/week-04-data-cleaning-log/data/processed/week04_cleaned_tcsol_scores.csv", index=False)
cleaning_log.to_csv("weeks/week-04-data-cleaning-log/outputs/tables/week04_cleaning_log.csv", index=False)
```

The cleaned CSV is a derived artifact. It should not replace the raw CSV.

## Cleaning Decision Note

Use this Methods-style frame:

```text
Before analysis, labels in [columns] were standardized with a predefined mapping.
Score columns were converted to numeric values, and invalid entries were treated as missing.
The raw file was preserved, and all changes were exported in a cleaning log.
After cleaning, [N] rows had complete pre/post scores for the descriptive summary.
```

## Common Mistakes

Mistake 1: Editing the raw CSV by hand.

Fix: make a new cleaned file with code.

Mistake 2: Replacing missing scores with zero.

Fix: zero is a real score. Missing means unknown.

Mistake 3: Normalizing labels without a record.

Fix: write down the mapping rule.

Mistake 4: Claiming the cleaned dataset is "objective."

Fix: describe cleaning as documented research decisions.

## Transfer to Other Research Tracks

| Track | Messy input | Cleaning decision |
|---|---|---|
| TCSOL | activity labels and score fields | standardize labels and numeric scores |
| Contrastive analysis | grammar category variants | map examples to a codebook |
| MTPE | error labels typed inconsistently | normalize labels before counting |
| Education policy | ministry/source names and dates | standardize metadata before timeline work |

Week 04 prepares the habit needed for every later track: never count messy labels before cleaning them.
