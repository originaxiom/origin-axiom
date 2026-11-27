#!/usr/bin/env python3
"""
Standalone Failing Control for Card A2-WEIL-CHIRAL-LATTICE-BRIDGE (seat fam3-v1-high-03).

Tests 3 independent corruptions against the decisive producer's own functions:
  C1: Dropping Gauss quadratic reciprocity (predicting tr(C_{3,omega}) = -i*sqrt(3) at N=21).
  C2: Using the wrong weight y^1 (instead of y^2) for the weight-2 odd cusp form V_odd(tau)
      on L_15 under S: tau -> -1/tau.
  C3: Claiming L'_15 non-principal even theta has full rank 3 (violated by swap isometry j -> -4j).

Exits with code 1 and 0 stderr bytes when all corruptions are properly detected as failing.
"""

import sys
import mpmath as mp

import a2_weil_chiral_lattice_bridge_decisive as prod


def main() -> int:
    mp.mp.dps = 35
    # C1: Corrupted quadratic-reciprocity trace claim at N = 21 (r = 1)
    G21 = prod.gauss_sum(21, (-11) % 21)
    tr21 = prod.gauss_sum(21, (-33) % 21) / mp.conj(G21)
    c1_pass = abs(tr21 - (-1j * mp.sqrt(3))) < mp.mpf(1) / mp.mpf(10**10)

    # C2: Corrupted modular weight y^1 on weight-2 cusp form Theta_{L_15}^odd under S
    tau0 = mp.mpc(prod.f_mp(23, 100), prod.f_mp(137, 100))
    v0 = prod.theta_lattice_LN(15, tau0, True, 7, 5)
    vS = prod.theta_lattice_LN(15, -1 / tau0, True, 9, 7)
    w0 = mp.im(tau0) * (mp.norm(v0) ** 2)
    wS = mp.im(-1 / tau0) * (mp.norm(vS) ** 2)
    c2_pass = abs(w0 - wS) / w0 < mp.mpf(1) / mp.mpf(10**10)

    # C3: Corrupted rank-3 claim for non-principal L'_15 even CRT matrix M_even
    ve_p = prod.theta_lattice_L15_prime(tau0, False, 7, 7)
    se_p, _ = prod.svd_left_3x5(prod.crt_3x5(ve_p))
    c3_pass = (se_p[2] / se_p[0]) > mp.mpf(1) / mp.mpf(10**6)

    if c1_pass or c2_pass or c3_pass:
        print("CONTROL_UNEXPECTED_PASS")
        return 0
    print(
        "CONTROL_EXPECTED_FAIL: C1_qr_err=%s C2_wt_S_err=%s C3_L15p_sv3_ratio=%s"
        % (
            mp.nstr(abs(tr21 + 1j * mp.sqrt(3)), 6),
            mp.nstr(abs(w0 - wS) / w0, 6),
            mp.nstr(se_p[2] / se_p[0], 6),
        )
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
