#!/usr/bin/env sage-python
"""BITE CONTROL for the mod-p obstruction: can it exclude ANYTHING?

The obstruction returned INCONCLUSIVE on every word tested. Two readings: the child is
genuinely not excludable, or the test is VACUOUS. A degree-7000 polynomial over F_p has
irreducible factors of nearly every small degree, so 'the pattern is realisable' may be
true for essentially any target. This checks that directly.
"""
import os, sys
from sage.all import GF, PolynomialRing, ZZ

Zt = PolynomialRing(ZZ, 't')
TARGETS = {
    "child x^4-x-1":        Zt([-1, -1, 0, 0, 1]),
    "x^4+1 (very split)":   Zt([1, 0, 0, 0, 1]),
    "x^4-2":                Zt([-2, 0, 0, 0, 1]),
    "x^4+x^3+x^2+x+1":      Zt([1, 1, 1, 1, 1]),
    "deg-13 x^13-x-1":      Zt([-1, -1] + [0]*11 + [1]),
    "deg-29 x^29-x-1":      Zt([-1, -1] + [0]*27 + [1]),
}
PRIMES = [10007, 10009, 10037, 10039]

def pattern(f, p):
    Fp = PolynomialRing(GF(p), 't')
    return tuple(sorted(g.degree() for g, e in Fp(f).factor() for _ in range(e)))

def eliminant_modp(word, p):
    R = PolynomialRing(GF(p), ['x', 'y', 'z']); x, y, z = R.gens()
    F = lambda q: (q[2], q[0], q[0]*q[2] - q[1])
    M = lambda q: (q[2], q[2], q[0]*q[1]*q[2] - q[0]**2 - q[1]**2 + 2)
    D = lambda q: (q[0]**2 - 2, q[1]**2 - 2, q[0]*q[1]*q[2] - q[0]**2 - q[1]**2 + 2)
    G = {'F': F, 'M': M, 'D': D}
    q = (x, y, z)
    for c in reversed(word): q = G[c](q)
    f1, f2, f3 = q[0] - x, q[1] - y, q[2] - z
    return f1.resultant(f3, z).resultant(f2.resultant(f3, z), y).univariate_polynomial()

def realisable(h, pat):
    degs = []
    for g, e in h.factor(): degs.extend([g.degree()] * e)
    pool = list(degs)
    for d in pat:
        if d in pool: pool.remove(d)
        else: return False
    return True

W = "FMMMD"
print("bite control on word %s -- does the obstruction EVER fire?\n" % W)
for name, f in TARGETS.items():
    fired = None
    for p in PRIMES:
        h = eliminant_modp(W, p)
        if h == 0: continue
        if not realisable(h, pattern(f, p)): fired = p; break
    print("  %-24s -> %s" % (name, ("EXCLUDED at p=%d" % fired) if fired else "not excluded"))
print("\nIf nothing is ever excluded, the test is VACUOUS and its INCONCLUSIVE verdicts mean nothing.")
