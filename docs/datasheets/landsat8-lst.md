# Dataset Datasheet — Landsat 8 Collection 2 Level 2 Land Surface Temperature (LST)

> One datasheet per adopted dataset. Save as `docs/datasheets/landsat8-lst.md` in
> your repo. Based on Gebru et al. 2021, "Datasheets for Datasets."

---

## 0. Quick reference

* **Dataset name:** Landsat 8 Collection 2 Tier 1 Level 2
* **Version / vintage:** Summer 2018 subset used for project analysis
* **Source URL:** https://www.usgs.gov/landsat-missions/landsat-collection-2
* **License:** Public domain
* **Spatial coverage:** Manhattan, New York City, USA
* **Temporal coverage:** 2018-06-01 to 2018-08-31
* **Native resolution (spatial / temporal):** 30 m spatial resolution, ~16-day revisit cycle
* **Format:** Earth Engine raster imagery / GeoTIFF-compatible raster data
* **Size:** Global archive several TB; project subset <500 MB
* **Datasheet last updated:** 2026-05-13 by Jinesh Narendra Jain

---

## 1. Motivation

### Why was the dataset created?

The dataset was created to provide calibrated multispectral and thermal Earth observation imagery for environmental monitoring, land cover analysis, climate studies, and surface temperature analysis.

### Who created the dataset (individuals, organizations)?

The dataset was created and maintained jointly by NASA and the United States Geological Survey (USGS).

### Who funded the creation of the dataset?

The United States federal government through NASA and USGS Earth observation programs.

### For what tasks was the dataset originally intended?

* Land surface temperature analysis
* Environmental monitoring
* Climate and ecological studies
* Land cover classification
* Agricultural and urban analysis
* Long-term Earth observation

---

## 2. Composition

### What does an instance represent?

A single satellite image scene containing thermal and multispectral raster bands for a specific geographic region and timestamp.

### How many instances are there in total?

The project uses multiple Landsat scenes covering Manhattan during Summer 2018.

### What features / fields does each instance have?

| Field             | Type         | Description                      | Required? |
| ----------------- | ------------ | -------------------------------- | --------- |
| ST_B10            | Float Raster | Surface temperature thermal band | Yes       |
| system:time_start | Timestamp    | Acquisition date and time        | Yes       |
| CLOUD_COVER       | Float        | Cloud cover metadata percentage  | Yes       |

### Are there labels or targets associated with each instance?

No. The dataset is observational remote sensing imagery without predefined labels or targets.

### Is any information missing from instances?

Yes. Some pixels may be obscured due to:

* Cloud contamination
* Atmospheric interference
* Sensor artifacts
* Missing thermal retrievals

### Are there relationships between individual instances?

Yes. Instances are spatially overlapping and temporally sequential, enabling time-series analysis and compositing.

### Are there recommended data splits (train/val/test)?

No official train/validation/test splits exist because the dataset was not designed as a benchmark machine learning dataset.

---

## 3. Collection process

### How was the data acquired?

Remote sensing through satellite-based thermal and multispectral imaging.

### What instruments / sensors / software were used?

* Landsat 8 Operational Land Imager (OLI)
* Thermal Infrared Sensor (TIRS)

### Who was involved in the data collection process?

Automated satellite acquisition systems operated by NASA and USGS.

### Over what time period was the data collected?

The project subset covers June–August 2018.

### What was the sampling strategy?

Deterministic global Earth observation with regular revisit intervals.

### Is the sample representative of the larger population it claims to describe?

The dataset reasonably represents summer surface temperature conditions across Manhattan but does not represent:

* Full yearly climate variation
* Indoor conditions
* Fine-scale pedestrian thermal conditions

### Were any ethical review processes conducted?

Not applicable because the dataset contains no personal or human subject data.

---

## 4. Preprocessing & cleaning

### What preprocessing was done by the dataset creators?

* Radiometric calibration
* Atmospheric correction
* Geometric correction
* Surface temperature derivation
* Quality masking

### Is the raw data also available?

Yes.

### What preprocessing did WE do before adopting the dataset?

* Spatial clipping to Manhattan
* Summer-period temporal filtering
* Cloud-cover filtering
* Conversion of thermal band values into degrees Celsius
* Temporal mean compositing

### Where is the preprocessing software / code available?

Python notebooks using:

* Google Earth Engine API
* Geemap
* Pandas
* NumPy

---

## 5. Uses

### What tasks has the dataset been used for?

* Urban heat island analysis
* Environmental monitoring
* Climate research
* Land surface temperature mapping
* Urban planning analysis

### Is there a repository linking to papers / systems that use this dataset?

Yes. Documentation and research examples are available through:

* USGS Landsat documentation
* Google Earth Engine examples
* Peer-reviewed urban climate studies

### What other tasks could this dataset be used for?

* Ecological monitoring
* Land cover analysis
* Climate adaptation studies
* Environmental AI workflows
* Change detection analysis

### What tasks should this dataset NOT be used for?

1. Should not be used for direct human thermal comfort estimation because Land Surface Temperature does not account for humidity, wind, or radiation exposure.

2. Should not be used for precise street-level or building-level thermal analysis because the spatial resolution is insufficient for microclimate interpretation.

### Are there any considerations about discrimination, bias, or harm that could result from use of this dataset?

Urban heat interpretations may oversimplify social vulnerability if environmental indicators are interpreted without broader socioeconomic context.

---

## 6. Distribution & licensing

### Under what license is the dataset distributed?

Public domain.

### Are there any restrictions on use, redistribution, attribution, or modification?

No major restrictions for research or educational use.

### What's the required attribution string?

“Landsat-8 imagery courtesy of the U.S. Geological Survey.”

### Are there fees for access?

No.

### Are there export controls or regulatory restrictions?

None known for public research use.

---

## 7. Maintenance

### Who supports / hosts / maintains the dataset?

NASA and USGS.

### How can the maintainer be contacted?

Through official USGS Landsat support portals.

### Is there an erratum?

Periodic calibration updates and corrections are published by USGS.

### Will the dataset be updated?

Yes.

### How often is the dataset updated?

Continuously as new acquisitions are processed.

### Are older versions of the dataset still available?

Yes.

---

## 8. Limitations relative to OUR project

### Resolution mismatch with our decision unit?

The 30 m spatial resolution limits interpretation at exact street or building scale. Results are more appropriate for neighbourhood-scale hotspot analysis.

### Geographic gaps that matter for us?

The project focuses only on Manhattan and does not capture thermal interactions with surrounding boroughs.

### Temporal gaps that matter for us?

The analysis only uses Summer 2018 imagery and does not represent long-term or seasonal variability.

### Biases that could distort our conclusions?

* Cloud filtering may suppress extreme heat events
* Surface temperature differs from air temperature
* Temporal compositing may smooth short-duration anomalies

### What additional sources would compensate for these limits?

* Local weather station data
* LiDAR datasets
* High-resolution aerial imagery
* Socioeconomic vulnerability datasets
* Urban morphology datasets

### Verdict for our project

Primary dataset used for identifying relative urban heat exposure patterns across Manhattan.
