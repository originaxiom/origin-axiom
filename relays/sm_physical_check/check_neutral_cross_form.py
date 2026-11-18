#!/usr/bin/env python3
"""The SM seat's check of the physical lane's packet neutral_cross_form_2026_11_18 (audit/physical-bridge-2026-09-05 at
01dc0774f), asked by main in M43: every finite algebraic step, on this seat's own symbolic code.  The analytic
premises (Hodge identification, the D5 inverse, the nonlinear map, compact resolvent, current continuity) are not
checked here.  No data; no physical value.
    python3 check_neutral_cross_form.py"""
import json
import pathlib

import sympy as sp

out = {}
E = lambda i, j: sp.Matrix(4, 4, lambda a, b: 1 if (a, b) == (i - 1, j - 1) else 0)
p, r = sp.symbols("p r", nonzero=True)
Q = p * E(1, 2) + r * E(2, 3) + p * E(3, 4)                 # the raising chain p e12 + r e23 + p e34
X = E(1, 3) + E(2, 4)
Xm = E(1, 3) - E(2, 4)
comm = lambda A, B: A * B - B * A
out["F1 [Q, e13 + e24] = 0 (highest vector, equal entries)"] = bool(sp.simplify(comm(Q, X)) == sp.zeros(4, 4))
out["F1 hand control 4: [Q, e13 - e24] = -2p e14"] = bool(sp.simplify(comm(Q, Xm) + 2 * p * E(1, 4)) == sp.zeros(4, 4))
a, b = sp.symbols("a b")
Xg = a * E(1, 3) + b * E(2, 4)
sol = sp.solve(list(comm(Q, Xg)), [a, b], dict=True)
out["F1 the highest vectors of the form a e13 + b e24 (solutions of [Q, X] = 0)"] = str(sol)
# F2: X (x) X on the spinor product; m = 3/2, 1/2, -1/2, -3/2 are indices 1..4
idx = {sp.Rational(3, 2): 1, sp.Rational(1, 2): 2, sp.Rational(-1, 2): 3, sp.Rational(-3, 2): 4}
def ket(m1, m2):
    v = sp.zeros(16, 1); v[(idx[m1] - 1) * 4 + idx[m2] - 1] = 1; return v
XX = sp.kronecker_product(X, X)
u1, u2 = ket(-sp.Rational(3, 2), -sp.Rational(1, 2)), ket(-sp.Rational(1, 2), -sp.Rational(3, 2))
v1, v2 = ket(sp.Rational(3, 2), sp.Rational(1, 2)), ket(sp.Rational(1, 2), sp.Rational(3, 2))
out["F2 Z_B u1 = c v2 and Z_B u2 = c v1 with the same c (X(x)X)"] = bool(XX * u1 == v2 and XX * u2 == v1)
# F3: the local Wronskian
u = sp.symbols("u")
cs = sp.symbols("a_m1 a0 a1 a2 c_m1 c0 c1 c2")
F = cs[0] / u + cs[1] + cs[2] * u + cs[3] * u ** 2
H = cs[4] / u + cs[5] + cs[6] * u + cs[7] * u ** 2
f, g = sp.sqrt(u) * F, sp.sqrt(u) * H
W = sp.simplify(f * sp.diff(g, u) - g * sp.diff(f, u))
out["F3 W = u (F H' - H F')"] = bool(sp.simplify(W - u * (F * sp.diff(H, u) - H * sp.diff(F, u))) == 0)
lead = sp.series(sp.expand(F * sp.diff(H, u) - H * sp.diff(F, u)), u, 0, 0).removeO()
out["F3 F H' - H F' has no u^-3 term (the cubic pole cancels)"] = bool(sp.expand(lead).coeff(u, -3) == 0)
out["F3 W has at most a simple pole (W * u is regular at 0)"] = bool(sp.limit(sp.expand(W * u), u, 0) != sp.oo and
                                                                     sp.series(sp.expand(W), u, 0, 0).removeO().coeff(u, -2) == 0)
# F5: no common invariant line of A = i alpha sigma_x and D = diag(i, -i)
alpha = 1
A = sp.I * alpha * sp.Matrix([[0, 1], [1, 0]]); D = sp.diag(sp.I, -sp.I)
lines_A = [sp.Matrix(v[2][0]).normalized() for v in A.eigenvects()]
lines_D = [sp.Matrix(v[2][0]).normalized() for v in D.eigenvects()]
common = any(sp.Matrix.hstack(x, y).rank() == 1 for x in lines_A for y in lines_D)
out["F5 A and D have a common invariant line"] = bool(common)
# F7: the block [[0, conj L], [L, 0]] has eigenvalues +-|L|; F8: the vectors (11) carry |g|^2/2 on each test channel
L = sp.symbols("L"); Lr, Li = sp.symbols("L_r L_i", real=True)
B = sp.Matrix([[0, Lr - sp.I * Li], [Lr + sp.I * Li, 0]])
out["F7 eigenvalues of (9)"] = [str(sp.simplify(e)) for e in B.eigenvals()]
th = sp.symbols("theta", real=True)
vec = sp.Matrix([1, sp.exp(sp.I * th)]) / sp.sqrt(2)
out["F8 |<w_L|v>|^2 and |<w_R|v>|^2 for (11)"] = [str(sp.simplify(abs(vec[0]) ** 2)), str(sp.simplify(sp.Abs(vec[1]) ** 2))]
print(json.dumps(out, indent=1))
pathlib.Path(__file__).with_name("check_neutral_cross_form.json").write_text(json.dumps(out, indent=1))
