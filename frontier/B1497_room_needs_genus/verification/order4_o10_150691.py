#!/usr/bin/env python3
"""B1497 G6 -- o10_150691 at its characters of order four (nu^4 = 1: the line L = nu^-4 is trivial, b0 = 1, Theorem C's cap
is 1 + n(1) = 2): every class of H^1(nu (x) four) read in W1 = [[V, z], [0, 1]] with its cusp decomposition, by B1493's
instrument (room.py's Room.read).  Writes order4_o10_150691.json."""
import sys, json, pathlib, itertools
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1493_the_room_on_the_companions" / "verification"))
import room as RM
from mpmath import mpc
S = RM.site("o10_150691"); gens = S.gens; print("gens", gens, "rels", len(S.rels), "cusps", S.m, flush=True)
out = []; n_char = 0
for ks in itertools.product((0, 2, 4, 6), repeat=len(gens)):
    if all(k % 4 == 0 for k in ks): continue                      # sign or trivial characters: B1492's survey
    nu = {g: RM.zeta(k) for g, k in zip(gens, ks)}
    if not RM.is_character(S, nu): continue
    n_char += 1; r = S.read(nu); r["exponents_of_zeta8"] = list(ks); out.append(r)
    print(ks, "b0", r["b0"], "room", r["room"]["n"], "second", r["second"], "m_A", r["m_A"], "int", r["interior"], "oth", r["other"], [(x["cls"], x["k"], x["I_W1"], x["I_L2W1"], x["relator_ok"]) for x in r["readings"]], flush=True)
    json.dump(out, open(HERE / "order4_o10_150691.json", "w"), indent=1, default=str)
every = [x for r in out for x in r["readings"]]
print("ORDER4", "characters", n_char, "readings", len(every), "min I(W1) =", min((x["I_W1"] for x in every), default=None), "max generations =", max((-x["I_W1"] for x in every), default=None))
