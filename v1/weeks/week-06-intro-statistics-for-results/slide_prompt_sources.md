# Week 06 Slide Prompt And Source Log

## Design Prompt

Create a beginner-friendly HTML slide deck for Week 06 of a Python-for-research course. Use the Week 02/05 visual style: large type, restrained blue/green/amber/rose palette, white cards, grid background, slide overview, page number jump, and bilingual Vietnamese/English content. Avoid dense math notation; show statistics as a writing workflow.

## Content Requirements

- Start from a cleaned pre/post TCSOL dataset.
- Teach `n`, `mean`, `SD`, `SE`, and `95% CI`.
- Keep t-test as optional stretch.
- Include multiple research-track transfer examples.
- Show a Results paragraph frame.
- Avoid claims such as "proved" or "caused".

## Sources Checked

| Source | URL | Use |
|---|---|---|
| pandas GroupBy | https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html | split-apply-combine and aggregation |
| pandas SEM | https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sem.html | standard error calculation |
| SciPy t distribution | https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.t.html | `stats.t.ppf` for CI |
| SciPy paired t-test | https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html | optional stretch |
| Gardner & Altman 1986 | https://www.bmj.com/content/292/6522/746 | confidence intervals for reporting estimates |
| ASA p-value statement | https://www.tandfonline.com/doi/full/10.1080/00031305.2016.1154108 | p-value caution |
