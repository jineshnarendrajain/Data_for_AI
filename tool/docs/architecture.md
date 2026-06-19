# Architecture — Manhattan Heat Mitigation Decision Support Tool

The application is organised as five cooperating layers. The trained model is **one
component** inside the workflow, not the final output.

```text
Data Layer
   ↓
Prediction Layer
   ↓
Recommendation Engine
   ↓
Planning Layer
   ↓
Export Layer
```

All layers live in `tool/app.py` as modular, individually testable functions. The
Streamlit UI is confined to `main()` so the logic functions can be imported and tested
without launching a server.

---

## Data Flow

```text
manhattan_heat_risk_training.csv
   ↓  load_data()
keep [LST, NDVI, Risk, latitude, longitude]
   ↓  drop NaN · sort by Risk (desc)
top 500 highest-risk locations  +  Rank (1..500)
   ↓
in-memory DataFrame used by every downstream layer
```

- Source: a **copy** of the Session-5 dataset at `tool/data/manhattan_heat_risk_training.csv`.
- The raw file also contains `system:index` and `.geo`; these are dropped.
- Cached with `@st.cache_data` so the CSV is parsed once per session.
- Latitude/longitude are used directly — **no geocoding** is performed.

---

## Model Flow

```text
heat_risk_model.joblib  (RandomForestRegressor)
   ↓  load_model()  (cached with @st.cache_resource)
predict_risk(model, LST, NDVI)
   → DataFrame({"LST":..,"NDVI":..})   # exact feature names/order the model was fit on
   → model.predict(...)
   → predicted Risk
```

- Inputs: **LST, NDVI**. Output: **predicted Risk**.
- Predictions always go through a named DataFrame (`_features_frame`) to match
  `model.feature_names_in_ = ['LST','NDVI']`, avoiding scikit-learn feature-name warnings.
- The model is **not retrained**; it is treated as the production model.
- `scikit-learn` is pinned to `1.6.1` (the training version) so the pickle loads cleanly.

---

## Recommendation Flow

```text
selected hotspot (LST, NDVI)
   ↓  evaluate_interventions()
baseline current_risk = predict_risk(LST, NDVI)
   ↓  for each of 4 interventions:
        simulate:  new_LST  = LST  + lst_delta
                   new_NDVI = clip(NDVI + ndvi_delta, -1, 1)
        re-score:  new_risk = predict_risk(new_LST, new_NDVI)
        measure:   reduction       = current_risk - new_risk
                   reduction_%      = reduction / |current_risk| * 100
                   cost_effectiveness = reduction / (cost / 1000)
   ↓  rank_interventions(by="impact"|"cost")
two rankings: Maximum Impact  &  Cost Effectiveness
```

Intervention assumptions (planning simulations, not engineering guarantees):

| Intervention | Simulation | Cost |
| --- | --- | --- |
| Tree Planting | NDVI + 0.15 | $10,000 |
| Shade Structures | LST − 3 °C | $20,000 |
| Green Infrastructure | NDVI + 0.10, LST − 2 °C | $50,000 |
| Cooling Infrastructure | LST − 2 °C | $100,000 |

The engine ranks options; **the planner makes the final decision.**

---

## Planning Workflow

```text
select hotspot (map / table / selectbox, all synced via session_state.selected_rank)
   ↓
review recommendations + comparison mode
   ↓
choose intervention → "Add to plan"
   ↓  add guarded by remaining budget (rejected if cost > remaining)
session_state.plan  (list of plan items, multiple sites & interventions)
   ↓
Planning Dashboard recomputes live:
   total sites · budget used · remaining · average risk reduction
   · highest-impact intervention · total estimated risk reduction
```

Budget is user-configurable: default **$500,000**, min **$50,000**, max **$5,000,000**.
Over-budget additions are blocked, and an over-budget plan is flagged.

**Demo mode** (`run_demo`) auto-builds a plan greedily: it walks the highest-risk sites and
applies each site's most cost-effective affordable intervention until the $500,000 budget
is spent or the site cap is reached.

---

## Export Workflow

```text
session_state.plan
   ↓  plan_to_dataframe() → fixed export schema
   ↓  plan_to_csv()
st.download_button → manhattan_intervention_plan.csv
```

Exported columns:

```text
Rank, Latitude, Longitude, Current Risk,
Selected Intervention, Predicted Risk, Risk Reduction, Cost
```

---

## Module map (`tool/app.py`)

| Layer | Functions |
| --- | --- |
| Data | `load_data` |
| Prediction | `load_model`, `predict_risk`, `predict_risk_batch`, `clip_ndvi`, `_features_frame` |
| Recommendation | `evaluate_interventions`, `rank_interventions` |
| Planning | `plan_total_cost`, `_make_plan_item`, `run_demo` |
| Export | `plan_to_dataframe`, `plan_to_csv` |
| UI helpers | `risk_color`, `nearest_rank` |
| UI | `main` (Streamlit only) |
