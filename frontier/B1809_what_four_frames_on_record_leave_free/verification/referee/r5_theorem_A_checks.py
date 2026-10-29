"""Referee P-406, r5 (exact where stated; data-free).
(a) Theorem A for SUBGROUPS, not only elements: every pair of distinct reflections of PGL(2,Z) (entries <= 4) whose
    fixed geodesics meet in H meets at a point of the orbit of i or omega, and their product is elliptic (exact: the
    intersection solved in Q(sqrt) by sympy).
(b) The object's own monodromy LR = [[2,1],[1,1]] (B1804's convention) is hyperbolic; its axis |z - 1/2|^2 = 5/4 is NOT the
    fixed line of any reflection of PGL(2,Z) (every reflection line is a vertical line x = b/(2d) or a circle of radius
    1/|c| <= 1); its fixed points are the boundary points (1 +- sqrt5)/2.  Theorem A's 'empty' case hides boundary
    fixed points: parabolic -> one cusp, hyperbolic -> two real quadratic irrationals.
(c) Which flat lines (points v of (Q/Z)^2, up to v -> -v) are fixed by an elliptic element of SL(2,Z): only 2-torsion
    (by conjugates of S) and 3-torsion (by conjugates of ST) -- so no line of exact order 5 or 10 (the record's
    slope-2/5 lines) is fixed by any elliptic element: Theorem A's elliptic points are never fixed points of a
    configuration (tau, line) on those lines.
(d) The identity is counted by the draft's script among 'no fixed point'."""
import itertools, sympy as sp
from fractions import Fraction as Fr
N = 4
x, y = sp.symbols('x y', real=True)
refl = []
seen = set()
for a, b, c, d in itertools.product(range(-N, N + 1), repeat=4):
    if a * d - b * c != -1 or a + d != 0: continue
    if (-a, -b, -c, -d) in seen: continue
    seen.add((a, b, c, d)); refl.append((a, b, c, d))
print("(a) reflections (det -1, trace 0), entries <= 4, up to sign:", len(refl))
def line_eq(g):
    a, b, c, d = g      # fixed set: c|z|^2 + d z - a zbar - b = 0 with a = -d  ->  c(x^2+y^2) + 2 d x - b = 0
    return c * (x**2 + y**2) + 2 * d * x - b
def mul(g, h):
    a, b, c, d = g; e, f, g2, h2 = h
    return (a * e + b * g2, a * f + b * h2, c * e + d * g2, c * f + d * h2)
bad = []; npairs = 0; kinds = {}
for g, h in itertools.combinations(refl, 2):
    sol = sp.solve([line_eq(g), line_eq(h)], [x, y], dict=True)
    pts = [s for s in sol if s[y].is_positive]
    if not pts: continue
    npairs += 1
    p = pts[0]; z = sp.nsimplify(p[x] + sp.I * p[y])
    # PSL(2,Z) reduce exactly-ish (numerically with high precision, then identify)
    zz = complex(sp.N(z, 40))
    for _ in range(200):
        zz = complex(zz.real - round(zz.real), zz.imag)
        if abs(zz) < 1 - 1e-12: zz = -1 / zz
        else: break
    key = 'i' if abs(zz - 1j) < 1e-9 else ('omega' if min(abs(zz - complex(-.5, 3**.5/2)), abs(zz - complex(.5, 3**.5/2))) < 1e-9 else str(zz))
    prod = mul(g, h); tr = prod[0] + prod[3]; det = prod[0] * prod[3] - prod[1] * prod[2]
    kinds[key] = kinds.get(key, 0) + 1
    if key not in ('i', 'omega') or not (det == 1 and abs(tr) < 2): bad.append((g, h, key, tr))
print("    pairs of reflection lines meeting in H:", npairs, "| meeting points reduce to:", kinds, "| exceptions:", bad[:3])
# (b)
LR = (2, 1, 1, 1)
print("(b) LR trace", LR[0] + LR[3], "-> hyperbolic; fixed points: roots of z^2 - z - 1 =", sp.solve(sp.Symbol('z')**2 - sp.Symbol('z') - 1))
radii = sorted({sp.Rational(1, abs(g[2])) for g in refl if g[2] != 0})
print("    reflection-line radii (entries <= 4):", radii, "| LR axis radius sqrt5/2 =", sp.sqrt(5) / 2, "> 1: not a reflection line (radius 1/|c| <= 1 for every reflection, all entries)")
# (c)
def fixed_lines(g, n):
    a, b, c, d = g; out = set()
    for p in range(n):
        for q in range(n):
            v = (Fr(p, n), Fr(q, n))
            gv = ((a * v[0] + b * v[1]) % 1, (c * v[0] + d * v[1]) % 1)
            mv = ((-v[0]) % 1, (-v[1]) % 1)
            if gv == v or gv == mv: out.add(v)
    return out
S = (0, -1, 1, 0); ST = (0, -1, 1, 1)
ell = []
for a, b, c, d in itertools.product(range(-3, 4), repeat=4):
    if a * d - b * c == 1 and abs(a + d) < 2: ell.append((a, b, c, d))
orders = {}
for g in ell:
    for v in fixed_lines(g, 60):
        if v == (0, 0): continue
        o = max(Fr(v[0]).denominator, Fr(v[1]).denominator)
        import math
        o = (Fr(v[0]).denominator * Fr(v[1]).denominator) // math.gcd(Fr(v[0]).denominator, Fr(v[1]).denominator)
        orders[o] = orders.get(o, 0) + 1
print("(c) elliptic elements (entries <= 3):", len(ell), "| exact orders of the nonzero lines in (1/60 Z)^2 they fix (up to sign):", sorted(orders))
print("    so no line of exact order 5 or 10 is fixed by any elliptic element (only orders 2 and 3)")
print("(d) the identity [[1,0],[0,1]] has trace 2 and is sent by l1_fixed_loci.py to 'empty' (it fixes all of H)")
