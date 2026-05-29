from pathlib import Path

import joblib
import pandas as pd

from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


FEATURES = [
    "air_temp_c",
    "humidity_pct",
    "wind_speed_ms",
    "solar_radiation",
]

TARGET = "utci"

MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)


def main():

    train_df = pd.read_parquet(
        "data/processed/manhattan-utci-train.parquet"
    )

    val_df = pd.read_parquet(
        "data/processed/manhattan-utci-val.parquet"
    )

    X_train = train_df[FEATURES]
    y_train = train_df[TARGET]

    X_val = val_df[FEATURES]
    y_val = val_df[TARGET]

    baseline = DummyRegressor(strategy="mean")
    baseline.fit(X_train, y_train)

    baseline_pred = baseline.predict(X_val)

    print("\nBASELINE")
    print(
        "MAE:",
        mean_absolute_error(y_val, baseline_pred),
    )
    print(
        "R2:",
        r2_score(y_val, baseline_pred),
    )

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
    )

    model.fit(X_train, y_train)

    pred = model.predict(X_val)

    print("\nRANDOM FOREST")
    print(
        "MAE:",
        mean_absolute_error(y_val, pred),
    )
    print(
        "R2:",
        r2_score(y_val, pred),
    )

    joblib.dump(
        model,
        MODEL_DIR / "baseline.joblib",
    )

    print("\nModel saved")


if __name__ == "__main__":
    main()