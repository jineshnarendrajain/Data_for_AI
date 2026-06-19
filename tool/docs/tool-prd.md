# Tool PRD — Manhattan Heat Mitigation Decision Support Tool

## Purpose

Convert the Session-5 Random Forest heat-risk model into a **decision-support system**
that helps allocate a limited heat-mitigation budget across Manhattan. The tool answers
three planning questions:

- **Where** should interventions be deployed first?
- **Which** intervention produces the largest expected reduction in heat risk?
- **How** should a limited budget be allocated across sites?

The model is a component, not the deliverable. The deliverable is the decision workflow:

```text
Data → Model → Recommendation → Decision
```

…understandable by a non-technical audience in roughly 60 seconds.

## User

**NYC Urban Planner.** Works with constrained resources, cannot mitigate heat everywhere,
and needs evidence-based prioritisation. No machine-learning knowledge is required to
operate the tool.

## Features

- **Interactive Manhattan risk map** — top 500 highest-risk locations, risk-based marker
  colouring, popups showing Risk / LST / NDVI / latitude / longitude, click-to-select.
- **Priority locations table** — ranked by risk, searchable, row-selectable; selection is
  synchronised with the map and the decision panel.
- **Decision support panel** — current conditions for the selected hotspot (Risk, LST,
  NDVI, coordinates).
- **Recommendation engine** — automatically simulates all four interventions, re-scores
  each with the model, and ranks them by expected risk reduction.
- **Intervention comparison mode** — side-by-side options with cost-effectiveness and two
  rankings: **Maximum Impact** and **Cost Effectiveness** (risk reduction per $1,000).
- **Intervention planning** — add interventions across multiple sites to a single plan.
- **Budget management** — configurable budget ($50k–$5M, default $500k); spending beyond
  the remaining budget is prevented.
- **Planning dashboard** — live totals: sites selected, budget used, remaining budget,
  average risk reduction, highest-impact intervention, total estimated risk reduction.
- **Export** — downloadable CSV intervention plan.
- **Demo mode** — one-click `$500,000` scenario that auto-generates recommended sites,
  interventions, total cost, and estimated impact for live presentation.

## Decision Workflow

```text
1. Identify   — open the Risk Map (or Priority Locations table) and select a hotspot.
2. Diagnose   — read its current conditions (Risk, LST, NDVI, coordinates).
3. Compare    — review ranked recommendations and the impact vs cost-effectiveness views.
4. Decide     — choose an intervention and add it to the plan (budget enforced).
5. Allocate   — repeat across sites; watch the planning dashboard stay within budget.
6. Communicate— export the plan as CSV (or run the demo scenario) for stakeholders.
```

## Intervention assumptions

| Intervention | Simulated environmental change | Cost |
| --- | --- | --- |
| Tree Planting | NDVI + 0.15 | $10,000 |
| Shade Structures | LST − 3 °C | $20,000 |
| Green Infrastructure | NDVI + 0.10, LST − 2 °C | $50,000 |
| Cooling Infrastructure | LST − 2 °C | $100,000 |

These are deliberately simple planning simulations, not exact engineering outcomes. The
planner retains responsibility for the final decision.

## Non-goals

- Not a generic heatmap viewer.
- Does not retrain or alter the model.
- Does not modify Session 1–5 outputs or archived workflows.
