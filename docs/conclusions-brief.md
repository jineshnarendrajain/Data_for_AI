# Conclusions Brief

## Project

Manhattan Urban Heat Hotspot Prioritisation

---

## Executive Summary

This project developed a reproducible geospatial workflow for identifying relative urban heat hotspots across Manhattan using publicly available satellite imagery.

The workflow combines:

* Land Surface Temperature (LST) derived from Landsat 8
* Vegetation Density (NDVI) derived from Sentinel-2

to generate a heat risk indicator intended to support urban heat mitigation planning.

---

## Research Question

Can satellite-derived environmental indicators be combined to identify relative urban heat hotspots across Manhattan?

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

## Interpretation

The results support the hypothesis that areas exhibiting:

```text
Higher Surface Temperature
+
Lower Vegetation Density
```

represent locations of elevated relative heat exposure.

These locations may be suitable candidates for further investigation and heat mitigation interventions.

---

## Practical Implications

Potential applications include:

* Urban greening strategies
* Tree planting programmes
* Heat mitigation planning
* Environmental monitoring
* Climate adaptation initiatives

The workflow provides a transparent and reproducible basis for prioritisation.

---

## Limitations

### Temporal Scope

The analysis only represents Summer 2018 conditions.

### Relative Risk Framework

The outputs represent relative heat exposure rather than direct measurements of human thermal stress.

### External Validation

The workflow has not yet been formally compared against the NYC Heat Vulnerability Index.

---

## Future Work

Recommended future extensions include:

1. Comparison with the NYC Heat Vulnerability Index.
2. Aggregation to Manhattan neighbourhood boundaries.
3. Multi-year analysis.
4. Seasonal comparison studies.
5. Interactive decision-support dashboards.

---

## Final Conclusion

The project demonstrates that publicly available Earth observation data can be used to identify relative urban heat hotspots across Manhattan through a transparent and reproducible analytical workflow.

The resulting outputs are suitable for exploratory planning, educational applications, and urban heat decision-support tasks when interpreted within their documented limitations.
