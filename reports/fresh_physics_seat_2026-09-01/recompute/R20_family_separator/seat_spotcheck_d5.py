#!/usr/bin/env python3
"""Seat spot-check of R20's D5 (family-wide amphichirality refuted) and the o10_150700 witness.

Run from the repo root. Needs snappy. Writes seat_cs_h1_table.json beside this file.
"""
import collections
import json
import os

import snappy

HERE = os.path.dirname(os.path.abspath(__file__))
V_GIE = 1.0149416064096536  # Cl2(pi/3), the Gieseking volume


def cs_mod_half(M):
    cs = float(M.chern_simons()) % 0.5
    return 0.0 if abs(cs - 0.5) < 1e-6 else round(cs, 6)


# 1. The banked instrument cannot fail: unoriented is_isometric_to passes known-chiral manifolds.
print("== banked instrument (reverse_orientation + is_isometric_to) vs orientation-aware test ==")
for n in ["m015", "m016", "m019", "m202", "s118", "m208", "m004", "m003"]:
    M = snappy.Manifold(n)
    R = M.copy()
    R.reverse_orientation()
    print(f"{n:6s} banked={M.is_isometric_to(R)!s:5s} amphicheiral={M.symmetry_group().is_amphicheiral()!s:5s} CS={cs_mod_half(M)}")

# 2. Tabulate the 112 family from R20's oriented-amphichirality artifact.
d = json.load(open(os.path.join(HERE, "r20_amphichirality_oriented.json")))
rows = []
for n, v in d.items():
    M = snappy.Manifold(n)
    rows.append((n, bool(v[0] and v[1]), str(M.homology()), cs_mod_half(M), round(float(M.volume()) / V_GIE)))
json.dump(rows, open(os.path.join(HERE, "seat_cs_h1_table.json"), "w"), indent=0)
print("\n== 112 family ==", "amphichiral:", sum(a for _, a, *_ in rows))
for k, c in sorted(collections.Counter((a, cs) for _, a, _, cs, _ in rows).items()):
    print("  amphichiral=%s CS=%s : %d" % (k[0], k[1], c))
assert all(cs in (0.0, 0.25) for _, a, _, cs, _ in rows if a), "B1224 2-torsion law violated on an amphichiral member"
print("H1=Z members:", [(n, a, cs, nv) for n, a, _, cs, nv in rows if _ == "Z"])

# 3. The witness: o10_150700 -- H1=Z, ten regular ideal tetrahedra, chiral, CS = -1/12, not a cover of m004/m000.
T = snappy.Manifold("o10_150700")
sh = [complex(z) for z in T.tetrahedra_shapes("rect")]
assert all(abs(z - complex(0.5, 3 ** 0.5 / 2)) < 1e-9 for z in sh), "shapes are not all omega"
print("\n== o10_150700 ==", T.num_cusps(), "cusp;", T.homology(), "; tets", T.num_tetrahedra(), "; vol/V_gie", round(float(T.volume()) / V_GIE, 6))
print("  CS =", T.chern_simons(), "; amphicheiral:", T.symmetry_group().is_amphicheiral(), "; symmetry group:", T.symmetry_group())
m4 = snappy.Manifold("m004")
print("  is a 5-fold cover of m004:", any(C.is_isometric_to(T) for C in m4.covers(5)))
print("  is a 10-fold orientable cover of m000:", any(C.is_orientable() and C.is_isometric_to(T) for C in snappy.Manifold("m000").covers(10)))
print("  5-fold covers of m004 (H1, amphichiral, CS):", [(str(C.homology()), C.symmetry_group().is_amphicheiral(), cs_mod_half(C)) for C in m4.covers(5)])
