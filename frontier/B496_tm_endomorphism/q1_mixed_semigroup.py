#!/usr/bin/env python3
"""B493 Q1 — the mixed semigroup <T_golden, T_TM> on kappa=-2.

Findings: (a) T_TM is a one-way ejection off the Markov surface (kappa'=2+4z^2 >= 2 over R,
never -2); mixed orbits escape super-exponentially; the shared invariant stage is kappa=2.
(b) the fig-8 A-poly curve meets kappa=-2 at x=0 (reducible) and x=(3+-sqrt-3)/2 (geometric,
Eisenstein Q(sqrt-3)); under one T_TM the geometry is destroyed but the field Q(sqrt-3) is
preserved (kappa'=8-+6 sqrt-3).

  python3 q1_mixed_semigroup.py
"""
import sympy as sp
from sympy import symbols, simplify, sqrt, Rational, minimal_polynomial

x = symbols('x')
def kap(p): return p[0]**2 + p[1]**2 + p[2]**2 - p[0]*p[1]*p[2] - 2
Tg = lambda p: (p[2], p[0], p[0]*p[2] - p[1])
Ttm = lambda p: (p[2], p[2], p[0]*p[1]*p[2] - p[0]**2 - p[1]**2 + 2)

def golden_preserves_kappa():
    a, b, c = symbols('a b c')
    return simplify(kap(Tg((a, b, c))) - kap((a, b, c))) == 0

def tm_ejection():
    # on kappa=-2, T_TM -> kappa' = 2+4z^2, and never -2 over R (>=2)
    for p in [(3, 3, 3), (3, 3, 6), (3, 6, 15)]:
        p = tuple(Rational(v) for v in p)
        if kap(p) != -2:
            return False
        if kap(Ttm(p)) != 2 + 4*p[2]**2:
            return False
    return True

def eisenstein_preserved():
    xg = (3 + sqrt(-3))/2
    p = (xg, xg/(xg-1), xg/(xg-1))
    if simplify(kap(p)) != -2:
        return False
    # point field is Q(sqrt-3)
    if minimal_polynomial(xg, x) != x**2 - 3*x + 3:
        return False
    kq = simplify(kap(Ttm(p)))
    # kappa' = 8 - 6 sqrt(-3), still in Q(sqrt-3)
    return simplify(kq - (8 - 6*sqrt(-3))) == 0

if __name__ == "__main__":
    print("T_golden preserves kappa:", golden_preserves_kappa())
    print("T_TM one-way ejection off kappa=-2 (kappa'=2+4z^2):", tm_ejection())
    print("Eisenstein field Q(sqrt-3) preserved under one T_TM:", eisenstein_preserved())
    # the escape orbit
    p = tuple(Rational(v) for v in (3, 6, 15))
    ks = [kap(p)]
    for c in 'TTTT':
        p = Ttm(p); ks.append(kap(p))
    print("kappa escape under TTTT from (3,6,15):", [int(k) for k in ks])
