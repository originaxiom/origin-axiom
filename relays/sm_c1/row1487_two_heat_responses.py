#!/usr/bin/env python3
"""SM-C1, harvest row 1487 (TWO_HEAT_RESPONSES_AND_SCALE_FREE_COUPLING @ 3596d5bef): this seat's own check of
(4) the hyperbolic index-raising identity J K_a^1 J^-1 = K_(a-2)^0 + (a-2) (sympy, Omega = 1/y, B = dx + i dy,
Dz = dx - i dy, as the item writes), (6) the spin-power recurrence and (7) F_a = F_(2-a), the pairing (10) -> (11) and
the j = 0..4 table, (12) from row 1421's charge coefficients with the order-seven classes, (13) B_C, (15) h_C, and the
light limits (0, 0) / (-4, -6). Planted: a wrong order-seven class (-4 taken as 4 instead of 3) must change (12)."""
import json
import sys
from fractions import Fraction as Fr
from pathlib import Path

import sympy as sp

out = {}
# (4)
X, Y = sp.symbols("x y", real=True)
a = sp.Symbol("a")
f = sp.Function("f")(X, Y)
Om = 1 / Y
Db = lambda h: sp.diff(h, X) + sp.I * sp.diff(h, Y)
Dz = lambda h: sp.diff(h, X) - sp.I * sp.diff(h, Y)
lhs = -Om ** (-2) * Db(Om ** (a - 2) * Dz(Om ** (2 - a) * f))
K0 = -Om ** (a - 4) * Dz(Om ** (2 - a) * Db(f))
shift = sp.simplify(sp.expand(lhs - K0) / f)
out["eq4_shift"] = str(shift)
explicit = sp.simplify(sp.expand(K0 - (-Y ** 2 * (sp.diff(f, X, 2) + sp.diff(f, Y, 2)) + sp.I * (a - 2) * Y * Db(f))))
out["eq4_explicit_form_residual"] = str(explicit)
# (6), (7): build F_a from the recurrence F_a = x^(a-2) F_(a-2) with x = e^{-s}, F_0 = E, F_1 = O
xs, E, O = sp.symbols("x E O")


def Fa(n):
    if n in (0, 1):
        return E if n == 0 else O
    if n > 1:
        return sp.expand(xs ** (n - 2) * Fa(n - 2))
    return sp.expand(Fa(n + 2) / xs ** n)            # F_n = x^{-(n)} F_(n+2) from F_(n+2) = x^{n} F_n


rec_ok = all(sp.simplify(Fa(2 * r) - xs ** (r * (r - 1)) * E) == 0 and sp.simplify(Fa(2 * r + 1) - xs ** (r * r) * O) == 0
             for r in range(-4, 5))
refl_ok = all(sp.simplify(Fa(n) - Fa(2 - n)) == 0 for n in range(-8, 10))
out["eq6_recurrence"], out["eq7_reflection"] = rec_ok, refl_ok
# (10) -> (11) and the table
s_ = sp.Symbol("s")


def Phi(j):
    tot = 0
    for m in range(-j, j + 1):
        k2 = sp.Rational((j - m) * (j + m + 1), 2)
        tot += sp.exp(-s_ * k2) * (Fa(1 - m) - Fa(-m))
    return sp.simplify(sp.expand(tot + Fa(j + 1) - Fa(-j)))


TABLE = {0: 2 * (O - E), 1: 2 * (E - xs * O), 2: 2 * (xs * O - xs ** 2 * E), 3: 2 * (xs ** 2 * E - xs ** 4 * O),
         4: 2 * (xs ** 4 * O - xs ** 6 * E)}
tab = {}
tab_ok = True
for j in range(5):
    p = Phi(j)
    d = sp.simplify(p - TABLE[j])
    tab[str(j)] = {"Phi": str(p), "minus_claimed": str(d), "eq11_check": str(sp.simplify(p - 2 * (Fa(j + 1) - Fa(-j))))}
    tab_ok &= d == 0
out["table"] = tab
# (12): per charge class at order seven, from row 1421's coefficients; sectors and copies
def cls(q, wrong=False):
    r = q % 7
    if wrong and q == -4:
        return 4
    return min(r, 7 - r)        # the class of +-q mod 7, represented by 0, 1, 2, 3


def B(wrong=False):
    Psi = {c: sp.Symbol("Psi%d" % c) for c in range(4)}
    T = {c: sp.Symbol("T%d" % c) for c in range(5)}
    Phi0 = {c: sp.Symbol("Phi0_%d" % c) for c in range(4)}
    Phi0[0] = 0                                          # relative to q = 0: vanishes
    D21 = {"5": {3: Fr(1, 5), -2: Fr(-1, 5)}, "10": {1: Fr(7, 5), -4: Fr(-4, 5), 6: Fr(-3, 5)},
           "24": {0: Fr(2), 5: Fr(-1), -5: Fr(-1)}}
    D31 = {"5": {3: Fr(-3, 10), -2: Fr(3, 10)}, "10": {1: Fr(9, 10), -4: Fr(-3, 10), 6: Fr(-6, 10)},
           "24": {0: Fr(3), 5: Fr(-3, 2), -5: Fr(-3, 2)}}
    sect = {"5": (2, Psi), "10": (2, T), "24": (1, Phi0)}      # copies: (5bar_g,10_b)+(5_g,10bar_b); (10_g,5_b)+conj; 24
    res = []
    for D in (D21, D31):
        tot = 0
        for R, coeffs in D.items():
            copies, fam = sect[R]
            for q, cq in coeffs.items():
                c = cls(q, wrong) if not (wrong and R != "10") else cls(q)
                tot += copies * sp.Rational(cq.numerator, cq.denominator) * fam.get(c, sp.Symbol("BAD%d" % c))
        res.append(sp.expand(tot))
    return res, Psi, T, Phi0


(B21, B31), Psi, T, Phi0 = B()
claim21 = sp.Rational(2, 5) * (Psi[3] - Psi[2]) + sp.Rational(8, 5) * (T[1] - T[3]) - 2 * Phi0[2]
claim31 = -sp.Rational(3, 5) * (Psi[3] - Psi[2]) + sp.Rational(3, 5) * (T[1] - T[3]) - 3 * Phi0[2]
eq12_ok = sp.simplify(B21 - claim21) == 0 and sp.simplify(B31 - claim31) == 0
BC = sp.expand(B31 - sp.Rational(3, 2) * B21)
eq13_ok = sp.simplify(BC - (-sp.Rational(6, 5) * (Psi[3] - Psi[2]) - sp.Rational(9, 5) * (T[1] - T[3]))) == 0
out["eq12"] = {"B21": str(B21), "B31": str(B31), "holds": eq12_ok}
out["eq13"] = {"B_C": str(BC), "holds": eq13_ok}
# (15) and the light limits: x -> 0, E_q -> delta(L^q) - 1, O_q -> delta(eta L^q) - delta(eta)
dL2, dL3, dL1, deta, deL2 = sp.symbols("dL2 dL3 dL1 deta deL2")
lim = lambda Lq, eLq: {"E": Lq - 1, "O": eLq - deta}
def Phi_inf(j, Lq, eLq):
    l = lim(Lq, eLq)
    return sp.limit(TABLE[j].subs({E: l["E"], O: l["O"]}), xs, 0)
Psi_inf = lambda Lq, eLq: Phi_inf(1, Lq, eLq) + Phi_inf(3, Lq, eLq)
hC = sp.expand(-sp.Rational(6, 5) * (Psi_inf(dL3, 0) - Psi_inf(dL2, 0)) - sp.Rational(9, 5) * (Phi_inf(2, dL1, 0) - Phi_inf(2, dL3, 0)))
eq15_ok = sp.simplify(hC - sp.Rational(12, 5) * (dL2 - dL3)) == 0
out["eq15"] = {"h_C": str(hC), "holds": eq15_ok}
# order seven: delta(L^q) = 0 for q != 0, delta(eta L^q) = 0; Phi0(2) -> 2(O - E)
light = {}
for spin, de in (("trivial", 1), ("nontrivial", 0)):
    p0 = sp.limit(TABLE[0].subs({E: 0 - 1, O: 0 - de}), xs, 0)
    b21 = sp.Rational(2, 5) * 0 + sp.Rational(8, 5) * 0 - 2 * p0
    b31 = -3 * p0
    light[spin] = [str(b21), str(b31)]
out["light_limits"] = light
light_ok = light == {"trivial": ["0", "0"], "nontrivial": ["-4", "-6"]}
# planted
(B21w, _), *_ = B(wrong=True)
out["PLANTED_wrong_class_changes_B21"] = bool(sp.simplify(B21w - claim21) != 0)
ok = (shift == a - 2 and explicit == 0 and rec_ok and refl_ok and tab_ok and eq12_ok and eq13_ok and eq15_ok and light_ok)
out["all_claims_hold_and_plants_caught"] = bool(ok and out["PLANTED_wrong_class_changes_B21"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
print(out["eq4_shift"], out["eq4_explicit_form_residual"], rec_ok, refl_ok, tab_ok, eq12_ok, eq13_ok, eq15_ok, light,
      out["PLANTED_wrong_class_changes_B21"], out["all_claims_hold_and_plants_caught"])
