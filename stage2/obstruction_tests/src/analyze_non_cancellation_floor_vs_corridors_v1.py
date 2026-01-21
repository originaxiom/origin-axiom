#!/usr/bin/env python3
from pathlib import Path

import pandas as pd


def main() -> int:
    repo_root = Path(__file__).resolve().parents[3]
    base_path = repo_root / "stage2/obstruction_tests/outputs/tables"

    kernel_mech_path = base_path / "stage2_obstruction_kernel_with_mech_v1.csv"
    age_exp_path = base_path / "stage2_obstruction_external_age_expansion_corridors_v1.csv"

    df_km = pd.read_csv(kernel_mech_path)
    df_ageexp = pd.read_csv(age_exp_path)

    # align on theta
    merged = pd.merge(
        df_km,
        df_ageexp[
            [
                "theta",
                "in_pre_data_kernel",
                "lcdm_like",
                "in_toy_corridor",
                "age_broad_v1",
                "age_tight_v1",
                "expansion_broad_v1",
                "expansion_tight_v1",
                "struct_proxy_basic_v1",
                "struct_proxy_tight_v1",
            ]
        ],
        on="theta",
        suffixes=("", "_ageexp"),
    )

    # sanity: we expect these flags to match between tables
    merged["in_pre_data_kernel"] = merged["in_pre_data_kernel"]

    # simple non-cancellation floor (v1)
    # threshold chosen inside the kernel A0 band; tweakable later.
    floor_thresh = 0.045
    merged["mech_non_cancel_floor_v1"] = merged["mech_binding_A0"] >= floor_thresh

    families = {}

    # basic sets
    kernel_mask = merged["in_pre_data_kernel"]
    age_tight_struct_tight = (
        merged["age_tight_v1"] & merged["expansion_tight_v1"] & merged["struct_proxy_tight_v1"]
    )

    # sweet subset in kernel + external age v2 + toy corridor + lcdm_like
    # approximated here as "kernel & toy_corridor & lcdm_like & age_tight_struct_tight"
    sweet_like = kernel_mask & merged["in_toy_corridor"] & merged["lcdm_like"] & age_tight_struct_tight

    # families with floor
    families["KERNEL_AND_FLOOR_V1"] = kernel_mask & merged["mech_non_cancel_floor_v1"]
    families["KERNEL_AGE_TIGHT_EXP_STRUCT_TIGHT_AND_FLOOR_V1"] = (
        kernel_mask & age_tight_struct_tight & merged["mech_non_cancel_floor_v1"]
    )
    families["KERNEL_SWEETLIKE_AND_FLOOR_V1"] = sweet_like & merged["mech_non_cancel_floor_v1"]

    all_grid_n = len(merged)
    kernel_n = int(kernel_mask.sum())

    amp_cols = [
        "mech_baseline_A0",
        "mech_baseline_A_floor",
        "mech_baseline_bound",
        "mech_binding_A0",
        "mech_binding_A",
        "mech_binding_bound",
    ]

    rows = []
    for name, mask in families.items():
        n_points = int(mask.sum())
        if n_points == 0:
            row = {
                "family_name": name,
                "n_points": 0,
                "frac_of_grid": 0.0,
                "n_points_in_kernel": 0,
                "frac_of_kernel": 0.0,
            }
            for col in amp_cols:
                row[f"{col}_min"] = float("nan")
                row[f"{col}_max"] = float("nan")
                row[f"{col}_mean"] = float("nan")
        else:
            sub = merged.loc[mask, :]
            n_in_kernel = int(sub["in_pre_data_kernel"].sum())
            row = {
                "family_name": name,
                "n_points": n_points,
                "frac_of_grid": n_points / all_grid_n,
                "n_points_in_kernel": n_in_kernel,
                "frac_of_kernel": n_in_kernel / kernel_n if kernel_n > 0 else float("nan"),
            }
            for col in amp_cols:
                s = sub[col]
                row[f"{col}_min"] = float(s.min())
                row[f"{col}_max"] = float(s.max())
                row[f"{col}_mean"] = float(s.mean())

        rows.append(row)

    out = pd.DataFrame(rows)
    out_path = base_path / "stage2_obstruction_non_cancel_floor_vs_corridors_v1.csv"
    out.to_csv(out_path, index=False)

    print("[analyze_non_cancellation_floor_vs_corridors_v1]")
    print(f"  repo_root: {repo_root}")
    print(f"  total grid points: {all_grid_n}, kernel size: {kernel_n}")
    print(f"  floor threshold on mech_binding_A0: {floor_thresh:.6f}")
    print(f"  wrote summary: {out_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
