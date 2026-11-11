#!/usr/bin/env python3
"""SM-C2, harvest row 1530 (EXISTING_NEUTRAL_FIELD_LIFTS_THE_UP_KERNEL @ b061fd9a9): this seat's own exact check of
(a) the generator change (2): with Q = a(E+ + E-) + eps c psi Z, R = b(E+ - E-) + eps d psi Z, K_+- = (Q/a +- R/b)/2 =
E_+- + eps kappa_+- psi Z, kappa_+- = (c/a +- d/b)/2; (b) the source-level coefficients (4): the fermion direction
(a, b) in (2,0) and (a, -b) in (0,2) paired antisymmetrically with the neutral direction (c, d) give ad - bc and ad + bc,
equal to -2ab kappa_- and 2ab kappa_+; (c) the pole bounds b(-2) = b(-1) = -1, b(3) = b(4) = 1 that make multiplication
by psi an isomorphism on the retained lines; (d) the first-order block (two rank-two blocks, (2,0) carrying q kappa_- psi,
(0,2) carrying q kappa_+ psi, nonzero overlaps m1..m4) has determinant proportional to (ad - bc)^2 (ad + bc)^2, vanishing
exactly on ad = +-bc; (e) the block elimination (6): for M_eps = M0 + eps B with M0 = 0 (+) T0, det M_eps =
det(T0 + eps Q'BQ) det F(eps), F(eps) = eps A - eps^2 P'BQ [T0 + eps Q'BQ]^-1 Q'BP, exactly (sympy, a random rational
instance of sizes 4 + 6), and F(eps)/eps -> A. Planted: one entry's sign flipped (d -> -d in one (2,0) slot) must break
the determinant law."""
import json
import random
import sys
from pathlib import Path

import sympy as sp

out = {}
a, b, c, d, eps, psi, q = sp.symbols("a b c d epsilon psi q", nonzero=True)
Ep, Em, Z = sp.symbols("E_p E_m Z", commutative=True)
Q = a * (Ep + Em) + eps * c * psi * Z
R = b * (Ep - Em) + eps * d * psi * Z
Kp, Km = sp.expand((Q / a + R / b) / 2), sp.expand((Q / a - R / b) / 2)
kp, km = (c / a + d / b) / 2, (c / a - d / b) / 2
out["(a)_K_plus_ok"] = sp.simplify(Kp - (Ep + eps * kp * psi * Z)) == 0
out["(a)_K_minus_ok"] = sp.simplify(Km - (Em + eps * km * psi * Z)) == 0
omega = lambda u, v: u[0] * v[1] - u[1] * v[0]
c20, c02 = omega((a, b), (c, d)), omega((a, -b), (c, d))
out["(b)_coefficients"] = [str(c20), str(c02)]
out["(b)_ok"] = (sp.expand(c20 - (a * d - b * c)) == 0 and sp.expand(c02 - (a * d + b * c)) == 0
                 and sp.simplify(c20 + 2 * a * b * km) == 0 and sp.simplify(c02 - 2 * a * b * kp) == 0)
bf = lambda x: x // 2 if x <= 0 else -(-x // 2) - 1
out["(c)_pole_bounds"] = {k: bf(k) for k in (-2, -1, 3, 4)}
out["(c)_ok"] = bf(-2) == bf(-1) == -1 and bf(3) == bf(4) == 1
m1, m2, m3, m4 = sp.symbols("m1:5", nonzero=True)


def block(flip=False):
    km2 = (c / a - (d if not flip else -d) / b) / 2
    return sp.diag(eps * q * km * psi * m1, eps * q * km2 * psi * m2, eps * q * kp * psi * m3, eps * q * kp * psi * m4)


det = sp.factor(block().det())
out["(d)_determinant"] = str(det)
ratio = sp.simplify(det / ((a * d - b * c) ** 2 * (a * d + b * c) ** 2))
out["(d)_ratio_free_of_c_d"] = not ratio.has(c) and not ratio.has(d)
out["(d)_ok"] = out["(d)_ratio_free_of_c_d"]
# (e) the Schur complement identity on a finite instance (exact rationals)
random.seed(1530)
rnd = lambda: sp.Rational(random.randint(-9, 9), random.randint(1, 5))
k, n = 4, 6
T0 = sp.Matrix(n, n, lambda i, j: rnd() + (10 if i == j else 0))
Bm = sp.Matrix(k + n, k + n, lambda i, j: rnd())
M0 = sp.diag(sp.zeros(k), T0)
Me = M0 + eps * Bm
A = Bm[:k, :k]
BPQ, BQP, BQQ = Bm[:k, k:], Bm[k:, :k], Bm[k:, k:]
inner = T0 + eps * BQQ
Fe = eps * A - eps ** 2 * BPQ * inner.inv() * BQP
lhs = sp.expand(Me.det())
rhs = sp.simplify(inner.det() * Fe.det())
out["(e)_det_identity"] = sp.simplify(lhs - rhs) == 0
lim = sp.simplify((Fe / eps).applyfunc(lambda x: sp.limit(x, eps, 0)) - A)
out["(e)_F_over_eps_to_A"] = lim == sp.zeros(k, k)
out["(e)_ok"] = out["(e)_det_identity"] and out["(e)_F_over_eps_to_A"]
bad = sp.factor(block(flip=True).det())
out["PLANTED_flipped_entry_determinant"] = str(bad)
r2 = sp.simplify(bad / ((a * d - b * c) ** 2 * (a * d + b * c) ** 2))
out["PLANTED_caught"] = r2.has(c) or r2.has(d)
ok = all(out[k_] for k_ in ("(a)_K_plus_ok", "(a)_K_minus_ok", "(b)_ok", "(c)_ok", "(d)_ok", "(e)_ok"))
out["all_claims_hold_and_plants_caught"] = bool(ok and out["PLANTED_caught"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1, default=str))
