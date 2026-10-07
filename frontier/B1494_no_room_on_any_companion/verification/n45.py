#!/usr/bin/env python3
"""B1494 R3 -- N45 rebuilt on main from the SM seat's recipe (its golden-covers dossier §7; sm:B1540): m003 -> a one-cusped
degree-9 cover d9.2 -> its 5-fold cyclic cover along the restriction of m003's Z/5 character.  Every one-cusped degree-9
cover of m003 is tried; every 5-fold cyclic cover of each with five cusps is recorded with its H1; the ones with
H1 = Z^9 + (Z/2)^2 are N45 candidates (the seat's identification), saved by isosig.  Then the room instrument's targets:
n(1) = b1 - cusps = 4; the sign characters' rooms are read by B1493's room.py on the isosig (R4)."""
import json, pathlib
import snappy
HERE = pathlib.Path(__file__).resolve().parent

M = snappy.Manifold("m003"); out = dict(base="m003", H1_base=str(M.homology()), degree9=[], candidates=[])
for i, C9 in enumerate(M.covers(9)):
    if C9.num_cusps() != 1: continue
    row = dict(index=i, H1=str(C9.homology()), isosig=C9.triangulation_isosig(), fivefold=[])
    for C5 in C9.covers(5, cover_type="cyclic"):
        H = C5.homology(); r = dict(cusps=C5.num_cusps(), H1=str(H), b1=H.betti_number(), isosig=C5.triangulation_isosig(), volume_over_m003=float(C5.volume() / M.volume()))
        row["fivefold"].append(r)
        if C5.num_cusps() == 5 and str(H).replace(" ", "") == "Z/2+Z/2+" + "+".join(["Z"] * 9):
            r2 = dict(r, degree9_index=i, n1=H.betti_number() - 5, sym=C5.symmetry_group().order()); out["candidates"].append(r2); print("N45 candidate:", r2, flush=True)
    out["degree9"].append(row); print("degree-9 cover", i, row["H1"], "five-fold cyclic covers:", [(f["cusps"], f["H1"]) for f in row["fivefold"]], flush=True)
json.dump(out, open(HERE / "n45.json", "w"), indent=1)
print("one-cusped degree-9 covers:", len(out["degree9"]), "N45 candidates:", len(out["candidates"]))
