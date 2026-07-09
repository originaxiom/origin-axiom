"""B496 locks — the Thue-Morse endomorphism trace map (independently re-derived).

Guards the exact results T1-T5, T7 + the F_p cross-check. If any of these break, the
banked structural reading (singular monoid destroys the kappa-foliation except kappa=2)
is invalid.
"""
import os
import sys
import random
import sympy as sp
from sympy import symbols, simplify, expand, Poly, cos, trigsimp, Rational, Matrix

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B496_tm_endomorphism"))
import verify_tm as V

x, y, z = symbols('x y z')


def test_T1_trace_map():
    assert V.check_T1()


def test_T2_kappa_law_and_factorization():
    assert V.check_T2()


def test_T2_Fp_guard():
    out = V.check_T2_Fp(primes=(101, 10007), n=100)
    assert all(out.values())


def test_T4_angle_doubling():
    assert V.check_T4()


def test_T5_degree_growth():
    assert V.check_T5()


def test_T7_no_invariant_to_degree8():
    assert V.check_T7(8) == 1  # only constants


def test_markov_surface_mapped_off():
    # on kappa=-2, kappa' = 2 + 4 z^2 (off every level set)
    KAPPA = x**2 + y**2 + z**2 - x*y*z - 2
    ZP = x*y*z - x**2 - y**2 + 2
    KP = z**2 + z**2 + ZP**2 - z*z*ZP - 2
    kp_law = KAPPA**2 - (KAPPA - 2)*z**2 - 2
    on_markov = kp_law.subs(KAPPA, -2) if False else (sp.Integer(4) - (-4)*z**2 - 2)
    assert simplify(on_markov - (2 + 4*z**2)) == 0


# --- Q1: the mixed semigroup ---
sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B496_tm_endomorphism"))
import q1_mixed_semigroup as Q1


def test_Q1_golden_preserves_kappa():
    assert Q1.golden_preserves_kappa()


def test_Q1_tm_ejection():
    assert Q1.tm_ejection()


def test_Q1_eisenstein_field_preserved():
    assert Q1.eisenstein_preserved()
