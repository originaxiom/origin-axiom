#!/usr/bin/env python3
"""B1239 -- the CLOSED-case computed control for codex R040's theorem chain.

Hypothesis of the chain: M closed orientable hyperbolic with a fixed-point-free orientation-reversing
isometry (= orientation double cover of a closed nonorientable hyperbolic N). Oddness alone gives
cs(M) in {0, 1/2} mod 1; the Kawauchi + CGHN chain claims cs(M) = 0 mod 1. SnapPy's 17-manifold
NonorientableClosedCensus supplies 17 such M. SnapPea's closed CS needs the value propagated from the
cusped parent: unfill -> Zickert CS -> refill. Quad-double throughout. Also records Tor H1(M).
"""
import json
import snappy

TOL = 1e-15
out = []
for N in snappy.NonorientableClosedCensus:
    M = N.orientation_cover().high_precision()
    fills = [c["filling"] for c in M.cusp_info()]
    Mc = M.copy()
    for i in range(Mc.num_cusps()):
        Mc.dehn_fill((0, 0), i)
    cs_parent = Mc.chern_simons()
    for i, f in enumerate(fills):
        Mc.dehn_fill(f, i)
    cs = Mc.chern_simons()
    r = float(cs) % 1.0
    d0, dh = min(r, 1 - r), abs(r - 0.5)
    cls = "zero" if d0 < TOL else ("half" if dh < TOL else "other")
    vol_ratio = float(Mc.volume() / N.high_precision().volume())
    row = dict(base=N.name(), base_filling=str(N.cusp_info()[0]["filling"]),
               base_cusp=N.cusp_info()[0]["topology"], cover=Mc.name(), cover_orientable=Mc.is_orientable(),
               vol_ratio=vol_ratio, cs_parent=str(cs_parent), cs_closed=str(cs), residue_mod1=r,
               cls=cls, dist=min(d0, dh), H1_cover=str(Mc.homology()), H1_base=str(N.homology()))
    out.append(row)
    print(f"{row['base']:>6} {row['base_filling']:>12} {row['base_cusp']:>18} | cover vol/base={vol_ratio:.12f} "
          f"cs={float(cs):+.3e} -> {cls:5s} | H1(cover)={row['H1_cover']:<16} H1(base)={row['H1_base']}")
counts = {}
for r in out:
    counts[r["cls"]] = counts.get(r["cls"], 0) + 1
print("classes mod 1:", counts, " all vol ratios 2:", all(abs(r["vol_ratio"] - 2) < 1e-12 for r in out),
      " all orientable:", all(r["cover_orientable"] for r in out))
json.dump({"counts": counts, "tolerance": TOL, "rows": out}, open("r040_closed_control.json", "w"), indent=1)
