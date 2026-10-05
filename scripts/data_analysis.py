"""
Traffic Accidents Analysis
Reads traffic_accidents_cleaned.csv and produces analysis_results.csv.
"""

from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent
INPUT = BASE / "traffic_accidents_cleaned.csv"
OUTPUT = BASE / "analysis_results.csv"

df = pd.read_csv(INPUT)
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Time"] = pd.to_datetime(df["Time"], format="%H:%M", errors="coerce")
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month_name()
df["Month_Num"] = df["Date"].dt.month
df["Weekday"] = df["Date"].dt.day_name()
df["Hour"] = df["Time"].dt.hour

def time_block(h):
    if h < 6: return "00:00-05:59"
    if h < 12: return "06:00-11:59"
    if h < 18: return "12:00-17:59"
    return "18:00-23:59"

df["Time_Block"] = df["Hour"].apply(time_block)

results = []

def add_counts(section, series):
    counts = series.value_counts()
    for category, count in counts.items():
        results.append({
            "section": section, "metric": "accidents",
            "category": category, "count": int(count),
            "percentage": round(count / len(df) * 100, 1)
        })

results += [
    {"section":"overall","metric":"total_accidents","category":"All","count":len(df),"percentage":100.0},
    {"section":"overall","metric":"total_vehicles_involved","category":"All","count":int(df["Vehicles_Involved"].sum()),"percentage":""},
    {"section":"overall","metric":"total_injuries","category":"All","count":int(df["Injuries"].sum()),"percentage":""},
    {"section":"overall","metric":"total_fatalities","category":"All","count":int(df["Fatalities"].sum()),"percentage":""},
    {"section":"overall","metric":"avg_vehicles_per_accident","category":"All","count":round(df["Vehicles_Involved"].mean(),3),"percentage":""},
    {"section":"overall","metric":"avg_injuries_per_accident","category":"All","count":round(df["Injuries"].mean(),3),"percentage":""},
    {"section":"overall","metric":"avg_fatalities_per_accident","category":"All","count":round(df["Fatalities"].mean(),3),"percentage":""},
]
add_counts("year", df["Year"])
add_counts("month", df["Month"])
add_counts("time_block", df["Time_Block"])
add_counts("weekday", df["Weekday"])
add_counts("severity", df["Accident_Severity"])
add_counts("city", df["City"])
add_counts("weather", df["Weather_Condition"])
add_counts("road", df["Road_Condition"])
add_counts("vehicle", df["Vehicle_Type"])
add_counts("cause", df["Accident_Cause"])

pd.DataFrame(results).to_csv(OUTPUT, index=False)
print(f"Analysis complete: {OUTPUT}")
