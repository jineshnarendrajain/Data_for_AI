"""
Manhattan Heat Mitigation Decision Support Tool
================================================

Session 6 deliverable for the Data for AI project.

This is NOT a generic map viewer. It is a decision-support system that turns the
trained Random Forest heat-risk model into actionable urban-planning recommendations
for an NYC urban planner working with a limited budget.

Layered architecture:

    Data Layer  ->  Prediction Layer  ->  Recommendation Engine
                ->  Planning Layer    ->  Export Layer

The pure logic functions (load_data, load_model, predict_risk, evaluate_interventions,
run_demo, plan_to_dataframe) are importable without launching Streamlit so they can be
unit-tested. The Streamlit UI lives entirely inside ``main()``.

Run with:

    streamlit run tool/app.py
"""

from __future__ import annotations

import io
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Paths (resolved relative to this file -- no hardcoded absolute paths)
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "manhattan_heat_risk_training.csv"
MODEL_PATH = BASE_DIR / "models" / "heat_risk_model.joblib"
STYLES_PATH = BASE_DIR / "assets" / "styles.css"

# ---------------------------------------------------------------------------
# Configuration constants
# ---------------------------------------------------------------------------
TOP_N = 500                      # number of highest-risk locations to surface
DEFAULT_BUDGET = 500_000
MIN_BUDGET = 50_000
MAX_BUDGET = 5_000_000
BUDGET_STEP = 50_000
DEMO_MAX_SITES = 12              # cap on sites picked automatically in demo mode

# Manhattan-ish map centre / zoom
MAP_CENTER = (40.776, -73.969)
MAP_ZOOM = 12

# Feature order expected by the trained model (model.feature_names_in_)
MODEL_FEATURES = ["LST", "NDVI"]

# Columns we actually use from the raw Session-5 dataset
USED_COLUMNS = ["LST", "NDVI", "Risk", "latitude", "longitude"]

# Intervention simulation assumptions (planning simulations -- intentionally simple).
# ndvi_delta / lst_delta are applied to the location's environmental indicators;
# the model then re-predicts risk on the modified indicators.
INTERVENTIONS: Dict[str, Dict[str, float]] = {
    "Tree Planting":          {"ndvi_delta": 0.15, "lst_delta": 0.0,  "cost": 10_000},
    "Shade Structures":       {"ndvi_delta": 0.0,  "lst_delta": -3.0, "cost": 20_000},
    "Green Infrastructure":   {"ndvi_delta": 0.10, "lst_delta": -2.0, "cost": 50_000},
    "Cooling Infrastructure": {"ndvi_delta": 0.0,  "lst_delta": -2.0, "cost": 100_000},
}


# ===========================================================================
# DATA LAYER
# ===========================================================================
def load_data(path: Path = DATA_PATH, top_n: int = TOP_N) -> pd.DataFrame:
    """Load the training dataset and return the ``top_n`` highest-risk locations.

    The returned frame is sorted by descending ``Risk`` and carries a 1-based
    ``Rank`` column. Only the columns required by the tool are retained.

    Raises
    ------
    FileNotFoundError
        If the dataset cannot be located.
    ValueError
        If expected columns are missing.
    """
    if not Path(path).exists():
        raise FileNotFoundError(f"Dataset not found at: {path}")

    df = pd.read_csv(path)

    missing = [c for c in USED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Dataset is missing required columns: {missing}")

    df = df[USED_COLUMNS].dropna(subset=USED_COLUMNS).copy()
    df = df.sort_values("Risk", ascending=False).head(top_n).reset_index(drop=True)
    df.insert(0, "Rank", np.arange(1, len(df) + 1))
    return df


# ===========================================================================
# PREDICTION LAYER
# ===========================================================================
def load_model(path: Path = MODEL_PATH):
    """Load and return the trained Random Forest model.

    Raises
    ------
    FileNotFoundError
        If the model artifact cannot be located.
    """
    if not Path(path).exists():
        raise FileNotFoundError(f"Model not found at: {path}")
    import joblib  # imported lazily so the module imports cheaply for tests

    return joblib.load(path)


def clip_ndvi(value: float) -> float:
    """Keep simulated NDVI within its physically valid range [-1, 1]."""
    return float(min(max(value, -1.0), 1.0))


def _features_frame(lst_values, ndvi_values) -> pd.DataFrame:
    """Build a DataFrame with the exact column names/order the model was fit on.

    Passing a named DataFrame (rather than a bare array) avoids scikit-learn's
    "X does not have valid feature names" warning and guarantees correct ordering.
    """
    return pd.DataFrame({"LST": np.atleast_1d(lst_values),
                         "NDVI": np.atleast_1d(ndvi_values)})[MODEL_FEATURES]


def predict_risk(model, lst: float, ndvi: float) -> float:
    """Predict heat risk for a single (LST, NDVI) pair."""
    X = _features_frame([lst], [ndvi])
    return float(model.predict(X)[0])


def predict_risk_batch(model, df: pd.DataFrame) -> np.ndarray:
    """Predict heat risk for a DataFrame containing ``LST`` and ``NDVI`` columns."""
    X = _features_frame(df["LST"].to_numpy(), df["NDVI"].to_numpy())
    return model.predict(X)


# ===========================================================================
# RECOMMENDATION ENGINE
# ===========================================================================
def evaluate_interventions(model, lst: float, ndvi: float) -> pd.DataFrame:
    """Evaluate every intervention for a single location.

    For each intervention the environmental change is simulated, risk is
    re-predicted with the model, and the reduction / cost-effectiveness computed.

    Returns
    -------
    pandas.DataFrame
        One row per intervention with columns: Intervention, Current Risk,
        Predicted Risk, Risk Reduction, Risk Reduction %, Cost,
        Cost Effectiveness (risk reduction per $1,000).
    """
    current_risk = predict_risk(model, lst, ndvi)
    rows: List[Dict[str, float]] = []

    for name, params in INTERVENTIONS.items():
        new_lst = lst + params["lst_delta"]
        new_ndvi = clip_ndvi(ndvi + params["ndvi_delta"])
        new_risk = predict_risk(model, new_lst, new_ndvi)

        reduction = current_risk - new_risk
        denom = abs(current_risk) if current_risk != 0 else 1e-9
        reduction_pct = (reduction / denom) * 100.0
        cost = float(params["cost"])
        cost_effectiveness = reduction / (cost / 1000.0)  # reduction per $1,000

        rows.append({
            "Intervention": name,
            "Current Risk": current_risk,
            "Predicted Risk": new_risk,
            "Risk Reduction": reduction,
            "Risk Reduction %": reduction_pct,
            "Cost": cost,
            "Cost Effectiveness": cost_effectiveness,
        })

    result = pd.DataFrame(rows)
    return result


def rank_interventions(eval_df: pd.DataFrame, by: str = "impact") -> pd.DataFrame:
    """Return a ranked copy of an evaluation frame.

    Parameters
    ----------
    by : {"impact", "cost"}
        "impact" -> rank by highest absolute risk reduction;
        "cost"   -> rank by highest risk reduction per dollar.
    """
    sort_col = "Risk Reduction" if by == "impact" else "Cost Effectiveness"
    ranked = eval_df.sort_values(sort_col, ascending=False).reset_index(drop=True)
    ranked.insert(0, "Rank", np.arange(1, len(ranked) + 1))
    return ranked


# ===========================================================================
# PLANNING LAYER
# ===========================================================================
def plan_total_cost(plan: List[Dict]) -> float:
    """Sum the cost of every intervention currently in the plan."""
    return float(sum(item["Cost"] for item in plan))


def plan_to_dataframe(plan: List[Dict]) -> pd.DataFrame:
    """Convert the plan into the export schema required by the PRD."""
    columns = ["Rank", "Latitude", "Longitude", "Current Risk",
               "Selected Intervention", "Predicted Risk", "Risk Reduction", "Cost"]
    if not plan:
        return pd.DataFrame(columns=columns)
    return pd.DataFrame(plan)[columns]


def plan_to_csv(plan: List[Dict]) -> str:
    """Serialise the plan to CSV text for download."""
    buffer = io.StringIO()
    plan_to_dataframe(plan).to_csv(buffer, index=False)
    return buffer.getvalue()


# ===========================================================================
# DEMO MODE
# ===========================================================================
def run_demo(df: pd.DataFrame, model, budget: float = DEFAULT_BUDGET,
             max_sites: int = DEMO_MAX_SITES) -> List[Dict]:
    """Generate a ready-made intervention plan for the live presentation.

    Greedy strategy: walk the highest-risk sites in order and, for each, pick the
    most cost-effective intervention that still fits the remaining budget. Stops
    when the budget is exhausted or ``max_sites`` is reached.

    Returns the plan as a list of plan-item dicts (same schema used by the UI).
    """
    plan: List[Dict] = []
    remaining = float(budget)

    for _, row in df.head(max_sites).iterrows():
        options = evaluate_interventions(model, row["LST"], row["NDVI"])
        # Only interventions that (a) fit the budget and (b) actually reduce risk.
        affordable = options[(options["Cost"] <= remaining) &
                             (options["Risk Reduction"] > 0)]
        if affordable.empty:
            continue
        best = affordable.sort_values("Cost Effectiveness", ascending=False).iloc[0]
        plan.append(_make_plan_item(row, best))
        remaining -= float(best["Cost"])
        if remaining < min(INTERVENTIONS[k]["cost"] for k in INTERVENTIONS):
            break

    return plan


def _make_plan_item(location_row: pd.Series, intervention_row: pd.Series) -> Dict:
    """Assemble a single plan entry from a location and a chosen intervention."""
    return {
        "Rank": int(location_row["Rank"]),
        "Latitude": float(location_row["latitude"]),
        "Longitude": float(location_row["longitude"]),
        "Current Risk": float(intervention_row["Current Risk"]),
        "Selected Intervention": str(intervention_row["Intervention"]),
        "Predicted Risk": float(intervention_row["Predicted Risk"]),
        "Risk Reduction": float(intervention_row["Risk Reduction"]),
        "Risk Reduction %": float(intervention_row["Risk Reduction %"]),
        "Cost": float(intervention_row["Cost"]),
    }


# ===========================================================================
# UI HELPERS
# ===========================================================================
def risk_color(risk: float, low: float, high: float) -> str:
    """Map a risk value to a traffic-light colour using the visible risk range."""
    if high <= low:
        return "#d73027"
    t = (risk - low) / (high - low)
    if t >= 0.75:
        return "#d73027"   # red    - extreme
    if t >= 0.5:
        return "#fc8d59"   # orange - high
    if t >= 0.25:
        return "#fee08b"   # yellow - moderate
    return "#91cf60"       # green  - lower


def nearest_rank(df: pd.DataFrame, lat: float, lon: float) -> int:
    """Return the Rank of the dataset point closest to (lat, lon)."""
    d2 = (df["latitude"] - lat) ** 2 + (df["longitude"] - lon) ** 2
    return int(df.loc[d2.idxmin(), "Rank"])


# ===========================================================================
# STREAMLIT APPLICATION
# ===========================================================================
# --- presentation-only constants for the environmental analysis layer ------
ESRI_SAT = ("https://server.arcgisonline.com/ArcGIS/rest/services/"
            "World_Imagery/MapServer/tile/{z}/{y}/{x}")
ESRI_REF = ("https://server.arcgisonline.com/ArcGIS/rest/services/Reference/"
            "World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}")
# Green -> yellow -> orange -> red heat-risk gradient for the derived surface.
HEAT_GRADIENT = {0.0: "#1a9850", 0.45: "#fee08b", 0.7: "#fdae61", 1.0: "#d73027"}
INFLUENCE_ZONE_M = 90            # visual planning-area radius around a selected site
BA_CURRENT = "Current Conditions"
BA_POST = "Post-Intervention"


def _intervention_blurb(name: str) -> str:
    """Short human description of what an intervention does (presentation only)."""
    p = INTERVENTIONS[name]
    parts = []
    if p["ndvi_delta"]:
        parts.append(f"NDVI +{p['ndvi_delta']:.2f}")
    if p["lst_delta"]:
        parts.append(f"LST {p['lst_delta']:+.0f}°C")
    return " · ".join(parts)


def _norm(value: float, low: float, high: float) -> float:
    """Normalise a value into [0, 1] over the [low, high] risk range."""
    if high <= low:
        return 0.5
    return float(min(1.0, max(0.0, (value - low) / (high - low))))


def _ring_radius_m(risk: float, low: float, high: float) -> float:
    """Map a risk score to a metres radius for the planning ring (visual only)."""
    return 35.0 + _norm(risk, low, high) * 120.0


def _heat_points(surface_df: pd.DataFrame, low: float, high: float) -> list:
    """Build weighted [lat, lon, weight] points for the derived heat-risk surface.

    This is a *derived visualisation* of the existing risk scores at their sampled
    coordinates (no new analysis, no building-level data) -- defensible during Q&A.
    """
    pts = []
    for lat, lon, risk in surface_df[["latitude", "longitude", "Risk"]].itertuples(index=False):
        pts.append([float(lat), float(lon), _norm(risk, low, high)])
    return pts


def _build_planning_map(df, surface_df, plan, selected_row, layers, preview,
                        ba_mode, low, high):
    """Construct the environmental planning map (presentation layer only).

    Layers: satellite basemap + optional heat-risk surface, hotspots and planned
    interventions, plus a selection influence zone and current/predicted risk rings.
    """
    import folium
    from folium.plugins import HeatMap

    if selected_row is not None:
        center = [float(selected_row["latitude"]), float(selected_row["longitude"])]
        zoom = 15
    else:
        center, zoom = list(MAP_CENTER), MAP_ZOOM

    m = folium.Map(location=center, zoom_start=zoom, tiles=None, control_scale=True)
    folium.TileLayer(ESRI_SAT, attr="Esri, Maxar, Earthstar Geographics",
                     name="Satellite", control=False).add_to(m)
    folium.TileLayer(ESRI_REF, attr="Esri", name="Labels", control=False,
                     overlay=True, opacity=0.9).add_to(m)

    planned_ranks = {int(p["Rank"]) for p in plan}
    sel_rank = int(selected_row["Rank"]) if selected_row is not None else None

    # 1. Derived heat-risk surface (kept light so satellite imagery shows through:
    #    low min_opacity + high `max` lowers peak intensity = context, not a blanket).
    if layers.get("surface", True):
        HeatMap(_heat_points(surface_df, low, high), radius=16, blur=26,
                min_opacity=0.12, max=2.6, gradient=HEAT_GRADIENT,
                name="Heat Risk Surface").add_to(m)

    # 2. Hotspots (excluding ones already planned, which get their own style)
    if layers.get("hotspots", True):
        for row in df.itertuples(index=False):
            rank = int(row.Rank)
            if rank in planned_ranks:
                continue
            base = risk_color(row.Risk, low, high)
            folium.CircleMarker(
                location=[row.latitude, row.longitude],
                radius=6 if rank == sel_rank else 4,
                color="#08304f" if rank == sel_rank else base,
                weight=2 if rank == sel_rank else 1,
                fill=True, fill_color=base, fill_opacity=0.9,
                tooltip=f"Rank #{rank} · Risk {row.Risk:.3f}",
                popup=folium.Popup(
                    f"<b>Rank #{rank}</b><br>Risk: {row.Risk:.3f}<br>"
                    f"LST: {row.LST:.1f} °C<br>NDVI: {row.NDVI:.3f}", max_width=200),
            ).add_to(m)

    # 3. Planned interventions
    if layers.get("planned", True):
        for p in plan:
            folium.CircleMarker(
                location=[p["Latitude"], p["Longitude"]],
                radius=7, color="#ffffff", weight=3,
                fill=True, fill_color="#1f78b4", fill_opacity=1.0,
                tooltip=f"✓ {p['Selected Intervention']} (Rank #{int(p['Rank'])})",
                popup=folium.Popup(
                    f"<b>✓ Planned · Rank #{int(p['Rank'])}</b><br>"
                    f"{p['Selected Intervention']}<br>"
                    f"−{p['Risk Reduction %']:.1f}% risk · ${p['Cost']:,.0f}",
                    max_width=220),
            ).add_to(m)

    # 4. Selection highlight: influence zone + current/predicted risk rings
    if selected_row is not None:
        loc = [float(selected_row["latitude"]), float(selected_row["longitude"])]
        folium.Circle(loc, radius=INFLUENCE_ZONE_M, color="#1f78b4", weight=1,
                      fill=True, fill_color="#1f78b4", fill_opacity=0.06,
                      dash_array="5", tooltip="Planning influence zone (~90 m)").add_to(m)

        if preview is not None:
            cur_bold = ba_mode != BA_POST
            folium.Circle(
                loc, radius=_ring_radius_m(preview["current"], low, high),
                color="#d73027", weight=4 if cur_bold else 1,
                opacity=1.0 if cur_bold else 0.4, fill=False,
                tooltip=f"Current risk {preview['current']:.3f}").add_to(m)
            folium.Circle(
                loc, radius=_ring_radius_m(preview["predicted"], low, high),
                color="#2e8b57", weight=4 if not cur_bold else 1,
                opacity=1.0 if not cur_bold else 0.4, fill=False,
                tooltip=f"Predicted risk {preview['predicted']:.3f}").add_to(m)

        marker_fill = "#2e8b57" if (preview is not None and ba_mode == BA_POST) else "#08304f"
        folium.CircleMarker(loc, radius=9, color="#ffffff", weight=3, fill=True,
                            fill_color=marker_fill, fill_opacity=1.0,
                            tooltip=f"Selected · Rank #{sel_rank}").add_to(m)

    return m


def main() -> None:  # pragma: no cover - exercised via the live app, not unit tests
    import streamlit as st
    import streamlit.components.v1 as components
    from streamlit_folium import st_folium

    st.set_page_config(
        page_title="Manhattan Heat Mitigation Planner",
        page_icon="🌡️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    # ---- styling (graceful fallback if the stylesheet is missing) ----------
    try:
        st.markdown(f"<style>{STYLES_PATH.read_text(encoding='utf-8')}</style>",
                    unsafe_allow_html=True)
    except OSError:
        pass

    # ---- cached resources --------------------------------------------------
    @st.cache_data(show_spinner=False)
    def _cached_data() -> pd.DataFrame:
        return load_data()

    @st.cache_data(show_spinner=False)
    def _cached_surface() -> pd.DataFrame:
        # Full sampled dataset -> derived heat-risk surface (visualisation only).
        return load_data(top_n=10_000)

    @st.cache_resource(show_spinner=False)
    def _cached_model():
        return load_model()

    try:
        df = _cached_data()
        surface_df = _cached_surface()
        model = _cached_model()
    except Exception as exc:  # noqa: BLE001 - surface any load error to the planner
        st.error(f"Failed to load required resources: {exc}")
        st.stop()

    # Use the full surface range so colours/rings stay consistent everywhere.
    low = float(surface_df["Risk"].min())
    high = float(surface_df["Risk"].max())

    # ---- session state -----------------------------------------------------
    # selected_rank starts as None so recommendations only appear AFTER a click.
    st.session_state.setdefault("plan", [])
    st.session_state.setdefault("selected_rank", None)
    st.session_state.setdefault("budget", DEFAULT_BUDGET)
    st.session_state.setdefault("ba_mode", BA_CURRENT)

    def set_rank(rank) -> None:
        st.session_state.selected_rank = None if rank is None else int(rank)

    planned_ranks = {int(p["Rank"]) for p in st.session_state.plan}
    used = plan_total_cost(st.session_state.plan)
    remaining = st.session_state.budget - used

    # ===================================================================
    # REPORT MODAL  (RUN ANALYSIS -> clean report -> export)
    # ===================================================================
    @st.dialog("📑 Intervention Analysis Report", width="large")
    def show_report() -> None:
        plan = st.session_state.plan
        if not plan:
            st.warning("Add at least one intervention to the plan before running analysis.")
            return

        r_used = plan_total_cost(plan)
        r_remaining = st.session_state.budget - r_used
        avg_pct = float(np.mean([p["Risk Reduction %"] for p in plan]))
        total_reduction = float(np.sum([p["Risk Reduction"] for p in plan]))
        top_intervention = (pd.Series([p["Selected Intervention"] for p in plan])
                            .value_counts().index[0])

        st.markdown("#### Planning Summary")
        a1, a2, a3 = st.columns(3)
        a1.metric("Sites Selected", f"{len(plan)}")
        a2.metric("Budget Used", f"${r_used:,.0f}")
        a3.metric("Budget Remaining", f"${r_remaining:,.0f}")
        b1, b2, b3 = st.columns(3)
        b1.metric("Average Risk Reduction", f"{avg_pct:.1f}%")
        b2.metric("Total Risk Reduction", f"{total_reduction:.3f}")
        b3.metric("Best Intervention", top_intervention)

        if r_remaining < 0:
            st.error("⚠️ This plan exceeds the available budget.")

        st.markdown("#### Spatial Summary")
        st.caption("Selected intervention sites over the heat-risk surface "
                   "(satellite basemap).")
        spatial = _build_planning_map(
            df, surface_df, plan, None,
            {"surface": True, "hotspots": False, "planned": True},
            None, BA_CURRENT, low, high)
        components.html(spatial.get_root().render(), height=420)

        st.markdown("#### Recommended Intervention Plan")
        st.dataframe(
            plan_to_dataframe(plan), use_container_width=True, hide_index=True,
            column_config={
                "Latitude": st.column_config.NumberColumn(format="%.5f"),
                "Longitude": st.column_config.NumberColumn(format="%.5f"),
                "Current Risk": st.column_config.NumberColumn(format="%.3f"),
                "Predicted Risk": st.column_config.NumberColumn(format="%.3f"),
                "Risk Reduction": st.column_config.NumberColumn(format="%.3f"),
                "Cost": st.column_config.NumberColumn(format="$%d"),
            },
        )

        st.download_button(
            "⬇️  Export Plan (CSV)",
            data=plan_to_csv(plan),
            file_name="manhattan_intervention_plan.csv",
            mime="text/csv",
            type="primary",
            use_container_width=True,
        )
        st.caption("Recommendations are model-driven planning simulations. "
                   "The planner makes the final funding decision.")

    # ===================================================================
    # MAP-FIRST: the map is the application; all controls are overlays.
    # Layer toggles / preview / before-after are read from session_state so
    # overlay widgets rendered *after* the map still drive it on rerun.
    # ===================================================================
    layers = {
        "surface": st.session_state.setdefault("layer_surface", True),
        "hotspots": st.session_state.setdefault("layer_hotspots", True),
        "planned": st.session_state.setdefault("layer_planned", True),
    }

    # ---- compute selection + intervention preview (reuses existing engine) --
    selected_row = None
    evaluation = ranked = None
    preview = None
    ba_mode = st.session_state.get("ba_mode", BA_CURRENT)
    if st.session_state.selected_rank is not None:
        selected_row = df[df["Rank"] == st.session_state.selected_rank].iloc[0]
        evaluation = evaluate_interventions(model, selected_row["LST"], selected_row["NDVI"])
        ranked = rank_interventions(evaluation, by="impact")
        best_name = ranked.iloc[0]["Intervention"]
        if st.session_state.get("preview_iv") not in INTERVENTIONS:
            st.session_state["preview_iv"] = best_name
        prow = evaluation[evaluation["Intervention"] == st.session_state["preview_iv"]].iloc[0]
        preview = {
            "current": float(prow["Current Risk"]),
            "predicted": float(prow["Predicted Risk"]),
            "intervention": st.session_state["preview_iv"],
            "reduction_pct": float(prow["Risk Reduction %"]),
            "cost": float(prow["Cost"]),
        }

    # ---------------------------------------- FULL-VIEWPORT ENVIRONMENTAL MAP
    fmap = _build_planning_map(df, surface_df, st.session_state.plan, selected_row,
                               layers, preview, ba_mode, low, high)
    map_state = st_folium(fmap, height=760, use_container_width=True,
                          returned_objects=["last_object_clicked"], key="planmap")
    clicked = (map_state or {}).get("last_object_clicked")
    if clicked and clicked.get("lat") is not None:
        new_rank = nearest_rank(df, clicked["lat"], clicked["lng"])
        if new_rank != st.session_state.selected_rank:
            set_rank(new_rank)
            st.rerun()

    # ===================================================================
    # FLOATING OVERLAYS  (position:fixed via CSS on keyed containers)
    # ===================================================================
    over = remaining < 0
    pct = (used / st.session_state.budget * 100) if st.session_state.budget else 0

    # ---- top-left: ONE unified control panel (title + Layers + Tools + Demo)
    with st.container(key="ov_panel"):
        st.markdown("<div class='brandchip'>🌡️ <b>Heat Mitigation Planner</b>"
                    "<span>Manhattan · NYC</span></div>", unsafe_allow_html=True)
        pcol1, pcol2, pcol3 = st.columns(3)
        with pcol1:
            with st.popover("🗂️ Layers", use_container_width=True):
                st.markdown("**Map layers**")
                st.checkbox("Heat Risk Surface", value=True, key="layer_surface")
                st.checkbox("Hotspots", value=True, key="layer_hotspots")
                st.checkbox("Planned Interventions", value=True, key="layer_planned")
        with pcol2:
            with st.popover("⚙️ Tools", use_container_width=True):
                st.markdown("**Budget**")
                st.session_state.budget = st.slider(
                    "Total available budget (USD)",
                    min_value=MIN_BUDGET, max_value=MAX_BUDGET,
                    value=int(st.session_state.budget), step=BUDGET_STEP, format="$%d",
                )
                st.markdown("**Jump to hotspot**")
                jump = st.selectbox(
                    "Select a hotspot by rank", df["Rank"].tolist(),
                    index=(df["Rank"].tolist().index(st.session_state.selected_rank)
                           if st.session_state.selected_rank in df["Rank"].tolist() else 0),
                    format_func=lambda r: f"Rank #{r}", label_visibility="collapsed",
                )
                if st.button("Go to hotspot", use_container_width=True):
                    set_rank(jump)
                    st.rerun()
                if st.button("🗑️  Reset plan", use_container_width=True):
                    st.session_state.plan = []
                    set_rank(None)
                    st.rerun()
        with pcol3:
            if st.button("▶ Demo", use_container_width=True,
                         help="Auto-build a $500k example plan for the presentation"):
                st.session_state.plan = run_demo(df, model, budget=DEFAULT_BUDGET)
                st.session_state.budget = DEFAULT_BUDGET
                if st.session_state.plan:
                    set_rank(st.session_state.plan[0]["Rank"])
                st.rerun()

    # ---- top-right: RUN ANALYSIS + dedicated budget card (large typography) -
    with st.container(key="ov_action"):
        if st.button("📊  RUN ANALYSIS", type="primary", use_container_width=True):
            show_report()
        st.markdown(
            "<div class='budgetcard'>"
            f"<div class='bc-stat {'bc-stat--bad' if over else ''}'>"
            f"<span>Budget Remaining</span><b>${remaining:,.0f}</b></div>"
            f"<div class='bc-stat'>"
            f"<span>Sites Planned</span><b>{len(st.session_state.plan)}</b></div>"
            "</div>", unsafe_allow_html=True)

    # ---- bottom-left: collapsible legend -----------------------------------
    with st.container(key="ov_legend"):
        with st.popover("ℹ️ Legend", use_container_width=False):
            st.markdown(
                "<div class='legend legend--stack'>"
                "<b>Heat Risk Surface</b><br>"
                "<span class='dot' style='background:#1a9850'></span> Low &nbsp;"
                "<span class='dot' style='background:#fee08b'></span> Moderate &nbsp;"
                "<span class='dot' style='background:#fdae61'></span> High &nbsp;"
                "<span class='dot' style='background:#d73027'></span> Extreme<br>"
                "<span class='dot dot--planned' style='background:#1f78b4'></span> "
                "Planned site &nbsp; "
                "<span class='ring ring--cur'></span> Current risk &nbsp; "
                "<span class='ring ring--pred'></span> Predicted risk"
                "</div>", unsafe_allow_html=True)

    # ---- right slide-out drawer: appears only when a hotspot is selected ----
    if selected_row is None:
        with st.container(key="ov_hint"):
            st.markdown("<div class='maphint'>📍 Click a hotspot on the map to plan an "
                        "intervention</div>", unsafe_allow_html=True)
    else:
        rank = int(selected_row["Rank"])
        already = rank in planned_ranks
        with st.container(key="ov_drawer"):
            dh1, dh2 = st.columns([4, 1])
            dh1.markdown(f"<div class='drawer-head'>📍 Selected Hotspot"
                         f"<span class='panel-rank'>Rank #{rank}</span></div>",
                         unsafe_allow_html=True)
            with dh2:
                if st.button("✕", key="drawer_close", help="Back to overview",
                             use_container_width=True):
                    set_rank(None)
                    st.rerun()

            st.markdown(
                "<div class='condpills'>"
                f"<span class='cond'>Risk<b>{selected_row['Risk']:.3f}</b></span>"
                f"<span class='cond'>LST<b>{selected_row['LST']:.1f}°C</b></span>"
                f"<span class='cond'>NDVI<b>{selected_row['NDVI']:.3f}</b></span>"
                f"<span class='cond cond--wide'>° {selected_row['latitude']:.4f}, "
                f"{selected_row['longitude']:.4f}</span>"
                "</div>", unsafe_allow_html=True)

            st.radio("Map view", [BA_CURRENT, BA_POST], key="ba_mode", horizontal=True,
                     help="Toggle the selected site's risk ring on the map.")
            st.selectbox("Preview intervention", list(INTERVENTIONS.keys()),
                         key="preview_iv")
            st.markdown(
                "<div class='previewrow'>"
                f"<div class='pstat pstat--cur'><span>Current</span>"
                f"<b>{preview['current']:.3f}</b></div>"
                f"<div class='pstat pstat--pred'><span>Predicted</span>"
                f"<b>{preview['predicted']:.3f}</b></div>"
                f"<div class='pstat pstat--red'><span>Reduction</span>"
                f"<b>−{preview['reduction_pct']:.1f}%</b></div>"
                "</div>", unsafe_allow_html=True)

            if already:
                pi = next(p for p in st.session_state.plan if int(p["Rank"]) == rank)
                st.markdown(
                    "<div class='planned-note'>✓ Already in plan: "
                    f"<b>{pi['Selected Intervention']}</b> "
                    f"(−{pi['Risk Reduction %']:.1f}% · ${pi['Cost']:,.0f})</div>",
                    unsafe_allow_html=True)

            st.markdown("<div class='rec-title'>Recommended interventions</div>",
                        unsafe_allow_html=True)
            for i, (_, opt) in enumerate(ranked.iterrows()):
                name = opt["Intervention"]
                best = i == 0
                affordable = opt["Cost"] <= remaining
                st.markdown(
                    f"<div class='reccard {'best' if best else ''}'>"
                    + ("<span class='rec-badge'>★ RECOMMENDED</span>" if best else "")
                    + f"<div class='rec-name'>{name}</div>"
                    f"<div class='rec-sub'>{_intervention_blurb(name)}</div>"
                    f"<div class='rec-figure'>−{opt['Risk Reduction %']:.1f}%"
                    "<span class='rec-figure__lbl'>risk</span></div>"
                    "<div class='rec-meta'>"
                    f"<span>Predicted <b>{opt['Predicted Risk']:.3f}</b></span>"
                    f"<span>Cost <b>${opt['Cost']:,.0f}</b></span>"
                    f"<span>Per $1k <b>{opt['Cost Effectiveness']:.3f}</b></span>"
                    "</div></div>", unsafe_allow_html=True)
                if already:
                    continue
                if affordable:
                    if st.button(f"➕  Add {name}", key=f"add_{rank}_{name}",
                                 use_container_width=True,
                                 type="primary" if best else "secondary"):
                        st.session_state.plan.append(_make_plan_item(selected_row, opt))
                        st.rerun()
                else:
                    st.button(f"Exceeds budget (${opt['Cost']:,.0f})",
                              key=f"add_{rank}_{name}", use_container_width=True,
                              disabled=True)


if __name__ == "__main__":
    main()
