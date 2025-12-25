#!/usr/bin/env python3
"""
Act VIII / Gate 3 (CALCS): theta-star injected cosmology scan (Model B: vacuum running)
Option A: include a tunable sensitivity kappa and run several kappas in one run.

Model:
  rho_DE(a) = rho_DE0 * a^{-nu(theta)}
  nu(theta) = (kappa * nu0) * (theta - theta_best) / DeltaTheta

where DeltaTheta = theta_max - theta_min of the Gate-1 overlap corridor,
so nu0 is "per-corridor" amplitude and kappa is an extra strength knob.

Scan:
  theta_star in [2.432, 3.860]  (Gate 1 overlap)
  Omega_m in [0.20, 0.40]
  nu0 in a small discrete set
  kappa in [1, 3, 10]  (Option A)

Flatness at z=0:
  Omega_DE0 = 1 - Omega_m

Compute:
  - q0
  - age t0
  - dL(z)/(c/H0) at z={0.3,0.5,1.0}
  - growth D(a=1) (simple ODE)
  - R_sigma8_like = D/D_ref within each (kappa,nu0) slice

Outputs per kappa:
  - data/processed/act8_k{K}_theta_injected_frw_growth_scan.npz
  - data/processed/act8_k{K}_theta_injected_corridor_summary.json
  - figures/act8_k{K}_theta_injected_corridor.png
  - figures/act8_k{K}_theta_injected_growth.png
"""

from __future__ import annotations

import json
import math
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

import numpy as np
import matplotlib.pyplot as plt


REPO_ROOT = Path(__file__).resolve().parents[1]

# Inputs from existing pipeline
BKG_SUMMARY = REPO_ROOT / "data/processed/theta_star_lcdm_background_corridor_plot_summary.json"

# -------------------------
# Scan / cut constants
# -------------------------
THETA_MIN = 2.4320
THETA_MAX = 3.8600
OM_MIN = 0.20
OM_MAX = 0.40

N_THETA = 25
N_OM = 21

NU0_LIST = [-0.05, -0.02, 0.0, 0.02, 0.05]
KAPPA_LIST = [1.0, 3.0, 10.0]

H0_KM_S_MPC = 70.0

AGE_MIN_GYR = 12.0
AGE_MAX_GYR = 15.0
DL_TOL_FRAC = 0.05
R_SIGMA8_MIN = 0.92
R_SIGMA8_MAX = 1.08
Z_POINTS = [0.3, 0.5, 1.0]

OM_REF_LCDM = 0.30  # baseline reference

# SI constants for age
MPC_M = 3.0856775814913673e22
KM_M = 1e3
SEC_PER_GYR = 3600 * 24 * 365.25 * 1e9


@dataclass(frozen=True)
class Obs:
    q0: float
    t0_gyr: float
    dL_over_cH0: Dict[float, float]


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


def H0_si() -> float:
    return H0_KM_S_MPC * KM_M / MPC_M


def nu_of_theta(theta: float, theta_best: float, nu0: float, kappa: float, delta_theta: float) -> float:
    # normalized by corridor width so nu0 is "per corridor" amplitude
    if delta_theta <= 0:
        raise ValueError("delta_theta must be > 0")
    return float((kappa * nu0) * (theta - theta_best) / delta_theta)


def E2_of_a(a: np.ndarray, om: float, ode0: float, nu: float) -> np.ndarray:
    # E^2(a) = Omega_m a^-3 + Omega_DE0 a^-nu
    return om / (a**3) + ode0 * (a ** (-nu))


def E_of_a(a: np.ndarray, om: float, ode0: float, nu: float) -> np.ndarray:
    return np.sqrt(E2_of_a(a, om, ode0, nu))


def E_of_z(z: np.ndarray, om: float, ode0: float, nu: float) -> np.ndarray:
    # a^-3 = (1+z)^3, a^-nu = (1+z)^nu
    return np.sqrt(om * (1.0 + z) ** 3 + ode0 * (1.0 + z) ** nu)


def q0_modelB(om: float, ode0: float, nu: float) -> float:
    """
    rho_DE ~ a^{-nu} => effective constant w = -1 + nu/3
    q0 = 0.5*Omega_m + 0.5*(1+3w)*Omega_DE0 = 0.5*om + 0.5*(-2+nu)*ode0
    """
    return 0.5 * om + 0.5 * (-2.0 + nu) * ode0


def age_t0_gyr(om: float, ode0: float, nu: float) -> float:
    a = np.linspace(1e-6, 1.0, 25000)
    integrand = 1.0 / (a * E_of_a(a, om, ode0, nu))
    t0_over_H0 = np.trapezoid(integrand, a)
    t0_sec = t0_over_H0 / H0_si()
    return float(t0_sec / SEC_PER_GYR)


def comoving_chi_over_cH0(zmax: float, om: float, ode0: float, nu: float) -> float:
    z = np.linspace(0.0, zmax, 9000)
    Ez = E_of_z(z, om, ode0, nu)
    return float(np.trapezoid(1.0 / Ez, z))


def dL_over_cH0(z: float, om: float, ode0: float, nu: float) -> float:
    return (1.0 + z) * comoving_chi_over_cH0(z, om, ode0, nu)


def observables(om: float, theta: float, theta_best: float, nu0: float, kappa: float, delta_theta: float) -> Obs:
    ode0 = 1.0 - om
    nu = nu_of_theta(theta, theta_best, nu0, kappa, delta_theta)
    q0 = q0_modelB(om, ode0, nu)
    t0 = age_t0_gyr(om, ode0, nu)
    dls = {z: dL_over_cH0(z, om, ode0, nu) for z in Z_POINTS}
    return Obs(q0=q0, t0_gyr=t0, dL_over_cH0=dls)


def growth_D_today(om: float, ode0: float, nu: float) -> float:
    """
    D'' + [3/a + d ln E/da] D' - (3/2) * Omega_m0/(a^5 E^2) * D = 0
    with D(a_i)=a_i, D'(a_i)=1
    """
    a_i = 1e-3
    a_f = 1.0
    n = 9000
    a = np.linspace(a_i, a_f, n)

    E = E_of_a(a, om, ode0, nu)
    dE_da = np.gradient(E, a)
    dlnE_da = dE_da / E

    D = np.zeros_like(a)
    V = np.zeros_like(a)
    D[0] = a_i
    V[0] = 1.0

    for i in range(n - 1):
        ai = a[i]
        Ei = E[i]
        dlnEi = dlnE_da[i]

        def fD(_D: float, _V: float) -> float:
            return _V

        def fV(_D: float, _V: float) -> float:
            term_grav = 1.5 * om / (ai**5 * (Ei**2)) * _D
            term_fric = (3.0 / ai + dlnEi) * _V
            return term_grav - term_fric

        da = a[i + 1] - ai

        k1D = fD(D[i], V[i])
        k1V = fV(D[i], V[i])

        Dm = D[i] + 0.5 * da * k1D
        Vm = V[i] + 0.5 * da * k1V

        am = ai + 0.5 * da
        Em = math.sqrt(om / (am**3) + ode0 * (am ** (-nu)))
        eps = 1e-6
        Ep = math.sqrt(om / ((am + eps) ** 3) + ode0 * ((am + eps) ** (-nu)))
        Emm = math.sqrt(om / ((am - eps) ** 3) + ode0 * ((am - eps) ** (-nu)))
        dlnEm = (Ep - Emm) / (2 * eps) / Em

        def fVmid(_D: float, _V: float) -> float:
            term_grav = 1.5 * om / (am**5 * (Em**2)) * _D
            term_fric = (3.0 / am + dlnEm) * _V
            return term_grav - term_fric

        k2D = Vm
        k2V = fVmid(Dm, Vm)

        D[i + 1] = D[i] + da * k2D
        V[i + 1] = V[i] + da * k2V

    return float(D[-1])


def bg_metric(obs: Obs, ref: Obs) -> float:
    r_age = (obs.t0_gyr - ref.t0_gyr) / ref.t0_gyr
    r_d = 0.0
    for z in Z_POINTS:
        rr = (obs.dL_over_cH0[z] - ref.dL_over_cH0[z]) / ref.dL_over_cH0[z]
        r_d += rr * rr
    return float(r_age * r_age + r_d)


def run_one_kappa(kappa: float) -> None:
    ts = datetime.now(timezone.utc).isoformat()
    head = git_head(REPO_ROOT)

    d_bkg = load_json(BKG_SUMMARY)
    theta_best = float(d_bkg.get("theta_best"))
    theta_corr = d_bkg.get("theta_corridor", None)

    delta_theta = float(THETA_MAX - THETA_MIN)

    theta_grid = np.linspace(THETA_MIN, THETA_MAX, N_THETA)
    om_grid = np.linspace(OM_MIN, OM_MAX, N_OM)

    # Reference LCDM-like baseline (nu=0)
    ref_obs = observables(OM_REF_LCDM, theta_best, theta_best, nu0=0.0, kappa=kappa, delta_theta=delta_theta)

    n_nu0 = len(NU0_LIST)

    q0_arr = np.full((n_nu0, N_THETA, N_OM), np.nan)
    t0_arr = np.full((n_nu0, N_THETA, N_OM), np.nan)
    dl_arr = np.full((n_nu0, N_THETA, N_OM, len(Z_POINTS)), np.nan)
    D_arr = np.full((n_nu0, N_THETA, N_OM), np.nan)
    bgm_arr = np.full((n_nu0, N_THETA, N_OM), np.nan)
    accept_bg = np.zeros((n_nu0, N_THETA, N_OM), dtype=bool)
    accept_all = np.zeros((n_nu0, N_THETA, N_OM), dtype=bool)
    Rsig_arr = np.full((n_nu0, N_THETA, N_OM), np.nan)
    nu_arr = np.full((n_nu0, N_THETA), np.nan)

    summary: Dict[str, Any] = {
        "schema_version": "act8.injected_scan.v2",
        "git_head": head,
        "timestamp_utc": ts,
        "kappa": float(kappa),
        "inputs": {"theta_best_from": str(BKG_SUMMARY.relative_to(REPO_ROOT))},
        "theta_best": theta_best,
        "theta_corridor_from_R23": theta_corr,
        "grid": {
            "theta_star": [THETA_MIN, THETA_MAX, N_THETA],
            "Omega_m": [OM_MIN, OM_MAX, N_OM],
            "nu0_list": NU0_LIST,
            "DeltaTheta": delta_theta,
        },
        "cuts": {
            "q0": "< 0",
            "t0_gyr": [AGE_MIN_GYR, AGE_MAX_GYR],
            "distance_frac_tol": DL_TOL_FRAC,
            "z_points": Z_POINTS,
            "R_sigma8_like": [R_SIGMA8_MIN, R_SIGMA8_MAX],
        },
        "per_nu0": [],
    }

    for inu, nu0 in enumerate(NU0_LIST):
        for it, theta in enumerate(theta_grid):
            nu_arr[inu, it] = nu_of_theta(float(theta), theta_best, float(nu0), float(kappa), delta_theta)

        for it, theta in enumerate(theta_grid):
            for io, om in enumerate(om_grid):
                omf = float(om)
                ode0 = 1.0 - omf
                nu = nu_of_theta(float(theta), theta_best, float(nu0), float(kappa), delta_theta)

                ob = observables(omf, float(theta), theta_best, float(nu0), float(kappa), delta_theta)
                q0_arr[inu, it, io] = ob.q0
                t0_arr[inu, it, io] = ob.t0_gyr
                for iz, z in enumerate(Z_POINTS):
                    dl_arr[inu, it, io, iz] = ob.dL_over_cH0[z]

                bgm = bg_metric(ob, ref_obs)
                bgm_arr[inu, it, io] = bgm

                # background cuts
                if not (ob.q0 < 0.0):
                    continue
                if not (AGE_MIN_GYR <= ob.t0_gyr <= AGE_MAX_GYR):
                    continue
                ok_dl = True
                for z in Z_POINTS:
                    frac = abs(ob.dL_over_cH0[z] - ref_obs.dL_over_cH0[z]) / ref_obs.dL_over_cH0[z]
                    if frac > DL_TOL_FRAC:
                        ok_dl = False
                        break
                if not ok_dl:
                    continue

                accept_bg[inu, it, io] = True
                D_arr[inu, it, io] = growth_D_today(omf, ode0, nu)

        mask = accept_bg[inu]
        if not np.any(mask):
            summary["per_nu0"].append({"nu0": float(nu0), "bg_accepted": 0, "all_accepted": 0, "note": "No bg points."})
            continue

        idxs = np.argwhere(mask)
        best = None
        best_val = None
        for (it, io) in idxs:
            v = float(bgm_arr[inu, it, io])
            if best_val is None or v < best_val:
                best_val = v
                best = (int(it), int(io))

        itb, iob = best
        theta_ref = float(theta_grid[itb])
        om_ref = float(om_grid[iob])
        ode_ref = 1.0 - om_ref
        nu_ref = nu_of_theta(theta_ref, theta_best, float(nu0), float(kappa), delta_theta)
        D_ref = float(D_arr[inu, itb, iob])

        bg_count = int(np.sum(mask))
        all_count = 0

        for (it, io) in idxs:
            D = float(D_arr[inu, it, io])
            R = D / D_ref if D_ref != 0 else np.nan
            Rsig_arr[inu, it, io] = R
            if np.isfinite(R) and (R_SIGMA8_MIN <= R <= R_SIGMA8_MAX):
                accept_all[inu, it, io] = True
                all_count += 1

        def ranges(m: np.ndarray) -> Dict[str, float] | None:
            if not np.any(m):
                return None
            pts = np.argwhere(m)
            thetas = [float(theta_grid[it]) for it, _ in pts]
            oms = [float(om_grid[io]) for _, io in pts]
            return {
                "theta_min": float(min(thetas)),
                "theta_max": float(max(thetas)),
                "Omega_m_min": float(min(oms)),
                "Omega_m_max": float(max(oms)),
            }

        summary["per_nu0"].append(
            {
                "nu0": float(nu0),
                "bg_accepted": bg_count,
                "all_accepted": all_count,
                "ref_point": {
                    "theta_star": theta_ref,
                    "Omega_m": om_ref,
                    "nu(theta_ref)": float(nu_ref),
                    "bg_metric": float(best_val),
                    "D_ref": float(D_ref),
                },
                "accepted_ranges": ranges(accept_all[inu]),
            }
        )

    # Outputs (per kappa)
    tag = f"k{int(kappa)}"
    out_npz = REPO_ROOT / f"data/processed/act8_{tag}_theta_injected_frw_growth_scan.npz"
    out_json = REPO_ROOT / f"data/processed/act8_{tag}_theta_injected_corridor_summary.json"
    fig_corr = REPO_ROOT / f"figures/act8_{tag}_theta_injected_corridor.png"
    fig_grow = REPO_ROOT / f"figures/act8_{tag}_theta_injected_growth.png"

    out_npz.parent.mkdir(parents=True, exist_ok=True)
    np.savez(
        out_npz,
        theta_grid=theta_grid,
        omega_m_grid=om_grid,
        nu0_list=np.array(NU0_LIST, dtype=float),
        kappa=float(kappa),
        delta_theta=float(delta_theta),
        nu_theta=nu_arr,
        q0=q0_arr,
        t0_gyr=t0_arr,
        dL_over_cH0=dl_arr,
        D_today=D_arr,
        bg_metric=bgm_arr,
        accept_bg=accept_bg,
        accept_all=accept_all,
        R_sigma8_like=Rsig_arr,
        theta_best=theta_best,
    )
    print(f"Wrote {out_npz.relative_to(REPO_ROOT)}")

    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(summary, indent=2))
    print(f"Wrote {out_json.relative_to(REPO_ROOT)}")

    # Figures
    fig_corr.parent.mkdir(parents=True, exist_ok=True)
    fig_grow.parent.mkdir(parents=True, exist_ok=True)

    fig1 = plt.figure(figsize=(10, 6))
    ncol = 3
    nrow = int(math.ceil(len(NU0_LIST) / ncol))

    for i, nu0 in enumerate(NU0_LIST):
        ax = fig1.add_subplot(nrow, ncol, i + 1)
        m = accept_all[i]
        if np.any(m):
            pts = np.argwhere(m)
            th = [theta_grid[it] for it, _ in pts]
            om = [om_grid[io] for _, io in pts]
            ax.scatter(th, om, s=8)
        ax.set_title(f"nu0={nu0:+.3f}")
        ax.set_xlabel("theta_star")
        ax.set_ylabel("Omega_m")
        ax.set_xlim(THETA_MIN, THETA_MAX)
        ax.set_ylim(OM_MIN, OM_MAX)

    fig1.suptitle(f"Act VIII (Model B, Option A): accepted window (kappa={kappa:g})")
    fig1.tight_layout()
    fig1.savefig(fig_corr, dpi=200)
    print(f"Wrote {fig_corr.relative_to(REPO_ROOT)}")

    fig2 = plt.figure(figsize=(10, 6))
    ax2 = fig2.add_subplot(1, 1, 1)

    for i, nu0 in enumerate(NU0_LIST):
        m = accept_all[i]
        if not np.any(m):
            continue
        pts = np.argwhere(m)
        th = np.array([theta_grid[it] for it, _ in pts], dtype=float)
        rs = np.array([Rsig_arr[i, it, io] for it, io in pts], dtype=float)
        ax2.scatter(th, rs, s=8, label=f"nu0={nu0:+.3f}")

    ax2.axhline(R_SIGMA8_MIN, linestyle="--")
    ax2.axhline(R_SIGMA8_MAX, linestyle="--")
    ax2.set_xlabel("theta_star")
    ax2.set_ylabel("R_sigma8_like")
    ax2.set_title(f"Act VIII (Model B, Option A): growth sanity (kappa={kappa:g})")
    ax2.legend()
    fig2.tight_layout()
    fig2.savefig(fig_grow, dpi=200)
    print(f"Wrote {fig_grow.relative_to(REPO_ROOT)}")


def main() -> None:
    for kappa in KAPPA_LIST:
        run_one_kappa(float(kappa))


if __name__ == "__main__":
    main()
