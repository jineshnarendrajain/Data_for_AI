# Evaluation Report

## Project

Manhattan Urban Heat Hotspot Prioritisation

---

## Evaluation Objective

The purpose of this evaluation is to assess whether the analytical workflow produces credible and useful evidence for identifying relative urban heat hotspots across Manhattan.

Unlike predictive machine learning projects, this evaluation focuses on the validity of derived conclusions rather than prediction accuracy.

---

## System Evaluated

The workflow combines:

* Landsat 8 Land Surface Temperature (LST)
* Sentinel-2 Normalized Difference Vegetation Index (NDVI)

to generate a relative heat risk score.

The final output is a set of hotspot locations intended to support urban heat mitigation planning.

---

## Evaluation Questions

### EQ1

Does the workflow successfully identify spatial variation in heat exposure across Manhattan?

### EQ2

Does the workflow incorporate a meaningful environmental indicator associated with heat mitigation?

### EQ3

Are the resulting hotspot locations plausible given known urban heat island behaviour?

### EQ4

Are the outputs sufficiently interpretable for planning and decision-support purposes?

---

## Evidence Reviewed

### Land Surface Temperature

| Metric  | Value    |
| ------- | -------- |
| Minimum | 10.33 °C |
| Mean    | 30.73 °C |
| Maximum | 49.20 °C |

Observed range:

```text
38.87 °C
```

The large temperature range indicates meaningful spatial variation across the study area.

---

### Vegetation Density

| Metric  | Value |
| ------- | ----- |
| Minimum | -0.27 |
| Mean    | 0.09  |
| Maximum | 0.70  |

The NDVI distribution indicates substantial variation in vegetation coverage across Manhattan.

---

### Satellite Coverage

| Dataset    | Scenes |
| ---------- | ------ |
| Landsat 8  | 2      |
| Sentinel-2 | 7      |

Coverage was sufficient to generate complete summer composites for the study period.

---

## Hotspot Identification

The workflow successfully generated:

```text
Top hotspot samples extracted: 10
```

indicating that the heat risk framework is capable of distinguishing higher-risk and lower-risk areas within the study area.

---

## Strengths

### Transparent Methodology

All calculations are explicitly documented and reproducible.

### Public Data Sources

The workflow uses publicly available Earth observation datasets.

### Explainable Logic

The risk score is straightforward:

```text
Normalized LST − Normalized NDVI
```

making the analysis easy to communicate to non-technical stakeholders.

### Planning Relevance

Outputs directly support urban heat mitigation prioritisation.

---

## Limitations

### Temporal Scope

The analysis only represents Summer 2018 conditions.

### Spatial Resolution

Some microclimatic effects may not be captured.

### Relative Risk Framework

The output represents relative heat exposure rather than measured human thermal stress.

### Limited Validation

The workflow has not yet been formally compared against the NYC Heat Vulnerability Index.

---

## Overall Assessment

The evaluation indicates that the workflow produces plausible, interpretable, and reproducible urban heat hotspot indicators suitable for exploratory planning and educational purposes.

The system should be viewed as a decision-support tool rather than an operational heat-risk forecasting system.

---

## Recommendation

Proceed to Session 6 development with the current workflow while documenting the need for future validation against external vulnerability datasets.
