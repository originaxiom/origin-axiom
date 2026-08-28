#!/usr/bin/env python3
"""OG-3: the volume spectrum of the 112-family in the object's own meter.

Question: is the family a DISCRETE SCALE LADDER -- Vol(M)/Vol(m004) an exact
integer (or simple rational) for every member? If yes, the observer's "choice
of scale" collapses to a choice of family member: a finite menu, not R^+.
Method: high-precision volumes (SnapPy 212-bit), ratio to m004, recognize
integer/rational at tight tolerance; cross-check: members' tetrahedron counts
(all-regular members have Vol = n_tets * V_reg, V_reg = Vol(m004)/2 exactly).
"""
import json
import snappy, mpmath as mp
mp.mp.dps = 50

fam = json.load(open("/Users/dri/origin-axiom/frontier/B1186_family_is_112/verification/family_census.json"))
members = fam["members_B"]; regs = set(fam["members_A"])
V0 = mp.mpf(str(snappy.Manifold("m004").high_precision().volume()).replace(" ", ""))
rows, nonint = [], []
for name in members:
    M = snappy.Manifold(name).high_precision()
    V = mp.mpf(str(M.volume()).replace(" ", ""))
    r = V / V0
    half = r * 2
    is_half_int = abs(half - mp.nint(half)) < mp.mpf(10) ** -30
    val = float(mp.nint(half)) / 2 if is_half_int else float(r)
    rows.append({"name": name, "tets": M.num_tetrahedra(), "cusps": M.num_cusps(),
                 "regular": name in regs, "ratio": val if is_half_int else None,
                 "ratio_float": float(r)})
    if not is_half_int:
        nonint.append((name, float(r)))
from collections import Counter
spec = Counter(r["ratio"] for r in rows if r["ratio"] is not None)
print("HALF-INTEGER LADDER SPECTRUM (ratio -> count):", dict(sorted(spec.items())))
print("non-half-integer members:", nonint if nonint else "NONE")
ints = Counter(r["ratio"] for r in rows if r["ratio"] is not None and r["ratio"] == int(r["ratio"]))
halfs = {k: v for k, v in spec.items() if k != int(k)}
print("integer rungs:", dict(sorted(ints.items())), "| half rungs:", dict(sorted(halfs.items())))
# regular members exactness: Vol = n_tets * V0/2
reg_exact = all(abs(r["ratio_float"] - r["tets"] / 2) < 1e-25 for r in rows if r["regular"])
print("all-regular members satisfy Vol = n_tets * Vol(m004)/2 exactly:", reg_exact)
json.dump({"V0_m004": str(V0), "rows": rows,
           "spectrum_half_integer": {str(k): v for k, v in sorted(spec.items())},
           "non_half_integer": nonint, "regular_exactness": bool(reg_exact)},
          open("og3_volume_spectrum.json", "w"), indent=1)
print("DONE")
