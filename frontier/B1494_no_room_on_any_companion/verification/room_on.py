#!/usr/bin/env python3
"""B1494 R1/R2/R4 -- the room of the line at every sign character of a manifold given by ISOSIG (B1493's instrument,
imported from its arc): room_on.py <label> <isosig>  ->  room_<label>.json"""
import sys, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1493_the_room_on_the_companions" / "verification"))
import room as RM
label, isosig = sys.argv[1], sys.argv[2]
S = RM.Room(isosig); out = []
for vals, chi in RM.sign_characters(S):
    r = S.room(chi); triv = []
    for (mu, lam) in S.cusps:
        vm = 1
        for ch in mu: vm *= (chi[ch.lower()] if ch.islower() else 1 / chi[ch.lower()])
        vl = 1
        for ch in lam: vl *= (chi[ch.lower()] if ch.islower() else 1 / chi[ch.lower()])
        triv.append(bool(abs(vm - 1) < RM.MC.TOL and abs(vl - 1) < RM.MC.TOL))
    row = dict(chi=list(vals), trivial_on_cusp=triv, m_A=sum(triv), **r); out.append(row); print(row, flush=True)
summary = dict(label=label, isosig=isosig, cusps=S.m, gens=S.gens, characters=len(out), rows=out,
               n_trivial=[r["n"] for r in out if all(v == 1 for v in r["chi"])][0], max_room=max(r["n"] for r in out), rooms=sorted(r["n"] for r in out))
json.dump(summary, open(HERE / f"room_{label}.json", "w"), indent=1, default=str)
print("ROOM", label, "cusps", S.m, "characters", len(out), "n(1) =", summary["n_trivial"], "max n(chi) =", summary["max_room"])
