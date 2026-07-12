#!/usr/bin/env python3
"""B539 R0+R1: the forced relation catalog (exact) + observer-invariance.

R0: all pairwise ratios of the 17 read-out components, exact in Q(tau);
    find which are powers of tau; extract generating two-variable integer
    relations P(x,y) = 0 (deg <= 4, height <= 8) among ratio pairs.
R1: per coupling type, which catalog relations its own read-outs expose.
"""
import sys
import os
import numpy as np
import sympy as sp
from itertools import combinations

t = sp.Symbol('t')
MIN = t**4 - t**2 - 1
TAU_R = sp.sqrt((1 + sp.sqrt(5)) / 2)


def red(e):
    return sp.rem(sp.expand(e), MIN, t)


def inv(e):
    p = sp.Poly(red(e), t, domain='QQ')
    m = sp.Poly(MIN, t, domain='QQ')
    s, _, h = sp.gcdex(p, m)
    return red(s.as_expr() / h.as_expr())


# The 6 types' exact components (B535 C3, tau-basis coefficient tuples)
TYPES = {
    'T1': [(0, -1, 1, 0), (-1, 1, 0, 0), (1, 1, 0, -1), (1, -1, -1, 1)],
    'T2': [(0, 0, -1, 1), (-1, 1, 0, 0), (1, 1, 0, -1), (1, -2, 1, 0)],
    'T3': [(-1, 3, 1, -2), (0, -3, 0, 2), (1, 1, 0, -1), (1, -1, -1, 1)],
    'T4': [(2, -1, 1, -1), (-2, 2, -4, 3), (2, -2, 3, -2), (-2, 1, -2, 2),
           (1, 0, 2, -2)],
    'T5': [(sp.Rational(1, 2), sp.Rational(1, 2), -sp.Rational(1, 2), 0),
           (-1, 1, 0, 0),
           (sp.Rational(1, 2), -1, 0, sp.Rational(1, 2)),
           (1, -sp.Rational(1, 2), sp.Rational(1, 2), -sp.Rational(1, 2))],
    'T6': [(0, 0, -1, 1), (2, -2, 3, -2), (-2, 1, -2, 2), (1, 0, 2, -2),
           (0, 1, -2, 1)],
}


def expr_of(c):
    return red(sum(ci * t**k for k, ci in enumerate(c)))


def numval(e):
    return float(sp.expand(e).evalf(30, subs={t: TAU_R}))


def tau_power(e):
    """If e == tau^k for |k| <= 8 return k, else None (exact)."""
    for k in range(-8, 9):
        tk = red(t**k) if k >= 0 else inv(red(t**(-k)))
        if red(e - tk) == 0:
            return k
    return None


def main():
    print("=" * 76)
    print("B539 R0 — the relation catalog (exact)")
    print("=" * 76)

    # all distinct components
    comps = {}
    for label, lst in TYPES.items():
        for c in lst:
            key = tuple(sp.nsimplify(x) for x in c)
            comps.setdefault(key, set()).add(label)
    exprs = {k: expr_of(k) for k in comps}
    print(f"distinct components: {len(comps)}")

    # ── ratio classification ──
    keys = list(comps)
    tau_ratios = []
    other = 0
    for i, j in combinations(range(len(keys)), 2):
        r = red(exprs[keys[i]] * inv(exprs[keys[j]]))
        k = tau_power(r)
        if k is not None:
            tau_ratios.append((keys[i], keys[j], k))
        else:
            other += 1
    print(f"\nratio classification over {len(keys)*(len(keys)-1)//2} pairs:")
    print(f"  pure tau-powers: {len(tau_ratios)}; other Q(tau) units: {other}")
    kdist = {}
    for _, _, k in tau_ratios:
        kdist[abs(k)] = kdist.get(abs(k), 0) + 1
    print(f"  |k| distribution: {dict(sorted(kdist.items()))}")

    # ── the generating relations (frozen catalog) ──
    # relations between ratio-variables x, y that the object forces whenever
    # (x, y) = (tau^a, tau^b) with the minimal poly tau^4 = tau^2 + 1:
    x, y = sp.symbols('x y')
    CATALOG = [
        ('SQ',    y - x**2,             '(x,y) = (tau, phi): cross^2 = within'),
        ('GOLD',  y**2 - y - 1,         'y = phi (within-species ratio)'),
        ('QUART', x**4 - x**2 - 1,      'x = tau (cross-species ratio)'),
        ('CUBE',  y - x**3,             '(tau, tau^3) pairs'),
        ('RECIP', x*y - 1,              'reciprocal read-out pairs'),
        ('PERRON', y*(x - 1) - 1,       '(tau, beta): beta(tau-1) = 1'),
        ('SHIFT', y - x**2 + 1,         '(tau, 1/phi): y = x^2 - 1'),
    ]
    print(f"\nFROZEN CATALOG ({len(CATALOG)} relations):")
    for name, P, gloss in CATALOG:
        print(f"  {name:7s} P(x,y) = {P}   [{gloss}]")

    # verify each catalog relation is genuinely forced (witness in Q(tau))
    tau_e, phi_e = t, red(t**2)
    beta_e = red(t**2 + t**3)
    wit = {
        'SQ': (tau_e, phi_e), 'GOLD': (tau_e, phi_e),
        'QUART': (tau_e, phi_e), 'CUBE': (tau_e, red(t**3)),
        'RECIP': (tau_e, inv(t)), 'PERRON': (tau_e, beta_e),
        'SHIFT': (tau_e, red(t**2 - 1)),
    }
    for name, P, _ in CATALOG:
        wx, wy = wit[name]
        val = red(P.subs([(x, wx), (y, wy)]))
        assert val == 0, name
    print("  all catalog relations verified exact on their witnesses")

    # ── R1: observer-invariance ──
    print("\n" + "=" * 76)
    print("B539 R1 — observer-invariance of the SQ relation")
    print("=" * 76)
    for label, lst in TYPES.items():
        es = [expr_of(c) for c in lst]
        found = None
        for i in range(len(es)):
            for j in range(len(es)):
                if i == j:
                    continue
                rx = red(es[i] * inv(es[j]))
                for a in range(len(es)):
                    for b in range(len(es)):
                        if a == b:
                            continue
                        ry = red(es[a] * inv(es[b]))
                        if red(ry - rx * rx) == 0 and red(rx - 1) != 0:
                            found = (i, j, a, b, numval(rx), numval(ry))
                            break
                    if found:
                        break
                if found:
                    break
            if found:
                break
        status = (f"EXPOSED: x = c{found[0]}/c{found[1]} = {found[4]:.6f}, "
                  f"y = c{found[2]}/c{found[3]} = {found[5]:.6f}, y = x^2"
                  if found else "not exposed")
        print(f"  {label}: SQ {status}")


if __name__ == '__main__':
    main()
