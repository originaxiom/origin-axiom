"""
F1 mapping family: map the Phase 3 global amplitude into a toy
vacuum-energy-like scalar E_vac(theta).

This module is intentionally narrow and explicit. It:

  - locates the Phase 3 baseline diagnostics
    (mech_baseline_scan_diagnostics.json) under
    phase3/outputs/tables/;
  - loads the quantile-based floor epsfloor from that file;
  - reuses the Phase 3 vacuum mechanism (phase3_mech) to compute
    A(theta) with the floor enforced; and
  - maps A(theta) into E_vac(theta) = alpha * A(theta)^beta.

No FRW dynamics, theta-corridors, or filters are defined here; this is
just the scalar mapping and its metadata.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Tuple

import numpy as np

# --------------------------------------------------------------------
# Repo root and Phase 3 imports
# --------------------------------------------------------------------

THIS_FILE = Path(__file__).resolve()
# .../origin-axiom/phase4/src/phase4/mappings_f1.py -> repo root is parents[3]
REPO_ROOT = THIS_FILE.parents[3]

PHASE3_SRC = REPO_ROOT / "phase3" / "src"
if str(PHASE3_SRC) not in sys.path:
    sys.path.insert(0, str(PHASE3_SRC))

from phase3_mech import (  # type: ignore[import]
    make_vacuum_config,
    scan_amplitude_with_floor,
)

# Phase 3 baseline diagnostics (already produced by run_baseline_scan)
BASELINE_DIAG_DEFAULT = Path(
    "phase3/outputs/tables/mech_baseline_scan_diagnostics.json"
)


# --------------------------------------------------------------------
# Config dataclass
# --------------------------------------------------------------------

@dataclass
class F1MappingConfig:
    """
    Configuration for the F1 mapping family.

    Fields
    ------
    name : str
        Human-readable label for this mapping configuration.
    baseline_diag_path : Path
        Path (relative to repo root or absolute) to the Phase 3
        baseline diagnostics JSON.
    alpha : float
        Overall normalisation factor in E_vac(theta) = alpha * A(theta)^beta.
    beta : float
        Exponent in E_vac(theta) = alpha * A(theta)^beta.
    vacuum_name : str
        Name passed to phase3_mech.make_vacuum_config (e.g. "baseline_v1").
    """

    name: str = "F1_baseline_v1"
    baseline_diag_path: Path = BASELINE_DIAG_DEFAULT
    alpha: float = 1.0
    beta: float = 4.0
    vacuum_name: str = "baseline_v1"


def build_default_f1_config() -> F1MappingConfig:
    """
    Return the default F1 mapping configuration.
    """
    return F1MappingConfig()


# --------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------

def _resolve_repo_relative(path: Path) -> Path:
    """
    Interpret a path as repo-relative if it is not already absolute.
    """
    if path.is_absolute():
        return path
    return REPO_ROOT / path


def load_baseline_epsfloor(path: Path) -> Tuple[float, Dict]:
    """
    Load epsfloor and diagnostics from the Phase 3 baseline JSON.

    Parameters
    ----------
    path : Path
        Path to mech_baseline_scan_diagnostics.json, either absolute
        or relative to the repo root.

    Returns
    -------
    epsfloor : float
        The quantile-based floor used in the Phase 3 baseline scan.
    diag : dict
        Full diagnostics dictionary for reference.
    """
    resolved = _resolve_repo_relative(path)
    if not resolved.exists():
        raise FileNotFoundError(
            f"Baseline diagnostics not found at {resolved}. "
            "Make sure you've run phase3/src/phase3_mech/run_baseline_scan.py "
            "and committed the outputs."
        )

    with resolved.open("r", encoding="utf-8") as f:
        diag = json.load(f)

    if "epsfloor" not in diag:
        raise KeyError(
            f"Diagnostics file {resolved} does not contain 'epsfloor'. "
            "Did the Phase 3 baseline scan complete correctly?"
        )

    epsfloor = float(diag["epsfloor"])
    return epsfloor, diag


# --------------------------------------------------------------------
# Main mapping: E_vac(theta)
# --------------------------------------------------------------------

def compute_f1_vacuum_curve(
    cfg: F1MappingConfig,
):
    """
    Compute the F1 vacuum-energy-like curve E_vac(theta).

    Steps:
      1. Load epsfloor and baseline diagnostics from Phase 3.
      2. Build the Phase 3 vacuum configuration (baseline_v1).
      3. Rescan A(theta) with the floor enforced.
      4. Map A(theta) -> E_vac(theta) = alpha * A(theta)^beta.
      5. Return (thetas, E_vac(theta), metadata).

    Returns
    -------
    thetas : np.ndarray
        1D array of theta values.
    evac : np.ndarray
        1D array of E_vac(theta) values.
    meta : dict
        Metadata describing the mapping and diagnostics.
    """
    # 1. Load epsfloor and diagnostics from Phase 3 baseline.
    epsfloor, diag_base = load_baseline_epsfloor(cfg.baseline_diag_path)

    # Use the theta grid recorded in the baseline diagnostics if present.
    n_grid = int(diag_base.get("n_grid", 2048))
    theta_min = float(diag_base.get("theta_min", 0.0))
    theta_max = float(diag_base.get("theta_max", 2.0 * np.pi))

    # 2. Build the Phase 3 vacuum configuration.
    vac_cfg = make_vacuum_config(cfg.vacuum_name)

    # 3. Rescan amplitudes with the same grid and epsfloor.
    thetas, amps0, amps_floor, binds, vac_diag = scan_amplitude_with_floor(
        vac_cfg,
        epsfloor=epsfloor,
        n_grid=n_grid,
        theta_min=theta_min,
        theta_max=theta_max,
    )

    # 4. Map A(theta) -> E_vac(theta).
    evac = cfg.alpha * np.power(amps_floor, cfg.beta)

    # 5. Metadata for sanity checks and later corridor work.
    resolved_diag_path = _resolve_repo_relative(cfg.baseline_diag_path)

    meta = {
        "mapping_family": "F1",
        "mapping_name": cfg.name,
        "alpha": float(cfg.alpha),
        "beta": float(cfg.beta),
        "vacuum_name": cfg.vacuum_name,
        "baseline_diag_path": str(resolved_diag_path),
        "n_grid": int(n_grid),
        "theta_min": float(theta_min),
        "theta_max": float(theta_max),
        "epsfloor": float(epsfloor),
        "baseline_diagnostics": diag_base,
        "vacuum_diagnostics": vac_diag,
        "frac_bound": float(vac_diag.get("frac_bound", float(binds.mean()))),
    }

    return thetas, evac, meta


__all__ = [
    "F1MappingConfig",
    "build_default_f1_config",
    "compute_f1_vacuum_curve",
]
