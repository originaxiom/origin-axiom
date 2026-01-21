#!/usr/bin/env python3
"""
Stage 2 obstruction helper: theta-star alignment diagnostic (v1).

Reads the static FRW kernel and obstruction external-corridor tables,
finds the grid point closest to theta_star_target, and records the
corridor membership flags in a one-row CSV.

Inputs (must already exist):
- stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv
- stage2/obstruction_tests/outputs/tables/stage2_obstruction_toy_lt_corridor_from_lcdm_box_v1.csv
- stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_lt_corridor_v1.csv
- stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_corridor_v2.csv
- stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_expansion_corridors_v1.csv

Output:
- stage2/obstruction_tests/outputs/tables/stage2_obstruction_theta_star_alignment_v1.csv
"""

from pathlib import Path
import sys

import numpy as np
import pandas as pd


def main() -> int:
    name = "stage2_obstruction_theta_star_alignment_v1"
    theta_star_target = 2.178458

    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[3]
    print(f"[{name}] Repo root: {repo_root}")

    static_path = repo_root / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv"
    toy_lt_path = repo_root / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_toy_lt_corridor_from_lcdm_box_v1.csv"
    ext_lt_path = repo_root / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_lt_corridor_v1.csv"
    age_v2_path = repo_root / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_corridor_v2.csv"
    ageexp_path = repo_root / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_expansion_corridors_v1.csv"

    inputs = [
        ("static_kernel", static_path),
        ("toy_lt_corridor_from_lcdm_box_v1", toy_lt_path),
        ("external_lt_corridor_v1", ext_lt_path),
        ("external_age_corridor_v2", age_v2_path),
        ("external_age_expansion_corridors_v1", ageexp_path),
    ]

    for label, path in inputs:
        if not path.exists():
            print(f"[{name}] ERROR: input table not found: {path}")
            return 1

    df_static = pd.read_csv(static_path)
    df_toy_lt = pd.read_csv(toy_lt_path)
    df_ext_lt = pd.read_csv(ext_lt_path)
    df_age_v2 = pd.read_csv(age_v2_path)
    df_ageexp = pd.read_csv(ageexp_path)

    n = len(df_static)
    for label, df in [
        ("toy_lt_corridor_from_lcdm_box_v1", df_toy_lt),
        ("external_lt_corridor_v1", df_ext_lt),
        ("external_age_corridor_v2", df_age_v2),
        ("external_age_expansion_corridors_v1", df_ageexp),
    ]:
        if len(df) != n:
            print(f"[{name}] ERROR: length mismatch for {label}: {len(df)} vs {n}")
            return 1
        if "theta" not in df.columns:
            print(f"[{name}] ERROR: missing 'theta' column in {label}")
            return 1

    theta_static = df_static["theta"].to_numpy()
    for label, df in [
        ("toy_lt_corridor_from_lcdm_box_v1", df_toy_lt),
        ("external_lt_corridor_v1", df_ext_lt),
        ("external_age_corridor_v2", df_age_v2),
        ("external_age_expansion_corridors_v1", df_ageexp),
    ]:
        theta_other = df["theta"].to_numpy()
        if not np.allclose(theta_static, theta_other, rtol=0.0, atol=1e-9):
            print(f"[{name}] ERROR: theta grid mismatch for {label}")
            return 1

    idx = int(np.argmin(np.abs(theta_static - theta_star_target)))
    theta_nearest = float(theta_static[idx])
    delta_theta = float(theta_nearest - theta_star_target)

    row_static = df_static.iloc[idx]
    row_toy_lt = df_toy_lt.iloc[idx]
    row_ext_lt = df_ext_lt.iloc[idx]
    row_age_v2 = df_age_v2.iloc[idx]
    row_ageexp = df_ageexp.iloc[idx]

    out_row = {
        "grid_index": idx,
        "theta_star_target": theta_star_target,
        "theta_nearest": theta_nearest,
        "delta_theta": delta_theta,
        "E_vac": float(row_static["E_vac"]),
        "omega_lambda": float(row_static["omega_lambda"]),
        "age_Gyr": float(row_static["age_Gyr"]),
        "in_pre_data_kernel": int(row_static["in_pre_data_kernel"]),
        "lcdm_like": int(row_static["lcdm_like"]),
        "in_toy_corridor": int(row_static["in_toy_corridor"]),
        "lt_corridor_box_from_lcdm": int(row_toy_lt["lt_corridor_box_from_lcdm"]),
        "external_age_corridor_v2": int(row_age_v2["external_age_corridor_v2"]),
        "external_lt_corridor_v1": int(row_ext_lt["external_lt_corridor_v1"]),
        "age_broad_v1": int(row_ageexp["age_broad_v1"]),
        "age_tight_v1": int(row_ageexp["age_tight_v1"]),
        "expansion_broad_v1": int(row_ageexp["expansion_broad_v1"]),
        "expansion_tight_v1": int(row_ageexp["expansion_tight_v1"]),
        "struct_proxy_basic_v1": int(row_ageexp["struct_proxy_basic_v1"]),
        "struct_proxy_tight_v1": int(row_ageexp["struct_proxy_tight_v1"]),
    }

    out_dir = repo_root / "stage2/obstruction_tests/outputs/tables"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "stage2_obstruction_theta_star_alignment_v1.csv"

    pd.DataFrame([out_row]).to_csv(out_path, index=False)

    print(f"[{name}] Grid points: {n}")
    print(f"[{name}] theta_star_target: {theta_star_target:.6f}")
    print(f"[{name}] theta_nearest:     {theta_nearest:.6f}")
    print(f"[{name}] delta_theta:       {delta_theta:.6e}")
    print(f"[{name}] Output: {out_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
