# Week 04 Readings

Last source audit: 2026-06-03

## Must Read in 10 Minutes

1. pandas API Reference: `to_numeric`
   - Link: https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html
   - Why: Week 04 uses `errors="coerce"` to turn invalid score text into missing values.

2. pandas User Guide: Working with missing data
   - Link: https://pandas.pydata.org/docs/user_guide/missing_data.html
   - Why: explains why missing values should be detected before analysis.

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

## Required Research/Method Reading

1. Initial data analysis for longitudinal studies to build a solid foundation for reproducible analysis
   - Link: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0295726
   - Citation: Eekhout et al. (2024), PLOS ONE.
   - Research question/method: how initial data analysis can support longitudinal research before formal modeling.
   - What we borrow: document screening and cleaning decisions before interpreting results.

2. A Checklist for Analyzing Data
   - Link: https://doi.org/10.1016/j.jclinepi.2020.07.026
   - Citation: Jager et al. (2020), Journal of Clinical Epidemiology.
   - Research question/method: what practical checks help analysts avoid common data-analysis errors.
   - What we borrow: treat data checks as part of the analysis workflow.

3. Tidy Data
   - Link: https://vita.had.co.nz/papers/tidy-data.html
   - Citation: Wickham (2014), Journal of Statistical Software.
   - Research question/method: how table structure supports consistent analysis tools.
   - What we borrow: keep variables in columns and observations in rows before summarizing.

## Source Update Log

| Search date | Search terms | Sources checked | Selected source | Reason |
|---|---|---|---|---|
| 2026-06-03 | pandas missing data to_numeric text cleaning | pandas official docs | pandas missing data, text data, `to_numeric` | official technical reference for notebook functions |
| 2026-06-03 | reproducible data cleaning initial data analysis | PLOS ONE, Journal of Clinical Epidemiology | Eekhout et al. (2024), Jager et al. (2020) | supports documenting early data checks before analysis |
| 2026-06-03 | tidy data paper rows columns variables | Journal of Statistical Software / author page | Wickham (2014) | connects cleaned data structure to analysis-ready tables |

## Optional

- pandas `DataFrame.replace`: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html
- pandas `Series.map`: https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html
- JupyterLab User Guide: https://jupyterlab.readthedocs.io/en/stable/user/

## Reading Questions

1. Why is missing not the same as zero?
2. Why should raw data and cleaned data be separate files?
3. What is the difference between normalizing a label and changing a result?
4. Which cleaning decisions should be mentioned in a Methods section?
