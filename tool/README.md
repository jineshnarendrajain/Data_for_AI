# Manhattan Heat Mitigation Decision Support Tool

Session 6 deliverable — a Streamlit decision-support system that turns the trained
Random Forest heat-risk model into a funded, exportable urban-heat intervention plan
for an NYC urban planner.

## What it does

`Data → Model Prediction → Recommendation Engine → Planning → Export`

- Maps the **top 500 highest-risk** locations in Manhattan.
- Lets you select a hotspot from the **map** or the **ranked table**.
- Simulates four interventions, re-scores each with the model, and **ranks them by
  impact and by cost-effectiveness**.
- Tracks a configurable **budget** as you add interventions to a plan.
- **Exports** the plan as CSV, and includes a one-click **demo scenario** for presenting.

## Run

```bash
# from the repository root
pip install -r tool/requirements.txt
streamlit run tool/app.py
```

The app is self-contained: it reads its own copies of the dataset
(`tool/data/manhattan_heat_risk_training.csv`) and model
(`tool/models/heat_risk_model.joblib`). The original Session 1–5 artifacts are not
modified.

## Layout

| Tab | Purpose |
| --- | ------- |
| 🗺️ Risk Map | Interactive Folium map, risk-coloured markers, click to select |
| 📋 Priority Locations | Searchable ranked table, select a row to choose a location |
| 🧠 Decision Support | Current conditions, ranked recommendations, comparison mode, add-to-plan |
| 📊 Plan & Export | Planning dashboard metrics, plan table, CSV export |

See [`docs/tool-prd.md`](docs/tool-prd.md) and [`docs/architecture.md`](docs/architecture.md)
for the full specification and architecture.
