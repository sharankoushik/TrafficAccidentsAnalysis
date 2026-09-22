# Data Sources

## Dataset
**File:** `traffic_accidents_raw.csv`
**Records:** 500
**Columns:** 13
**Geographic scope:** Cities and states across India

## Provenance
This dataset is a **synthetic / simulated dataset**, not a live extract from an official
government or law-enforcement database (e.g. it is not sourced from NCRB, MoRTH, or any state
traffic police records system). The file's own metadata shows it was generated
programmatically (creator: `openpyxl`), with no external source citation embedded in the
workbook.

**Treat this data as illustrative/demo data for analysis, dashboarding, or teaching purposes —
not as an authoritative record of real traffic accidents.** If this dataset is meant to
represent real-world accident statistics, the original source (survey, government open-data
portal, insurance records, etc.) should be identified and cited before any findings are
published or acted on.

## Structure
- One row = one accident record, identified by `Accident_ID` (format `TAxxxx`).
- Fields cover when (`Date`, `Time`), where (`City`, `State`), conditions (`Weather_Condition`,
  `Road_Condition`), what was involved (`Vehicle_Type`, `Vehicles_Involved`), outcome
  (`Accident_Severity`, `Injuries`, `Fatalities`), and the recorded cause (`Accident_Cause`).
- Full field-by-field definitions are in `data_dictionary.xlsx`.

## Known limitations
- No documented sampling method, collection window rationale, or update cadence.
- No source URL, agency, or citation accompanies the original workbook.
- Values (severity categories, causes, weather/road conditions) appear to be drawn from a
  fixed, small set of labels — consistent with generated rather than field-collected data.

## Recommended next step
Confirm the intended source and real-world validity of this data with whoever supplied the
original workbook before using it for anything beyond practice analysis.
