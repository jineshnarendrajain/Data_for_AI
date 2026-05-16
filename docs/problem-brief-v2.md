# Problem Brief v2 — Urban Thermal Hotspot Mapping for Manhattan

> Phase-1 loopback artifact. After data understanding and dataset evaluation, the original project brief was revised to better align with the actual capabilities and limitations of the adopted datasets.
>
> This revision reflects a refinement of scope rather than a change in project direction. The project remains focused on urban thermal hotspot analysis using remote sensing data, but unsupported claims and overly broad objectives were narrowed to improve methodological consistency and defensibility.

---

## Was v1 revised? (yes / no)

Yes

---

## What did the data reveal?

* Landsat-derived Land Surface Temperature (LST) is suitable for neighbourhood-scale thermal hotspot analysis but not for fine-grained street-level or building-level heat assessment.

* Sentinel-2 NDVI provides useful vegetation context at 10m resolution, but NDVI should be treated as a proxy for vegetation presence rather than a direct measure of cooling performance or human comfort.

* Cloud cover, atmospheric conditions, and seasonal variability significantly affect both NDVI and LST consistency, requiring careful filtering and temporal normalization.

* The available datasets support relative spatial comparison of thermal conditions during Summer 2018, but do not support long-term forecasting or direct human thermal comfort modelling.

---

## What changed in the brief

### Decision

* **Was:** Identify areas experiencing “heat stress” and potential long-term environmental risk across Manhattan.
* **Now:** Identify neighbourhood-scale urban thermal hotspots and support prioritisation of near-term urban heat mitigation interventions using spatial analysis of LST and vegetation patterns.

### User

* **Was:** Broad framing around environmental risk assessment and general urban analysis.
* **Now:** Climate resilience analysts and municipal planning professionals requiring interpretable geospatial evidence for urban heat mitigation planning.

### Success criteria

* **Was:** Included broad temporal claims, predictive framing, and general environmental risk outputs.
* **Now:** Focused on producing a reproducible and interpretable spatial analysis pipeline using Landsat LST and Sentinel-2 NDVI to identify relative urban thermal hotspots within Manhattan.

### Sub-questions

* **Was:** Included broader questions around long-term change, thermal discomfort, and environmental risk forecasting.
* **Now:** Refocused on:

  * Where elevated land surface temperatures are concentrated spatially
  * How vegetation density relates to observed LST variation
  * Which neighbourhood-scale zones should be prioritised for heat mitigation planning
  * How preprocessing and filtering decisions affect data reliability

### Out of scope

*New additions, given data limits:*

* Human thermal comfort modelling using humidity, wind, or physiological heat stress indicators
* Long-term predictive climate forecasting or causal attribution analysis

---

## What we still don't know

* What spatial aggregation strategy produces the most interpretable neighbourhood-scale hotspot classification.
* How strongly NDVI variation correlates with observed LST variation across different urban morphologies in Manhattan.
* Whether additional auxiliary datasets would improve hotspot validation and interpretation.

---

## Sign-off

The full revised brief lives in `docs/problem-brief.md` (overwritten after revision).
This file (`problem-brief-v2.md`) documents why the revision was necessary and how the project scope evolved after data understanding.

**Team:** Dhruvil Mahendra Bhanushali, Jinesh Narendra Jain, Rudra Mhatre, Sumit Sudhir Shingne
**Committed by:** Jinesh Narendra Jain
**Date:** 2026-05-13
