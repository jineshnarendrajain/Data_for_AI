# Modelling Log

## Objective

Develop a transparent and reproducible geospatial analysis workflow to identify relative urban heat hotspots across Manhattan using remotely sensed environmental indicators.

The workflow supports neighbourhood-scale heat mitigation planning by combining land surface temperature (LST) and vegetation density (NDVI) into a composite heat risk score.

---

## Analysis Overview

This project follows a rule-based analytical approach rather than a predictive machine learning workflow.

The objective is to identify areas that simultaneously exhibit:

* High land surface temperature
* Low vegetation density

These areas are interpreted as relative urban heat hotspots and may represent priority locations for heat mitigation interventions such as tree planting, greening programs, shading infrastructure, and public-space cooling strategies.

---

## Study Area

**Location:** Manhattan, New York City

**Study Period:** Summer 2018

```text
2018-06-01
to
2018-08-31
```

---

## Data Sources

### Landsat 8 Collection 2 Level 2

Purpose:

* Land Surface Temperature (LST) estimation

Dataset:

```text
LANDSAT/LC08/C02/T1_L2
```

Scenes used:

```text
2 scenes
```

Thermal processing:

```text
LST = (ST_B10 × 0.00341802) + 149.0 − 273.15
```

Output:

```text
Mean Summer Land Surface Temperature Raster
```

---

### Sentinel-2 Surface Reflectance

Purpose:

* Vegetation density assessment

Dataset:

```text
COPERNICUS/S2_SR
```

Scenes used:

```text
7 scenes
```

NDVI calculation:

```text
NDVI = (B8 − B4) / (B8 + B4)
```

Output:

```text
Median Summer NDVI Raster
```

---

## Environmental Profiling Results

### Land Surface Temperature (LST)

| Statistic | Value    |
| --------- | -------- |
| Minimum   | 10.33 °C |
| Mean      | 30.73 °C |
| Maximum   | 49.20 °C |

Interpretation:

Large temperature variation exists across Manhattan during the study period, indicating substantial spatial differences in urban heat exposure.

---

### Normalized Difference Vegetation Index (NDVI)

| Statistic | Value |
| --------- | ----- |
| Minimum   | -0.27 |
| Mean      | 0.09  |
| Maximum   | 0.70  |

Interpretation:

Vegetation density varies considerably across Manhattan, with some areas exhibiting very limited green coverage while others contain substantial vegetation.

---

## Heat Risk Model

### Concept

Urban heat exposure is influenced by both temperature and vegetation.

Areas with:

```text
High LST
+
Low NDVI
```

are expected to experience greater relative heat stress.

---

### Risk Score Construction

#### Step 1

Normalize LST values:

```text
LST_normalized
```

#### Step 2

Normalize NDVI values:

```text
NDVI_normalized
```

#### Step 3

Compute relative heat risk:

```text
Risk Score =
LST_normalized − NDVI_normalized
```

Interpretation:

* Higher values indicate higher relative heat risk
* Lower values indicate lower relative heat risk

---

## Hotspot Identification

The heat risk raster was used to identify areas exhibiting the highest relative heat exposure.

Results:

```text
Top hotspot samples extracted: 10
```

These hotspot locations form the basis for later prioritisation and evaluation activities.

---

## Reproducibility Strategy

The workflow was designed to be reproducible through:

* Publicly accessible satellite datasets
* Explicit processing formulas
* Documented study period
* Version-controlled notebooks
* Saved summary statistics
* Deterministic analytical procedures

No stochastic model training was used.

---

## Lessons Learned

* Remote sensing data can provide meaningful indicators of urban heat exposure.
* Vegetation density is an important contextual factor when interpreting surface temperature.
* Transparent analytical rules are easier to explain to planners than black-box predictive systems.
* Spatial hotspot identification can support targeted urban heat mitigation planning.

---

## Produced Artifacts

### Notebook

```text
notebooks/01-data-profiling.ipynb
```

### Summary Statistics

```text
data/profile-summary.json
```

### Derived Outputs

```text
Mean Summer LST Raster
Median Summer NDVI Raster
Heat Risk Raster
Top 10 Hotspot Samples
```

---

## Session 4 Outcome

Session 4 produced a reproducible urban heat hotspot identification workflow for Manhattan based on Landsat-derived land surface temperature and Sentinel-derived vegetation density.

The resulting heat risk model establishes the analytical foundation for Session 5 evaluation and Session 6 decision-support development.
