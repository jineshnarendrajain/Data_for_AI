# Problem Brief v2 — Urban Vegetation Health & Environmental Risk Mapping

> Phase-1 loopback artifact. After today's data understanding work, does your
> Session 1 brief still hold? CRISP-DM is iterative — phase 2 routinely sends
> you back to phase 1 to revise the question. That's not failure; that's the
> process working correctly.

---

## Was v1 revised? (yes / no)

Yes

## What did the data reveal?

- Sentinel-2 imagery provides sufficient spatial resolution for neighborhood-scale vegetation analysis, but not for individual tree-level assessment.
- NDVI values are strongly affected by cloud cover, atmospheric conditions, and seasonal variation, requiring careful filtering and temporal consistency.
- Temporal comparisons between datasets from different seasons can produce misleading vegetation trends if acquisition periods are not normalized.
- Some urban areas with dense built environments naturally produce low NDVI values, meaning low NDVI should not automatically be treated as anomalous or erroneous.

---

## What changed in the brief

### Decision

- **Was:** Identify vegetation and environmental conditions across the study area.
- **Now:** Support identification and prioritization of urban zones with declining vegetation health and increased environmental vulnerability using cleaned NDVI-derived indicators.

### User

- **Was:** General users interested in environmental analysis.
- **Now:** Urban planners, environmental analysts, and municipal decision-makers requiring interpretable geospatial evidence for vegetation and environmental risk assessment.

### Success criteria

- **Was:** Produce NDVI maps and environmental analysis outputs.
- **Now:** 
  - Produce a reproducible NDVI preprocessing and cleaning pipeline.
  - Generate spatially and temporally consistent NDVI datasets from Sentinel-2 imagery.
  - Document all preprocessing assumptions, cleaning decisions, and limitations.
  - Produce outputs suitable for downstream spatial/environmental modeling and decision-support workflows.

### Sub-questions

- **Was:** How does vegetation vary across the study area?
- **Now:** 
  - Which urban areas consistently exhibit low vegetation health?
  - How do temporal and seasonal variations affect NDVI interpretation?
  - Which preprocessing steps most strongly influence NDVI reliability?
  - How can NDVI-derived indicators support environmental risk assessment?

### Out of scope

*New additions, given data limits:*

- Individual tree health assessment at fine-grain scale.
- Direct inference of human thermal comfort or indoor environmental conditions solely from NDVI values.

---

## What we still don't know

- What temporal aggregation strategy produces the most stable NDVI representation for the study area.
- How strongly cloud masking and atmospheric correction affect downstream NDVI consistency.
- Whether additional auxiliary datasets will be required to strengthen environmental risk interpretation.

---

## Sign-off

The full revised brief lives in `docs/problem-brief.md` (overwritten if revised).
This file (`problem-brief-v2.md`) is the changelog explaining *why*.

**Team:** [names]
**Committed by:** [name]
**Date:** [YYYY-MM-DD]
