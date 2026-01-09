#!/usr/bin/env python
from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List

import numpy as np
import pandas as pd

TAG = "[stage2_frw_data_probe_rung2]"


@dataclass
class ProbeViabilityCross:
    probe: str
    n_tt: int  # frw_viable=True, probe=True
    n_tf: int  # frw_viable=True, probe=False
    n_ft: int  # frw_viable=False, probe=True
    n_ff: int  # frw_viable=False, probe=False
    frac_tt: float
    frac_tf: float
    frac_ft: float
    frac_ff: float
    frac_probe_true: float
    frac_viable_true: float


def find_repo_root(start: Path | None = None) -> Path:
    here = (start or Path(__file__)).resolve()
    for p in [here] + list(here.parents):
        if (p / ".git").is_dir():
            return p
    raise RuntimeError(f"{TAG} Could not find repo root (.git not found)")


def is_bool_like(s: pd.Series) -> bool:
    if s.dtype == bool:
        return True
    vals = pd.unique(s.dropna())
    if len(vals) == 0:
        return False
    try:
        arr = np.asarray(vals, dtype=float)
    except Exception:
        return False
    return set(np.unique(arr)).issubset({0.0, 1.0})


def assert_theta_align(theta_a: pd.Series, theta_b: pd.Series, label_b: str, tol: float = 1e-8) -> None:
    if len(theta_a) != len(theta_b):
        raise ValueError(
            f"{TAG} Theta length mismatch vs {label_b}: "
            f"{len(theta_a)} vs {len(theta_b)}"
        )
    diff = np.max(np.abs(theta_a.to_numpy() - theta_b.to_numpy()))
    if diff > tol:
        raise ValueError(
            f"{TAG} Theta mismatch vs {label_b}: max |Δθ| ≈ {diff:.3e} > tol={tol:.1e}"
        )
    print(f"{TAG} Theta alignment OK vs {label_b} (max |Δθ| ≈ {diff:.3e})")


def main() -> None:
    repo_root = find_repo_root()
    print(f"{TAG} Repo root: {repo_root}")

    data_path = (
        repo_root
        / "phase4"
        / "outputs"
        / "tables"
        / "phase4_F1_frw_data_probe_mask.csv"
    )
    viab_path = (
        repo_root
        / "phase4"
        / "outputs"
        / "tables"
        / "phase4_F1_frw_viability_mask.csv"
    )

    if not data_path.is_file():
        raise FileNotFoundError(f"{TAG} Data probe mask not found at {data_path}")
    if not viab_path.is_file():
        raise FileNotFoundError(f"{TAG} Viability mask not found at {viab_path}")

    df_data = pd.read_csv(data_path)
    df_viab = pd.read_csv(viab_path)

    print(f"{TAG} Loaded data probes: {data_path} shape={df_data.shape}")
    print(f"{TAG} Loaded viability mask: {viab_path} shape={df_viab.shape}")

    # Assume both have theta or theta_index columns used earlier in Stage 4.
    theta_cols = [c for c in df_data.columns if c.lower().startswith("theta")]
    if not theta_cols:
        raise RuntimeError(f"{TAG} No theta* column found in data probes")
    theta_col = theta_cols[0]

    theta_data = df_data[theta_col]
    theta_viab = df_viab[theta_col]
    assert_theta_align(theta_data, theta_viab, "viability_mask", tol=1e-8)

    if "frw_viable" not in df_viab.columns:
        raise RuntimeError(f"{TAG} Column 'frw_viable' not found in viability mask")

    frw_viable = df_viab["frw_viable"]
    if frw_viable.dtype != bool:
        frw_viable = (frw_viable != 0)

    mask_viable = frw_viable.to_numpy()
    n = len(mask_viable)

    results: List[ProbeViabilityCross] = []

    for col in df_data.columns:
        if col == theta_col:
            continue
        if col == "frw_data_ok":
            # We already know this is empty in the current snapshot; skip
            continue

        s = df_data[col]
        if not is_bool_like(s):
            continue

        print(f"{TAG} Analyzing probe column: {col}")
        if s.dtype == bool:
            probe = s.fillna(False).to_numpy()
        else:
            probe = (s != 0).fillna(False).to_numpy()

        n_tt = int((mask_viable & probe).sum())
        n_tf = int((mask_viable & ~probe).sum())
        n_ft = int((~mask_viable & probe).sum())
        n_ff = int((~mask_viable & ~probe).sum())

        frac_tt = n_tt / n if n > 0 else 0.0
        frac_tf = n_tf / n if n > 0 else 0.0
        frac_ft = n_ft / n if n > 0 else 0.0
        frac_ff = n_ff / n if n > 0 else 0.0

        frac_probe_true = (n_tt + n_ft) / n if n > 0 else 0.0
        frac_viable_true = (n_tt + n_tf) / n if n > 0 else 0.0

        results.append(
            ProbeViabilityCross(
                probe=col,
                n_tt=n_tt,
                n_tf=n_tf,
                n_ft=n_ft,
                n_ff=n_ff,
                frac_tt=frac_tt,
                frac_tf=frac_tf,
                frac_ft=frac_ft,
                frac_ff=frac_ff,
                frac_probe_true=frac_probe_true,
                frac_viable_true=frac_viable_true,
            )
        )
        print(
            f"{TAG} {col}: n_tt={n_tt}, n_tf={n_tf}, n_ft={n_ft}, n_ff={n_ff}, "
            f"frac_probe_true={frac_probe_true:.5f}, "
            f"frac_viable_true={frac_viable_true:.5f}"
        )

    out_dir = (
        repo_root
        / "stage2"
        / "frw_data_probe_analysis"
        / "outputs"
        / "tables"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / "stage2_frw_data_probe_rung2_viability_cross_v1.csv"

    df_out = pd.DataFrame([asdict(r) for r in results])
    df_out.to_csv(out_csv, index=False)

    print(
        f"{TAG} Wrote viability cross table: {out_csv} "
        f"({out_csv.stat().st_size} bytes; rows={len(df_out)})"
    )


if __name__ == "__main__":
    main()
