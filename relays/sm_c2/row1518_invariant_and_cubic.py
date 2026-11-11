#!/usr/bin/env python3
"""SM-C2, harvest row 1518 (QUANTUM_NORMALIZATION_AND_WEIGHTED_GAUGE_MATCHING @ 8f4d100ad), sections 3, 4, 6 and 7 -- the
parts row1518_two_loop.py does not cover: (a) from (1) R_a = 8 pi^2/g_a^2 + C_a log g_a^2 + sum_r T_a(r) log det Z_r and
dR_a/dt = -b_a, the beta function (11) beta = g^3 [b + sum T s] / [16 pi^2 (1 - C g^2/(8 pi^2))], and its pure-SYM limit
-3C g^3/[16 pi^2 (1 - C g^2/(8 pi^2))]; (b) w = (1/2, -3/2, 1): w.b = 0 for b = (10, 4 + 2k, 1 + 3k) at k = 1 and 3, w.C = 0
for C = (0, 2, 3), and I = sum w_a R_a = 2 pi C + 3 log(g3^2/g2^2) + W_Z (so dI/dt = 0 at fixed frame); (c) control 2's
cancellations -6/5 + 9/10 + 3/10 = 0, 3/5 - 3/5 = 0, 3 - 3 = 0; control 3: Z' = A^-dag Z A^-1 shifts log det Z by
-2 log|det A| (random complex 3 x 3 instance); (d) the cubic zero (14): with Q0 = E/2 in the principal five, every a in
ker ad(Q0) and v = c Q0 give kappa(u, [a, v]) = 0 for every u (a basis of ker ad(E) on gl5, random rational u).
Planted: (11) with 8 pi^2 in place of 16 pi^2 (the factor the item flags in its source's printed 4.7) must fail the
pure-SYM limit."""
import json
import random
import sys
from fractions import Fraction as Fr
from pathlib import Path

import sympy as sp

out = {}
t = sp.Symbol("t")
g = sp.Function("g")(t)
b, C, S = sp.symbols("b C S")              # S = sum_r T_a(r) s_r
R = 8 * sp.pi ** 2 / g ** 2 + C * sp.log(g ** 2)
eq = sp.Eq(sp.diff(R, t) + S, -b)          # d/dt sum T log det Z = S
gdot = sp.solve(eq, sp.diff(g, t))[0]
claim = g ** 3 * (b + S) / (16 * sp.pi ** 2 * (1 - C * g ** 2 / (8 * sp.pi ** 2)))
out["(a)_beta_11"] = sp.simplify(gdot - claim) == 0
sym = claim.subs({S: 0, b: -3 * C})
out["(a)_pure_SYM"] = sp.simplify(sym - (-3 * C * g ** 3 / (16 * sp.pi ** 2 * (1 - C * g ** 2 / (8 * sp.pi ** 2))))) == 0
w = (Fr(1, 2), Fr(-3, 2), Fr(1))
wb = {k: sum(x * y for x, y in zip(w, (10, 4 + 2 * k, 1 + 3 * k))) for k in (1, 3)}
wC = sum(x * y for x, y in zip(w, (0, 2, 3)))
g1, g2, g3, WZ = sp.symbols("g1 g2 g3 W_Z", positive=True)
Ca = (0, 2, 3)
I = sum(sp.Rational(wa.numerator, wa.denominator) * (8 * sp.pi ** 2 / ga ** 2 + c * sp.log(ga ** 2))
        for wa, ga, c in zip(w, (g1, g2, g3), Ca)) + WZ
alpha = lambda ga: ga ** 2 / (4 * sp.pi)
Cc = 1 / alpha(g3) - sp.Rational(3, 2) / alpha(g2) + sp.Rational(1, 2) / alpha(g1)
out["(b)_w.b"], out["(b)_w.C"] = {k: str(v) for k, v in wb.items()}, str(wC)
out["(b)_I_identity"] = sp.simplify(sp.expand_log(I - (2 * sp.pi * Cc + 3 * sp.log(g3 ** 2 / g2 ** 2) + WZ), force=True)) == 0
canc = (Fr(-6, 5) + Fr(9, 10) + Fr(3, 10), Fr(3, 5) - Fr(3, 5), 3 - 3)
out["(c)_cancellations"] = [str(x) for x in canc]
random.seed(1518)
rc = lambda: sp.Rational(random.randint(-4, 4), random.randint(1, 3)) + sp.I * sp.Rational(random.randint(-4, 4), 2)
A = sp.Matrix(3, 3, lambda i, j: rc() + (3 if i == j else 0))
Hm = sp.Matrix(3, 3, lambda i, j: rc())
Z = Hm.H * Hm + sp.eye(3)
Zp = A.inv().H * Z * A.inv()
shift = sp.nsimplify(sp.log(sp.Abs(Zp.det())) - sp.log(sp.Abs(Z.det())) + 2 * sp.log(sp.Abs(A.det())))
out["(c)_frame_shift_ok"] = sp.simplify(sp.expand_log(shift, force=True)) == 0 or abs(complex(shift.evalf(40))) < 1e-30
# (d) cubic zero
E5 = sp.zeros(5)
for i, c in enumerate([2, sp.sqrt(6), sp.sqrt(6), 2]):
    E5[i + 1, i] = c
Q0 = E5 / 2
basis = [sp.Matrix(5, 5, lambda r, s, k=k: 1 if r * 5 + s == k else 0) for k in range(25)]
syms = sp.symbols("x0:25")
X = sum((sv * Bm for sv, Bm in zip(syms, basis)), sp.zeros(5))
sol = sp.solve(list(Q0 * X - X * Q0), syms, dict=True)[0]
free = [s_ for s_ in syms if s_ not in sol]
kern = [X.subs(sol).subs({f: (1 if f == fr else 0) for f in free}) for fr in free]
u = sp.Matrix(5, 5, lambda i, j: sp.Rational(random.randint(-5, 5), random.randint(1, 4)))
cc = sp.Rational(7, 3)
vals = [sp.simplify((u * (a_ * (cc * Q0) - (cc * Q0) * a_)).trace()) for a_ in kern]
out["(d)_dim_ker_ad_Q0_on_gl5"] = len(kern)
out["(d)_cubic_values"] = [str(v) for v in vals]
ok = (out["(a)_beta_11"] and out["(a)_pure_SYM"] and all(v == 0 for v in wb.values()) and wC == 0
      and out["(b)_I_identity"] and all(x == 0 for x in canc) and out["(c)_frame_shift_ok"]
      and len(kern) == 5 and all(v == 0 for v in vals))
bad = g ** 3 * (b + S) / (8 * sp.pi ** 2 * (1 - C * g ** 2 / (8 * sp.pi ** 2)))
out["PLANTED_8pi2_fails_SYM_limit"] = sp.simplify(bad.subs({S: 0, b: -3 * C}) - sym) != 0
out["all_claims_hold_and_plants_caught"] = bool(ok and out["PLANTED_8pi2_fails_SYM_limit"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1, default=str))
