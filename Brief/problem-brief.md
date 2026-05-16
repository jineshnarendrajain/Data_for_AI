# Problem Brief — Urban Thermal Hotspot Mapping for Manhattan

---

## The Environmental Question

Where are Manhattan’s urban thermal hotspots during peak summer conditions, and how is vegetation associated with spatial variation in land surface temperature (LST) across neighbourhood-scale zones?

---

## The Design Decision This Supports

A climate resilience analyst at a New York City municipal agency (e.g., Department of City Planning or the Mayor’s Office of Climate & Environmental Justice) must decide which neighbourhood-scale zones in Manhattan should be prioritised for near-term urban heat mitigation interventions such as tree planting, shading infrastructure, or surface material modifications.

This project supports targeted allocation of limited public resources by identifying spatially explicit urban thermal hotspots and analysing their relationship with vegetation density. The goal is to enable prioritised and evidence-based intervention planning rather than uniform city-wide strategies.

---

## The Intended User

A capital planning or climate resilience analyst working within a New York City municipal agency.

* Works with GIS-based spatial datasets and urban policy frameworks
* Responsible for recommending where limited intervention budgets should be allocated
* Needs outputs that are spatially explicit, interpretable, and defensible
* Must communicate decisions to non-technical stakeholders such as policymakers, planners, and community boards

**Moment of use:**
Tuesday morning, preparing a shortlist of priority zones for inclusion in a seasonal urban heat mitigation plan.

---

## Measurable Success Criteria

1. The full pipeline (data loading → preprocessing → analysis → output) runs from the repository on a new machine in under 10 minutes using clearly documented steps.

2. Land Surface Temperature (LST) and NDVI maps are generated for Manhattan using satellite imagery with spatial resolution appropriate for neighbourhood-scale environmental analysis.

3. The system identifies and visualises 5–10 neighbourhood-scale zones exhibiting the highest relative land surface temperature during peak summer conditions.

4. At least one comparison is performed using an external reference dataset or proxy (e.g., NYC Heat Vulnerability Index), with agreement and discrepancies explicitly documented.

5. The final output (map or dashboard) clearly distinguishes relatively high-temperature and low-temperature zones while transparently communicating limitations and uncertainty.

6. The relationship between vegetation density (NDVI) and land surface temperature is analysed and documented using interpretable methods understandable to non-technical stakeholders.

---

## Risks and Open Questions

### Risks

* **Proxy limitation:**
  Land Surface Temperature (LST) represents surface thermal conditions rather than complete human thermal comfort. Factors such as humidity, wind, radiation exposure, and building geometry are not directly captured.

* **Spatial resolution limits:**
  Satellite-derived datasets (~10–30m resolution) may not capture fine-grained urban variations such as street-level shading or material differences.

* **Cloud contamination and atmospheric effects:**
  Satellite imagery quality may be affected by cloud cover, haze, and atmospheric variability, potentially introducing inconsistencies into NDVI and LST calculations.

* **Temporal consistency challenges:**
  Satellite revisit cycles and seasonal variability may affect comparability between image acquisitions if temporal filtering is not carefully controlled.

* **Data integration mismatch:**
  External datasets (e.g., Heat Vulnerability Index) may differ in spatial resolution, temporal coverage, or methodology.

* **Validation limitations:**
  Limited access to high-resolution ground-truth thermal measurements may constrain validation accuracy.

---

### Open Questions

* What is the most appropriate spatial aggregation unit for defining “neighbourhood-scale zones” (grid cells, census tracts, or custom aggregation)?
* What threshold or classification method should define a “thermal hotspot” (absolute threshold vs relative ranking)?
* How strongly does vegetation density correlate with observed land surface temperature variation across Manhattan?

---

## Out of Scope

* Indoor or building-level thermal comfort analysis
* Human physiological heat stress modelling
* High-resolution microclimate or CFD-based simulations
* Real-time or live environmental monitoring systems
* Long-term climate forecasting or predictive climate modelling
* Causal attribution of temperature variation solely to vegetation cover
* Geographic scope beyond Manhattan

---

## Team

| Name                        | Role on this project |
| --------------------------- | -------------------- |
| Dhruvil Mahendra Bhanushali | Data Lead            |
| Jinesh Narendra Jain        | Visualization Lead   |
| Rudra Mhatre                | Documentation Lead   |
| Sumit Sudhir Shingne        | Domain Research Lead |

---

**This document defines the purpose and scope of the project. All subsequent artifacts (data inventory, data audit, decision map, system design, and outputs) must align with this brief.**
