#!/usr/bin/env python3
"""HOLOMORPHIC TEST, POST HOC (labelled; written before the test's rows existed, committed before its run; it runs
after the cells are read).  Tracks B-2 and B-3 of THE_PLAN_AFTER_THE_READING_TEST on the committed rows of THE
HOLOMORPHIC READING TEST (holo_rows.json, holo_store.npz):
  B-2  read the Higgs off the fits: on the rows whose minimum chi2_nine is below 100 (or the 100 lowest if fewer),
       (a) the Fubini-Study distance from the fitted direction h to each record direction at the same tau (DR, F_a, h2,
           h3, each as stored and conjugated) - the nearest form and its distance;
       (b) the covariant pencil DR + mu E2* R (complex mu on a grid, then refined): the closest member to h or conj h,
           its mu and distance;
       (c) every pair of the 26 record directions: the median distance from h to their complex span - the best pair;
       (d) smoothness along Im tau: on each (line, horocycle, Re tau) with at least three such rows, the distance between
           consecutive fitted directions against DR's own change between the same tau.
  B-3  at every such row's optimum: J (Jarlskog), m_b/m_tau and m_t/m_b from the frame's heaviest singular values.
    python3 -B holo_posthoc.py      # writes holo_posthoc.json"""
import contextlib, importlib.util, io, json, math, sys, pathlib
import numpy as np
from scipy.optimize import minimize

HERE = pathlib.Path(__file__).resolve().parent


def load(name, f):
    argv = sys.argv; sys.argv = ["x"]
    spec = importlib.util.spec_from_file_location(name, HERE / f); m = importlib.util.module_from_spec(spec); sys.modules[name] = m
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    sys.argv = argv
    return m


ht = load("ht", "holo_test.py")
wp = load("wp", "weight_pencil.py")
oh = ht.oh
d = json.loads((HERE / "holo_rows.json").read_text()); tasks, rows = d["tasks"], d["rows"]
I = json.loads((HERE / "holo_store_index.json").read_text()); DIRS = I["dirs"]
st = np.load(HERE / "holo_store.npz"); U, H = st["U"], st["H"]
main = [r for r in rows if not r.get("degenerate") and tasks[r["p"]][1] != ht.RE_MIRROR and np.isfinite(r["chi2_nine"])]
good = [r for r in main if r["chi2_nine"] < 100]
if len(good) < 100:
    good = sorted(main, key=lambda r: r["chi2_nine"])[:100]
NAMES = [f"{n}" for n in DIRS] + [f"conj {n}" for n in DIRS]


def fs(a, b):
    return math.acos(min(1.0, abs(np.vdot(a / np.linalg.norm(a), b / np.linalg.norm(b)))))


def hvec(r):
    return np.array([complex(a, b) for a, b in r["h"]])


out = {"rows used": len(good), "chi2_nine range of the rows used": [min(r["chi2_nine"] for r in good), max(r["chi2_nine"] for r in good)]}
# B-2a
near, cnt = [], {}
for r in good:
    h = hvec(r); rec = list(H[r["p"]]) + [np.conj(v) for v in H[r["p"]]]
    ds = [fs(h, v) for v in rec]; j = int(np.argmin(ds))
    near.append(ds[j]); cnt[NAMES[j]] = cnt.get(NAMES[j], 0) + 1
out["B-2a nearest record direction: counts"] = dict(sorted(cnt.items(), key=lambda kv: -kv[1]))
out["B-2a distance to the nearest record direction (rad): quantiles 10/50/90%"] = [float(np.quantile(near, q)) for q in (0.1, 0.5, 0.9)]
# B-2b the covariant pencil
pen = []
for r in good:
    k, re_t, im_t = tasks[r["p"]]
    R = wp.rbs.at(wp.rbs.R, re_t, im_t); DR = wp.rbs.at(wp.rbs.H1, re_t, im_t); e2s = wp.E2(complex(re_t, im_t)) - 3 / (math.pi * im_t)
    h = hvec(r)
    best = (9.0, None, None)
    for target, lab in ((h, "h"), (np.conj(h), "conj h")):
        f = lambda x: fs(DR + complex(x[0], x[1]) * e2s * R, target)
        grid = [(a, b) for a in np.linspace(-2, 2, 41) for b in np.linspace(-2, 2, 41)]
        x0 = min(grid, key=f)
        res = minimize(f, x0, method="Nelder-Mead", options={"xatol": 1e-6, "fatol": 1e-9, "maxiter": 400})
        if res.fun < best[0]:
            best = (float(res.fun), complex(res.x[0], res.x[1]), lab)
    pen.append(best)
out["B-2b the covariant pencil DR + mu E2* R: distance quantiles 10/50/90%"] = [float(np.quantile([p[0] for p in pen], q)) for q in (0.1, 0.5, 0.9)]
out["B-2b mu at the rows within 0.05 rad (re, im)"] = [[round(p[1].real, 4), round(p[1].imag, 4), p[2]] for p in pen if p[0] < 0.05]
# B-2c pairs of record directions
best_pairs = []
for i in range(26):
    for j in range(i + 1, 26):
        dd = []
        for r in good:
            rec = list(H[r["p"]]) + [np.conj(v) for v in H[r["p"]]]
            A = np.stack([rec[i], rec[j]], 1); Q, _ = np.linalg.qr(A)
            h = hvec(r); h = h / np.linalg.norm(h)
            dd.append(math.asin(min(1.0, float(np.linalg.norm(h - Q @ (Q.conj().T @ h))))))
        best_pairs.append((float(np.median(dd)), NAMES[i], NAMES[j]))
best_pairs.sort()
out["B-2c the best pairs by median distance from h to their span (rad)"] = [[round(a, 4), b, c] for a, b, c in best_pairs[:8]]
# B-2d smoothness
seq = {}
for r in good:
    k, re_t, im_t = tasks[r["p"]]; seq.setdefault((k, r["hor"], re_t), []).append((im_t, r))
sm = []
for key, lst in seq.items():
    if len(lst) < 3:
        continue
    lst.sort()
    for (y1, r1), (y2, r2) in zip(lst[:-1], lst[1:]):
        dr1 = H[r1["p"]][DIRS.index("dR")]; dr2 = H[r2["p"]][DIRS.index("dR")]
        sm.append([fs(hvec(r1), hvec(r2)), fs(dr1, dr2)])
out["B-2d consecutive fitted directions along Im tau vs DR's change: pairs, median of each, median ratio"] = (
    [len(sm), float(np.median([a for a, b in sm])), float(np.median([b for a, b in sm])), float(np.median([a / max(b, 1e-12) for a, b in sm]))] if sm else None)
# B-3
b3 = []
for r in good:
    Uh = U[r["p"], :, ht.cs.HORS.index(r["hor"])]; h = hvec(r); h = h / np.linalg.norm(h)
    Uu, su, _ = np.linalg.svd(oh.Ybatch(Uh[0], h[None])[0]); Ud, sd, _ = np.linalg.svd(oh.Ybatch(Uh[1], h[None])[0])
    se = np.linalg.svd(oh.Ybatch(Uh[2], h[None])[0], compute_uv=False)
    V = np.conj(Uu[:, ::-1].T) @ Ud[:, ::-1]
    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    b3.append({"chi2_nine": r["chi2_nine"], "J": J, "m_b/m_tau": float(sd[0] / se[0]), "m_t/m_b": float(su[0] / sd[0])})
out["B-3 at the ten lowest rows: chi2_nine, J, m_b/m_tau, m_t/m_b"] = [[round(x["chi2_nine"], 2), x["J"], round(x["m_b/m_tau"], 4), round(x["m_t/m_b"], 3)]
                                                                     for x in sorted(b3, key=lambda x: x["chi2_nine"])[:10]]
out["B-3 |J| quantiles 10/50/90% over the rows used (the data: 3.08e-5)"] = [float(np.quantile([abs(x["J"]) for x in b3], q)) for q in (0.1, 0.5, 0.9)]
out["B-3 m_b/m_tau quantiles 10/50/90% (M_Z about 1.64 in the SM; M_GUT about 0.76 in the MSSM at eta = 0)"] = [float(np.quantile([x["m_b/m_tau"] for x in b3], q)) for q in (0.1, 0.5, 0.9)]
(HERE / "holo_posthoc.json").write_text(json.dumps(out, indent=1, default=float) + "\n")
print("written")
