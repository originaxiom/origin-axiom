#!/usr/bin/env python3
"""
Stage 2 – mech–anchor diagnostics
Rung M1: theta-gradients of mechanism amplitudes.

Reads:
  - stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv
  - stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv

Computes:
  - finite-difference gradients d(mech)/d(theta) for selected mech columns,
  - summary stats over:
      ALL_GRID
      FRW_VIABLE
      TOY_CORRIDOR
      CORRIDOR_AND_VIABLE
      CORRIDOR_AND_VIABLE_AND_ANCHOR
      CORRIDOR_AND_VIABLE_NOT_ANCHOR

Outputs:
  - stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung7_theta_gradients_v1.csv
"""

from pathlib import Path

import numpy as np
import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[3]

JOINT_GRID = REPO_ROOT / "stage2" / "joint_mech_frw_analysis" / "outputs" / "tables" / "stage2_joint_theta_grid_v1.csv"
ANCHOR_MASK = REPO_ROOT / "stage2" / "frw_data_probe_analysis" / "outputs" / "tables" / "stage2_frw_empirical_anchor_mask_v1.csv"

OUT_DIR = REPO_ROOT / "stage2" / "mech_measure_analysis" / "outputs" / "tables"
OUT_PATH = OUT_DIR / "stage2_mech_rung7_theta_gradients_v1.csv"

MECH_COLUMNS = [
    "mech_baseline_A0",
    "mech_baseline_A_floor",
    "mech_binding_A0",
    "mech_binding_A",
]


def load_joint_grid() -> pd.DataFrame:
    if not JOINT_GRID.exists():
        raise FileNotFoundError(f"Joint grid not found at {JOINT_GRID}")
    df = pd.read_csv(JOINT_GRID)
    required = [
        "theta_index",
        "theta",
        "frw_viable",
        "in_toy_corridor",
    ]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise RuntimeError(f"Missing columns in joint grid: {missing}")
    for c in MECH_COLUMNS:
        if c not in df.columns:
            raise RuntimeError(f"Missing mech column in joint grid: {c}")
    # Ensure sorted by theta_index
    df = df.sort_values("theta_index").reset_index(drop=True)
    return df


def load_anchor_mask() -> pd.DataFrame:
    if not ANCHOR_MASK.exists():
        raise FileNotFoundError(f"Anchor mask not found at {ANCHOR_MASK}")
    df = pd.read_csv(ANCHOR_MASK)
    # We built it earlier with theta and in_empirical_anchor_box
    required = ["theta", "in_empirical_anchor_box"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise RuntimeError(f"Missing columns in anchor mask: {missing}")
    return df


def compute_gradients(df: pd.DataFrame) -> pd.DataFrame:
    """Add finite-difference gradients d(mech)/d(theta) as new columns."""
    theta = df["theta"].values
    # Guard against degenerate theta spacing
    if not np.all(np.diff(theta) > 0):
        # If theta not strictly increasing, fall back to theta_index as parameter
        x = df["theta_index"].values.astype(float)
    else:
        x = theta

    df_grad = df.copy()
    for col in MECH_COLUMNS:
        y = df[col].values
        # Use central differences via np.gradient
        dy_dx = np.gradient(y, x)
        grad_col = f"{col}__dtheta"
        df_grad[grad_col] = dy_dx
    return df_grad


def build_sets(df: pd.DataFrame) -> dict:
    """Return boolean masks for the sets we care about."""
    frw_viable = df["frw_viable"].astype(bool)
    in_corridor = df["in_toy_corridor"].astype(bool)
    in_anchor = df["in_empirical_anchor_box"].astype(bool)

    masks = {
        "ALL_GRID": np.ones(len(df), dtype=bool),
        "FRW_VIABLE": frw_viable,
        "TOY_CORRIDOR": in_corridor,
        "CORRIDOR_AND_VIABLE": in_corridor & frw_viable,
        "CORRIDOR_AND_VIABLE_AND_ANCHOR": in_corridor & frw_viable & in_anchor,
        "CORRIDOR_AND_VIABLE_NOT_ANCHOR": in_corridor & frw_viable & ~in_anchor,
    }
    return masks


def summarize_gradients(df: pd.DataFrame) -> pd.DataFrame:
    masks = build_sets(df)
    rows = []

    for set_name, mask in masks.items():
        n_theta = int(mask.sum())
        frac = n_theta / len(df)
        if n_theta == 0:
            # Still record empty sets explicitly
            for col in MECH_COLUMNS:
                rows.append(
                    {
                        "set": set_name,
                        "mech_column": col,
                        "n_theta": n_theta,
                        "frac_of_grid": frac,
                        "grad_mean": np.nan,
                        "grad_std": np.nan,
                        "grad_min": np.nan,
                        "grad_max": np.nan,
                        "abs_grad_mean": np.nan,
                        "abs_grad_p95": np.nan,
                        "abs_grad_max": np.nan,
                    }
                )
            continue

        for col in MECH_COLUMNS:
            grad_col = f"{col}__dtheta"
            g = df.loc[mask, grad_col].values
            abs_g = np.abs(g)
            rows.append(
                {
                    "set": set_name,
                    "mech_column": col,
                    "n_theta": n_theta,
                    "frac_of_grid": frac,
                    "grad_mean": float(np.mean(g)),
                    "grad_std": float(np.std(g)),
                    "grad_min": float(np.min(g)),
                    "grad_max": float(np.max(g)),
                    "abs_grad_mean": float(np.mean(abs_g)),
                    "abs_grad_p95": float(np.quantile(abs_g, 0.95)),
                    "abs_grad_max": float(np.max(abs_g)),
                }
            )

    return pd.DataFrame(rows)


def main() -> None:
    print("[stage2_mech_rung7] Repo root:", REPO_ROOT)
    print("[stage2_mech_rung7] Joint grid:", JOINT_GRID)
    print("[stage2_mech_rung7] Anchor mask:", ANCHOR_MASK)

    df_joint = load_joint_grid()
    df_anchor = load_anchor_mask()

    # Join anchor mask onto joint grid using theta
    df = df_joint.merge(
        df_anchor[["theta", "in_empirical_anchor_box"]],
        on="theta",
        how="left",
        validate="one_to_one",
    )
    df["in_empirical_anchor_box"] = df["in_empirical_anchor_box"].fillna(False).astype(bool)

    df_grad = compute_gradients(df)
    summary = summarize_gradients(df_grad)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    summary.to_csv(OUT_PATH, index=False)

    print("[stage2_mech_rung7] Output written:", OUT_PATH)
    print("[stage2_mech_rung7] Rows:", len(summary))


if __name__ == "__main__":
    main()
