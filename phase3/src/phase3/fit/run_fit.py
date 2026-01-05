import argparse
import json
import math
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any, Tuple, List

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

try:
    import yaml  # pyyaml
except ImportError as e:
    raise SystemExit("Missing dependency: pyyaml. Install: pip install pyyaml") from e


# -----------------------------
# Contract-driven fit machinery
# -----------------------------

@dataclass
class Observable:
    key: str
    target: float
    sigma: float
    weight: float
    notes: str = ""


@dataclass
class FitConfig:
    placeholder_mode: bool
    dataset_name: str
    dataset_notes: str
    ansatz_name: str
    ansatz_version: str
    ansatz_description: str
    theta_min: float
    theta_max: float
    grid_points: int
    delta_chi2_68: float
    observables: List[Observable]


def _git_head_sha(repo_root: Path) -> str:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        return out
    except Exception:
        return "UNKNOWN"


def _sha256_text(s: str) -> str:
    import hashlib
    h = hashlib.sha256()
    h.update(s.encode("utf-8"))
    return h.hexdigest()


def load_config(repo_root: Path) -> Tuple[FitConfig, Path, str]:
    cfg_path = repo_root / "phase3" / "fit" / "targets.yaml"
    raw = cfg_path.read_text(encoding="utf-8")
    y = yaml.safe_load(raw)

    placeholder_mode = bool(y["meta"]["placeholder_mode"])
    dataset_name = str(y["meta"].get("dataset_name", "UNKNOWN"))
    dataset_notes = str(y["meta"].get("dataset_notes", ""))

    ansatz_name = str(y["ansatz"]["name"])
    ansatz_version = str(y["ansatz"]["version"])
    ansatz_description = str(y["ansatz"].get("description", ""))

    theta_min = float(y["scan"]["theta_min_rad"])
    theta_max = float(y["scan"]["theta_max_rad"])
    grid_points = int(y["scan"]["grid_points"])
    delta_chi2_68 = float(y["scan"]["delta_chi2_for_68"])

    obs_list: List[Observable] = []
    for o in y["observables"]:
        obs_list.append(
            Observable(
                key=str(o["key"]),
                target=float(o["target"]),
                sigma=float(o["sigma"]),
                weight=float(o.get("weight", 1.0)),
                notes=str(o.get("notes", "")),
            )
        )

    cfg = FitConfig(
        placeholder_mode=placeholder_mode,
        dataset_name=dataset_name,
        dataset_notes=dataset_notes,
        ansatz_name=ansatz_name,
        ansatz_version=ansatz_version,
        ansatz_description=ansatz_description,
        theta_min=theta_min,
        theta_max=theta_max,
        grid_points=grid_points,
        delta_chi2_68=delta_chi2_68,
        observables=obs_list,
    )
    return cfg, cfg_path, raw


def validate_config(cfg: FitConfig) -> None:
    if cfg.grid_points < 1000:
        raise SystemExit("grid_points too small; must be >=1000 for stable scanning.")
    if cfg.theta_max <= cfg.theta_min:
        raise SystemExit("Invalid theta range.")
    if cfg.delta_chi2_68 <= 0:
        raise SystemExit("delta_chi2_for_68 must be > 0.")
    if len(cfg.observables) == 0:
        raise SystemExit("No observables defined in targets.yaml.")

    for ob in cfg.observables:
        if ob.sigma <= 0:
            raise SystemExit(f"Observable {ob.key} has non-positive sigma.")
        if ob.weight <= 0:
            raise SystemExit(f"Observable {ob.key} has non-positive weight.")

    if not cfg.placeholder_mode:
        # Hard block placeholder keys if placeholder_mode is false
        bad = [ob.key for ob in cfg.observables if "proxy" in ob.key.lower()]
        if bad:
            raise SystemExit(
                "placeholder_mode=false but placeholder keys still present: " + ", ".join(bad)
            )


# -----------------------------
# Ansatz mapping (TO BE LOCKED)
# -----------------------------
def ansatz_predictions(theta: float, keys: List[str]) -> Dict[str, float]:
    """
    Contract:
    - This function is the only place where theta -> predictions are defined.
    - Any change requires bump ansatz.version in targets.yaml + update logs/claims table.

    Placeholder implementation:
    - Produces two proxy observables to keep pipeline runnable.
    Replace with real CKM+PMNS mapping once locked.
    """
    base = {
        "ckm_proxy": math.sin(theta),
        "pmns_proxy": math.cos(theta),
    }
    # Only return requested keys (prevents silent key drift)
    return {k: base[k] for k in keys}


def chi2_objective(theta: float, observables: List[Observable]) -> float:
    keys = [ob.key for ob in observables]
    preds = ansatz_predictions(theta, keys)

    chi2 = 0.0
    for ob in observables:
        pred = float(preds[ob.key])
        chi2 += ob.weight * ((pred - ob.target) / ob.sigma) ** 2
    return float(chi2)


def contiguous_interval_from_mask(xs: np.ndarray, mask: np.ndarray) -> Tuple[float, float, bool]:
    """
    Returns (lo, hi, multi_segment_flag).
    If mask has multiple disjoint segments, we return envelope and flag=True.
    """
    idx = np.where(mask)[0]
    if idx.size == 0:
        return (float("nan"), float("nan"), True)

    # detect segment breaks
    breaks = np.where(np.diff(idx) > 1)[0]
    multi = breaks.size > 0

    lo = float(xs[idx.min()])
    hi = float(xs[idx.max()])
    return (lo, hi, multi)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out_summary", required=True)
    ap.add_argument("--out_fig", required=True)
    ap.add_argument("--out_diagnostics", required=False, default=None)
    args = ap.parse_args()

    # repo root = current working directory
    repo_root = Path.cwd().resolve()
    cfg, cfg_path, cfg_raw = load_config(repo_root)
    validate_config(cfg)

    out_summary = Path(args.out_summary).resolve()
    out_fig = Path(args.out_fig).resolve()
    out_summary.parent.mkdir(parents=True, exist_ok=True)
    out_fig.parent.mkdir(parents=True, exist_ok=True)

    out_diag = (
        Path(args.out_diagnostics).resolve()
        if args.out_diagnostics is not None
        else out_summary.parent / "theta_fit_diagnostics.json"
    )

    # Scan grid
    thetas = np.linspace(cfg.theta_min, cfg.theta_max, cfg.grid_points)
    chi2s = np.array([chi2_objective(th, cfg.observables) for th in thetas], dtype=float)

    idx_min = int(np.argmin(chi2s))
    theta_best = float(thetas[idx_min])
    chi2_best = float(chi2s[idx_min])
    dof = max(1, len(cfg.observables) - 1)

    # 68% interval via delta chi2 (1-parameter convention)
    mask = chi2s <= (chi2_best + cfg.delta_chi2_68)
    theta_lo, theta_hi, multi_segment = contiguous_interval_from_mask(thetas, mask)

    # Summary CSV
    df = pd.DataFrame([{
        "theta_best_rad": theta_best,
        "theta_best_deg": theta_best * 180.0 / np.pi,
        "chi2": chi2_best,
        "dof": dof,
        "theta_68_lo_rad": theta_lo,
        "theta_68_hi_rad": theta_hi,
        "ansatz_name": cfg.ansatz_name,
        "ansatz_version": cfg.ansatz_version,
        "dataset_name": cfg.dataset_name,
        "placeholder_mode": cfg.placeholder_mode,
    }])
    df.to_csv(out_summary, index=False)

    # Sidecar meta for summary (provenance)
    meta = {
        "generated_by": "phase3/src/phase3/fit/run_fit.py",
        "config_path": str(cfg_path),
        "config_sha256": _sha256_text(cfg_raw),
        "git_head": _git_head_sha(repo_root),
        "ansatz": {
            "name": cfg.ansatz_name,
            "version": cfg.ansatz_version,
            "description": cfg.ansatz_description,
        },
        "scan": {
            "theta_min_rad": cfg.theta_min,
            "theta_max_rad": cfg.theta_max,
            "grid_points": cfg.grid_points,
            "delta_chi2_for_68": cfg.delta_chi2_68,
        },
        "fit": {
            "theta_best_rad": theta_best,
            "theta_best_deg": theta_best * 180.0 / np.pi,
            "chi2_best": chi2_best,
            "dof": dof,
            "interval_68_rad": [theta_lo, theta_hi],
            "multi_segment_interval": bool(multi_segment),
        },
        "observables": [
            {"key": ob.key, "target": ob.target, "sigma": ob.sigma, "weight": ob.weight, "notes": ob.notes}
            for ob in cfg.observables
        ],
        "dataset_notes": cfg.dataset_notes,
    }
    out_summary.with_suffix(".meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")

    # Diagnostics JSON (extra detail to support reviewer questions)
    diagnostics = {
        "theta_grid_rad": {
            "min": float(cfg.theta_min),
            "max": float(cfg.theta_max),
            "n": int(cfg.grid_points),
        },
        "chi2_min": chi2_best,
        "theta_best_rad": theta_best,
        "theta_68_interval_rad": [theta_lo, theta_hi],
        "multi_segment_interval": bool(multi_segment),
        "note": "If multi_segment_interval=true, the 68% region was disjoint; envelope reported.",
    }
    out_diag.write_text(json.dumps(diagnostics, indent=2), encoding="utf-8")

    # Diagnostic figure
    plt.figure()
    plt.plot(thetas, chi2s)
    plt.axvline(theta_best, linestyle="--")
    plt.xlabel("theta [rad]")
    plt.ylabel("chi2")
    plt.tight_layout()
    plt.savefig(out_fig)
    plt.close()


if __name__ == "__main__":
    main()
