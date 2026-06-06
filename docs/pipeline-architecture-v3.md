# Pipeline Architecture V3

## Purpose

Pipeline Architecture V3 documents the final validated workflow after Session 5 evaluation.

The architecture describes how publicly available Earth observation data are transformed into actionable urban heat intelligence for decision-support applications.

---

## Final Workflow

```text
Manhattan Study Area
        ↓

Landsat 8 Collection 2 Level 2
        ↓

Land Surface Temperature (LST)
        ↓

Sentinel-2 Surface Reflectance
        ↓

Vegetation Density (NDVI)
        ↓

Environmental Profiling
        ↓

Data Validation
        ↓

LST Normalization
        ↓

NDVI Normalization
        ↓

Heat Risk Score
        ↓

Hotspot Identification
        ↓

Evaluation & Validity Audit
        ↓

Priority Intervention Zones
        ↓

Decision Support Outputs
```

---

## Inputs

### Landsat 8

Purpose:

* Land Surface Temperature estimation

Dataset:

```text
LANDSAT/LC08/C02/T1_L2
```

Scenes:

```text
2
```

---

### Sentinel-2

Purpose:

* Vegetation density estimation

Dataset:

```text
COPERNICUS/S2_SR
```

Scenes:

```text
7
```

---

## Environmental Indicators

### Land Surface Temperature

Observed Statistics:

| Statistic | Value    |
| --------- | -------- |
| Minimum   | 10.33 °C |
| Mean      | 30.73 °C |
| Maximum   | 49.20 °C |

---

### Vegetation Density

Observed Statistics:

| Statistic | Value |
| --------- | ----- |
| Minimum   | -0.27 |
| Mean      | 0.09  |
| Maximum   | 0.70  |

---

## Heat Risk Framework

### Formula

```text
Heat Risk Score =
Normalized LST − Normalized NDVI
```

Interpretation:

* Higher temperature increases risk
* Greater vegetation reduces risk
* Higher scores indicate greater relative heat exposure

---

## Hotspot Identification

Output:

```text
Top hotspot samples extracted: 10
```

Purpose:

Identify candidate locations for:

* Urban greening
* Tree planting
* Heat mitigation interventions
* Climate adaptation planning

---

## Evaluation Layer

Session 5 introduced:

* Evaluation Report
* Evaluation Log
* Validity Audit
* Conclusions Brief

Evaluation confirmed:

* Appropriate data sources
* Plausible environmental variation
* Transparent methodology
* Reproducible workflow

---

## Decision Support Layer

The validated outputs support:

### Planning Activities

* Urban heat assessment
* Greening prioritisation
* Environmental monitoring
* Climate adaptation planning

### Future Tool Development

The workflow provides the analytical foundation for a future interactive dashboard capable of visualising:

* LST
* NDVI
* Heat Risk
* Hotspot locations

for non-technical stakeholders.

---

## Limitations

### Temporal

Summer 2018 only.

### Spatial

Dependent on satellite imagery resolution.

### Interpretation

Represents relative heat exposure rather than direct human thermal stress.

### Validation

External comparison with the NYC Heat Vulnerability Index remains future work.

---

## Final Status

```text
VALIDATED
```

Pipeline Architecture V3 represents the final evaluated workflow and serves as the foundation for future decision-support development.
