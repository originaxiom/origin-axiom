import argparse
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

import numpy as np
import pandas as pd

# ---- Ensure repo root is on sys.path so imports work when run as a script ----
REPO_ROOT = Path(__file__).resolve().parents[4]  # .../origin-axiom
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from phase3.src.phase3.fit.run_fit import load_config, validate_config, chi2_objective  # noqa: E402


@dataclass
class HypothesisResult:
    b_pmns: float
    theta_best: float
    chi2_best: float
    dof: int
    theta_68_lo: float
    theta_68_hi: float
    multi_segment: bool


def contiguous_interval(xs: np.ndarray, mask: np.ndarray) -> Tuple[float, float, bool]:
    idx = np.where(mask)[0]
    if idx.size == 0:
        return (float("nan"), float("nan"), True)
    breaks = np.where(np.diff(idx) > 1)[0]
    multi = breaks.size > 0
    return (float(xs[idx.min()]), float(xs[idx.max()]), bool(multi))


def run_one(cfg, b_pmns: float) -> HypothesisResult:
    mapping = dict(cfg.mapping)
    mapping["delta_pmns"] = dict(mapping.get("delta_pmns", {}))
    mapping["delta_pmns"]["b"] = float(b_pmns)

    thetas = np.linspace(cfg.theta_min, cfg.theta_max, cfg.grid_points)
    chi2s = np.array([chi2_objective(th, cfg.observables, mapping) for th in thetas], dtype=float)

    idx_min = int(np.argmin(chi2s))
    theta_best = float(thetas[idx_min])
    chi2_best = float(chi2s[idx_min])
    dof = max(1, len([ob for ob in cfg.observables if ob.enabled]) - 1)

    mask = chi2s <= (chi2_best + cfg.delta_chi2_68)
    lo, hi, multi = contiguous_interval(thetas, mask)

    return HypothesisResult(
        b_pmns=float(b_pmns),
        theta_best=theta_best,
        chi2_best=chi2_best,
        dof=dof,
        theta_68_lo=lo,
        theta_68_hi=hi,
        multi_segment=multi,
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out_csv", required=True)
    ap.add_argument("--out_json", required=True)
    ap.add_argument(
        "--b_list",
        required=False,
        default=None,
        help="Comma-separated b values (radians). Default: 0, pi, -pi/2, +pi/2.",
    )
    args = ap.parse_args()

    repo_root = Path.cwd().resolve()
    cfg, cfg_path, cfg_raw = load_config(repo_root)
    validate_config(cfg)

    if args.b_list:
        b_vals = [float(x.strip()) for x in args.b_list.split(",") if x.strip()]
    else:
        b_vals = [0.0, math.pi, -math.pi / 2.0, math.pi / 2.0]

    results = [run_one(cfg, b) for b in b_vals]
    chi2_min = min(r.chi2_best for r in results)

    rows = []
    for r in results:
        rows.append(
            {
                "b_pmns_rad": r.b_pmns,
                "b_pmns_deg": r.b_pmns * 180.0 / math.pi,
                "theta_best_rad": r.theta_best,
                "theta_best_deg": r.theta_best * 180.0 / math.pi,
                "chi2": r.chi2_best,
                "dof": r.dof,
                "delta_chi2": r.chi2_best - chi2_min,
                "theta_68_lo_rad": r.theta_68_lo,
                "theta_68_hi_rad": r.theta_68_hi,
                "multi_segment_interval": r.multi_segment,
            }
        )

    df = pd.DataFrame(rows).sort_values(["chi2", "b_pmns_rad"]).reset_index(drop=True)

    out_csv = Path(args.out_csv)
    out_json = Path(args.out_json)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    out_json.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(out_csv, index=False)

    payload = {
        "config_path": str(cfg_path),
        "ansatz_name": cfg.ansatz_name,
        "ansatz_version": cfg.ansatz_version,
        "b_values_rad": b_vals,
        "chi2_min": chi2_min,
        "note": "Discrete fixed-offset hypotheses; b is NOT fit.",
    }
    out_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()