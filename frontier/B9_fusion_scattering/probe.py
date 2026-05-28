"""
B9 -- fusion-scattering correspondence. SPECULATIVE (GOVERNANCE.md sec. 5).

The cubic vertex (eps^2 term in expanding V(phi+eps)) and the Fibonacci fusion
rule tau x tau = 1 + tau both rest on tau^2 - tau - 1. This probe records the
SHARED POLYNOMIAL -- not a derived equivalence (see README caveat).

Run:  python frontier/B9_fusion_scattering/probe.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

import sympy as sp

from origin_axiom.constants import PHI
from origin_axiom.mobius import KAPPA, potential, tau

eps = sp.symbols("epsilon")


def main():
    print("=" * 72)
    print("B9 -- fusion-scattering correspondence (SPECULATIVE; not a claim)")
    print("=" * 72)

    # (1) Fusion rule tau x tau = 1 + tau  ->  tau^2 - tau - 1 = 0  (P2, exact).
    fusion = tau**2 - (1 + tau)
    print(f"\n  Fibonacci fusion: tau x tau = 1 + tau  =>  {sp.expand(fusion)} = 0   [P2, exact]")

    # (2) Cubic vertex from expanding V(phi + eps) about the minimum.
    Vexp = sp.expand(potential(PHI + eps))
    Vseries = sp.series(potential(PHI + eps), eps, 0, 4).removeO()
    cubic_coeff = sp.simplify(Vseries.coeff(eps, 3))
    quad_coeff = sp.simplify(Vseries.coeff(eps, 2))
    print(f"\n  V(phi+eps) expanded around the minimum:")
    print(f"    quadratic coeff (eps^2): {quad_coeff}  = (1/2) m^2 = (1/2) kappa sqrt(5)")
    print(f"    cubic coeff     (eps^3): {cubic_coeff}  = kappa/3  (the 2<->1 vertex)")
    assert sp.simplify(cubic_coeff - KAPPA / 3) == 0

    # Both rest on the same polynomial.
    print(f"\n  Shared structure: both the fusion rule and the vertex rest on")
    print(f"  tau^2 - tau - 1 (the golden polynomial; P2 and P16 -- 'six faces').")

    print("\n[verdict] STALLED. Shared polynomial, NOT a rigorous fusion<->scattering")
    print("map. The fusion category is exact algebra; the cubic vertex is an artifact")
    print("of the inserted field theory (B6). See FINDINGS.md.")


if __name__ == "__main__":
    main()
