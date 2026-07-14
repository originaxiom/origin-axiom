"""B581 — the six torsions: fast locks from the committed exact data + m=1 analytics.

(The full ~8-min recomputation is the reproducer six_torsions.py; a slow-tier
rerun lock can be added under OA_SLOW at Review 17 if wanted.)
"""
import json
import os
from fractions import Fraction as Fr

import sympy as sp

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, "..", "frontier", "B581_six_torsions", "six_torsions_results.json")


def _poly(m, d):
    t = sp.Symbol('t')
    q = d[m]['quotient']
    assert all(Fr(b) == 0 for a, b in q)            # integer/rational coefficients
    P = sum(sp.Rational(Fr(a)) * t**k for k, (a, b) in enumerate(q))
    lead = sp.Poly(P, t).all_coeffs()[0]
    return sp.Poly(sp.expand(P / lead), t)


def test_spectrum_structure_and_sign_law():
    d = json.load(open(DATA))
    t = sp.Symbol('t')
    signs = {}
    for m in ['1', '4', '5', '7', '8', '11']:
        P = _poly(m, d)
        cs = P.all_coeffs()
        n = len(cs) - 1
        # skew-palindromic: c_k = -c_{n-k}
        assert all(cs[k] == -cs[n - k] for k in range(len(cs)))
        # vanishes at 1 (the deformation direction)
        assert P.eval(1) == 0
        red, rem = sp.div(P.as_expr(), t - 1)
        assert rem == 0
        tau = sp.expand(red.subs(t, 1))
        signs[int(m)] = int(sp.sign(tau))
    # THE SIGN LAW: positive exactly at the theta-odd exponents {4, 8}
    assert signs == {1: -1, 4: 1, 5: -1, 7: -1, 8: 1, 11: -1}


def test_m1_is_banked_torsion_and_btz():
    d = json.load(open(DATA))
    t = sp.Symbol('t')
    P = _poly('1', d)
    fac = sp.factor_list(P.as_expr())[1]
    polys = sorted([sp.expand(f) for f, e in fac], key=sp.default_sort_key)
    assert sp.expand(t**2 - 5 * t + 1) in polys      # the BTZ quadratic
    red, _ = sp.div(P.as_expr(), t - 1)
    assert sp.expand(red.subs(t, 1)) == -3           # tau_1 = the banked B425 value


def test_seven_saturates_and_charge_arrival():
    d = json.load(open(DATA))
    t = sp.Symbol('t')
    taus = {}
    for m in ['4', '5', '7', '8', '11']:
        P = _poly(m, d)
        red, _ = sp.div(P.as_expr(), t - 1)
        taus[int(m)] = sp.Integer(sp.expand(red.subs(t, 1)))
    assert all(tau % 7 == 0 for tau in taus.values())          # 7 saturates
    assert taus[4] % 11 != 0 and taus[5] % 11 != 0             # 11 absent before m=7
    assert taus[7] % 11 == 0 and taus[8] % 11 == 0 and taus[11] % 121 == 0
