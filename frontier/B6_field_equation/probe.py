"""
B6 -- derived field equation. SPECULATIVE FRONTIER (GOVERNANCE.md sec. 5).

Confirms that the Euler-Lagrange equation of L = (1/2)(d tau)^2 - V(tau), with the
DERIVED potential V (P16), is exactly  box tau + kappa*(tau^2 - tau - 1) = 0.

This is a consistency check on the standard potential->field-theory promotion,
NOT a derivation of the field theory. The kinetic term is a choice (see README).

Run:  python frontier/B6_field_equation/probe.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

import sympy as sp

from origin_axiom.constants import PHI
from origin_axiom.mobius import KAPPA, potential, potential_derivative, tau


def main():
    print("=" * 72)
    print("B6 -- derived field equation (SPECULATIVE; not a claim)")
    print("=" * 72)

    # Euler-Lagrange for L = (1/2)(d tau)^2 - V(tau) is:  box tau + dV/dtau = 0.
    dV = sp.diff(potential(), tau)
    golden = KAPPA * (tau**2 - tau - 1)
    print(f"\n  dV/dtau            = {sp.simplify(dV)}")
    print(f"  kappa*(t^2-t-1)    = {sp.simplify(golden)}")
    assert sp.simplify(dV - golden) == 0
    print("  => EL eq: box tau + kappa*(tau^2 - tau - 1) = 0   [exact]")

    # The two fixed points are the constant (homogeneous) solutions.
    print(f"\n  Constant solutions (box tau = 0): dV/dtau = 0")
    print(f"    tau = phi      : dV/dtau = {sp.simplify(potential_derivative(PHI))}  (stable vacuum)")
    print(f"    tau = -1/phi   : dV/dtau = {sp.simplify(potential_derivative(-1/PHI))}  (unstable)")
    print(f"    tau = 0        : dV/dtau = {sp.simplify(potential_derivative(0))} = -kappa != 0  (NOT a solution)")

    print("\n[verdict] STALLED at the field-theory bridge: V is derived (P16);")
    print("the kinetic term / dimension / field interpretation are inserted.")
    print("See FINDINGS.md.")


if __name__ == "__main__":
    main()
