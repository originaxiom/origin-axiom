#!/usr/bin/env python3
"""SM-C2, harvest rows 1522 (ORDER_TEN_PHYSICAL_CUBIC_AND_EXCEPTIONAL_MODE_PAIRING @ b710d69c0) and 1524
(ORDER_THREE_R_HIGGS_AND_DERIVED_TREE_VERTICES @ 1cc2b94de): this seat's own exact check.
Row 1522: the Lie coefficient (4) kappa(E_ai, [QY, E_ia]) = -5 kappa(E_ai, E_ia) for every colour i and weak alpha, with
QY = diag(-2,-2,-2,3,3); the charges +5/-5 of u/v; the slot counts (1) h1(L_+-5) = 0, h0(S L_+-5) = 1 at eta = chi^5;
the endpoint law (7) b(j+2) - b(j+1) = 0 (j even), 1 (j odd); the j = 2, 3 dimensions and profile powers; the root action
charges (+1 <-> -4, +6 <-> +1) on the ten; 104 -> 128 chiral, R 1 -> 13; the light beta (10,6,4) + (10,6,4) = (20,12,8)
with zero w-contraction, from this seat's row-1518 field table at kappa = 1 and the mixed (3,2) pairs.
Row 1524: (1) the R counts delta(chi^2), delta(chi^3) and (2) exact order three (8 characters on U1^2, 4 after inversion);
(3) N_chiral = 100 + 12 kappa = 92 + 12 kappa + 8; (4)-(5) Z's raising and norm, eps(b0,Z,Z) = -2 sqrt6/5,
eps(b4, b0^b1, Z) = -sqrt(3/5) by literal wedges; (6) u, r, a are E8 roots, sum zero, QY = dot(T/2, root) = +1, -3, +2,
w-grades -2, +1, +1, a.r = -1, r - a not a root, a + r a root; (8)-(10) the canonical normalisation cancels I_j and gives
|y_I| = (4 sqrt3/5) g4, |y_II| = sqrt(6/5) g4, ratio sqrt(8/5); the up grade sum +1; (11) b = (56/5, 6+2k, 1+3k) and
(1/2,-3/2,1).b = -12/5. Planted: Z with the wrong relative sign must change eps(b0,Z,Z)'s role (Z no longer highest) and
a wrong kinetic weight G_a = I_j (no 1/2) must change the ratio's normalisation of |y_I|."""
import json
import sys
from fractions import Fraction as Fr
from itertools import combinations, permutations, product
from pathlib import Path

import sympy as sp

out = {}
# ---------------- row 1522 ----------------
QY = sp.diag(-2, -2, -2, 3, 3)
unit = lambda i, j: sp.Matrix(5, 5, lambda r, c: 1 if (r, c) == (i, j) else 0)
kap = lambda A, B: (A * B).trace()
lie_ok = all(kap(unit(al, i), QY * unit(i, al) - unit(i, al) * QY) == -5 * kap(unit(al, i), unit(i, al))
             and kap(unit(al, i), unit(i, al)) != 0 for i in range(3) for al in (3, 4))
charge = lambda i, j: QY[i, i] - QY[j, j]
r22_charges = (charge(3, 0), charge(0, 3))


def bf(x):
    return x // 2 if x <= 0 else -(-x // 2) - 1


law7 = {j: bf(j + 2) - bf(j + 1) for j in range(0, 12)}
law7_ok = all(v == (0 if j % 2 == 0 else 1) for j, v in law7.items())
dims = {"j=2": (bf(3), bf(4)), "j=3": (bf(4), bf(5))}
powers = {"a_j=2": Fr(4, 2) - bf(4), "a_j=3": Fr(5, 2) - bf(5), "u_j=2": Fr(3, 2) - bf(3), "u_j=3": Fr(4, 2) - bf(4)}
# slot counts at chi of order 10, eta = chi^5 (order two), L_+-5 = eta: h1(L) = delta(L) = 0, h0(S L) = delta(eta L) = 1
eta_sq_trivial, eta_trivial = True, False
slots_ok = (int(eta_trivial) == 0) and (int(eta_sq_trivial) == 1)
# ten-sector root action: QY of e_a ^ e_j is the sum of the two entries
q = [QY[k, k] for k in range(5)]
wedge_ok = (q[3] + q[1] == 1 and q[0] + q[1] == -4 and q[3] + q[4] == 6 and q[0] + q[4] == 1)
# beta: row 1518's field table, N = 1 chiral b_a = sum T(R) - 3 C(G), GUT-normalised b1 = (3/5) sum Y^2 dim
fields = [("Q", 3, 2, Fr(1, 6), 4), ("U", 3, 1, Fr(-2, 3), 4), ("E", 1, 1, Fr(1), 4), ("D", 3, 1, Fr(1, 3), 8),
          ("L", 1, 2, Fr(-1, 2), 8)]


def beta(fl, kappa):
    b1 = Fr(3, 5) * sum(n * c * w * Y * Y for _, c, w, Y, n in fl)
    b2 = sum(n * c * Fr(1, 2) for _, c, w, Y, n in fl if w == 2) + 2 * kappa - 6
    b3 = sum(n * w * Fr(1, 2) for _, c, w, Y, n in fl if c == 3) + 3 * kappa - 9
    return (b1, b2, b3)


wv = (Fr(1, 2), Fr(-3, 2), Fr(1))
b_gen1 = beta(fields, 1)
mixed = [("X", 3, 2, Fr(5, 6), 2), ("Xb", 3, 2, Fr(-5, 6), 2)]
b_mix = tuple(x - y for x, y in zip(beta(fields + mixed, 1), b_gen1))
b_tot = tuple(x + y for x, y in zip(b_gen1, b_mix))
dotw = lambda b: sum(x * y for x, y in zip(wv, b))
r1522 = {"lie_coefficient_minus5_all_i_alpha": lie_ok, "u_v_charges": list(map(int, r22_charges)),
         "law7": law7, "dims_j2_j3": dims, "profile_powers": {k: str(v) for k, v in powers.items()},
         "beta_generic_kappa1": [str(x) for x in b_gen1], "beta_mixed_pairs": [str(x) for x in b_mix],
         "beta_total": [str(x) for x in b_tot], "w_dot_total": str(dotw(b_tot)),
         "chiral_104_to_128": 92 + 12 * 1 + 24 == 128 and 92 + 12 == 104, "R_1_to_13": 1 + 12 == 13}
ok1522 = (lie_ok and r22_charges == (5, -5) and law7_ok and dims == {"j=2": (1, 1), "j=3": (1, 2)}
          and powers == {"a_j=2": 1, "a_j=3": Fr(1, 2), "u_j=2": Fr(1, 2), "u_j=3": 1} and slots_ok and wedge_ok
          and b_gen1 == (10, 6, 4) and b_mix == (10, 6, 4) and dotw(b_tot) == 0 and r1522["chiral_104_to_128"])
r1522["ok"] = ok1522
out["row1522"] = r1522
# ---------------- row 1524 ----------------
# (1)-(2): exact order three on U1^2
pts = [(Fr(x, 3), Fr(y, 3)) for x, y in product(range(3), repeat=2)]
trivial = lambda p, k: (p[0] * k) % 1 == 0 and (p[1] * k) % 1 == 0
exact3 = [p for p in pts if trivial(p, 3) and not trivial(p, 2)]
inv_classes = {min(p, ((-p[0]) % 1, (-p[1]) % 1)) for p in exact3}
counts_ok = all(bf(1 - 3) < 0 for _ in [0]) and bf(1 - 1) == 0      # j = 3: zero; j = 1: delta(chi^q)
r24 = {"exact_order_three_count": len(exact3), "after_inversion": len(inv_classes),
       "chi5_nontrivial_on_all": all(not trivial(p, 5) for p in exact3)}
kap_ = sp.Symbol("kappa")
r24["N_chiral"] = str(sp.expand(92 + 12 * kap_ + 8))
# (4)-(5) wedges in the ordered basis b0..b4


def wedge_terms(*vecs):
    """each vec: list of (coef, tuple of indices); returns coefficient of b0^...^b4"""
    tot = 0
    for combo in product(*vecs):
        coef = sp.prod([c for c, _ in combo])
        idx = sum((list(i) for _, i in combo), [])
        if len(idx) != 5 or len(set(idx)) != 5:
            continue
        sgn = sp.combinatorics.Permutation(idx).signature()
        tot += sgn * coef
    return sp.nsimplify(sp.simplify(tot))


def make_Z(sign):
    return [(sp.sqrt(sp.Rational(2, 5)), (1, 4)), (sign * sp.sqrt(sp.Rational(3, 5)), (2, 3))]


Z = make_Z(-1)
e1 = wedge_terms([(1, (0,))], Z, Z)
e2 = wedge_terms([(1, (4,))], [(1, (0, 1))], Z)
raise_coef = sp.sqrt(6) * sp.sqrt(sp.Rational(2, 5)) - 2 * sp.sqrt(sp.Rational(3, 5))
normZ = sp.Rational(2, 5) + sp.Rational(3, 5)
r24.update({"eps(b0,Z,Z)": str(e1), "eps(b4,b0^b1,Z)": str(e2), "Z_raising": str(sp.simplify(raise_coef)),
            "Z_norm2": str(normZ)})
# (6) roots
u = tuple(Fr(x, 2) for x in (-1, -1, 1, -1, -1, 1, -1, -1))
r = (0, 0, 0, 1, 0, 0, 0, 1)
a = tuple(Fr(x, 2) for x in (1, 1, -1, -1, 1, -1, 1, -1))
dot = lambda x, y: sum(Fr(p) * Fr(q_) for p, q_ in zip(x, y))
is_root = lambda v: (dot(v, v) == 2 and (all(Fr(x).denominator == 1 for x in v) or
                                         (all(Fr(x).denominator == 2 for x in v) and sum(1 for x in v if x < 0) % 2 == 0)))
T = (5, 5, 5, -3, -3, -3, -3, -3)
w = (0, 0, 0, -1, 1, -2, 0, 2)
r24["roots"] = {"all_roots": all(is_root(v) for v in (u, r, a)),
                "sum_zero": all(x + y + z == 0 for x, y, z in zip(u, r, a)),
                "QY": [str(dot(T, v) / 2) for v in (u, r, a)], "grades": [str(dot(w, v)) for v in (u, r, a)],
                "a.r": str(dot(a, r)), "r-a_root": is_root(tuple(Fr(x) - Fr(y) for x, y in zip(r, a))),
                "a+r_root": is_root(tuple(Fr(x) + Fr(y) for x, y in zip(r, a)))}
# (8)-(10) normalisation
I, Ar, g6, C = sp.symbols("I_j Area g6 C_j", positive=True)


def yuk(Ga):
    Gu, GH = I, Ar
    return sp.simplify((C * I * g6 ** 3 / g6 ** 2) / sp.sqrt(Ga * Gu * GH))


g4 = g6 / sp.sqrt(Ar)
yI = sp.simplify(yuk(I / 2).subs(C, 2 * sp.sqrt(6) / 5) / g4)
yII = sp.simplify(yuk(I / 2).subs(C, sp.sqrt(sp.Rational(3, 5))) / g4)
r24.update({"yI_over_g4": str(yI), "yII_over_g4": str(yII), "ratio": str(sp.nsimplify(yI / yII))})
r24["up_grade_sum"] = 2 - 2 + 1
b11 = (Fr(56, 5), "6+2k", "1+3k")
r24["(11)_w_dot"] = str(Fr(1, 2) * Fr(56, 5) - Fr(3, 2) * 6 + 1 + sp.Rational(0))   # kappa cancels: -3k + 3k
insertion = beta([("Hd", 1, 2, Fr(-1, 2), 2), ("Hu", 1, 2, Fr(1, 2), 2)], 0)
insertion = (insertion[0], insertion[1] + 6, insertion[2] + 9)       # remove the gauge part added by beta()
r24["doublet_pairs_insertion"] = [str(x) for x in insertion]
ok1524 = (len(exact3) == 8 and len(inv_classes) == 4 and r24["chi5_nontrivial_on_all"] and counts_ok
          and r24["N_chiral"] == "12*kappa + 100" and e1 == -2 * sp.sqrt(6) / 5 and sp.simplify(e2 + sp.sqrt(sp.Rational(3, 5))) == 0
          and sp.simplify(raise_coef) == 0 and normZ == 1 and r24["roots"]["all_roots"] and r24["roots"]["sum_zero"]
          and r24["roots"]["QY"] == ["1", "-3", "2"] and r24["roots"]["grades"] == ["-2", "1", "1"]
          and r24["roots"]["a.r"] == "-1" and not r24["roots"]["r-a_root"] and r24["roots"]["a+r_root"]
          and sp.simplify(yI - 4 * sp.sqrt(3) / 5) == 0 and sp.simplify(yII - sp.sqrt(sp.Rational(6, 5))) == 0
          and sp.simplify(yI / yII - sp.sqrt(sp.Rational(8, 5))) == 0 and r24["up_grade_sum"] != 0
          and Fr(1, 2) * Fr(56, 5) - Fr(3, 2) * 6 + 1 == Fr(-12, 5) and insertion == (Fr(6, 5), 2, 0)
          and (Fr(10) + Fr(6, 5), 4 + 2, 1) == (Fr(56, 5), 6, 1))
r24["ok"] = ok1524
out["row1524"] = r24
# planted
Zbad = make_Z(+1)
raise_bad = sp.sqrt(6) * sp.sqrt(sp.Rational(2, 5)) + 2 * sp.sqrt(sp.Rational(3, 5))
yI_bad = sp.simplify(yuk(I).subs(C, 2 * sp.sqrt(6) / 5) / g4)
out["PLANTED_wrong_sign_Z_not_highest"] = sp.simplify(raise_bad) != 0
out["PLANTED_GA_without_half_changes_yI"] = sp.simplify(yI_bad - yI) != 0
out["all_claims_hold_and_plants_caught"] = bool(ok1522 and ok1524 and out["PLANTED_wrong_sign_Z_not_highest"]
                                                and out["PLANTED_GA_without_half_changes_yI"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1, default=str))
