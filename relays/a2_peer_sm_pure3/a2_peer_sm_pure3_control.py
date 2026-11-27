#!/usr/bin/env python3
"""
Standalone Failing Control for Card A2-PEER-SM-PURE3 (seat fam3-v1-high-03).

Tests 3 independent corruptions (one per verified card):
  C1 (SM-R384): Claiming K = {(2/5, odd/10)} is closed under unit multiplication u = 3 mod 10.
  C2 (SM-R614): Using wrong sign eta_bad = (3*chi + 5*psi)/4 and claiming nu^c and N have equal charge.
  C3 (SM-R635): Replacing Q_8 by the trivial representation rho = I_2 and claiming boundary restriction rank = 3.

Exits with code 1 and 0 stderr bytes when all corruptions are properly detected as failing.
"""

import sys
from fractions import Fraction
import sympy as sp

import a2_peer_sm_pure3_decisive as prod


def main() -> int:
    # C1: Corrupted unit-closure claim for K under u = 3
    K = {prod.canon_line(Fraction(2, 5), Fraction(k, 10)) for k in (1, 3, 5, 7, 9)}
    v_rot = prod.canon_line(3 * Fraction(2, 5), 3 * Fraction(1, 10))
    c1_pass = (v_rot in K)

    # C2: Corrupted sign eta_bad = (3*chi + 5*psi)/4
    _, _, _, psi, chi, _, _, w_nuc, w_N = prod.build_e6_27_and_roots()
    eta_bad = [(3 * chi[i] + 5 * psi[i]) / sp.Rational(4) for i in range(6)]
    e_nuc = sum(w_nuc[i] * eta_bad[i] for i in range(6))
    e_N = sum(w_N[i] * eta_bad[i] for i in range(6))
    c2_pass = (e_nuc == e_N)

    # C3: Corrupted trivial rep rho(a) = rho(b) = I_2 -> Ad_a = Ad_b = I_3
    R_bdry_triv = sp.zeros(3, 6)
    c3_pass = (R_bdry_triv.rank() == 3)

    if c1_pass or c2_pass or c3_pass:
        print("CONTROL_UNEXPECTED_PASS")
        return 0
    print(
        "CONTROL_EXPECTED_FAIL: C1_rot_in_K=%s C2_eta_bad=(%s,%s) C3_triv_rk=%d"
        % (c1_pass, e_nuc, e_N, R_bdry_triv.rank())
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
