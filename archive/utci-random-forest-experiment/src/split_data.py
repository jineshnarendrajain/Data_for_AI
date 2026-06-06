from pathlib import Path
import pandas as pd

RANDOM_SEED = 42

DATA_PATH = "data/processed/manhattan-utci-clean.parquet"

OUTPUT_DIR = Path("data/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main():

    df = pd.read_parquet(DATA_PATH)

    df = df.sort_values("timestamp").reset_index(drop=True)

    n = len(df)

    train_end = int(n * 0.70)
    val_end = int(n * 0.85)

    train_df = df.iloc[:train_end].copy()
    val_df = df.iloc[train_end:val_end].copy()
    test_df = df.iloc[val_end:].copy()

    train_df.to_parquet(
        OUTPUT_DIR / "manhattan-utci-train.parquet",
        index=False,
    )

    val_df.to_parquet(
        OUTPUT_DIR / "manhattan-utci-val.parquet",
        index=False,
    )

    test_df.to_parquet(
        OUTPUT_DIR / "manhattan-utci-test.parquet",
        index=False,
    )

    assert len(train_df) > 0
    assert len(val_df) > 0
    assert len(test_df) > 0

    print("Split complete")
    print("Train:", train_df.shape)
    print("Val:", val_df.shape)
    print("Test:", test_df.shape)


if __name__ == "__main__":
    main()