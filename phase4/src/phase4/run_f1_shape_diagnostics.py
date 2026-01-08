#!/usr/bin/env python3
"""
Phase 4 F1 shape diagnostics (Rung 4).

This script:
  - rebuilds the F1 vacuum-energy-like curve E_vac(theta);
  - computes basic shape descriptors (min/max, mean, std);
  - defines a *toy, non-binding* theta-corridor as the set of thetas
    with E_vac(theta) <= E_vac_min + 1 * sigma;
  - writes summary diagnostics to a JSON file; and
  - writes a per-theta CSV mask for future figures / corridor work.

Nothing here defines a canonical theta_* or a binding Phase 4 filter.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path
from typing import Any, Dict, Tuple

import numpy as np

# ----------------------------------------------------------------------
# Ensure the phase4 *package* (phase4/src/phase4) is on sys.path
# ----------------------------------------------------------------------
THIS_FILE = Path(__file__).resolve()
PHASE4_SRC = THIS_FILE.parents[1]  # .../phase4/src
REPO_ROOT = THIS_FILE.parents[3]   # .../origin-axiom

if str(PHASE4_SRC) not in sys.path:
    sys.path.insert(0, str(PHASE4_SRC))

from phase4 import (  # type: ignore[import]
    build_default_f1_config,
    compute_f1_vacuum_curve,
)


def repo_root() -> Path:
    return REPO_ROOT


def compute_shape_diagnostics() -> Tuple[Dict[str, Any], np.ndarray, np.ndarray, np.ndarray]:
    cfg = build_default_f1_config()
    thetas, evac, meta = compute_f1_vacuum_curve(cfg)

    thetas = np.asarray(thetas, dtype=float)
    evac = np.asarray(evac, dtype=float)

    if thetas.shape != evac.shape:
        raise RuntimeError("theta and E_vac arrays have mismatched shapes")

    idx_min = int(np.argmin(evac))
    idx_max = int(np.argmax(evac))

    theta_min = float(thetas[idx_min])
    theta_max = float(thetas[idx_max])
    ev_min = float(evac[idx_min])
    ev_max = float(evac[idx_max])
    ev_mean = float(np.mean(evac))
    ev_std = float(np.std(evac))

    # Toy, non-binding corridor definition:
    #   E_vac(theta) <= E_vac_min + 1 * sigma
    k_sigma = 1.0
    threshold = ev_min + k_sigma * ev_std
    mask = evac <= threshold

    frac_corridor = float(mask.mean())
    if mask.any():
        theta_corr_min = float(thetas[mask].min())
        theta_corr_max = float(thetas[mask].max())
    else:
        theta_corr_min = None
        theta_corr_max = None

    diagnostics: Dict[str, Any] = {
        "mapping_family": meta.get("mapping_family", "F1"),
        "mapping_name": meta.get("mapping_name", ""),
        "k_sigma": float(k_sigma),
        "corridor_definition": (
            "E_vac(theta) <= E_vac_min + k_sigma * sigma "
            "(k_sigma = 1.0; toy, non-binding diagnostic)"
        ),
        "theta_min_global": theta_min,
        "theta_max_global": theta_max,
        "E_vac_min": ev_min,
        "E_vac_max": ev_max,
        "E_vac_mean": ev_mean,
        "E_vac_std": ev_std,
        "corridor_fraction": frac_corridor,
        "corridor_theta_min": theta_corr_min,
        "corridor_theta_max": theta_corr_max,
        "baseline_meta": meta,
    }

    return diagnostics, thetas, evac, mask


def main() -> None:
    root = repo_root()
    out_dir = root / "phase4" / "outputs" / "tables"
    out_dir.mkdir(parents=True, exist_ok=True)

    diag_path = out_dir / "phase4_F1_shape_diagnostics.json"
    mask_csv_path = out_dir / "phase4_F1_shape_mask.csv"

    diagnostics, thetas, evac, mask = compute_shape_diagnostics()

    # Write JSON diagnostics
    with diag_path.open("w", encoding="utf-8") as f:
        json.dump(diagnostics, f, indent=2, sort_keys=True)

    # Per-theta CSV mask for reproducibility / figures
    with mask_csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["theta", "E_vac", "in_toy_corridor"])
        for th, ev, inside in zip(thetas, evac, mask):
            writer.writerow([float(th), float(ev), int(bool(inside))])

    print("[F1_shape] Wrote diagnostics to", diag_path)
    print("[F1_shape] Wrote per-theta mask CSV to", mask_csv_path)
    print("[F1_shape] Summary:")
    for k, v in diagnostics.items():
        if k == "baseline_meta":
            continue
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
