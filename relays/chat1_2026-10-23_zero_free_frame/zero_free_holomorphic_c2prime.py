#!/usr/bin/env python3
"""POST HOC control, labelled (ZERO_FREE_HOLOMORPHIC: written after the sealed control C2 failed, before any output of
the run is read; committed before its own run).  C2 as written took the first grid point, which lies on the trivial
line (0, 0).  There Y_up = Y_down, so V = 1 and |V_us|, |V_cb|, |V_ub| are rounding noise near 1e-16; its 1.89 in ln
is that noise, while every ratio agreed to 3.4e-13 (the same artefact as the zero-free census's C1).
C2': the same T-covariance check (tau -> tau + 1, b -> b - a; every ratio and every |V| above 1e-12, both readings and
horocycles) for F_6, F_-2, F_22 and DR at three grid points on non-trivial lines: (2/5, 1/10) at 0.15 + 2.05i,
(1/4, 3/8) at 0.60 + 2.75i and (2/7, 3/7) at 0.90 + 3.45i.
    python3 -B zero_free_holomorphic_c2prime.py      # writes zero_free_holomorphic_c2prime.json"""
import contextlib, importlib.util, io, json, math, sys, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("zht", HERE / "zero_free_holomorphic_test.py")
zht = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(zht)
zfc, rbs = zht.zfc, zht.rbs
want = [("(2/5, 1/10)", 0.15, 2.05), ("(1/4, 3/8)", 0.60, 2.75), ("(2/7, 3/7)", 0.90, 3.45)]
out = {}
for name, re_t, im_t in want:
    k = next(i for i, l in enumerate(zfc.LINES) if l[2] == name)
    a, b, _ = zfc.LINES[k]
    M0, M1 = rbs.channels(re_t, im_t, a, b), rbs.channels(re_t + 1, im_t, a, b - a)
    for d in zht.DIRS:
        x0 = zfc.rows_at(M0, zfc.direction(d, re_t, im_t)); x1 = zfc.rows_at(M1, zfc.direction(d, re_t + 1, im_t))
        r0, r1 = x0[:, :12], x1[:, :12]
        keep = (r0 > -12) & (r1 > -12)
        dr = float(np.max(np.abs(r0 - r1)[keep])) * math.log(10) if keep.any() else None
        sel_v = [12 + 4 * p + q for p in range(4) for q in range(3)]
        v0, v1 = x0[:, sel_v], x1[:, sel_v]
        keepv = (v0 > 1e-12) & (v1 > 1e-12)
        dv = float(np.max(np.abs(np.log(v0 / v1))[keepv])) if keepv.any() else None
        out[f"{name} at {re_t} + {im_t}i, {d}"] = {"ratios": dr, "|V|": dv}
worst = max(max(x for x in v.values() if x is not None) for v in out.values())
out["worst"] = worst; out["C2' holds"] = worst < 1e-9
print(json.dumps(out, indent=1))
(HERE / "zero_free_holomorphic_c2prime.json").write_text(json.dumps(out, indent=1) + "\n")
