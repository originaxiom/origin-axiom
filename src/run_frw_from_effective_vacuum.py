"""
run_frw_from_effective_vacuum.py

FRW toy universe driven by an "effective vacuum" model.

This script is the Act III version of the earlier demos:
  - instead of hard-coding Omega_Lambda,
  - we ask the EffectiveVacuumModel (backed by microcavity \u0394E(theta_star))
    for Omega_Lambda(theta_star), with theta_star coming from the Act II config.

In other words:
  theta_star (\u03B8\u2605) prior  -->  microcavity delta_E(theta_star)
  --> EffectiveVacuumModel         -->  FRW (a(t)) histories
"""

from __future__ import annotations

from pathlib import Path
from typing import Tuple

import numpy as np

from vacuum_effective import build_effective_vacuum_from_microcavity


def integrate_frw_flat(
    omega_m: float,
    omega_lambda: float,
    a_init: float = 1.0e-3,
    t_final: float = 5.0,
    n_steps: int = 1000,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Integrate a flat FRW model with matter + Lambda.

    Equation:
        (da/dt) = a * sqrt(omega_m * a^{-3} + omega_lambda)

    We use a simple RK4 integrator with H0 = 1 in code units.
    This is the same phenomenological level as the earlier FRW demos.
    """
    t = np.linspace(0.0, t_final, n_steps + 1)
    a = np.empty_like(t)
    a[0] = float(a_init)

    def H(a_val: float) -> float:
        return float(np.sqrt(omega_m * a_val ** (-3.0) + omega_lambda))

    for i in range(n_steps):
        dt = t[i + 1] - t[i]
        a_i = float(a[i])

        k1 = H(a_i) * a_i
        a_k2 = a_i + 0.5 * dt * k1
        k2 = H(a_k2) * a_k2

        a_k3 = a_i + 0.5 * dt * k2
        k3 = H(a_k3) * a_k3

        a_k4 = a_i + dt * k3
        k4 = H(a_k4) * a_k4

        a[i + 1] = a_i + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)

    return t, a


def main() -> None:
    print("=== FRW from Effective Vacuum (microcavity-backed) ===\n")

    # 1) Build the effective vacuum model based on current Act II config
    model = build_effective_vacuum_from_microcavity()
    print(model.summary())
    print("")

    theta_fid = model.cfg.theta_prior.theta_fid_rad
    theta_lo, theta_hi = model.cfg.theta_prior.theta_band_rad

    omega_lambda_fid = model.omega_lambda_of_theta(theta_fid)
    omega_m_fid = model.omega_m_of_theta(theta_fid)

    print("=== Effective cosmological parameters at fiducial theta_star ===")
    print(f"  theta_fid (rad)     = {theta_fid:.6f}")
    print(f"  Omega_Lambda(fid)   = {omega_lambda_fid:.3f}")
    print(f"  Omega_m(fid)        = {omega_m_fid:.3f}")
    print("")

    # 2) Integrate FRW histories
    a_init = 1.0e-3
    t_final = 5.0
    n_steps = 1000

    print("=== Integrating FRW histories ===")
    print("  [matter_only] Omega_m = 1.0, Omega_Lambda = 0.0")
    t_m, a_m = integrate_frw_flat(
        omega_m=1.0,
        omega_lambda=0.0,
        a_init=a_init,
        t_final=t_final,
        n_steps=n_steps,
    )
    print(f"    a(0)       = {a_m[0]:.3e}")
    print(f"    a(t_final) = {a_m[-1]:.3e}")

    print(f"\n  [effective] Omega_m = {omega_m_fid:.3f}, Omega_Lambda = {omega_lambda_fid:.3f}")
    t_eff, a_eff = integrate_frw_flat(
        omega_m=omega_m_fid,
        omega_lambda=omega_lambda_fid,
        a_init=a_init,
        t_final=t_final,
        n_steps=n_steps,
    )
    print(f"    a(0)       = {a_eff[0]:.3e}")
    print(f"    a(t_final) = {a_eff[-1]:.3e}")
    print("")

    # 3) Save results for plotting / paper
    out_dir = Path("data/processed")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "frw_from_effective_vacuum.npz"

    np.savez(
        out_path,
        t_matter_only=t_m,
        a_matter_only=a_m,
        t_effective=t_eff,
        a_effective=a_eff,
        theta_fid=float(theta_fid),
        theta_band=np.array([theta_lo, theta_hi], dtype=float),
        omega_lambda_fid=float(omega_lambda_fid),
        omega_m_fid=float(omega_m_fid),
        k_scale=float(model.cfg.k_scale),
    )

    print(f"Saved FRW-from-effective-vacuum results to {out_path}")
    print("You can inspect them later with, e.g.:")
    print(
        '  PYTHONPATH=src python3 -c \'import numpy as np; '
        'd=np.load("data/processed/frw_from_effective_vacuum.npz"); '
        'print(d.files)\''
    )


if __name__ == "__main__":
    main()