# Week 04 Readings

Last source audit: 2026-06-03

## Required Technical Reading

1. pandas User Guide: Working with missing data
   - Link: https://pandas.pydata.org/docs/user_guide/missing_data.html
   - Why: explains missing values and beginner tools such as `isna`, `dropna`, `fillna`, and `replace`.

2. pandas User Guide: Working with text data
   - Link: https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html
   - Why: official source for string cleaning patterns such as `str.strip`, `str.lower`, and replacing text patterns.

3. pandas API Reference: `to_numeric`
   - Link: https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html
   - Why: Week 04 uses `errors="coerce"` to turn invalid score text into missing values.

## Required Research/Writing Reading

1. Initial data analysis for longitudinal studies to build a solid foundation for reproducible analysis
   - Link: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0295726
   - Why: useful framing for cleaning, screening, and documenting early data work before formal analysis.

2. A Checklist for Analyzing Data
   - Link: https://doi.org/10.1016/j.jclinepi.2020.07.026
   - Why: supports the idea that checking and understanding data is part of analysis, not an optional cleanup chore.

3. Tidy Data
   - Link: https://vita.had.co.nz/papers/tidy-data.html
   - Why: reinforces that rows, columns, and values should be organized consistently before analysis.

## Optional

- pandas `DataFrame.replace`: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html
- pandas `Series.map`: https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html
- JupyterLab User Guide: https://jupyterlab.readthedocs.io/en/stable/user/

## Reading Questions

1. Why is missing not the same as zero?
2. Why should raw data and cleaned data be separate files?
3. What is the difference between normalizing a label and changing a result?
4. Which cleaning decisions should be mentioned in a Methods section?
