"""
B8 -- particle spectrum around the golden vacuum. SPECULATIVE (GOVERNANCE.md sec. 5).

Expanding tau = phi + eps in the B6 field equation gives a massive scalar with
cubic self-interaction. mass^2 = kappa*sqrt(5) is exact (P16). The ratio
m/g = sqrt(5/(4 log phi)) is exact but is NOT phi -- an honest near-miss that
must NOT be inflated.

Run:  python frontier/B8_particle_spectrum/probe.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

import sympy as sp

from origin_axiom.constants import PHI
from origin_axiom.mobius import KAPPA, mass_squared


def main():
    print("=" * 72)
    print("B8 -- particle spectrum (SPECULATIVE; near-miss NOT a claim)")
    print("=" * 72)

    m2 = mass_squared()              # kappa*sqrt(5)  -- exact (P16)
    m = sp.sqrt(m2)
    g = KAPPA
    ratio = m / g
    ratio_closed = sp.sqrt(5 / (4 * sp.log(PHI)))

    print(f"\n  mass^2 = V''(phi) = kappa*sqrt(5) = {float(m2):.6f}   [exact, P16]")
    print(f"  mass            = {float(m):.6f}")
    print(f"  coupling g = kappa = {float(g):.6f}")
    print(f"  m/g             = {float(ratio):.6f}")
    print(f"  closed form     = sqrt(5/(4 log phi)) = {float(ratio_closed):.10f}")
    # confirm the closed form equals m/g
    assert abs(float(ratio) - float(ratio_closed)) < 1e-12
    print(f"  phi             = {float(PHI):.6f}")
    print(f"  |m/g - phi|     = {abs(float(ratio) - float(PHI)):.6f}   <-- NEAR-MISS, not phi")

    print("\n[verdict] STALLED. mass^2 and coupling are exact functions of kappa;")
    print("their reading as a PARTICLE spectrum needs the inserted 1+1 field theory")
    print("(B6). The m/g ~ phi near-miss is recorded and explicitly NOT promoted.")
    print("See FINDINGS.md.")


if __name__ == "__main__":
    main()
