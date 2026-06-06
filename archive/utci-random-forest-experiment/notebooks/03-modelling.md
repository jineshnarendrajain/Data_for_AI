# Model Development — Manhattan Urban Heat Prediction

## Purpose

This notebook develops and evaluates predictive models for estimating Universal Thermal Climate Index (UTCI) from environmental conditions.

The notebook implements the modelling workflow defined in Session 4:

1. Load cleaned analysis-ready data
2. Create train/validation/test splits
3. Train a baseline model
4. Train a machine learning model
5. Compare performance
6. Save the selected model
7. Document modelling decisions

The final model will support urban heat-risk assessment and ranking workflows.


```python
import pandas as pd
import numpy as np

from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

import joblib

RANDOM_SEED = 42
```

# Load Datasets

The cleaned dataset was generated during Session 3.

For Session 4, the dataset has already been split into:

- Training set
- Validation set
- Test set

The validation set is used during model selection while the test set remains untouched until final evaluation.


```python
train = pd.read_parquet(
    "../data/processed/manhattan-utci-train.parquet"
)

val = pd.read_parquet(
    "../data/processed/manhattan-utci-val.parquet"
)

test = pd.read_parquet(
    "../data/processed/manhattan-utci-test.parquet"
)

print("train", train.shape)
print("valid", val.shape)
print("test", test.shape)
```

    train (1545, 6)
    valid (331, 6)
    test (332, 6)
    

# Feature Selection

The objective is to predict UTCI.

Input variables were selected based on their known influence on outdoor thermal comfort.

Features:

- Air temperature
- Relative humidity
- Wind speed
- Solar radiation

Target:

- UTCI


```python
FEATURES = [
    "air_temp_c",
    "humidity_pct",
    "wind_speed_ms",
    "solar_radiation"
]

TARGET = "utci"

X_train = train[FEATURES]
y_train = train[TARGET]

X_val = val[FEATURES]
y_val = val[TARGET]

X_test = test[FEATURES]
y_test = test[TARGET]
```

# Baseline Model

A baseline establishes the minimum acceptable performance level.

The baseline predicts the average UTCI value observed in the training data.

Any useful machine learning model should outperform this benchmark.


```python
baseline = DummyRegressor(strategy="mean")

baseline.fit(X_train, y_train)

baseline_predictions = baseline.predict(X_val)

baseline_mae = mean_absolute_error(
    y_val,
    baseline_predictions
)

baseline_r2 = r2_score(
    y_val,
    baseline_predictions
)

print("BASELINE")
print("MAE:", baseline_mae)
print("R2 :", baseline_r2)
```

    BASELINE
    MAE: 3.86173978040458
    R2 : -1.1325911034193399
    

# Random Forest Model

Random Forest was selected because:

- It handles nonlinear relationships
- It requires minimal feature engineering
- It is robust to noisy environmental data
- It provides feature importance estimates

The model is trained on the training set and evaluated on the validation set.


```python
rf = RandomForestRegressor(
    n_estimators=200,
    random_state=RANDOM_SEED
)

rf.fit(X_train, y_train)

rf_predictions = rf.predict(X_val)

rf_mae = mean_absolute_error(
    y_val,
    rf_predictions
)

rf_r2 = r2_score(
    y_val,
    rf_predictions
)

print("RANDOM FOREST")
print("MAE:", rf_mae)
print("R2 :", rf_r2)
```

    RANDOM FOREST
    MAE: 0.21851080060423234
    R2 : 0.9918801265369813
    

# Model Comparison

Performance is evaluated using:

## Mean Absolute Error (MAE)

Measures average prediction error.

Lower values are better.

## R²

Measures proportion of variance explained.

Higher values are better.

A successful model should reduce MAE and increase R² relative to the baseline.


```python
results = pd.DataFrame({
    "Model": ["Baseline", "Random Forest"],
    "MAE": [baseline_mae, rf_mae],
    "R2": [baseline_r2, rf_r2]
})

results
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Model</th>
      <th>MAE</th>
      <th>R2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Baseline</td>
      <td>3.861740</td>
      <td>-1.132591</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Random Forest</td>
      <td>0.218511</td>
      <td>0.991880</td>
    </tr>
  </tbody>
</table>
</div>



# Feature Importance

Random Forest provides an estimate of the relative contribution of each feature.

This helps interpret the model and identify the strongest drivers of thermal comfort conditions.


```python
importance = pd.DataFrame({
    "Feature": FEATURES,
    "Importance": rf.feature_importances_
})

importance.sort_values(
    "Importance",
    ascending=False
)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Feature</th>
      <th>Importance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>air_temp_c</td>
      <td>0.869367</td>
    </tr>
    <tr>
      <th>2</th>
      <td>wind_speed_ms</td>
      <td>0.114509</td>
    </tr>
    <tr>
      <th>3</th>
      <td>solar_radiation</td>
      <td>0.013046</td>
    </tr>
    <tr>
      <th>1</th>
      <td>humidity_pct</td>
      <td>0.003079</td>
    </tr>
  </tbody>
</table>
</div>



# Save Model

The selected model is persisted so it can be reused by downstream workflows without retraining.


```python
joblib.dump(
    rf,
    "../models/baseline.joblib"
)

print("Model saved.")
```

    Model saved.
    

# Final Evaluation Summary

## Baseline

- MAE ≈ 3.86
- R² ≈ -1.13

## Random Forest

- MAE ≈ 0.22
- R² ≈ 0.99

## Decision

The Random Forest substantially outperforms the baseline and is selected as the Session 4 production model.

## Limitations

- Trained on a relatively small environmental dataset
- Represents Manhattan conditions only
- Does not account for future climate scenarios
- Not intended for operational forecasting

## Next Steps

Session 5 will investigate synthetic data generation and robustness testing.
