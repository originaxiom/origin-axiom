#!/usr/bin/env python3
"""
Stage 2 – External FRW host – Rung X3: age-consistency mask

Goal:
  - Starting from:
      * the joint mech–FRW theta grid, and
      * the external host age cross-check table, and
      * the empirical anchor mask,
    construct a boolean mask indicating where the host age and Phase 4 toy age
    agree to within a chosen relative threshold (default: 20%).

  - Summarise how many theta points are age-consistent in:
      * ALL_GRID
      * FRW_VIABLE
      * CORRIDOR_AND_VIABLE
      * CORRIDOR_AND_VIABLE_AND_ANCHOR

Outputs:
  - Row-level table:
      stage2/external_frw_host/outputs/tables/
        stage2_external_frw_rung3_age_consistency_mask_v1.csv

    with columns including:
      - theta_index, theta
      - omega_lambda
      - age_Gyr, age_Gyr_host, age_Gyr_rel_diff
      - frw_viable, in_toy_corridor
      - <anchor mask column> (e.g. in_empirical_anchor_box)
      - age_rel_err_abs
      - age_consistent_rel_le_20pct
"""

from pathlib import Path
import pandas as pd


def main() -> None:
    # Resolve repo root assuming:
    #   stage2/external_frw_host/src/flag_age_consistent_subset_v1.py
    repo_root = Path(__file__).resolve().parents[3]

    joint_grid_path = (
        repo_root
        / "stage2"
        / "joint_mech_frw_analysis"
        / "outputs"
        / "tables"
        / "stage2_joint_theta_grid_v1.csv"
    )
    host_age_path = (
        repo_root
        / "stage2"
        / "external_frw_host"
        / "outputs"
        / "tables"
        / "stage2_external_frw_rung1_age_crosscheck_v1.csv"
    )
    anchor_mask_path = (
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
        / "stage2_external_frw_rung3_age_consistency_mask_v1.csv"
    )

    print("[external_frw_host_rungX3]")
    print(f"  Repo root:         {repo_root}")
    print(f"  Joint grid:        {joint_grid_path}")
    print(f"  Host cross-check:  {host_age_path}")
    print(f"  Anchor mask:       {anchor_mask_path}")

    # --- Load inputs ---
    df_joint = pd.read_csv(joint_grid_path)
    df_host = pd.read_csv(host_age_path)
    df_anchor = pd.read_csv(anchor_mask_path)

    # Sanity checks on required columns
    for col in ["theta_index", "age_Gyr_rel_diff"]:
        if col not in df_host.columns:
            raise RuntimeError(f"Missing column in host cross-check table: {col}")

    for col in ["theta_index", "theta", "frw_viable", "in_toy_corridor"]:
        if col not in df_joint.columns:
            raise RuntimeError(f"Missing column in joint grid: {col}")

    if "theta" not in df_anchor.columns:
        raise RuntimeError("Anchor mask table must contain 'theta' column.")

    # Try to infer the anchor mask column name
    anchor_col = None
    for c in df_anchor.columns:
        if c.startswith("in_") and "anchor" in c:
            anchor_col = c
            break
    if anchor_col is None:
        raise RuntimeError(
            "Could not find empirical anchor mask column in anchor table "
            "(expected something like 'in_empirical_anchor_box')."
        )

    # --- Join: joint grid + host age on theta_index ---
    cols_joint = ["theta_index", "theta", "frw_viable", "in_toy_corridor"]
    cols_host = [
        "theta_index",
        "omega_lambda",
        "age_Gyr",
        "age_Gyr_host",
        "age_Gyr_rel_diff",
    ]

    df = pd.merge(
        df_joint[cols_joint],
        df_host[cols_host],
        on="theta_index",
        how="inner",
        validate="one_to_one",
    )

    # --- Join: anchor mask on theta ---
    df = pd.merge(
        df,
        df_anchor[["theta", anchor_col]],
        on="theta",
        how="left",
        validate="one_to_one",
    )

    # Fill missing anchor flags as False
    df[anchor_col] = df[anchor_col].fillna(False).astype(bool)

    # --- Define age-consistency mask ---
    df["age_rel_err_abs"] = df["age_Gyr_rel_diff"].abs()

    # Threshold: 20% relative error
    rel_thresh = 0.20
    mask_col = f"age_consistent_rel_le_{int(rel_thresh * 100)}pct"
    df[mask_col] = df["age_rel_err_abs"] <= rel_thresh

    # --- Summaries ---
    n_total = len(df)
    print(f"  Rows after joins:  {n_total}")
    print(f"  Relative-error threshold: {rel_thresh:.3f} (i.e. {rel_thresh*100:.1f}%)")
    print(f"  Anchor column:     {anchor_col}")
    print(f"  Consistency column:{mask_col}")

    def summarise(mask, name: str) -> None:
        subset = df[mask]
        n = len(subset)
        frac = n / n_total if n_total > 0 else 0.0
        if n == 0:
            print(
                f"  {name}: n_age_consistent=0, frac=0.000000, "
                f"<rel_diff>=nan, rel_diff_min=nan, rel_diff_max=nan"
            )
            return
        mu = subset["age_Gyr_rel_diff"].mean()
        mn = subset["age_Gyr_rel_diff"].min()
        mx = subset["age_Gyr_rel_diff"].max()
        print(
            f"  {name}: n_age_consistent={n}, frac={frac:.6f}, "
            f"<rel_diff>={mu:.3f}, rel_diff_min={mn:.3f}, rel_diff_max={mx:.3f}"
        )

    # Define masks
    m_all = df[mask_col]
    m_frw = (df["frw_viable"] == 1) & df[mask_col]
    m_corr_frw = (
        (df["frw_viable"] == 1)
        & (df["in_toy_corridor"] == 1)
        & df[mask_col]
    )
    m_corr_frw_anchor = (
        (df["frw_viable"] == 1)
        & (df["in_toy_corridor"] == 1)
        & df[anchor_col]
        & df[mask_col]
    )

    # Print summaries
    summarise(m_all, "ALL_GRID")
    summarise(m_frw, "FRW_VIABLE")
    summarise(m_corr_frw, "CORRIDOR_AND_VIABLE")
    summarise(m_corr_frw_anchor, "CORRIDOR_AND_VIABLE_AND_ANCHOR")

    # --- Write row-level table ---
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"  Output written:    {out_path}")


if __name__ == "__main__":
    main()
