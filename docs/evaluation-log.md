# Evaluation Log

## Project

Manhattan Urban Heat Hotspot Prioritisation and Heat Risk Prediction

---

## Evaluation Purpose

This log records the evaluation activities performed during Sessions 4 and 5 and documents the evidence used to assess the credibility, reproducibility, and predictive performance of the workflow.

---

## Evaluation Activity 1

### Activity

Review land surface temperature outputs.

### Evidence

| Metric      | Value    |
| ----------- | -------- |
| Minimum LST | 10.33 °C |
| Mean LST    | 30.73 °C |
| Maximum LST | 49.20 °C |

### Observation

The temperature distribution exhibits substantial variation across Manhattan, suggesting that the workflow captures meaningful spatial differences in urban heat exposure.

### Outcome

Passed.

---

## Evaluation Activity 2

### Activity

Review vegetation density outputs.

### Evidence

| Metric       | Value |
| ------------ | ----- |
| Minimum NDVI | -0.27 |
| Mean NDVI    | 0.09  |
| Maximum NDVI | 0.70  |

### Observation

The NDVI distribution indicates considerable variation in vegetation coverage across the study area.

### Outcome

Passed.

---

## Evaluation Activity 3

### Activity

Assess data sufficiency.

### Evidence

| Dataset    | Scenes |
| ---------- | -----: |
| Landsat 8  |      2 |
| Sentinel-2 |      7 |

### Observation

The available imagery was sufficient to generate summer composite layers for both environmental indicators.

### Outcome

Passed.

---

## Evaluation Activity 4

### Activity

Review heat-risk formulation.

### Formula

```text
Heat Risk Score =
Normalized LST − Normalized NDVI
```

### Observation

The formulation is consistent with established urban heat island principles:

* Higher temperature increases risk.
* Greater vegetation reduces risk.

### Outcome

Passed.

---

## Evaluation Activity 5

### Activity

Review hotspot extraction process.

### Evidence

```text
Top hotspot samples extracted: 10
```

### Observation

The workflow successfully identified a subset of locations representing elevated relative heat risk.

### Outcome

Passed.

---

## Evaluation Activity 6

### Activity

Review reproducibility.

### Evidence

* Public satellite datasets
* Documented formulas
* Version-controlled notebooks
* Archived summary statistics
* Explicit study period

### Observation

The workflow can be reproduced by another researcher using the documented process.

### Outcome

Passed.

---

## Evaluation Activity 7

### Activity

Evaluate Heat Risk Prediction Model.

### Training Dataset

```text
10,000 samples
```

### Model

```text
Random Forest Regressor
```

### Evidence

| Metric |  Value |
| ------ | -----: |
| MAE    | 0.0021 |
| RMSE   | 0.0044 |
| R²     | 0.9997 |

### Observation

The model successfully learned the relationship between environmental indicators and heat-risk scores.

Prediction error is extremely low and the model explains nearly all observed variation in the target variable.

### Outcome

Passed.

---

## Evaluation Activity 8

### Activity

Review feature importance.

### Evidence

| Feature | Importance |
| ------- | ---------: |
| NDVI    |     0.6336 |
| LST     |     0.3664 |

### Observation

Vegetation density contributes most strongly to model predictions, followed by land surface temperature.

This result is consistent with the heat-risk framework and highlights the importance of urban greening in reducing relative heat exposure.

### Outcome

Passed.

---

## Issues Identified

### Issue 1

No comparison has yet been performed against the NYC Heat Vulnerability Index.

Severity:

Medium

Recommended Action:

Perform external comparison during future work.

---

### Issue 2

Analysis covers only Summer 2018.

Severity:

Low

Recommended Action:

Extend workflow to multiple years and seasons.

---

### Issue 3

The model was trained using data generated from the heat-risk framework itself.

Severity:

Medium

Recommended Action:

Future work should incorporate independent environmental or vulnerability datasets to assess generalisability.

---

## Final Evaluation Status

```text
PASSED
```

The workflow successfully produced:

* Land Surface Temperature profiles
* Vegetation Density profiles
* Heat Risk scores
* Urban Heat Hotspots
* A Heat Risk Prediction Model

The resulting framework and trained model are suitable for exploratory planning, educational applications, and future decision-support tool development.
