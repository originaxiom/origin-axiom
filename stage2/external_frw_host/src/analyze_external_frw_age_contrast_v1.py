#!/usr/bin/env python3
"""
Stage 2 – External FRW host age contrast (rung X2)

Reads:
  - stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv
      (theta, omega_lambda, age_Gyr, age_Gyr_host, age_Gyr_diff, age_Gyr_rel_diff, frw_viable)
  - stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv
      (theta, in_toy_corridor, ... FRW-related columns)
  - stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv
      (theta, in_empirical_anchor_box)

Produces:
  - stage2/external_frw_host/outputs/tables/stage2_external_frw_rung2_age_contrast_v1.csv

This summarises the age difference between the external FRW host and the repo
FRW ages across key sets:
  - ALL_GRID
  - FRW_VIABLE
  - CORRIDOR_AND_VIABLE
  - CORRIDOR_AND_VIABLE_AND_ANCHOR
"""

from pathlib import Path
import pandas as pd


def load_tables(repo_root: Path) -> pd.DataFrame:
    host_path = repo_root / "stage2" / "external_frw_host" / "outputs" / "tables" / "stage2_external_frw_rung1_age_crosscheck_v1.csv"
    joint_path = repo_root / "stage2" / "joint_mech_frw_analysis" / "outputs" / "tables" / "stage2_joint_theta_grid_v1.csv"
    anchor_path = repo_root / "stage2" / "frw_data_probe_analysis" / "outputs" / "tables" / "stage2_frw_empirical_anchor_mask_v1.csv"

    if not host_path.exists():
        raise FileNotFoundError(f"Missing host cross-check table: {host_path}")
    if not joint_path.exists():
        raise FileNotFoundError(f"Missing joint theta grid: {joint_path}")
    if not anchor_path.exists():
        raise FileNotFoundError(f"Missing empirical anchor mask: {anchor_path}")

    df_host = pd.read_csv(host_path)
    df_joint = pd.read_csv(joint_path)
    df_anchor = pd.read_csv(anchor_path)

    # We join on theta, which is present in all three tables
    cols_joint = ["theta"]
    if "in_toy_corridor" in df_joint.columns:
        cols_joint.append("in_toy_corridor")
    df = df_host.merge(df_joint[cols_joint], on="theta", how="left")

    # Anchor mask: expect column 'in_empirical_anchor_box'
    cols_anchor = ["theta"]
    if "in_empirical_anchor_box" in df_anchor.columns:
        cols_anchor.append("in_empirical_anchor_box")
    df = df.merge(df_anchor[cols_anchor], on="theta", how="left")

    # Normalise boolean-like columns
    bool_cols = []
    if "frw_viable" in df.columns:
        bool_cols.append("frw_viable")
    if "in_toy_corridor" in df.columns:
        bool_cols.append("in_toy_corridor")
    if "in_empirical_anchor_box" in df.columns:
        bool_cols.append("in_empirical_anchor_box")

    for c in bool_cols:
        df[c] = df[c].fillna(False).astype(bool)

    return df


def summarise_set(name: str, df: pd.DataFrame, mask: pd.Series, total_n: int) -> dict:
    subset = df[mask].copy()
    n = len(subset)
    frac = n / float(total_n) if total_n > 0 else 0.0

    if n == 0:
        return {
            "set": name,
            "n_theta": 0,
            "frac_of_grid": 0.0,
            "age_Gyr_diff_mean": 0.0,
            "age_Gyr_diff_std": 0.0,
            "age_Gyr_diff_min": 0.0,
            "age_Gyr_diff_max": 0.0,
            "age_Gyr_rel_diff_mean": 0.0,
            "age_Gyr_rel_diff_std": 0.0,
            "age_Gyr_rel_diff_min": 0.0,
            "age_Gyr_rel_diff_max": 0.0,
        }

    def s(col: str):
        return subset[col].mean(), subset[col].std(), subset[col].min(), subset[col].max()

    diff_mean, diff_std, diff_min, diff_max = s("age_Gyr_diff")
    rdiff_mean, rdiff_std, rdiff_min, rdiff_max = s("age_Gyr_rel_diff")

    return {
        "set": name,
        "n_theta": int(n),
        "frac_of_grid": frac,
        "age_Gyr_diff_mean": diff_mean,
        "age_Gyr_diff_std": diff_std,
        "age_Gyr_diff_min": diff_min,
        "age_Gyr_diff_max": diff_max,
        "age_Gyr_rel_diff_mean": rdiff_mean,
        "age_Gyr_rel_diff_std": rdiff_std,
        "age_Gyr_rel_diff_min": rdiff_min,
        "age_Gyr_rel_diff_max": rdiff_max,
    }


def main() -> None:
    repo_root = Path(__file__).resolve().parents[3]
    print("[external_frw_host_rungX2] Repo root:", repo_root)

    df = load_tables(repo_root)
    total_n = len(df)
    print(f"[external_frw_host_rungX2] Rows in host cross-check table: {total_n}")

    # Ensure required numeric columns exist
    required_cols = ["age_Gyr_diff", "age_Gyr_rel_diff"]
    for c in required_cols:
        if c not in df.columns:
            raise RuntimeError(f"Required column '{c}' not found in host cross-check table.")

    # Define masks
    frw_viable = df.get("frw_viable", False)
    corridor = df.get("in_toy_corridor", False)
    anchor = df.get("in_empirical_anchor_box", False)

    if not isinstance(frw_viable, pd.Series):
        frw_viable = pd.Series([False] * total_n)
    if not isinstance(corridor, pd.Series):
        corridor = pd.Series([False] * total_n)
    if not isinstance(anchor, pd.Series):
        anchor = pd.Series([False] * total_n)

    masks = {
        "ALL_GRID": pd.Series([True] * total_n),
        "FRW_VIABLE": frw_viable,
        "CORRIDOR_AND_VIABLE": corridor & frw_viable,
        "CORRIDOR_AND_VIABLE_AND_ANCHOR": corridor & frw_viable & anchor,
    }

    records = []
    for name, mask in masks.items():
        rec = summarise_set(name, df, mask, total_n)
        records.append(rec)

    out_df = pd.DataFrame.from_records(records)
    out_path = repo_root / "stage2" / "external_frw_host" / "outputs" / "tables" / "stage2_external_frw_rung2_age_contrast_v1.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_df.to_csv(out_path, index=False)

    print("[external_frw_host_rungX2] Output written:", out_path)
    for rec in records:
        print(
            f"  {rec['set']}: n={rec['n_theta']}, frac={rec['frac_of_grid']:.6f}, "
            f"⟨Δage⟩={rec['age_Gyr_diff_mean']:.3f} Gyr, "
            f"⟨|Δage|/age_repo⟩≈{abs(rec['age_Gyr_rel_diff_mean']):.3f}"
        )


if __name__ == "__main__":
    main()
