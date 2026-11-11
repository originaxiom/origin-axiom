#!/usr/bin/env python3
"""SM-C1, harvest row 1488 (TWO_HEAT_RESPONSES_AUTHOR_AUDIT_2026_10_29 @ db1d44b69): this seat's own check of the
unspecialised B21, B31 (charges kept apart, evenness in q used), B_C, h_C = (12/5)[delta(L^2) - delta(L^3)], the
full-family countercontrol (-4, -6) and (-4/5, 6/5) with determinant -48/5, K_a^0 = -y^2 Delta + i a y Dbar, and the two
norm identities. Planted: the order-seven alias T_4 = T_3, T_6 = T_1 applied to the order-two line must give a different
second vector."""
import json
import sys
from pathlib import Path

import sympy as sp

R = sp.Rational
Psi = {q: sp.Symbol("Psi%d" % q) for q in (2, 3)}
T = {q: sp.Symbol("T%d" % q) for q in (1, 3, 4, 6)}
Phi05 = sp.Symbol("Phi0_5")
# row 1421's coefficients, copies 2 (five), 2 (ten), 1 (adjoint); evenness: Psi_-2 = Psi_2, T_-4 = T_4, Phi0(-5) = Phi0(5)
B21 = 2 * (R(1, 5) * Psi[3] - R(1, 5) * Psi[2]) + 2 * (R(7, 5) * T[1] - R(4, 5) * T[4] - R(3, 5) * T[6]) + (-1 - 1) * Phi05
B31 = 2 * (-R(3, 10) * Psi[3] + R(3, 10) * Psi[2]) + 2 * (R(9, 10) * T[1] - R(3, 10) * T[4] - R(6, 10) * T[6]) \
      + (-R(3, 2) - R(3, 2)) * Phi05
c21 = R(2, 5) * (Psi[3] - Psi[2]) + R(2, 5) * (7 * T[1] - 4 * T[4] - 3 * T[6]) - 2 * Phi05
c31 = R(3, 5) * (Psi[2] - Psi[3]) + R(1, 5) * (9 * T[1] - 3 * T[4] - 6 * T[6]) - 3 * Phi05
BC = sp.expand(B31 - R(3, 2) * B21)
cBC = R(6, 5) * (Psi[2] - Psi[3]) + R(9, 5) * T[4] + R(3, 5) * T[6] - R(12, 5) * T[1]
out = {"B21_holds": sp.simplify(B21 - c21) == 0, "B31_holds": sp.simplify(B31 - c31) == 0,
       "BC_holds": sp.simplify(BC - cBC) == 0, "BC": str(BC)}
# infrared limits for a general line: Phi_1(q) -> 2[delta(L^q) - 1], Phi_j>=2 -> 0, Phi_0(q) -> 2[(d(eta L^q) - d(eta)) - (d(L^q) - 1)]
def ir(delta, deta, deta_q):
    sub = {Psi[2]: 2 * (delta(2) - 1), Psi[3]: 2 * (delta(3) - 1), T[1]: 0, T[3]: 0, T[4]: 0, T[6]: 0,
           Phi05: 2 * ((deta_q(5) - deta) - (delta(5) - 1))}
    return sp.simplify(c21.subs(sub)), sp.simplify(c31.subs(sub)), sp.simplify(cBC.subs(sub))
d2, d3 = sp.symbols("d2 d3")
_, _, hC = ir(lambda q: {2: d2, 3: d3, 5: 0}[q], 0, lambda q: 0)
out["h_C"] = str(sp.expand(hC))
out["h_C_holds"] = sp.simplify(hC - R(12, 5) * (d2 - d3)) == 0
# order seven, nontrivial spin: delta(L^q) = 0 for q = 2, 3, 5; eta nontrivial, eta L^5 nontrivial
v1 = ir(lambda q: 0, 0, lambda q: 0)[:2]
# order two, trivial spin: L^2 = O, L^3 = L, L^5 = L nontrivial; eta = O so delta(eta) = 1, delta(eta L^5) = delta(L) = 0
v2 = ir(lambda q: {2: 1, 3: 0, 5: 0}[q], 1, lambda q: 0)[:2]
det = sp.Matrix([list(v1), list(v2)]).det()
out["countercontrol"] = {"order7_nontrivial_spin": [str(x) for x in v1], "order2_trivial_spin": [str(x) for x in v2],
                         "det": str(det)}
cc_ok = [sp.nsimplify(x) for x in v1] == [-4, -6] and [sp.nsimplify(x) for x in v2] == [R(-4, 5), R(6, 5)] \
        and det == R(-48, 5)
# K_a^0 and the norms
X, Y = sp.symbols("x y", real=True)
a = sp.Symbol("a")
f = sp.Function("f")(X, Y)
Db = lambda h: sp.diff(h, X) + sp.I * sp.diff(h, Y)
Dz = lambda h: sp.diff(h, X) - sp.I * sp.diff(h, Y)
K0 = -Y ** (2 - a) * Dz(Y ** a * Db(f))
k0_ok = sp.simplify(sp.expand(K0 - (-Y ** 2 * (sp.diff(f, X, 2) + sp.diff(f, Y, 2)) + sp.I * a * Y * Db(f)))) == 0
Om, g = sp.symbols("Omega g", positive=True)
norms_ok = sp.simplify(Om ** (4 - a) * (Om ** -2 * g) ** 2 - Om ** (-a) * g ** 2) == 0 and \
           sp.simplify(Om ** a * (Om ** (-a) * g) ** 2 - Om ** (-a) * g ** 2) == 0
out["K0_form_holds"], out["norms_hold"] = k0_ok, norms_ok
# planted: the order-seven alias T4 = T3, T6 = T1 is harmless in the IR (T -> 0); alias Phi0(5) -> Phi0(2) with the
# order-two line (L^2 = O) changes Phi0's IR limit: delta(L^2) = 1, delta(eta L^2) = 1 -> 2[(1 - 1) - (1 - 1)] = 0 too;
# the alias that matters is Psi: taking Psi_3 as Psi_(-4) (order-seven, -4 = 3) on the order-two line, where L^-4 = O
v2_alias = ir(lambda q: {2: 1, 3: 1, 5: 0}[q], 1, lambda q: 0)[:2]
out["PLANTED_order7_alias_on_order2_line"] = {"vector": [str(x) for x in v2_alias],
                                              "caught": [sp.nsimplify(x) for x in v2_alias] != [R(-4, 5), R(6, 5)]}
ok = out["B21_holds"] and out["B31_holds"] and out["BC_holds"] and out["h_C_holds"] and cc_ok and k0_ok and norms_ok
out["countercontrol_holds"] = cc_ok
out["all_claims_hold_and_plants_caught"] = bool(ok and out["PLANTED_order7_alias_on_order2_line"]["caught"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1, default=str))
