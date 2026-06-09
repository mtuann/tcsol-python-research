# Python Data Visualization for Academic Research Papers

V2 clean-slate course repository.

This project is being rebuilt from scratch as a practical graduate-level course on using Python for research data processing, academic visualization, figure critique, paper-ready export, captions, Results paragraphs, and reproducible paper packages.

## Versioning

V1 is frozen and kept out of the V2 working tree.

- V1 branch: `v1-tcsol-beginner`
- V1 tag: `v1.0-tcsol-beginner`
- V1 live archive: `https://mtuann.github.io/tcsol-python-research/v1/`
- V2 root site: `https://mtuann.github.io/tcsol-python-research/`

The GitHub Pages workflow checks out the V1 branch during deployment and publishes it under `/v1/`. That means V2 can stay clean without carrying hundreds of V1 files locally.

## V2 Goal

The learner should finish the course able to:

- inspect and clean research datasets;
- create analysis-ready tables;
- choose chart types based on research claims;
- build publication-quality figures with Python;
- critique weak or misleading figures;
- export figures for academic papers;
- write captions and short Results/Methods notes;
- assemble a reproducible figure package for a paper.

## Current V2 Structure

```text
.
├── README.md
├── index.html
├── requirements.txt
├── modules/
├── data_bank/
├── figure_gallery/
├── paper_package/
└── resources/
```

## Key Planning Documents

- [`resources/V2_REDESIGN_BLUEPRINT.md`](resources/V2_REDESIGN_BLUEPRINT.md)
- [`resources/V2_MODULE_DESIGN_STANDARD.md`](resources/V2_MODULE_DESIGN_STANDARD.md)

## Planned Module Sequence

| Module | Theme | Output |
|---|---|---|
| 01 | Research data workflow | research question + data inventory |
| 02 | Tidy data and codebook | codebook + dataset schema |
| 03 | Cleaning research data | cleaning log + before/after table |
| 04 | Transforming data for analysis | analysis-ready dataset |
| 05 | Figure anatomy | first publication-style figure |
| 06 | Visual encoding and perception | redesigned weak chart |
| 07 | Comparisons | comparison figure + caption |
| 08 | Distributions | distribution figure + interpretation |
| 09 | Relationships | relationship figure + limitation |
| 10 | Time and change | longitudinal or change figure |
| 11 | Uncertainty | uncertainty-aware Results paragraph |
| 12 | Categorical and coded text data | coded-data figure/table |
| 13 | Color, annotation, accessibility | polished journal-style figure |
| 14 | Interactive exploration, static paper output | interactive view + paper figure |
| 15 | Multi-figure Results section | 2-3 figure Results package |
| 16 | Reproducible paper package | final figure package + reproducibility note |

## Working Rule

Build V2 module by module. Do not revive the old `weeks/` structure on `main`. If V1 material is useful, copy ideas selectively from the branch archive and rewrite them for the V2 data-visualization standard.
