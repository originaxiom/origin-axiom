"""Referee B1804, check 1 (independent of the draft's hand-coded signs).

(a) Build the exterior algebra on R^4 with basis e0=dx1, e1=dy1, e2=dx2, e3=dy2 from permutation signs.
(b) Decompose a general real 2-form F into (p,q) parts in the basis dz1, dzb1, dz2, dzb2 with tau, taub, tp, tpb
    treated as independent symbols (conjugation = swapping tau<->taub, tp<->tpb), and show
       F ^ dz1 ^ dz2  =  c02(F) * dzb1 ^ dzb2 ^ dz1 ^ dz2,
    with dzb1^dzb2^dz1^dz2 = (tau - taub)(tp - tpb) vol  (nonzero on H x H),
    and c20(F) = conj(c02(F)) for real F, so F ^ dz1 ^ dz2 = 0  <=>  F^{0,2} = 0  <=>  F^{2,0} = 0  <=>  F is (1,1).
    Also show F ^ dz1 ^ dzb2 picks out a (1,1) component (so it is NOT an extra condition).
(c) Re-derive the mixed-class condition and compare with the draft's  -Nxx tau tp + Nxy tau + Nyx tp - Nyy.
(d) Intersection form on mixed classes: F_N ^ F_N = -2 det N vol, and the Hodge-index consequence (a (1,1) mixed
    class must have det N > 0) checked against the draft's det -1 statement.
"""
import itertools
import sympy as sp

tau, taub, tp, tpb = sp.symbols("tau taub tp tpb")


def perm_sign(seq):
    s = list(seq); sign = 1
    for i in range(len(s)):
        for j in range(len(s) - 1 - i):
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]; sign = -sign
    return sign


def wedge(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            idx = ka + kb
            if len(set(idx)) < len(idx):
                continue
            key = tuple(sorted(idx))
            out[key] = sp.expand(out.get(key, 0) + perm_sign(idx) * va * vb)
    return {k: v for k, v in out.items() if v != 0}


def one(c):  # 1-form from coefficient list on (dx1, dy1, dx2, dy2)
    return {(i,): sp.sympify(ci) for i, ci in enumerate(c) if ci != 0}


def vol_coeff(f):
    return sp.expand(f.get((0, 1, 2, 3), 0))


dz1, dzb1 = one([1, tau, 0, 0]), one([1, taub, 0, 0])
dz2, dzb2 = one([0, 0, 1, tp]), one([0, 0, 1, tpb])

# general real 2-form: coefficients f_ij (real symbols), basis e_i ^ e_j, i<j
pairs = list(itertools.combinations(range(4), 2))
fs = sp.symbols("f01 f02 f03 f12 f13 f23", real=True)
F = {p: f for p, f in zip(pairs, fs)}

# (b) express e_i in the dz basis: dx = (tau dzb - taub dz)/(tau - taub), dy = (dz - dzb)/(tau - taub)
# Work in an abstract basis u0=dz1,u1=dzb1,u2=dz2,u3=dzb2; e -> u is linear.
D1 = tau - taub; D2 = tp - tpb
e_in_u = {0: {(0,): -taub / D1, (1,): tau / D1},
          1: {(0,): 1 / D1, (1,): -1 / D1},
          2: {(2,): -tpb / D2, (3,): tp / D2},
          3: {(2,): 1 / D2, (3,): -1 / D2}}
Fu = {}
for (i, j), f in F.items():
    w = wedge(e_in_u[i], e_in_u[j])
    for k, v in w.items():
        Fu[k] = sp.simplify(Fu.get(k, 0) + f * v)
c20 = sp.simplify(Fu.get((0, 2), 0))   # dz1 ^ dz2
c02 = sp.simplify(Fu.get((1, 3), 0))   # dzb1 ^ dzb2
conj = {tau: taub, taub: tau, tp: tpb, tpb: tp}
print("(b) c20 - conj(c02) =", sp.simplify(c20 - c02.subs(conj, simultaneous=True)), "(0 => F^{2,0} = conj F^{0,2} for real F)")

lhs = vol_coeff(wedge(wedge(F, dz1), dz2))
basis4 = vol_coeff(wedge(wedge(dzb1, dzb2), wedge(dz1, dz2)))
print("(b) dzb1^dzb2^dz1^dz2 =", sp.factor(basis4), "vol")
print("(b) F^dz1^dz2 - c02 * that =", sp.simplify(lhs - c02 * basis4))

# F ^ dz1 ^ dzb2: which component does it see?  It should be c_{(dzb1? no)}: dz1^dzb2 pairs with the dzb1^dz2 component.
lhs2 = vol_coeff(wedge(wedge(F, dz1), dzb2))
c_b1_2 = sp.simplify(Fu.get((1, 2), 0))  # dzb1 ^ dz2 : a (1,1) component
basis4b = vol_coeff(wedge(wedge(dzb1, dz2), wedge(dz1, dzb2)))
print("(b) F^dz1^dzb2 - c(dzb1^dz2) * basis =", sp.simplify(lhs2 - c_b1_2 * basis4b), "-> it is a (1,1) component, not a condition")

# (c) mixed classes F_N = sum N_ab da1 ^ db2
Nxx, Nxy, Nyx, Nyy = sp.symbols("Nxx Nxy Nyx Nyy")
FN = {(0, 2): Nxx, (0, 3): Nxy, (1, 2): Nyx, (1, 3): Nyy}
cond = vol_coeff(wedge(wedge(FN, dz1), dz2))
draft = -Nxx * tau * tp + Nxy * tau + Nyx * tp - Nyy
print("(c) F_N^dz1^dz2 =", cond, "; minus the draft's expression =", sp.expand(cond - draft))

# solve for tp: Moebius matrix and its determinant
M = sp.Matrix([[-Nxy, Nyy], [-Nxx, Nyx]])
tps = sp.solve(cond, tp)[0]
print("(c) tau' =", sp.simplify(tps), "; check M.tau:", sp.simplify(tps - (M[0, 0] * tau + M[0, 1]) / (M[1, 0] * tau + M[1, 1])),
      "; det M - det N =", sp.expand(M.det() - sp.Matrix([[Nxx, Nxy], [Nyx, Nyy]]).det()))

# (d) intersection form
self_int = vol_coeff(wedge(FN, FN))
print("(d) F_N ^ F_N =", sp.factor(self_int), "vol  (= -2 det N)")
# area forms: always (1,1)
for p in [(0, 1), (2, 3)]:
    print("(d) area form", p, "^ dz1 ^ dz2 =", vol_coeff(wedge(wedge({p: 1}, dz1), dz2)))
# orientation: (i/2) dz ^ dzb = Im tau dx ^ dy > 0
print("(d) (i/2) dz1^dzb1 coefficient of dx1^dy1 =", sp.simplify(sp.I / 2 * wedge(dz1, dzb1)[(0, 1)]), "(= Im tau for taub = conj tau)")
print("r1 exit 0")
