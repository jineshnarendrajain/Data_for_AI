# Dataset Datasheet — Landsat 8 Collection 2 Level 2 Land Surface Temperature (LST)

> One datasheet per adopted dataset. Save as `docs/datasheets/landsat8-lst.md` in
> your repo. Based on Gebru et al. 2021, "Datasheets for Datasets."

---

## 0. Quick reference

- **Dataset name:** Landsat 8 Collection 2 Tier 1 Level 2
- **Version / vintage:** Collection 2, Summer 2018 subset
- **Source URL:** https://www.usgs.gov/landsat-missions/landsat-collection-2
- **License:** Public domain
- **Spatial coverage:** Manhattan, New York City, USA
- **Temporal coverage:** 2018-06-01 to 2018-08-31
- **Native resolution (spatial / temporal):** 30 m spatial resolution, 16-day revisit cycle
- **Format:** Earth Engine raster imagery / GeoTIFF compatible
- **Size:** Approx. several GB globally; project subset <500 MB
- **Datasheet last updated:** 2026-05-13 

---

## 1. Motivation

*Why does this dataset exist? Who created it? What was it built for?*

- **Why was the dataset created?**

  The dataset was created to provide calibrated multispectral and thermal Earth observation imagery for environmental monitoring, climate analysis, land cover analysis, and urban thermal studies.

- **Who created the dataset (individuals, organizations)?**

  The dataset was created jointly by NASA and the United States Geological Survey (USGS).

- **Who funded the creation of the dataset?**

  The United States federal government through NASA and USGS programs.

- **For what tasks was the dataset originally intended?**

  Environmental monitoring, thermal mapping, vegetation analysis, land use analysis, and climate research.

---

## 2. Composition

*What does the dataset contain? At what unit? What's missing?*

- **What does an instance represent?**

  A single satellite image scene containing multispectral and thermal raster bands for a specific timestamp and geographic region.

- **How many instances are there in total?**

  The project used multiple Landsat scenes between June and August 2018 over Manhattan.

- **What features / fields does each instance have?**

| Field | Type | Description | Required? |
|---|---|---|---|
| ST_B10 | Float Raster | Surface temperature thermal band | Yes |
| system:time_start | Timestamp | Acquisition date and time | Yes |
| CLOUD_COVER | Float | Percentage cloud cover metadata | Yes |

- **Are there labels or targets associated with each instance?**

  No explicit labels or targets are included. The dataset is observational remote sensing imagery.

- **Is any information missing from instances?**

  Some pixels may be obscured due to cloud contamination, atmospheric interference, or sensor artifacts.

- **Are there relationships between individual instances?**

  Yes. Instances are temporally sequential and spatially overlapping.

- **Are there recommended data splits (train/val/test)?**

  No official train/validation/test splits are provided because this is not a benchmark machine learning dataset.

---

## 3. Collection process

*How was the data acquired? By whom? When? Is the sample representative?*

- **How was the data acquired?**

  Remote sensing through satellite-based thermal and multispectral imaging.

- **What instruments / sensors / software were used?**

  Landsat 8 Operational Land Imager (OLI) and Thermal Infrared Sensor (TIRS).

- **Who was involved in the data collection process?**

  Automated satellite acquisition systems managed by NASA and USGS.

- **Over what time period was the data collected?**

  Summer 2018 for the subset used in this project.

- **What was the sampling strategy?**

  Deterministic Earth observation with regular global coverage intervals.

- **Is the sample representative of the larger population it claims to describe?**

  The dataset reasonably represents summer land surface temperature conditions in Manhattan but does not represent yearly or seasonal variability.

- **Were any ethical review processes conducted?**

  Not applicable because the dataset contains no personal or human subject data.

---

## 4. Preprocessing & cleaning

*What was done to the data before you got it? What did you do?*

- **What preprocessing was done by the dataset creators?**

  Radiometric calibration, atmospheric correction, geometric correction, and Level 2 surface temperature derivation.

- **Is the raw data also available?**

  Yes.

- **What preprocessing did WE do before adopting the dataset?**

  Cloud filtering, spatial clipping to Manhattan, conversion of thermal band values to Celsius, and temporal averaging.

- **Where is the preprocessing software / code available?**

  Python notebook using Google Earth Engine API and Geemap.

---

## 5. Uses

*What's this dataset good for? What's it NOT good for?*

- **What tasks has the dataset been used for?**

  Urban heat island analysis, climate studies, land surface temperature mapping, and environmental monitoring.

- **Is there a repository linking to papers / systems that use this dataset?**

  Yes. Documentation and examples are available through USGS and Google Earth Engine repositories.

- **What other tasks could this dataset be used for?**

  Urban planning, ecological analysis, climate adaptation studies, and AI-based environmental prediction.

- **What tasks should this dataset NOT be used for?**

  1. Should not be used for indoor temperature estimation because measurements represent outdoor land surface temperature only.
  2. Should not be used for fine-scale pedestrian thermal comfort analysis due to the 30 m spatial resolution limitation.

- **Are there any considerations about discrimination, bias, or harm that could result from use of this dataset?**

  Urban thermal interpretations may overgeneralize vulnerable communities if combined with incomplete demographic or socioeconomic datasets.

---

## 6. Distribution & licensing

- **Under what license is the dataset distributed?**

  Public domain.

- **Are there any restrictions on use, redistribution, attribution, or modification?**

  No major restrictions for academic or research use.

- **What's the required attribution string?**

  "Landsat-8 imagery courtesy of the U.S. Geological Survey."

- **Are there fees for access?**

  No.

- **Are there export controls or regulatory restrictions?**

  None known for public research use.

---

## 7. Maintenance

- **Who supports / hosts / maintains the dataset?**

  USGS and NASA.

- **How can the maintainer be contacted?**

  Through official USGS Landsat support portals.

- **Is there an erratum?**

  Periodic calibration updates and corrections are published by USGS.

- **Will the dataset be updated?**

  Yes.

- **How often is the dataset updated?**

  Continuously as new satellite acquisitions are processed.

- **Are older versions of the dataset still available?**

  Yes.

---

## 8. Limitations relative to OUR project

*The most important section for the seminar. How does this dataset's
character intersect with our problem brief?*

- **Resolution mismatch with our decision unit?**

  The 30 m spatial resolution may miss micro-scale urban heat variations between individual streets and buildings.

- **Geographic gaps that matter for us?**

  The dataset captures only Manhattan and excludes broader metropolitan heat interactions.

- **Temporal gaps that matter for us?**

  The study only uses Summer 2018 data and does not capture long-term or seasonal change patterns.

- **Biases that could distort our conclusions?**

  Cloud filtering and seasonal averaging may suppress short-duration extreme heat events.

- **What additional sources would compensate for these limits?**

  Higher-resolution thermal imagery, local weather station data, LiDAR datasets, and socioeconomic datasets.

- **Verdict for our project:**

  Primary dataset.
