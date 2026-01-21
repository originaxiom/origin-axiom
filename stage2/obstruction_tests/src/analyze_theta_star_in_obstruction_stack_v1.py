#!/usr/bin/env python3
import math
from pathlib import Path

import pandas as pd


def main() -> int:
    repo_root = Path(__file__).resolve().parents[3]
    base_path = repo_root / "stage2/obstruction_tests/outputs/tables"

    kernel_with_mech_path = base_path / "stage2_obstruction_kernel_with_mech_v1.csv"
    age_exp_path = base_path / "stage2_obstruction_external_age_expansion_corridors_v1.csv"

    df_kernel = pd.read_csv(kernel_with_mech_path)
    df_ageexp = pd.read_csv(age_exp_path)

    # φ^φ
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    theta_star = phi ** phi

    # Find nearest grid point in kernel table
    idx = (df_kernel["theta"] - theta_star).abs().idxmin()
    row_kernel = df_kernel.iloc[idx]

    theta_nearest = float(row_kernel["theta"])
    delta_theta = float(theta_nearest - theta_star)

    # Align with age/expansion table on theta
    # (they are on the same 2048-point grid)
    row_ageexp = df_ageexp.loc[(df_ageexp["theta"] - theta_nearest).abs().idxmin()]

    # Collect a compact summary row
    out = {
        "theta_star_target": theta_star,
        "theta_nearest": theta_nearest,
        "delta_theta": delta_theta,
        "idx": int(idx),
        "E_vac": float(row_kernel["E_vac"]),
        "omega_lambda": float(row_kernel["omega_lambda"]),
        "age_Gyr": float(row_kernel["age_Gyr"]),
        "in_pre_data_kernel": bool(row_kernel["in_pre_data_kernel"]),
        "lcdm_like": bool(row_kernel["lcdm_like"]),
        "in_toy_corridor": bool(row_ageexp["in_toy_corridor"]),
        "in_age_broad_v1": bool(row_ageexp["age_broad_v1"]),
        "in_age_tight_v1": bool(row_ageexp["age_tight_v1"]),
        "in_expansion_broad_v1": bool(row_ageexp["expansion_broad_v1"]),
        "in_expansion_tight_v1": bool(row_ageexp["expansion_tight_v1"]),
        "in_struct_proxy_basic_v1": bool(row_ageexp["struct_proxy_basic_v1"]),
        "in_struct_proxy_tight_v1": bool(row_ageexp["struct_proxy_tight_v1"]),
        "mech_baseline_A0": float(row_kernel["mech_baseline_A0"]),
        "mech_baseline_A_floor": float(row_kernel["mech_baseline_A_floor"]),
        "mech_baseline_bound": float(row_kernel["mech_baseline_bound"]),
        "mech_binding_A0": float(row_kernel["mech_binding_A0"]),
        "mech_binding_A": float(row_kernel["mech_binding_A"]),
        "mech_binding_bound": float(row_kernel["mech_binding_bound"]),
    }

    out_df = pd.DataFrame([out])

    out_path = base_path / "stage2_obstruction_theta_star_in_stack_v1.csv"
    out_df.to_csv(out_path, index=False)

    print("[analyze_theta_star_in_obstruction_stack_v1]")
    print(f"  repo_root: {repo_root}")
    print(f"  theta_star target: {theta_star:.9f}")
    print(f"  nearest grid theta: {theta_nearest:.9f} (Δθ = {delta_theta:.3e}, idx={idx})")
    print(f"  in_pre_data_kernel: {out['in_pre_data_kernel']}")
    print(f"  lcdm_like: {out['lcdm_like']}")
    print(f"  in_toy_corridor: {out['in_toy_corridor']}")
    print(f"  in_age_tight_v1: {out['in_age_tight_v1']}, in_expansion_tight_v1: {out['in_expansion_tight_v1']}")
    print(f"  wrote summary: {out_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
