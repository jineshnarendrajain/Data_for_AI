# Data → Decision Map

---

## The map

| Brief sub-question                                                                                                                                             | Primary data source               | Secondary source                                                     | Confidence (H/M/L) | Notes                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | -------------------------------------------------------------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sub-Q 1: Where are elevated land surface temperatures concentrated across Manhattan during peak summer conditions?                                             | Landsat Surface Temperature (LST) | —                                                                    | MEDIUM             | Landsat provides direct thermal surface measurements suitable for neighbourhood-scale hotspot identification, but limited by revisit frequency and cloud contamination |
| Sub-Q 2: How does vegetation density vary spatially across Manhattan?                                                                                          | Sentinel-2 NDVI                   | —                                                                    | MEDIUM             | NDVI provides a useful proxy for vegetation presence and density at 10m resolution, though it does not directly measure cooling performance or canopy structure        |
| Sub-Q 3: How is vegetation density associated with observed land surface temperature variation across Manhattan?                                               | Landsat Surface Temperature (LST) | Sentinel-2 NDVI                                                      | MEDIUM             | Relationship between NDVI and LST is spatially correlational rather than causal; interpretation must remain proxy-based                                                |
| Sub-Q 4: Which neighbourhood-scale zones should be prioritised for urban heat mitigation planning based on elevated LST and relatively low vegetation density? | Landsat Surface Temperature (LST) | Sentinel-2 NDVI, NYC Heat Vulnerability Index (validation reference) | MEDIUM             | Priority zones derived using interpretable rule-based spatial classification combining relatively high LST and relatively low NDVI values                              |

---

## Coverage check

* **Sub-questions with HIGH confidence:**

  * None

* **Sub-questions with MEDIUM confidence:**

  * All four sub-questions

* **Sub-questions with LOW confidence:**

  * None

* **Sub-questions with NO data backing:**

  * None

---

## What this means for the brief

* [ ] Find a new source — not currently required; all major sub-questions are supported by adopted datasets

* [x] Revise the brief — completed after data understanding and scope refinement

* [x] Accept MEDIUM confidence as a documented limitation

---

## Limitation statement

All sub-questions rely on satellite-derived proxy variables (LST and NDVI). These datasets support relative spatial comparison of surface thermal conditions and vegetation distribution, but they do not directly measure human thermal comfort, street-level microclimate dynamics, or causal environmental relationships. Results should therefore be interpreted as neighbourhood-scale thermal hotspot patterns rather than precise physiological heat exposure measurements.

---

## Sign-off

**Team:** Dhruvil Mahendra Bhanushali, Jinesh Narendra Jain, Rudra Mhatre, Sumit Sudhir Shingne
**Last updated:** 2026-05-13
