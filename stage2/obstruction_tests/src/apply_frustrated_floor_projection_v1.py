from __future__ import annotations

from pathlib import Path
from typing import List

import pandas as pd


def find_repo_root(start: Path | None = None) -> Path:
    here = start or Path(__file__).resolve()
    for parent in [here] + list(here.parents):
        if (parent / ".git").is_dir():
            return parent
    raise RuntimeError("Could not find repo root")


def safe_read_csv(path: Path, required: bool = True) -> pd.DataFrame:
    if not path.exists():
        msg = f"[apply_frustrated_floor_projection_v1] missing input: {path}"
        if required:
            print(msg)
            raise SystemExit(1)
        print(msg + " (optional, continuing with empty frame)")
        return pd.DataFrame()
    return pd.read_csv(path)


def main() -> int:
    repo_root = find_repo_root()
    print("[apply_frustrated_floor_projection_v1]")
    print(f"  repo_root: {repo_root}")

    base = repo_root / "stage2/obstruction_tests/outputs/tables"
    kernel_path = base / "stage2_obstruction_kernel_with_mech_v1.csv"
    ageexp_path = base / "stage2_obstruction_external_age_expansion_corridors_v1.csv"

    df_kernel = safe_read_csv(kernel_path, required=True)
    df_ageexp = safe_read_csv(ageexp_path, required=False)

    if df_kernel.empty:
        print("[apply_frustrated_floor_projection_v1] kernel_with_mech table is empty; nothing to do.")
        return 0

    if "theta" not in df_kernel.columns:
        print("[apply_frustrated_floor_projection_v1] kernel_with_mech table has no 'theta' column")
        return 1

    if not df_ageexp.empty and "theta" in df_ageexp.columns:
        wanted_cols: List[str] = [
            "theta",
            "age_tight_v1",
            "expansion_tight_v1",
            "struct_proxy_tight_v1",
        ]
        cols = [c for c in wanted_cols if c in df_ageexp.columns]
        df_kernel = df_kernel.merge(df_ageexp[cols], on="theta", how="left")
    else:
        print("[apply_frustrated_floor_projection_v1] age/expansion table missing or unusable; corridor flags will default to False.")

    required_cols = ["in_pre_data_kernel", "mech_binding_A0"]
    missing_required = [c for c in required_cols if c not in df_kernel.columns]
    if missing_required:
        print("[apply_frustrated_floor_projection_v1] missing required columns in kernel_with_mech table:")
        for c in missing_required:
            print(f"    - {c}")
        return 1

    for flag in ["age_tight_v1", "expansion_tight_v1", "struct_proxy_tight_v1"]:
        if flag not in df_kernel.columns:
            df_kernel[flag] = False

    kernel_flag = df_kernel["in_pre_data_kernel"].astype(bool)
    amp = df_kernel["mech_binding_A0"].astype(float)

    floor_thresh = 0.045
    in_floor = amp >= floor_thresh

    in_tight_corr = (
        df_kernel["age_tight_v1"].astype(bool)
        & df_kernel["expansion_tight_v1"].astype(bool)
        & df_kernel["struct_proxy_tight_v1"].astype(bool)
    )

    df_out = df_kernel.copy()
    df_out["in_frustrated_floor_core_v1"] = kernel_flag & in_floor & in_tight_corr

    out_path = base / "stage2_obstruction_kernel_with_frustrated_floor_v1.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df_out.to_csv(out_path, index=False)

    n_core = int(df_out["in_frustrated_floor_core_v1"].sum())
    kernel_n = int(kernel_flag.sum())
    print(f"[apply_frustrated_floor_projection_v1] wrote: {out_path}")
    print(f"[apply_frustrated_floor_projection_v1] core size: {n_core} out of {kernel_n} kernel points")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
