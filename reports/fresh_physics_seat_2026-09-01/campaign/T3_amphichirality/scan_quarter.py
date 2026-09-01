#!/usr/bin/env python3
"""
Supplementary scan (T3): does ANY orientation double cover attain the 1/4
end of the 2-torsion set, or do covers sit identically at 0?

CS only (amphichirality is guaranteed by Thm A; symmetry_group omitted for
speed), bases 0..119 of NonorientableCuspedCensus, quad-double precision.
"""
import json, os
import snappy

CELL = os.path.dirname(os.path.abspath(__file__))
TOL = 1e-9
rows = []
NC = snappy.NonorientableCuspedCensus
for i in range(120):
    N = NC[i]
    rec = {"base": N.name(), "index": i}
    try:
        M = N.orientation_cover()
        cs = float(M.high_precision().chern_simons())
        r = cs % 0.5
        d0 = min(r, 0.5 - r)
        d4 = abs(r - 0.25)
        rec["cs"] = cs
        rec["value"] = "0" if d0 <= d4 else "1/4"
        rec["dist"] = min(d0, d4)
    except Exception as e:
        rec["error"] = repr(e)
    rows.append(rec)

ok = [r for r in rows if "cs" in r]
n0 = sum(1 for r in ok if r["value"] == "0" and r["dist"] < TOL)
n4 = sum(1 for r in ok if r["value"] == "1/4" and r["dist"] < TOL)
off = [r for r in ok if r["dist"] >= TOL]
summary = {"scanned": len(rows), "with_cs": len(ok), "at_0": n0,
           "at_quarter": n4, "off_lattice": len(off),
           "max_dist": max((r["dist"] for r in ok), default=None),
           "quarter_cases": [r["base"] for r in ok if r["value"] == "1/4"],
           "off_cases": [r["base"] for r in off]}
print(json.dumps(summary, indent=1))
json.dump({"rows": rows, "summary": summary},
          open(os.path.join(CELL, "scan_quarter_results.json"), "w"), indent=1)
