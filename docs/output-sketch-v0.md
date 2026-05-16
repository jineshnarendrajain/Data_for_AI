# Output Sketch v0

---

## What is the final output?

* [x] Interactive spatial dashboard

### One-sentence description of the output

An interactive geospatial decision-support dashboard that visualises relative urban heat exposure patterns across Manhattan using Land Surface Temperature (LST) and vegetation density indicators (NDVI) to support heat mitigation prioritisation.

---

## Who is the user?

A climate resilience or urban planning analyst working within a New York City municipal agency.

### What does the user already know?

* Basic GIS and spatial analysis workflows
* Urban heat island concepts
* Heat mitigation planning strategies
* Interpretation of environmental maps and spatial indicators

### What does the user NOT know?

* Which neighbourhood-scale areas consistently exhibit elevated surface temperatures
* How vegetation distribution spatially relates to heat exposure patterns
* Which zones should be prioritised first for mitigation interventions under limited budgets

---

## The top 3 actions this output enables

1. Identify neighbourhood-scale urban heat hotspot zones across Manhattan
2. Compare vegetation distribution against surface temperature patterns
3. Prioritise areas for urban heat mitigation interventions such as tree planting, greening, or shading infrastructure

---

## Sketch (layout description)

### Main Interface

* Interactive Manhattan map
* Layer controls
* Heat-risk legend
* Dataset transparency information

### Map Layers

* Land Surface Temperature (LST) layer
* NDVI vegetation layer
* Relative heat-risk classification layer
* Optional NYC Heat Vulnerability Index comparison layer

### Side Panel

* Toggle datasets on/off
* Display selected pixel or zone statistics
* Show relative hotspot classification
* Explain analytical limitations and assumptions

### Bottom Panel (Optional)

* Ranked list of priority intervention zones
* Summary statistics for selected regions

---

## Example Output (Illustrative Only)

The system identifies relative hotspot zones using a rule-based combination of:

* Higher Land Surface Temperature values
* Lower NDVI vegetation values

### Sample Priority Zones

| Rank | Approximate Area                 | Relative Risk Level |
| ---- | -------------------------------- | ------------------- |
| 1    | Lower Manhattan                  | High                |
| 2    | Midtown Commercial Corridor      | High                |
| 3    | East Harlem Built-Up Zone        | Medium–High         |
| 4    | Upper Midtown Dense Corridor     | Medium–High         |
| 5    | Lower East Side Dense Urban Area | Medium              |

### Interpretation

* Areas with dense impervious surfaces and limited vegetation tend to exhibit elevated surface temperatures
* Vegetated areas such as Central Park generally correspond with lower relative heat exposure
* Results represent neighbourhood-scale thermal patterns rather than exact street-level thermal conditions

---

## What this output is NOT

* A real-time monitoring system
* A predictive climate forecasting platform
* A full human thermal comfort model
* A building-scale or pedestrian-scale simulation system

The system does not directly account for:

* Humidity
* Wind
* Shade geometry
* Human activity patterns
* Indoor environmental conditions

---

## What would make a user trust this output?

Clear communication of:

* Data provenance and sources
* Processing methodology
* Classification logic
* Known limitations
* Resolution constraints
* Validation comparisons with external datasets

---

## How does this connect to the rest of the work?

| Seminar artifact       | Contribution to output                            |
| ---------------------- | ------------------------------------------------- |
| Problem Brief v1/v2    | Defines the planning decision and project scope   |
| Datasheets             | Documents dataset suitability and limitations     |
| Data Quality Audit     | Identifies uncertainty and preprocessing concerns |
| Data → Decision Map    | Connects analytical questions to datasets         |
| System Sketch          | Defines pipeline structure and processing logic   |
| Future Model Card      | Will document classification assumptions          |
| Future Failure Gallery | Will communicate known edge cases and weaknesses  |

---

## Limitations in Output

* Uses satellite-derived proxy indicators rather than direct thermal comfort measurements
* Results are dependent on Summer 2018 imagery only
* Spatial resolution limits fine-scale urban interpretation
* Classification logic is rule-based and non-predictive
* Vegetation indicators represent broad green-cover patterns rather than exact canopy structure

---

## Conclusion

The proposed output provides an interpretable and reproducible geospatial decision-support tool for identifying relative urban heat exposure patterns across Manhattan.

The dashboard supports evidence-based prioritisation of heat mitigation interventions while maintaining transparency about data limitations, analytical assumptions, and uncertainty.
