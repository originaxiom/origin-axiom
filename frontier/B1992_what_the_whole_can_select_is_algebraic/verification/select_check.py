"""B1992 (main, 2026-11-25; data-free): T2's exact check. For every positive word w in L, R up to length 4 (the composite
trace map), the readings on the cusp's leaf kappa = -2 that w fixes: is the set zero-dimensional, and are its points algebraic
(zero-dimensional over Q, hence algebraic, T1; the points are not solved for)? Also the numbers the listening line found, typed.
    python3 -B select_check.py > select_check_run.txt"""
import sympy as sp
from itertools import product
X, Y, Z = sp.symbols("X Y Z")
Lm = lambda v: (v[0], v[2], sp.expand(v[0] * v[2] - v[1])); Rm = lambda v: (v[2], v[1], sp.expand(v[1] * v[2] - v[0]))
cusp = X ** 2 + Y ** 2 + Z ** 2 - X * Y * Z
seen = set(); rows = []
for n in range(1, 5):
    for w in product("LR", repeat=n):
        v = (X, Y, Z)
        for c in w: v = (Lm if c == "L" else Rm)(v)
        eqs = [sp.expand(v[i] - (X, Y, Z)[i]) for i in range(3)] + [cusp]
        G = sp.groebner(eqs, X, Y, Z, order="grevlex")
        zero_dim = G.is_zero_dimensional
        sols = None
        alg = zero_dim   # a zero-dimensional ideal over Q has only algebraic solutions (T1)
        rows.append(("".join(w), zero_dim, "not solved", alg))
for r in rows: print("word %-5s fixed readings on the cusp's leaf: zero-dimensional %s; points %s; all algebraic %s" % r)
print("SUMMARY T2a: words of length <= 4 whose fixed set on the cusp's leaf is zero-dimensional with algebraic points: %d of %d; not zero-dimensional: %s" % (
    sum(1 for r in rows if r[1] and r[3]), len(rows), [r[0] for r in rows if not r[1]]))
found = {"fixed points": [0, 2], "levels": [-2, 2] + [2 * sp.cos(2 * sp.pi * sp.Rational(k, n)) for n in (3, 4, 5, 6, 10) for k in range(1, n)],
         "rates": [sp.Rational(1, 2), 1 / sp.sqrt(2), (1 + sp.I * sp.sqrt(7)) / 2], "count coefficients": [0, 2, 3, 4]}
print("SUMMARY T2b: every number the listening line found is algebraic: %s" % all(sp.nsimplify(x).is_algebraic for xs in found.values() for x in xs))
print("T3: e^pi algebraic? %s (sympy's is_algebraic: None means unknown to sympy; the theorem is Gelfond's)" % sp.exp(sp.pi).is_algebraic)
