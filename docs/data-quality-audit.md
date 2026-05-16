# Data Quality Audit

---

## Dataset Overview

Two satellite-derived datasets were analysed for Manhattan during peak summer conditions (June–August 2018):

* Landsat 8 Land Surface Temperature (LST)
* Sentinel-2 NDVI (Normalized Difference Vegetation Index)

The datasets were processed using temporal filtering, cloud filtering/masking, spatial clipping, and aggregation techniques to generate neighbourhood-scale environmental indicators.

---

## Key Findings

### 1. Land Surface Temperature (LST)

Observed LST statistics:

* Minimum: ~10.3°C
* Mean: ~30.7°C
* Maximum: ~49.2°C

The results indicate strong spatial variation in surface temperature across Manhattan, with elevated temperatures concentrated in dense built-up urban areas and transportation corridors.

---

### 2. Vegetation Distribution (NDVI)

Observed NDVI statistics:

* Minimum: ~-0.27
* Mean: ~0.09
* Maximum: ~0.69

NDVI values indicate generally low vegetation density across much of Manhattan, with higher vegetation concentrations primarily located in Central Park and smaller urban green spaces.

---

### 3. Relationship Between LST and NDVI

A consistent inverse spatial relationship was observed between vegetation density and land surface temperature:

* Areas with relatively low NDVI values generally correspond to elevated LST values
* Areas with higher NDVI values generally correspond to lower observed LST values

This suggests that vegetation density is spatially associated with reduced surface temperature intensity across the study area. However, the relationship should be interpreted as correlational rather than causal.

---

## Data Limitations

* LST represents land surface thermal conditions rather than full human thermal comfort
* NDVI is a vegetation proxy and does not directly measure canopy structure, shading performance, or ecological quality
* Temporal scope is limited to Summer 2018 and does not support long-term trend analysis or forecasting
* Cloud contamination and atmospheric variability may introduce inconsistencies despite filtering procedures
* Spatial resolution differences between Landsat (~30m) and Sentinel-2 (~10m) may affect pixel-level alignment
* Satellite-derived observations cannot fully capture street-level microclimate variability

---

## Data Fitness for Purpose

Despite limitations, the datasets are suitable for:

* Identifying relative urban thermal hotspot patterns
* Comparing spatial variation in vegetation density
* Analysing relationships between vegetation distribution and surface temperature
* Supporting neighbourhood-scale urban heat mitigation prioritisation

The datasets are not suitable for:

* Human physiological heat stress analysis
* Detailed microclimate simulation
* Building-scale or street-scale thermal modelling
* Predictive climate forecasting

---

## Conclusion

The datasets provide a reliable and interpretable basis for neighbourhood-scale urban thermal hotspot analysis in Manhattan. Landsat-derived LST enables identification of elevated surface temperature zones, while Sentinel-2 NDVI provides contextual information about vegetation distribution. Although the analysis relies on satellite-derived proxy variables with known limitations, the datasets are appropriate for relative spatial comparison and urban heat mitigation planning support.
