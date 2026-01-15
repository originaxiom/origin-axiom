#!/usr/bin/env python3
"""
Stage2: external host omega-naming scan (v1)

Purpose:
    - Scan key Stage 2 external-host CSV endpoints and report which
      omega-like columns they expose:
        * omega_lambda          (ambiguous / legacy)
        * omega_lambda_repo     (toy / Phase 4 side)
        * Omega_lambda          (host side)
        * Omega_tot, Omega_m    (for context)

    - Output a single CSV:
        stage2/external_cosmo_host/outputs/tables/
            stage2_external_host_omega_naming_scan_v1.csv

This does NOT enforce anything; it is a diagnostic we can inspect
whenever we touch external hosts, to avoid repeating the same error.
"""

import sys
from pathlib import Path

import pandas as pd


def main() -> None:
    repo_root = Path(__file__).resolve().parents[3]
    print("[external_host_omega_scan] Repo root:", repo_root)

    # List of CSVs we want to inspect.
    # We only include files that actually live in the repo right now.
    csv_relpaths = [
        # External FRW host side
        "stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv",
        "stage2/external_frw_host/outputs/tables/stage2_external_frw_background_bridge_v1.csv",
        "stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_mask_v1.csv",
        "stage2/external_frw_host/outputs/tables/stage2_external_frw_host_age_anchor_summary_v1.csv",
        "stage2/external_frw_host/outputs/tables/stage2_external_frw_rung4_age_window_summary_v1.csv",

        # External cosmo host side
        "stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_params_grid_v1.csv",
        "stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_background_grid_v1.csv",
        "stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_rung3_age_contrast_v1.csv",
        "stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_anchor_mask_v1.csv",
        "stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_flat_subset_mask_v1.csv",
        "stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_anchor_corridor_kernel_v1.csv",
        "stage2/external_cosmo_host/outputs/tables/stage2_external_cosmo_host_age_window_sensitivity_v1.csv",
        "stage2/external_cosmo_host/outputs/tables/stage2_external_host_kernel_comparison_v1.csv",
    ]

    records = []
    for rel in csv_relpaths:
        path = repo_root / rel
        if not path.exists():
            print(f"[external_host_omega_scan] SKIP (missing): {rel}")
            continue

        try:
            df_head = pd.read_csv(path, nrows=0)
        except Exception as e:  # pragma: no cover
            print(f"[external_host_omega_scan] ERROR reading {rel}: {e}", file=sys.stderr)
            continue

        cols = list(df_head.columns)
        colset = set(cols)

        has_omega_lambda = "omega_lambda" in colset
        has_omega_lambda_repo = "omega_lambda_repo" in colset
        has_Omega_lambda = "Omega_lambda" in colset
        has_Omega_m = "Omega_m" in colset
        has_Omega_tot = "Omega_tot" in colset

        print(
            f"[external_host_omega_scan] {rel}: "
            f"omega_lambda={has_omega_lambda}, "
            f"omega_lambda_repo={has_omega_lambda_repo}, "
            f"Omega_lambda={has_Omega_lambda}, "
            f"Omega_m={has_Omega_m}, "
            f"Omega_tot={has_Omega_tot}"
        )

        records.append(
            {
                "relpath": rel,
                "columns": ",".join(cols),
                "has_omega_lambda": has_omega_lambda,
                "has_omega_lambda_repo": has_omega_lambda_repo,
                "has_Omega_lambda": has_Omega_lambda,
                "has_Omega_m": has_Omega_m,
                "has_Omega_tot": has_Omega_tot,
            }
        )

    if not records:
        print("[external_host_omega_scan] WARNING: no CSVs found from the list.")
        return

    out_dir = (
        repo_root
        / "stage2"
        / "external_cosmo_host"
        / "outputs"
        / "tables"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "stage2_external_host_omega_naming_scan_v1.csv"

    out_df = pd.DataFrame.from_records(
        records,
        columns=[
            "relpath",
            "columns",
            "has_omega_lambda",
            "has_omega_lambda_repo",
            "has_Omega_lambda",
            "has_Omega_m",
            "has_Omega_tot",
        ],
    )
    out_df.to_csv(out_path, index=False)
    print("[external_host_omega_scan] Scan written:", out_path)


if __name__ == "__main__":
    main()
