"""
run_frw_from_microcavity.py

Bridge between:
  - Act II theta★ prior (config/theta_star_config.json via theta_star_config.py)
  - 1D microcavity ΔE(θ★) scan (theta_star_microcavity_scan_full_2pi.npz)
  - simple FRW toy universe with matter + effective vacuum Ω_Λ(θ★).

This is NOT a precision cosmology tool. It is a conceptual wiring demo:
  theta★  --(microcavity ΔE)-->  effective Ω_Λ  --(FRW)-->  a(t) histories.
"""

from __future__ import annotations

import math
import os
from dataclasses import dataclass
from typing import Tuple

import numpy as np

from theta_star_config import load_theta_star_config


# --------------------------------------------------------------------------- #
# Small FRW helper: flat universe with matter + Λ, H0 = 1
# --------------------------------------------------------------------------- #

@dataclass
class FRWParams:
    omega_m: float
    omega_lambda: float
    a_init: float = 1e-3
    t_max: float = 5.0
    dt: float = 0.01


def integrate_frw(params: FRWParams) -> Tuple[np.ndarray, np.ndarray]:
    """
    Integrate a(t) for a flat FRW universe with Ω_m, Ω_Λ, H0 = 1.

    da/dt = H(a) * a
    H(a)^2 = Ω_m / a^3 + Ω_Λ
    """
    n_steps = int(params.t_max / params.dt) + 1
    t = np.linspace(0.0, params.t_max, n_steps)
    a = np.zeros_like(t)
    a[0] = params.a_init

    om = float(params.omega_m)
    ol = float(params.omega_lambda)

    for i in range(n_steps - 1):
        a_i = a[i]
        # Avoid numerical crashes if a → 0
        a_i = max(a_i, 1e-8)
        H_sq = om / (a_i ** 3) + ol
        H = math.sqrt(max(H_sq, 0.0))
        a[i + 1] = a_i + params.dt * H * a_i

    return t, a


# --------------------------------------------------------------------------- #
# Microcavity helper: load ΔE(θ★) scan over [0, 2π)
# --------------------------------------------------------------------------- #

@dataclass
class MicrocavityScan:
    theta: np.ndarray     # radians, over [0, 2π)
    deltaE: np.ndarray    # ΔE(θ) = E_cavity - E_uniform


def load_microcavity_scan(
    path: str = "data/processed/theta_star_microcavity_scan_full_2pi.npz",
) -> MicrocavityScan:
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Could not find microcavity scan file at {path}.\n"
            "Make sure you ran src/scan_1d_theta_star_microcavity_full_band.py first."
        )

    data = np.load(path, allow_pickle=True)
    files = list(data.files)

    # Try to be robust about key names
    theta_keys = ["theta_vals", "theta_grid", "theta", "theta_samples"]
    delta_keys = ["deltaE_vals", "deltaE", "delta_E", "deltaE_theta", "deltaE_values"]

    theta_arr = None
    for k in theta_keys:
        if k in data:
            theta_arr = np.asarray(data[k], dtype=float)
            break

    delta_arr = None
    for k in delta_keys:
        if k in data:
            delta_arr = np.asarray(data[k], dtype=float)
            break

    if theta_arr is None or delta_arr is None:
        raise KeyError(
            "Could not identify theta / deltaE arrays in "
            f"{path}. Available keys: {files}"
        )

    if theta_arr.shape != delta_arr.shape:
        raise ValueError(
            f"theta and deltaE have mismatched shapes: "
            f"{theta_arr.shape} vs {delta_arr.shape}"
        )

    return MicrocavityScan(theta=theta_arr, deltaE=delta_arr)


def interp_deltaE(scan: MicrocavityScan, theta: float) -> float:
    """
    Simple 1D interpolation of ΔE(θ) on [0, 2π).
    Wrap θ into [0, 2π) before interpolating.
    """
    tau = 2.0 * math.pi
    # wrap into [0, 2π)
    theta_wrapped = theta % tau

    # ensure theta grid is monotonically increasing over [0, 2π)
    theta_grid = np.asarray(scan.theta, dtype=float)
    deltaE = np.asarray(scan.deltaE, dtype=float)

    # If the grid is not sorted, sort it once.
    order = np.argsort(theta_grid)
    theta_sorted = theta_grid[order]
    delta_sorted = deltaE[order]

    # Handle periodicity: if first point != 0 or last != 2π, np.interp is still fine
    # as long as we stay within the range of theta_sorted.
    return float(np.interp(theta_wrapped, theta_sorted, delta_sorted))


# --------------------------------------------------------------------------- #
# Map ΔE -> Ω_Λ using a simple scaling based on fiducial θ★
# --------------------------------------------------------------------------- #

@dataclass
class MicrocavityToLambdaScaling:
    """
    Tiny record of how we map microcavity ΔE(θ★) to an effective Ω_Λ.

    This is intentionally simple: choose a scale so that the *fiducial* θ★
    corresponds to Ω_Λ,fid ≈ 0.7, then apply the same scale to other θ★.
    """

    k_scale: float          # Ω_Λ ≈ k_scale * ΔE
    deltaE_fid: float       # reference ΔE at fiducial θ★
    omega_lambda_fid: float # target Ω_Λ at fiducial θ★


def build_scaling_from_fiducial(
    scan: MicrocavityScan,
    theta_fid: float,
    omega_lambda_target: float = 0.7,
) -> MicrocavityToLambdaScaling:
    deltaE_fid = interp_deltaE(scan, theta_fid)

    if abs(deltaE_fid) < 1e-12:
        raise ValueError(
            f"Fiducial ΔE(θ_fid={theta_fid:.3f}) is ~0, cannot define scaling.\n"
            "Check the microcavity scan: perhaps the chosen parameters make ΔE almost flat."
        )

    k_scale = omega_lambda_target / deltaE_fid

    return MicrocavityToLambdaScaling(
        k_scale=k_scale,
        deltaE_fid=deltaE_fid,
        omega_lambda_fid=omega_lambda_target,
    )


def deltaE_to_omega_lambda(deltaE: float, scaling: MicrocavityToLambdaScaling) -> float:
    """
    Convert a microcavity ΔE into an effective Ω_Λ, with a simple clamp to [0, 1].
    """
    omega_lambda = scaling.k_scale * deltaE
    # enforce 0 <= Ω_Λ <= 1 for this toy model
    return float(max(0.0, min(1.0, omega_lambda)))


# --------------------------------------------------------------------------- #
# Main driver
# --------------------------------------------------------------------------- #

def main() -> None:
    print("=== FRW from microcavity ΔE(θ★) ===")

    # 1) Load Act II theta★ config
    cfg = load_theta_star_config()
    theta_fid = float(cfg.theta_star_fid_rad)
    theta_lo, theta_hi = cfg.theta_star_band_rad

    print("\n=== Act II theta★ configuration ===")
    print(f"  θ★_fid (rad) = {theta_fid:.6f}")
    print(f"  θ★ band (rad) = [{theta_lo:.6f}, {theta_hi:.6f}]")

    # 2) Load microcavity scan
    scan = load_microcavity_scan()
    print("\n=== Microcavity ΔE(θ★) scan ===")
    print(f"  loaded from: data/processed/theta_star_microcavity_scan_full_2pi.npz")
    print(f"  n_theta = {scan.theta.size}")
    print(f"  ΔE_min = {scan.deltaE.min(): .6e}")
    print(f"  ΔE_max = {scan.deltaE.max(): .6e}")

    # 3) Build ΔE -> Ω_Λ scaling from fiducial θ★
    scaling = build_scaling_from_fiducial(scan, theta_fid, omega_lambda_target=0.7)
    omega_lambda_fid = deltaE_to_omega_lambda(scaling.deltaE_fid, scaling)

    print("\n=== Scaling ΔE(θ★) -> Ω_Λ ===")
    print(f"  ΔE(θ★_fid)          = {scaling.deltaE_fid: .6e}")
    print(f"  chosen Ω_Λ,fid      = {scaling.omega_lambda_fid: .3f}")
    print(f"  resulting k_scale   = {scaling.k_scale: .6e}")
    print(f"  Ω_Λ(θ★_fid) after clamp = {omega_lambda_fid: .3f}")

    omega_m_fid = max(0.0, 1.0 - omega_lambda_fid)
    print(f"  Ω_m(θ★_fid)         = {omega_m_fid: .3f}")

    # 4) Integrate FRW for:
    #    - matter-only (Ω_m=1, Ω_Λ=0)
    #    - effective vacuum from microcavity at θ★_fid
    print("\n=== Integrating FRW histories ===")

    frw_matter = FRWParams(omega_m=1.0, omega_lambda=0.0, a_init=1e-3, t_max=5.0, dt=0.01)
    t_matter, a_matter = integrate_frw(frw_matter)
    print(f"  [matter_only] a(0) = {a_matter[0]:.3e}, a(t_final) = {a_matter[-1]:.3e}")

    frw_cavity = FRWParams(
        omega_m=omega_m_fid,
        omega_lambda=omega_lambda_fid,
        a_init=1e-3,
        t_max=5.0,
        dt=0.01,
    )
    t_cav, a_cav = integrate_frw(frw_cavity)
    print(
        f"  [microcavity] Ω_m = {omega_m_fid:.3f}, Ω_Λ = {omega_lambda_fid:.3f}, "
        f"a(0) = {a_cav[0]:.3e}, a(t_final) = {a_cav[-1]:.3e}"
    )

    # 5) Save everything to a single NPZ for later plotting or analysis
    os.makedirs("data/processed", exist_ok=True)
    out_path = "data/processed/frw_from_microcavity.npz"

    np.savez(
        out_path,
        theta_fid=theta_fid,
        theta_band=np.array([theta_lo, theta_hi]),
        theta_grid=scan.theta,
        deltaE_grid=scan.deltaE,
        deltaE_fid=scaling.deltaE_fid,
        k_scale=scaling.k_scale,
        omega_lambda_fid=omega_lambda_fid,
        omega_m_fid=omega_m_fid,
        t_matter_only=t_matter,
        a_matter_only=a_matter,
        t_microcavity=t_cav,
        a_microcavity=a_cav,
    )

    print(f"\nSaved FRW-from-microcavity results to {out_path}")
    print("You can inspect it later with, e.g.:")
    print('  PYTHONPATH=src python3 -c \'import numpy as np; d=np.load(')
    print('    "data/processed/frw_from_microcavity.npz"); print(d.files)\'')


if __name__ == "__main__":
    main()