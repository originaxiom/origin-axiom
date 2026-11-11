#!/usr/bin/env python3
"""SM-C2, harvest row 1537 (REGISTER_FLAVOUR_ACTION_GRAM_AND_QUARTIC_STATE_TEST @ e19aa4ddc): this seat's own exact check
of (a) [Q', R'] = det(U)[Q, R] and U^T eps U = det(U) eps for symbolic U and random matrices; (b) the Gram law (2):
[D, Fi] = [D, Fj] = 0 forces D = N I2 (one generator alone does not); on the EW branch D = (5/l^2) diag(|a|^2, |b|^2), so
|a| = |b| = 1/sqrt2 and N = 5/(2 l^2); (c) the two-triple traces with kappa = (1/2) Tr_10: kappa(E+^dag E+) =
kappa(E-^dag E-) = 10, kappa(H+^2) = kappa(H-^2) = 20, kappa(H+ H-) = 0; (d) the quartic (3)-(5): C_Phi(z) =
kappa([X_z, X_z^dag]^2) on Phi0 = n(E, G), n = 1/(2 sqrt2 l), and on gL Phi0, gR Phi0 with gL = (I + Fi)/sqrt2,
gR = (I - Fj)/sqrt2, equals C[r2^2 + s^2] with s = sx, sy, sz respectively and C = 5/(8 l^4), as polynomials in
Re/Im z; the readout (6) [[2,1,1],[1,2,1],[1,1,2]] C; all three have Gram N I2; (e) covariance X_(U Phi)(U^-T z) = X_Phi(z).
Planted: gL replaced by the identity must make rows Phi0 and PhiL of (6) equal (the discriminator then fails)."""
import json
import random
import sys
from pathlib import Path

import sympy as sp

out = {}
# ---------- D5 matrices (as in row 1525) ----------
H5 = sp.diag(-4, -2, 0, 2, 4)
E5 = sp.zeros(5)
for i, c in enumerate([2, sp.sqrt(6), sp.sqrt(6), 2]):
    E5[i + 1, i] = c
BZ = sp.zeros(5)
for (i, j, c) in [(1, 4, sp.sqrt(sp.Rational(2, 5))), (2, 3, -sp.sqrt(sp.Rational(3, 5)))]:
    BZ[i, j] += c
    BZ[j, i] -= c
J5 = sp.zeros(5)
for i, s in enumerate([1, -1, 1, -1, 1]):
    J5[i, 4 - i] = s
Z5 = sp.zeros(5)
blk = lambda A, B_, C, D: sp.Matrix(sp.BlockMatrix([[A, B_], [C, D]]))
E = blk(E5, Z5, Z5, -E5.T)
G = sp.sqrt(10) * (blk(Z5, BZ, Z5, Z5) + blk(Z5, Z5, J5 * BZ * J5, Z5))
kap = lambda A, B_: sp.nsimplify(sp.simplify((A * B_).trace() / 2))
comm = lambda A, B_: A * B_ - B_ * A
# (a)
random.seed(1537)
rm = lambda: sp.Matrix(3, 3, lambda i, j: sp.Rational(random.randint(-5, 5), random.randint(1, 3)))
Q, R = rm(), rm()
u11, u12, u21, u22 = sp.symbols("u11 u12 u21 u22")
Qp, Rp = u11 * Q + u12 * R, u21 * Q + u22 * R
a_ok = sp.expand(comm(Qp, Rp) - (u11 * u22 - u12 * u21) * comm(Q, R)) == sp.zeros(3)
Um = sp.Matrix([[u11, u12], [u21, u22]])
eps = sp.Matrix([[0, 1], [-1, 0]])
a_ok = a_ok and sp.expand(Um.T * eps * Um - Um.det() * eps) == sp.zeros(2)
# (b)
x, y = sp.symbols("x y", real=True)
zz = sp.Symbol("z")
D = sp.Matrix([[x, zz], [sp.conjugate(zz), y]])
Fi = sp.diag(sp.I, -sp.I)
Fj = sp.Matrix([[0, 1], [-1, 0]])
sol_both = sp.solve(list(comm(D, Fi)) + list(comm(D, Fj)), [zz, y], dict=True)
sol_one = sp.solve(list(comm(D, Fi)), [zz], dict=True)
b_ok = sol_both == [{zz: 0, y: x}] and sol_one == [{zz: 0}]
a_, b_ = sp.symbols("a b")
l = sp.Symbol("ell", positive=True)
qh, rh = a_ * E / (2 * l), b_ * G / (2 * l)
Phi = [qh, rh]
Dm = sp.Matrix(2, 2, lambda i, j: kap(Phi[j].H, Phi[i]))
b_ok = b_ok and sp.simplify(Dm - 5 / l ** 2 * sp.diag(a_ * sp.conjugate(a_), b_ * sp.conjugate(b_))) == sp.zeros(2)
N_half = sp.simplify((5 / l ** 2) * sp.Rational(1, 2))
out["(b)_N_at_|a|=|b|=1/sqrt2"] = str(N_half)
b_ok = b_ok and N_half == 5 / (2 * l ** 2)
# (c)
Ep, Em = (E + G) / 2, (E - G) / 2
Hp, Hm = comm(Ep, Ep.H), comm(Em, Em.H)
traces = {"k(E+dE+)": kap(Ep.H, Ep), "k(E-dE-)": kap(Em.H, Em), "k(H+^2)": kap(Hp, Hp), "k(H-^2)": kap(Hm, Hm),
          "k(H+H-)": kap(Hp, Hm)}
out["(c)_traces"] = {k: str(v) for k, v in traces.items()}
c_ok = [traces[k] for k in traces] == [10, 10, 20, 20, 0]
# (d)
x1, y1, x2, y2 = sp.symbols("x1 y1 x2 y2", real=True)
z1, z2 = x1 + sp.I * y1, x2 + sp.I * y2
n = 1 / (2 * sp.sqrt(2) * l)
gL = (sp.eye(2) + Fi) / sp.sqrt(2)
gR = (sp.eye(2) - Fj) / sp.sqrt(2)


def state(g):
    return [n * (g[0, 0] * E + g[0, 1] * G), n * (g[1, 0] * E + g[1, 1] * G)]


def C_of(ph, zv):
    X = zv[0] * ph[0] + zv[1] * ph[1]
    K = comm(X, X.H)
    return sp.expand(sp.simplify((K * K).trace() / 2))


r2 = sp.expand(x1 ** 2 + y1 ** 2 + x2 ** 2 + y2 ** 2)
sx = sp.expand(2 * sp.re(sp.expand_complex(z1 * sp.conjugate(z2))))
sy = sp.expand(2 * sp.im(sp.expand_complex(sp.conjugate(z1) * z2)))
sz = sp.expand(x1 ** 2 + y1 ** 2 - x2 ** 2 - y2 ** 2)
Cc = sp.Rational(5, 8) / l ** 4
forms = {}
states = {"Phi0": state(sp.eye(2)), "PhiL": state(gL), "PhiR": state(gR)}
for (name, ph), s_ in zip(states.items(), (sx, sy, sz)):
    val = C_of(ph, (z1, z2))
    forms[name] = sp.simplify(val - Cc * (r2 ** 2 + s_ ** 2)) == 0
out["(d)_forms_match"] = forms
probes = {"zx": (1 / sp.sqrt(2), 1 / sp.sqrt(2)), "zy": (1 / sp.sqrt(2), sp.I / sp.sqrt(2)), "zz": (1, 0)}
readout = [[sp.simplify(C_of(states[s_], probes[p]) / Cc) for p in probes] for s_ in states]
out["(d)_readout_over_C"] = [[str(v) for v in row] for row in readout]
grams = {s_: sp.simplify(sp.Matrix(2, 2, lambda i, j: kap(ph[j].H, ph[i]))) for s_, ph in states.items()}
out["(d)_grams"] = {k: [str(v) for v in m] for k, m in grams.items()}
d_ok = (all(forms.values()) and readout == [[2, 1, 1], [1, 2, 1], [1, 1, 2]]
        and all(m == 5 / (2 * l ** 2) * sp.eye(2) for m in grams.values()))
# (e) covariance
w1, w2 = sp.symbols("w1 w2")
Ug = gR
zp = (Ug.T).inv() * sp.Matrix([w1, w2])
P0 = states["Phi0"]
UPhi = [Ug[0, 0] * P0[0] + Ug[0, 1] * P0[1], Ug[1, 0] * P0[0] + Ug[1, 1] * P0[1]]
e_ok = sp.simplify(zp[0] * UPhi[0] + zp[1] * UPhi[1] - (w1 * P0[0] + w2 * P0[1])) == sp.zeros(10)
out["checks_ok"] = {"a": a_ok, "b": b_ok, "c": c_ok, "d": d_ok, "e": e_ok}
bad_row = [sp.simplify(C_of(state(sp.eye(2)), probes[p]) / Cc) for p in probes]
out["PLANTED_identity_gL_row"] = [str(v) for v in bad_row]
out["PLANTED_caught"] = bad_row == readout[0] and bad_row != readout[1]
out["all_claims_hold_and_plants_caught"] = bool(all(out["checks_ok"].values()) and out["PLANTED_caught"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1, default=str))
