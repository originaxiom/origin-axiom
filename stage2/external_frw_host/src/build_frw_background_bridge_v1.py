"""
Stage 2: FRW background bridge (toy ↔ host ages)

This script builds a small, canonical FRW background table that carries both:
- the Phase 4 toy FRW age (renamed to `age_Gyr_toy`), and
- the external host FRW age (`age_Gyr_host`),

together with the key background columns on the shared θ-grid.

It is intentionally minimal: it does not recompute anything, it just selects and
renames columns from the existing host cross-check table.
"""

from pathlib import Path
import pandas as pd


def main() -> None:
    # Resolve repo root from this file location.
    repo_root = Path(__file__).resolve().parents[3]

    host_table = repo_root / "stage2/external_frw_host/outputs/tables/stage2_external_frw_rung1_age_crosscheck_v1.csv"
    out_table = repo_root / "stage2/external_frw_host/outputs/tables/stage2_external_frw_background_bridge_v1.csv"

    if not host_table.exists():
        raise FileNotFoundError(f"Host cross-check table not found: {host_table}")

    df = pd.read_csv(host_table)

    required_cols = [
        "theta_index",
        "theta",
        "omega_lambda",
        "age_Gyr",       # toy FRW age (Phase 4)
        "age_Gyr_host",  # external host age
        "frw_viable",
    ]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise RuntimeError(f"Missing required columns in host table: {missing}")

    # Select and rename for clarity.
    bridge = df[required_cols].copy()
    bridge = bridge.rename(columns={"age_Gyr": "age_Gyr_toy"})

    out_table.parent.mkdir(parents=True, exist_ok=True)
    bridge.to_csv(out_table, index=False)

    n_total = len(bridge)
    n_viable = int(bridge["frw_viable"].sum())

    print("[frw_background_bridge_v1]")
    print(f"  Repo root: {repo_root}")
    print(f"  Input host table: {host_table}")
    print(f"  Output bridge table: {out_table}")
    print(f"  Rows: {n_total}, FRW-viable rows: {n_viable}")


if __name__ == "__main__":
    main()
