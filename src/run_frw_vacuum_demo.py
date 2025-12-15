#!/usr/bin/env python3
"""
run_frw_vacuum_demo.py

Goal
----
Tiny FRW toy universe with:
  - pressureless matter (Ω_m),
  - an effective vacuum component (Ω_Λ),

so we can see:
  - how the scale factor a(t) behaves with and without a vacuum term,
  - where a θ★-driven vacuum component would slot in conceptually.

This is deliberately minimal and uses only NumPy, no SciPy.

Notes on relation to Origin Axiom
---------------------------------
- In Act II, origin-axiom-theta-star gives us a θ★ posterior and a band
  [θ_lo, θ_hi] with fiducial θ_fid.
- In origin-axiom, our 1D microcavity scripts show that ΔE(θ★) has
  a minimum near θ ≈ π, and that ΔE(θ_fid) is close to that minimum.
- Here, we do NOT yet try to calibrate the absolute scale of ΔE(θ★)
  to the observed cosmological constant. We simply treat Ω_Λ as a
  tunable parameter that *will later* be derived from the microcavity
  sector once we decide on units and coarse-graining.

Usage
-----
PYTHONPATH=src python3 src/run_frw_vacuum_demo.py
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

import numpy as np


@dataclass
class FRWParams:
    """
    Simple flat FRW with matter + vacuum.

    All quantities are dimensionless:
      - we set H0 = 1 in our units,
      - time t is in units of H0^{-1},
      - a(t=0) is some small initial scale factor.
    """
    Omega_m: float = 0.3   # "matter" fraction
    Omega_L: float = 0.7   # "vacuum" fraction (effective Λ)
    a_init: float = 1e-3   # starting scale factor (early universe)
    t_final: float = 5.0   # final time in H0^{-1} units
    n_steps: int = 2000    # integration steps


def _frw_rhs(a: float, Omega_m: float, Omega_L: float) -> float:
    """
    da/dt = a * H(a) with
      H^2(a) = H0^2 [ Ω_m a^{-3} + Ω_Λ ]  (flat, no radiation).

    We set H0 = 1 in these units.
    """
    # Avoid division issues when a is tiny
    a_safe = max(a, 1e-12)
    H_sq = Omega_m / (a_safe ** 3) + Omega_L
    if H_sq < 0.0:
        # Shouldn't happen for positive Ω_m, Ω_Λ, but guard anyway
        H_sq = 0.0
    H = np.sqrt(H_sq)
    return a_safe * H


def integrate_frw(params: FRWParams) -> Tuple[np.ndarray, np.ndarray]:
    """
    Integrate the FRW equation with a simple explicit scheme.

    Returns
    -------
    t : array, shape (n_steps + 1,)
        Time samples.
    a : array, shape (n_steps + 1,)
        Scale factor samples.
    """
    t0 = 0.0
    t1 = params.t_final
    N = params.n_steps

    t = np.linspace(t0, t1, N + 1)
    dt = t[1] - t[0]

    a = np.empty_like(t)
    a[0] = params.a_init

    for i in range(N):
        # Simple RK2 (midpoint) for better stability than pure Euler
        k1 = _frw_rhs(a[i], params.Omega_m, params.Omega_L)
        a_mid = a[i] + 0.5 * dt * k1
        k2 = _frw_rhs(a_mid, params.Omega_m, params.Omega_L)
        a[i + 1] = a[i] + dt * k2

    return t, a


def main() -> None:
    # ------------------------------------------------------------------
    # 1) Define a few scenarios: no vacuum vs vacuum-dominated
    # ------------------------------------------------------------------
    cases = {
        "matter_only": FRWParams(Omega_m=1.0, Omega_L=0.0),
        "lambda_30":   FRWParams(Omega_m=0.7, Omega_L=0.3),
        "lambda_70":   FRWParams(Omega_m=0.3, Omega_L=0.7),
    }

    print("=== FRW toy universe with matter + vacuum ===")
    print("All units are dimensionless with H0 = 1.")
    print("We integrate from a_init ≪ 1 up to t ~ few H0^{-1}.\n")

    results = {}

    for name, cfg in cases.items():
        t, a = integrate_frw(cfg)
        results[name] = (t, a)

        # Rough "doubling time" of the scale factor, just for intuition
        a0 = a[0]
        a2 = 2.0 * a0
        idx = np.where(a >= a2)[0]
        if idx.size > 0:
            t_double = t[idx[0]]
        else:
            t_double = np.nan

        print(f"[{name}] Ω_m = {cfg.Omega_m:.3f}, Ω_Λ = {cfg.Omega_L:.3f}")
        print(f"  a(0)       = {a0:.3e}")
        print(f"  a(t_final) = {a[-1]:.3e}")
        if np.isfinite(t_double):
            print(f"  t at which a ≈ 2 a_init: t ≈ {t_double:.3f}")
        else:
            print("  a never reached 2 a_init within this integration window.")
        print()

    # ------------------------------------------------------------------
    # 2) Save results for later plotting / analysis
    # ------------------------------------------------------------------
    out_path = "data/processed/frw_vacuum_demo.npz"
    np.savez(
        out_path,
        t_matter_only=results["matter_only"][0],
        a_matter_only=results["matter_only"][1],
        t_lambda_30=results["lambda_30"][0],
        a_lambda_30=results["lambda_30"][1],
        t_lambda_70=results["lambda_70"][0],
        a_lambda_70=results["lambda_70"][1],
    )
    print(f"Saved FRW toy results to {out_path}")
    print("\nYou can inspect them later with, e.g.:")
    print(
        "  PYTHONPATH=src python3 -c 'import numpy as np; d=np.load("
        "\"data/processed/frw_vacuum_demo.npz\"); print(d.files)'"
    )
    print()
    print("Conceptual mapping to our axiom:")
    print("  - Ω_Λ here stands in for a coarse-grained vacuum component.")
    print("  - In a later step, we will tie Ω_Λ to the microcavity ΔE(θ★)")
    print("    and the non-cancelling rule, using the Act II θ★ prior band.")


if __name__ == "__main__":
    main()