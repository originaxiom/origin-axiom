#!/usr/bin/env python3
"""
Act VII / Gate 2 entrypoint
Implements: docs/ACT_VII_MINI_CONTRACT.txt (Option A)

Outputs (canonical for Act VII):
- data/processed/act7_toy_matter_window.json
- figures/act7_toy_matter_window.png
- figures/act7_growth_sigma8_like_vs_params.png

Model: flat FRW with matter + Lambda.
Toy baryon fraction fb = Omega_b/Omega_m scanned; (Omega_b, Omega_c) recorded but do not
change background/gravity in this toy gate (they are bookkeeping degrees of freedom here).

Acceptance cuts (frozen):
- theta_star in [2.4320, 3.8600] rad
- Omega_m in [0.20, 0.40]
- fb in [0.12, 0.22]
- Omega_Lambda = 1 - Omega_m
- q0 < 0
- t0 in [12, 15] Gyr
- distance residual vs ref at z=0.3,0.5,1.0 within 5%
- growth sigma8-like ratio within [0.92, 1.08] relative to best accepted bg residual

Notes:
- This is a survivability/sanity gate, not observational inference.
- Uses only numpy/matplotlib; no external data.
"""

from __future__ import annotations

import json
import math
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np
import matplotlib.pyplot as plt


REPO_ROOT = Path(__file__).resolve().parents[1]

OUT_JSON = REPO_ROOT / "data/processed/act7_toy_matter_window.json"
FIG_WINDOW = REPO_ROOT / "figures/act7_toy_matter_window.png"
FIG_SIGMA8 = REPO_ROOT / "figures/act7_growth_sigma8_like_vs_params.png"

# -------------------------
# Mini-contract constants
# -------------------------
THETA_MIN = 2.4320
THETA_MAX = 3.8600

OM_MIN = 0.20
OM_MAX = 0.40

FB_MIN = 0.12
FB_MAX = 0.22

H0_KM_S_MPC = 70.0

AGE_MIN_GYR = 12.0
AGE_MAX_GYR = 15.0

DL_TOL_FRAC = 0.05  # 5%

R_SIGMA8_MIN = 0.92
R_SIGMA8_MAX = 1.08

Z_POINTS = [0.3, 0.5, 1.0]

# Grid (reasonable default)
N_THETA = 25
N_OM = 21
N_FB = 11


# Physical constants (SI) for age in Gyr
MPC_M = 3.0856775814913673e22
KM_M = 1e3
SEC_PER_GYR = 3600 * 24 * 365.25 * 1e9


@dataclass(frozen=True)
class BackgroundObs:
    q0: float
    t0_gyr: float
    dL_over_cH0: Dict[float, float]  # z -> dL/(c/H0)


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


def H0_si() -> float:
    """H0 in 1/s."""
    return H0_KM_S_MPC * KM_M / MPC_M


def E_of_a(a: np.ndarray, om: float, ol: float) -> np.ndarray:
    """Dimensionless H(a)/H0 for flat matter+Lambda."""
    return np.sqrt(om / (a**3) + ol)


def age_t0_gyr(om: float, ol: float) -> float:
    """Compute age t0 in Gyr for flat matter+Lambda via integral."""
    # t0 = ∫_0^1 da / (a H(a)) = (1/H0) ∫_0^1 da / (a E(a))
    a = np.linspace(1e-6, 1.0, 20000)
    integrand = 1.0 / (a * E_of_a(a, om, ol))
    t0_over_H0 = np.trapezoid(integrand, a)
    t0_sec = t0_over_H0 / H0_si()
    return t0_sec / SEC_PER_GYR


def comoving_chi_over_cH0(z: float, om: float, ol: float) -> float:
    """χ(z) in units of (c/H0): ∫_0^z dz'/E(z')."""
    z_grid = np.linspace(0.0, z, 8000)
    Ez = np.sqrt(om * (1.0 + z_grid) ** 3 + ol)
    return float(np.trapezoid(1.0 / Ez, z_grid))


def dL_over_cH0(z: float, om: float, ol: float) -> float:
    """Luminosity distance in units of (c/H0): (1+z) * χ(z)."""
    return (1.0 + z) * comoving_chi_over_cH0(z, om, ol)


def q0_flat_m_lambda(om: float, ol: float) -> float:
    """Deceleration parameter for matter + Lambda at z=0 (w=-1)."""
    # q0 = 0.5*Omega_m - Omega_Lambda
    return 0.5 * om - ol


def background_observables(om: float) -> BackgroundObs:
    """Compute background observables for a flat model with Omega_Lambda = 1 - Omega_m."""
    ol = 1.0 - om
    q0 = q0_flat_m_lambda(om, ol)
    t0 = age_t0_gyr(om, ol)
    dls = {z: dL_over_cH0(z, om, ol) for z in Z_POINTS}
    return BackgroundObs(q0=q0, t0_gyr=t0, dL_over_cH0=dls)


def growth_Drel_today(om: float) -> float:
    """
    Compute linear growth factor D(a) for flat matter+Lambda, then return
    D_rel(a=1) relative to EdS, i.e. D(a=1)/a(=1) normalized to 1 at early times.

    We solve in a from a_i to 1:
      D'' + [ (3/a) + d ln E / da ] D' - (3/2) * Omega_m/(a^5 E^2) * D = 0
    with initial conditions in matter-dominated regime: D ~ a, so
      D(a_i)=a_i, D'(a_i)=1
    """
    ol = 1.0 - om
    a_i = 1e-3
    a_f = 1.0
    n = 8000
    a = np.linspace(a_i, a_f, n)

    E = E_of_a(a, om, ol)
    # d ln E / da
    dE_da = np.gradient(E, a)
    dlnE_da = dE_da / E

    D = np.zeros_like(a)
    V = np.zeros_like(a)  # V = dD/da

    D[0] = a_i
    V[0] = 1.0

    for i in range(n - 1):
        ai = a[i]
        Ei = E[i]
        dlnEi = dlnE_da[i]

        # ODE system:
        # D' = V
        # V' = (3/2)*Omega_m/(a^5 E^2)*D - [ (3/a) + dlnE/da ]*V
        def f_D(_D: float, _V: float) -> float:
            return _V

        def f_V(_D: float, _V: float) -> float:
            term_grav = 1.5 * om / (ai**5 * (Ei**2)) * _D
            term_fric = (3.0 / ai + dlnEi) * _V
            return term_grav - term_fric

        # RK2 (midpoint)
        da = a[i + 1] - ai
        k1D = f_D(D[i], V[i])
        k1V = f_V(D[i], V[i])

        Dm = D[i] + 0.5 * da * k1D
        Vm = V[i] + 0.5 * da * k1V

        am = ai + 0.5 * da
        Em = math.sqrt(om / (am**3) + ol)
        # approximate dlnE/da at midpoint
        # (cheap finite diff around am)
        eps = 1e-6
        Ep = math.sqrt(om / ((am + eps) ** 3) + ol)
        Emm = math.sqrt(om / ((am - eps) ** 3) + ol)
        dlnEm = (Ep - Emm) / (2 * eps) / Em

        def fV_mid(_D: float, _V: float) -> float:
            term_grav = 1.5 * om / (am**5 * (Em**2)) * _D
            term_fric = (3.0 / am + dlnEm) * _V
            return term_grav - term_fric

        k2D = Vm
        k2V = fV_mid(Dm, Vm)

        D[i + 1] = D[i] + da * k2D
        V[i + 1] = V[i] + da * k2V

    # Normalize relative to EdS (EdS D=a, so at a=1, D_rel = D(1)/1)
    return float(D[-1])


def bg_residual_metric(obs: BackgroundObs, ref: BackgroundObs) -> float:
    """Background residual metric used to choose reference model (chi2_bg-like)."""
    r_age = (obs.t0_gyr - ref.t0_gyr) / ref.t0_gyr
    r_dls = []
    for z in Z_POINTS:
        r = (obs.dL_over_cH0[z] - ref.dL_over_cH0[z]) / ref.dL_over_cH0[z]
        r_dls.append(r)
    # Sum squares (q0 not included as a residual; it's a hard cut)
    return float(r_age * r_age + sum(rr * rr for rr in r_dls))


def main() -> None:
    ts = datetime.now(timezone.utc).isoformat()
    head = git_head(REPO_ROOT)

    # Reference ΛCDM-like backbone slice (fixed)
    om_ref = 0.30
    obs_ref = background_observables(om_ref)

    theta_grid = np.linspace(THETA_MIN, THETA_MAX, N_THETA)
    om_grid = np.linspace(OM_MIN, OM_MAX, N_OM)
    fb_grid = np.linspace(FB_MIN, FB_MAX, N_FB)

    failure_counts = {
        "q0_not_negative": 0,
        "age_outside_window": 0,
        "distance_outside_tolerance": 0,
        "growth_sigma8_outside_tolerance": 0,  # applied after reference selection
    }

    # First pass: background cuts only (plus store bg residuals)
    candidates: List[Dict[str, Any]] = []
    for theta in theta_grid:
        for om in om_grid:
            ol = 1.0 - om
            obs = background_observables(om)

            if not (obs.q0 < 0.0):
                failure_counts["q0_not_negative"] += len(fb_grid)
                continue

            if not (AGE_MIN_GYR <= obs.t0_gyr <= AGE_MAX_GYR):
                failure_counts["age_outside_window"] += len(fb_grid)
                continue

            # Distance residual cuts
            ok_dl = True
            for z in Z_POINTS:
                frac = abs(obs.dL_over_cH0[z] - obs_ref.dL_over_cH0[z]) / obs_ref.dL_over_cH0[z]
                if frac > DL_TOL_FRAC:
                    ok_dl = False
                    break
            if not ok_dl:
                failure_counts["distance_outside_tolerance"] += len(fb_grid)
                continue

            # For each fb, record bookkeeping; background doesn't depend on fb in this toy
            bg_metric = bg_residual_metric(obs, obs_ref)
            for fb in fb_grid:
                ob = fb * om
                oc = (1.0 - fb) * om
                candidates.append(
                    {
                        "theta_star": float(theta),
                        "Omega_m": float(om),
                        "Omega_Lambda": float(ol),
                        "f_b": float(fb),
                        "Omega_b": float(ob),
                        "Omega_c": float(oc),
                        "q0": float(obs.q0),
                        "t0_gyr": float(obs.t0_gyr),
                        "dL_over_cH0": {str(z): float(obs.dL_over_cH0[z]) for z in Z_POINTS},
                        "bg_metric": float(bg_metric),
                    }
                )

    # Choose reference model among background-accepted candidates
    if len(candidates) == 0:
        OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "schema_version": "act7.window.v1",
            "git_head": head,
            "timestamp_utc": ts,
            "contract": "docs/ACT_VII_MINI_CONTRACT.txt",
            "grid": {
                "theta_star": [THETA_MIN, THETA_MAX, N_THETA],
                "Omega_m": [OM_MIN, OM_MAX, N_OM],
                "f_b": [FB_MIN, FB_MAX, N_FB],
            },
            "reference": {
                "Omega_m_ref": om_ref,
                "Omega_Lambda_ref": 1.0 - om_ref,
                "t0_ref_gyr": obs_ref.t0_gyr,
                "dL_ref_over_cH0": {str(z): obs_ref.dL_over_cH0[z] for z in Z_POINTS},
            },
            "result": {
                "accepted_count": 0,
                "accepted_region_summary": None,
                "reason": "No points passed background cuts (q0/age/distance).",
                "failure_counts_background_pass": failure_counts,
            },
        }
        OUT_JSON.write_text(json.dumps(payload, indent=2))
        print(f"Wrote {OUT_JSON.relative_to(REPO_ROOT)} (EMPTY)")
        return

    ref_model = min(candidates, key=lambda d: d["bg_metric"])
    om_ref2 = ref_model["Omega_m"]
    # Growth reference uses only Omega_m in this toy model
    D_ref = growth_Drel_today(float(om_ref2))

    # Second pass: growth sigma8-like constraint
    accepted: List[Dict[str, Any]] = []
    for d in candidates:
        D = growth_Drel_today(float(d["Omega_m"]))
        R = D / D_ref
        if (R_SIGMA8_MIN <= R <= R_SIGMA8_MAX):
            d2 = dict(d)
            d2["D_rel_a1"] = float(D)
            d2["R_sigma8_like"] = float(R)
            accepted.append(d2)
        else:
            failure_counts["growth_sigma8_outside_tolerance"] += 1

    # Summaries
    def minmax(key: str) -> Tuple[float, float]:
        vals = [float(x[key]) for x in accepted]
        return (min(vals), max(vals))

    accepted_region = None
    if accepted:
        theta_lo, theta_hi = minmax("theta_star")
        om_lo, om_hi = minmax("Omega_m")
        fb_lo, fb_hi = minmax("f_b")
        accepted_region = {
            "theta_star_min": theta_lo,
            "theta_star_max": theta_hi,
            "Omega_m_min": om_lo,
            "Omega_m_max": om_hi,
            "f_b_min": fb_lo,
            "f_b_max": fb_hi,
        }

    payload = {
        "schema_version": "act7.window.v1",
        "git_head": head,
        "timestamp_utc": ts,
        "contract": "docs/ACT_VII_MINI_CONTRACT.txt",
        "grid": {
            "theta_star": [THETA_MIN, THETA_MAX, N_THETA],
            "Omega_m": [OM_MIN, OM_MAX, N_OM],
            "f_b": [FB_MIN, FB_MAX, N_FB],
        },
        "cuts": {
            "q0": "< 0",
            "t0_gyr": [AGE_MIN_GYR, AGE_MAX_GYR],
            "distance_frac_tol": DL_TOL_FRAC,
            "z_points": Z_POINTS,
            "R_sigma8_like": [R_SIGMA8_MIN, R_SIGMA8_MAX],
        },
        "reference": {
            "lcdm_backbone": {
                "Omega_m": om_ref,
                "Omega_Lambda": 1.0 - om_ref,
                "t0_ref_gyr": obs_ref.t0_gyr,
                "dL_ref_over_cH0": {str(z): obs_ref.dL_over_cH0[z] for z in Z_POINTS},
            },
            "act7_ref_model": {
                "definition": "accepted point with minimum bg_metric (sum of squared fractional residuals in age and dL)",
                "theta_star": ref_model["theta_star"],
                "Omega_m": ref_model["Omega_m"],
                "Omega_Lambda": ref_model["Omega_Lambda"],
                "f_b": ref_model["f_b"],
                "bg_metric": ref_model["bg_metric"],
                "D_rel_a1_ref": D_ref,
            },
        },
        "result": {
            "accepted_count": len(accepted),
            "candidate_count_after_background": len(candidates),
            "accepted_region_summary": accepted_region,
            "failure_counts_total": failure_counts,
        },
        # Keep accepted list bounded for git: store at most first 2000 points (deterministic order)
        "accepted_points_preview": accepted[:2000],
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, indent=2))
    print(f"Wrote {OUT_JSON.relative_to(REPO_ROOT)} (accepted={len(accepted)})")

    # -------------------------
    # Figures
    # -------------------------
    FIG_WINDOW.parent.mkdir(parents=True, exist_ok=True)
    FIG_SIGMA8.parent.mkdir(parents=True, exist_ok=True)

    # 1) Window plot: theta_star vs Omega_m (accepted points)
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(1, 1, 1)
    if accepted:
        th = [d["theta_star"] for d in accepted]
        om = [d["Omega_m"] for d in accepted]
        ax1.scatter(th, om, s=8)
    ax1.set_xlabel("theta_star (rad)")
    ax1.set_ylabel("Omega_m")
    ax1.set_title("Act VII accepted window: theta_star vs Omega_m")
    fig1.tight_layout()
    fig1.savefig(FIG_WINDOW, dpi=200)
    print(f"Wrote {FIG_WINDOW.relative_to(REPO_ROOT)}")

    # 2) Growth plot: R_sigma8_like vs theta_star (accepted points)
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(1, 1, 1)
    if accepted:
        th = [d["theta_star"] for d in accepted]
        rs = [d["R_sigma8_like"] for d in accepted]
        ax2.scatter(th, rs, s=8)
        ax2.axhline(R_SIGMA8_MIN, linestyle="--")
        ax2.axhline(R_SIGMA8_MAX, linestyle="--")
    ax2.set_xlabel("theta_star (rad)")
    ax2.set_ylabel("R_sigma8_like")
    ax2.set_title("Act VII growth sanity: R_sigma8_like vs theta_star")
    fig2.tight_layout()
    fig2.savefig(FIG_SIGMA8, dpi=200)
    print(f"Wrote {FIG_SIGMA8.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
