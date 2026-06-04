# Week 14 Lecture Notes

## Big Idea

A paper package is the set of files and decisions that make a draft believable: question, dataset, code, outputs, captions, source notes, references, and a route for writing. Week 14 is not about learning more code; it is about using code to prevent forgotten pieces.

## Concept 1: Package Before Formatting

A formatted document is not automatically a paper. Before opening Overleaf or choosing a Word template, the learner should know:

1. the paper question;
2. the dataset and unit of analysis;
3. the key table or figure;
4. the source/citation method;
5. the limitation;
6. which missing pieces remain.

## Concept 2: Word + Zotero Is The Default

For a beginner in applied linguistics or education policy, Word + Zotero is the least disruptive first route. Zotero manages citations and bibliography. Word lets the learner focus on argument and prose.

Use Overleaf only when a target template requires LaTeX, a collaborator uses LaTeX, or the learner is ready to manage `.tex`, `.bib`, and figure/table paths.

## Concept 3: Quarto Is A Reproducible Report Route

Quarto can combine Markdown, code, figures, tables, and citations. It is useful when the learner wants the paper draft to stay close to the notebook. It is optional because it adds another syntax layer.

## Tiny Worked Example

```python
from pathlib import Path
import pandas as pd

inventory = pd.read_csv("week14_paper_package_inventory.csv")
inventory["file_exists"] = inventory["source_path"].apply(lambda p: Path(p).exists())
missing = inventory[(inventory["required_core"] == "yes") & (~inventory["file_exists"])]
```

This does not judge paper quality. It only tells the learner which files are missing or need attention.

## Common Mistakes

- Opening Overleaf before references and figures are ready.
- Treating a notebook as final paper prose.
- Forgetting access dates for web sources.
- Submitting a figure without caption, N, or limitation.
- Keeping data/output paths only in memory instead of writing a package README.

## Debugging Signs

- `file_exists` is false for an artifact the learner thinks is ready.
- A citation has no organization/author or URL.
- A table exists but has no paragraph explaining what it means.
- The chosen tool route does not match the target: Word for a LaTeX-only template, or Overleaf for a simple class paper.

## Paper Package Logic

1. Select one research track.
2. Choose one main evidence output.
3. Write a mini paper skeleton.
4. Attach citation/source workflow.
5. Write reproducibility note.
6. Decide whether Word, Quarto, or Overleaf is appropriate.
