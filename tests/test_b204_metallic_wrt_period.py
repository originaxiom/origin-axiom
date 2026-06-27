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


# ---- Gauss-sum reciprocity proof locks (B204 PROOF.md) ----
import mpmath as mp  # noqa: E402
from gauss_proof import (Ztil_direct, Z_orig, Ztil_closed, diag_closed,  # noqa: E402
                         cross_closed, G_a, sub_period, lcm as glcm,
                         v2, cross_support_gcd, cross_period_exact, cross_period_closed)
from math import gcd  # noqa: E402
import pytest  # noqa: E402


@pytest.fixture(autouse=True)
def _mp_dps():
    """set precision per-test (not at module level): the module-level set ran during collection and, being
    last alphabetically among the mp.dps setters, leaked dps=25 globally -> starved the higher-precision
    pslq tests (b173/b182/b184/b196). Per-test setting is order-independent."""
    mp.mp.dps = 25


def test_proof_full_range_and_winding():
    # de-wound full-range Ztil == original Z * winding phase (range extension + winding identity)
    for (a, b) in [(1, 1), (2, 2), (1, 2), (1, 3)]:
        lhs = Ztil_direct(a, b, 6)
        rhs = Z_orig(a, b, 6) * mp.e**(1j * mp.pi * (a - b) / 12)
        assert abs(lhs - rhs) < mp.mpf(10) ** -18, (a, b)


def test_proof_reciprocity_closed_form():
    # Ztil == (Landsberg-Schaar diagonal) + (2D Gauss-reciprocity cross), an EXACT identity
    for (a, b) in [(1, 1), (2, 2), (3, 3), (1, 2), (1, 3), (2, 3)]:
        assert abs(Ztil_direct(a, b, 6) - Ztil_closed(a, b, 6)) < mp.mpf(10) ** -18, (a, b)


def test_proof_diagonal_period_is_lcm():
    # G_a has period exactly a (s=1) => per(diagonal G_a conj G_b) = lcm(a,b)
    for (a, b) in [(1, 1), (2, 2), (3, 3), (1, 2), (1, 3), (2, 3), (3, 5)]:
        assert sub_period(lambda n: diag_closed(a, b, n), 2 * glcm(a, b) + 6) == glcm(a, b), (a, b)
    # the s=1 argument itself: G_a(n) != G_a(n+d) for 0<d<a (period is exactly a)
    for a in [2, 3, 4, 5, 6]:
        for d in range(1, a):
            assert abs(G_a(a, 1) - G_a(a, 1 + d)) > mp.mpf(10) ** -6 or \
                   any(abs(G_a(a, n) - G_a(a, n + d)) > mp.mpf(10) ** -6 for n in range(1, a))


def test_proof_exact_period_equals_formula():
    # lcm(per(diag)=lcm(a,b), per(cross)) == P = lcm(a,b)(4+ab)/gcd(4+ab,4)
    for (a, b) in [(1, 1), (2, 2), (3, 3), (4, 4), (1, 2), (2, 3), (2, 4), (2, 6)]:
        P = period_predicted(a, b)
        pC = sub_period(lambda n: cross_closed(a, b, n), 4 * (a * b + 4) + 8)
        assert glcm(glcm(a, b), pC) == P, (a, b, pC, P)


def test_cross_period_closed_form_matches_mpmath():
    # the CLOSED FORM L_c = (4+ab)/2^min(v2a,v2b,2) == the mpmath cross-sum period (cross-check)
    for (a, b) in [(1, 1), (2, 2), (4, 4), (1, 2), (2, 3), (3, 5), (5, 6), (3, 7)]:
        pC = sub_period(lambda n: cross_closed(a, b, n), 4 * (a * b + 4) + 8)
        assert cross_period_closed(a, b) == pC == cross_period_exact(a, b), (a, b)


def test_closing_lemma_exact_integer():
    # LOAD-BEARING (the lemma close, no numerics): content gcd = 2^c, period = D/2^c, and the lcm identity
    for a in range(1, 15):
        for b in range(1, 15):
            D = a * b + 4
            c = min(v2(a), v2(b), 2)
            assert cross_support_gcd(a, b) == 2 ** c, (a, b)                 # form content = 2^c
            assert cross_period_exact(a, b) == cross_period_closed(a, b)     # period = D/2^c
            assert glcm(glcm(a, b), cross_period_closed(a, b)) == \
                glcm(a, b) * D // gcd(D, 4)                                  # the exact-period identity
    # the no-odd-prime step, spot-checked: no odd p divides the content
    for (a, b) in [(3, 5), (5, 7), (3, 3)]:
        assert cross_support_gcd(a, b) % 2 in (0, 1) and cross_support_gcd(a, b) & (cross_support_gcd(a, b) - 1) == 0


if __name__ == "__main__":
    test_sum_and_matrix_paths_agree()
    test_m1_period5_anchor()
    test_metallic_period_law()
    test_general_period_law()
    test_nonmetallic_is_complex_metallic_is_real()
    test_proof_full_range_and_winding()
    test_proof_reciprocity_closed_form()
    test_proof_diagonal_period_is_lcm()
    test_proof_exact_period_equals_formula()
    print("ALL CHECKS PASS")
