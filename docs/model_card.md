# Model Card — Manhattan Heat Risk Prediction Model

## Model Overview

### Model Name

Heat Risk Prediction Model

### Version

1.0

### Date

June 2026

### Model Type

Random Forest Regressor

### Purpose

The model predicts relative urban heat risk across Manhattan using satellite-derived environmental indicators.

The model supports urban heat mitigation planning and decision-support workflows by estimating heat-risk conditions from environmental observations.

---

## Intended Use

### Primary Use

Predict relative heat-risk scores using:

* Land Surface Temperature (LST)
* Vegetation Density (NDVI)

### Intended Users

* Urban planners
* Climate adaptation practitioners
* Environmental analysts
* Municipal decision-makers

### Decision-Support Applications

* Urban greening prioritisation
* Heat mitigation planning
* Hotspot identification
* Environmental monitoring

---

## Training Data

### Dataset

```text
manhattan_heat_risk_training.csv
```

### Data Source

The dataset was generated using Google Earth Engine from:

#### Landsat 8 Collection 2 Level 2

```text
LANDSAT/LC08/C02/T1_L2
```

Used to derive:

```text
Land Surface Temperature (LST)
```

#### Sentinel-2 Surface Reflectance

```text
COPERNICUS/S2_SR
```

Used to derive:

```text
Normalized Difference Vegetation Index (NDVI)
```

### Study Area

```text
Manhattan
New York City
United States
```

### Study Period

```text
2018-06-01
to
2018-08-31
```

### Dataset Size

| Metric          |           Value |
| --------------- | --------------: |
| Samples         |          10,000 |
| Features        |               2 |
| Target Variable | Heat Risk Score |

---

## Features

### Inputs

| Feature | Description              |
| ------- | ------------------------ |
| LST     | Land Surface Temperature |
| NDVI    | Vegetation Density Index |

### Target

| Variable | Description              |
| -------- | ------------------------ |
| Risk     | Relative heat-risk score |

---

## Model Development

### Train/Test Split

| Dataset  | Samples |
| -------- | ------: |
| Training |   8,000 |
| Testing  |   2,000 |

### Random Seed

```text
42
```

### Algorithm

```python
RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
```

---

## Evaluation Results

### Baseline Model

| Metric |   Value |
| ------ | ------: |
| MAE    |  0.2019 |
| R²     | -0.0007 |

### Random Forest Model

| Metric |  Value |
| ------ | -----: |
| MAE    | 0.0021 |
| RMSE   | 0.0044 |
| R²     | 0.9997 |

---

## Feature Importance

| Feature | Importance |
| ------- | ---------: |
| NDVI    |     0.6336 |
| LST     |     0.3664 |

The model identifies vegetation density as the strongest predictor of relative heat risk within the study area.

---

## Limitations

### Geographic Limitation

The model was trained exclusively on Manhattan data and should not be assumed to generalise to other cities without validation.

### Temporal Limitation

The model represents Summer 2018 conditions only.

### Methodological Limitation

The model reproduces a rule-based heat-risk framework derived from environmental indicators.

It should not be interpreted as discovering causal relationships.

### Interpretation Limitation

Predicted values represent relative heat risk rather than direct measurements of human thermal stress or health outcomes.

---

## Ethical Considerations

The model is intended to support evidence-based planning decisions.

Predictions should be used alongside local knowledge, field observations, and additional environmental assessments.

The model should not be used as the sole basis for resource allocation decisions.

---

## Reproducibility

Model artifact:

```text
models/heat_risk_model.joblib
```

Training notebook:

```text
notebooks/04-heat-risk-modelling.ipynb
```

Dataset:

```text
data/processed/manhattan_heat_risk_training.csv
```

The workflow is reproducible through:

* Public satellite datasets
* Documented processing methods
* Fixed random seed
* Version-controlled code
* Saved model artifact

---

## Summary

The Heat Risk Prediction Model successfully estimates relative urban heat-risk conditions using satellite-derived environmental indicators.

The model achieves high predictive accuracy and provides the AI component required for downstream urban heat decision-support applications.
