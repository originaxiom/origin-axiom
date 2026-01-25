import sys
from pathlib import Path

import numpy as np
import pandas as pd


def main() -> int:
    repo_root = Path.cwd()
    print("[stage2_obstruction_planck_like_corridor_v1] Repo root:", repo_root)

    kernel_path = repo_root / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv"
    if not kernel_path.is_file():
        print("[stage2_obstruction_planck_like_corridor_v1] ERROR: kernel table not found:", kernel_path)
        return 1

    df = pd.read_csv(kernel_path)
    grid_n = len(df)

    # Basic sanity checks on expected columns
    required_cols = [
        "theta",
        "E_vac",
        "omega_lambda",
        "age_Gyr",
        "in_pre_data_kernel",
        "lcdm_like",
        "in_toy_corridor",
    ]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        print("[stage2_obstruction_planck_like_corridor_v1] ERROR: missing columns in kernel table:")
        for c in missing:
            print("   -", c)
        return 1

    # Planck-like toy bands (v1)
    # These are deliberately simple, external-style corridors inspired by Planck ΛCDM:
    #   age_Gyr in [13.75, 13.85]
    #   omega_lambda in [0.68, 0.70]
    age_min = 13.75
    age_max = 13.85
    omL_min = 0.68
    omL_max = 0.70

    print("[stage2_obstruction_planck_like_corridor_v1] Using Planck-like toy bands:")
    print(f"  age_Gyr in [{age_min:.3f}, {age_max:.3f}]")
    print(f"  omega_lambda in [{omL_min:.3f}, {omL_max:.3f}]")

    age = df["age_Gyr"].to_numpy()
    omL = df["omega_lambda"].to_numpy()
    kernel_mask = df["in_pre_data_kernel"].astype(bool).to_numpy()
    lcdm_mask = df["lcdm_like"].astype(bool).to_numpy()
    toy_mask = df["in_toy_corridor"].astype(bool).to_numpy()

    planck_like_mask = (age >= age_min) & (age <= age_max) & (omL >= omL_min) & (omL <= omL_max)

    # Attach flag
    df["in_planck_like_corridor_v1"] = planck_like_mask

    kernel_n = int(kernel_mask.sum())

    # Families for summary
    families = {
        "ALL_GRID": np.ones(grid_n, dtype=bool),
        "PRE_DATA_KERNEL": kernel_mask,
        "PLANCK_LIKE_V1": planck_like_mask,
        "KERNEL_AND_PLANCK_LIKE_V1": kernel_mask & planck_like_mask,
        "LCDM_AND_PLANCK_LIKE_V1": lcdm_mask & planck_like_mask,
        "TOY_CORRIDOR_AND_PLANCK_LIKE_V1": toy_mask & planck_like_mask,
        "KERNEL_LCDM_TOY_AND_PLANCK_LIKE_V1": kernel_mask & lcdm_mask & toy_mask & planck_like_mask,
    }

    rows = []
    for name, mask in families.items():
        n_points = int(mask.sum())
        n_in_kernel = int((mask & kernel_mask).sum())
        frac_grid = float(n_points / grid_n) if grid_n > 0 else float("nan")
        frac_kernel = float(n_in_kernel / kernel_n) if kernel_n > 0 else float("nan")
        rows.append(
            {
                "family_name": name,
                "n_points": n_points,
                "frac_of_grid": frac_grid,
                "n_points_in_kernel": n_in_kernel,
                "frac_of_kernel": frac_kernel,
            }
        )

    summary = pd.DataFrame(rows)

    out_table = repo_root / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_planck_like_corridor_v1.csv"
    out_summary = repo_root / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_planck_like_corridor_summary_v1.csv"

    out_table.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_table, index=False)
    summary.to_csv(out_summary, index=False)

    print("[stage2_obstruction_planck_like_corridor_v1] Grid points:", grid_n)
    print("[stage2_obstruction_planck_like_corridor_v1] Kernel size:", kernel_n)
    print("[stage2_obstruction_planck_like_corridor_v1] Wrote augmented table:", out_table)
    print("[stage2_obstruction_planck_like_corridor_v1] Wrote summary:", out_summary)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
