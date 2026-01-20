import sys
from pathlib import Path

import numpy as np
import pandas as pd


def main() -> int:
    here = Path(__file__).resolve()
    repo_root = here.parents[3]

    static_kernel_path = repo_root / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv"
    output_table_path = repo_root / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_corridor_v2.csv"
    summary_path = repo_root / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_corridor_summary_v2.csv"

    print("[stage2_obstruction_external_age_corridor_v2] Repo root:", repo_root)

    if not static_kernel_path.exists():
        print("[stage2_obstruction_external_age_corridor_v2] ERROR: static kernel table not found at", static_kernel_path, file=sys.stderr)
        return 1

    df = pd.read_csv(static_kernel_path)
    n_grid = len(df)

    required_cols = ["age_Gyr", "in_pre_data_kernel"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        print("[stage2_obstruction_external_age_corridor_v2] ERROR: missing required columns:", ", ".join(missing), file=sys.stderr)
        return 1

    kernel_mask = df["in_pre_data_kernel"] == 1
    n_kernel = int(kernel_mask.sum())

    lcdm_mask = df["lcdm_like"] == 1 if "lcdm_like" in df.columns else np.zeros(n_grid, dtype=bool)
    toy_mask = df["in_toy_corridor"] == 1 if "in_toy_corridor" in df.columns else np.zeros(n_grid, dtype=bool)

    print(f"[stage2_obstruction_external_age_corridor_v2] Grid points: {n_grid}, pre-data kernel size: {n_kernel}")

    age_min = 12.0
    age_max = 15.0
    print(f"[stage2_obstruction_external_age_corridor_v2] Using external-style age band: [{age_min:.2f}, {age_max:.2f}] Gyr (toy v2)")

    ages = df["age_Gyr"].to_numpy()
    in_external_age = (ages >= age_min) & (ages <= age_max)

    df_out = df.copy()
    df_out["external_age_corridor_v2"] = in_external_age.astype(int)

    output_table_path.parent.mkdir(parents=True, exist_ok=True)
    df_out.to_csv(output_table_path, index=False)
    print("[stage2_obstruction_external_age_corridor_v2] Wrote table with external age corridor flag:", output_table_path)

    families = []

    def add_family(name: str, mask: np.ndarray) -> None:
        n_points = int(mask.sum())
        frac_of_grid = float(n_points / n_grid) if n_grid > 0 else float("nan")
        n_points_in_kernel = int((mask & kernel_mask.to_numpy()).sum())
        frac_of_kernel = float(n_points_in_kernel / n_kernel) if n_kernel > 0 else float("nan")
        families.append(
            {
                "family_name": name,
                "n_points": n_points,
                "frac_of_grid": frac_of_grid,
                "n_points_in_kernel": frac_of_kernel * n_kernel if n_kernel == 0 else n_points_in_kernel,
                "frac_of_kernel": frac_of_kernel,
            }
        )

    all_mask = np.ones(n_grid, dtype=bool)
    add_family("ALL_GRID", all_mask)
    add_family("PRE_DATA_KERNEL", kernel_mask.to_numpy())

    ext_age_mask = in_external_age
    add_family("EXTERNAL_AGE_CORRIDOR_V2", ext_age_mask)
    add_family("KERNEL_AND_EXTERNAL_AGE_V2", kernel_mask.to_numpy() & ext_age_mask)
    add_family("LCDM_AND_EXTERNAL_AGE_V2", lcdm_mask & ext_age_mask)
    add_family("TOY_CORRIDOR_AND_EXTERNAL_AGE_V2", toy_mask & ext_age_mask)
    add_family("KERNEL_LCDM_TOY_AND_EXTERNAL_AGE_V2", kernel_mask.to_numpy() & lcdm_mask & toy_mask & ext_age_mask)

    summary_df = pd.DataFrame(families, columns=["family_name", "n_points", "frac_of_grid", "n_points_in_kernel", "frac_of_kernel"])
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_df.to_csv(summary_path, index=False)
    print("[stage2_obstruction_external_age_corridor_v2] Wrote summary:", summary_path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
