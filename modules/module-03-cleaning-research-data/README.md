# Module 03 - Cleaning Research Data

Default language on the website is Vietnamese; English is available through the language toggle.

## Goal

This module teaches the learner to turn a messy research dataset into a clean, auditable, figure-ready dataset. The lesson is intentionally beginner-friendly: the code uses a few pandas commands, but every command is tied to an academic decision.

Core question:

> How can messy data make a figure say the wrong thing?

## What Learners Build

- a cleaned learner-survey dataset;
- a cleaning log that explains every decision;
- a before/after data-quality figure;
- a label-normalization map;
- a short Methods note suitable for a research paper draft.

## Files

| File | Purpose |
|---|---|
| `index.html` | learner-facing module page |
| `slides.html` | visual lecture slides with TOC and slide jump |
| `interactive_demo.html` | cleaning-log explorer |
| `live_coding.ipynb` | runnable notebook |
| `live_coding.html` | rendered notebook for GitHub Pages |
| `materials.html` | rendered assignment, rubric, and readings |
| `lecture_notes.md` | instructor notes |
| `data_dictionary.md` | variables, sources, and cleaning policy |
| `figure_critique.md` | guided critique of misleading dirty-data figures |
| `assignment.md` | learner task |
| `rubric.md` | grading criteria |
| `readings.md` | current documentation and conceptual readings |

## Datasets

| Dataset | Unit of observation | Teaching use |
|---|---|---|
| `module03_messy_learner_survey.csv` | one learner activity record before duplicate-key cleaning | missing values, duplicate keys, label variants, invalid ranges |
| `module03_messy_education_indicators.csv` | one country-year-school-level record | country labels, percent strings, missing year, missing indicator values |
| `module03_transfer_cleaning_bank.csv` | one transfer cleaning scenario | apply cleaning logic to education policy, TCSOL, contrastive linguistics, translation studies |

## Teaching Emphasis

Cleaning is not cosmetic. A cleaning decision changes what evidence can be shown in a figure.

The learner should be able to explain:

- which observation key defines a duplicate;
- why missing values should not be silently filled;
- why label variants can split one group into several bars;
- why `errors="coerce"` must be followed by an audit;
- how to write a Methods sentence that does not overclaim.
