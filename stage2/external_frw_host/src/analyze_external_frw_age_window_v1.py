import math
from pathlib import Path

import numpy as np
import pandas as pd


def get_repo_root() -> Path:
    here = Path(__file__).resolve()
    # .../stage2/external_frw_host/src/analyze_external_frw_age_window_v1.py
    # parents[0]=src, [1]=external_frw_host, [2]=stage2, [3]=repo root
    return here.parents[3]


def main() -> None:
    repo_root = get_repo_root()

    bridge_path = (
        repo_root
        / "stage2"
        / "external_frw_host"
        / "outputs"
        / "tables"
        / "stage2_external_frw_background_bridge_v1.csv"
    )

    frw_anchor_path = (
        repo_root
        / "stage2"
        / "frw_data_probe_analysis"
        / "outputs"
        / "tables"
        / "stage2_frw_empirical_anchor_mask_v1.csv"
    )

    out_path = (
        repo_root
        / "stage2"
        / "external_frw_host"
        / "outputs"
        / "tables"
        / "stage2_external_frw_rung4_age_window_summary_v1.csv"
    )

    if not bridge_path.is_file():
        raise FileNotFoundError(f"Bridge table not found: {bridge_path}")

    print("[external_frw_host_rung4_age_window]")
    print(f"  Repo root: {repo_root}")
    print(f"  Bridge table: {bridge_path}")

    df = pd.read_csv(bridge_path)

    required_cols = [
        "theta_index",
        "theta",
        "omega_lambda",
        "age_Gyr_toy",
        "age_Gyr_host",
        "frw_viable",
    ]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise RuntimeError(f"Missing required columns in bridge table: {missing}")

    # Define a very simple "Universe age window" around ~13.8 Gyr.
    AGE_CENTER_GYR = 13.8
    AGE_HALF_WIDTH_GYR = 0.5

    age_min = AGE_CENTER_GYR - AGE_HALF_WIDTH_GYR
    age_max = AGE_CENTER_GYR + AGE_HALF_WIDTH_GYR

    print(
        "  Age window (Gyr) around the observed Universe age: "
        f"[{age_min:.3f}, {age_max:.3f}]"
    )

    df["host_in_age_window"] = (
        (df["age_Gyr_host"] >= age_min) & (df["age_Gyr_host"] <= age_max)
    )
    df["toy_in_age_window"] = (
        (df["age_Gyr_toy"] >= age_min) & (df["age_Gyr_toy"] <= age_max)
    )

    # Optionally join the FRW empirical anchor mask to see overlap.
    if not frw_anchor_path.is_file():
        print(f"  FRW anchor mask not found (optional): {frw_anchor_path}")
        df["in_empirical_anchor_box"] = False
    else:
        print(f"  FRW anchor mask: {frw_anchor_path}")
        df_anchor = pd.read_csv(frw_anchor_path)
        if "theta" not in df_anchor.columns or "in_empirical_anchor_box" not in df_anchor.columns:
            raise RuntimeError(
                "FRW anchor table must contain 'theta' and 'in_empirical_anchor_box' columns."
            )
        df = df.merge(
            df_anchor[["theta", "in_empirical_anchor_box"]],
            on="theta",
            how="left",
        )
        df["in_empirical_anchor_box"] = df["in_empirical_anchor_box"].fillna(False)

    n_total = len(df)
    print(f"  Rows: {n_total}")

    def count_frac(mask: pd.Series) -> tuple[int, float]:
        n = int(mask.sum())
        frac = float(n) / float(n_total) if n_total > 0 else math.nan
        return n, frac

    def summarize_set(name: str, mask: pd.Series) -> dict:
        n, frac = count_frac(mask)
        if n == 0:
            row = {
                "set": name,
                "n_theta": n,
                "frac_of_grid": frac,
                "age_Gyr_host_mean": math.nan,
                "age_Gyr_host_std": math.nan,
                "age_Gyr_host_min": math.nan,
                "age_Gyr_host_max": math.nan,
                "age_Gyr_toy_mean": math.nan,
                "age_Gyr_toy_std": math.nan,
                "age_Gyr_toy_min": math.nan,
                "age_Gyr_toy_max": math.nan,
            }
        else:
            sub = df.loc[mask]
            def _safe_stats(col: str):
                series = sub[col].to_numpy(dtype=float)
                return float(series.mean()), float(series.std()), float(series.min()), float(series.max())

            host_mean, host_std, host_min, host_max = _safe_stats("age_Gyr_host")
            toy_mean, toy_std, toy_min, toy_max = _safe_stats("age_Gyr_toy")

            row = {
                "set": name,
                "n_theta": n,
                "frac_of_grid": frac,
                "age_Gyr_host_mean": host_mean,
                "age_Gyr_host_std": host_std,
                "age_Gyr_host_min": host_min,
                "age_Gyr_host_max": host_max,
                "age_Gyr_toy_mean": toy_mean,
                "age_Gyr_toy_std": toy_std,
                "age_Gyr_toy_min": toy_min,
                "age_Gyr_toy_max": toy_max,
            }

        print(
            f"  {name:30s} n={row['n_theta']:4d}, "
            f"frac={row['frac_of_grid']:.6f}, "
            f"<age_host>={row['age_Gyr_host_mean'] if not math.isnan(row['age_Gyr_host_mean']) else float('nan'):.3f}, "
            f"<age_toy>={row['age_Gyr_toy_mean'] if not math.isnan(row['age_Gyr_toy_mean']) else float('nan'):.3f}"
        )
        return row

    mask_all = np.ones(n_total, dtype=bool)
    mask_frw = df["frw_viable"].astype(bool)
    mask_host_window = df["host_in_age_window"]
    mask_toy_window = df["toy_in_age_window"]
    mask_anchor = df["in_empirical_anchor_box"].astype(bool)

    sets = {
        "ALL_GRID": mask_all,
        "FRW_VIABLE": mask_frw,
        "HOST_AGE_WINDOW": mask_host_window,
        "FRW_VIABLE_AND_HOST_WINDOW": mask_frw & mask_host_window,
        "TOY_AGE_WINDOW": mask_toy_window,
        "FRW_VIABLE_AND_TOY_WINDOW": mask_frw & mask_toy_window,
        "HOST_WINDOW_AND_ANCHOR": mask_host_window & mask_anchor,
        "FRW_VIABLE_AND_HOST_WINDOW_AND_ANCHOR": mask_frw & mask_host_window & mask_anchor,
    }

    rows = []
    for name, m in sets.items():
        rows.append(summarize_set(name, m))

    out_df = pd.DataFrame(rows, columns=[
        "set",
        "n_theta",
        "frac_of_grid",
        "age_Gyr_host_mean",
        "age_Gyr_host_std",
        "age_Gyr_host_min",
        "age_Gyr_host_max",
        "age_Gyr_toy_mean",
        "age_Gyr_toy_std",
        "age_Gyr_toy_min",
        "age_Gyr_toy_max",
    ])

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_df.to_csv(out_path, index=False)
    print(f"  Output written: {out_path}")


if __name__ == "__main__":
    main()
