# Data Cleaning Log — Manhattan Urban Heat Dataset

> Every transformation in the urban heat cleaning pipeline is documented
> below to preserve transparency, reproducibility, and downstream
> interpretability.

---

# Dataset under cleaning

- **Dataset:** Manhattan Urban Heat Dataset
- **Raw path:** `data/raw/`
- **Clean output:** `data/processed/`
- **Cleaning module:** `src/clean_data.py`
- **Cleaning notebook:** `notebooks/02-data-cleaning.ipynb`
- **Maintainer:** [your name]
- **Last updated:** [YYYY-MM-DD]

---

# Pipeline summary

- **Primary datasets:** Landsat 8 thermal imagery and Sentinel-2 optical imagery
- **Spatial scope:** Manhattan, New York City
- **Temporal scope:** Summer-season urban heat analysis
- **Primary outputs:** LST layers, NDVI layers, hotspot outputs, and heat-risk visualizations
- **Processing environment:** Python and Google Earth Engine workflow
- **Pipeline structure:** exploratory cleaning workflow promoted toward a modular pipeline

---

# The transforms — every one logged

---

## Transform 1 — `validate_crs`

- **What it changed:** Applied CRS validation checks between Landsat and Sentinel datasets before raster integration.

- **Why this and not the alternative:** CRS mismatches can silently distort spatial overlays and hotspot interpretation. Early validation was preferred over correcting issues after integration.

- **Downstream effect:** Supports more reliable alignment between thermal and vegetation datasets during hotspot and heat-risk analysis.

- **Reversibility:** Yes — validation checks do not overwrite original raster data.

- **Assertion that proves it worked:**  
  `assert crs_consistent, "CRS mismatch detected"`

---

## Transform 2 — `apply_cloud_mask`

- **What it changed:** Applied cloud masking procedures intended to reduce cloud-contaminated imagery regions.

- **Why this and not the alternative:** Cloud contamination can introduce misleading thermal and vegetation values. Masking was preferred over retaining visibly contaminated imagery.

- **Downstream effect:** Improves interpretability of LST and NDVI outputs during hotspot analysis.

- **Reversibility:** Yes — original imagery remains preserved separately from cleaned outputs.

- **Assertion that proves it worked:**  
  `assert cloud_mask_applied, "Cloud masking failed"`

---

## Transform 3 — `handle_nodata_pixels`

- **What it changed:** Applied NoData handling procedures to reduce invalid raster regions and missing spatial values.

- **Why this and not the alternative:** NoData regions can interfere with hotspot extraction and raster comparison. Cleaning was preferred over interpolation to avoid introducing artificial temperature patterns.

- **Downstream effect:** Reduces invalid raster artifacts during spatial analysis and heat-risk interpretation.

- **Reversibility:** Yes — original raster layers remain preserved.

- **Assertion that proves it worked:**  
  `assert nodata_cleaned, "NoData handling failed"`

---

## Transform 4 — `validate_lst_range`

- **What it changed:** Applied validation checks to ensure Land Surface Temperature values remained within plausible urban thermal ranges.

- **Why this and not the alternative:** Unrealistic thermal values may originate from raster inconsistencies, atmospheric effects, or sensor noise. Validation was preferred over unrestricted retention of all thermal values.

- **Downstream effect:** Supports more stable hotspot interpretation and heat-risk visualization.

- **Reversibility:** Partially reversible — validation filters influence cleaned outputs while original raster sources remain available.

- **Assertion that proves it worked:**  
  `assert 0 <= lst_min <= 70`

---

## Transform 5 — `normalize_ndvi`

- **What it changed:** Applied NDVI normalization procedures to improve consistency across vegetation outputs.

- **Why this and not the alternative:** NDVI normalization improves comparability between vegetation regions and supports clearer comparison against thermal intensity patterns.

- **Downstream effect:** Supports interpretation of vegetation influence on urban heat concentration.

- **Reversibility:** Yes — normalization affects derived outputs only.

- **Assertion that proves it worked:**  
  `assert ndvi_normalized, "NDVI normalization failed"`

---

## Transform 6 — `remove_hotspot_artifacts`

- **What it changed:** Applied hotspot-cleaning procedures intended to reduce invalid thermal hotspot artifacts.

- **Why this and not the alternative:** Unfiltered hotspot artifacts can exaggerate heat concentration and reduce interpretability of hotspot maps.

- **Downstream effect:** Supports cleaner heat-risk visualization and hotspot interpretation.

- **Reversibility:** Partially reversible — cleaned outputs are derived while original thermal layers remain preserved.

- **Assertion that proves it worked:**  
  `assert hotspot_cleaned, "Hotspot cleaning failed"`

---

## Transform 7 — `integrate_rasters`

- **What it changed:** Combined Landsat thermal outputs and Sentinel vegetation outputs into a unified analysis workflow.

- **Why this and not the alternative:** Integrated raster analysis supports comparison between vegetation density and thermal intensity patterns.

- **Downstream effect:** Supports combined NDVI-LST interpretation and urban heat-risk assessment.

- **Reversibility:** Yes — integration produces derived outputs without overwriting original imagery.

- **Assertion that proves it worked:**  
  `assert raster_integrated, "Raster integration failed"`

---

# What we did NOT clean — and why

| Issue | Why we left it | What downstream needs to know |
|---|---|---|
| Minor seasonal atmospheric variation | Preserving realistic summer environmental variation was preferred over aggressive correction | Some thermal variation may still reflect atmospheric influence |
| Small thermal anomalies | Some anomalies may represent real urban heat conditions rather than noise | Hotspot interpretation should consider local spatial context |
| Spatial edge inconsistencies | Edge clipping was minimized to preserve study-area coverage | Boundary regions may contain minor raster inconsistencies |

---

# Cumulative effect — raw vs cleaned

The cleaning workflow focused on improving consistency between Landsat
and Sentinel raster datasets while preserving the overall spatial and
thermal structure of the Manhattan urban heat analysis workflow.
Cleaning operations primarily targeted cloud contamination, CRS
consistency, NoData regions, thermal plausibility checks, and hotspot
artifact reduction. The resulting outputs are more suitable for
exploratory hotspot analysis, NDVI-LST comparison, and heat-risk
visualization workflows. However, the outputs should still be considered
part of an exploratory remote sensing workflow rather than a fully
validated atmospheric correction pipeline.

---

# Sign-off

The following workflow components were structured for reproducibility and
modular cleaning:

- [ ] `python src/clean_data.py` tested end-to-end
- [ ] Reproducibility verified on repeated runs
- [ ] Cleaned outputs re-profiled in `01-data-profiling.ipynb`
- [ ] Assertions validated successfully
- [ ] Cleaning log reviewed against implemented transforms

**Prepared by:** Rudra Mhatre

**Notes:**  
This workflow currently represents a structured exploratory cleaning
pipeline for Manhattan urban heat analysis using Landsat and Sentinel
imagery. Some cleaning operations remain conceptual and may require
further implementation refinement in future phases.