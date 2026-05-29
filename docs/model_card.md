# Model Card

## Model Name

Manhattan UTCI Prediction Model

---

## Model Type

Random Forest Regressor

---

## Intended Use

The model is intended to estimate UTCI conditions from environmental variables for exploratory urban heat analysis.

Potential applications:

* Urban heat assessment
* Thermal stress exploration
* Environmental data analysis
* Educational modelling workflows

---

## Inputs

The model uses:

* Air temperature (°C)
* Relative humidity (%)
* Wind speed (m/s)
* Solar radiation (W/m²)

---

## Output

Predicted UTCI value.

---

## Training Data

Source:

Historical environmental observations for Manhattan, New York City.

Dataset size:

2208 observations.

---

## Evaluation Results

Baseline:

* MAE = 3.862
* R² = -1.133

Random Forest:

* MAE = 0.225
* R² = 0.992

---

## Limitations

This model should not be used for:

1. Public safety decisions.
2. Medical risk assessment.
3. Operational weather forecasting.
4. Emergency management.
5. Climate policy decisions.

The model was developed as part of an academic urban heat workflow and has not undergone operational validation.

---

## Ethical Considerations

Outputs should be interpreted as analytical estimates rather than authoritative predictions.

Human review remains necessary when using thermal comfort information in real-world contexts.

---

## Version

Version 1.0

Session 4 Modelling Deliverable
