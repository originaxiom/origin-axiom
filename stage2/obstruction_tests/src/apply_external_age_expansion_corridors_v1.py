#!/usr/bin/env python3

import sys
from pathlib import Path

import pandas as pd


TAG = "[stage2_obstruction_external_age_expansion_v1]"


def find_repo_root(start: Path) -> Path:
    current = start
    while True:
        if (current / ".git").is_dir():
            return current
        if current.parent == current:
            return start
        current = current.parent


def main() -> int:
    script_path = Path(__file__).resolve()
    repo_root = find_repo_root(script_path)
    print(f"{TAG} Repo root: {repo_root}")

    input_path = repo_root / "stage2" / "obstruction_tests" / "outputs" / "tables" / "stage2_obstruction_static_frw_kernel_v1.csv"
    output_table_path = repo_root / "stage2" / "obstruction_tests" / "outputs" / "tables" / "stage2_obstruction_external_age_expansion_corridors_v1.csv"
    output_summary_path = repo_root / "stage2" / "obstruction_tests" / "outputs" / "tables" / "stage2_obstruction_external_age_expansion_summary_v1.csv"

    if not input_path.exists():
        print(f"{TAG} ERROR: input table not found: {input_path}", file=sys.stderr)
        return 1

    df = pd.read_csv(input_path)
    n_grid = len(df)
    if n_grid == 0:
        print(f"{TAG} ERROR: input table is empty", file=sys.stderr)
        return 1

    required_cols = ["E_vac", "omega_lambda", "age_Gyr", "has_matter_era", "smooth_H2", "frw_viable"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        print(f"{TAG} ERROR: missing required columns: {missing}", file=sys.stderr)
        return 1

    kernel_mask = (df["has_matter_era"] == 1) & (df["smooth_H2"] == 1) & (df["frw_viable"] == 1)
    n_kernel = int(kernel_mask.sum())
    print(f"{TAG} Grid points: {n_grid}, pre-data kernel size: {n_kernel}")

    if n_kernel == 0:
        print(f"{TAG} WARNING: pre-data kernel is empty; percentiles will be undefined", file=sys.stderr)

    age = df["age_Gyr"]
    df["age_broad_v1"] = (age >= 11.5) & (age <= 15.0)
    df["age_tight_v1"] = (age >= 13.0) & (age <= 14.2)

    evac_kernel = df.loc[kernel_mask, "E_vac"]
    if len(evac_kernel) > 0:
        evac_p05 = float(evac_kernel.quantile(0.05))
        evac_p95 = float(evac_kernel.quantile(0.95))
        evac_p10 = float(evac_kernel.quantile(0.10))
        evac_p90 = float(evac_kernel.quantile(0.90))
    else:
        evac_p05 = evac_p95 = evac_p10 = evac_p90 = float("nan")

    omega = df["omega_lambda"]

    df["expansion_broad_v1"] = (
        (omega >= 0.55)
        & (omega <= 0.85)
        & (df["E_vac"] >= evac_p05)
        & (df["E_vac"] <= evac_p95)
    )

    df["expansion_tight_v1"] = (
        (omega >= 0.62)
        & (omega <= 0.78)
        & (df["E_vac"] >= evac_p10)
        & (df["E_vac"] <= evac_p90)
    )

    df["struct_proxy_basic_v1"] = kernel_mask & df["age_broad_v1"]

    df["struct_proxy_tight_v1"] = (
        kernel_mask
        & df["age_tight_v1"]
        & df["expansion_tight_v1"]
    )

    output_table_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_table_path, index=False)
    print(f"{TAG} Wrote augmented table with external age/expansion flags: {output_table_path}")

    families = {
        "ALL_GRID": pd.Series(True, index=df.index),
        "PRE_DATA_KERNEL": kernel_mask,
        "AGE_BROAD_V1": df["age_broad_v1"],
        "AGE_TIGHT_V1": df["age_tight_v1"],
        "EXPANSION_BROAD_V1": df["expansion_broad_v1"],
        "EXPANSION_TIGHT_V1": df["expansion_tight_v1"],
        "STRUCT_PROXY_BASIC_V1": df["struct_proxy_basic_v1"],
        "STRUCT_PROXY_TIGHT_V1": df["struct_proxy_tight_v1"],
    }

    rows = []
    for name, mask in families.items():
        mask = mask.astype(bool)
        n_points = int(mask.sum())
        frac_of_grid = n_points / n_grid if n_grid > 0 else float("nan")
        n_points_in_kernel = int((mask & kernel_mask).sum())
        frac_of_kernel = n_points_in_kernel / n_kernel if n_kernel > 0 else float("nan")
        rows.append(
            {
                "family_name": name,
                "n_points": n_points,
                "frac_of_grid": frac_of_grid,
                "n_points_in_kernel": n_points_in_kernel,
                "frac_of_kernel": frac_of_kernel,
            }
        )

    summary_df = pd.DataFrame(rows)
    summary_df.to_csv(output_summary_path, index=False)
    print(f"{TAG} Wrote summary: {output_summary_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
