#!/usr/bin/env python3
"""SM-C2, harvest row 1518 (the physical lane @ 8f4d100ad, QUANTUM_NORMALIZATION_AND_WEIGHTED_GAUGE_MATCHING, sections
4-5): this seat's own check of the one-loop balance w.b = 0, the N=1 two-loop pure-gauge matrix B (its eq. 9), the weighted
row G = wB (eq. 10), the kappa = 1 proportion G ~ (2, -37, 33) quoted in harvest row 1518, the symmetry
dim(G_a) B_ab = dim(G_b) B_ba, and the equal-coupling sums -24/5 (kappa = 1) and 156/5 (kappa = 3). Field table built here
from SM quantum numbers (Y with Q = T3 + Y; GUT-normalised C1 = (3/5) Y^2; T(fund) = 1/2). B_ab = 2 C(G_a) b_a delta_ab
+ 4 sum_r n_r T_a(r) C_b(r) (Martin-Vaughn, N=1). Planted: an un-normalised hypercharge (C1 = Y^2) must be caught."""
import json
import sys
from fractions import Fraction as F
from pathlib import Path

import sympy as sp

kap = sp.Symbol("kappa")
# (name, dim SU3, dim SU2, Y, copies including conjugates); conjugates have the same T and C
FIELDS = [("Q", 3, 2, F(1, 6), 4), ("U", 3, 1, F(-2, 3), 4), ("E", 1, 1, F(1), 4),
          ("D", 3, 1, F(1, 3), 8), ("L", 1, 2, F(-1, 2), 8)]
T_fund, C3_fund, C2_fund = F(1, 2), F(4, 3), F(3, 4)
CG = [0, 2, 3]                       # C(G_a) for U1, SU2, SU3
DIMG = [1, 3, 8]


def tables(c1norm):
    rows = []
    for name, d3, d2, Y, n in FIELDS:
        T = [c1norm * Y ** 2 * d3 * d2, (T_fund if d2 == 2 else 0) * d3, (T_fund if d3 == 3 else 0) * d2]
        C = [c1norm * Y ** 2, C2_fund if d2 == 2 else 0, C3_fund if d3 == 3 else 0]
        rows.append((n, T, C))
    # kappa adjoints: (8,1)_0 with T3 = 3, C3 = 3; (1,3)_0 with T2 = 2, C2 = 2; singlets contribute nothing
    rows.append((kap, [0, 0, 3], [0, 0, 3]))
    rows.append((kap, [0, 2, 0], [0, 2, 0]))
    return rows


def compute(c1norm):
    rows = tables(c1norm)
    S = [sum(n * sp.Rational(T[a].numerator, T[a].denominator) if not isinstance(T[a], int) else n * T[a] for n, T, C in rows)
         for a in range(3)]
    S = [sp.nsimplify(x) for x in S]
    b = [sp.expand(S[a] - 3 * CG[a]) for a in range(3)]
    B = sp.zeros(3, 3)
    for a in range(3):
        for bb in range(3):
            tot = 0
            for n, T, C in rows:
                tot += 4 * n * sp.nsimplify(T[a]) * sp.nsimplify(C[bb])
            if a == bb:
                tot += 2 * CG[a] * b[a]
            B[a, bb] = sp.expand(tot)
    return b, B


b, B = compute(F(3, 5))
w = sp.Matrix([[sp.Rational(1, 2), sp.Rational(-3, 2), 1]])
G = sp.expand(w * B)
claimB = sp.Matrix([[sp.Rational(166, 15), sp.Rational(42, 5), sp.Rational(416, 15)],
                    [sp.Rational(14, 5), 46 + 24 * kap, 32],
                    [sp.Rational(52, 15), 12, sp.Rational(178, 3) + 54 * kap]])
claimG = [sp.Rational(24, 5), -sp.Rational(264, 5) - 36 * kap, sp.Rational(126, 5) + 54 * kap]
out = {"b": [str(x) for x in b], "w_dot_b": str(sp.simplify((w * sp.Matrix(b))[0])),
       "B": [[str(B[i, j]) for j in range(3)] for i in range(3)],
       "B_equals_claim": sp.simplify(B - claimB) == sp.zeros(3, 3),
       "G": [str(x) for x in G], "G_equals_claim": all(sp.simplify(G[i] - claimG[i]) == 0 for i in range(3))}
G1 = [sp.nsimplify(G[i].subs(kap, 1)) for i in range(3)]
ratio = [sp.nsimplify(x / G1[0] * 2) for x in G1]
out["G_kappa1"], out["G_kappa1_scaled_to_2"] = [str(x) for x in G1], [str(x) for x in ratio]
out["symmetry_dimG"] = all(sp.simplify(DIMG[i] * B[i, j] - DIMG[j] * B[j, i]) == 0 for i in range(3) for j in range(3))
out["equal_coupling_sums"] = {"kappa1": str(sp.nsimplify(sum(G).subs(kap, 1))), "kappa3": str(sp.nsimplify(sum(G).subs(kap, 3)))}
# the matching table c_r = sum_a w_a T_a(r) (its section 4)
rows = tables(F(3, 5))
wv = [sp.Rational(1, 2), sp.Rational(-3, 2), 1]
c_r = {name: sp.nsimplify(sum(wv[a] * sp.nsimplify(T[a]) for a in range(3)))
       for (name, *_), (n, T, C) in zip(FIELDS + [("colour_adjoint",), ("weak_adjoint",)], rows)}
claim_c = {"Q": sp.Rational(-6, 5), "U": sp.Rational(9, 10), "E": sp.Rational(3, 10), "D": sp.Rational(3, 5),
           "L": sp.Rational(-3, 5), "colour_adjoint": 3, "weak_adjoint": -3}
out["c_r"] = {k: str(v) for k, v in c_r.items()}
out["c_r_equals_claim"] = all(c_r[k] == claim_c[k] for k in claim_c)
ok = (out["c_r_equals_claim"] and out["w_dot_b"] == "0" and out["B_equals_claim"] and out["G_equals_claim"] and ratio == [2, -37, 33]
      and out["symmetry_dimG"] and out["equal_coupling_sums"] == {"kappa1": "-24/5", "kappa3": "156/5"})
bb, Bbad = compute(F(1))
out["PLANTED_unnormalised_hypercharge_caught"] = bool(sp.simplify(Bbad - claimB) != sp.zeros(3, 3))
out["all_claims_hold_and_plants_caught"] = bool(ok and out["PLANTED_unnormalised_hypercharge_caught"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1))
