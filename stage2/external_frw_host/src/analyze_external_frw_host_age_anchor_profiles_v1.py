#!/usr/bin/env python3
"""
Stage 2 – external FRW host age-anchor profiles (hx-age2)

Summarise the host-age anchor subset in terms of:
  - theta range
  - omega_lambda, age_host, age_toy
  - mechanism amplitudes (via the joint grid)

Inputs:
  - stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_mask_v1.csv
      (from flag_external_frw_host_age_anchor_v1.py)

  - stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv

Output:
  - stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_profiles_v1.csv
"""

from pathlib import Path
import pandas as pd


def main() -> None:
    here = Path(__file__).resolve()
    repo_root = here.parents[3]

    host_mask_path = repo_root / "stage2" / "external_frw_host" / "outputs" / "tables" / "stage2_external_frw_host_age_anchor_mask_v1.csv"
    joint_grid_path = repo_root / "stage2" / "joint_mech_frw_analysis" / "outputs" / "tables" / "stage2_joint_theta_grid_v1.csv"
    out_path = repo_root / "stage2" / "external_frw_host" / "outputs" / "tables" / "stage2_external_frw_host_age_anchor_profiles_v1.csv"

    print("[external_frw_host_age_anchor_profiles_v1]")
    print(f"  Host age-anchor mask: {host_mask_path}")
    print(f"  Joint grid:           {joint_grid_path}")

    if not host_mask_path.is_file():
        raise FileNotFoundError(f"Host age-anchor mask not found: {host_mask_path}")
    if not joint_grid_path.is_file():
        raise FileNotFoundError(f"Joint grid not found: {joint_grid_path}")

    df_host = pd.read_csv(host_mask_path)
    df_joint = pd.read_csv(joint_grid_path)

    required_host = {"theta_index", "theta", "omega_lambda", "age_Gyr_host", "age_Gyr_toy", "frw_viable", "in_host_age_anchor_window"}
    missing_host = required_host - set(df_host.columns)
    if missing_host:
        raise RuntimeError(f"Missing columns in host age-anchor mask: {sorted(missing_host)}")

    required_joint = {"theta_index", "theta",
                      "mech_baseline_A0", "mech_baseline_A_floor", "mech_baseline_bound",
                      "mech_binding_A0", "mech_binding_A", "mech_binding_bound",
                      "in_toy_corridor"}
    missing_joint = required_joint - set(df_joint.columns)
    if missing_joint:
        raise RuntimeError(f"Missing columns in joint grid: {sorted(missing_joint)}")

    # Merge to pull mechanism columns and corridor flag onto the host anchor subset.
    df = df_host.merge(
        df_joint[list(required_joint)],
        on=["theta_index", "theta"],
        how="left",
        validate="one_to_one",
    )

    mask_anchor = df["in_host_age_anchor_window"].astype(bool)
    df_anchor = df[mask_anchor].copy()
    n_anchor = len(df_anchor)

    print(f"  Total rows in host mask: {len(df)}")
    print(f"  Rows in host age-anchor: {n_anchor}")

    if n_anchor == 0:
        print("  No host age-anchor points; nothing to profile.")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        # Write an empty file with just a header.
        pd.DataFrame(columns=["n_theta"]).to_csv(out_path, index=False)
        print(f"  Wrote empty profiles table: {out_path}")
        return

    theta_min = df_anchor["theta"].min()
    theta_max = df_anchor["theta"].max()

    summary = {
        "n_theta": n_anchor,
        "theta_min": theta_min,
        "theta_max": theta_max,
        "omega_lambda_mean": df_anchor["omega_lambda"].mean(),
        "omega_lambda_std": df_anchor["omega_lambda"].std(),
        "omega_lambda_min": df_anchor["omega_lambda"].min(),
        "omega_lambda_max": df_anchor["omega_lambda"].max(),
        "age_Gyr_host_mean": df_anchor["age_Gyr_host"].mean(),
        "age_Gyr_host_std": df_anchor["age_Gyr_host"].std(),
        "age_Gyr_host_min": df_anchor["age_Gyr_host"].min(),
        "age_Gyr_host_max": df_anchor["age_Gyr_host"].max(),
        "age_Gyr_toy_mean": df_anchor["age_Gyr_toy"].mean(),
        "age_Gyr_toy_std": df_anchor["age_Gyr_toy"].std(),
        "age_Gyr_toy_min": df_anchor["age_Gyr_toy"].min(),
        "age_Gyr_toy_max": df_anchor["age_Gyr_toy"].max(),
        "mech_baseline_A0_mean": df_anchor["mech_baseline_A0"].mean(),
        "mech_baseline_A0_std": df_anchor["mech_baseline_A0"].std(),
        "mech_baseline_A0_min": df_anchor["mech_baseline_A0"].min(),
        "mech_baseline_A0_max": df_anchor["mech_baseline_A0"].max(),
        "mech_baseline_A_floor_mean": df_anchor["mech_baseline_A_floor"].mean(),
        "mech_baseline_A_floor_std": df_anchor["mech_baseline_A_floor"].std(),
        "mech_baseline_A_floor_min": df_anchor["mech_baseline_A_floor"].min(),
        "mech_baseline_A_floor_max": df_anchor["mech_baseline_A_floor"].max(),
        "mech_binding_A0_mean": df_anchor["mech_binding_A0"].mean(),
        "mech_binding_A0_std": df_anchor["mech_binding_A0"].std(),
        "mech_binding_A0_min": df_anchor["mech_binding_A0"].min(),
        "mech_binding_A0_max": df_anchor["mech_binding_A0"].max(),
        "mech_binding_A_mean": df_anchor["mech_binding_A"].mean(),
        "mech_binding_A_std": df_anchor["mech_binding_A"].std(),
        "mech_binding_A_min": df_anchor["mech_binding_A"].min(),
        "mech_binding_A_max": df_anchor["mech_binding_A"].max(),
        "frac_in_toy_corridor": float(df_anchor["in_toy_corridor"].sum()) / float(n_anchor),
    }

    out_df = pd.DataFrame([summary])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_df.to_csv(out_path, index=False)
    print(f"  Profiles written: {out_path}")


if __name__ == "__main__":
    main()
