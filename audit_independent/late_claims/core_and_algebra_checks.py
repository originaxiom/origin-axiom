"""Independent recomputation of the core object and of agy's small algebraic claims (exact / SnapPy)."""
from __future__ import annotations

import json
import warnings

import sympy as sp

warnings.filterwarnings("ignore")
import snappy  # noqa: E402

res = {}
M = snappy.Manifold("m004")
K = snappy.Manifold("4_1")
res["m004"] = {
    "volume": float(M.volume()), "4_1_volume": float(K.volume()), "is_isometric_to_4_1": bool(M.is_isometric_to(K)),
    "H1": str(M.homology()), "cusps": M.num_cusps(), "CS": float(M.chern_simons()),
    "fibered_monodromy_check": "see LR below",
}
# Clausen form 6*Lambda(pi/3) = 2*Cl2(pi/3)*... check
cl = sp.N(2 * sp.Rational(3, 1) * sp.Integral(-sp.log(2 * sp.sin(sp.Symbol('t'))), (sp.Symbol('t'), 0, sp.pi / 3)), 20)
res["m004"]["6*Lobachevsky(pi/3)"] = float(cl)

L = sp.Matrix([[1, 1], [0, 1]]); R = sp.Matrix([[1, 0], [1, 1]]); A = L * R
res["LR"] = {"A": A.tolist(), "trace": int(A.trace()), "det": int(A.det()), "charpoly": str(A.charpoly().as_expr()),
             "det(A-I)": int((A - sp.eye(2)).det())}
t = sp.symbols("t")
res["alexander"] = {"Delta(t)": "t - 3 + 1/t", "|Delta(omega)|": float(abs(sp.N((sp.exp(2 * sp.pi * sp.I / 3) - 3 + sp.exp(-2 * sp.pi * sp.I / 3)))))}
w = sp.exp(2 * sp.pi * sp.I / 3)
res["agy_RS_torsion_claim"] = {"|Delta(w)|/|1-w|": float(sp.N(4 / sp.Abs(sp.expand_complex(1 - w)))), "4/sqrt3": float(4 / sp.sqrt(3)),
                               "note": "this is |Delta(w)|/|1-w|, the (Milnor/Reidemeister) abelian torsion of the twisted chain complex up to conventions; it is a number about m004, but nothing derives its log as an SU(3) threshold"}

# torsion-free bundles among short positive words (T-ROOT check)
import itertools
tf = []
for n in range(1, 9):
    for word in itertools.product("LR", repeat=n):
        Mw = sp.eye(2)
        for c in word:
            Mw = Mw * (L if c == "L" else R)
        if abs((Mw - sp.eye(2)).det()) == 1:
            tf.append("".join(word))
res["T_ROOT_words_len<=8_with_|det(phi-I)|=1"] = sorted(set(tf))

A3 = A ** 3
U = (A3 - sp.eye(2)) / 4
res["cover_monodromy"] = {"A^3": A3.tolist(), "(A^3-I)/4": U.tolist(), "det": int(U.det()), "trace": int(U.trace()),
                          "agy_relay_U_[[1,2],[2,3]]_equals_(A^3-I)/4": U == sp.Matrix([[1, 2], [2, 3]]),
                          "det(A^3-I)": int((A3 - sp.eye(2)).det())}
for nm, Um in [("U=(A^3-I)/4", U), ("U_relay=[[1,2],[2,3]]", sp.Matrix([[1, 2], [2, 3]]))]:
    Um5 = Um.applyfunc(lambda x: x % 5)
    sq = (Um * Um).applyfunc(lambda x: x % 5)
    img = (Um * sp.Matrix([2, 0])).applyfunc(lambda x: x % 5)
    eig = [(lam, [(a, b) for a in range(5) for b in range(5) if (a, b) != (0, 0) and ((Um * sp.Matrix([a, b]) - lam * sp.Matrix([a, b])).applyfunc(lambda x: x % 5) == sp.zeros(2, 1))]) for lam in range(5)]
    res["phase1_" + nm] = {"U^2 mod 5": sq.tolist(), "U^2==I mod 5 (relay claim)": sq == sp.eye(2),
                           "U*(2,0) mod 5": img.T.tolist(), "is (2,0) an eigenvector mod 5": any((2, 0) in v for _, v in eig),
                           "eigenvectors mod 5": {lam: v for lam, v in eig if v}}
# A^3-fixed 5-torsion points on the fibre?
fixed5 = [(a, b) for a in range(5) for b in range(5) if ((A3 - sp.eye(2)) * sp.Matrix([a, b])).applyfunc(lambda x: x % 5) == sp.zeros(2, 1) and (a, b) != (0, 0)]
res["A^3_fixed_nonzero_5torsion_points"] = fixed5

# Phase 5: Riley rep of the figure-eight group
om = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2
a = sp.Matrix([[1, 1], [0, 1]]); b = sp.Matrix([[1, 0], [-om, 1]])
lhs = a * b.inv() * a.inv() * b * a; rhs = b * a * b.inv() * a.inv() * b
res["riley_relation_exact"] = sp.simplify(lhs - rhs) == sp.zeros(2, 2)

# Theorem 9A: |1+c^2| for the lepton choice c_e=-1, and an alternative uniform rule
res["theorem9A"] = {"|1+c_e^2| with c_e=-1": 2, "norm_preserving_requires": "|1+c^2|=1",
                    "uniform_quark_rule_applied_to_lepton(k_R=3 -> k^2 mod 8 = 1)": "1+c_e^2 = e^{i pi/4}, c_e=-sqrt(e^{i pi/4}-1) (same as down)"}
print(json.dumps(res, indent=1, default=str))
json.dump(res, open("core_and_algebra_checks.json", "w"), indent=1, default=str)
