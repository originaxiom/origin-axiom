"""B211 -- the metallic family's arithmetic/geometric/quantum faces (L29-L34). Nothing to CLAIMS.md.

Load-bearing locks (not the easy part):
 - L34: independently count the character variety AND a_p(40a1) and assert  #X = p-1-a_p  (the Weil-zeta
        connection itself), plus the known 40a1 a_p sequence as a third cross-check.
 - L33: the WRT level-period IS the metallic Pisano period (period of x_{n+1}=m x_n+x_{n-1}).
 - L29: ord(R^mL^m mod m^2+4) = 2Q(m).
 - L30: rank 4 (SU(2)_3 Verlinde) != rank 9 (2I rep ring).
 - L31/L32: the recorded SnapPy data (sage-gated) + the pyenv-checkable arithmetic constants.
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier",
                                "B211_metallic_arithmetic_geometric_faces"))
from charvar_zeta import count_charvar, ap_40a1, derive_charvar  # noqa: E402
from metallic_numbertheory import (Q, pisano, P_wrt, order_monodromy,  # noqa: E402
                                   VERLINDE_RANK_SU2_3, TWO_I_REP_RANK)
from geometric_limit_sage import L31_DRILL, L32_CS, V_OCT, BORROMEAN_VOL  # noqa: E402
import sympy as sp  # noqa: E402

# known a_p of Cremona 40a1 (good primes), independent reference for the cross-check
A40A1 = {3: 0, 7: -4, 11: 4, 13: -2, 17: 2, 19: 4, 23: 4, 29: -2, 31: -8, 37: 6,
         41: -6, 43: -8, 47: 4, 53: 6, 59: -4, 61: -2, 67: 8, 71: 0, 73: -6}


def test_L34_charvar_polynomial_and_complete_structure():
    # the DERIVED variety polynomial and its verification at the complete structure
    x, z, u = sp.symbols('x z u')
    Phi, riley = derive_charvar()
    assert sp.expand(Phi - (z**2 - (x**2 + 1) * z + (2 * x**2 - 1))) == 0
    # complete structure x=2 -> Riley param u solves u^2+u+1=0 (omega; trace field Q(sqrt-3))
    assert sp.expand(riley.subs(x, 2) - (u**2 + u + 1)) == 0
    # z-discriminant is the genus-1 branch locus (x^2-1)(x^2-5)
    D = sp.expand((x**2 + 1)**2 - 4 * (2 * x**2 - 1))
    assert sp.expand(D - (x**2 - 1) * (x**2 - 5)) == 0


def test_L34_weil_zeta_equals_40a1():
    # LOAD-BEARING: char-variety count, naive a_p, and the reference 40a1 a_p all agree, and
    # #X(F_p) = p - 1 - a_p for every good prime.
    for p, a_ref in A40A1.items():
        c = count_charvar(p)
        a = ap_40a1(p)
        assert a == a_ref, f"a_{p}: naive {a} != 40a1 {a_ref}"
        assert c == p - 1 - a, f"p={p}: #X={c} != p-1-a_p={p-1-a}"
    # Hasse bound sanity (E is an honest elliptic curve)
    for p, a in A40A1.items():
        assert abs(a) <= 2 * math.isqrt(p) + 2


def test_L33_wrt_period_is_metallic_pisano():
    for m in range(1, 13):
        N = m * m + 4
        pi = pisano(m, N)
        assert pi == 4 * Q(m), f"m={m}: pi {pi} != 4Q {4*Q(m)}"
        assert P_wrt(m) == m * pi // 4, f"m={m}: P_WRT {P_wrt(m)} != (m/4)pi"


def test_L29_order_tracks_Q():
    for m in range(1, 13):
        assert order_monodromy(m) == 2 * Q(m), f"m={m}"


def test_L30_skein_quotient_not_2I():
    assert VERLINDE_RANK_SU2_3 == 4 and TWO_I_REP_RANK == 9
    assert VERLINDE_RANK_SU2_3 != TWO_I_REP_RANK


def test_L31_borromean_limit_recorded():
    # 2*v_oct constant + the m-independent Borromean identification (sage-gated drill data)
    assert abs(BORROMEAN_VOL - 7.327724753417752) < 1e-12
    for m, d in L31_DRILL.items():
        assert d["drilled_cusps"] == 3
        assert abs(d["drilled_vol"] - BORROMEAN_VOL) < 1e-5
        assert "Borromean" in d["identify"]


def test_L32_amphichiral_cs_zero_recorded():
    for m, d in L32_CS.items():
        assert d["amphichiral"] is True
        assert abs(d["cs"]) < 1e-9
    assert abs(V_OCT - 3.66386237670887606) < 1e-12


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn()
            print(f"{name}  PASS")
    print("ALL CHECKS PASS")
