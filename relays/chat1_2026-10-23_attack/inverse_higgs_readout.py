#!/usr/bin/env python3
"""POST HOC read-out of inverse_higgs_<grid>.json (labelled; committed before its run): per structure, the lowest
chi2_nine and the best rows with their parts; for A2, the optimal departures in units of the cusp scales
(delta / r^(1/2), epsilon / r) beside the record's forms (R: 2.83, 4; DR: 5.66, 20; F_a: 0, 2a); the floor by horocycle
and by Im tau; and how often each structure's optimum puts the light states on the same null line.
    python3 -B inverse_higgs_readout.py --grid two_higgs      # writes inverse_higgs_<grid>_readout.json"""
import json, math, sys, pathlib
from collections import defaultdict
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
gname = sys.argv[sys.argv.index("--grid") + 1]
D = json.loads((HERE / f"inverse_higgs_{gname}.json").read_text())
rows = D["rows"]
out = {"grid": gname, "screen": D["screen"], "screen min and median": D["screen minimum and median over all (point, horocycle)"],
       "summary": D["summary"]}
for stt in ("A2", "A1", "SM"):
    rs = sorted(rows, key=lambda r: r[stt]["min chi2_nine"])
    best = []
    for r in rs[:8]:
        x = r[stt]; rr = r["r = exp(-pi Im tau)"]
        def units(h):
            d, e = h["delta = e1 / leading"], h["epsilon = other null / leading"]
            return {"leading": h["leading null"], "delta/r^.5": None if d is None else round(d / rr ** 0.5, 2),
                    "eps/r": None if e is None else round(e / rr, 2), "|e1|,|h0|,|conj h0|": h["|e1|, |h0|, |conj h0|"]}
        best.append({"line": r["line"], "tau": r["point"][1:], "hor": r["hor"], "chi2_nine": x["min chi2_nine"],
                     "chi2_six there": x["chi2_six there"], "min chi2_six": x["min chi2_six (separately)"],
                     "model/data (c/t, u/t, s/b, d/b, mu/tau, e/tau, Vus, Vcb, Vub)": x["model/data"], "J": x["J"], "D": x["D"],
                     "h_u": units(x["h_u"]), "h_d": units(x["h_d"])})
    out[f"{stt}: the eight best rows"] = best
    byh = defaultdict(list); byim = defaultdict(list)
    for r in rows:
        byh[r["hor"]].append(r[stt]["min chi2_nine"]); byim[round(r["point"][2], 1)].append(r[stt]["min chi2_nine"])
    out[f"{stt}: lowest chi2_nine by horocycle"] = {h: min(v) for h, v in byh.items()}
    out[f"{stt}: lowest chi2_nine by Im tau (rows optimised)"] = {str(k): min(v) for k, v in sorted(byim.items())}
    out[f"{stt}: rows (of {len(rows)}) below 21.67, 50, 100"] = [sum(r[stt]["min chi2_nine"] < b for r in rows) for b in (21.67, 50, 100)]
    same = sum(r[stt]["h_u"]["leading null"] == r[stt]["h_d"]["leading null"] for r in rows)
    out[f"{stt}: rows whose optimal up and down Higgs share the leading null line"] = same
(HERE / f"inverse_higgs_{gname}_readout.json").write_text(json.dumps(out, indent=1) + "\n")
print("written")
