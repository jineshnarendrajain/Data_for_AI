# Pipeline Architecture V2

## Purpose

Pipeline Architecture V2 extends the Session 3 data preparation workflow by introducing data splitting, model training, model evaluation, and model persistence.

The objective of this pipeline is to develop a reproducible machine learning workflow capable of predicting Universal Thermal Climate Index (UTCI) conditions from environmental variables for urban heat assessment.

---

## Pipeline Overview

```text
Historical Environmental Data
        ↓
Data Validation & Cleaning
        ↓
Feature Engineering
        ↓
manhattan-utci-clean.parquet
        ↓
split_data.py
        ↓
Train / Validation / Test Datasets
        ↓
Baseline Model
        ↓
Random Forest Regressor
        ↓
Model Evaluation
        ↓
Model Persistence
        ↓
models/baseline.joblib
```

---

## Pipeline Components

### 1. Data Acquisition

Purpose:

Acquire historical environmental observations for Manhattan, New York City.

Source:

* Open-Meteo Historical Weather Archive

Variables collected:

* Air Temperature (°C)
* Relative Humidity (%)
* Wind Speed (m/s)
* Solar Radiation (W/m²)

Output:

* Raw environmental observations

---

### 2. Data Cleaning and Validation

Purpose:

Prepare the raw environmental observations for machine learning analysis.

Cleaning operations:

* Timestamp validation
* Missing value inspection
* Data type standardization
* Range validation
* Feature consistency checks

Responsible script:

* `src/clean_data.py`

Output:

* `data/processed/manhattan-utci-clean.parquet`

Dataset size:

* 2208 observations
* 6 variables

---

### 3. Feature Engineering

Purpose:

Generate the target variable required for predictive modelling.

Generated feature:

* Universal Thermal Climate Index (UTCI)

Model inputs:

* air_temp_c
* humidity_pct
* wind_speed_ms
* solar_radiation

Target variable:

* utci

Output:

* Analysis-ready modelling dataset

---

### 4. Data Splitting

Purpose:

Create leakage-safe datasets for training, validation, and testing.

Method:

* Chronological split
* No random shuffling
* Temporal ordering preserved

Responsible script:

* `src/split_data.py`

Outputs:

* `data/processed/manhattan-utci-train.parquet`
* `data/processed/manhattan-utci-val.parquet`
* `data/processed/manhattan-utci-test.parquet`

Split summary:

| Dataset    | Records |
| ---------- | ------: |
| Train      |    1545 |
| Validation |     331 |
| Test       |     332 |

---

### 5. Baseline Model

Purpose:

Establish a benchmark performance level.

Algorithm:

* DummyRegressor(strategy="mean")

Evaluation Results:

| Metric |  Value |
| ------ | -----: |
| MAE    |  3.862 |
| R²     | -1.133 |

Interpretation:

The baseline predicts the average UTCI observed during training and serves as the minimum acceptable benchmark.

---

### 6. Predictive Model

Purpose:

Predict UTCI from environmental conditions.

Algorithm:

* Random Forest Regressor

Configuration:

* n_estimators = 100
* random_state = 42

Responsible script:

* `src/baseline_model.py`

Inputs:

* air_temp_c
* humidity_pct
* wind_speed_ms
* solar_radiation

Output:

* Predicted UTCI value

---

### 7. Model Evaluation

Purpose:

Assess predictive performance using the validation dataset.

Metrics:

* Mean Absolute Error (MAE)
* Coefficient of Determination (R²)

Validation Results:

| Model         |   MAE |     R² |
| ------------- | ----: | -----: |
| Baseline      | 3.862 | -1.133 |
| Random Forest | 0.225 |  0.992 |

Outcome:

The Random Forest model substantially outperformed the baseline model and was selected as the final model.

---

### 8. Model Persistence

Purpose:

Save the trained model for future reuse.

Stored Artifact:

* `models/baseline.joblib`

Benefits:

* Reproducible predictions
* Reduced retraining requirements
* Consistent deployment workflow

---

## Repository Artifacts

### Data

```text
data/processed/
├── manhattan-utci-clean.parquet
├── manhattan-utci-train.parquet
├── manhattan-utci-val.parquet
└── manhattan-utci-test.parquet
```

### Source Code

```text
src/
├── clean_data.py
├── split_data.py
└── baseline_model.py
```

### Models

```text
models/
└── baseline.joblib
```

### Notebooks

```text
notebooks/
├── 01-data-profiling.ipynb
├── 02-data-cleaning.ipynb
└── 03-modelling.ipynb
```

---

## Reproducibility Strategy

The pipeline was designed to be reproducible through:

* Fixed random seed (42)
* Version-controlled source code
* Explicit train/validation/test splits
* Saved model artifacts
* Documented evaluation metrics
* Structured notebook workflow

---

## Future Extensions

Potential improvements include:

* Additional environmental predictors
* Spatially explicit modelling
* Cross-validation experiments
* Hyperparameter optimization
* Thermal stress classification models
* Integration with urban heat mapping workflows

---

## Summary

Pipeline Architecture V2 transforms validated environmental observations into a deployable machine learning workflow capable of predicting UTCI conditions.

The workflow incorporates:

* Data cleaning
* Feature engineering
* Dataset splitting
* Baseline benchmarking
* Random Forest modelling
* Model evaluation
* Artifact persistence

and establishes the foundation for future urban heat analysis and decision-support applications.
