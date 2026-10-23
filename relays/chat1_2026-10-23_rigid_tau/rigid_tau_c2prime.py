#!/usr/bin/env python3
"""POST HOC control, labelled (RIGID_TAU_HOLOMORPHIC: written after the sealed control C2 failed, before any output of
the run is read; committed before its own run).  C2 as written checked F_6's T-covariance at the first family-A point,
the class LR's apex, Im tau = 1.118, the lowest height in the census; it found 9.0e-8 (ratios) and 1.4e-7 (|V|) against
a sealed bar of 1e-9.  At Im tau >= 2 the same check held to about 1e-13 in the earlier tests.  The suspicion is the
instrument's numerical precision at low Im tau (main's residues and regularised areas are quadratures), not a broken
covariance: B1720's own basis-covariance control accepted T-moves up to 1e-6 and measured 5.9e-8 at its points.
C2': the same T-covariance check (tau -> tau + 1, b -> b - alpha; ratios, and |V| above 1e-12, both readings and
horocycles) for F_6 and for DR at seven family-A points spanning the census's heights: the class LR's apex (the C2
point) and the first point of the classes whose apex heights are nearest 1.5, 2.0, 2.5, 3.0, 3.5 and 3.9.
    python3 -B rigid_tau_c2prime.py      # writes rigid_tau_c2prime.json"""
import contextlib, importlib.util, io, json, math, sys, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("rtt", HERE / "rigid_tau_test.py")
rtt = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(rtt)
zfc, rbs, TC = rtt.zfc, rtt.rbs, rtt.TC
C = TC.CENSUS
targets = [0] + [min(range(len(C)), key=lambda k: abs(C[k]["tau"][1] - h)) for h in (1.5, 2.0, 2.5, 3.0, 3.5, 3.9)]
OUT = {}
for k in targets:
    r = C[k]; a, b = r["lines"][0]; re_t, im_t = float(r["tau"][0]), float(r["tau"][1])
    M0 = rbs.channels(re_t, im_t, float(a), float(b)); M1 = rbs.channels(re_t + 1, im_t, float(a), float(b - a))
    rec = {"class": r["word"], "tau": [re_t, im_t], "line": f"({a}, {b})"}
    for d in ("F_6", "dR"):
        x0 = zfc.rows_at(M0, zfc.direction(d, re_t, im_t)); x1 = zfc.rows_at(M1, zfc.direction(d, re_t + 1, im_t))
        keep = (x0[:, :12] > -12) & (x1[:, :12] > -12)
        dr = float(np.max(np.abs(x0[:, :12] - x1[:, :12])[keep])) * math.log(10) if keep.any() else None
        sel_v = [12 + 4 * p + q for p in range(4) for q in range(3)]
        v0, v1 = x0[:, sel_v], x1[:, sel_v]
        keepv = (v0 > 1e-12) & (v1 > 1e-12)
        dv = float(np.max(np.abs(np.log(v0 / v1))[keepv])) if keepv.any() else None
        rec[d] = {"ratios": dr, "|V|": dv}
    OUT[f"{r['word']} at Im tau {im_t:.3f}"] = rec
(HERE / "rigid_tau_c2prime.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("written")
