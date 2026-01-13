#!/usr/bin/env python
"""
Stage 2 – External FRW host: host-anchored empirical box (v3, collision-safe).

Idea:
  - Use the FRW empirical anchor mask (toy-age based) ONLY as a boolean selector
    keyed by theta: in_empirical_anchor_box.
  - Join that onto the host cross-check table, which already has
    (theta_index, theta, omega_lambda, age_Gyr, age_Gyr_host, frw_viable, ...).
  - On the host side, infer a box in (omega_lambda, age_Gyr_host) from the
    subset where in_empirical_anchor_box is True.
  - Flag any theta whose (omega_lambda, age_Gyr_host) lies in that box.

Reads:
  - stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv
      (theta_index, theta, omega_lambda, age_Gyr, age_Gyr_host, age_Gyr_diff,
       age_Gyr_rel_diff, frw_viable)
  - stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_empirical_anchor_mask_v1.csv
      (theta, in_empirical_anchor_box, ...)

Writes:
  - stage2/external_frw_host/outputs/tables/stage2_external_frw_host_anchor_mask_v1.csv
      (theta_index, theta, omega_lambda, age_Gyr, age_Gyr_host, frw_viable,
       in_host_empirical_anchor_box)
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


def main() -> None:
    root = Path(__file__).resolve().parents[3]

    host_table = (
        root
        / "stage2"
        / "external_frw_host"
        / "outputs"
        / "tables"
        / "stage2_external_frw_rung1_age_crosscheck_v1.csv"
    )
    frw_anchor_table = (
        root
        / "stage2"
        / "frw_data_probe_analysis"
        / "outputs"
        / "tables"
        / "stage2_frw_empirical_anchor_mask_v1.csv"
    )
    out_table = (
        root
        / "stage2"
        / "external_frw_host"
        / "outputs"
        / "tables"
        / "stage2_external_frw_host_anchor_mask_v1.csv"
    )

    print("[external_frw_host_anchor_v1]")
    print(f"  Host table:        {host_table}")
    print(f"  FRW anchor table:  {frw_anchor_table}")

    if not host_table.is_file():
        raise FileNotFoundError(f"Host cross-check table not found: {host_table}")
    if not frw_anchor_table.is_file():
        raise FileNotFoundError(f"FRW anchor mask table not found: {frw_anchor_table}")

    df_host = pd.read_csv(host_table)
    df_frw = pd.read_csv(frw_anchor_table)

    required_host = [
        "theta_index",
        "theta",
        "omega_lambda",
        "age_Gyr",
        "age_Gyr_host",
        "frw_viable",
    ]
    missing_host = [c for c in required_host if c not in df_host.columns]
    if missing_host:
        raise RuntimeError(f"Missing columns in host table: {missing_host}")

    # FRW anchor table is only required to provide a boolean mask keyed by theta.
    required_frw = [
        "theta",
        "in_empirical_anchor_box",
    ]
    missing_frw = [c for c in required_frw if c not in df_frw.columns]
    if missing_frw:
        raise RuntimeError(f"Missing columns in FRW anchor table: {missing_frw}")

    # Join on theta; keep host's omega_lambda and age_Gyr_host intact.
    df = df_host.merge(
        df_frw[required_frw],
        on="theta",
        how="left",
        validate="many_to_one",
    )

    # Any theta not present in the FRW anchor table is treated as not-in-anchor.
    df["in_empirical_anchor_box"] = df["in_empirical_anchor_box"].fillna(False)

    # Use the FRW-anchor-selected subset to infer a host-space box.
    df_anchor = df[df["in_empirical_anchor_box"]]

    if df_anchor.empty:
        print("  WARNING: FRW empirical anchor set is empty; no host anchor can be defined.")
        df["in_host_empirical_anchor_box"] = False
    else:
        omega_min = float(df_anchor["omega_lambda"].min())
        omega_max = float(df_anchor["omega_lambda"].max())
        age_host_min = float(df_anchor["age_Gyr_host"].min())
        age_host_max = float(df_anchor["age_Gyr_host"].max())

        print("  Inferred host anchor box from FRW empirical anchor:")
        print(f"    omega_lambda in [{omega_min:.6f}, {omega_max:.6f}]")
        print(f"    age_Gyr_host in [{age_host_min:.6f}, {age_host_max:.6f}]")

        mask = (
            (df["omega_lambda"] >= omega_min)
            & (df["omega_lambda"] <= omega_max)
            & (df["age_Gyr_host"] >= age_host_min)
            & (df["age_Gyr_host"] <= age_host_max)
        )

        df["in_host_empirical_anchor_box"] = mask

    n_total = len(df)
    n_anchor = int(df["in_host_empirical_anchor_box"].sum())
    frac_anchor = n_anchor / float(n_total) if n_total > 0 else np.nan

    print(f"  Rows: {n_total}")
    print(f"  In host empirical anchor: n={n_anchor}, frac={frac_anchor:.6f}")

    out_cols = [
        "theta_index",
        "theta",
        "omega_lambda",
        "age_Gyr",
        "age_Gyr_host",
        "frw_viable",
        "in_host_empirical_anchor_box",
    ]
    for c in out_cols:
        if c not in df.columns:
            raise RuntimeError(f"Expected column missing after join: {c}")

    out_table.parent.mkdir(parents=True, exist_ok=True)
    df[out_cols].to_csv(out_table, index=False)
    print(f"  Output written: {out_table}")


if __name__ == "__main__":
    main()
