# Pipeline Architecture v1

> This document describes the transition from an exploratory urban heat
> analysis workflow into a structured and reproducible cleaning pipeline
> for Manhattan urban heat analysis using Landsat and Sentinel imagery.

---

# What changed since v0

In Session 2, the workflow primarily focused on exploratory profiling,
visualization, and hotspot mapping. Session 3 introduces structured
cleaning logic, modular transforms, and reproducibility-oriented
pipeline design.

The cleaning workflow now includes:
- CRS validation
- cloud masking
- NoData handling
- LST validation
- NDVI normalization
- hotspot cleaning
- raster integration

Implemented components are now connected to:
- `src/clean_data.py`
- `02-data-cleaning.ipynb`
- `data-cleaning-log.md`

Future modeling and evaluation components remain planned for later
sessions.

---

# The diagram

```mermaid
flowchart LR

    subgraph raw [Raw Data Sources]
        R1[Landsat 8 Thermal Imagery]
        R2[Sentinel-2 Optical Imagery]
    end

    subgraph clean [Phase 3 · Cleaning Pipeline]
        C1[validate_crs<br/>src/clean_data.py]
        C2[apply_cloud_mask<br/>src/clean_data.py]
        C3[handle_nodata_pixels<br/>src/clean_data.py]
        C4[validate_lst_range<br/>src/clean_data.py]
        C5[normalize_ndvi<br/>src/clean_data.py]
        C6[remove_hotspot_artifacts<br/>src/clean_data.py]
        C7[integrate_rasters<br/>src/clean_data.py]
    end

    subgraph processed [Processed Outputs]
        P1[Cleaned LST Outputs]
        P2[Cleaned NDVI Outputs]
        P3[Heat-Risk Layers]
        P4[Hotspot Visualizations]
    end

    subgraph future [Future · Phase 4-7]
        F1["Hotspot Prediction Model<br/>(planned · Session 4)"]
        F2["Spatial Risk Evaluation<br/>(planned · Session 5-6)"]
        F3["Decision-facing Dashboard<br/>(planned · Session 7)"]
    end

    R1 --> C1 --> C2 --> C3 --> C4 --> C7 --> P1
    R2 --> C1 --> C2 --> C5 --> C7 --> P2

    P1 --> P3
    P2 --> P3
    P3 --> P4

    P4 --> F1 --> F2 --> F3