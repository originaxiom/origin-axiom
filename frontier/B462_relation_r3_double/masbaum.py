#!/usr/bin/env python3
"""B462 — the twist-knot colored Jones (Masbaum's cyclotomic expansion).

Source (lit-gate): Masbaum, "Skein-theoretical derivation of some formulas of
Habiro", AGT 3 (2003); formula as transcribed from Fuji-Gukov-Sulkowski
(arXiv:1209.1409, eq. 2.4 + Table 2), verified in-session against the PDF:

  J_n(K_p; q) = sum_{k>=0} sum_{l=0}^{k} q^k (q^{1-n};q)_k (q^{1+n};q)_k
                x (-1)^l q^{l(l+1)p + l(l-1)/2} (1 - q^{2l+1})
                x (q;q)_k / ( (q;q)_{k+l+1} (q;q)_{k-l} )

  Table 2: p=-2 -> 6_1, p=-1 -> 4_1, p=1 -> 3_1, p=2 -> 5_2.

Root-of-unity trap: (q;q)_{k+l+1} vanishes at q = e^{2 pi i/r} once k+l+1 >= r,
so the formula is evaluated SYMBOLICALLY in q (exact, sympy) and only then
specialized. Structural self-check: after cancel(), every cyclotomic
coefficient must be a Laurent polynomial (Habiro integrality) — asserted.

Gates (all must pass before any payload value is read):
  G1: p=-1 reproduces B441's validated cj_fig8 exactly (numeric, r=5,7,9).
  G2: n=2, p=2 equals the Jones polynomial of 5_2 (Knot Atlas, up to mirror).
  G3: p=1 double-sum equals the trefoil single-sum (paper eq. 2.5).
"""
import os
import sys
from functools import lru_cache

import mpmath as mp
import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "B441_child_wrt"))
import wrt as B441

Q = sp.Symbol('q')


def qpoch(z, k):
    out = sp.Integer(1)
    for j in range(k):
        out *= (1 - z * Q**j)
    return sp.expand(out)


@lru_cache(maxsize=None)
def masbaum_poly(n, p):
    """J_n(K_p; q) as an exact sympy Laurent polynomial in Q."""
    total = sp.Integer(0)
    for k in range(n):                       # (q^{1-n};q)_k kills k >= n
        pre = Q**k * qpoch(Q**(1 - n), k) * qpoch(Q**(1 + n), k)
        inner = sp.Integer(0)
        for l in range(k + 1):
            term = sp.Integer(-1)**l * Q**(l*(l+1)*p + l*(l-1)//2) * (1 - Q**(2*l+1)) \
                * qpoch(Q, k) / (qpoch(Q, k + l + 1) * qpoch(Q, k - l))
            inner += term
        coeff = sp.cancel(sp.together(inner))
        num, den = sp.fraction(coeff)
        # Habiro integrality: the coefficient must be a Laurent polynomial
        dp = sp.Poly(den, Q)
        assert dp.is_monomial, f"non-Laurent coefficient at n={n},k={k}: den={den}"
        total += sp.expand(pre * coeff)
    return sp.expand(sp.cancel(total))


def masbaum_cj(p):
    """A cj(n, q)-shaped callable (B441 interface) for the twist knot K_p."""
    def cj(n, q):
        poly = masbaum_poly(n, p)
        return sp.lambdify(Q, poly, modules=mp)(q)
    return cj


def gates():
    mp.mp.dps = 30
    # G1: p=-1 = the figure-eight, against B441's validated cj_fig8
    g1 = True
    cjm1 = masbaum_cj(-1)
    for r in (5, 7, 9):
        q = mp.e**(2j * mp.pi / r)
        for n in range(1, r):
            g1 &= abs(cjm1(n, q) - B441.cj_fig8(n, q)) < mp.mpf(10)**-20
    print(f"G1 (p=-1 == cj_fig8, r=5,7,9, all colors): {'PASS' if g1 else 'FAIL'}")

    # G2: n=2, p=2 vs the Jones polynomial of 5_2 (Knot Atlas):
    # V(5_2) = q^{-1} - q^{-2} + 2q^{-3} - q^{-4} + q^{-5} - q^{-6}  (or its mirror)
    j2 = sp.expand(masbaum_poly(2, 2))
    atlas = sp.expand(Q**-1 - Q**-2 + 2*Q**-3 - Q**-4 + Q**-5 - Q**-6)
    mirror = sp.expand(atlas.subs(Q, Q**-1))
    which = 'atlas' if sp.simplify(j2 - atlas) == 0 else ('mirror' if sp.simplify(j2 - mirror) == 0 else 'NEITHER')
    print(f"G2 (J_2(K_2) == Jones(5_2)): {which}  [J_2 = {j2}]")

    # G3: p=1 (trefoil) double-sum vs the paper's single-sum (2.5)
    g3 = True
    cj1 = masbaum_cj(1)
    for r in (5, 7):
        q = mp.e**(2j * mp.pi / r)
        for n in range(1, r):
            single = sum(q**k * mp.mpf(1) * _num_qpoch(q**(1-n), k, q) * _num_qpoch(q**(1+n), k, q)
                         for k in range(n))
            g3 &= abs(cj1(n, q) - single) < mp.mpf(10)**-20
    print(f"G3 (p=1 == trefoil single-sum 2.5): {'PASS' if g3 else 'FAIL'}")
    return g1 and which != 'NEITHER' and g3


def _num_qpoch(z, k, q):
    out = mp.mpf(1)
    for j in range(k):
        out *= (1 - z * q**j)
    return out


if __name__ == '__main__':
    ok = gates()
    print("ALL GATES PASS" if ok else "GATE FAILURE — payload blocked")
    sys.exit(0 if ok else 1)
