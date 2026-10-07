#!/usr/bin/env python3
"""B1602 -- the count at the new odd-trace carrier (post-census, disclosed): on the forced A4 cover of a thread, at a sign
character nu with an interior class of the four, the extension W1 = [[V, z], [0, 1]] by that class and its reading
(I(W1), I(Lambda^2 W1)) with B1492's stacked index; the per-cusp pattern of the class; the character's trivial cusps.
Controls: +LR at one of its 24 members ((-1, -1) expected as sm:B1550 / the seat's census read it), -LR at one of its six.

    python3 read_carrier.py b+-LLRLRLRR b++LR b+-LR   -> read_<thread>.json beside this file"""
import sys, json, pathlib
import snappy
from mpmath import mpc, mpf
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import forced_every as FE
MC, RM = FE.MC, FE.RM


def run(name):
    M = snappy.Manifold(name); G, eps, label, group, good, ks = FE.forced(M)
    assert label == "A4" and len(ks) == 1, (name, label, len(ks))
    img = ks[0]
    perms = [[group.index(FE.mul(group[i], img[g])) for i in range(len(group))] for g in G.generators()]
    N = M.cover(perms); S = FE.site_of(N)
    out = {"thread": name, "cover_homology": str(N.homology()), "cusps": N.num_cusps(), "members": []}
    for vals, nu in RM.sign_characters(S):
        V = S.four(nu); c = S.counts(V)
        if c["n"] <= 0:
            continue
        interior, other = S.classes(V)
        trivial_cusps = [i for i in range(S.m) if all(abs(nu[g] - 1) < 1e-20 for g in S.gens if any(ch.lower() == g for ch in S.cusps[i][0] + S.cusps[i][1]))]
        m_A = len(S.trivial_cusps(nu)) if hasattr(S, "trivial_cusps") else None
        row = {"nu": list(vals), "h1": c["a1"], "r1": c["r1"], "n": c["n"], "t0": c["t0"], "interior": len(interior), "other": len(other), "readings": []}
        for z, dead in interior:
            W = S.extension(V, z); I1 = S.index(W); L2 = {g: MC.ext2(W[g]) for g in S.gens}; I2 = S.index(L2)
            row["readings"].append({"dead_on_cusps": dead, "I_W1": I1["I"], "I_L2W1": I2["I"], "W1_counts": {k: I1["E"][k] for k in ("a1", "r1", "n")}, "W1dual_counts": {k: I1["Edual"][k] for k in ("a1", "r1", "n")}})
        out["members"].append(row)
        if name != "b+-LLRLRLRR" and len(out["members"]) >= 2:
            break      # the controls: two members suffice
    (HERE / f"read_{name}.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
    print(json.dumps(out, default=str), flush=True)


if __name__ == "__main__":
    for n in sys.argv[1:]:
        run(n)
