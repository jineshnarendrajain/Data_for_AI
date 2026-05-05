# Data Quality Audit

---

## Dataset Overview

Two primary datasets were analysed:

* Landsat 8 Surface Temperature (LST) for heat patterns
* Sentinel-2 NDVI for vegetation distribution

Both datasets were filtered for Manhattan during peak summer (June–August 2018).

---

## Key Findings

### 1. Land Surface Temperature (LST)

* Minimum: ~10.3°C
* Mean: ~30.7°C
* Maximum: ~49.2°C

These values indicate strong urban heat island conditions, with extreme hotspots likely associated with dense built-up areas such as commercial zones and transportation infrastructure.

---

### 2. Vegetation (NDVI)

* Minimum: ~-0.27
* Mean: ~0.09
* Maximum: ~0.69

NDVI values suggest that Manhattan has generally low vegetation coverage, with high NDVI values limited to specific areas such as Central Park and smaller green spaces.

---

### 3. Relationship Between LST and NDVI

A clear inverse relationship is observed:

* Areas with low NDVI correspond to high LST
* Areas with high NDVI correspond to lower LST

This supports the hypothesis that vegetation plays a significant role in reducing surface temperatures in urban environments.

---

## Data Limitations

* LST represents surface temperature, not human thermal comfort
* NDVI is a proxy for vegetation and does not capture canopy density or shading effects
* Temporal scope is limited to summer 2018 and does not represent long-term trends
* Satellite revisit cycles and cloud filtering may introduce sampling bias
* Spatial resolution differences (Landsat ~30m vs Sentinel ~10m) may affect alignment

---

## Data Fitness for Purpose

Despite limitations, the datasets are suitable for:

* Identifying relative heat hotspots
* Comparing vegetation influence on surface temperature
* Supporting prioritisation of heat mitigation zones

They are not suitable for:

* Detailed microclimate analysis
* Direct human thermal comfort assessment

---

## Conclusion

The datasets provide a reliable basis for identifying high-risk heat zones in Manhattan and understanding the role of vegetation in mitigating urban heat, with clearly defined limitations that must be considered in interpretation.
