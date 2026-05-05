# Output Sketch v0

---

## What is the final output?

- [x] Dashboard (interactive map interface)

**One-sentence description of the output:**

An interactive spatial decision-support map that visualises heat exposure risk across Manhattan using land surface temperature (LST) and vegetation (NDVI) data, enabling identification of priority zones for heat mitigation.

---

## Who is the user?

A climate resilience analyst at a New York City municipal agency, working on urban heat mitigation planning and resource allocation.

### What does the user already know?

- Familiar with GIS-based spatial data  
- Understands urban heat island concepts  
- Uses maps and data to support policy decisions  

### What does the user NOT know?

- Exact street-block-level heat hotspots  
- Where vegetation is insufficient relative to heat  
- Which specific zones should be prioritised for intervention  

---

## The top 3 actions this output enables

1. Identify the top 5–10 highest heat-risk zones in Manhattan  
2. Compare heat levels with vegetation distribution across locations  
3. Select priority areas for targeted interventions such as tree planting or shading  

---

## Sketch (layout description)

- **Top:** Title + legend (heat scale and vegetation scale)  
- **Center:** Interactive map displaying Manhattan  
- **Layers:**
  - LST heat map (blue → red)
  - NDVI vegetation map (brown → green)
  - Heat risk classification (green → yellow → red)  
- **Side panel (optional):**
  - Toggle layers on/off  
  - Display selected point values (LST, NDVI, risk score)  
- **Bottom (optional):**
  - List of top 5–10 priority zones  

---

## Example Output (Derived Results)

The system identifies high-risk zones using a rule-based combination of high LST and low NDVI.

### Top Priority Zones (Sample)

| Rank | Latitude | Longitude | Risk Score |
|---|---|---|---|
| 1 | 40.7103 | -73.9851 | 1.09 |
| 2 | 40.7436 | -73.9949 | 0.98 |
| 3 | 40.7449 | -73.9762 | 0.95 |
| 4 | 40.7183 | -73.9921 | 0.94 |
| 5 | 40.7542 | -73.9872 | 0.92 |

### Interpretation

- High-risk zones are concentrated in dense urban areas with low vegetation  
- Lower Manhattan and Midtown emerge as priority intervention zones  
- These areas are dominated by impervious surfaces such as concrete and asphalt  

---

## What this output is NOT

- A real-time monitoring system  
- A full thermal comfort model (does not include humidity, wind, or shading effects)  

---

## What would make a user trust this output?

Clear communication of:
- Data sources (Landsat, Sentinel-2, NYC datasets)  
- Methodology (rule-based classification)  
- Limitations (proxy-based analysis and resolution constraints)  

---

## How does this connect to the rest of the work?

| Seminar artifact | How it feeds into this output |
|---|---|
| Problem brief (v2) | Defines the decision: prioritising heat mitigation zones |
| Datasheets | Provide data source credibility and transparency |
| Quality audit | Explains limitations and uncertainty |
| Decision map | Links questions to datasets |
| System sketch | Describes how the output is generated |
| (Future) Model card | Documents model logic and assumptions |
| (Future) Failure gallery | Highlights known limitations and edge cases |

---

## Limitations in Output

- Uses satellite-derived proxies (LST, NDVI), not direct thermal comfort measurements  
- Hotspots are pixel-based approximations of street-block conditions  
- Temporal scope limited to selected summer period  
- Does not include socio-economic or behavioural factors  

---

## Conclusion

The output provides a clear, interpretable, and actionable interface for identifying urban heat risk zones in Manhattan. It enables data-driven prioritisation of interventions, supporting urban climate resilience planning with transparent assumptions and limitations.

---

## Sign-off

**Team:** Dhruvil Mahendra Bhanushali, Jinesh Narendra Jain, Rudra Mhatre, Sumit Sudhir Shingne  
**Last updated:** 2026-05-04