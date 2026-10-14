#!/usr/bin/env python3
"""B1645, post-seal (labelled): T1-T3 as exact identities (the sealed tolerances 1e-25/1e-20 exceeded the instrument's double
precision).  (1) B1644's table in the units' labels equals a R^T + R a^T - (a.R) 1; (2) Y(a) R = a (R.R); (3) with
R = r(e1 + i e2), a = (al, be, ga) real: s1^2 s2^2 = e2(Y^dag Y) = 4 r^4 |a|^4 and s1^2 + s2^2 = tr(Y^dag Y) = r^2 (4|a|^2 + al^2 + be^2)."""
import json, pathlib
import sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
ai, aj, ak, Ri, Rj, Rk = sp.symbols("a_i a_j a_k R_i R_j R_k")
a = sp.Matrix([ai, aj, ak]); R = sp.Matrix([Ri, Rj, Rk])
F = a * R.T + R * a.T - (a.dot(R)) * sp.eye(3)
blk = {"i": sp.Matrix([[-Ri, Rj, 0], [Rj, Ri, Rk], [0, Rk, -Ri]]), "j": sp.Matrix([[Rj, Ri, Rk], [Ri, -Rj, 0], [Rk, 0, -Rj]]),
       "k": sp.Matrix([[-Rk, 0, Rj], [0, -Rk, Ri], [Rj, Ri, Rk]])}
Yb = ai * blk["i"] + aj * blk["j"] + ak * blk["k"]           # blocks ordered (j, i, k)
perm = [1, 0, 2]                                              # to the units' labels (i, j, k)
Yu = sp.Matrix(3, 3, lambda r, c: Yb[perm[r], perm[c]])
res = {"table_equals_formula": sp.simplify(Yu - F) == sp.zeros(3, 3),
       "Y_R_equals_a_RR": sp.simplify(F * R - a * R.dot(R)) == sp.zeros(3, 1)}
r, al, be, ga = sp.symbols("r alpha beta gamma", real=True)
z = al - sp.I * be
Y = r * sp.Matrix([[z, sp.I * z, ga], [sp.I * z, -z, sp.I * ga], [ga, sp.I * ga, -sp.conjugate(z)]])
YY = Y.H * Y
e2 = sum(YY.extract([i, j], [i, j]).det() for i, j in ((0, 1), (0, 2), (1, 2)))
res["e2_equals_4r4a4"] = sp.simplify(sp.expand(e2 - 4 * r**4 * (al**2 + be**2 + ga**2)**2)) == 0
res["trace_equals"] = sp.simplify(sp.expand(YY.trace() - r**2 * (4 * (al**2 + be**2 + ga**2) + al**2 + be**2))) == 0
# the basis form of step 3 is the formula with R = r(1, i, 0), a = (al, be, ga)
Rb = r * sp.Matrix([1, sp.I, 0]); ab = sp.Matrix([al, be, ga])
res["basis_form_is_the_formula"] = sp.simplify(Y - (ab * Rb.T + Rb * ab.T - ab.dot(Rb) * sp.eye(3))) == sp.zeros(3, 3)
json.dump({k: bool(v) for k, v in res.items()}, open(HERE / "post_seal_symbolic.json", "w"), indent=1)
print({k: bool(v) for k, v in res.items()})
