# Module 03 Readings

Source check: 2026-06-09.

## Required

1. pandas User Guide: Working with missing data  
   <https://pandas.pydata.org/docs/user_guide/missing_data.html>  
   Focus: how pandas represents missing values and why `NA` handling affects data types.

2. pandas API: `DataFrame.duplicated`  
   <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html>  
   Focus: duplicate detection can use a subset of columns, which is essential for observation keys.

3. pandas API: `DataFrame.drop_duplicates`  
   <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html>  
   Focus: removing duplicates should follow a documented key and `keep` decision.

4. pandas API: `to_numeric`  
   <https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html>  
   Focus: `errors="coerce"` converts failed numeric parsing into missing values; this requires an audit.

5. pandas API: `to_datetime`  
   <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html>  
   Focus: invalid date parsing can become `NaT`; date cleaning matters before timeline figures.

## Recommended

6. pandas string methods: `Series.str.strip` and `Series.str.lower`  
   <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.strip.html>  
   <https://pandas.pydata.org/docs/reference/api/pandas.Series.str.lower.html>  
   Focus: label normalization is usually string cleaning plus a documented map.

7. Wickham, H. (2014). Tidy Data. *Journal of Statistical Software*.  
   <https://www.jstatsoft.org/article/view/v059i10>  
   Focus: data cleaning and data structure are connected; messy data makes analysis harder.

## Instructor Note

The learner does not need to memorize every pandas option. They need to know which function to search for and what research decision the function supports:

- `isna()` answers "what is missing?";
- `duplicated(subset=...)` answers "what repeats under my observation key?";
- `.str.strip().str.lower()` helps with label consistency;
- `to_numeric(..., errors="coerce")` and `to_datetime(..., errors="coerce")` reveal failed conversions.
