import argparse
import json
import math
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any, Tuple, List, Optional

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

try:
    import yaml  # pyyaml
except ImportError as e:
    raise SystemExit("Missing dependency: pyyaml. Install: pip install pyyaml") from e


@dataclass
class Observable:
    key: str
    enabled: bool
    metric: str               # "linear" | "circular_rad"
    target: float
    sigma: float
    weight: float
    periodicity_rad: Optional[float] = None
    source: str = "UNKNOWN"
    notes: str = ""


@dataclass
class FitConfig:
    placeholder_mode: bool
    dataset_name: str
    dataset_notes: str

    ansatz_name: str
    ansatz_version: str
    ansatz_description: str
    mapping: Dict[str, Any]

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
    mapping = dict(y["ansatz"].get("mapping", {}))

    theta_min = float(y["scan"]["theta_min_rad"])
    theta_max = float(y["scan"]["theta_max_rad"])
    grid_points = int(y["scan"]["grid_points"])
    delta_chi2_68 = float(y["scan"]["delta_chi2_for_68"])

    obs_list: List[Observable] = []
    for o in y["observables"]:
        obs_list.append(
            Observable(
                key=str(o["key"]),
                enabled=bool(o.get("enabled", True)),
                metric=str(o.get("metric", "linear")),
                periodicity_rad=(float(o["periodicity_rad"]) if "periodicity_rad" in o else None),
                target=float(o["target"]),
                sigma=float(o["sigma"]),
                weight=float(o.get("weight", 1.0)),
                source=str(o.get("source", "UNKNOWN")),
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
        mapping=mapping,
        theta_min=theta_min,
        theta_max=theta_max,
        grid_points=grid_points,
        delta_chi2_68=delta_chi2_68,
        observables=obs_list,
    )
    return cfg, cfg_path, raw


def validate_config(cfg: FitConfig) -> None:
    if cfg.grid_points < 1000:
        raise SystemExit("grid_points too small; must be >=1000.")
    if cfg.theta_max <= cfg.theta_min:
        raise SystemExit("Invalid theta range.")
    if cfg.delta_chi2_68 <= 0:
        raise SystemExit("delta_chi2_for_68 must be > 0.")

    enabled = [ob for ob in cfg.observables if ob.enabled]
    if len(enabled) == 0:
        raise SystemExit("No enabled observables.")

    for ob in enabled:
        if ob.sigma <= 0:
            raise SystemExit(f"Observable {ob.key} has non-positive sigma.")
        if ob.weight <= 0:
            raise SystemExit(f"Observable {ob.key} has non-positive weight.")
        if ob.metric not in ("linear", "circular_rad"):
            raise SystemExit(f"Observable {ob.key} has invalid metric: {ob.metric}")
        if ob.metric == "circular_rad" and (ob.periodicity_rad is None or ob.periodicity_rad <= 0):
            raise SystemExit(f"Observable {ob.key} requires periodicity_rad > 0 for circular metric.")

    if not cfg.placeholder_mode:
        bad = [ob.key for ob in enabled if "proxy" in ob.key.lower() or "PLACEHOLDER" in ob.source]
        if bad:
            raise SystemExit("placeholder_mode=false but placeholder content still present: " + ", ".join(bad))


def wrap_mod(x: float, period: float) -> float:
    return x % period


def circ_diff_rad(a: float, b: float, period: float) -> float:
    """
    Minimal signed distance on circle: returns value in [-period/2, +period/2].
    """
    d = (a - b) % period
    if d > period / 2:
        d -= period
    return d


def apply_affine_mod(theta: float, a: float, b: float, period: float) -> float:
    return wrap_mod(a * theta + b, period)


# -----------------------------
# Ansatz predictions (LOCK POINT)
# -----------------------------
def ansatz_predictions(theta: float, keys: List[str], mapping: Dict[str, Any]) -> Dict[str, float]:
    """
    Phase 3 single-parameter ansatz prediction map.

    Current v1-schema:
      - Predicts CP phases as affine transforms of theta (mod 2pi):
          delta_ckm(theta)  = (a*theta + b) mod 2pi
          delta_pmns(theta) = (a*theta + b) mod 2pi
      - Angles/J are NOT predicted unless you extend this (requires version bump + logs).

    This is intentionally minimal and scope-safe: Phase 3 core claim can be
    "one theta consistently anchors both CP phases under a declared mapping".
    """
    two_pi = 2.0 * math.pi

    # Defaults
    ckm_map = mapping.get("delta_ckm", {"type": "affine_mod_2pi", "a": 1.0, "b": 0.0})
    pmns_map = mapping.get("delta_pmns", {"type": "affine_mod_2pi", "a": 1.0, "b": 0.0})

    # Only supported mapping type in v1-schema
    if ckm_map.get("type") != "affine_mod_2pi" or pmns_map.get("type") != "affine_mod_2pi":
        raise SystemExit("Unsupported mapping type. v1-schema supports only affine_mod_2pi.")

    delta_ckm = apply_affine_mod(theta, float(ckm_map.get("a", 1.0)), float(ckm_map.get("b", 0.0)), two_pi)
    delta_pmns = apply_affine_mod(theta, float(pmns_map.get("a", 1.0)), float(pmns_map.get("b", 0.0)), two_pi)

    base = {
        "ckm.delta_rad": delta_ckm,
        "pmns.delta_cp_rad": delta_pmns,
    }

    # Return requested keys only
    out: Dict[str, float] = {}
    for k in keys:
        if k not in base:
            raise SystemExit(f"ansatz_predictions: key not implemented in v1-schema: {k}")
        out[k] = float(base[k])
    return out


def residual(pred: float, target: float, ob: Observable) -> float:
    if ob.metric == "linear":
        return pred - target
    if ob.metric == "circular_rad":
        assert ob.periodicity_rad is not None
        return circ_diff_rad(pred, target, ob.periodicity_rad)
    raise SystemExit(f"Unknown metric: {ob.metric}")


def chi2_objective(theta: float, observables: List[Observable], mapping: Dict[str, Any]) -> float:
    enabled = [ob for ob in observables if ob.enabled]
    keys = [ob.key for ob in enabled]
    preds = ansatz_predictions(theta, keys, mapping)

    chi2 = 0.0
    for ob in enabled:
        pred = float(preds[ob.key])
        r = residual(pred, ob.target, ob)
        chi2 += ob.weight * (r / ob.sigma) ** 2
    return float(chi2)


def contiguous_interval_from_mask(xs: np.ndarray, mask: np.ndarray) -> Tuple[float, float, bool]:
    idx = np.where(mask)[0]
    if idx.size == 0:
        return (float("nan"), float("nan"), True)

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

    thetas = np.linspace(cfg.theta_min, cfg.theta_max, cfg.grid_points)
    chi2s = np.array([chi2_objective(th, cfg.observables, cfg.mapping) for th in thetas], dtype=float)

    idx_min = int(np.argmin(chi2s))
    theta_best = float(thetas[idx_min])
    chi2_best = float(chi2s[idx_min])
    dof = max(1, len([ob for ob in cfg.observables if ob.enabled]) - 1)

    mask = chi2s <= (chi2_best + cfg.delta_chi2_68)
    theta_lo, theta_hi, multi_segment = contiguous_interval_from_mask(thetas, mask)

    enabled = [ob for ob in cfg.observables if ob.enabled]
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
        "enabled_observables": ",".join([ob.key for ob in enabled]),
    }])
    df.to_csv(out_summary, index=False)

    meta = {
        "generated_by": "phase3/src/phase3/fit/run_fit.py",
        "config_path": str(cfg_path),
        "config_sha256": _sha256_text(cfg_raw),
        "git_head": _git_head_sha(repo_root),
        "ansatz": {
            "name": cfg.ansatz_name,
            "version": cfg.ansatz_version,
            "description": cfg.ansatz_description,
            "mapping": cfg.mapping,
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
        "observables_enabled": [
            {
                "key": ob.key,
                "metric": ob.metric,
                "periodicity_rad": ob.periodicity_rad,
                "target": ob.target,
                "sigma": ob.sigma,
                "weight": ob.weight,
                "source": ob.source,
                "notes": ob.notes,
            } for ob in enabled
        ],
        "dataset_notes": cfg.dataset_notes,
    }
    out_summary.with_suffix(".meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")

    diagnostics = {
        "theta_grid_rad": {"min": cfg.theta_min, "max": cfg.theta_max, "n": cfg.grid_points},
        "chi2_min": chi2_best,
        "theta_best_rad": theta_best,
        "theta_68_interval_rad": [theta_lo, theta_hi],
        "multi_segment_interval": bool(multi_segment),
        "note": "If multi_segment_interval=true, the 68% region was disjoint; envelope reported.",
    }
    out_diag.write_text(json.dumps(diagnostics, indent=2), encoding="utf-8")

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
