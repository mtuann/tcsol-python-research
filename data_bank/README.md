# V2 Data Bank

This folder stores or documents datasets used in V2 modules.

V2 should practice with more data than V1. Each module should use:

- one toy dataset for syntax;
- one realistic academic dataset;
- one learner-track transfer dataset when possible.

## Dataset Categories

- `general_academic/`: country-year, health, economy, demographic, or public indicator data.
- `education_policy/`: UNESCO UIS, World Bank education indicators, OECD/PISA-style tables.
- `social_science/`: survey, Likert, demographic, pre/post, or intervention data.
- `language_translation/`: learner errors, bilingual examples, MT quality ratings, MTPE logs.

## Data Rules

- Do not publish identifiable learner or participant data.
- Prefer small cleaned teaching extracts when licensing allows it.
- When full public data is large or frequently updated, store a download script and source note instead of the data itself.
- Every dataset needs a data dictionary before it is used in a module.
- Keep raw data separate from cleaned teaching outputs.

## Minimum Dataset Metadata

Each dataset should document:

- source name and URL;
- access date;
- license or usage note;
- unit of observation;
- row count and column count;
- missing-data policy;
- known teaching limitations.
