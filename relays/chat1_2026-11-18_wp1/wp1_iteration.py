#!/usr/bin/env python3
"""Card W-P1 (the process reading): what the golden thread's own iteration forces, computed exactly.
Data-free; standard mathematics of one matrix, with no frame, no point of the modulus, no direction and no class.

    python3 -I wp1_iteration.py

gamma = [[2, 1], [1, 1]] is the golden thread's monodromy as B1922 writes it on the modulus, tau -> (2 tau + 1)/(tau + 1)
(LR in the record's letters). Printed, each in closed form:
  P1  on the fibre torus: trace and determinant; the stretch factor and its entropy; the expanding and contracting
      slopes; the number of points fixed by gamma^n, |det(gamma^n - I)| = |2 - tr gamma^n|, for n = 1 to 8;
  P2  on the modulus: gamma's fixed points on the real line; its axis (centre, radius, highest point); that i and 1 + i
      lie on it; gamma(i); the translation length 2 arccosh(tr/2);
  P3  how high a thread can rise: the axis radius of L^n R = [[n + 1, n], [1, 1]] for n = 1 to 8, against gamma's.
"""
import sympy as sp

g = sp.Matrix([[2, 1], [1, 1]])
I2 = sp.eye(2)
t, d = g.trace(), g.det()
lam = sp.nsimplify(max(g.eigenvals(), key=lambda e: float(e)))
print("P1: tr %s, det %s; stretch factor %s = %s; entropy log of it = %s" % (t, d, lam, sp.N(lam, 12), sp.N(sp.log(lam), 12)))
for ev, mult, vecs in g.eigenvects():
    v = vecs[0]
    print("P1: eigenvalue %s, slope y/x of its direction %s" % (sp.simplify(ev), sp.simplify(v[1] / v[0])))
print("P1: points fixed by gamma^n on the torus, n = 1..8:", [abs((g ** n - I2).det()) for n in range(1, 9)],
      "| 2 - tr gamma^n:", [abs(2 - (g ** n).trace()) for n in range(1, 9)])

z = sp.symbols("z")
fp = sp.solve(sp.Eq(z * (z + 1), 2 * z + 1), z)
c = sp.nsimplify((fp[0] + fp[1]) / 2)
r = sp.simplify(abs(fp[0] - fp[1]) / 2)
print("P2: fixed points %s; axis centre %s, radius %s = %s (its highest point, Im tau)" % (fp, c, r, sp.N(r, 12)))
for p in (sp.I, 1 + sp.I):
    print("P2: |%s - centre|^2 - radius^2 = %s (0: on the axis)" % (p, sp.simplify(abs(p - c) ** 2 - r ** 2)))
gi = sp.simplify((2 * sp.I + 1) / (sp.I + 1))
print("P2: gamma(i) = %s; translation length 2 arccosh(3/2) = %s = 2 log(stretch) = %s" %
      (gi, sp.N(2 * sp.acosh(sp.Rational(3, 2)), 12), sp.N(2 * sp.log(lam), 12)))

L, R = sp.Matrix([[1, 1], [0, 1]]), sp.Matrix([[1, 0], [1, 1]])
rows = []
for n in range(1, 9):
    M = L ** n * R
    tr_, cc = M.trace(), M[1, 0]
    rows.append((n, list(M), sp.N(sp.sqrt(tr_ ** 2 - 4) / (2 * abs(cc)), 6)))
print("P3: L^n R, its entries and its axis radius (highest Im tau):", rows)
print("P3: gamma's axis radius for comparison:", sp.N(r, 6))
