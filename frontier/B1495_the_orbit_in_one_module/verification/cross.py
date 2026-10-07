#!/usr/bin/env python3
"""B1495 -- the orbit in one module.  On a manifold N with members nu_1..nu_m (sign characters of the four with one
interior class each; B1492's survey), W_i = W1(nu_i) = [[V_i, z_i], [0, 1]] (rank 5).  The orbit module W = (+) W_i has
I(W) = sum I(W_i) (additivity) and Lambda^2 W = (+) Lambda^2 W_i (+) (+)_{i<j} W_i (x) W_j, so
    I(Lambda^2 W) = sum_i I(Lambda^2 W_i) + sum_{i<j} I(W_i (x) W_j).
This reads the cross terms I(W_i (x) W_j) (rank 25) with B1492's stacked instrument, and the orbit's two indices.
Usage: cross.py <name>  (members from B1492's survey_<name>.json; or --control m136)."""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "B1492_the_three_ended_companion_read" / "verification"))   # parents[2] = frontier/ (the sealed file said parents[1], the arc directory: an import error, corrected before any reading)
import multicusp as MC
from mpmath import mpc, matrix, zeros
HERE = pathlib.Path(__file__).resolve().parent


def kron(A, B):
    n, m = A.rows, B.rows; K = zeros(n * m)
    for i in range(n):
        for j in range(n):
            if A[i, j] == 0: continue
            for k in range(m):
                for l in range(m): K[i * m + k, j * m + l] = A[i, j] * B[k, l]
    return K


def members(S, survey):
    out = []
    for r in survey["rows"]:
        if r["interior"] == 1:
            nu = {g: mpc(r["nu"][g]) for g in S.gens}; V = S.four(nu); interior, other = S.classes(V)
            assert len(interior) == 1; z, dead = interior[0]; out.append(dict(nu=r["nu"], V=V, W=S.extension(V, z), dead=dead))
    return out


def run(name, survey_path):
    S = MC.Site(name); survey = json.load(open(survey_path)); ms = members(S, survey); print(name, "members:", [m["nu"] for m in ms], flush=True)
    res = dict(name=name, members=[m["nu"] for m in ms], single=[], cross=[])
    for m in ms:
        a, b = S.index(m["W"]), S.index({g: MC.ext2(m["W"][g]) for g in S.gens}); res["single"].append(dict(nu=m["nu"], I_W1=a["I"], I_L2W1=b["I"])); print("  W1", m["nu"], a["I"], b["I"], flush=True)
    for i in range(len(ms)):
        for j in range(i + 1, len(ms)):
            T = {g: kron(ms[i]["W"][g], ms[j]["W"][g]) for g in S.gens}
            relok = all(max(abs(x) for x in (MC.word(r, T) - MC.eye(25))) < 1e-20 for r in S.rels)
            c = S.index(T); res["cross"].append(dict(i=i, j=j, I=c["I"], E=c["E"], Edual=c["Edual"], relator_ok=relok)); print("  cross", i, j, "I =", c["I"], "relator ok", relok, c["E"], flush=True)
    res["I_W"] = sum(x["I_W1"] for x in res["single"]); res["I_L2W"] = sum(x["I_L2W1"] for x in res["single"]) + sum(x["I"] for x in res["cross"])
    print("ORBIT", name, "I(W) =", res["I_W"], "I(Lambda^2 W) =", res["I_L2W"], "(singles", sum(x["I_L2W1"] for x in res["single"]), "+ cross", sum(x["I"] for x in res["cross"]), ")")
    json.dump(res, open(HERE / f"cross_{name}.json", "w"), indent=1, default=str); return res


if __name__ == "__main__":
    if sys.argv[1] == "--control":
        run(sys.argv[2], str(HERE.parents[1] / "B1492_the_three_ended_companion_read" / "verification" / f"control_{sys.argv[2]}.json"))
    else:
        run(sys.argv[1], str(HERE.parents[1] / "B1492_the_three_ended_companion_read" / "verification" / f"survey_{sys.argv[1]}.json"))
