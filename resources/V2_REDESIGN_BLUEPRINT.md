# V2 Redesign Blueprint: Python Data Visualization for Academic Research Papers

Source check: 2026-06-08

## Versioning Decision

V1 is frozen as the beginner TCSOL-oriented course.

- Git branch: `v1-tcsol-beginner`
- Git tag: `v1.0-tcsol-beginner`
- Static website archive: `/v1/`, generated during GitHub Pages deployment from the V1 branch.
- Frozen commit: `713cd5dad388d319086c2afe4fcd3760d7472d23`

The root website on `main` is V2. Do not keep a local `/v1/` folder on `main`. The deploy workflow checks out `v1-tcsol-beginner` separately and publishes it under `/v1/`.

## V2 Course Identity

Working title:

> Python Data Visualization for Academic Research Papers

Core promise:

> The learner moves from messy research data to publication-ready figures, tables, captions, Results paragraphs, and a reproducible paper package.

V2 is not limited to TCSOL. TCSOL, education policy, translation studies, and contrastive linguistics become application tracks. The core course is data handling, visual reasoning, figure design, paper interpretation, and reproducible research practice.

## External Course Patterns Used

These courses inform the redesign, without copying their materials:

- University of Washington CSE512: visual encoding, perception, interaction, and project-centered visualization.
- Cornell INFO 3312/5312: preprocessing, mapping data to aesthetics, accessibility, critique, and refinement.
- George Washington DATS 2102: tidy data, distributions, wrangling, perception, comparisons, labels, mapping, color, relationships, and uncertainty.
- University of Colorado DTSA 5304: task/user needs, Altair, evaluation, and honest visualization.
- Princeton Research Computing workshop: Python tooling for publication-quality plots with pandas, Matplotlib, Seaborn, and Plotly.
- Purdue CS490-VIZ: repeated programming assignments and a final dataset project.

## Recommended V2 Repository Structure

```text
tcsol-python-research-syllabus/
├── index.html                         # V2 homepage
├── README.md                          # V2 course overview
├── site/
│   ├── README.md
│   └── modules.json                   # canonical module metadata for website rendering
├── modules/                           # V2 lesson modules
│   ├── module-01-research-data-workflow/
│   ├── module-02-tidy-data-codebook/
│   └── ...
├── data_bank/
│   ├── README.md
│   ├── general_academic/
│   ├── education_policy/
│   ├── social_science/
│   └── language_translation/
├── figure_gallery/
│   ├── README.md
│   ├── comparison/
│   ├── distribution/
│   ├── relationship/
│   ├── time_change/
│   ├── uncertainty/
│   └── coded_text/
├── paper_package/
│   ├── README.md
│   ├── figure_checklist.md
│   ├── caption_templates.md
│   └── reproducibility_checklist.md
├── resources/
│   ├── V2_REDESIGN_BLUEPRINT.md
│   ├── V2_MODULE_DESIGN_STANDARD.md
│   └── ...
└── requirements.txt
```

Do not revive the old `weeks/` folder on `main`. New V2 work should use `modules/` so the conceptual shift is visible.

## V2 Module Design Standard

Each module must include:

1. `index.html`: learner-facing bilingual overview.
2. `slides.html`: visual lecture deck with table of contents and slide jump.
3. `lecture_notes.md`: instructor explanation and teaching flow.
4. `live_coding.ipynb`: runnable notebook from raw data to output.
5. `live_coding.html`: rendered notebook for GitHub Pages.
6. `interactive_demo.html`: only when interaction makes the concept clearer.
7. `data/raw/`: one toy dataset and at least one research-style dataset.
8. `data_dictionary.md`: unit of observation, column meaning, type, missingness, source.
9. `outputs/figures/`: final figure in PNG and SVG or PDF when useful.
10. `outputs/tables/`: cleaned or summary tables.
11. `figure_critique.md`: weak chart diagnosis and redesign rationale.
12. `assignment.md`: data task, figure task, caption task, paper transfer.
13. `rubric.md`: data correctness, visual reasoning, export quality, interpretation, reproducibility.
14. `readings.md`: 3-5 focused sources, with core and optional labels.

Every module must have three practice layers:

- Lab A: toy data for syntax.
- Lab B: public or semi-real academic data.
- Lab C: learner-track data for paper transfer.

## 16-Module V2 Syllabus

| Module | Theme | Python focus | Paper-facing output |
|---|---|---|---|
| 01 | Research data workflow | Jupyter, folders, CSV, Markdown | research question + data inventory |
| 02 | Tidy data and codebook | DataFrame, units, variable types | codebook + dataset schema |
| 03 | Cleaning research data | missingness, duplicates, labels, types | cleaning log + before/after table |
| 04 | Transforming data for analysis | filter, groupby, pivot/melt, merge | analysis-ready dataset |
| 05 | Figure anatomy | Matplotlib objects, savefig, DPI, formats | first publication-style figure |
| 06 | Visual encoding and perception | Seaborn, Altair basics, chart critique | redesigned weak chart |
| 07 | Comparisons | bars, dot plots, slope charts, small multiples | comparison figure + caption |
| 08 | Distributions | histogram, KDE, ECDF, box/violin | distribution figure + interpretation |
| 09 | Relationships | scatter, trend line, overplotting, faceting | relationship figure + limitation |
| 10 | Time and change | line plots, event timelines, pre/post panels | longitudinal or change figure |
| 11 | Uncertainty | CI, SE, bootstrap, error bars, bands | uncertainty-aware Results paragraph |
| 12 | Categorical and coded text data | crosstab, heatmap, stacked bars | coded-data figure/table |
| 13 | Color, annotation, accessibility | palettes, direct labels, typography | polished journal-style figure |
| 14 | Interactive exploration, static paper output | Altair/Plotly + final static export | interactive view + paper figure |
| 15 | Multi-figure Results section | panels, numbering, tables, captions | 2-3 figure Results package |
| 16 | Reproducible paper package | notebook, README, references, export audit | final figure package + reproducibility note |

## Data Bank Policy

V2 should use more data than V1. Each module should touch at least two datasets, and every 3-4 modules should add one larger public dataset.

Recommended categories:

- General academic: Gapminder-style country-year data, World Bank indicators, Our World in Data CSVs.
- Education policy: UNESCO UIS, World Bank education indicators, OECD/PISA summary tables.
- Social science: surveys, Likert responses, demographic comparisons, pre/post studies.
- Language and translation: coded learner errors, bilingual examples, MT quality ratings, MTPE time logs.

For public data, store only small cleaned teaching extracts when licensing allows it. Otherwise store a download script, source URL, and data dictionary.

## Figure Gallery Policy

Every finished module should contribute at least one figure to `figure_gallery/`.

Each gallery item should include:

- final figure image;
- source notebook link;
- dataset link;
- chart type;
- research question;
- caption;
- why this chart fits the claim;
- common mistake this figure avoids.

This makes the website feel richer and gives the learner examples to imitate when writing papers.

## Tooling Policy

Use tools according to role:

- `pandas`: data cleaning, transformation, summary tables.
- `matplotlib`: final paper figure control and export.
- `seaborn`: fast statistical visualization and exploratory figures.
- `altair`: visual grammar and interactive exploration.
- `plotly`: optional interactive website demos.
- `scipy` and `statsmodels`: simple uncertainty, tests, and models.
- `openpyxl`: Excel bridge.
- Zotero + Word: default writing and citation workflow.
- Quarto or Overleaf: optional when the paper format truly needs it.

Do not make dashboard-building the core. The main deliverable is a paper-quality figure package.

## Migration Steps

1. Freeze V1 through branch, tag, and deploy-time `/v1/` static archive.
2. Replace root homepage with V2 course identity and navigation.
3. Add `data_bank/`, `figure_gallery/`, and `paper_package/`.
4. Create Module 01 using the V2 module design standard.
5. Build modules sequentially, keeping every module data-heavy and paper-facing.
6. Keep V1 accessible through `/v1/`, but keep V2 development on `main` clean.

## V2 Quality Bar

A V2 module is not complete until a learner can:

- load data;
- inspect structure;
- clean or transform it;
- build at least two candidate figures;
- justify the better figure;
- export a publication-ready version;
- write a caption;
- write a short Results or Methods note;
- rerun the notebook from top to bottom;
- find the output from the website without opening raw Markdown or notebook JSON.
