import pandas as pd
from pathlib import Path


# ---------------------------------------------------------
# 1. File paths
# ---------------------------------------------------------

INPUT_FILE = Path("traffic_accidents_raw.csv")
OUTPUT_FILE = Path("traffic_accidents_cleaned.csv")


# ---------------------------------------------------------
# 2. Load the raw dataset
# ---------------------------------------------------------

df = pd.read_csv(INPUT_FILE)

print("Raw dataset loaded successfully.")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")


# ---------------------------------------------------------
# 3. Remove completely duplicated rows
# ---------------------------------------------------------

duplicate_rows = df.duplicated().sum()

print(f"\nDuplicate rows found: {duplicate_rows}")

df = df.drop_duplicates()


# ---------------------------------------------------------
# 4. Remove duplicate Accident IDs
# ---------------------------------------------------------

duplicate_ids = df["Accident_ID"].duplicated().sum()

print(f"Duplicate Accident IDs found: {duplicate_ids}")

df = df.drop_duplicates(subset="Accident_ID", keep="first")


# ---------------------------------------------------------
# 5. Clean text columns
# ---------------------------------------------------------

text_columns = [
    "Accident_ID",
    "City",
    "State",
    "Accident_Severity",
    "Weather_Condition",
    "Road_Condition",
    "Vehicle_Type",
    "Accident_Cause"
]

for column in text_columns:
    df[column] = df[column].astype(str).str.strip()


# ---------------------------------------------------------
# 6. Standardize Date
# ---------------------------------------------------------

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

invalid_dates = df["Date"].isna().sum()

print(f"Invalid dates found: {invalid_dates}")


# ---------------------------------------------------------
# 7. Standardize Time
# ---------------------------------------------------------

df["Time"] = pd.to_datetime(
    df["Time"],
    format="%H:%M",
    errors="coerce"
).dt.strftime("%H:%M")

invalid_times = df["Time"].isna().sum()

print(f"Invalid times found: {invalid_times}")


# ---------------------------------------------------------
# 8. Validate numerical columns
# ---------------------------------------------------------

numeric_columns = [
    "Vehicles_Involved",
    "Injuries",
    "Fatalities"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# ---------------------------------------------------------
# 9. Check for negative numerical values
# ---------------------------------------------------------

for column in numeric_columns:

    negative_values = (df[column] < 0).sum()

    print(
        f"Negative values in {column}: "
        f"{negative_values}"
    )


# ---------------------------------------------------------
# 10. Format Date consistently
# ---------------------------------------------------------

df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")


# ---------------------------------------------------------
# 11. Save cleaned dataset
# ---------------------------------------------------------

df.to_csv(
    OUTPUT_FILE,
    index=False
)


# ---------------------------------------------------------
# 12. Final dataset information
# ---------------------------------------------------------

print("\nCleaning completed successfully.")

print(f"Final rows: {df.shape[0]}")
print(f"Final columns: {df.shape[1]}")

print(f"\nCleaned dataset saved as:")
print(OUTPUT_FILE)