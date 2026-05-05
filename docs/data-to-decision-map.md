# Data → Decision Map

---

## The map

| Brief sub-question | Primary data source | Secondary source | Confidence (H/M/L) | Notes |
|---|---|---|---|---|
| Sub-Q 1: How has land surface temperature (LST) varied spatially across Manhattan during peak summer periods over the past 10–15 years? | Landsat Surface Temperature | — | MEDIUM | Direct LST measurement with long historical coverage; limited by revisit frequency and cloud gaps |
| Sub-Q 2: Which street-block-level zones in Manhattan exhibit the highest land surface temperature (LST) during peak summer conditions? | Landsat Surface Temperature | — | MEDIUM | Spatial resolution (~30–100m) allows block-level approximation but not exact precision |
| Sub-Q 3: How does green cover (vegetation) influence land surface temperature (LST) across street-block-level zones in Manhattan? | Sentinel-2 NDVI | Landsat Surface Temperature | MEDIUM | NDVI is a proxy for vegetation; relationship with LST is correlational, not causal |
| Sub-Q 4: Which street-block-level zones in Manhattan should be prioritised for heat mitigation based on high land surface temperature (LST) and low green cover? | Landsat Surface Temperature | Sentinel-2 NDVI (NYC Heat Vulnerability Index for validation) | MEDIUM | Priority derived using rule-based combination (high LST + low NDVI); simplified model without full thermal comfort factors |

---

## Coverage check

- **Sub-questions with HIGH confidence:**
  - None

- **Sub-questions with MEDIUM confidence:**
  - All four sub-questions

- **Sub-questions with LOW confidence:**
  - None

- **Sub-questions with NO data backing:**
  - None

---

## What this means for the brief

- [ ] Find a new source — not required; all sub-questions are supported by available datasets  

- [ ] Revise the brief — not required at this stage  

- [x] Accept MEDIUM confidence as a documented limitation  

**Limitation statement:**
All sub-questions rely on satellite-derived proxies (LST and NDVI), which do not fully capture human thermal comfort or microclimate dynamics (e.g., humidity, wind, shading). Results should be interpreted as relative heat exposure patterns rather than precise thermal comfort measurements.

---

## Sign-off

**Team:** Dhruvil Mahendra Bhanushali, Jinesh Narendra Jain, Rudra Mhatre, Sumit Sudhir Shingne  
**Last updated:** 2026-05-04