# Week 14: Paper Package, Zotero, And Optional Overleaf

Week 14 consolidates the course into a small paper package. The learner does not learn a heavy new Python topic. Instead, Python becomes a checklist auditor: it helps inspect which question, data, output, figure, source note, reference, and draft pieces are ready to move into a mini paper.

## Research Frame

- Research area: final paper packaging across TCSOL, Chinese-Vietnamese contrastive research, MT/MTPE, and education policy.
- Small research question: Which pieces of evidence are ready for a mini paper, and which writing tool route fits the target submission?
- Why this matters: a paper fails more often from missing source notes, unclear files, or weak section structure than from missing advanced code.
- Unit of analysis: one paper-package artifact or checklist item.
- Dataset: a 17-row starter package inventory and a 9-row reference checklist for the course outputs.
- Core learner output: package audit table, missing-action table, tool-decision table, readiness figure, source/reproducibility note, and one 180-220 word mini paper package plan.
- Stretch output: optional Quarto or Overleaf skeleton with `.bib` export notes when the route truly needs them.

## Python Skill

- Main skill: audit a research folder with `pandas` and `Path.exists()`.
- Supporting skills: boolean filters, `value_counts()`, `groupby()`, simple bar figures, Markdown export.
- Functions/libraries: `pathlib`, `pandas`, `matplotlib`.

## Writing Support

- Paper section supported: whole-paper package, reference list, appendix, reproducibility note.
- Writing output: one 180-220 word mini paper package plan plus a source/reproducibility note.
- Tool support: Word + Zotero by default; Quarto or Overleaf only if the learner needs a reproducible report, LaTeX template, collaborator requirement, or `.bib` workflow.
- Sentence frame: "My mini paper will use `___` as the main question, `___` as the dataset, `___` as the key table/figure, and `___` as the writing route. The package is not complete until `___` is fixed."
- Common writing risk: spending time formatting in Overleaf before the research question, figure, references, and source note are ready.

## Learning Objectives

By the end of this week, the learner can:

1. identify what belongs in a paper package: question, data, code, table/figure, writing, references, and reproducibility note;
2. run a simple Python audit to find ready, revise, and missing artifacts;
3. choose Word + Zotero, Quarto, or Overleaf based on the submission need;
4. write a short package plan that names missing work honestly;
5. prepare a minimal file map for future paper writing.

## Required Outputs

- [ ] Notebook runs from top to bottom.
- [ ] `week14_package_audit.csv` is exported.
- [ ] `week14_missing_actions.csv` is exported.
- [ ] `week14_tool_decision_table.csv` is exported.
- [ ] `week14_reference_status.csv` is exported.
- [ ] `week14_reference_checklist_review.csv` is exported.
- [ ] `week14_package_readiness.png` is exported.
- [ ] `week14_submission_plan.md` contains a learner-specific 180-220 word mini paper package plan.
- [ ] The learner chooses one route, with Word + Zotero as the default unless Quarto/Overleaf has a concrete submission reason.
- [ ] The learner writes one reproducibility note: where data, notebook, outputs, and references live.

## Files

- Slides: `slides.html`
- Interactive demo: `interactive_demo.html`
- Lecture notes: `lecture_notes.md`
- Notebook: `live_coding.ipynb` and `live_coding.html`
- Exercises: `exercises.md`
- Assignment: `assignment.md`
- Data dictionary: `data_dictionary.md`
- Rubric: `rubric.md`
- Glossary: `glossary_week14.csv`
- Translation QA: `translation_qa.md`
- Paper package QA: `paper_package_qa.md`

## Data Provenance

- File: `data/raw/week14_paper_package_inventory.csv`
- Type: synthetic course-package inventory derived from public course artifacts.
- SHA-256: `bfcbb6e657bd8bd1b961dde13ec1c632b8f0ed135cf71e4716b511d9b1b1d97e`
- File: `data/raw/week14_reference_checklist.csv`
- Type: synthetic citation/source checklist based on official documentation and method sources.
- SHA-256: `d964e61a560cb1fe585e5e0c77491891c62f3b2a097f3e6f9d1e5fa98d90c6b1`
- Copyright note: the data describes course artifacts and source metadata; it does not contain private learner data.
