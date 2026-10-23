#!/usr/bin/env python3
"""READING PRE-SCAN (data-free; committed before its run; it reads no target).  Step 2a of THE_NEXT_ATTACK: the
structure behind the Standard Model's reading on every one of B1713's 266 lines, at two points that the reading test's
grid will not contain (0.3 + 2.6i and 0.3 + 3.1i), both horocycles (1 064 rows).  Per row:
  - the up and the down quarks' channel weights in rho(T)'s eigenframe (f3 = n, f2 = e1, f1 = n-bar): |u.u|/|u|^2,
    |w|/|u|, |a1|, |a2|, |a3| over |u|, and for the down quarks |a2 - i w| and |a2 + i w| over |u|;
  - the leptons' channel weights against the down quarks': the best of the sixteen sign patterns on (u_1, u_i, u_j, u_k)
    up to one complex factor, and its relative deviation;
  - the exactly null Higgs h = n and h = n-bar under the Standard Model's reading (up sees conj h, down and leptons h)
    and under one reading in every sector: |V_ud|, |V_us|, |V_cb|, |V_ub|, the up and down m2/m3.
Summary: by line order, the lines on which the Standard Model's reading with h = n or h = n-bar gives a CKM near the
identity (|V_ud| > 0.9 and |V_cb| < 0.2) on some row.  The idealised two-branch argument (THE_NEXT_ATTACK §1.6) says
this needs the down quarks' heavy state to sit where the up quarks' does; the scan shows on which lines it can.
    python3 -B reading_prescan.py [--workers 2]      # writes reading_prescan.json"""
import contextlib, importlib.util, io, json, math, sys, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
_argv = sys.argv; sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("cs", HERE / "channel_store.py"); cs = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(cs)
sys.argv = _argv
tic = cs.tic
LINES = [(tag, Fr(a), Fr(b)) for (tag, a, b) in tic.LINES]
PTS = [(0.3, 2.6), (0.3, 3.1)]
F1 = np.array([0, 1, -1j]) / math.sqrt(2); F2 = np.array([1, 0, 0], dtype=complex); F3 = np.array([0, 1, 1j]) / math.sqrt(2)
SIGNS = [np.array([a, b, c, d]) for a in (1, -1) for b in (1, -1) for c in (1, -1) for d in (1, -1)]


def frame(u4):
    w, u = u4[0], u4[1:]; nu = np.linalg.norm(u)
    a1, a2, a3 = np.vdot(F1, u), np.vdot(F2, u), np.vdot(F3, u)
    return [abs(u @ u) / nu ** 2, abs(w) / nu, abs(a1) / nu, abs(a2) / nu, abs(a3) / nu, abs(a2 - 1j * w) / nu, abs(a2 + 1j * w) / nu]


def ckm(Yu, Yd):
    Uu, su, _ = np.linalg.svd(Yu); Ud, sd, _ = np.linalg.svd(Yd)
    V = np.abs(np.conj(Uu[:, ::-1].T) @ Ud[:, ::-1])
    return [float(V[0, 0]), float(V[0, 1]), float(V[1, 2]), float(V[0, 2]), float(su[1] / su[0]), float(sd[1] / sd[0])]


def one(task):
    k, (re_t, im_t) = task
    tag, a, b = LINES[k]
    U = cs.weights(re_t, im_t, float(a), float(b))
    rows = []
    for ih, hor in enumerate(cs.HORS):
        up, dn, lp = U[0, ih], U[1, ih], U[2, ih]
        best = (9.0, None)
        for sg in SIGNS:
            x = sg * dn; c = np.vdot(x, lp) / np.vdot(x, x)
            e = float(np.max(np.abs(lp - c * x)) / max(np.max(np.abs(lp)), 1e-300))
            if e < best[0]:
                best = (e, sg.tolist())
        r = {"line": f"({a}, {b})", "order": tag, "tau": [re_t, im_t], "hor": hor, "up frame": frame(up), "down frame": frame(dn),
             "lep vs down: best sign pattern, deviation": [best[1], best[0]]}
        for name, h in (("n", F3), ("n-bar", F1)):
            r[f"SM reading, h = {name}"] = ckm(cs.closed(up, np.conj(h)), cs.closed(dn, h))
            r[f"one reading, h = {name}"] = ckm(cs.closed(up, h), cs.closed(dn, h))
        rows.append(r)
    return rows


if __name__ == "__main__":
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 2
    tasks = [(k, p) for k in range(len(LINES)) for p in PTS]
    rows = []
    with Pool(nw) as P:
        for rr in P.imap(one, tasks, chunksize=4):
            rows.extend(rr)
    summ = {}
    for r in rows:
        o = r["order"]; s = summ.setdefault(o, {"lines": set(), "SM-near-identity lines": set(), "one-reading-near-identity lines": set()})
        s["lines"].add(r["line"])
        for name in ("n", "n-bar"):
            v = r[f"SM reading, h = {name}"]
            if v[0] > 0.9 and v[2] < 0.2:
                s["SM-near-identity lines"].add(r["line"])
            v = r[f"one reading, h = {name}"]
            if v[0] > 0.9 and v[2] < 0.2:
                s["one-reading-near-identity lines"].add(r["line"])
    out = {"points": PTS, "rows": rows,
           "summary by order: lines, lines where the SM reading with h = n or n-bar gives |V_ud| > 0.9 and |V_cb| < 0.2 on some row, the same for one reading":
           {o: [len(s["lines"]), sorted(s["SM-near-identity lines"]), len(s["one-reading-near-identity lines"])] for o, s in sorted(summ.items(), key=lambda kv: int(kv[0][2:]))}}
    (HERE / "reading_prescan.json").write_text(json.dumps(out, indent=1, default=float) + "\n")
    print("written")
