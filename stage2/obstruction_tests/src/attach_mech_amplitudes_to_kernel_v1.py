from pathlib import Path
import sys

import pandas as pd


def find_repo_root(start: Path) -> Path:
    for p in (start,) + tuple(start.parents):
        git_dir = p / ".git"
        if git_dir.is_dir() or git_dir.is_file():
            return p
    return start


def main() -> int:
    here = Path(__file__).resolve()
    repo_root = find_repo_root(here)
    print(f"[stage2_obstruction_kernel_with_mech_v1] Repo root: {repo_root}")

    kernel_path = repo_root / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_static_frw_kernel_v1.csv"
    joint_path = repo_root / "stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv"

    if not kernel_path.is_file():
        print(f"[stage2_obstruction_kernel_with_mech_v1] ERROR: kernel table not found: {kernel_path}")
        return 1

    if not joint_path.is_file():
        print(f"[stage2_obstruction_kernel_with_mech_v1] ERROR: joint mech–FRW table not found: {joint_path}")
        return 1

    print(f"[stage2_obstruction_kernel_with_mech_v1] Kernel table: {kernel_path}")
    print(f"[stage2_obstruction_kernel_with_mech_v1] Joint mech–FRW table: {joint_path}")

    df_kernel = pd.read_csv(kernel_path)
    df_joint = pd.read_csv(joint_path)

    if "theta" not in df_kernel.columns:
        print("[stage2_obstruction_kernel_with_mech_v1] ERROR: 'theta' column missing in kernel table")
        return 1

    if "theta" not in df_joint.columns:
        print("[stage2_obstruction_kernel_with_mech_v1] ERROR: 'theta' column missing in joint mech–FRW table")
        return 1

    print(f"[stage2_obstruction_kernel_with_mech_v1] Kernel shape: {df_kernel.shape}")
    print(f"[stage2_obstruction_kernel_with_mech_v1] Joint mech–FRW shape: {df_joint.shape}")

    amp_cols = [c for c in df_joint.columns if c.startswith("mech_baseline_") or c.startswith("mech_binding_")]
    if not amp_cols:
        print("[stage2_obstruction_kernel_with_mech_v1] WARNING: no mech amplitude columns found with prefixes 'mech_baseline_' or 'mech_binding_'.")
    else:
        print(f"[stage2_obstruction_kernel_with_mech_v1] Mech amplitude columns in joint table: {amp_cols}")

    use_index_alignment = False

    if len(df_kernel) == len(df_joint):
        df_kernel_sorted = df_kernel.sort_values("theta").reset_index(drop=True)
        df_joint_sorted = df_joint.sort_values("theta").reset_index(drop=True)
        diff = (df_kernel_sorted["theta"] - df_joint_sorted["theta"]).abs()
        max_diff = diff.max()
        print(f"[stage2_obstruction_kernel_with_mech_v1] Max |theta_kernel - theta_joint| after sorting: {max_diff:.3e}")
        tol = 1e-10
        if max_diff <= tol:
            use_index_alignment = True
            print(f"[stage2_obstruction_kernel_with_mech_v1] Using index-aligned attach with tolerance {tol}.")
            df_kernel = df_kernel_sorted
            df_joint = df_joint_sorted
        else:
            print("[stage2_obstruction_kernel_with_mech_v1] Index alignment skipped: max theta mismatch above tolerance, falling back to merge.")

    if use_index_alignment:
        df_out = df_kernel.copy()
        for col in amp_cols:
            df_out[col] = df_joint[col].values
        print(f"[stage2_obstruction_kernel_with_mech_v1] Output shape (index-aligned): {df_out.shape}")
    else:
        merged = pd.merge(df_kernel, df_joint[["theta"] + amp_cols], on="theta", how="inner")
        print(f"[stage2_obstruction_kernel_with_mech_v1] Output shape (inner merge): {merged.shape}")
        df_out = merged

    out_path = repo_root / "stage2/obstruction_tests/outputs/tables/stage2_obstruction_kernel_with_mech_v1.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df_out.to_csv(out_path, index=False)
    print(f"[stage2_obstruction_kernel_with_mech_v1] Wrote: {out_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
