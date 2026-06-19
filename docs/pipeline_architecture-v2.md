# Pipeline Architecture V2

## Purpose

Pipeline Architecture V2 extends the Session 3 data preparation workflow by introducing a reproducible geospatial heat-risk analysis framework.

The objective of this pipeline is to identify relative urban heat hotspots across Manhattan using satellite-derived land surface temperature (LST) and vegetation density (NDVI).

The resulting outputs support neighbourhood-scale heat mitigation planning and form the analytical foundation for later evaluation and decision-support activities.

---

## Pipeline Overview

```text
Manhattan Study Area
        ↓
Landsat 8 Collection 2 Level 2
        ↓
Land Surface Temperature (LST)
        ↓

Sentinel-2 Surface Reflectance
        ↓
Normalized Difference Vegetation Index (NDVI)
        ↓

Environmental Profiling
        ↓

LST Normalization
        ↓

NDVI Normalization
        ↓

Heat Risk Score
(LSTnorm − NDVInorm)
        ↓

Hotspot Identification
        ↓

Priority Intervention Zones
        ↓

Evaluation & Decision Support
```

---

## Pipeline Components

### 1. Study Area Definition

Purpose:

Define the geographic extent for analysis.

Study Area:

```text
Manhattan
New York City
United States
```

Time Period:

```text
2018-06-01
to
2018-08-31
```

Output:

* Analysis boundary

---

### 2. Land Surface Temperature Extraction

Purpose:

Measure spatial variation in urban surface temperature.

Dataset:

```text
LANDSAT/LC08/C02/T1_L2
```

Scenes Used:

```text
2 scenes
```

Thermal Processing:

```text
LST = (ST_B10 × 0.00341802) + 149.0 − 273.15
```

Output:

* Mean Summer LST raster

Observed Statistics:

| Metric  | Value    |
| ------- | -------- |
| Minimum | 10.33 °C |
| Mean    | 30.73 °C |
| Maximum | 49.20 °C |

---

### 3. Vegetation Density Extraction

Purpose:

Measure vegetation presence and spatial greenness.

Dataset:

```text
COPERNICUS/S2_SR
```

Scenes Used:

```text
7 scenes
```

NDVI Calculation:

```text
NDVI = (B8 − B4) / (B8 + B4)
```

Output:

* Median Summer NDVI raster

Observed Statistics:

| Metric  | Value |
| ------- | ----- |
| Minimum | -0.27 |
| Mean    | 0.09  |
| Maximum | 0.70  |

---

### 4. Environmental Profiling

Purpose:

Summarise environmental conditions across Manhattan.

Profiling Activities:

* LST distribution assessment
* NDVI distribution assessment
* Spatial consistency review
* Plausibility checking
* Range validation

Artifact Produced:

```text
data/profile-summary.json
```

---

### 5. Heat Risk Scoring

Purpose:

Combine thermal exposure and vegetation conditions into a single interpretable indicator.

#### Step 1

Normalize LST values.

#### Step 2

Normalize NDVI values.

#### Step 3

Compute heat risk score:

```text
Heat Risk Score =
Normalized LST − Normalized NDVI
```

Interpretation:

* High LST increases risk
* High NDVI reduces risk
* Higher scores indicate greater relative heat exposure

Output:

* Heat Risk raster

---

### 6. Hotspot Identification

Purpose:

Identify locations exhibiting the highest relative heat risk.

Method:

* Evaluate heat risk raster
* Extract highest-risk locations
* Generate hotspot samples

Output:

```text
Top hotspot samples extracted
Count: 10
```

Produced Artifacts:

* Hotspot layer
* Hotspot summary

---

### 7. Decision-Support Outputs

Purpose:

Translate analytical outputs into actionable planning information.

Outputs:

* LST visualisation
* NDVI visualisation
* Heat risk visualisation
* Hotspot maps
* Priority intervention locations

Potential Applications:

* Urban greening
* Tree planting
* Heat mitigation planning
* Environmental monitoring
* Climate adaptation planning

---

## Repository Artifacts

### Data

```text
data/
├── profile-summary.json
└── processed/
```

### Notebooks

```text
notebooks/
├── 01-data-profiling.ipynb
├── 02-data-cleaning.ipynb
└── 03-heat-risk-analysis.ipynb
```

### Documentation

```text
docs/
├── problem-brief-v2.md
├── system-sketch-v0.md
├── output-sketch-v0.md
├── modelling_log.md
└── heat-risk-analysis-card.md
```

---

## Reproducibility Strategy

The pipeline was designed to be reproducible through:

* Public satellite datasets
* Explicit processing formulas
* Documented study period
* Version-controlled notebooks
* Archived summary statistics
* Transparent analytical rules

The V2 analytical pipeline itself uses no stochastic model training. The heat risk outputs produced here are later used to train the Heat Risk Prediction Model (Random Forest Regressor), documented in [`model_card.md`](model_card.md) and reflected in Pipeline Architecture V3.

---

## Limitations

### Temporal Limitation

The analysis represents conditions during Summer 2018 only.

### Spatial Resolution Limitation

Results are constrained by the resolution of Landsat and Sentinel imagery.

### Interpretation Limitation

The heat risk score represents relative spatial heat exposure and should not be interpreted as a direct measure of human thermal stress.

---

## Future Extensions

Potential future improvements include:

* Neighbourhood-scale aggregation using NYC NTAs
* Comparison against the NYC Heat Vulnerability Index
* Multi-year temporal analysis
* Seasonal comparisons
* Interactive web-based decision-support tools
* Additional environmental indicators

---

## Summary

Pipeline Architecture V2 transforms satellite observations into a reproducible urban heat hotspot identification workflow.

The pipeline combines:

* Land Surface Temperature
* Vegetation Density
* Heat Risk Scoring
* Hotspot Identification

to support evidence-based urban heat mitigation planning across Manhattan.
