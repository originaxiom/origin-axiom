import sys
from pathlib import Path

import numpy as np
import pandas as pd


def main() -> int:
    here = Path(__file__).resolve()
    repo_root = here.parents[3]

    static_kernel_path = repo_root / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv"
    output_table_path = repo_root / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_lt_corridor_v1.csv"
    summary_path = repo_root / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_lt_corridor_summary_v1.csv"

    print("[stage2_obstruction_external_lt_corridor_v1] Repo root:", repo_root)

    if not static_kernel_path.exists():
        print("[stage2_obstruction_external_lt_corridor_v1] ERROR: static kernel table not found at", static_kernel_path, file=sys.stderr)
        return 1

    df = pd.read_csv(static_kernel_path)
    n_grid = len(df)

    if "in_pre_data_kernel" not in df.columns or "lcdm_like" not in df.columns:
        print("[stage2_obstruction_external_lt_corridor_v1] ERROR: expected columns 'in_pre_data_kernel' and 'lcdm_like' missing", file=sys.stderr)
        return 1

    kernel_mask = df["in_pre_data_kernel"] == 1
    lcdm_mask = df["lcdm_like"] == 1

    n_kernel = int(kernel_mask.sum())
    n_lcdm = int(lcdm_mask.sum())

    print(f"[stage2_obstruction_external_lt_corridor_v1] Grid points: {n_grid}, pre-data kernel size: {n_kernel}, lcdm_like points: {n_lcdm}")

    if n_lcdm == 0:
        print("[stage2_obstruction_external_lt_corridor_v1] WARNING: no lcdm_like points in kernel; cannot derive LCDM-based box.", file=sys.stderr)
        evac_min = df["E_vac"].min()
        evac_max = df["E_vac"].max()
        omega_min = df["omega_lambda"].min()
        omega_max = df["omega_lambda"].max()
    else:
        lcdm_df = df[lcdm_mask]
        evac_min = float(lcdm_df["E_vac"].min())
        evac_max = float(lcdm_df["E_vac"].max())
        omega_min = float(lcdm_df["omega_lambda"].min())
        omega_max = float(lcdm_df["omega_lambda"].max())

    print("[stage2_obstruction_external_lt_corridor_v1] External LT box (v1, LCDM-derived):")
    print(f"  E_vac in [{evac_min:.6e}, {evac_max:.6e}]")
    print(f"  omega_lambda in [{omega_min:.6e}, {omega_max:.6e}]")

    in_external_lt = (
        (df["E_vac"] >= evac_min)
        & (df["E_vac"] <= evac_max)
        & (df["omega_lambda"] >= omega_min)
        & (df["omega_lambda"] <= omega_max)
    )

    df_out = df.copy()
    df_out["external_lt_corridor_v1"] = in_external_lt.astype(int)

    output_table_path.parent.mkdir(parents=True, exist_ok=True)
    df_out.to_csv(output_table_path, index=False)
    print("[stage2_obstruction_external_lt_corridor_v1] Wrote table with external LT corridor flag:", output_table_path)

    families = []

    def add_family(name: str, mask: np.ndarray) -> None:
        n_points = int(mask.sum())
        frac_of_grid = float(n_points / n_grid) if n_grid > 0 else np.nan
        n_points_in_kernel = int((mask & kernel_mask.to_numpy()).sum())
        frac_of_kernel = float(n_points_in_kernel / n_kernel) if n_kernel > 0 else np.nan
        families.append(
            {
                "family_name": name,
                "n_points": n_points,
                "frac_of_grid": frac_of_grid,
                "n_points_in_kernel": n_points_in_kernel,
                "frac_of_kernel": frac_of_kernel,
            }
        )

    all_mask = np.ones(n_grid, dtype=bool)
    add_family("ALL_GRID", all_mask)
    add_family("PRE_DATA_KERNEL", kernel_mask.to_numpy())

    ext_mask = in_external_lt.to_numpy()
    add_family("EXTERNAL_LT_CORRIDOR_V1", ext_mask)
    add_family("KERNEL_AND_EXTERNAL_LT_V1", kernel_mask.to_numpy() & ext_mask)
    add_family("LCDM_AND_EXTERNAL_LT_V1", lcdm_mask.to_numpy() & ext_mask)

    toy_mask = df["in_toy_corridor"] == 1 if "in_toy_corridor" in df.columns else np.zeros(n_grid, dtype=bool)
    add_family("TOY_CORRIDOR_AND_EXTERNAL_LT_V1", toy_mask.to_numpy() & ext_mask)
    add_family("KERNEL_LCDM_TOY_AND_EXTERNAL_LT_V1", kernel_mask.to_numpy() & lcdm_mask.to_numpy() & toy_mask.to_numpy() & ext_mask)

    summary_df = pd.DataFrame(families, columns=["family_name", "n_points", "frac_of_grid", "n_points_in_kernel", "frac_of_kernel"])
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_df.to_csv(summary_path, index=False)
    print("[stage2_obstruction_external_lt_corridor_v1] Wrote summary:", summary_path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
