"""Referee B1808, check 4.
(a) The first launch's B_4 count 160 vs the corrected 138: the 22 extra pairs have det Gram(w, u) = 0 -- a degenerate
    plane, whose (1,1) loci are tangent on the real boundary (a real double root), so no point of H x H exists; the
    first launch's floating-point root finder reported them.  Count det = 0 pairs exactly and show the double root.
(b) The minimum of det NS over points on the LR chi = -3 curve is 3 (A_2(-1)); show that that point is B1804's
    Q(sqrt5, sqrt-3) point up to the curve's own data, and that A_2(-1) carries three pairs of norm -6 classes.
(c) Does A_2(-1) embed in Lambda_A for the null matrices (search |coeff| <= 6)?
"""
import itertools, json, math, pathlib
import sympy as sp
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
AUTH = json.loads((HERE.parent / "three_generations_in_f2h.json").read_text())
out = {}
# (a)
G = sp.Matrix(AUTH["B_4"]["Gram Q"]); w = sp.Matrix(AUTH["B_4"]["w (chi = -3)"])
zero = []
for cu in itertools.product(range(-2, 3), repeat=4):
    if all(x == 0 for x in cu) or math.gcd(*cu) != 1: continue
    u = sp.Matrix(cu)
    d = -6 * (u.T * G * u)[0] - ((w.T * G * u)[0]) ** 2
    if d == 0: zero.append(cu)
out["B_4: primitive u in [-2,2]^4 with det Gram(w,u) = 0"] = len(zero)
out["B_4: first launch minus corrected count"] = 160 - 138
# a degenerate plane <w,u> has a null direction n (Q(n, w) = Q(n, u) = Q(n, n) = 0 on the plane); w^perp cap u^perp is
# then (1,1)-tangent to the real quadric: the two (1,1) curves meet only at a real boundary point (double root).
# (b) A_2(-1) vectors of norm -6
A2 = sp.Matrix([[-2, -1], [-1, -2]])
n6 = [(x, y) for x in range(-3, 4) for y in range(-3, 4) if (sp.Matrix([[x, y]]) * A2 * sp.Matrix([x, y]))[0] == -6]
out["A_2(-1): vectors of norm -6"] = n6
q2 = json.loads((HERE / "q2_points.json").read_text())
rows3 = [r for r in q2["LR"]["rows"] if r["det NS (saturated)"] == 3]
out["LR: planes on w's curve with det NS = 3"] = [(r["u's"], r["NS Gram"]) for r in rows3]


# (c) search for x, y in Lambda_A with Q(x) = Q(y) = -2, Q(x, y) = -1 (an A_2(-1)), |coeff| <= 6
def find_A2(Gm, R=6):
    Gm = np.array(Gm, dtype=int)
    vecs = [np.array(c) for c in itertools.product(range(-R, R + 1), repeat=4) if any(c)]
    m2 = [v for v in vecs if v @ Gm @ v == -2]
    for i, x in enumerate(m2):
        for y in m2[i + 1:]:
            if abs(x @ Gm @ y) == 1:
                return x.tolist(), y.tolist(), len(m2)
    return None, None, len(m2)


for name in ("LR", "B_4", "B_5", "B_6", "B_7"):
    x, y, n = find_A2(AUTH[name]["Gram Q"])
    out["%s: an A_2(-1) inside Lambda_A (|coeff| <= 6)" % name] = {"x": x, "y": y, "norm -2 vectors found": n}
for k, v in out.items():
    print(k, ":", v)
(HERE / "q4_first_launch_and_A2.json").write_text(json.dumps(out, indent=1, default=str))
print("q4 exit 0")
