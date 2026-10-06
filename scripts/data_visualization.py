"""
Traffic Accidents Analysis - Issue #5
Data Visualization Script

Run from the repository root:
    python scripts/data_visualization.py

Input:
    data/traffic_accidents_raw.csv

Outputs:
    results/figures/accidents_by_year.png
    results/figures/accidents_by_month.png
    results/figures/accidents_by_severity.png
    results/figures/accidents_by_location.png
    results/figures/accidents_by_weather.png
    results/figures/accidents_by_road_condition.png
    results/figures/accidents_by_vehicle_type.png
    results/figures/accident_heatmap.png

A geographic map is intentionally not generated because the supplied CSV
does not contain latitude/longitude coordinates.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "traffic_accidents_raw.csv"
OUT = ROOT / "results" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_PATH)
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Month_Name"] = df["Date"].dt.strftime("%b")

def save_bar(series, title, xlabel, filename, rotate=0, top_n=None):
    s = series.dropna()
    if top_n:
        s = s.value_counts().head(top_n)
    else:
        s = s.value_counts()
    fig, ax = plt.subplots(figsize=(10, 6))
    s.plot(kind="bar", ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Number of Accidents")
    ax.tick_params(axis="x", rotation=rotate)
    fig.tight_layout()
    fig.savefig(OUT / filename, dpi=200, bbox_inches="tight")
    plt.close(fig)

# 1. Accident trend by year
year_counts = df["Year"].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(year_counts.index, year_counts.values, marker="o")
ax.set_title("Traffic Accidents by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Accidents")
ax.grid(True, alpha=0.25)
fig.tight_layout()
fig.savefig(OUT / "accidents_by_year.png", dpi=200, bbox_inches="tight")
plt.close(fig)

# 2. Accident trend by month
month_counts = df["Month"].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(month_counts.index, month_counts.values, marker="o")
ax.set_title("Traffic Accidents by Month")
ax.set_xlabel("Month")
ax.set_ylabel("Number of Accidents")
ax.set_xticks(range(1, 13))
fig.tight_layout()
fig.savefig(OUT / "accidents_by_month.png", dpi=200, bbox_inches="tight")
plt.close(fig)

# 3. Severity
save_bar(
    df["Accident_Severity"],
    "Traffic Accidents by Severity",
    "Accident Severity",
    "accidents_by_severity.png"
)

# 4. Location
save_bar(
    df["City"],
    "Traffic Accidents by Location",
    "City",
    "accidents_by_location.png",
    rotate=60,
    top_n=20
)

# 5. Weather
save_bar(
    df["Weather_Condition"],
    "Traffic Accidents by Weather Condition",
    "Weather Condition",
    "accidents_by_weather.png",
    rotate=30
)

# 6. Road condition
save_bar(
    df["Road_Condition"],
    "Traffic Accidents by Road Condition",
    "Road Condition",
    "accidents_by_road_condition.png",
    rotate=30
)

# 7. Vehicle type
save_bar(
    df["Vehicle_Type"],
    "Traffic Accidents by Vehicle Type",
    "Vehicle Type",
    "accidents_by_vehicle_type.png",
    rotate=30
)

# 8. Heatmap: accident counts by weather and road condition
heatmap = pd.crosstab(df["Weather_Condition"], df["Road_Condition"])

fig, ax = plt.subplots(figsize=(10, 6))
im = ax.imshow(heatmap.values, aspect="auto")
ax.set_title("Accident Count: Weather Condition vs Road Condition")
ax.set_xlabel("Road Condition")
ax.set_ylabel("Weather Condition")
ax.set_xticks(range(len(heatmap.columns)))
ax.set_xticklabels(heatmap.columns, rotation=30, ha="right")
ax.set_yticks(range(len(heatmap.index)))
ax.set_yticklabels(heatmap.index)

for i in range(heatmap.shape[0]):
    for j in range(heatmap.shape[1]):
        ax.text(j, i, heatmap.iloc[i, j], ha="center", va="center")

fig.colorbar(im, ax=ax, label="Number of Accidents")
fig.tight_layout()
fig.savefig(OUT / "accident_heatmap.png", dpi=200, bbox_inches="tight")
plt.close(fig)

# Map applicability check
coordinate_columns = {
    c.lower() for c in df.columns
} & {"latitude", "longitude", "lat", "lon", "lng"}

if not coordinate_columns:
    note = ROOT / "results" / "map_not_applicable.md"
    note.write_text(
        "# Geographic Map — Not Applicable\n\n"
        "The supplied `traffic_accidents_raw.csv` does not contain latitude/longitude "
        "coordinates. Issue #5 therefore does not require an accident hotspot map for "
        "the current dataset. A map can be added later if coordinate columns are "
        "provided or a verified location-coordinate dataset is joined using a documented "
        "method.\n",
        encoding="utf-8",
    )

print("Visualization generation completed.")
print(f"Figures saved to: {OUT}")
print("Geographic map: not generated because coordinate columns are unavailable.")
