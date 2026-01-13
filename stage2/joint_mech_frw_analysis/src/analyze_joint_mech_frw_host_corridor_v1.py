#!/usr/bin/env python3
"""
Stage 2 – Host-calibrated FRW corridor summary (rung HX1)

Defines a "host-calibrated FRW corridor" using:
  - frw_viable (from the Phase 4 FRW toy)
  - age_consistent_rel_le_20pct (from external_frw_host rung3)

Then inspects its overlap with:
  - the original toy corridor (in_toy_corridor),
  - the empirical anchor box (in_empirical_anchor_box).

Outputs a small summary CSV.

Scope: diagnostic only. This does NOT promote any new claims into the Phase narrative.
"""

from pathlib import Path
import pandas as pd


def get_repo_root() -> Path:
    # this script lives under stage2/joint_mech_frw_analysis/src/
    return Path(__file__).resolve().parents[3]


def main() -> None:
    repo_root = get_repo_root()

    joint_grid_path = (
        repo_root
        / "stage2"
        / "joint_mech_frw_analysis"
        / "outputs"
        / "tables"
        / "stage2_joint_theta_grid_v1.csv"
    )

    age_mask_path = (
        repo_root
        / "stage2"
        / "external_frw_host"
        / "outputs"
        / "tables"
        / "stage2_external_frw_rung3_age_consistency_mask_v1.csv"
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
        / "joint_mech_frw_analysis"
        / "outputs"
        / "tables"
        / "stage2_joint_mech_frw_host_corridor_summary_v1.csv"
    )

    print("[stage2_host_corridor_hx1]")
    print(f"  Repo root:        {repo_root}")
    print(f"  Joint grid:       {joint_grid_path}")
    print(f"  Age mask:         {age_mask_path}")
    print(f"  Anchor mask:      {anchor_mask_path}")

    # Joint grid (has theta_index, theta, frw_viable, in_toy_corridor, etc.)
    df_joint = pd.read_csv(joint_grid_path)

    # Age-consistency mask (built in external_frw_host rungX3) – join on theta_index
    df_age = pd.read_csv(age_mask_path)
    age_cols = ["theta_index", "age_consistent_rel_le_20pct"]
    for c in age_cols:
        if c not in df_age.columns:
            raise RuntimeError(f"Missing column '{c}' in age-consistency table.")
    df_age = df_age[age_cols]

    # Empirical anchor mask (built in frw_data_probe_analysis A3) – join on theta
    df_anchor = pd.read_csv(anchor_mask_path)
    anchor_cols = ["theta", "in_empirical_anchor_box"]
    for c in anchor_cols:
        if c not in df_anchor.columns:
            raise RuntimeError(f"Missing column '{c}' in anchor-mask table.")
    df_anchor = df_anchor[anchor_cols]

    # Join age mask on theta_index
    df = df_joint.merge(df_age, on="theta_index", how="left")

    # Join anchor mask on theta
    df = df.merge(df_anchor, on="theta", how="left")

    # fill missing booleans with False
    for col in ["age_consistent_rel_le_20pct", "in_empirical_anchor_box"]:
        if col in df.columns:
            df[col] = df[col].fillna(False).astype(bool)

    # sanity checks
    for required in ["frw_viable", "in_toy_corridor"]:
        if required not in df.columns:
            raise RuntimeError(f"Joint grid is missing required column '{required}'.")

    # define host-calibrated corridor
    df["in_host_calibrated_corridor"] = df["frw_viable"] & df["age_consistent_rel_le_20pct"]
    df["in_host_corridor_and_anchor"] = (
        df["in_host_calibrated_corridor"] & df["in_empirical_anchor_box"]
    )

    n_total = len(df)
    sets = {
        "ALL_GRID": df.index,
        "FRW_VIABLE": df.index[df["frw_viable"]],
        "TOY_CORRIDOR": df.index[df["in_toy_corridor"]],
        "HOST_CALIBRATED_CORRIDOR": df.index[df["in_host_calibrated_corridor"]],
        "HOST_CORRIDOR_AND_ANCHOR": df.index[df["in_host_corridor_and_anchor"]],
    }

    rows = []
    print(f"  Total grid rows:  {n_total}")
    for name, idx in sets.items():
        n = len(idx)
        frac = n / n_total if n_total > 0 else 0.0
        rows.append(
            {
                "set": name,
                "n_theta": n,
                "frac_of_grid": frac,
            }
        )
        print(f"  {name:24s} n={n:4d}, frac={frac:0.6f}")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(out_path, index=False)
    print(f"  Output written:   {out_path}")


if __name__ == "__main__":
    main()
