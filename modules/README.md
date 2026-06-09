# V2 Modules

V2 modules are the new teaching units for **Python Data Visualization for Academic Research Papers**.

The old V1 lessons are preserved in branch `v1-tcsol-beginner` and published at `/v1/` during deployment. New development should happen here.

## Planned Modules

| Module | Theme | Status |
|---|---|---|
| 01 | [Research data workflow](module-01-research-data-workflow/) | available |
| 02 | [Tidy data and codebook](module-02-tidy-data-codebook/) | available |
| 03 | [Cleaning research data](module-03-cleaning-research-data/) | available |
| 04 | Transforming data for analysis | planned |
| 05 | Figure anatomy | planned |
| 06 | Visual encoding and perception | planned |
| 07 | Comparisons | planned |
| 08 | Distributions | planned |
| 09 | Relationships | planned |
| 10 | Time and change | planned |
| 11 | Uncertainty | planned |
| 12 | Categorical and coded text data | planned |
| 13 | Color, annotation, accessibility | planned |
| 14 | Interactive exploration, static paper output | planned |
| 15 | Multi-figure Results section | planned |
| 16 | Reproducible paper package | planned |

## Required Module Files

Each completed module should include:

- `index.html`
- `slides.html`
- `lecture_notes.md`
- `live_coding.ipynb`
- `live_coding.html`
- `materials.html`
- `data/raw/`
- `data_dictionary.md`
- `outputs/figures/`
- `outputs/tables/`
- `figure_critique.md`
- `assignment.md`
- `rubric.md`
- `readings.md`

See [`../resources/V2_REDESIGN_BLUEPRINT.md`](../resources/V2_REDESIGN_BLUEPRINT.md).

## Template

Start new modules by copying [`_template/`](_template/) and then filling in the module-specific dataset, notebook, figures, assignment, and readings.

The template uses shared assets:

- [`../assets/course.css`](../assets/course.css)
- [`../assets/slides.css`](../assets/slides.css)
- [`../assets/module.js`](../assets/module.js)
- [`../assets/slides.js`](../assets/slides.js)
