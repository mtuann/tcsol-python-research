# Writing and Paper Tooling Roadmap

Last source audit: 2026-06-03

This course treats writing as a weekly research habit, not as a final-week add-on. Every week must produce a small paper-facing text: a research question, caption, Methods sentence, Results paragraph, limitation note, or source note.

Overleaf and LaTeX are useful, but they should not be introduced before the learner has enough paper material to format. The default writing workflow is Word + Zotero first; Overleaf is an optional Week 14 packaging path.

## Core Policy

1. Writing appears every week.
2. Overleaf appears only when the learner already has tables, figures, captions, and a draft structure.
3. Word + Zotero is the default early workflow because it is familiar in applied linguistics, translation studies, and education policy.
4. Quarto is introduced as a reproducible report option after notebooks and figures are comfortable.
5. Overleaf is introduced as a formatting and collaboration option, not as a new research method.

## Tool Progression

| Stage | Weeks | Writing focus | Default tool | Optional tool |
|---|---:|---|---|---|
| Foundation | 1-2 | research question, data unit, source note | Markdown in notebook | Word |
| Evidence | 3-5 | descriptive table, figure caption, figure note | notebook + exported output | Word + Zotero |
| Results | 6-8 | Results paragraph, limitation, teaching implication | Word + Zotero | Markdown |
| Track writing | 9-13 | track-specific analysis paragraph | Word + Zotero | Quarto |
| Paper package | 14 | package plan, appendix/source map, references, reproducibility note | Word + Zotero | Overleaf or Quarto |

## Weekly Writing Contract

Every weekly lesson must include these fields:

```markdown
## Writing Support

- Paper section supported:
- Writing output:
- Tool support:
- Sentence frame:
- Common writing risk:
```

Example:

```markdown
## Writing Support

- Paper section supported: Results
- Writing output: one paragraph interpreting a pre/post score table
- Tool support: write in the notebook first, then paste into Word
- Sentence frame: "Table 1 shows that..., but this pattern should be interpreted cautiously because..."
- Common writing risk: claiming causality from descriptive classroom data
```

## Week-by-Week Writing Progression

| Week | Writing output | Tool support |
|---|---|---|
| 1 | research question + 100-150 word memo | notebook Markdown |
| 2 | data description paragraph | notebook Markdown or Word |
| 3 | descriptive table caption | Word + Zotero setup begins |
| 4 | cleaning decision note | Word + source log |
| 5 | figure caption and figure note | Word + exported figure |
| 6 | Results paragraph with limitation | Word + Zotero citation |
| 7 | short teaching-study Methods draft | Word |
| 8 | learner-error Results paragraph | Word |
| 9 | contrastive example interpretation | Word + Zotero |
| 10 | pedagogical adaptation paragraph | Word |
| 11 | MT evaluation Results paragraph | Word + metric/source notes |
| 12 | MTPE workflow discussion paragraph | Word |
| 13 | policy coding Methods paragraph | Word or Quarto |
| 14 | mini paper package | Word + Zotero, optional Overleaf/Quarto |

## Overleaf Entry Point

Introduce Overleaf in Week 14 only after the learner can answer:

- What is the paper title and research question?
- Which table or figure is ready to include?
- Which references are in Zotero or a `.bib` file?
- Which sections are mapped or drafted: Introduction, Data, Methods, Results, Limitations?
- Does the target journal, conference, or university require LaTeX?

If the answer to the last question is "no", Word + Zotero remains the default. Overleaf should be presented as an optional packaging route for collaboration, LaTeX templates, and `.bib`-based references.

## Week 14 Paper Package

Week 14 should not introduce a heavy new Python skill or require a full paper draft from a beginner. It should consolidate:

- cleaned dataset or derived table;
- final notebook that runs top to bottom;
- exported table/figure;
- caption, package plan, and section map;
- source list or Zotero bibliography workflow;
- mini paper draft as stretch/future work after the package plan is approved;
- appendix or reproducibility note;
- optional Overleaf project with `main.tex`, `.bib` export, and figure/table files only when a LaTeX route is required.

## Tool Decision Guide

| Need | Recommended tool |
|---|---|
| Draft prose quickly | Word |
| Manage citations in familiar writing | Zotero + Word |
| Keep code, output, and prose together | Jupyter notebook |
| Produce reproducible report from code and text | Quarto |
| Use a LaTeX template or collaborate on LaTeX | Overleaf |
| Publish a static course page | GitHub Pages for course admin, not learner paper citation |

## Starter Source Links

- Zotero Word processor plugin: https://www.zotero.org/support/word_processor_plugin_usage
- Zotero word processor integration: https://www.zotero.org/support/word_processor_integration
- Quarto authoring in VS Code: https://quarto.org/docs/get-started/authoring/vscode.html
- Quarto citations: https://quarto.org/docs/authoring/citations.html
- Overleaf Learn LaTeX: https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes
- Overleaf bibliography management: https://www.overleaf.com/learn/latex/Bibliography_management_in_LaTeX
- Overleaf `.bib` files: https://docs.overleaf.com/citing-and-references/working-with-.bib-files
- Overleaf Zotero integration: https://docs.overleaf.com/integrations-and-add-ons/reference-manager-integrations/zotero (direct sync is premium; free route is Zotero `.bib` export/upload)
