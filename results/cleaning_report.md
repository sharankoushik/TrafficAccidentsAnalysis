# Data Cleaning and Preprocessing Report

## 1. Overview

The traffic accidents dataset was cleaned and standardized using Python and pandas. The purpose of preprocessing was to improve data quality, consistency, and reliability before analysis and visualization.

**Input:** `traffic_accidents_raw.csv`  
**Output:** `traffic_accidents_cleaned.csv`

## 2. Missing Values

- The dataset was checked for missing values in every column.
- Missing-value counts were reviewed before and after preprocessing.
- No unexpected missing values remained in the validated cleaned dataset.

## 3. Duplicate Records

- Complete duplicate rows were identified using pandas `duplicated()`.
- Duplicate rows were removed using `drop_duplicates()`.
- `Accident_ID` was separately checked for duplicate identifiers.
- Duplicate Accident IDs were removed while retaining the first occurrence.

## 4. Standardization

The following standardization steps were performed:

- Leading and trailing whitespace was removed from text/categorical columns.
- **Date** values were parsed and standardized to `YYYY-MM-DD`.
- **Time** values were parsed and standardized to 24-hour `HH:MM` format.
- **Vehicles_Involved**, **Injuries**, and **Fatalities** were converted to numeric data types.
- Invalid date/time or numeric values were identified during validation.

## 5. Invalid Values and Validation

- Numeric accident-count fields were checked for negative values.
- Date and time columns were revalidated after conversion.
- Final checks confirmed that duplicate Accident IDs and invalid values were not present in the validated cleaned dataset.

## 6. Columns Removed

No original analytical columns were intentionally removed from the dataset. The preprocessing focused on cleaning and standardizing the existing fields rather than reducing the feature set.

The raw CSV also contained a Git merge-conflict marker (`<<<<<<< HEAD`) before the header. This non-data artifact was removed before parsing and was not retained as a dataset column.

## 7. Final Dataset

The cleaned dataset contains **500 rows and 13 columns**, with Accident IDs ranging from **TA1001 to TA1500**.

The cleaned file is saved as:

`traffic_accidents_cleaned.csv`

## 8. Conclusion

The preprocessing workflow produced a consistent and analysis-ready traffic accident dataset by handling missing values, duplicates, formatting inconsistencies, invalid values, and the raw-file merge-conflict artifact. The cleaned dataset can now be used for exploratory data analysis and visualization.
