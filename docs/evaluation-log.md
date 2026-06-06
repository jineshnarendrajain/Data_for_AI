# Evaluation Log

## Project

Manhattan Urban Heat Hotspot Prioritisation

---

## Evaluation Purpose

This log records the evaluation activities performed during Session 5 and documents the evidence used to assess the credibility and usefulness of the analytical workflow.

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
| ---------- | ------ |
| Landsat 8  | 2      |
| Sentinel-2 | 7      |

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

## Final Evaluation Status

```text
PASSED
```

The workflow produced reproducible and interpretable outputs suitable for urban heat hotspot identification and decision-support applications.
