import sys
from pathlib import Path

import pandas as pd


def main() -> None:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[3]

    kernel_path = repo_root / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv"
    out_table_path = repo_root / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_corridor_v1.csv"
    summary_path = repo_root / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_external_age_corridor_summary_v1.csv"

    print(f"[stage2_obstruction_external_age_corridor_v1] Repo root: {repo_root}")
    print(f"[stage2_obstruction_external_age_corridor_v1] Input: {kernel_path}")

    if not kernel_path.is_file():
        print(f"[stage2_obstruction_external_age_corridor_v1] ERROR: kernel table not found: {kernel_path}", file=sys.stderr)
        raise SystemExit(1)

    df = pd.read_csv(kernel_path)

    required_cols = [
        "theta",
        "age_Gyr",
        "in_pre_data_kernel",
        "lcdm_like",
        "in_toy_corridor",
    ]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        print(f"[stage2_obstruction_external_age_corridor_v1] ERROR: missing required columns: {missing}", file=sys.stderr)
        raise SystemExit(1)

    n_grid = len(df)
    n_kernel = int((df["in_pre_data_kernel"] == 1).sum())
    print(f"[stage2_obstruction_external_age_corridor_v1] Grid points: {n_grid}, pre-data kernel size: {n_kernel}")

    age_min = 10.0
    age_max = 20.0
    print(f"[stage2_obstruction_external_age_corridor_v1] Using toy age corridor band: [{age_min}, {age_max}] Gyr (placeholder values)")

    age_mask = (df["age_Gyr"] >= age_min) & (df["age_Gyr"] <= age_max)
    df["external_age_corridor_v1"] = age_mask.astype(int)

    out_table_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_table_path, index=False)
    print(f"[stage2_obstruction_external_age_corridor_v1] Wrote table with external-age corridor flag: {out_table_path}")

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
    add_row("EXTERNAL_AGE_CORRIDOR_V1", df["external_age_corridor_v1"] == 1)
    add_row(
        "KERNEL_AND_EXTERNAL_AGE_V1",
        (df["external_age_corridor_v1"] == 1) & kernel_mask,
    )
    add_row(
        "LCDM_AND_EXTERNAL_AGE_V1",
        (df["external_age_corridor_v1"] == 1) & (df["lcdm_like"] == 1),
    )
    add_row(
        "TOY_CORRIDOR_AND_EXTERNAL_AGE_V1",
        (df["external_age_corridor_v1"] == 1) & (df["in_toy_corridor"] == 1),
    )
    add_row(
        "KERNEL_LCDM_TOY_AND_EXTERNAL_AGE_V1",
        (df["external_age_corridor_v1"] == 1)
        & kernel_mask
        & (df["lcdm_like"] == 1)
        & (df["in_toy_corridor"] == 1),
    )

    summary_df = pd.DataFrame(rows)
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_df.to_csv(summary_path, index=False)
    print(f"[stage2_obstruction_external_age_corridor_v1] Wrote summary: {summary_path}")


if __name__ == "__main__":
    main()
