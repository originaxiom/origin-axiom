"""B204 -- the WRT level-period law for once-punctured-torus bundles (V197). Fast pyenv locks.

Z(a,b;k) = tr(rho_k(R^a L^b)) on SU(2)_k.  Established law (predict-then-confirm, fundamental):
    per|Z(a,b)| in k = lcm(a,b)*(4+ab)/gcd(4+ab,4),
diagonal a=b=m gives the metallic period P(m)=m(m^2+4)/gcd(m^2+4,4); m=1 reproduces chat1's
verified period-5 sequence. numpy-only; nothing to CLAIMS.md.
"""
import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..",
                                "frontier", "B204_metallic_wrt_period"))
from period_law import Z, Z_mat, period_predicted, is_period, is_fundamental  # noqa: E402

PHI = (1 + np.sqrt(5)) / 2


def test_sum_and_matrix_paths_agree():
    for a in range(1, 4):
        for b in range(1, 4):
            for k in range(1, 12):
                assert abs(Z(a, b, k) - Z_mat(a, b, k)) < 1e-9, (a, b, k)


def test_m1_period5_anchor():
    # chat1's verified figure-eight sequence (cyclic): k=1..5 -> 1,0,-1/phi,0,1
    seq = [Z(1, 1, k).real for k in range(1, 6)]
    expect = [1.0, 0.0, -1 / PHI, 0.0, 1.0]
    assert np.allclose(seq, expect, atol=1e-6), seq
    # and it is genuinely real (a=b)
    assert max(abs(Z(1, 1, k).imag) for k in range(1, 12)) < 1e-9


def test_metallic_period_law():
    # P(m) = m(m^2+4)/gcd(m^2+4,4), the diagonal of the general law; fundamental period
    for m in range(1, 9):
        P = period_predicted(m, m)
        assert is_fundamental(m, m, P), (m, P)


def test_general_period_law():
    # per|Z(a,b)| = lcm(a,b)(4+ab)/gcd(4+ab,4) -- non-metallic incl. large held-out cells
    for (a, b) in [(1, 2), (1, 3), (2, 3), (3, 4), (2, 5), (4, 5), (3, 7), (5, 6)]:
        P = period_predicted(a, b)
        assert is_fundamental(a, b, P), (a, b, P)


def test_nonmetallic_is_complex_metallic_is_real():
    # a != b: Z genuinely complex (the constant phase rotates) -> only |Z| is periodic
    assert max(abs(Z(1, 2, k).imag) for k in range(3, 15)) > 0.1
    # and Re(Z(1,2)) is NOT periodic at the |Z| period (6), while |Z| is
    P = period_predicted(1, 2)
    assert is_period(1, 2, P)                                   # |Z| periodic
    re_ok = all(abs(Z(1, 2, k).real - Z(1, 2, k + P).real) < 1e-6 for k in range(23, 40))
    assert not re_ok                                            # Re(Z) is not


if __name__ == "__main__":
    test_sum_and_matrix_paths_agree()
    test_m1_period5_anchor()
    test_metallic_period_law()
    test_general_period_law()
    test_nonmetallic_is_complex_metallic_is_real()
    print("ALL CHECKS PASS")
