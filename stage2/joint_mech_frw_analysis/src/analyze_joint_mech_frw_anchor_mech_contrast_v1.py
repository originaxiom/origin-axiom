#!/usr/bin/env python3
"""
Stage 2 – joint mech–FRW anchor belt
Rung A8: mechanism contrast inside vs. outside the empirical anchor kernel.

This script:
  - loads the joint theta grid (FRW + mech) and the empirical anchor mask,
  - defines the sets:
      ALL_GRID
      FRW_VIABLE
      CORRIDOR_AND_VIABLE
      CORRIDOR_AND_VIABLE_AND_ANCHOR   (18-point kernel)
      CORRIDOR_AND_VIABLE_NOT_ANCHOR   (corridor+viable but outside kernel)
  - computes summary stats for the mechanism columns in each set,
  - writes a single CSV summary table under stage2/joint_mech_frw_analysis/outputs/tables/.
"""

from pathlib import Path
import numpy as np
import pandas as pd


def get_repo_root() -> Path:
    # Same pattern as other Stage 2 scripts: repo root = parents[3]
    return Path(__file__).resolve().parents[3]


def load_joint_grid(repo_root: Path) -> pd.DataFrame:
    joint_path = repo_root / "stage2" / "joint_mech_frw_analysis" / "outputs" / "tables" / "stage2_joint_theta_grid_v1.csv"
    if not joint_path.is_file():
        raise FileNotFoundError(f"Joint theta grid not found at {joint_path}")
    df = pd.read_csv(joint_path)
    return df


def load_anchor_mask(repo_root: Path) -> pd.DataFrame:
    anchor_path = repo_root / "stage2" / "frw_data_probe_analysis" / "outputs" / "tables" / "stage2_frw_empirical_anchor_mask_v1.csv"
    if not anchor_path.is_file():
        raise FileNotFoundError(f"Empirical anchor mask not found at {anchor_path}")
    df_anchor = pd.read_csv(anchor_path)
    # We join on theta (consistent with earlier A6/A7 scripts).
    if "theta" not in df_anchor.columns:
        raise RuntimeError("Empirical anchor mask must contain a 'theta' column.")
    if "in_empirical_anchor_box" not in df_anchor.columns:
        raise RuntimeError("Empirical anchor mask must contain 'in_empirical_anchor_box' column.")
    return df_anchor[["theta", "in_empirical_anchor_box"]]


def compute_mech_contrast(df: pd.DataFrame, out_path: Path) -> None:
    # Expected columns (already present in the joint grid):
    required_cols = [
        "theta",
        "in_toy_corridor",
        "frw_viable",
        "mech_baseline_A0",
        "mech_baseline_A_floor",
        "mech_baseline_bound",
        "mech_binding_A0",
        "mech_binding_A",
        "mech_binding_bound",
        "in_empirical_anchor_box",
    ]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise RuntimeError(f"Missing columns in joint+anchor DataFrame: {missing}")

    # Boolean masks
    corr = df["in_toy_corridor"].astype(bool)
    frw = df["frw_viable"].astype(bool)
    anchor = df["in_empirical_anchor_box"].astype(bool)

    mask_all = np.ones(len(df), dtype=bool)
    mask_frw = frw
    mask_corr_frw = corr & frw
    mask_corr_frw_anchor = mask_corr_frw & anchor
    mask_corr_frw_not_anchor = mask_corr_frw & (~anchor)

    # Define sets we will report
    sets = {
        "ALL_GRID": mask_all,
        "FRW_VIABLE": mask_frw,
        "CORRIDOR_AND_VIABLE": mask_corr_frw,
        "CORRIDOR_AND_VIABLE_AND_ANCHOR": mask_corr_frw_anchor,
        "CORRIDOR_AND_VIABLE_NOT_ANCHOR": mask_corr_frw_not_anchor,
    }

    mech_cols = [
        "mech_baseline_A0",
        "mech_baseline_A_floor",
        "mech_baseline_bound",
        "mech_binding_A0",
        "mech_binding_A",
        "mech_binding_bound",
    ]

    rows = []
    total_rows = len(df)

    print("[stage2_anchor_mech_contrast_rungA8]")
    print(f"  Total grid rows: {total_rows}")

    for set_name, mask in sets.items():
        n = int(mask.sum())
        frac = n / total_rows if total_rows > 0 else np.nan
        print(f"  {set_name}: n={n}, frac={frac:.6f}")

        for col in mech_cols:
            sub = df.loc[mask, col].astype(float)
            if n == 0:
                mean = std = vmin = vmax = np.nan
            else:
                mean = float(sub.mean())
                std = float(sub.std(ddof=0))
                vmin = float(sub.min())
                vmax = float(sub.max())
            rows.append(
                {
                    "set": set_name,
                    "mech_column": col,
                    "n_theta": n,
                    "frac_of_grid": frac,
                    "mean": mean,
                    "std": std,
                    "min": vmin,
                    "max": vmax,
                }
            )

    out_df = pd.DataFrame(rows)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_df.to_csv(out_path, index=False)
    print(f"  Output written: {out_path}")


def main() -> None:
    repo_root = get_repo_root()
    print(f"[stage2_anchor_mech_contrast_rungA8] Repo root: {repo_root}")

    df_joint = load_joint_grid(repo_root)
    df_anchor = load_anchor_mask(repo_root)

    # Join on theta (inner join; every joint-theta should have an anchor flag)
    df = df_joint.merge(df_anchor, on="theta", how="left")
    if df["in_empirical_anchor_box"].isna().any():
        n_missing = int(df["in_empirical_anchor_box"].isna().sum())
        raise RuntimeError(f"'in_empirical_anchor_box' missing for {n_missing} rows after merge on theta.")

    out_path = repo_root / "stage2" / "joint_mech_frw_analysis" / "outputs" / "tables" / "stage2_joint_mech_frw_anchor_mech_contrast_v1.csv"
    compute_mech_contrast(df, out_path)


if __name__ == "__main__":
    main()
