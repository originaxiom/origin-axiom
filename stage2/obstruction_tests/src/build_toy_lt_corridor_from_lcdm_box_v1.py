import sys
from pathlib import Path

import pandas as pd


def main() -> None:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[3]

    kernel_path = repo_root / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv"
    out_table_path = repo_root / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_toy_lt_corridor_from_lcdm_box_v1.csv"
    summary_path = repo_root / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_toy_lt_corridor_from_lcdm_box_summary_v1.csv"

    print(f"[stage2_obstruction_toy_lt_corridor_from_lcdm_box_v1] Repo root: {repo_root}")
    print(f"[stage2_obstruction_toy_lt_corridor_from_lcdm_box_v1] Input: {kernel_path}")

    if not kernel_path.is_file():
        print(f"[stage2_obstruction_toy_lt_corridor_from_lcdm_box_v1] ERROR: kernel table not found: {kernel_path}", file=sys.stderr)
        raise SystemExit(1)

    df = pd.read_csv(kernel_path)

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
        print(f"[stage2_obstruction_toy_lt_corridor_from_lcdm_box_v1] ERROR: missing required columns: {missing}", file=sys.stderr)
        raise SystemExit(1)

    n_grid = len(df)
    n_kernel = int((df["in_pre_data_kernel"] == 1).sum())
    print(f"[stage2_obstruction_toy_lt_corridor_from_lcdm_box_v1] Grid points: {n_grid}, pre-data kernel size: {n_kernel}")

    lcdm_mask = df["lcdm_like"] == 1
    n_lcdm = int(lcdm_mask.sum())
    if n_lcdm == 0:
        print("[stage2_obstruction_toy_lt_corridor_from_lcdm_box_v1] ERROR: no LCDM-like points found in kernel table", file=sys.stderr)
        raise SystemExit(1)

    lcdm_df = df[lcdm_mask]
    e_min = float(lcdm_df["E_vac"].min())
    e_max = float(lcdm_df["E_vac"].max())
    w_min = float(lcdm_df["omega_lambda"].min())
    w_max = float(lcdm_df["omega_lambda"].max())

    print("[stage2_obstruction_toy_lt_corridor_from_lcdm_box_v1] LCDM-like band box (derived from current snapshot):")
    print(f"  E_vac      in [{e_min:.6e}, {e_max:.6e}]")
    print(f"  omega_lambda in [{w_min:.6e}, {w_max:.6e}]")
    print(f"  LCDM-like points: {n_lcdm}")

    lt_mask = (
        (df["E_vac"] >= e_min)
        & (df["E_vac"] <= e_max)
        & (df["omega_lambda"] >= w_min)
        & (df["omega_lambda"] <= w_max)
    )
    df["lt_corridor_box_from_lcdm"] = lt_mask.astype(int)

    out_table_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_table_path, index=False)
    print(f"[stage2_obstruction_toy_lt_corridor_from_lcdm_box_v1] Wrote table with toy LT-corridor flag: {out_table_path}")

    rows = []
    kernel_mask = df["in_pre_data_kernel"] == 1

    def add_row(name: str, mask: pd.Series) -> None:
        n_points = int(mask.sum())
        frac_grid = float(n_points / n_grid) if n_grid else float("nan")
        n_in_kernel = int((mask & kernel_mask).sum())
        frac_kernel = float(n_in_kernel / n_kernel) if n_kernel else float("nan")
        rows.append(
            {
                "family_name": name,
                "n_points": n_points,
                "frac_of_grid": frac_grid,
                "n_points_in_kernel": n_in_kernel,
                "frac_of_kernel": frac_kernel,
            }
        )

    add_row("ALL_GRID", df["theta"].notna())
    add_row("PRE_DATA_KERNEL", kernel_mask)
    add_row("TOY_LT_BOX_FROM_LCDM", df["lt_corridor_box_from_lcdm"] == 1)
    add_row(
        "KERNEL_AND_TOY_LT_BOX_FROM_LCDM",
        (df["lt_corridor_box_from_lcdm"] == 1) & kernel_mask,
    )
    add_row(
        "LCDM_AND_TOY_LT_BOX_FROM_LCDM",
        (df["lt_corridor_box_from_lcdm"] == 1) & (df["lcdm_like"] == 1),
    )
    add_row(
        "TOY_CORRIDOR_AND_TOY_LT_BOX_FROM_LCDM",
        (df["lt_corridor_box_from_lcdm"] == 1) & (df["in_toy_corridor"] == 1),
    )

    summary_df = pd.DataFrame(rows)
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_df.to_csv(summary_path, index=False)
    print(f"[stage2_obstruction_toy_lt_corridor_from_lcdm_box_v1] Wrote summary: {summary_path}")


if __name__ == "__main__":
    main()
