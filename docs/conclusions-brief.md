# Conclusions Brief

## Project

Manhattan Urban Heat Hotspot Prioritisation and Heat Risk Prediction

---

## Executive Summary

This project developed a reproducible urban heat analysis and prediction workflow for Manhattan using publicly available Earth observation data.

The workflow combines:

* Land Surface Temperature (LST) derived from Landsat 8
* Vegetation Density (NDVI) derived from Sentinel-2

to generate a relative heat-risk framework and identify urban heat hotspots.

Building on this framework, a machine learning dataset containing 10,000 spatial samples was generated and used to train a Random Forest model capable of predicting relative heat-risk conditions from environmental indicators.

The resulting workflow provides both:

* A transparent geospatial heat-risk assessment framework
* An AI model that can support future decision-support applications

---

## Research Question

Can satellite-derived environmental indicators be combined to identify and predict relative urban heat hotspots across Manhattan?

---

## Key Findings

### Finding 1

Substantial spatial variation exists in land surface temperature across Manhattan.

Observed values:

| Statistic | Value    |
| --------- | -------- |
| Minimum   | 10.33 °C |
| Mean      | 30.73 °C |
| Maximum   | 49.20 °C |

This suggests that heat exposure is not uniformly distributed throughout the borough.

---

### Finding 2

Vegetation density varies considerably across the study area.

Observed values:

| Statistic | Value |
| --------- | ----- |
| Minimum   | -0.27 |
| Mean      | 0.09  |
| Maximum   | 0.70  |

This indicates meaningful differences in green infrastructure availability across Manhattan.

---

### Finding 3

Combining thermal and vegetation indicators produces an interpretable heat-risk framework.

The workflow successfully generated:

```text
Top hotspot samples extracted: 10
```

demonstrating that the analysis can distinguish relatively higher-risk and lower-risk locations.

---

### Finding 4

A machine learning model can accurately reproduce the heat-risk framework.

Training dataset:

```text
10,000 samples
```

Model:

```text
Random Forest Regressor
```

Performance:

| Metric | Value  |
| ------ | ------ |
| MAE    | 0.0021 |
| RMSE   | 0.0044 |
| R²     | 0.9997 |

The model successfully learned the relationship between environmental indicators and heat-risk scores.

---

## Interpretation

The results support the hypothesis that areas exhibiting:

```text
Higher Surface Temperature
+
Lower Vegetation Density
```

represent locations of elevated relative heat exposure.

The trained model demonstrates that these relationships can be reliably reproduced and used within future planning and decision-support workflows.

---

## Practical Implications

Potential applications include:

* Urban greening strategies
* Tree planting programmes
* Shade infrastructure planning
* Heat mitigation planning
* Environmental monitoring
* Climate adaptation initiatives

The workflow provides a transparent and reproducible basis for identifying and prioritising intervention locations.

---

## Limitations

### Temporal Scope

The analysis only represents Summer 2018 conditions.

### Relative Risk Framework

The outputs represent relative heat exposure rather than direct measurements of human thermal stress.

### External Validation

The framework has not yet been formally compared against the NYC Heat Vulnerability Index.

### Model Scope

The trained model reproduces the heat-risk framework developed in this project and should not be interpreted as a causal model of human heat vulnerability.

---

## Future Work

Recommended future extensions include:

1. Comparison with the NYC Heat Vulnerability Index.
2. Aggregation to Manhattan neighbourhood boundaries.
3. Multi-year analysis.
4. Seasonal comparison studies.
5. Development of a Manhattan Heat Mitigation Decision Support Tool.
6. Integration of additional environmental indicators.
7. Interactive web-based planning workflows.

---

## Final Conclusion

The project demonstrates that publicly available Earth observation data can be used to identify relative urban heat hotspots across Manhattan through a transparent and reproducible analytical workflow.

The project further demonstrates that a machine learning model can accurately reproduce the resulting heat-risk framework using satellite-derived environmental indicators.

Together, the analytical framework and trained Heat Risk Prediction Model provide a foundation for future urban heat mitigation and decision-support applications.

The resulting outputs are suitable for exploratory planning, educational applications, urban climate analysis, and the development of AI-assisted heat mitigation tools when interpreted within their documented limitations.
