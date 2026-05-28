"""
B7 -- Fisher-KPP creation wave. SPECULATIVE FRONTIER (GOVERNANCE.md sec. 5).

Gradient flow of the derived potential (P16) is a Fisher-KPP reaction-diffusion
equation with reaction f(tau) = 1 + tau - tau^2. A seed near tau=0 spreads as a
travelling wave converting tau=0 (unstable) to tau=phi (stable vacuum).

CAVEAT: this is the dissipative gradient flow, not the wave equation; D is
inserted; the "creation spreading" reading is suggestive, not derived.

Run:  python frontier/B7_fisher_kpp_creation/probe.py
"""

import numpy as np
from scipy.constants import golden_ratio as phi


def run(N=500, L=60.0, D=1.0, steps=8000, seed_amp=0.3):
    dx = L / N
    dt = 0.2 * dx**2 / (2 * D)
    x = np.linspace(-L / 2, L / 2, N)
    tau = seed_amp * np.exp(-x**2 / 2.0)  # small seed near tau = 0
    for _ in range(steps):
        reaction = 1 + tau - tau**2          # = -V'(tau)/kappa  (P16)
        lap = np.zeros_like(tau)
        lap[1:-1] = (tau[2:] - 2 * tau[1:-1] + tau[:-2]) / dx**2
        tau = tau + dt * (reaction + D * lap)
    return tau, D


def main():
    print("=" * 72)
    print("B7 -- Fisher-KPP creation wave (SPECULATIVE; not a claim)")
    print("=" * 72)
    tau, D = run()
    avg = float(np.mean(tau))
    err = abs(avg - phi)
    print(f"\n  reaction f(tau) = 1 + tau - tau^2,  f(0)=1>0, f(phi)=0")
    print(f"  final <tau>      = {avg:.10f}")
    print(f"  |<tau> - phi|    = {err:.2e}")
    print(f"  Fisher-KPP speed = 2*sqrt(D*f'(0)) = 2*sqrt(D) = {2*np.sqrt(D):.4f}")
    assert err < 1e-6, f"did not converge to phi: {err}"
    print("\n  PASS: field converges from a seed at zero to the golden vacuum.")
    print("\n[verdict] STALLED: reaction term is exact (P16); the reaction-diffusion")
    print("dynamics and D are inserted. See FINDINGS.md.")


if __name__ == "__main__":
    main()
