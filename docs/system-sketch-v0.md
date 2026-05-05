# System Sketch v0

---

## Overview

This system processes satellite-derived datasets to identify heat exposure hotspots in Manhattan and prioritise zones for heat mitigation interventions.

The pipeline integrates land surface temperature (LST) and vegetation data (NDVI) to generate spatially explicit outputs that support decision-making.

---

## Pipeline Diagram

```mermaid
graph TD

A[Define Study Area: Manhattan] --> B[Load Landsat LST Data]
A --> C[Load Sentinel-2 NDVI Data]

B --> D[Filter Summer Period + Cloud Filtering]
C --> E[Filter Summer Period + Cloud Masking]

D --> F[Compute LST (°C)]
E --> G[Compute NDVI]

F --> H[Aggregate LST (Mean)]
G --> I[Aggregate NDVI (Median)]

H --> J[Spatial Alignment]
I --> J

J --> K[Combine LST + NDVI]

K --> L[Apply Rule-Based Classification]
L --> M[Identify High-Risk Zones]

M --> N[Validate with NYC Heat Vulnerability Index]

N --> O[Output Map / Priority Zones]
```

---

## Step-by-Step Explanation

### 1. Study Area Definition

* Manhattan boundary is extracted using administrative data
* Ensures analysis is restricted to relevant geographic extent

---

### 2. Data Ingestion

**Landsat (LST):**

* Source: Landsat 8 Collection 2
* Thermal band used to derive land surface temperature

**Sentinel-2 (NDVI):**

* Source: Sentinel-2 Surface Reflectance
* Red and Near-Infrared bands used to compute NDVI

---

### 3. Data Filtering

* Temporal filtering: June–August (peak summer)
* Cloud filtering applied:

  * Landsat: cloud cover metadata
  * Sentinel-2: SCL-based masking

---

### 4. Feature Extraction

* LST computed from thermal band and converted to °C
* NDVI computed using normalized difference formula

---

### 5. Aggregation

* LST aggregated using mean (captures overall heat pattern)
* NDVI aggregated using median (reduces noise and cloud artifacts)

---

### 6. Data Integration

* LST and NDVI layers are spatially aligned
* Combined to create a joint dataset representing heat + vegetation

---

### 7. Classification Logic

A rule-based approach is used:

* High LST + Low NDVI → High-risk zone
* Low LST + High NDVI → Low-risk zone

This provides a simplified but interpretable method for identifying priority areas.

---

### 8. Validation

* Results are compared with NYC Heat Vulnerability Index
* Used as a reference to check consistency with known vulnerable areas

---

### 9. Output

* Spatial map highlighting:

  * High-risk zones
  * Moderate zones
  * Low-risk zones

* Enables planners to prioritise interventions such as:

  * tree planting
  * shading
  * material changes

---

## Assumptions

* LST is a valid proxy for urban heat intensity
* NDVI adequately represents vegetation presence
* Summer conditions represent peak thermal stress
* Rule-based classification is sufficient for prioritisation

---

## Limitations

* Does not account for humidity, wind, or human thermal comfort
* Limited temporal scope (single season snapshot)
* Spatial resolution constraints (30m vs 10m)
* Simplified classification logic (no predictive modeling)

---

## Conclusion

The system provides a transparent and reproducible pipeline for identifying urban heat hotspots and prioritising intervention zones using satellite data. While simplified, it offers actionable insights for urban planning and climate resilience strategies.
