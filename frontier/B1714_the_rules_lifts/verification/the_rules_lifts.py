"""B1714 (P-225): where the rule and the moves lift to SU(2).  A move phi lifts at a character chi iff chi o phi equals
chi twisted by a central character eps: F2 -> {+-1} (signs e1, e2 on a, b; tr ab picks up e1 e2).  Traces x = tr a,
y = tr b, z = tr ab.  The rule a -> ab, b -> a acts as (z, x, xz - y) (the Fibonacci trace map); L: a -> a, b -> ab as
(x, z, xz - y); R: a -> ba, b -> b as (z, y, yz - x).  Exact (sympy) fixed sets; the points fixed by two of the three;
the rule's lifts at the common point (rho(a) = i, rho(b) = j) and their eigenvectors' Bloch vectors.  No data.
    python3 -B the_rules_lifts.py      # writes the_rules_lifts.json beside itself"""
import itertools, json, pathlib
import numpy as np
import sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
x, y, z = sp.symbols('x y z')
ACT = {"rule": (z, x, x*z - y), "L": (x, z, x*z - y), "R": (z, y, y*z - x)}
TW = list(itertools.product((1, -1), repeat=2))
def eqs(name, e):
    return [sp.expand(a - b) for a, b in zip(ACT[name], (e[0]*x, e[1]*y, e[0]*e[1]*z))]
fixed = {n: {str(e): [str(s) for s in sp.solve(eqs(n, e), [x, y, z], dict=True)] for e in TW} for n in ACT}
# points fixed by two of the three (each with its own twist): solve the union of the equations
pair_points = {}
for a, b in (("rule", "L"), ("rule", "R"), ("L", "R")):
    pts = set()
    for ea in TW:
        for eb in TW:
            for s in sp.solve(eqs(a, ea) + eqs(b, eb), [x, y, z], dict=True):
                P = tuple(s.get(v, v) for v in (x, y, z))
                pts.add(tuple(str(c) for c in P))
    pair_points["%s,%s" % (a, b)] = sorted(pts)
SPECIAL = {"(0, 0, 0)"} | {str((2*s1, 2*s2, 2*s1*s2)) for s1 in (1, -1) for s2 in (1, -1)}
def tup(p): return "(%s)" % ", ".join(p)
only_special = all(tup(p) in SPECIAL for v in pair_points.values() for p in v)
rule_only_special = all(len(v) == 2 for v in fixed["rule"].values())
# the rule's lifts at the common point
I2 = np.eye(2); qi = np.array([[1j, 0], [0, -1j]]); qj = np.array([[0, 1], [-1, 0]], dtype=complex); qk = qi @ qj
basis = [I2, qi, qj, qk]; A, Bm = qi, qj; RA, RB = A @ Bm, A
SX, SY, SZ = np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])
lifts = {}
for e in TW:
    Msys = np.vstack([np.array([(g @ X - Y @ g).reshape(-1) for g in basis]).T for X, Y in ((A, e[0]*RA), (Bm, e[1]*RB))])
    _, sv, vh = np.linalg.svd(Msys)
    c = vh[-1].conj(); g = sum(ci*b for ci, b in zip(c, basis)); g = g/np.sqrt(np.linalg.det(g))
    q = [float(np.trace(g @ np.conj(b).T).real/2) for b in basis]
    w, V = np.linalg.eig(g)
    blochs = []
    for k in range(2):
        v = V[:, k]/np.linalg.norm(V[:, k]); blochs.append([float(np.real(np.conj(v) @ s @ v)) for s in (SX, SY, SZ)])
    order = next(k for k in range(1, 13) if np.allclose(np.linalg.matrix_power(g, k), I2))
    lifts[str(e)] = {"kernel_sv": float(sv[-1]), "next_sv": float(sv[-2]), "quaternion": q, "order": order, "bloch": blochs,
                     "t_type": all(abs(abs(b) - 1/np.sqrt(3)) < 1e-12 for bl in blochs for b in bl)}
out = {"fixed_sets": fixed, "points_fixed_by_two": pair_points, "only_common_point_and_central": only_special,
       "rule_fixes_two_points_per_twist": rule_only_special, "lifts_at_common_point": lifts,
       "all_eigenvectors_T_type": all(v["t_type"] for v in lifts.values()), "orders": sorted({v["order"] for v in lifts.values()})}
if __name__ == "__main__":
    json.dump(out, open(HERE / "the_rules_lifts.json", "w"), indent=1)
    print("only the common point and the central characters:", only_special, "| rule:", rule_only_special,
          "| T-type:", out["all_eigenvectors_T_type"], "| orders", out["orders"])
    for k, v in pair_points.items(): print(k, v)
