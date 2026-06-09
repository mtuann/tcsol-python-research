# V2 Module Design Standard

Every V2 module must teach one visualization or data-processing capability through repeated academic practice.

Canonical implemented example: [`../modules/module-01-research-data-workflow/`](../modules/module-01-research-data-workflow/).

## Required Learning Arc

1. **Research task**: What paper claim could this module support?
2. **Data unit**: What does one row mean?
3. **Data check**: What can go wrong before plotting?
4. **Transformation**: What table does the figure actually need?
5. **Chart candidates**: What are two plausible chart choices?
6. **Design decision**: Why is one chart better for the claim?
7. **Final export**: How should the figure be saved for a paper?
8. **Caption and interpretation**: What can be claimed, and what cannot?
9. **Reproducibility**: Can the notebook recreate the output?

## Required Practice Layers

Each module needs three layers of practice:

- **Lab A: Toy data** for syntax and concept clarity.
- **Lab B: Academic data** for realistic structure and interpretation.
- **Lab C: Track transfer** for education policy, applied linguistics, TCSOL, contrastive linguistics, or translation studies.

## Required Web Experience

Each completed module should provide HTML-first learning paths so GitHub Pages users do not land on raw Markdown unless they choose to.

- `index.html`: learner overview with VI/EN switch, module links, dataset links, output preview, and paper-facing goal.
- `slides.html`: visual lecture deck with Home, Module, TOC, Previous/Next, slide-number jump, and keyboard navigation.
- `live_coding.html`: readable rendered notebook page that explains the code/output flow.
- `interactive_demo.html`: include only when interaction helps exploration or teaching; otherwise omit.
- `materials.html`: render assignment, rubric, and readings on the web; link to Markdown as editable source, not as the primary learner path.
- Markdown files remain the durable source notes, assignment, rubric, readings, and data dictionary.

## Required Files

```text
module-xx-topic/
├── index.html
├── slides.html
├── lecture_notes.md
├── live_coding.ipynb
├── live_coding.html
├── interactive_demo.html          # only when useful
├── data/
│   └── raw/
├── data_dictionary.md
├── outputs/
│   ├── figures/
│   └── tables/
├── figure_critique.md
├── assignment.md
├── rubric.md
└── readings.md
```

## Required Assignment Parts

Each assignment should require:

- inspect a dataset;
- clean or transform at least one column;
- create at least two candidate figures;
- choose and justify one final figure;
- export the final figure;
- write a caption;
- write a short Methods or Results note;
- submit the notebook and output files.

## Figure Quality Checklist

A final figure should:

- answer one clear research question;
- use a chart type that matches the data type and comparison;
- avoid misleading axes or unnecessary 3D effects;
- use readable labels and direct annotation where useful;
- use color for meaning, not decoration;
- remain interpretable in grayscale when possible;
- export cleanly for paper use;
- include a caption that states data source, sample, measure, pattern, and limitation.

## Minimum Rubric Categories

| Category | Suggested weight |
|---|---:|
| Data understanding and cleaning | 20 |
| Correct transformation for the figure | 20 |
| Visual encoding and design choice | 20 |
| Export quality and reproducibility | 15 |
| Caption and paper interpretation | 20 |
| Reflection on limitation | 5 |

Total: 100 points.
