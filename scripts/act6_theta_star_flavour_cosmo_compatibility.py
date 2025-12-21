#!/usr/bin/env python3
"""
Act VI / Gate 1:
Compare θ★ flavour posterior vs cosmology corridor and write:
- data/processed/theta_star_flavour_cosmo_compatibility.json
- figures/theta_star_flavour_vs_cosmo_overlap.png

Read-only inputs (origin-axiom):
- data/processed/theta_star_posterior_summary_from_flavour.json
- data/processed/theta_star_lcdm_background_corridor_plot_summary.json
- data/processed/theta_star_lcdm_growth_comparison.json
- data/processed/effective_vacuum_theta_frw_scan.npz   (fallback only; full band)
"""

from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Tuple

import matplotlib.pyplot as plt


REPO_ROOT = Path(__file__).resolve().parents[1]

FLAVOUR_JSON = REPO_ROOT / "data/processed/theta_star_posterior_summary_from_flavour.json"
BKG_JSON = REPO_ROOT / "data/processed/theta_star_lcdm_background_corridor_plot_summary.json"
GROWTH_JSON = REPO_ROOT / "data/processed/theta_star_lcdm_growth_comparison.json"
FRW_NPZ = REPO_ROOT / "data/processed/effective_vacuum_theta_frw_scan.npz"  # fallback only

OUT_JSON = REPO_ROOT / "data/processed/theta_star_flavour_cosmo_compatibility.json"
OUT_FIG = REPO_ROOT / "figures/theta_star_flavour_vs_cosmo_overlap.png"


@dataclass(frozen=True)
class Band:
    q16: float
    q50: float
    q84: float

    @property
    def lo(self) -> float:
        return float(self.q16)

    @property
    def hi(self) -> float:
        return float(self.q84)


def git_head(repo: Path) -> str:
    try:
        cp = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        return cp.stdout.strip()
    except Exception:
        return "UNKNOWN_GIT_HEAD"


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Missing required input: {path}")
    return json.loads(path.read_text())


def extract_flavour_band(d: Dict[str, Any]) -> Band:
    g = d.get("global", {})
    q16 = g.get("theta_q16")
    q50 = g.get("theta_q50")
    q84 = g.get("theta_q84")
    if q16 is None or q50 is None or q84 is None:
        raise KeyError("Flavour JSON missing global theta_q16/theta_q50/theta_q84")
    return Band(float(q16), float(q50), float(q84))


def extract_cosmo_corridor(d_bkg: Dict[str, Any], d_growth: Dict[str, Any]) -> Tuple[float, float]:
    """Return the *observable corridor* bounds in theta_star.

    Priority order:
    1) Background corridor summary JSON (R23): key `theta_corridor`
    2) Optional explicit corridor keys in growth JSON (future-proof)
    3) FRW NPZ band metadata (theta_min_band/theta_max_band) as LAST resort
       (note: this is the *full band*, not the corridor)
    """
    # 1) Authoritative: R23 summary contains theta_corridor
    tc = d_bkg.get("theta_corridor", None)
    if isinstance(tc, (list, tuple)) and len(tc) == 2:
        return float(tc[0]), float(tc[1])
    if isinstance(tc, dict) and "min" in tc and "max" in tc:
        return float(tc["min"]), float(tc["max"])

    # 2) Growth JSON explicit corridor bounds (if present in future)
    for k_lo, k_hi in [
        ("theta_corridor_min", "theta_corridor_max"),
        ("theta_min_corridor", "theta_max_corridor"),
    ]:
        if k_lo in d_growth and k_hi in d_growth:
            return float(d_growth[k_lo]), float(d_growth[k_hi])

    # 3) LAST resort fallback: FRW NPZ metadata (full band, not corridor)
    if FRW_NPZ.exists():
        import numpy as np

        z = np.load(FRW_NPZ, allow_pickle=True)
        files = set(z.files)
        if "theta_min_band" in files and "theta_max_band" in files:
            return float(z["theta_min_band"]), float(z["theta_max_band"])

    raise KeyError("Could not locate cosmology corridor theta bounds (theta_corridor).")


def overlap_interval(a_lo: float, a_hi: float, b_lo: float, b_hi: float) -> Tuple[bool, float, float]:
    lo = max(a_lo, b_lo)
    hi = min(a_hi, b_hi)
    return (hi >= lo), lo, hi


def main() -> None:
    ts = datetime.now(timezone.utc).isoformat()
    head = git_head(REPO_ROOT)

    d_flav = load_json(FLAVOUR_JSON)
    d_bkg = load_json(BKG_JSON)
    d_gr = load_json(GROWTH_JSON)

    flav = extract_flavour_band(d_flav)
    cos_lo, cos_hi = extract_cosmo_corridor(d_bkg, d_gr)

    ok, ov_lo, ov_hi = overlap_interval(flav.lo, flav.hi, cos_lo, cos_hi)

    payload: Dict[str, Any] = {
        "schema_version": "act6.compat.v1",
        "git_head": head,
        "timestamp_utc": ts,
        "inputs": {
            "flavour_posterior": str(FLAVOUR_JSON.relative_to(REPO_ROOT)),
            "cosmo_background_summary": str(BKG_JSON.relative_to(REPO_ROOT)),
            "cosmo_growth_summary": str(GROWTH_JSON.relative_to(REPO_ROOT)),
            "cosmo_frw_scan_npz_fallback": str(FRW_NPZ.relative_to(REPO_ROOT)) if FRW_NPZ.exists() else None,
        },
        "definition": {
            "flavour_band": "global theta★ quantiles (q16, q50, q84) from theta_star_posterior_summary_from_flavour.json",
            "cosmo_corridor": "theta★ corridor bounds from R23 summary key theta_corridor (FRW NPZ only as last-resort fallback)",
        },
        "bands": {
            "theta_flavour": {"q16": flav.q16, "q50": flav.q50, "q84": flav.q84},
            "theta_cosmo_corridor": {"min": cos_lo, "max": cos_hi},
        },
        "overlap": {
            "exists": bool(ok),
            "theta_min": float(ov_lo) if ok else None,
            "theta_max": float(ov_hi) if ok else None,
        },
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_FIG.parent.mkdir(parents=True, exist_ok=True)

    OUT_JSON.write_text(json.dumps(payload, indent=2))
    print(f"Wrote {OUT_JSON.relative_to(REPO_ROOT)}")

    # ---- Plot (1D band overlay) ----
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    y_flav = 1.0
    y_cos = 0.0

    ax.plot([flav.lo, flav.hi], [y_flav, y_flav], linewidth=8)
    ax.plot([flav.q50], [y_flav], marker="o")

    ax.plot([cos_lo, cos_hi], [y_cos, y_cos], linewidth=8)

    if ok:
        ax.plot([ov_lo, ov_hi], [0.5, 0.5], linewidth=10)

    ax.set_yticks([y_cos, 0.5, y_flav])
    ax.set_yticklabels(["cosmo corridor", "overlap", "flavour (q16–q84)"])
    ax.set_xlabel("theta_star (radians)")
    ax.set_title("Act VI: theta_star flavour posterior vs cosmology corridor")

    fig.tight_layout()
    fig.savefig(OUT_FIG, dpi=200)
    print(f"Wrote {OUT_FIG.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()