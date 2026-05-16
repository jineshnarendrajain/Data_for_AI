# Dataset Datasheet — Sentinel-2 Surface Reflectance NDVI Dataset

> One datasheet per adopted dataset. Save as `docs/datasheets/sentinel2-ndvi.md` in
> your repo. Based on Gebru et al. 2021, "Datasheets for Datasets."

---

## 0. Quick reference

* **Dataset name:** Sentinel-2 Surface Reflectance (COPERNICUS/S2_SR)
* **Version / vintage:** Summer 2018 subset used for project analysis
* **Source URL:** https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR
* **License:** Copernicus Open Access License
* **Spatial coverage:** Manhattan, New York City, USA
* **Temporal coverage:** 2018-06-01 to 2018-08-31
* **Native resolution (spatial / temporal):** 10 m spatial resolution, ~5-day revisit cycle
* **Format:** Earth Engine raster imagery / GeoTIFF-compatible raster data
* **Size:** Global archive several TB; project subset <1 GB
* **Datasheet last updated:** 2026-05-13 by Jinesh Narendra Jain

---

## 1. Motivation

### Why was the dataset created?

The dataset was created to provide high-resolution multispectral Earth observation imagery for vegetation monitoring, environmental assessment, land cover analysis, and ecological studies.

### Who created the dataset (individuals, organizations)?

The dataset was created and maintained by the European Space Agency (ESA) under the Copernicus Programme.

### Who funded the creation of the dataset?

The European Union through the Copernicus Earth observation programme.

### For what tasks was the dataset originally intended?

* Vegetation monitoring
* Land cover analysis
* Ecological assessment
* Agricultural monitoring
* Environmental change detection
* Urban environmental analysis

---

## 2. Composition

### What does an instance represent?

A single multispectral satellite image scene containing optical reflectance bands for a specific geographic region and timestamp.

### How many instances are there in total?

The project uses multiple Sentinel-2 scenes covering Manhattan during Summer 2018.

### What features / fields does each instance have?

| Field             | Type           | Description                                           | Required? |
| ----------------- | -------------- | ----------------------------------------------------- | --------- |
| B4                | Float Raster   | Red spectral band used for NDVI calculation           | Yes       |
| B8                | Float Raster   | Near Infrared spectral band used for NDVI calculation | Yes       |
| SCL               | Integer Raster | Scene Classification Layer used for cloud masking     | Yes       |
| system:time_start | Timestamp      | Acquisition date and time                             | Yes       |

### Are there labels or targets associated with each instance?

No. The dataset is observational multispectral satellite imagery without predefined labels.

### Is any information missing from instances?

Yes. Some pixels may be affected by:

* Cloud contamination
* Atmospheric interference
* Sensor noise
* Cloud shadows

### Are there relationships between individual instances?

Yes. Instances are spatially overlapping and temporally sequential, enabling temporal compositing and vegetation analysis.

### Are there recommended data splits (train/val/test)?

No official train/validation/test splits exist because the dataset was not designed as a benchmark machine learning dataset.

---

## 3. Collection process

### How was the data acquired?

Remote sensing through multispectral satellite imaging.

### What instruments / sensors / software were used?

Sentinel-2 MultiSpectral Instrument (MSI).

### Who was involved in the data collection process?

Automated satellite acquisition systems operated by ESA and the Copernicus Programme.

### Over what time period was the data collected?

The project subset covers June–August 2018.

### What was the sampling strategy?

Deterministic global Earth observation with continuous revisit coverage.

### Is the sample representative of the larger population it claims to describe?

The dataset reasonably represents broad summer vegetation patterns across Manhattan but does not capture:

* Fine-scale tree canopy structure
* Seasonal variability outside Summer 2018
* Real-time vegetation stress conditions

### Were any ethical review processes conducted?

Not applicable because the dataset contains no personal or human subject data.

---

## 4. Preprocessing & cleaning

### What preprocessing was done by the dataset creators?

* Atmospheric correction
* Radiometric calibration
* Geometric correction
* Surface reflectance generation

### Is the raw data also available?

Yes.

### What preprocessing did WE do before adopting the dataset?

* Spatial clipping to Manhattan
* Summer-period temporal filtering
* Cloud masking using the Scene Classification Layer (SCL)
* NDVI calculation using B8 and B4 bands
* Temporal median compositing

### Where is the preprocessing software / code available?

Python notebooks using:

* Google Earth Engine API
* Geemap
* Pandas
* NumPy

---

## 5. Uses

### What tasks has the dataset been used for?

* NDVI analysis
* Vegetation monitoring
* Ecological assessment
* Urban greening analysis
* Environmental monitoring

### Is there a repository linking to papers / systems that use this dataset?

Yes. Documentation and implementations are available through:

* ESA Copernicus documentation
* Google Earth Engine examples
* Peer-reviewed environmental research

### What other tasks could this dataset be used for?

* Land cover classification
* Biodiversity analysis
* Agricultural assessment
* Environmental AI workflows
* Urban ecological studies

### What tasks should this dataset NOT be used for?

1. Should not be used for direct human thermal comfort assessment because NDVI only represents vegetation presence and not actual thermal experience.

2. Should not be used for individual tree-level health analysis because the 10 m spatial resolution is insufficient for fine-grain vegetation interpretation.

### Are there any considerations about discrimination, bias, or harm that could result from use of this dataset?

Vegetation distribution patterns may be incorrectly interpreted without considering urban density, land use context, and socioeconomic conditions.

---

## 6. Distribution & licensing

### Under what license is the dataset distributed?

Copernicus Open Access License.

### Are there any restrictions on use, redistribution, attribution, or modification?

Open for research and educational use with attribution requirements.

### What's the required attribution string?

“Contains modified Copernicus Sentinel data processed by ESA.”

### Are there fees for access?

No.

### Are there export controls or regulatory restrictions?

None known for academic or research use.

---

## 7. Maintenance

### Who supports / hosts / maintains the dataset?

European Space Agency (ESA) and the Copernicus Programme.

### How can the maintainer be contacted?

Through official ESA Copernicus support portals.

### Is there an erratum?

Periodic calibration and processing updates are published.

### Will the dataset be updated?

Yes.

### How often is the dataset updated?

Continuously with new satellite acquisitions.

### Are older versions of the dataset still available?

Yes.

---

## 8. Limitations relative to OUR project

### Resolution mismatch with our decision unit?

The 10 m spatial resolution cannot capture exact tree canopy structure or street-level vegetation conditions.

### Geographic gaps that matter for us?

The project only analyses Manhattan and does not account for ecological interactions with adjacent boroughs.

### Temporal gaps that matter for us?

The analysis only uses Summer 2018 imagery and does not represent long-term vegetation dynamics.

### Biases that could distort our conclusions?

* Cloud masking may remove some valid observations
* Median compositing may suppress short-duration vegetation stress
* NDVI is a proxy indicator and not a direct measure of cooling performance

### What additional sources would compensate for these limits?

* LiDAR canopy datasets
* NYC tree inventory datasets
* High-resolution aerial imagery
* Field survey measurements

### Verdict for our project

Secondary dataset used to explain vegetation influence on relative urban heat exposure patterns across Manhattan.
