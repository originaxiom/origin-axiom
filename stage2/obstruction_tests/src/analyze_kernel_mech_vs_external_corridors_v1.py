from __future__ import annotations

from pathlib import Path
from typing import Dict, List

import pandas as pd


def find_repo_root(start: Path | None = None) -> Path:
    """Walk upwards until we find a .git directory."""
    here = start or Path(__file__).resolve()
    for parent in [here] + list(here.parents):
        if (parent / ".git").is_dir():
            return parent
    raise RuntimeError("Could not find repo root (no .git directory found).")


def safe_read_csv(path: Path, required: bool = True) -> pd.DataFrame:
    if not path.exists():
        msg = f"[stage2_obstruction_mech_vs_external_corridors_v1] ERROR: missing input {path}"
        if required:
            print(msg)
            raise SystemExit(1)
        else:
            print(msg + " (optional, continuing)")
            return pd.DataFrame()
    return pd.read_csv(path)


def main() -> int:
    repo_root = find_repo_root()
    print(f"[stage2_obstruction_mech_vs_external_corridors_v1] Repo root: {repo_root}")

    base_path = repo_root / "stage2/obstruction_tests/outputs/tables"

    kernel_path = base_path / "stage2_obstruction_kernel_with_mech_v1.csv"
    age2_path = base_path / "stage2_obstruction_external_age_corridor_v2.csv"
    lt_path = base_path / "stage2_obstruction_external_lt_corridor_v1.csv"
    toy_lt_path = base_path / "stage2_obstruction_toy_lt_corridor_from_lcdm_box_v1.csv"
    ageexp_path = base_path / "stage2_obstruction_external_age_expansion_corridors_v1.csv"

    df_kernel = safe_read_csv(kernel_path)
    df_age2 = safe_read_csv(age2_path)[["theta", "external_age_corridor_v2"]]
    df_lt = safe_read_csv(lt_path)[["theta", "external_lt_corridor_v1"]]
    df_toy = safe_read_csv(toy_lt_path)[["theta", "lt_corridor_box_from_lcdm"]]
    df_ageexp = safe_read_csv(ageexp_path)[
        [
            "theta",
            "age_broad_v1",
            "age_tight_v1",
            "expansion_broad_v1",
            "expansion_tight_v1",
            "struct_proxy_basic_v1",
            "struct_proxy_tight_v1",
        ]
    ]

    # Merge all flags onto the kernel-with-mech table.
    df = (
        df_kernel.merge(df_age2, on="theta", how="left")
        .merge(df_lt, on="theta", how="left")
        .merge(df_toy, on="theta", how="left")
        .merge(df_ageexp, on="theta", how="left")
    )

    n_grid = len(df)
    kernel_flag = df["in_pre_data_kernel"].astype(bool)
    n_kernel = int(kernel_flag.sum())

    print(
        "[stage2_obstruction_mech_vs_external_corridors_v1] "
        f"Grid points: {n_grid}, kernel size: {n_kernel}"
    )

    amp_cols: List[str] = [
        "mech_baseline_A0",
        "mech_baseline_A_floor",
        "mech_baseline_bound",
        "mech_binding_A0",
        "mech_binding_A",
        "mech_binding_bound",
    ]

    missing_amps = [c for c in amp_cols if c not in df.columns]
    if missing_amps:
        print(
            "[stage2_obstruction_mech_vs_external_corridors_v1] "
            f"ERROR: missing amplitude columns: {missing_amps}"
        )
        return 1

    families: Dict[str, pd.Series] = {
        "ALL_GRID": pd.Series([True] * n_grid, index=df.index),
        "PRE_DATA_KERNEL": kernel_flag,
        # The 40-point joint subset from earlier rungs:
        # kernel AND LCDM-like AND toy FRW corridor AND external age v2.
        "KERNEL_LCDM_TOY_AND_EXTERNAL_AGE_V2": (
            kernel_flag
            & df["lcdm_like"].astype(bool)
            & df["in_toy_corridor"].astype(bool)
            & df["external_age_corridor_v2"].astype(bool)
        ),
        # Kernel points that survive the external age v2 band,
        # irrespective of LCDM/toy flags.
        "KERNEL_AND_EXTERNAL_AGE_V2": (
            kernel_flag & df["external_age_corridor_v2"].astype(bool)
        ),
        # A deliberately tight "age + expansion + structure" subset
        # inside the kernel.
        "KERNEL_AGE_TIGHT_EXP_STRUCT_TIGHT": (
            kernel_flag
            & df["age_tight_v1"].astype(bool)
            & df["expansion_tight_v1"].astype(bool)
            & df["struct_proxy_tight_v1"].astype(bool)
        ),
    }

    rows = []
    for fam_name, mask in families.items():
        mask = mask.fillna(False)
        n = int(mask.sum())

        row: Dict[str, float | int | str] = {
            "family_name": fam_name,
            "n_points": n,
            "frac_of_grid": float(n) / float(n_grid) if n_grid > 0 else 0.0,
            "n_points_in_kernel": int((kernel_flag & mask).sum()),
            "frac_of_kernel": (
                float((kernel_flag & mask).sum()) / float(n_kernel)
                if n_kernel > 0
                else 0.0
            ),
        }

        if n == 0:
            for col in amp_cols:
                row[f"{col}_min"] = float("nan")
                row[f"{col}_max"] = float("nan")
                row[f"{col}_mean"] = float("nan")
        else:
            sub = df.loc[mask, amp_cols]
            for col in amp_cols:
                s = sub[col]
                row[f"{col}_min"] = float(s.min())
                row[f"{col}_max"] = float(s.max())
                row[f"{col}_mean"] = float(s.mean())

        rows.append(row)

    summary = pd.DataFrame(rows)
    out_path = base_path / "stage2_obstruction_kernel_mech_vs_external_corridors_summary_v1.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(out_path, index=False)
    print(
        "[stage2_obstruction_mech_vs_external_corridors_v1] "
        f"Wrote summary: {out_path}"
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
