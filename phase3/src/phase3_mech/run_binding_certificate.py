#!/usr/bin/env python
"""
Phase 3 mechanism: binding certificate diagnostics.

This script reuses the baseline toy vacuum configuration and the
quantile-based floor choice from the baseline scan to demonstrate
that the non-cancellation floor changes the observable in a
diagnostically relevant way.

It computes summary statistics for the unconstrained amplitude
A_0(theta) and the floor-enforced amplitude A(theta), as well as
simple distance measures between their distributions.
"""

import csv
import json
import pathlib
import sys

import numpy as np

# Resolve the repository root from this file location:
#   .../origin-axiom/phase3/src/phase3_mech/run_binding_certificate.py
# parents: [phase3_mech, src, phase3, origin-axiom, ...]
REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
PHASE3 = REPO_ROOT / "phase3"
SRC_DIR = PHASE3 / "src"

# Make phase3_mech importable
sys.path.insert(0, str(SRC_DIR))

from phase3_mech import (  # noqa: E402
    make_vacuum_config,
    scan_amplitude_unconstrained,
    scan_amplitude_with_floor,
)


def main() -> None:
    # Paths
    tables_dir = PHASE3 / "outputs" / "tables"
    tables_dir.mkdir(parents=True, exist_ok=True)

    baseline_diag_path = tables_dir / "mech_baseline_scan_diagnostics.json"
    cert_diag_path = tables_dir / "mech_binding_certificate_diagnostics.json"
    cert_csv_path = tables_dir / "mech_binding_certificate.csv"

    if not baseline_diag_path.exists():
        raise SystemExit(
            f"[binding_certificate] Baseline diagnostics not found at "
            f"{baseline_diag_path}. Run run_baseline_scan.py first."
        )

    # Load baseline diagnostics to reuse epsfloor and grid settings
    with baseline_diag_path.open("r", encoding="utf-8") as f:
        baseline_diag = json.load(f)

    epsfloor = float(baseline_diag["epsfloor"])
    n_grid = int(baseline_diag["n_grid"])
    theta_min = float(baseline_diag["theta_min"])
    theta_max = float(baseline_diag["theta_max"])

    print("[binding_certificate] Using parameters from baseline scan:")
    print(f"  epsfloor   = {epsfloor}")
    print(f"  n_grid     = {n_grid}")
    print(f"  theta_min  = {theta_min}")
    print(f"  theta_max  = {theta_max}")

    cfg = make_vacuum_config("baseline_v1")

    # Unconstrained scan
    thetas, amps0 = scan_amplitude_unconstrained(
        cfg,
        n_grid=n_grid,
        theta_min=theta_min,
        theta_max=theta_max,
    )

    # Floor-enforced scan (this re-runs the same grid internally)
    (
        thetas_floor,
        amps0_again,
        amps_floor,
        binds,
        diag_floor,
    ) = scan_amplitude_with_floor(
        cfg,
        epsfloor=epsfloor,
        n_grid=n_grid,
        theta_min=theta_min,
        theta_max=theta_max,
    )

    # Sanity: grids must match
    if not np.allclose(thetas, thetas_floor):
        raise RuntimeError("[binding_certificate] theta grids do not match")
    if not np.allclose(amps0, amps0_again):
        raise RuntimeError("[binding_certificate] A0(theta) mismatch between scans")

    # Summary statistics
    mean_a0 = float(amps0.mean())
    mean_af = float(amps_floor.mean())
    var_a0 = float(amps0.var())
    var_af = float(amps_floor.var())

    # Simple L2 distances
    l2_diff = float(np.sqrt(np.mean((amps_floor - amps0) ** 2)))
    mean_shift = mean_af - mean_a0

    # Fraction where the floor is active (should match diag_floor["frac_bound"])
    frac_bound = float(binds.mean())

    diag_cert = {
        "epsfloor": epsfloor,
        "n_grid": n_grid,
        "theta_min": theta_min,
        "theta_max": theta_max,
        "mean_A0": mean_a0,
        "mean_A": mean_af,
        "var_A0": var_a0,
        "var_A": var_af,
        "mean_shift": mean_shift,
        "l2_diff": l2_diff,
        "frac_bound": frac_bound,
        "min_unconstrained": float(diag_floor["min_unconstrained"]),
        "max_unconstrained": float(diag_floor["max_unconstrained"]),
    }

    # Write diagnostics JSON
    with cert_diag_path.open("w", encoding="utf-8") as f:
        json.dump(diag_cert, f, indent=2, sort_keys=True)

    # Per-theta CSV for reproducibility and future figures
    with cert_csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["theta", "A0", "A", "bound"])
        for theta, a0, af, b in zip(thetas, amps0, amps_floor, binds):
            writer.writerow([float(theta), float(a0), float(af), int(bool(b))])

    print(f"[binding_certificate] Wrote diagnostics to {cert_diag_path}")
    print(f"[binding_certificate] Wrote per-grid data to {cert_csv_path}")
    print("[binding_certificate] Summary diagnostics:")
    for k, v in diag_cert.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
