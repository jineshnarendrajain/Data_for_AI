# Data_for_AI — Urban Heat Prediction Pipeline (Sessions 1–4)

A complete academic data science workflow covering data profiling, quality assessment, data cleaning, feature engineering, machine learning modelling, and reproducible evaluation.

The project develops a predictive pipeline for estimating Universal Thermal Climate Index (UTCI) conditions in Manhattan using environmental variables.

---

# Project Objective

The objective of this project is to build a reproducible machine learning workflow capable of predicting thermal comfort conditions from environmental observations.

The workflow follows the progression of the course:

* Session 1 — Data Profiling
* Session 2 — Data Assessment & Decision Mapping
* Session 3 — Data Cleaning & Reproducibility
* Session 4 — Predictive Modelling & Evaluation

---

# Repository Structure

```text
Data_for_AI/
│
├── Brief/
│   └── problem-brief.md
│
├── data/
│   ├── raw/
│   └── processed/
│       ├── manhattan-utci-clean.parquet
│       ├── manhattan-utci-train.parquet
│       ├── manhattan-utci-val.parquet
│       └── manhattan-utci-test.parquet
│
├── docs/
│   ├── datasheets/
│   │
│   ├── data-cleaning-log.md
│   ├── data-quality-audit.md
│   ├── data-source-inventory.md
│   ├── data-to-decision-map.md
│   ├── function-design-checklist.md
│   ├── model_card.md
│   ├── modelling_log.md
│   ├── pipeline-architecture-v1.md
│   ├── pipeline-architecture-v2.md
│   ├── reproducibility-checklist.md
│   ├── problem-brief-v2.md
│   └── system-sketch-v0.md
│
├── models/
│   └── baseline.joblib
│
├── notebooks/
│   ├── 01-data-profiling.ipynb
│   ├── 02-data-cleaning.ipynb
│   └── 03-modelling.ipynb
│
├── src/
│   ├── clean_data.py
│   ├── split_data.py
│   └── baseline_model.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Dataset

The project uses historical environmental observations for Manhattan, New York City.

Variables include:

* Air Temperature (°C)
* Relative Humidity (%)
* Wind Speed (m/s)
* Solar Radiation (W/m²)

Target variable:

* Universal Thermal Climate Index (UTCI)

Final cleaned dataset:

```text
data/processed/manhattan-utci-clean.parquet
```

Dataset size:

* 2208 observations
* 6 variables

---

# Session Workflow

| Session   | Focus                           | Key Deliverables                                                 |
| --------- | ------------------------------- | ---------------------------------------------------------------- |
| Session 1 | Data Profiling                  | 01-data-profiling.ipynb                                          |
| Session 2 | Data Quality & Decision Mapping | Audit reports, datasheets, decision framework                    |
| Session 3 | Cleaning & Reproducibility      | clean_data.py, 02-data-cleaning.ipynb, Pipeline Architecture V1  |
| Session 4 | Modelling & Evaluation          | split_data.py, baseline_model.py, 03-modelling.ipynb, Model Card |

---

# Machine Learning Workflow

## Data Preparation

Raw environmental observations are cleaned and transformed into an analysis-ready dataset.

Output:

```text
manhattan-utci-clean.parquet
```

---

## Train / Validation / Test Split

Chronological splitting strategy:

| Dataset    | Records |
| ---------- | ------: |
| Train      |    1545 |
| Validation |     331 |
| Test       |     332 |

Responsible script:

```text
src/split_data.py
```

---

## Baseline Model

Algorithm:

```python
DummyRegressor(strategy="mean")
```

Performance:

| Metric |  Value |
| ------ | -----: |
| MAE    |  3.862 |
| R²     | -1.133 |

---

## Random Forest Model

Algorithm:

```python
RandomForestRegressor()
```

Performance:

| Metric | Value |
| ------ | ----: |
| MAE    | 0.225 |
| R²     | 0.992 |

Selected as the final model due to substantially improved predictive performance.

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

## Session 4 — Modelling

```bash
jupyter notebook notebooks/03-modelling.ipynb
```

---

## Run Scripts

Generate cleaned dataset:

```bash
python src/clean_data.py
```

Create train/validation/test splits:

```bash
python src/split_data.py
```

Train and evaluate models:

```bash
python src/baseline_model.py
```

---

# Documentation

The repository includes:

* Data Quality Audit
* Data Source Inventory
* Data Cleaning Log
* Datasheets
* Reproducibility Checklist
* Model Card
* Modelling Log
* Pipeline Architecture V1
* Pipeline Architecture V2

---

# Reproducibility

The workflow supports reproducibility through:

* Version-controlled source code
* Fixed random seed
* Explicit train/validation/test splits
* Saved model artifacts
* Documented modelling decisions
* Structured notebook workflow

---

# Future Work

Potential extensions include:

* Additional environmental predictors
* Spatial urban heat mapping
* Hyperparameter optimization
* Thermal stress classification
* Real-time environmental monitoring
* Decision-support dashboards

---

# Authors

Data_for_AI Project Team

Academic coursework submission for Sessions 1–4.
