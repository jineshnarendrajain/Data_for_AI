# Dataset Datasheet — Sentinel-2 Surface Reflectance NDVI Dataset

> One datasheet per adopted dataset. Save as `docs/datasheets/sentinel2-ndvi.md` in
> your repo. Based on Gebru et al. 2021, "Datasheets for Datasets."
>
> The datasheet is a contract: *this is what this data is, this is what it
> can do, this is what it cannot do.* Future-you and your reviewers will
> thank present-you.

---

## 0. Quick reference

- **Dataset name:** Sentinel-2 Surface Reflectance (COPERNICUS/S2_SR)
- **Version / vintage:** Summer 2018 subset
- **Source URL:** https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR
- **License:** Copernicus Open Access License
- **Spatial coverage:** Manhattan, New York City, USA
- **Temporal coverage:** 2018-06-01 to 2018-08-31
- **Native resolution (spatial / temporal):** 10 m spatial resolution, 5-day revisit cycle
- **Format:** Earth Engine raster imagery / GeoTIFF compatible
- **Size:** Approx. several TB globally; project subset <1 GB
- **Datasheet last updated:** 2026-05-13

---

## 1. Motivation

*Why does this dataset exist? Who created it? What was it built for?*

- **Why was the dataset created?**

  The dataset was created to provide high-resolution multispectral Earth observation imagery for vegetation analysis, land monitoring, environmental assessment, and climate-related studies.

- **Who created the dataset (individuals, organizations)?**

  The dataset was created and maintained by the European Space Agency (ESA) under the Copernicus Programme.

- **Who funded the creation of the dataset?**

  The European Union through the Copernicus Earth observation programme.

- **For what tasks was the dataset originally intended?**

  Vegetation monitoring, land cover mapping, agriculture studies, ecological monitoring, and environmental analysis.

---

## 2. Composition

*What does the dataset contain? At what unit? What's missing?*

- **What does an instance represent?**

  A single multispectral satellite image scene containing reflectance bands for a specific timestamp and geographic region.

- **How many instances are there in total?**

  The project used multiple Sentinel-2 scenes collected during Summer 2018 over Manhattan.

- **What features / fields does each instance have?**

| Field | Type | Description | Required? |
|---|---|---|---|
| B4 | Float Raster | Red spectral band used in NDVI calculation | Yes |
| B8 | Float Raster | Near Infrared spectral band used in NDVI calculation | Yes |
| SCL | Integer Raster | Scene classification layer for cloud masking | Yes |
| system:time_start | Timestamp | Acquisition date and time | Yes |

- **Are there labels or targets associated with each instance?**

  No explicit labels or target variables are associated with the dataset.

- **Is any information missing from instances?**

  Cloud-covered pixels, atmospheric disturbances, and shadows may obscure portions of the imagery.

- **Are there relationships between individual instances?**

  Yes. Images are temporally sequential and spatially overlapping.

- **Are there recommended data splits (train/val/test)?**

  No official train/validation/test splits are provided because this is not a benchmark machine learning dataset.

---

## 3. Collection process

*How was the data acquired? By whom? When? Is the sample representative?*

- **How was the data acquired?**

  Remote sensing through multispectral satellite imaging.

- **What instruments / sensors / software were used?**

  Sentinel-2 MultiSpectral Instrument (MSI).

- **Who was involved in the data collection process?**

  Automated satellite acquisition systems operated by ESA and the Copernicus Programme.

- **Over what time period was the data collected?**

  Summer 2018 for the subset used in this project.

- **What was the sampling strategy?**

  Deterministic Earth observation with continuous global revisit coverage.

- **Is the sample representative of the larger population it claims to describe?**

  The dataset reasonably represents vegetation conditions during Summer 2018 but may not reflect long-term seasonal variability.

- **Were any ethical review processes conducted?**

  Not applicable because the dataset contains no human subject or personal information.

---

## 4. Preprocessing & cleaning

*What was done to the data before you got it? What did you do?*

- **What preprocessing was done by the dataset creators?**

  Atmospheric correction, radiometric calibration, geometric correction, and generation of surface reflectance products.

- **Is the raw data also available?**

  Yes.

- **What preprocessing did WE do before adopting the dataset?**

  Cloud masking using the Scene Classification Layer (SCL), spatial clipping to Manhattan, NDVI calculation using B8 and B4 bands, and temporal median compositing.

- **Where is the preprocessing software / code available?**

  Python notebook using Google Earth Engine API and Geemap.

---

## 5. Uses

*What's this dataset good for? What's it NOT good for?*

- **What tasks has the dataset been used for?**

  NDVI analysis, vegetation monitoring, urban ecological studies, land cover analysis, and environmental monitoring.

- **Is there a repository linking to papers / systems that use this dataset?**

  Yes. ESA Copernicus documentation and Google Earth Engine repositories provide references and implementations.

- **What other tasks could this dataset be used for?**

  Biodiversity analysis, agricultural monitoring, urban greening studies, and AI-based environmental prediction.

- **What tasks should this dataset NOT be used for?**

  1. Should not be used for identifying individual trees or micro-scale vegetation structures due to the 10 m spatial resolution limitation.
  2. Should not be used for real-time vegetation monitoring because revisit intervals and cloud contamination introduce delays.

- **Are there any considerations about discrimination, bias, or harm that could result from use of this dataset?**

  Vegetation distribution analysis may oversimplify socioeconomic inequalities if interpreted without demographic or urban policy context.

---

## 6. Distribution & licensing

- **Under what license is the dataset distributed?**

  Copernicus Open Access License.

- **Are there any restrictions on use, redistribution, attribution, or modification?**

  Open for research and educational use with attribution requirements.

- **What's the required attribution string?**

  "Contains modified Copernicus Sentinel data processed by ESA."

- **Are there fees for access?**

  No.

- **Are there export controls or regulatory restrictions?**

  None known for academic or research use.

---

## 7. Maintenance

- **Who supports / hosts / maintains the dataset?**

  European Space Agency (ESA) and the Copernicus Programme.

- **How can the maintainer be contacted?**

  Through official ESA Copernicus support portals.

- **Is there an erratum?**

  Periodic calibration and processing updates are published.

- **Will the dataset be updated?**

  Yes.

- **How often is the dataset updated?**

  Continuously with new satellite acquisitions.

- **Are older versions of the dataset still available?**

  Yes.

---

## 8. Limitations relative to OUR project

*The most important section for the seminar. How does this dataset's
character intersect with our problem brief?*

- **Resolution mismatch with our decision unit?**

  The 10 m spatial resolution may not capture micro-scale vegetation variations at the building or street level.

- **Geographic gaps that matter for us?**

  The dataset only captures Manhattan and excludes broader ecological interactions from adjacent boroughs.

- **Temporal gaps that matter for us?**

  The project only uses Summer 2018 imagery and does not capture yearly or seasonal vegetation change trends.

- **Biases that could distort our conclusions?**

  Cloud masking and median compositing may suppress temporary vegetation stress or seasonal anomalies.

- **What additional sources would compensate for these limits?**

  LiDAR vegetation datasets, local tree inventory datasets, high-resolution aerial imagery, and field survey data.

- **Verdict for our project:****

  Secondary dataset.
