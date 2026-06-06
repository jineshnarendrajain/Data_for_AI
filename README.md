# Data_for_AI — Manhattan Urban Heat Hotspot Prioritisation

## Overview

This project develops a reproducible geospatial workflow for identifying relative urban heat hotspots across Manhattan using publicly available Earth observation data.

The workflow combines:

* Landsat 8 Land Surface Temperature (LST)
* Sentinel-2 Vegetation Density (NDVI)

to generate a relative heat risk framework capable of supporting urban heat mitigation planning and decision-support activities.

The project follows the progression of the Data for AI coursework and documents the complete analytical workflow from data profiling through evaluation.

---

# Project Objective

The objective of this project is to identify areas of elevated relative urban heat exposure across Manhattan.

The workflow uses satellite-derived environmental indicators to:

* Characterise thermal conditions
* Assess vegetation coverage
* Identify relative heat hotspots
* Support urban heat mitigation planning
* Provide evidence for future decision-support tools

---

# Project Timeline

| Session   | Focus                            | Outcome                                        |
| --------- | -------------------------------- | ---------------------------------------------- |
| Session 1 | Data Profiling                   | Environmental profiling and hotspot generation |
| Session 2 | Data Quality Assessment          | Audit and decision mapping                     |
| Session 3 | Data Cleaning & Reproducibility  | Cleaned datasets and workflow documentation    |
| Session 4 | Heat Risk Analysis               | Heat risk framework and hotspot identification |
| Session 5 | Evaluation & Validity Assessment | Evaluation reports and validity audit          |
| Session 6 | Decision Support Tool (Planned)  | Interactive planning tool                      |

---

# Analytical Workflow

```text
Landsat 8 Thermal Imagery
            +
Sentinel-2 Vegetation Imagery
            ↓
Environmental Profiling
            ↓
Land Surface Temperature (LST)
            ↓
Vegetation Density (NDVI)
            ↓
Heat Risk Framework
            ↓
Hotspot Identification
            ↓
Evaluation & Validity Assessment
            ↓
Decision Support Applications
```

---

# Study Area

**Location**

Manhattan, New York City

**Study Period**

2018-06-01 to 2018-08-31

---

# Data Sources

## Landsat 8 Collection 2 Level 2

Purpose:

* Land Surface Temperature estimation

Scenes processed:

* 2

Observed LST Statistics:

| Statistic | Value    |
| --------- | -------- |
| Minimum   | 10.33 °C |
| Mean      | 30.73 °C |
| Maximum   | 49.20 °C |

---

## Sentinel-2 Surface Reflectance

Purpose:

* Vegetation Density estimation

Scenes processed:

* 7

Observed NDVI Statistics:

| Statistic | Value |
| --------- | ----- |
| Minimum   | -0.27 |
| Mean      | 0.09  |
| Maximum   | 0.70  |

---

# Heat Risk Framework

The project combines thermal and vegetation indicators into a single interpretable framework.

## Formula

```text
Heat Risk Score =
Normalized LST − Normalized NDVI
```

Interpretation:

* Higher temperatures increase risk.
* Greater vegetation reduces risk.
* Higher scores indicate greater relative heat exposure.

---

# Hotspot Identification

The workflow generated a heat risk layer and extracted hotspot samples representing locations of elevated relative heat exposure.

Hotspot extraction parameters:

* Manhattan study area
* 30 m sampling resolution
* 10 hotspot samples

Output:

```text
Top hotspot samples extracted: 10
```

---

# Repository Structure

```text
Data_for_AI/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── profile-summary.json
│
├── docs/
│   ├── datasheets/
│   ├── data-cleaning-log.md
│   ├── data-quality-audit.md
│   ├── data-source-inventory.md
│   ├── data-to-decision-map.md
│   ├── function-design-checklist.md
│   ├── modelling_log.md
│   ├── heat-risk-analysis-card.md
│   ├── evaluation-report.md
│   ├── evaluation-log.md
│   ├── validity-audit.md
│   ├── conclusions-brief.md
│   ├── pipeline-architecture-v1.md
│   ├── pipeline_architecture-v2.md
│   ├── pipeline-architecture-v3.md
│   ├── problem-brief-v2.md
│   └── system-sketch-v0.md
│
├── notebooks/
│   ├── 01-data-profiling.ipynb
│   ├── 02-data-cleaning.ipynb
│   └── 03-heat-risk-analysis.ipynb
│
├── src/
│   └── clean_data.py
│
├── archive/
│   └── utci-random-forest-experiment/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Running the Project

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Session 1 — Data Profiling

```bash
jupyter notebook notebooks/01-data-profiling.ipynb
```

---

## Session 3 — Data Cleaning

```bash
jupyter notebook notebooks/02-data-cleaning.ipynb
```

---

## Session 4 — Heat Risk Analysis

```bash
jupyter notebook notebooks/03-heat-risk-analysis.ipynb
```

---

# Documentation

The repository includes:

## Core Project Documents

* Problem Brief
* System Sketch
* Output Sketch
* Modelling Log
* Heat Risk Analysis Card

## Evaluation Documents

* Evaluation Report
* Evaluation Log
* Validity Audit
* Conclusions Brief

## Architecture Documents

* Pipeline Architecture V1
* Pipeline Architecture V2
* Pipeline Architecture V3

## Data Governance Documents

* Datasheets
* Data Quality Audit
* Data Source Inventory
* Data Cleaning Log
* Reproducibility Checklist

---

# Evaluation Summary

Session 5 evaluation concluded that:

* The workflow uses appropriate environmental indicators.
* The methodology is transparent and reproducible.
* The resulting hotspot outputs are plausible.
* The workflow is suitable for exploratory planning and educational applications.

Overall validity status:

```text
PASS WITH DOCUMENTED LIMITATIONS
```

---

# Future Work

Planned future extensions include:

* NYC Heat Vulnerability Index comparison
* Neighbourhood-level aggregation
* Multi-year analysis
* Seasonal comparisons
* Interactive decision-support dashboards
* Urban heat intervention prioritisation tools

---

# Archive

The repository contains an archive folder documenting an earlier exploratory UTCI prediction workflow.

These materials are retained for transparency and project traceability but are not part of the final project deliverable.

---

# Authors

Dhruvil,Jinesh,Rudra,Sumit

Academic coursework project focused on urban heat hotspot identification, evaluation, and decision-support development.
