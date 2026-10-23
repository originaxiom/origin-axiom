#!/usr/bin/env python3
"""POST HOC, EXPLORATORY, labelled (written after TICK_LINE_HIGGS's comparison was read; committed before its run).
Not a test.  The sealed cell K6 failed (|J| = 2.1e-6 at the best nine-row).  This asks whether the CKM phase is reachable
anywhere the selected structure fits:
  (1) over the sealed grid's menu rows (S, c = 3), the largest |J| among rows whose nine is within 2.5, 3.0 and 4.0,
      and where it sits;
  (2) a fit of the "ten" (the nine plus |ln(|J| / 3.08e-5)|) over tau by Nelder-Mead, for F_22 and F_6 on S1's (2/5, 4/5) and
      S2's (2/5, 1/5) (their sign partners gave identical values in the sealed run) and both horocycles, each started at that combination's best grid row for the ten;
      reports the best ten, the nine and |J| there.
Targets: the record's pinned files at 3412bf09d, as in tick_line_compare.py.
    python3 -B tick_line_cp.py      # writes tick_line_cp.json"""
import contextlib, importlib.util, io, json, math, sys, pathlib
import numpy as np
from scipy.optimize import minimize

HERE = pathlib.Path(__file__).resolve().parent
sys.argv = ["x"]
src = (HERE / "tick_line_optimum.py").read_text()
src = src[:src.index("OUT = {}")]                       # reuse its loaders and model, not its run
tlo = {"__file__": str(HERE / "tick_line_optimum.py"), "__name__": "tlo"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src, "tick_line_optimum.py", "exec"), tlo)
T9, T6, X, IDX, model, l9_from_fields = tlo["T9"], tlo["T6"], tlo["X"], tlo["IDX"], tlo["model"], tlo["l9_from_fields"]
JPDG = 3.08e-5
MENU = ["F_6", "F_-2", "F_22"]
OUT = {"(1) largest |J| among well-fitting grid rows": {}, "(2) fits of the ten": {}}
rows = []
for p, t in enumerate(IDX["tasks"]):
    for d in MENU:
        for ih, hor in enumerate(IDX["hors"]):
            L9, J = l9_from_fields(X[p, IDX["dirs"].index(d), ih])
            nine = float(np.max(np.abs(L9 - T9)))
            rows.append((nine, abs(float(J)), d, IDX["lines"][t[0]], t[1], t[2], hor))
for bar in (2.5, 3.0, 4.0):
    good = [r for r in rows if math.exp(r[0]) <= bar]
    top = max(good, key=lambda r: r[1]) if good else None
    OUT["(1) largest |J| among well-fitting grid rows"][f"nine within {bar}"] = {
        "rows": len(good), "largest |J|": top[1] if top else None,
        "at": {"direction": top[2], "line": top[3], "tau": [top[4], top[5]], "hor": top[6], "nine": math.exp(top[0])} if top else None}


def ten(p, d, line, hor):
    re_t, im_t = p
    if not 1.5 <= im_t <= 4.0:
        return 50.0
    L9, J = model(d, line, hor, re_t, im_t)
    return float(max(np.max(np.abs(L9 - T9)), abs(math.log(max(abs(J), 1e-300) / JPDG))))


for d in ("F_22", "F_6"):
    for line in ("(2/5, 4/5)", "(2/5, 1/5)"):
        for hor in IDX["hors"]:
            cand = [r for r in rows if r[2] == d and r[3] == line and r[6] == hor]
            st = min(cand, key=lambda r: max(r[0], abs(math.log(max(r[1], 1e-300) / JPDG))))
            start = [st[4], st[5]]
            res = minimize(ten, x0=np.array(start), args=(d, line, hor), method="Nelder-Mead",
                           options={"xatol": 1e-4, "fatol": 1e-6, "maxfev": 120,
                                    "initial_simplex": np.array([start, [start[0] + 0.03, start[1]], [start[0], start[1] + 0.03]])})
            L9, J = model(d, line, hor, *res.x)
            OUT["(2) fits of the ten"][f"{d} on {line}, {hor}"] = {
                "start": start, "tau": [float(x) for x in res.x], "ten": math.exp(res.fun),
                "nine there": math.exp(float(np.max(np.abs(L9 - T9)))), "J there": float(J), "evaluations": int(res.nfev)}
            print(d, line, hor, "done", flush=True)
(HERE / "tick_line_cp.json").write_text(json.dumps(OUT, indent=1) + "\n")
