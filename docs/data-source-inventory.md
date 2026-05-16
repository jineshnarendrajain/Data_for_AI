# Data Source Inventory

---

## 1. Landsat 8 Collection 2 Level 2 Surface Temperature

* **Provider:** NASA / USGS
* **Access method:** Google Earth Engine / USGS EarthExplorer
* **Category:** remote-sensing-thermal

### Rubric scoring (0–2 per axis)

| Axis               | Score     | Justification                                                                         |
| ------------------ | --------- | ------------------------------------------------------------------------------------- |
| Provenance         | 2         | Produced by NASA/USGS and widely used in peer-reviewed environmental research         |
| Resolution match   | 2         | ~30m thermal resolution is appropriate for neighbourhood-scale thermal analysis       |
| Coverage           | 2         | Full global coverage with regular revisit intervals                                   |
| License            | 2         | Public domain and openly accessible                                                   |
| Access reliability | 2         | Stable access through USGS and Google Earth Engine                                    |
| Bias clarity       | 1         | Known limitations include cloud contamination and surface-vs-air temperature mismatch |
| Maintenance        | 2         | Continuously maintained and updated                                                   |
| **TOTAL**          | **13/14** |                                                                                       |

### One-paragraph description

Landsat 8 Collection 2 Level 2 provides satellite-derived Land Surface Temperature (LST) measurements derived from thermal infrared imagery. Each instance represents a satellite acquisition over a geographic area at a specific timestamp, enabling spatial analysis of urban surface thermal variation. The dataset is appropriate for identifying neighbourhood-scale urban thermal hotspots but is limited by revisit frequency (~16 days), cloud contamination, and moderate spatial resolution.

### Verdict

**Adopt** — Primary dataset used for identifying and analysing urban thermal hotspots across Manhattan.

---

## 2. Sentinel-2 Surface Reflectance NDVI

* **Provider:** European Space Agency (ESA)
* **Access method:** Google Earth Engine / Copernicus Open Access Hub
* **Category:** remote-sensing-optical

### Rubric scoring

| Axis               | Score     | Justification                                                             |
| ------------------ | --------- | ------------------------------------------------------------------------- |
| Provenance         | 2         | Produced by ESA and widely used in environmental and urban analysis       |
| Resolution match   | 2         | 10m resolution is appropriate for neighbourhood-scale vegetation analysis |
| Coverage           | 2         | Global coverage with frequent revisit intervals                           |
| License            | 2         | Open access through the Copernicus programme                              |
| Access reliability | 2         | Stable access through official portals and Google Earth Engine            |
| Bias clarity       | 1         | NDVI is a proxy metric with known limitations and seasonal sensitivity    |
| Maintenance        | 2         | Continuously maintained and updated                                       |
| **TOTAL**          | **13/14** |                                                                           |

### One-paragraph description

Sentinel-2 provides high-resolution multispectral optical imagery from which the Normalized Difference Vegetation Index (NDVI) can be calculated using red and near-infrared bands. NDVI acts as a proxy for vegetation presence and density and is useful for contextualising spatial variation in urban surface temperature. While it does not directly measure cooling performance or human thermal comfort, it serves as an interpretable explanatory environmental variable.

### Verdict

**Adopt** — Secondary dataset used to analyse the relationship between vegetation density and observed land surface temperature variation.

---

## 3. NYC Heat Vulnerability Index

* **Provider:** NYC Department of Health
* **Access method:** NYC Open Data portal
* **Category:** built-environment

### Rubric scoring

| Axis               | Score     | Justification                                                                |
| ------------------ | --------- | ---------------------------------------------------------------------------- |
| Provenance         | 2         | Produced by a government agency for policy and planning purposes             |
| Resolution match   | 1         | Aggregated at neighbourhood scale and coarser than satellite raster analysis |
| Coverage           | 2         | Covers all New York City boroughs                                            |
| License            | 2         | Publicly accessible through NYC Open Data                                    |
| Access reliability | 2         | Stable and well-documented access portal                                     |
| Bias clarity       | 1         | Combines multiple indicators using non-transparent weighting methodologies   |
| Maintenance        | 1         | Updated periodically but not continuously                                    |
| **TOTAL**          | **11/14** |                                                                              |

### One-paragraph description

The NYC Heat Vulnerability Index (HVI) combines socio-economic, environmental, and public health indicators to identify communities vulnerable to extreme heat exposure. While it does not directly measure land surface temperature, it provides an external contextual reference useful for validating and interpreting observed hotspot patterns derived from satellite imagery.

### Verdict

**Adopt** — Validation and contextual reference dataset for comparing identified hotspot zones with known heat-vulnerable areas.

---

## 4. ERA5 Climate Reanalysis Data

* **Provider:** ECMWF
* **Access method:** Copernicus Climate Data Store
* **Category:** climate-reanalysis

### Rubric scoring

| Axis               | Score     | Justification                                                   |
| ------------------ | --------- | --------------------------------------------------------------- |
| Provenance         | 2         | Produced by ECMWF and widely used in climate science            |
| Resolution match   | 0         | ~30km resolution is too coarse for neighbourhood-scale analysis |
| Coverage           | 2         | Continuous global temporal coverage                             |
| License            | 2         | Open access through Copernicus                                  |
| Access reliability | 2         | Stable APIs and official distribution channels                  |
| Bias clarity       | 1         | Model-based assumptions introduce complex uncertainties         |
| Maintenance        | 2         | Continuously maintained                                         |
| **TOTAL**          | **11/14** |                                                                 |

### One-paragraph description

ERA5 is a global climate reanalysis dataset providing atmospheric variables such as air temperature, humidity, and wind at coarse spatial resolution. Although useful for regional climate studies, its spatial granularity is insufficient for neighbourhood-scale urban thermal hotspot mapping and therefore does not align with the primary analytical requirements of this project.

### Verdict

**Reject** — Spatial resolution is too coarse for the project’s neighbourhood-scale thermal analysis goals.

---

## 5. OpenStreetMap (Built Environment Data)

* **Provider:** OpenStreetMap contributors
* **Access method:** Overpass API / Geofabrik downloads
* **Category:** built-environment

### Rubric scoring

| Axis               | Score     | Justification                                                      |
| ------------------ | --------- | ------------------------------------------------------------------ |
| Provenance         | 1         | Community-generated dataset with variable completeness and quality |
| Resolution match   | 2         | High spatial detail including roads and building footprints        |
| Coverage           | 2         | Broad global geographic coverage                                   |
| License            | 1         | Open license with attribution and share-alike requirements         |
| Access reliability | 1         | API reliability and extraction consistency can vary                |
| Bias clarity       | 1         | Coverage quality depends on contributor activity                   |
| Maintenance        | 2         | Continuously updated by the community                              |
| **TOTAL**          | **10/14** |                                                                    |

### One-paragraph description

OpenStreetMap provides detailed geospatial representations of buildings, roads, and urban infrastructure contributed by a global volunteer community. The dataset could potentially support future analysis of urban morphology or impervious surface characteristics, but additional preprocessing and validation would be required before analytical integration.

### Verdict

**Investigate further** — Potential future auxiliary dataset but not required for the current analytical pipeline.

---

## Summary

### Adopted datasets

* Landsat 8 Surface Temperature (Primary analytical dataset)
* Sentinel-2 NDVI (Secondary contextual dataset)
* NYC Heat Vulnerability Index (Validation/reference dataset)

### Rejected datasets

* ERA5 Climate Reanalysis Data — insufficient spatial resolution for neighbourhood-scale analysis

### Under investigation

* OpenStreetMap — potentially useful for future urban morphology analysis

### Coverage gaps

* No direct measurement of human thermal comfort variables such as humidity, wind, or radiation exposure
* Satellite revisit intervals and cloud contamination introduce temporal inconsistencies
* Moderate spatial resolution limits street-level interpretation
