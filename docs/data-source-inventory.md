# Data Source Inventory

---

## 1. Landsat 8/9 Surface Temperature (Collection 2)

* **Provider:** NASA / USGS
* **Access method:** https://earthexplorer.usgs.gov/ or Google Earth Engine
* **Category:** remote-sensing-thermal

### Rubric scoring (0–2 per axis)

| Axis               | Score     | Justification                                                                 |
| ------------------ | --------- | ----------------------------------------------------------------------------- |
| Provenance         | 2         | Produced by NASA/USGS, widely used in peer-reviewed research                  |
| Resolution match   | 2         | ~30–100m resolution aligns with neighbourhood/block-scale analysis            |
| Coverage           | 2         | Full global coverage with long historical archive (1980s–present)             |
| License            | 2         | Publicly available, open access                                               |
| Access reliability | 2         | Stable via USGS and Google Earth Engine                                       |
| Bias clarity       | 1         | Known limitations (cloud cover, surface vs air temp) but not fully quantified |
| Maintenance        | 2         | Actively maintained and updated                                               |
| **TOTAL**          | **13/14** |                                                                               |

### One-paragraph description

Landsat 8/9 Collection 2 Surface Temperature provides satellite-derived land surface temperature (LST) measurements using thermal infrared bands at approximately 30–100m resolution. Each instance represents a satellite scene captured at a specific time, enabling spatial and temporal analysis of surface heat patterns. The dataset is suitable for urban heat island studies and long-term trend analysis but is limited by revisit frequency (~16 days) and sensitivity to cloud cover.

### Verdict

**Adopt** — Primary dataset for measuring land surface temperature and identifying heat hotspots.

---

## 2. Sentinel-2 NDVI (Vegetation Index)

* **Provider:** European Space Agency (ESA)
* **Access method:** Google Earth Engine or Copernicus Open Access Hub
* **Category:** remote-sensing-optical

### Rubric scoring

| Axis               | Score     | Justification                                                                        |
| ------------------ | --------- | ------------------------------------------------------------------------------------ |
| Provenance         | 2         | Produced by ESA, widely used in environmental and urban studies                      |
| Resolution match   | 2         | 10m resolution exceeds required spatial detail for block-level analysis              |
| Coverage           | 2         | Global coverage with frequent revisit (~5 days)                                      |
| License            | 2         | Open access via Copernicus program                                                   |
| Access reliability | 2         | Stable via Google Earth Engine and official portals                                  |
| Bias clarity       | 1         | NDVI limitations (e.g., saturation, proxy nature) are known but not fully quantified |
| Maintenance        | 2         | Actively maintained and updated                                                      |
| **TOTAL**          | **13/14** |                                                                                      |

### One-paragraph description

Sentinel-2 provides high-resolution optical imagery from which the Normalized Difference Vegetation Index (NDVI) can be derived using red and near-infrared bands. NDVI serves as a proxy for vegetation presence and density at 10m resolution, making it suitable for analysing green cover variation at the street-block scale. While it does not directly measure cooling or shading effects, it is a strong explanatory variable for surface temperature differences.

### Verdict

**Adopt** — Secondary dataset used to explain variation in LST and assess the influence of green cover.

---

## 3. NYC Heat Vulnerability Index

* **Provider:** NYC Department of Health
* **Access method:** NYC Open Data portal
* **Category:** built-environment

### Rubric scoring

| Axis               | Score     | Justification                                                               |
| ------------------ | --------- | --------------------------------------------------------------------------- |
| Provenance         | 2         | Produced by a government agency for policy and planning use                 |
| Resolution match   | 1         | Aggregated at neighbourhood level, coarser than block-scale analysis        |
| Coverage           | 2         | Full coverage of New York City                                              |
| License            | 2         | Publicly available via NYC Open Data                                        |
| Access reliability | 2         | Stable and well-documented portal                                           |
| Bias clarity       | 1         | Combines multiple socio-environmental variables; bias not fully transparent |
| Maintenance        | 1         | Updated periodically but not at high frequency                              |
| **TOTAL**          | **11/14** |                                                                             |

### One-paragraph description

The NYC Heat Vulnerability Index (HVI) combines socio-economic, environmental, and health-related indicators to identify populations most at risk from extreme heat. It is typically aggregated at neighbourhood or census tract level and is widely used in policy-making. While it does not directly measure temperature, it provides a valuable reference layer for validating and contextualising heat exposure patterns identified through satellite data.

### Verdict

**Adopt** — Used as a validation and contextual dataset to compare identified hotspots with known vulnerable areas.

---

## 4. ERA5 Climate Reanalysis Data

* **Provider:** ECMWF
* **Access method:** Copernicus Climate Data Store
* **Category:** climate-reanalysis

### Rubric scoring

| Axis               | Score     | Justification                                                |
| ------------------ | --------- | ------------------------------------------------------------ |
| Provenance         | 2         | Produced by ECMWF, widely used in climate science            |
| Resolution match   | 0         | ~30km resolution too coarse for neighbourhood/block analysis |
| Coverage           | 2         | Global and continuous temporal coverage                      |
| License            | 2         | Open access via Copernicus                                   |
| Access reliability | 2         | Stable API and download system                               |
| Bias clarity       | 1         | Known modelling assumptions but complex                      |
| Maintenance        | 2         | Actively maintained                                          |
| **TOTAL**          | **11/14** |                                                              |

### One-paragraph description

ERA5 is a global climate reanalysis dataset providing hourly estimates of atmospheric variables such as air temperature, humidity, and wind at coarse spatial resolution (~30km). While useful for large-scale climate analysis, its resolution is insufficient for urban-scale heat mapping and does not align with the spatial granularity required for this project.

### Verdict

**Reject** — Resolution too coarse for neighbourhood or block-level decision-making.

---

## 5. OpenStreetMap (Built Environment Data)

* **Provider:** OpenStreetMap contributors
* **Access method:** Overpass API / Geofabrik downloads
* **Category:** built-environment

### Rubric scoring

| Axis               | Score     | Justification                                            |
| ------------------ | --------- | -------------------------------------------------------- |
| Provenance         | 1         | Community-generated dataset with variable quality        |
| Resolution match   | 2         | High spatial detail (building footprints, roads)         |
| Coverage           | 2         | Full global coverage                                     |
| License            | 1         | Open but requires attribution and share-alike            |
| Access reliability | 1         | API can be unstable; data extraction can be inconsistent |
| Bias clarity       | 1         | Coverage varies by area and contributor density          |
| Maintenance        | 2         | Continuously updated by community                        |
| **TOTAL**          | **10/14** |                                                          |

### One-paragraph description

OpenStreetMap provides detailed geospatial data on buildings, roads, and land use contributed by a global community. It can be used to derive indicators such as building density or impervious surface coverage. However, data quality and completeness vary, and preprocessing effort is required to make it analytically useful.

### Verdict

**Investigate further** — Potential auxiliary dataset for future analysis but not required for core pipeline.

---

## Summary

* **Adopted:**

  * Landsat Surface Temperature (Primary)
  * Sentinel-2 NDVI (Secondary)
  * NYC Heat Vulnerability Index (Validation)

* **Rejected:**

  * ERA5 Climate Data — resolution too coarse for urban-scale analysis

* **Under investigation:**

  * OpenStreetMap — useful but not essential for current scope

* **Coverage gaps:**

  * No direct measurement of human thermal comfort (humidity, wind, shading not included)
  * Temporal gaps due to satellite revisit cycles and cloud cover
