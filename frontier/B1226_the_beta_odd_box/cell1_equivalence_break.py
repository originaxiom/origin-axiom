"""B1226 Cell 1 -- the scale wall is NOT a symmetry theorem.

B1012 banked:  blind-to-k  <=>  CS = 0  <=>  amphichiral.
The first <=> is the sympy identity dS/dk = -CS and STANDS.
The second <=> is refuted here IN BOTH DIRECTIONS, by exhibited census counterexamples.
"""
import json, snappy

def cs_class(name):
    """CS as an element of R/(1/2)Z, taken at standard precision and
    cross-checked at high precision.  Returns Fraction-like float in [0,1/2)."""
    s = float(snappy.Manifold(name).chern_simons())
    h = float(snappy.ManifoldHP(name).chern_simons())
    assert abs((s - h) % 0.5) < 1e-9 or abs(((s - h) % 0.5) - 0.5) < 1e-9, (name, s, h)
    v = s % 0.5
    return 0.0 if min(v, 0.5 - v) < 1e-9 else round(v, 12)

def is_chiral(name):
    """Authoritative: symmetry_group().is_amphicheiral().
    NOTE is_isometric_to(mirror) is NOT a chirality test -- it happily returns
    True via an ORIENTATION-REVERSING isometry.  Cross-checked by det here."""
    M = snappy.Manifold(name)
    amph = M.symmetry_group().is_amphicheiral()
    B = snappy.Manifold(name); B.reverse_orientation()
    dets = sorted({I.cusp_maps()[0].det() for I in M.is_isometric_to(B, return_isometries=True)})
    # orientation-preserving self-mirror isometry exists iff amphichiral
    assert amph == (1 in dets), (name, amph, dets)
    return (not amph), dets

out = {"identity": "dS/dk = -CS  (B1012, sympy) -- STANDS",
       "census_scanned": 600, "cells": {}}
rows = []
for n in ['m004', 'm003', 'm136', 'm135', 'm206', 'm207', 'm208']:
    ch, dets = is_chiral(n)
    rows.append({"name": n, "chiral": ch, "cs_mod_half": cs_class(n), "mirror_iso_dets": dets})
out["exhibits"] = rows

# the four boxes of (amphichiral?, CS==0?) over the census
box = {"amph_cs0": [], "amph_csq": [], "chiral_cs0": [], "chiral_csq": 0}
for M in snappy.OrientableCuspedCensus(cusps=1)[:600]:
    try:
        a = M.symmetry_group().is_amphicheiral(); c = cs_class(M.name())
    except Exception:
        continue
    z = (c == 0.0)
    if a and z: box["amph_cs0"].append(M.name())
    elif a and not z: box["amph_csq"].append([M.name(), c])
    elif (not a) and z: box["chiral_cs0"].append(M.name())
    else: box["chiral_csq"] += 1
out["cells"] = box

fwd = len(box["amph_csq"]) == 0      # amphichiral => CS=0 ?
rev = len(box["chiral_cs0"]) == 0    # CS=0 => amphichiral ?
out["verdict"] = {
    "amphichiral_implies_CS0": fwd,
    "CS0_implies_amphichiral": rev,
    "B1012_equivalence_holds": fwd and rev,
    "counterexample_forward": box["amph_csq"][:3],
    "counterexample_reverse": box["chiral_cs0"][:3],
}
print(json.dumps(out["verdict"], indent=2))
print("\nboxes: amph&CS=0", box["amph_cs0"], "| amph&CS!=0", box["amph_csq"],
      "| CHIRAL&CS=0", box["chiral_cs0"], "| chiral&CS!=0", box["chiral_csq"])
json.dump(out, open("frontier/B1226_the_beta_odd_box/cell1_results.json", "w"), indent=2)
