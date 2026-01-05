import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# NOTE: Phase 3: this file intentionally defines the ansatz explicitly.
# Changing the ansatz requires a Scope Addendum + Claims Table update.

@dataclass
class FitResult:
    theta_best: float
    chi2: float
    dof: int
    theta_interval_68: Tuple[float, float]
    meta: Dict[str, Any]

def ansatz_predictions(theta: float) -> Dict[str, float]:
    """
    Placeholder ansatz mapping theta -> observables.
    Replace with Phase 3's chosen fixed ansatz (documented in paper).
    """
    # Minimal toy structure; MUST be replaced with actual Phase 3 mapping.
    return {
        "ckm_proxy": math.sin(theta),
        "pmns_proxy": math.cos(theta),
    }

def chi2_objective(theta: float, targets: Dict[str, float], sigmas: Dict[str, float]) -> float:
    preds = ansatz_predictions(theta)
    chi2 = 0.0
    for k, t in targets.items():
        s = sigmas[k]
        chi2 += ((preds[k] - t) / s) ** 2
    return chi2

def fit_theta(targets: Dict[str, float], sigmas: Dict[str, float]) -> FitResult:
    grid = np.linspace(0.0, 2.0*np.pi, 20001)
    chi2s = np.array([chi2_objective(th, targets, sigmas) for th in grid])
    idx = int(np.argmin(chi2s))
    theta_best = float(grid[idx])
    chi2_best = float(chi2s[idx])
    dof = max(1, len(targets) - 1)

    # crude 68% interval using delta-chi2=1 for 1 parameter
    mask = chi2s <= (chi2_best + 1.0)
    thetas_in = grid[mask]
    theta_lo = float(thetas_in.min())
    theta_hi = float(thetas_in.max())

    meta = {
        "grid_points": int(grid.size),
        "theta_best_rad": theta_best,
        "theta_best_deg": float(theta_best * 180.0 / np.pi),
        "chi2_best": chi2_best,
        "dof": dof,
        "interval_68_rad": [theta_lo, theta_hi],
    }
    return FitResult(theta_best, chi2_best, dof, (theta_lo, theta_hi), meta)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out_summary", required=True)
    ap.add_argument("--out_fig", required=True)
    args = ap.parse_args()

    out_summary = Path(args.out_summary)
    out_fig = Path(args.out_fig)
    out_summary.parent.mkdir(parents=True, exist_ok=True)
    out_fig.parent.mkdir(parents=True, exist_ok=True)

    # Phase 3 TODO: replace with real CKM+PMNS target extraction,
    # and record sources + version in meta.
    targets = {"ckm_proxy": 0.0, "pmns_proxy": 0.0}
    sigmas = {"ckm_proxy": 0.2, "pmns_proxy": 0.2}

    res = fit_theta(targets, sigmas)

    df = pd.DataFrame([{
        "theta_best_rad": res.theta_best,
        "theta_best_deg": res.theta_best * 180.0 / np.pi,
        "chi2": res.chi2,
        "dof": res.dof,
        "theta_68_lo_rad": res.theta_interval_68[0],
        "theta_68_hi_rad": res.theta_interval_68[1],
    }])
    df.to_csv(out_summary, index=False)

    # Diagnostic plot
    grid = np.linspace(0.0, 2.0*np.pi, 20001)
    chi2s = np.array([chi2_objective(th, targets, sigmas) for th in grid])
    plt.figure()
    plt.plot(grid, chi2s)
    plt.axvline(res.theta_best, linestyle="--")
    plt.xlabel("theta [rad]")
    plt.ylabel("chi2")
    plt.tight_layout()
    plt.savefig(out_fig)
    plt.close()

    # Also emit a small meta next to summary
    meta_path = out_summary.with_suffix(".meta.json")
    meta_path.write_text(json.dumps(res.meta, indent=2))

if __name__ == "__main__":
    main()
