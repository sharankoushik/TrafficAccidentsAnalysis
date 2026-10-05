# Traffic Accidents Analysis Summary

## Overview
The cleaned traffic accident dataset contains **500 accidents** recorded from **2 January 2023 to 27 December 2024** across **20 cities and 15 states**.

Overall totals:
- Vehicles involved: **1,264**
- Injuries: **2,031**
- Fatalities: **20**
- Average vehicles per accident: **2.528**
- Average injuries per accident: **4.062**

## Key Findings

### 1. Year-wise trend
The dataset contains **250 accidents in 2023** and **250 in 2024**, so the two years have an identical accident count.

### 2. Time and seasonal patterns
- The largest 6-hour time block is **00:00–05:59**, with **137 accidents (27.4%)**.
- Friday has the most accidents among weekdays, with **78 (15.6%)**.
- July is the highest-accident month with **50 (10.0%)**.
- June is the lowest with **29 (5.8%)**.

### 3. Accident severity
- **Minor:** 244 (48.8%)
- **Moderate:** 174 (34.8%)
- **Severe:** 65 (13.0%)
- **Fatal:** 17 (3.4%)

Minor accidents are the most common category, while fatal accidents form a small share of the dataset.

### 4. Accident-prone locations
The highest accident counts are:
1. Delhi — 36
2. Bhopal — 33
3. Visakhapatnam — 31
4. Kochi — 31
5. Indore — 31
6. Patna — 30

These are frequency findings only; they do not imply that a city is inherently more dangerous because exposure such as population, traffic volume, or road mileage is not included.

### 5. Weather conditions
- Rain — 110 (22.0%)
- Overcast — 109 (21.8%)
- Cloudy — 97 (19.4%)
- Clear — 92 (18.4%)
- Fog — 92 (18.4%)

Rain and overcast conditions account for the largest shares.

### 6. Road conditions
- Poor — 108 (21.6%)
- Under Construction — 104 (20.8%)
- Dry — 101 (20.2%)
- Potholes — 96 (19.2%)
- Wet — 91 (18.2%)

Poor and under-construction road conditions are the two most frequent categories.

### 7. Vehicle types
- Bus — 80 (16.0%)
- Car — 77 (15.4%)
- Van — 74 (14.8%)
- Truck — 74 (14.8%)
- Auto Rickshaw — 67 (13.4%)
- SUV — 64 (12.8%)
- Motorcycle — 64 (12.8%)

Buses have the highest accident count in this dataset.

### 8. Accident causes
The most frequently recorded contributing factors are:
1. Speeding — 79 (15.8%)
2. Weather — 77 (15.4%)
3. Drunk Driving — 75 (15.0%)
4. Distracted Driving — 73 (14.6%)
5. Poor Road Condition — 72 (14.4%)

These are associations recorded in the dataset, not proof of causation.

## Conclusion
The analysis shows that accidents are distributed evenly across the two years, with noticeable variation by month and time of day. Early-morning hours, July, Friday, Delhi, rainy/overcast weather, poor road conditions, buses, and speeding are prominent categories in the dataset. The results provide a useful descriptive baseline for later visualization and deeper relationship analysis.

## Files
- `data_analysis.ipynb` — reproducible analysis notebook
- `data_analysis.py` — Python analysis script
- `analysis_results.csv` — structured analysis results
- `analysis_summary.md` — major findings and interpretation
