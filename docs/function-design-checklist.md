# Function Design Checklist

> This checklist was used while structuring the exploratory modular
> cleaning workflow implemented in `src/clean_data.py` for the Manhattan
> Urban Heat Dataset.

---

# The minimum bar — every function

---

## `validate_crs`

- [x] Function name describes the transform clearly
- [x] Single-purpose function
- [x] Includes type hints
- [x] Includes docstring
- [x] Includes usage example
- [x] Includes assertion
- [x] Testable independently of full raster workflow
- [ ] Fully pure function (contains print statements)

---

## `apply_cloud_mask`

- [x] Function name describes the transform clearly
- [x] Single-purpose function
- [x] Includes type hints
- [x] Includes docstring
- [x] Includes usage example
- [x] Includes assertion
- [x] Testable independently of full raster workflow
- [ ] Fully pure function (contains print statements)

---

## `handle_nodata_pixels`

- [x] Function name describes the transform clearly
- [x] Single-purpose function
- [x] Includes type hints
- [x] Includes docstring
- [x] Includes usage example
- [x] Includes assertion
- [x] Testable independently of full raster workflow
- [ ] Fully pure function (contains print statements)

---

## `validate_lst_range`

- [x] Function name describes the transform clearly
- [x] Single-purpose function
- [x] Includes type hints
- [x] Includes docstring
- [x] Includes usage example
- [x] Includes assertion
- [x] Testable independently of full raster workflow
- [ ] Fully pure function (contains print statements)

---

## `normalize_ndvi`

- [x] Function name describes the transform clearly
- [x] Single-purpose function
- [x] Includes type hints
- [x] Includes docstring
- [x] Includes usage example
- [x] Includes assertion
- [x] Testable independently of full raster workflow
- [ ] Fully pure function (contains print statements)

---

## `remove_hotspot_artifacts`

- [x] Function name describes the transform clearly
- [x] Single-purpose function
- [x] Includes type hints
- [x] Includes docstring
- [x] Includes usage example
- [x] Includes assertion
- [x] Testable independently of full raster workflow
- [ ] Fully pure function (contains print statements)

---

## `integrate_rasters`

- [x] Function name describes the transform clearly
- [x] Single-purpose function
- [x] Includes type hints
- [x] Includes docstring
- [x] Includes usage example
- [x] Includes assertion
- [x] Testable independently of full raster workflow
- [ ] Fully pure function (contains print statements)

---

## `assert_clean_invariants`

- [x] Function name describes the transform clearly
- [x] Single-purpose function
- [x] Includes type hints
- [x] Includes docstring
- [x] Includes assertion
- [x] Testable independently of full raster workflow
- [ ] Includes usage example
- [ ] Fully pure function (contains print statements)

---

## `clean_urban_heat_dataset`

- [x] Function name describes the transform clearly
- [x] Pipeline orchestration isolated from individual transforms
- [x] Includes type hints
- [x] Includes docstring
- [x] Assertions delegated to helper functions
- [ ] Fully pure function (pipeline orchestration contains print statements)

---

# Structural review

The cleaning workflow was intentionally separated into modular
single-purpose functions rather than a single monolithic cleaning
routine.

The pipeline currently separates:

- CRS validation
- cloud masking
- NoData handling
- LST validation
- NDVI normalization
- hotspot cleaning
- raster integration
- invariant assertions

This structure was chosen to improve:
- readability,
- modularity,
- reproducibility,
- and future extensibility.

---

# Known limitations

| Limitation | Reason |
|---|---|
| Some helper functions still contain print statements | Pipeline remains exploratory rather than production-grade |
| Raster operations are partially conceptual | Full Earth Engine implementation refinement remains future work |
| Unit testing framework not yet implemented | Project scope focused primarily on pipeline architecture and cleaning structure |

---

# Notebook → module promotion review

The following workflow components were promoted from exploratory notebook
logic into modular pipeline functions:

| Workflow Component | Promoted to module? |
|---|---|
| CRS validation | Yes |
| Cloud masking workflow | Yes |
| NoData handling | Yes |
| LST validation | Yes |
| NDVI normalization | Yes |
| Hotspot cleaning | Yes |
| Raster integration | Yes |

The notebook remains the exploratory environment while
`src/clean_data.py` serves as the reproducibility-oriented modular
pipeline layer.

---

# Final assessment

The current cleaning workflow satisfies the majority of the Session 3
function design expectations while remaining appropriately scoped for an
exploratory urban heat analysis project using Landsat and Sentinel
imagery.

The workflow prioritizes:
- modularity,
- interpretability,
- deterministic structure,
- and reproducibility-oriented organization

over full production-grade remote sensing implementation.