0. Quick reference
Dataset name: Landsat 8 Collection 2 Tier 1 Level 2
Version / vintage: Collection 2, Summer 2018 subset
Source URL: USGS Landsat Collection 2
License: Public domain
Spatial coverage: Manhattan, New York City, USA
Temporal coverage: 2018-06-01 to 2018-08-31
Native resolution (spatial / temporal): 30 m spatial, 16-day revisit
Format: Earth Engine raster imagery / GeoTIFF compatible
Size: Approx. several GB globally; project subset <500 MB
Datasheet last updated: 2026-05-13 by Jinesh
1. Motivation
Why was the dataset created?
The dataset was created to provide calibrated multispectral Earth observation imagery for environmental monitoring, climate analysis, land cover analysis, and thermal studies.
Who created the dataset?
The dataset was created jointly by the National Aeronautics and Space Administration and the United States Geological Survey.
Who funded the creation of the dataset?
The United States federal government through NASA and USGS programs.
For what tasks was the dataset originally intended?
Environmental monitoring, thermal mapping, land use analysis, vegetation analysis, and climate research.
2. Composition
What does an instance represent?
One satellite image scene containing multispectral and thermal raster bands for a specific timestamp.
How many instances are there in total?
The project used multiple Landsat scenes between June and August 2018 over Manhattan.
Field	Type	Description	Required?
ST_B10	Float Raster	Surface temperature thermal band	Yes
system:time_start	Timestamp	Acquisition date/time	Yes
CLOUD_COVER	Float	Percentage cloud cover metadata	Yes
Are there labels or targets associated with each instance?
No explicit labels. The dataset is observational remote sensing imagery.
Is any information missing from instances?
Some pixels may be obscured due to atmospheric interference, cloud contamination, or sensor artifacts.
Are there relationships between individual instances?
Yes. Instances are temporally sequential and spatially overlapping.
Are there recommended data splits (train/val/test)?
No official splits are provided because this is not a benchmark ML dataset.
3. Collection process
How was the data acquired?
Remote sensing through satellite-based thermal and multispectral imaging.
What instruments / sensors / software were used?
Landsat 8 Operational Land Imager (OLI) and Thermal Infrared Sensor (TIRS).
Who was involved in the data collection process?
Automated satellite acquisition systems managed by NASA and USGS.
Over what time period was the data collected?
Summer 2018 for this project subset.
What was the sampling strategy?
Deterministic Earth observation with global periodic coverage.
Is the sample representative of the larger population it claims to describe?
It reasonably represents summer surface temperature conditions but may not represent yearly variability.
Were any ethical review processes conducted?
Not applicable because no personal or human subject data is involved.
4. Preprocessing & cleaning
What preprocessing was done by the dataset creators?
Radiometric calibration, atmospheric correction, geometric correction, and Level 2 surface temperature derivation.
Is the raw data also available?
Yes.
What preprocessing did WE do before adopting the dataset?
Cloud filtering, spatial clipping to Manhattan, conversion of thermal band values to Celsius, and temporal averaging.
Where is the preprocessing software / code available?
Python notebook using Earth Engine API and Geemap.
5. Uses
What tasks has the dataset been used for?
Urban heat island analysis, climate studies, land surface temperature mapping, and environmental monitoring.
Is there a repository linking to papers / systems that use this dataset?
Yes. USGS and Google Earth Engine repositories and documentation.
What other tasks could this dataset be used for?
Urban planning, climate adaptation studies, ecological analysis, and AI-based environmental prediction.
What tasks should this dataset NOT be used for?
Should not be used for indoor temperature estimation because measurements represent outdoor land surface temperature only.
Should not be used for fine-scale pedestrian thermal comfort analysis due to 30 m spatial resolution limitations.
Are there any considerations about discrimination, bias, or harm that could result from use of this dataset?
Urban thermal interpretations may overgeneralize vulnerable communities if combined with incomplete socioeconomic data.
6. Distribution & licensing
Under what license is the dataset distributed?
Public domain.
Are there any restrictions on use, redistribution, attribution, or modification?
No major restrictions.
What's the required attribution string?
“Landsat-8 imagery courtesy of the U.S. Geological Survey.”
Are there fees for access?
No.
Are there export controls or regulatory restrictions?
None known for public research use.
7. Maintenance
Who supports / hosts / maintains the dataset?
USGS and NASA.
How can the maintainer be contacted?
Through official USGS Landsat support portals.
Is there an erratum?
Periodic calibration updates are published.
Will the dataset be updated?
Yes.
How often is the dataset updated?
Continuously with new satellite acquisitions.
Are older versions of the dataset still available?
Yes.
8. Limitations relative to OUR project
Resolution mismatch with our decision unit?
30 m resolution may miss micro-scale urban heat variations between individual streets and buildings.
Geographic gaps that matter for us?
The dataset captures only Manhattan and excludes broader metropolitan heat interactions.
Temporal gaps that matter for us?
The study only uses Summer 2018 and does not capture long-term seasonal change.
Biases that could distort our conclusions?
Cloud filtering and seasonal averaging may suppress short-duration heat events.
What additional sources would compensate for these limits?
Higher-resolution thermal imagery, local weather station data, and socioeconomic datasets.
Verdict for our project:
Primary dataset.
