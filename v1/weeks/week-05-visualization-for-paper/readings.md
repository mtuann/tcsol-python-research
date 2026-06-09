# Week 05 Readings

Last source audit: 2026-06-03

## Must Read in 10 Minutes

1. Matplotlib: Plot types
   - Link: https://matplotlib.org/stable/plot_types/index.html
   - What to read: only the bar chart and scatter/dot-style examples.
   - Why: quick overview of common plot types and when they are used.

2. seaborn tutorial: Visualizing categorical data
   - Link: https://seaborn.pydata.org/tutorial/categorical.html
   - What to read: only the sections that explain categorical scatterplots and bar plots.
   - Why: Week 05 uses categorical groups such as `activity_focus`.

## Required Technical Reading

1. seaborn `barplot`
   - Link: https://seaborn.pydata.org/generated/seaborn.barplot.html
   - Why: Week 05 uses a bar chart for a group mean.

2. seaborn `stripplot`
   - Link: https://seaborn.pydata.org/generated/seaborn.stripplot.html
   - Why: Week 05 uses individual points to avoid hiding small samples.

3. Matplotlib `savefig`
   - Link: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
   - Why: figures must be exported as `.png` and `.svg` for paper drafting.

## Required Research/Method Reading

1. Ten Simple Rules for Better Figures
   - Link: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833
   - Citation: Rougier, Droettboom, and Bourne (2014), PLOS Computational Biology.
   - Research question/method: practical rules for making scientific figures clearer and less misleading.
   - What we borrow: simple figure type, clear labels, careful color, and no visual exaggeration.

## Optional

- Matplotlib: Choosing colormaps: https://matplotlib.org/stable/users/explain/colors/colormaps.html
- Tidy Data: https://vita.had.co.nz/papers/tidy-data.html
- Matplotlib tutorials: https://matplotlib.org/stable/tutorials/index.html
- seaborn examples gallery: https://seaborn.pydata.org/examples/index.html
- PLOS guide collection: https://collections.plos.org/collection/ten-simple-rules/

## Source Update Log

| Search date | Search terms | Sources checked | Selected source | Reason |
|---|---|---|---|---|
| 2026-06-03 | matplotlib plot types savefig stable docs | Matplotlib official docs | Plot types, `savefig` | current official reference for chart/export functions |
| 2026-06-03 | seaborn categorical barplot stripplot docs | seaborn official docs | categorical tutorial, `barplot`, `stripplot` | current official reference for categorical visualizations |
| 2026-06-03 | better scientific figures misleading color labels | PLOS Computational Biology | Ten Simple Rules for Better Figures | research-facing figure-design guidance |
| 2026-06-03 | matplotlib colormap colorblind perceptual official | Matplotlib official docs | Choosing colormaps | supports intentional color choices |
| 2026-06-03 | tidy data visualization table structure | Journal of Statistical Software / author page | Tidy Data | optional method background for one-row-per-observation plotting |

## Reading Questions

1. When is a bar chart useful, and what can it hide?
2. Why does a dot plot help when sample size is small?
3. What should a figure caption include that does not need to be printed inside the plot?
4. Why should a paper figure avoid causal language when the data are descriptive?
