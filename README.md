# Python Data Visualization for Academic Research Papers

Source check: 2026-06-08

V2 clean-slate course repository for a practical graduate-level course on using Python to move from messy research data to publication-ready figures, captions, Results paragraphs, and reproducible paper packages.

This course is no longer limited to TCSOL. TCSOL, applied linguistics, translation studies, education policy, and contrastive linguistics are treated as application tracks. The core course is academic data processing, visual reasoning, figure design, interpretation, and paper-facing communication.

## Versioning

V1 is frozen and kept out of the V2 working tree.

- V1 branch: `v1-tcsol-beginner`
- V1 tag: `v1.0-tcsol-beginner`
- V1 live archive: <https://mtuann.github.io/tcsol-python-research/v1/>
- V2 root site: <https://mtuann.github.io/tcsol-python-research/>

The GitHub Pages workflow checks out the V1 branch during deployment and publishes it under `/v1/`. V2 stays clean without carrying hundreds of V1 files locally.

## Course Promise

By the end of V2, the learner should be able to:

- inspect, clean, reshape, and document research datasets;
- create analysis-ready tables from raw or semi-raw data;
- choose chart types based on data type, comparison, and research claim;
- build publication-quality figures with Python;
- critique weak, misleading, or under-explained figures;
- export figures as PNG, SVG, or PDF for papers and presentations;
- write captions, Methods notes, Results paragraphs, and limitations;
- assemble a reproducible figure package for an academic paper.

## Design Principles

1. **Data first, chart second**: every figure begins with unit of observation, source, missingness, and transformation.
2. **Multiple datasets per module**: each module uses a toy dataset, a realistic academic dataset, and a transfer dataset when possible.
3. **Figure choice is argument choice**: students compare candidate charts and justify why one chart supports the paper claim better.
4. **Static paper output is core**: interactive visualization is useful for exploration, but the final deliverable is usually a paper-ready static figure.
5. **Writing is weekly**: every module ends with a caption, Results sentence, Methods note, or limitation.

## Current V2 Structure

```text
.
├── README.md
├── index.html
├── requirements.txt
├── site/
├── modules/
├── data_bank/
├── figure_gallery/
├── paper_package/
└── resources/
```

Key planning documents:

- [`resources/V2_REDESIGN_BLUEPRINT.md`](resources/V2_REDESIGN_BLUEPRINT.md)
- [`resources/V2_MODULE_DESIGN_STANDARD.md`](resources/V2_MODULE_DESIGN_STANDARD.md)
- [`site/modules.json`](site/modules.json)

## Tool Stack

| Purpose | Core tools | Role in the course |
|---|---|---|
| Data handling | `pandas`, `numpy`, `openpyxl` | CSV/Excel import, cleaning, joins, reshaping, summary tables |
| Paper figures | `matplotlib`, `seaborn` | static figures, statistical plots, figure control, export |
| Visual grammar and interaction | `altair` | encoding, interactive exploration, HTML chart export |
| Interactive demo | `plotly` | optional interactive views for teaching and exploration |
| Statistics and uncertainty | `scipy`, `statsmodels` | confidence intervals, tests, regression, model-aware plots |
| Writing workflow | Word + Zotero, optional Quarto/Overleaf | captions, references, reproducible reports, final paper package |

Tool rule:

- Use **Seaborn** for fast exploratory/statistical visualization.
- Use **Matplotlib** when final figure control matters.
- Use **Altair** to teach visual grammar and lightweight interaction.
- Use **Plotly** only when interactivity genuinely helps exploration.
- Do not make dashboards the core; the core deliverable is a paper-quality figure package.

## V2 Module Design

Each module must include:

- learner-facing overview;
- visual lecture slides;
- runnable notebook;
- rendered notebook HTML;
- data dictionary;
- toy dataset;
- realistic academic dataset;
- figure critique;
- final figure export;
- assignment;
- rubric;
- paper-facing writing task.

Every module should follow three practice layers:

1. **Lab A: Toy data** for syntax and concept clarity.
2. **Lab B: Academic data** for realistic structure and interpretation.
3. **Lab C: Transfer data** for education policy, applied linguistics, translation studies, TCSOL, or contrastive research.

## 16-Module Syllabus

| Module | Theme | Data practice | Visualization focus | Paper-facing output |
|---|---|---|---|---|
| 01 | Research data workflow | CSV, folders, source notes, data inventory | what counts as figure-ready evidence | research question + data inventory |
| 02 | Tidy data and codebook | unit of observation, variable type, schema | table structure before plotting | codebook + dataset schema |
| 03 | Cleaning research data | missingness, duplicates, labels, type conversion | before/after data quality view | cleaning log + before/after table |
| 04 | Transforming data for analysis | filter, groupby, pivot/melt, merge | analysis table design | analysis-ready dataset |
| 05 | Figure anatomy | small clean dataset | axes, labels, legends, export size | first publication-style figure |
| 06 | Visual encoding and perception | chart redesign dataset | marks, channels, color, hierarchy | redesigned weak chart |
| 07 | Comparisons | group comparison data | bars, dot plots, slope charts, small multiples | comparison figure + caption |
| 08 | Distributions | scores, survey, demographic variables | histogram, KDE, ECDF, box/violin | distribution figure + interpretation |
| 09 | Relationships | paired or multivariable data | scatter, trend, faceting, overplotting | relationship figure + limitation |
| 10 | Time and change | country-year, policy timeline, pre/post data | line, event timeline, panel figure | longitudinal or change figure |
| 11 | Uncertainty | sample means, CI, bootstrap, regression output | error bars, bands, interval plots | uncertainty-aware Results paragraph |
| 12 | Categorical and coded text data | coding categories, crosstabs, error labels | heatmap, stacked bar, dot summary | coded-data figure/table |
| 13 | Color, annotation, accessibility | figure polish dataset | palette, direct label, typography, alt text | polished journal-style figure |
| 14 | Interactive exploration, static paper output | larger public data extract | Altair/Plotly exploration to static export | interactive view + paper figure |
| 15 | Multi-figure Results section | 2-3 linked datasets or views | panels, numbering, figure sequence | 2-3 figure Results package |
| 16 | Reproducible paper package | final cleaned data and outputs | export audit and source map | final figure package + reproducibility note |

## Data Bank Plan

V2 should practice with more data than V1. The course should build a `data_bank/` with small teaching extracts, source notes, and download scripts.

Recommended categories:

- **General academic data**: country-year indicators, population, health, development, inequality.
- **Education policy data**: UNESCO UIS, World Bank education indicators, OECD/PISA summary tables.
- **Social science data**: surveys, Likert responses, demographic comparisons, pre/post interventions.
- **Language and translation data**: learner-error coding, bilingual examples, MT quality ratings, MTPE time logs.
- **Synthetic teaching data**: small controlled datasets for demonstrating one concept without cognitive overload.

Data rules:

- Do not publish identifiable learner or participant data.
- Store only small cleaned teaching extracts when licensing allows it.
- For large or frequently updated public data, store a download script and source note instead of the full dataset.
- Every dataset needs a data dictionary: source, access date, unit of observation, row count, column count, missing-data policy, and teaching limitation.

## Figure Gallery Plan

The course should maintain a `figure_gallery/` so learners can see what good academic figures look like.

Each gallery item should include:

- final figure image;
- source notebook link;
- dataset link;
- chart type;
- research question;
- caption;
- why this chart fits the claim;
- common mistake the redesign avoids;
- export format notes.

Suggested gallery categories:

- comparison;
- distribution;
- relationship;
- time and change;
- uncertainty;
- coded text/categorical data;
- multi-panel figure;
- interactive-to-static examples.

## Final Portfolio

The final learner output should be a compact academic figure package:

- one cleaned research dataset;
- one data dictionary;
- two to three paper-quality figures;
- one caption per figure;
- one short Results section;
- one Methods data-description paragraph;
- one limitation note;
- one reproducibility checklist;
- one source/citation note.

## Assessment Model

Suggested course-level weighting:

| Category | Weight |
|---|---:|
| Weekly data labs | 25% |
| Weekly figure builds | 25% |
| Figure critique and redesign | 15% |
| Caption and paper interpretation | 15% |
| Final figure package | 20% |

Suggested module-level rubric:

| Category | Weight |
|---|---:|
| Data understanding and cleaning | 20 |
| Correct transformation for the figure | 20 |
| Visual encoding and design choice | 20 |
| Export quality and reproducibility | 15 |
| Caption and paper interpretation | 20 |
| Reflection on limitation | 5 |

Total: 100 points.

## External Course Models

These sources informed the V2 structure. They are references for course design, not copied course materials.

- [University of Washington CSE512: Data Visualization](https://courses.cs.washington.edu/courses/cse512/) emphasizes visual encoding, graphical perception, color, interaction, automated design, readings, and project work.
- [Cornell INFO 3312/5312: Data Communication](https://info3312.infosci.cornell.edu/course-syllabus.html) uses a strong prepare-practice-perform rhythm and focuses on preprocessing, mapping data to aesthetics, accessibility, critique, refinement, reproducibility, and projects.
- [George Washington DATS 2102: Data Visualization for Data Science](https://junjunyin.com/datascience/dats2102/syllabus/) requires multiple visualizations, narrative, accessibility considerations, a reproducible Jupyter notebook, and datasets/data sources.
- [Purdue CS490-VIZ: Introduction to Data Visualization](https://www.cs.purdue.edu/CS49000-VIZ/syllabus.html) combines design principles, hands-on assignments, Python/JavaScript visualization tools, and a final project based on datasets related to student interests.
- [Princeton Research Computing: Data Visualization in Python](https://picscie.princeton.edu/events/2025/data-visualization-python) frames Python visualization around Matplotlib, Seaborn, Plotly, NumPy, pandas, hands-on practice, and publication-quality plots.
- [CU Boulder DTSA 5304: Fundamentals of Data Visualization](https://experts.colorado.edu/display/coursename_DTSA-5304) is useful as a compact reference for fundamentals, task framing, and visualization workflow.

## Python Visualization References

- [Matplotlib `savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html): reference for figure export, file formats, DPI, and publication-oriented output.
- [Seaborn objects interface](https://seaborn.pydata.org/tutorial/objects_interface.html): useful for teaching modern declarative statistical plotting in Python.
- [Vega-Altair saving charts](https://altair-viz.github.io/user_guide/saving_charts.html): useful for HTML, PNG, SVG, and PDF chart export, plus interactive chart workflows.
- [Plotly static image export](https://plotly.com/python/static-image-export/): useful when converting interactive Plotly figures into paper-ready static files.

## Public Data Sources

- [UNESCO UIS Bulk Data Download](https://databrowser.uis.unesco.org/documentation/bulk): official education, science, culture, and policy-relevant datasets in CSV format; useful for education policy modules.
- [World Bank Indicators API](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392): programmatic access to thousands of time-series indicators; useful for country-year data and development comparisons.
- [Our World in Data Grapher Chart API](https://docs.owid.io/projects/etl/api/chart-api/): CSV/JSON access to chart-level datasets and metadata; useful for data wrangling and visualization practice.
- [OECD PISA](https://www.oecd.org/pisa/): international education assessment data, codebooks, questionnaires, and databases; useful for advanced education-data modules.

## Working Rule

Build V2 module by module. Do not revive the old `weeks/` structure on `main`. If V1 material is useful, copy ideas selectively from the branch archive and rewrite them for the V2 data-visualization standard.
