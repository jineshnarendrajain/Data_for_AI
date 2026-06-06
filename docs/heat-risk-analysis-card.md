# Heat Risk Analysis Card

## Analysis Name

Manhattan Urban Heat Hotspot Prioritisation Framework

---

## Analysis Type

Rule-Based Geospatial Heat Risk Assessment

---

## Purpose

This analysis identifies relative urban heat hotspots across Manhattan using remotely sensed environmental indicators.

The framework combines land surface temperature (LST) and vegetation density (NDVI) to highlight areas that may benefit from heat mitigation interventions.

The analysis is intended to support:

* Urban heat assessment
* Greening strategy prioritisation
* Tree planting initiatives
* Heat mitigation planning
* Educational and research workflows

---

## Study Area

**Location:** Manhattan, New York City

**Study Period:** Summer 2018

```text
2018-06-01 to 2018-08-31
```

---

## Data Sources

### Landsat 8 Collection 2 Level 2

Purpose:

* Land Surface Temperature estimation

Dataset:

```text
LANDSAT/LC08/C02/T1_L2
```

Scenes used:

```text
2 scenes
```

---

### Sentinel-2 Surface Reflectance

Purpose:

* Vegetation density estimation

Dataset:

```text
COPERNICUS/S2_SR
```

Scenes used:

```text
7 scenes
```

---

## Inputs

### Environmental Inputs

#### Land Surface Temperature (LST)

Derived from Landsat thermal imagery using:

```text
LST = (ST_B10 × 0.00341802) + 149.0 − 273.15
```

Observed values:

| Statistic | Value    |
| --------- | -------- |
| Minimum   | 10.33 °C |
| Mean      | 30.73 °C |
| Maximum   | 49.20 °C |

---

#### Vegetation Density (NDVI)

Derived from Sentinel-2 imagery using:

```text
NDVI = (B8 − B4) / (B8 + B4)
```

Observed values:

| Statistic | Value |
| --------- | ----- |
| Minimum   | -0.27 |
| Mean      | 0.09  |
| Maximum   | 0.70  |

---

## Analysis Logic

### Step 1

Normalize LST values.

### Step 2

Normalize NDVI values.

### Step 3

Compute heat risk score:

```text
Heat Risk Score =
Normalized LST − Normalized NDVI
```

Interpretation:

* Higher scores indicate higher relative heat risk.
* Lower scores indicate lower relative heat risk.

---

## Outputs

The framework produces:

* Mean Summer LST raster
* Median Summer NDVI raster
* Relative heat risk raster
* Hotspot visualisation layer
* Top hotspot locations

Extracted hotspot count:

```text
10 hotspot samples
```

---

## Intended Users

* Urban planners
* Municipal agencies
* Climate adaptation researchers
* GIS analysts
* Academic researchers
* Students studying urban environmental systems

---

## Limitations

### Temporal Scope

The analysis only represents conditions during:

```text
Summer 2018
```

and should not be interpreted as a year-round assessment.

---

### Spatial Resolution

Results are constrained by:

* Landsat 8 thermal resolution
* Sentinel-2 optical resolution

Small-scale microclimatic variations may not be captured.

---

### Relative Risk Interpretation

The heat risk score represents:

```text
Relative heat exposure
```

not measured human heat stress.

The framework identifies priority areas for further investigation rather than definitive hazard levels.

---

### Data Availability

Results depend on satellite scene availability and cloud-filtering procedures.

---

## Ethical Considerations

Outputs should support planning and exploratory analysis rather than automated decision making.

Human review and local contextual knowledge remain essential before implementing interventions.

---

## Reproducibility

The workflow is reproducible because:

* Public satellite datasets are used.
* Processing formulas are documented.
* Study period is explicitly defined.
* Summary statistics are archived.
* Analytical rules are transparent.

---

## Version

Version 2.0

Session 4 Geospatial Analysis Deliverable
