# Data_for_AI — Session 1–3 Deliverables

A complete academic data pipeline project combining data profiling, exploratory analysis, and reproducible data cleaning.

## Repository Structure

```
Data_for_AI/
├── Brief/
│   └── problem-brief.md                 (Session 1: Problem definition)
│
├── data/
│   ├── raw/                             (Raw datasets — gitignored)
│   ├── processed/                       (Cleaned datasets)
│   └── profile-summary.json             (Data profiling summary)
│
├── docs/
│   ├── datasheets/
│   │   ├── landsat8-lst.md             (Landsat 8 LST datasheet — Session 3)
│   │   └── sentinel2-ndvi.md           (Sentinel-2 NDVI datasheet)
│   │
│   ├── data-cleaning-log.md            (Session 3: Cleaning decisions)
│   ├── function-design-checklist.md    (Session 3: Module design checklist)
│   ├── pipeline-architecture-v1.md     (Session 3: Architecture design)
│   ├── reproducibility-checklist.md    (Session 3: Reproducibility standards)
│   │
│   ├── data-quality-audit.md           (Session 2: Quality assessment)
│   ├── data-source-inventory.md        (Session 2: Dataset evaluation)
│   ├── data-to-decision-map.md         (Session 2: Decision framework)
│   ├── problem-brief-v2.md             (Session 2: Problem loopback)
│   └── system-sketch-v0.md             (Session 2: System architecture)
│
├── notebooks/
│   ├── 01-data-profiling.ipynb         (Session 1: EDA & profiling)
│   └── 02-data-cleaning.ipynb          (Session 3: Data cleaning pipeline)
│
├── src/
│   └── clean_data.py                   (Session 3: Cleaning module)
│
├── .gitignore
├── README.md
└── requirements.txt                    (Session 3: Dependencies)
```

## Session Workflow

| Session | Phase | Focus | Key Artifacts |
|---------|-------|-------|---|
| **1** | Profiling | Data understanding & exploration | `01-data-profiling.ipynb`, `profile-summary.json` |
| **2** | Analysis | Data quality & decision mapping | `data-quality-audit.md`, `data-to-decision-map.md`, datasheets |
| **3** | Cleaning | Reproducible pipeline & modularity | `clean_data.py`, `02-data-cleaning.ipynb`, `pipeline-architecture-v1.md` |

## Running the Pipeline

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run data profiling (Session 1)
```bash
jupyter notebook notebooks/01-data-profiling.ipynb
```

### 3. Run data cleaning (Session 3)
```bash
jupyter notebook notebooks/02-data-cleaning.ipynb
```

Or import the cleaning module directly:
```python
from src.clean_data import clean_data
```

## Key Design Principles

- **Reproducibility**: All cleaning steps documented in `data-cleaning-log.md`
- **Modularity**: `clean_data.py` exports functions for reuse
- **Provenance**: Every dataset has a datasheet in `docs/datasheets/`
- **Traceability**: Data pipeline architecture in `pipeline-architecture-v1.md`
