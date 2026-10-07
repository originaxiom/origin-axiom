#!/usr/bin/env python3
"""B1491 -- two facts of the SM seat's fixed-point companions (its note of 2026-10-07), checked on main with SnapPy:
(i) m003's companion o10_150729 is the link complement S^3 - L10n113 (isometric); (ii) the companion of +LLLR, whose monodromy
has trace 5 and so three fixed points, is the unique degree-3 cyclic cover with three cusps -- the link complement L8a15 --
chiral, with a symmetry group of order 12.  Also the end counts |2 - tr phi| against H_1's torsion on the four states."""
import json, pathlib, snappy
HERE = pathlib.Path(__file__).resolve().parent
out = {}
A = snappy.Manifold("o10_150729"); B = snappy.Manifold("L10n113")
out["o10_150729_is_L10n113"] = bool(A.is_isometric_to(B)); out["L10n113_cusps"] = B.num_cusps()
rows = {}
for name, tr in (("b++LR", 3), ("b+-LR", -3), ("b++LLRR", 6), ("b+-LLRR", -6), ("b++LLLR", 5)):
    M = snappy.Manifold(name); rows[name] = dict(tr=tr, ends=abs(2 - tr), H1=str(M.homology()))
out["states"] = rows
M = snappy.Manifold("b++LLLR"); comp = None
for C in M.covers(3):
    if C.num_cusps() == 3:
        S = C.symmetry_group()
        comp = dict(name=C.name(), cusps=3, H1=str(C.homology()), volume=float(C.volume()), volume_ratio=float(C.volume() / M.volume()),
                    symmetry_order=int(S.order()), amphicheiral=bool(S.is_amphicheiral()), identify=[str(x) for x in C.identify()][:3],
                    cusp_shapes=[str(s)[:24] for s in C.cusp_info("shape")])
out["LLLR_companion"] = comp
out["ok"] = out["o10_150729_is_L10n113"] and comp is not None and any("L8a15" in x for x in comp["identify"]) and abs(comp["volume_ratio"] - 3) < 1e-9
json.dump(out, open(HERE / "companions_check.json", "w"), indent=1); print(json.dumps(out, indent=1))
