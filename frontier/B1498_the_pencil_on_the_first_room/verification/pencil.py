#!/usr/bin/env python3
"""B1498 -- the pencil of rank-five extensions on o10_150691 at the eight order-four characters where the four has TWO interior
classes c1, c2 (B1497).  The rank-five object of the physics is ONE extension W1(z) = [[V, z], [0, 1]] (the line trivial at
order four), z = a c1 + b c2 -- a P^1 of them.  Reads I(W1), I(Lambda^2 W1) at the basis classes, at z = c1 + lambda c2 for
lambda in {1, -1, i, 2, random}, and reports the generic value (the least, by the SM seat's Lemma G) and the special ones.
Also the rank-six extension by both classes at once, [[V, (c1 c2)], [0, 1_2]] (outside the rank-five dictionary; for the record).
Uses B1492's multicusp Site and B1493's room instrument.  Writes pencil_o10_150691.json."""
import sys, json, pathlib, itertools, random
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1492_the_three_ended_companion_read" / "verification"))
sys.path.insert(0, str(HERE.parents[1] / "B1493_the_room_on_the_companions" / "verification"))
import multicusp as MC, room as RM
from mpmath import mpc, zeros, mpf
random.seed(1498)
S = RM.site("o10_150691"); gens = S.gens


def ext2(W): return {g: MC.ext2(W[g]) for g in gens}


def read_z(V, z):
    W = S.extension(V, z); a = S.index(W); b = S.index(ext2(W))
    relok = all(max(abs(x) for x in (MC.word(r, W) - MC.eye(5))) < 1e-20 for r in S.rels)
    return dict(I_W1=a["I"], I_L2W1=b["I"], n=a["E"]["n"], n_dual=a["Edual"]["n"], relator_ok=relok)


out = []
chars = [[2, 0, 0], [2, 2, 2], [2, 4, 4], [2, 6, 6], [6, 0, 0], [6, 2, 2], [6, 4, 4], [6, 6, 6]]
which = chars if len(sys.argv) < 2 else [list(map(int, w.split(","))) for w in sys.argv[1:]]
for ks in which:
    nu = {g: RM.zeta(k) for g, k in zip(gens, ks)}; assert RM.is_character(S, nu)
    V = S.four(nu); interior, other = S.classes(V); assert len(interior) == 2, (ks, len(interior))
    (c1, d1), (c2, d2) = interior
    row = dict(exponents=ks, basis=[read_z(V, c1), read_z(V, c2)], pencil={})
    lams = {"1": mpc(1), "-1": mpc(-1), "i": mpc(0, 1), "2": mpc(2), "random": mpc(random.uniform(-2, 2), random.uniform(-2, 2)), "random2": mpc(random.uniform(-2, 2), random.uniform(-2, 2))}
    for name, lam in lams.items():
        z = c1 + lam * c2; row["pencil"][name] = read_z(V, z)
    # the rank-six extension by both classes
    n = 4; W6 = {}
    for k, g in enumerate(gens):
        W = zeros(6); W[:4, :4] = V[g]
        for i in range(4): W[i, 4] = c1[k * 4 + i]; W[i, 5] = c2[k * 4 + i]
        W[4, 4] = 1; W[5, 5] = 1; W6[g] = W
    a = S.index(W6); row["rank6_both"] = dict(I=a["I"], n=a["E"]["n"], n_dual=a["Edual"]["n"], relator_ok=all(max(abs(x) for x in (MC.word(r, W6) - MC.eye(6))) < 1e-20 for r in S.rels))
    vals = [row["basis"][0]["I_W1"], row["basis"][1]["I_W1"]] + [v["I_W1"] for v in row["pencil"].values()]
    row["generic_I_W1"] = min(vals); row["special_values"] = sorted(set(vals))
    out.append(row); print(ks, "basis", [(b["I_W1"], b["I_L2W1"]) for b in row["basis"]], "pencil", {k: (v["I_W1"], v["I_L2W1"]) for k, v in row["pencil"].items()}, "rank6 I =", a["I"], "generic", row["generic_I_W1"], flush=True)
    json.dump(out, open(HERE / "pencil_o10_150691.json", "w"), indent=1, default=str)
print("PENCIL generic I(W1) over the eight characters:", [r["generic_I_W1"] for r in out], "rank-6 I:", [r["rank6_both"]["I"] for r in out])
