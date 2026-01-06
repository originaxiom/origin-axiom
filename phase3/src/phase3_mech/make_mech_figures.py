#!/usr/bin/env python
"""
Make Phase 3 mechanism figures.

At this rung we generate a single diagnostic figure that shows
A_0(theta) and the floor-enforced A(theta) over the baseline theta
grid, using the same configuration and parameters as the binding
certificate.
"""

import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Resolve phase3 directory and ensure we can import phase3_mech
THIS_FILE = Path(__file__).resolve()
PHASE3_DIR = THIS_FILE.parents[2]      # .../phase3
SRC_DIR = PHASE3_DIR / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from phase3_mech import (  # noqa: E402
    make_vacuum_config,
    scan_amplitude_with_floor,
)


def make_binding_profile_figure():
    """Plot A_0(theta) and A(theta) for the baseline binding configuration."""

    diag_path = PHASE3_DIR / "outputs" / "tables" / "mech_binding_certificate_diagnostics.json"
    if not diag_path.exists():
        raise FileNotFoundError(
            f"Diagnostics file not found: {diag_path}. "
            "Run run_binding_certificate.py first."
        )

    with diag_path.open("r", encoding="utf-8") as f:
        diag = json.load(f)

    epsfloor = float(diag["epsfloor"])
    n_grid = int(diag["n_grid"])
    theta_min = float(diag["theta_min"])
    theta_max = float(diag["theta_max"])

    cfg = make_vacuum_config("baseline_v1")
    thetas, amps0, amps_floor, binds, _ = scan_amplitude_with_floor(
        cfg,
        epsfloor=epsfloor,
        n_grid=n_grid,
        theta_min=theta_min,
        theta_max=theta_max,
    )

    fig_dir = PHASE3_DIR / "outputs" / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)
    fig_path = fig_dir / "fig1_mech_binding_profile.pdf"

    plt.figure()
    plt.plot(thetas, amps0, label=r"$A_0(\theta)$")
    plt.plot(thetas, amps_floor, label=r"$A(\theta)$ with floor")
    plt.axhline(epsfloor, linestyle="--", label=r"$\varepsilon_{\mathrm{floor}}$")
    plt.xlabel(r"$\theta$")
    plt.ylabel(r"amplitude")
    plt.title("Phase 3 toy vacuum: binding regime profile")
    plt.legend()
    plt.tight_layout()
    plt.savefig(fig_path)
    plt.close()

    print(f"[make_mech_figures] Wrote binding profile figure to {fig_path}")


def main():
    make_binding_profile_figure()


if __name__ == "__main__":
    main()
