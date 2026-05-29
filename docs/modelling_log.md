# Modelling Log

## Objective

Develop a reproducible machine learning workflow capable of predicting Universal Thermal Climate Index (UTCI) conditions in Manhattan using environmental variables.

---

## Dataset

Input dataset:

`data/processed/manhattan-utci-clean.parquet`

Observations: 2208

Variables:

* timestamp
* air_temp_c
* humidity_pct
* wind_speed_ms
* solar_radiation
* utci

Target variable:

* utci

Feature variables:

* air_temp_c
* humidity_pct
* wind_speed_ms
* solar_radiation

---

## Data Splitting Strategy

A chronological split was used to avoid temporal leakage.

| Split      | Rows |
| ---------- | ---: |
| Train      | 1545 |
| Validation |  331 |
| Test       |  332 |

Split proportions:

* Train: 70%
* Validation: 15%
* Test: 15%

---

## Baseline Model

Model:

DummyRegressor(strategy="mean")

Purpose:

Provide a simple benchmark that predicts the mean UTCI value observed during training.

Results:

| Metric |  Value |
| ------ | -----: |
| MAE    |  3.862 |
| R²     | -1.133 |

---

## Random Forest Model

Model:

RandomForestRegressor

Configuration:

* n_estimators = 100
* random_state = 42

Results:

| Metric | Value |
| ------ | ----: |
| MAE    | 0.225 |
| R²     | 0.992 |

---

## Comparison

The Random Forest model substantially outperformed the baseline model.

Performance improvements:

* Lower prediction error (MAE)
* Strong explanatory power (R²)
* Consistent performance across the validation dataset

---

## Lessons Learned

* Chronological train/validation/test splitting is important for reproducible modelling.
* Baseline models provide essential context for evaluating model quality.
* Environmental variables show a strong relationship with UTCI estimates.
* Reproducible pipelines improve transparency and future maintainability.

---

## Saved Artifacts

Dataset files:

* manhattan-utci-clean.parquet
* manhattan-utci-train.parquet
* manhattan-utci-val.parquet
* manhattan-utci-test.parquet

Model file:

* models/baseline.joblib
