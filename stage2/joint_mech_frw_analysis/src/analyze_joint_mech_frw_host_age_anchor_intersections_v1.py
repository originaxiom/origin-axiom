#!/usr/bin/env python3
"""
Stage 2 – host FRW age anchor intersections (hx-age1)

Goal:
  Take the joint θ-grid and the external FRW host age-anchor mask, and
  summarise how the host-age anchor overlaps with:
    - the full grid,
    - the FRW-viable subset,
    - the Phase 4 toy corridor.

Inputs:
  - stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv
      Expected columns (at least):
        * theta_index
        * theta
        * frw_viable
        * in_toy_corridor   (boolean; toy corridor mask)

  - stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_mask_v1.csv
      Expected columns (at least):
        * theta_index
        * in_host_age_anchor_window  (boolean; host age-anchor mask)

Output:
  - stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_age_anchor_intersections_v1.csv

The output table has:
  - set          (label)
  - n_theta      (number of θ points in the set)
  - frac_of_grid (fraction of the full θ-grid)
"""

from pathlib import Path
import pandas as pd


def count_frac(mask):
    n = int(mask.sum())
    frac = float(n) / float(len(mask)) if len(mask) > 0 else 0.0
    return n, frac


def main() -> None:
    here = Path(__file__).resolve()
    repo_root = here.parents[3]

    joint_grid_path = repo_root / "stage2" / "joint_mech_frw_analysis" / "outputs" / "tables" / "stage2_joint_theta_grid_v1.csv"
    host_age_mask_path = repo_root / "stage2" / "external_frw_host" / "outputs" / "tables" / "stage2_external_frw_host_age_anchor_mask_v1.csv"
    out_path = repo_root / "stage2" / "joint_mech_frw_analysis" / "outputs" / "tables" / "stage2_joint_mech_frw_host_age_anchor_intersections_v1.csv"

    print("[stage2_host_age_anchor_intersections_v1]")
    print(f"  Joint grid:    {joint_grid_path}")
    print(f"  Host age mask: {host_age_mask_path}")

    if not joint_grid_path.is_file():
        raise FileNotFoundError(f"Joint grid not found: {joint_grid_path}")
    if not host_age_mask_path.is_file():
        raise FileNotFoundError(f"Host age-anchor mask not found: {host_age_mask_path}")

    df_joint = pd.read_csv(joint_grid_path)
    df_host = pd.read_csv(host_age_mask_path)

    required_joint = {"theta_index", "frw_viable"}
    missing_joint = required_joint - set(df_joint.columns)
    if missing_joint:
        raise RuntimeError(f"Missing columns in joint grid: {sorted(missing_joint)}")

    required_host = {"theta_index", "in_host_age_anchor_window"}
    missing_host = required_host - set(df_host.columns)
    if missing_host:
        raise RuntimeError(f"Missing columns in host age-anchor table: {sorted(missing_host)}")

    # Optional corridor column: prefer in_toy_corridor, fall back to toy_corridor if present.
    corridor_col = None
    if "in_toy_corridor" in df_joint.columns:
        corridor_col = "in_toy_corridor"
    elif "toy_corridor" in df_joint.columns:
        corridor_col = "toy_corridor"

    if corridor_col is None:
        # If there is genuinely no corridor column, we still proceed,
        # but treat "TOY_CORRIDOR" as the full grid.
        print("  WARNING: no in_toy_corridor / toy_corridor column found; treating TOY_CORRIDOR as ALL_GRID.")
        df_joint["__corr_dummy__"] = True
        corridor_col = "__corr_dummy__"

    # Merge on theta_index so we can see the host-age anchor flag alongside the joint grid.
    df = df_joint.merge(
        df_host[["theta_index", "in_host_age_anchor_window"]],
        on="theta_index",
        how="left",
        validate="one_to_one",
    )

    # Normalise masks to boolean.
    n_total = len(df)
    df["frw_viable"] = df["frw_viable"].astype(bool)
    df[corridor_col] = df[corridor_col].astype(bool)
    df["in_host_age_anchor_window"] = df["in_host_age_anchor_window"].fillna(False).astype(bool)

    mask_all = df["theta"].notna()
    mask_frw = df["frw_viable"]
    mask_corr = df[corridor_col]
    mask_host_age = df["in_host_age_anchor_window"]

    sets = {
        "ALL_GRID": mask_all,
        "FRW_VIABLE": mask_frw,
        "TOY_CORRIDOR": mask_corr,
        "HOST_AGE_ANCHOR": mask_host_age,
        "FRW_VIABLE_AND_HOST_AGE_ANCHOR": mask_frw & mask_host_age,
        "CORRIDOR_AND_HOST_AGE_ANCHOR": mask_corr & mask_host_age,
        "CORRIDOR_AND_VIABLE_AND_HOST_AGE_ANCHOR": mask_corr & mask_frw & mask_host_age,
    }

    print(f"  Total grid rows: {n_total}")
    rows = []
    for name, m in sets.items():
        n, frac = count_frac(m)
        print(f"  {name:34s} n={n:4d}, frac={frac:0.6f}")
        rows.append({"set": name, "n_theta": n, "frac_of_grid": frac})

    out_df = pd.DataFrame(rows, columns=["set", "n_theta", "frac_of_grid"])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_df.to_csv(out_path, index=False)
    print(f"  Output written: {out_path}")


if __name__ == "__main__":
    main()
