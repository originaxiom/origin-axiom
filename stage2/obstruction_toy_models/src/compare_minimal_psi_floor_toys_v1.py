from __future__ import annotations

from pathlib import Path
from typing import Dict, List

import pandas as pd


def find_repo_root(start: Path | None = None) -> Path:
    here = start or Path(__file__).resolve()
    for parent in [here] + list(here.parents):
        if (parent / ".git").is_dir():
            return parent
    raise RuntimeError("Could not find repo root (no .git directory found)")


def load_table(path: Path, label: str) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"[compare_minimal_psi_floor_toys_v1] missing table for {label}: {path}")
    df = pd.read_csv(path)
    print(f"[compare_minimal_psi_floor_toys_v1] loaded {label} table:", path, f"(n={len(df)})")
    return df


def summarize_toy(df: pd.DataFrame, label: str) -> Dict[str, float]:
    n_ics = len(df)

    ever_counts = df["ever_on_floor"].value_counts(dropna=False)
    frac_ever = float(ever_counts.get(True, 0)) / float(n_ics)

    def stats(col: str) -> Dict[str, float]:
        s = df[col]
        return {
            f"{col}_min": float(s.min()),
            f"{col}_max": float(s.max()),
            f"{col}_mean": float(s.mean()),
        }

    row: Dict[str, float] = {
        "model": label,
        "n_ics": int(n_ics),
        "frac_ever_on_floor": frac_ever,
    }

    for col in ["r0", "r_min", "r_max", "r_final", "floor_active_fraction"]:
        row.update(stats(col))

    return row


def main() -> int:
    repo_root = find_repo_root()
    base = repo_root / "stage2/obstruction_toy_models/outputs/tables"

    no_drive_path = base / "stage2_minimal_psi_floor_toy_trajectories_v1.csv"
    drive_path = base / "stage2_minimal_psi_floor_toy_with_drive_trajectories_v1.csv"

    df_no = load_table(no_drive_path, "no_drive")
    df_drive = load_table(drive_path, "with_drive")

    rows: List[Dict[str, float]] = [
        summarize_toy(df_no, "no_drive"),
        summarize_toy(df_drive, "with_drive"),
    ]

    summary = pd.DataFrame(rows)

    out_path = base / "stage2_minimal_psi_floor_toys_comparison_v1.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(out_path, index=False)

    print("[compare_minimal_psi_floor_toys_v1] wrote summary:", out_path)
    print(summary.to_string(index=False))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
