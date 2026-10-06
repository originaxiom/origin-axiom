#!/usr/bin/env python3
"""B1486 CONTROL 2 (before the seal): the three-generator, two-relator code path on a NON-member of m135 (nu trivial,
V = four), where H^1(V) has one boundary-type class and no interior one -- not a sealed object.  (i) the series expansion:
c alone is unobstructed (W exists); (ii) the numerical index of W = [[V, c], [0, 1]] and of its exterior square against
the exact instrument of B1485 (second_route.reading), count by count; (iii) the exterior square path on the m004 control."""
import sys, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "frontier").is_dir())
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(ROOT / "frontier" / "B1485_the_silver_members_by_a_second_route" / "verification"))
import second_route as SR, fused as F, fused_cell as FC
from mpmath import mp, mpf, matrix, eye, zeros, inverse, nstr, norm
mp.dps = 50
Sd = SR.load(ROOT / "frontier" / "B1485_the_silver_members_by_a_second_route" / "verification" / "members_for_main.json", "-LLRR")
gens, rels, cusp = Sd["gens"], Sd["rels"], tuple(Sd["cusp"])
nu = {"a": 1, "b": 1, "t": 1}; V = SR.frame(Sd, nu); interior, boundary = SR.classes(Sd, V)
assert len(interior) == 0 and len(boundary) == 1, (len(interior), len(boundary))
z = FC.cxvec(boundary[0]); S = {}; N = {}
for k, g in enumerate(gens):
    M = zeros(5, 5); A = FC.cxmat(V[g])
    for i in range(4):
        for j in range(4): M[i, j] = A[i, j]
    M[4, 4] = 1; S[g] = M; P = zeros(5, 5)
    for i in range(4): P[i, 4] = z[k * 4 + i]
    N[g] = P
out = {}
ob = F.obstruction(gens, rels, S, {g: N[g] * inverse(S[g]) for g in gens})
out["c alone (3 generators, 2 relators)"] = dict(first_order_residual=nstr(ob["first_order_residual"], 3), rank_L=ob["rank_L"], residual=nstr(ob["residual"], 3))
W = {g: S[g] + N[g] for g in gens}
num = F.index(gens, rels, cusp, W); ex = SR.reading(Sd, SR.extension(Sd, V, boundary[0]), "W")
num2 = F.index(gens, rels, cusp, {g: FC.ext2_num(W[g]) for g in gens}); ex2 = SR.reading(Sd, {g: SR.ext2(SR.extension(Sd, V, boundary[0])[g]) for g in gens}, "L2W")
out["W: numeric vs exact"] = dict(numeric=num, exact=dict(I=ex["I"], E=ex["E"], Edual=ex["Edual"]), agree=(num["I"] == ex["I"] and num["E"] == ex["E"] and num["Edual"] == ex["Edual"]))
out["L2W: numeric vs exact"] = dict(numeric=num2, exact=dict(I=ex2["I"], E=ex2["E"], Edual=ex2["Edual"]), agree=(num2["I"] == ex2["I"] and num2["E"] == ex2["E"] and num2["Edual"] == ex2["Edual"]))
ok = float(ob["first_order_residual"]) < 1e-40 and float(ob["residual"]) < 1e-40 and out["W: numeric vs exact"]["agree"] and out["L2W: numeric vs exact"]["agree"]
print(json.dumps(out, indent=1, default=str)); print("CONTROL 2 PASS:", ok)
json.dump(dict(out, control_pass=ok), open(HERE / "control_three_generators.json", "w"), indent=1, default=str)
