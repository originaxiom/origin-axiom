#!/usr/bin/env python
"""
Stage 2 – Joint mech–FRW–host: host-anchored empirical box intersections.

Reads:
  - stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv
      (theta_index, theta, E_vac, omega_lambda, age_Gyr, in_toy_corridor,
       frw_viable, lcdm_like, ..., mech_* columns)
  - stage2/external_frw_host/outputs/tables/stage2_external_frw_host_anchor_mask_v1.csv
      (theta_index, theta, omega_lambda, age_Gyr, age_Gyr_host, frw_viable,
       in_host_empirical_anchor_box)

Writes:
  - stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_host_anchor_intersections_v1.csv

And prints counts/fractions for:
  - ALL_GRID
  - FRW_VIABLE
  - TOY_CORRIDOR
  - HOST_ANCHOR
  - FRW_VIABLE_AND_HOST_ANCHOR
  - CORRIDOR_AND_HOST_ANCHOR
  - CORRIDOR_AND_VIABLE_AND_HOST_ANCHOR
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


def main() -> None:
    root = Path(__file__).resolve().parents[3]

    joint_grid_path = (
        root
        / "stage2"
        / "joint_mech_frw_analysis"
        / "outputs"
        / "tables"
        / "stage2_joint_theta_grid_v1.csv"
    )
    host_anchor_path = (
        root
        / "stage2"
        / "external_frw_host"
        / "outputs"
        / "tables"
        / "stage2_external_frw_host_anchor_mask_v1.csv"
    )
    out_path = (
        root
        / "stage2"
        / "joint_mech_frw_analysis"
        / "outputs"
        / "tables"
        / "stage2_joint_mech_frw_host_anchor_intersections_v1.csv"
    )

    print("[stage2_host_anchor_intersections_v1]")
    print(f"  Joint grid:    {joint_grid_path}")
    print(f"  Host anchor:   {host_anchor_path}")

    if not joint_grid_path.is_file():
        raise FileNotFoundError(f"Joint grid not found: {joint_grid_path}")
    if not host_anchor_path.is_file():
        raise FileNotFoundError(f"Host anchor mask not found: {host_anchor_path}")

    df_joint = pd.read_csv(joint_grid_path)
    df_anchor = pd.read_csv(host_anchor_path)

    required_joint = ["theta_index", "theta", "frw_viable", "in_toy_corridor"]
    missing_joint = [c for c in required_joint if c not in df_joint.columns]
    if missing_joint:
        raise RuntimeError(f"Missing columns in joint grid: {missing_joint}")

    required_anchor = ["theta_index", "theta", "in_host_empirical_anchor_box"]
    missing_anchor = [c for c in required_anchor if c not in df_anchor.columns]
    if missing_anchor:
        raise RuntimeError(f"Missing columns in host-anchor table: {missing_anchor}")

    df = df_joint.merge(
        df_anchor[["theta_index", "theta", "in_host_empirical_anchor_box"]],
        on=["theta_index", "theta"],
        how="left",
        validate="one_to_one",
    )

    df["in_host_empirical_anchor_box"] = df["in_host_empirical_anchor_box"].fillna(False)

    n_total = len(df)
    mask_frw = df["frw_viable"].astype(bool)
    mask_corr = df["in_toy_corridor"].astype(bool)
    mask_anchor = df["in_host_empirical_anchor_box"].astype(bool)

    def count_frac(mask: np.ndarray) -> tuple[int, float]:
        n = int(mask.sum())
        frac = n / float(n_total) if n_total > 0 else np.nan
        return n, frac

    sets = {
        "ALL_GRID": np.ones(n_total, dtype=bool),
        "FRW_VIABLE": mask_frw,
        "TOY_CORRIDOR": mask_corr,
        "HOST_ANCHOR": mask_anchor,
        "FRW_VIABLE_AND_HOST_ANCHOR": mask_frw & mask_anchor,
        "CORRIDOR_AND_HOST_ANCHOR": mask_corr & mask_anchor,
        "CORRIDOR_AND_VIABLE_AND_HOST_ANCHOR": mask_corr & mask_frw & mask_anchor,
    }

    print(f"  Total grid rows: {n_total}")
    rows = []
    for name, m in sets.items():
        n, frac = count_frac(m)
        print(f"  {name:28s} n={n:4d}, frac={frac:0.6f}")
        rows.append({"set": name, "n_theta": n, "frac_of_grid": frac})

    out_df = pd.DataFrame(rows, columns=["set", "n_theta", "frac_of_grid"])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_df.to_csv(out_path, index=False)
    print(f"  Output written: {out_path}")


if __name__ == "__main__":
    main()
