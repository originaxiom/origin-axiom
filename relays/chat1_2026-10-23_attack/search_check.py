#!/usr/bin/env python3
"""SEARCH CHECK (POST HOC, labelled; committed before its run, its output committed before it is read).  sm_search.py's
search exercised on TWO_HIGGS's grid (channel_store_two_higgs.npz), whose rows have all been compared with the data under
the Standard Model's reading already (inverse_sm_all.py: lowest 1 027.661 over 2 560 rows, from twelve starts).
  P1 (data-free) power and timing: twelve rows (seed 4), a planted direction each, six near the null conic (|s| log-
     uniform in 10^-4 .. 10^-1) and six uniform in CP^2; the targets are the model's nine at the planted direction; the
     search should return chi2 <= 0.1 against them.
  P2 (post hoc, the data): the same search with the pinned targets on inverse_sm_all's fifteen lowest rows (their old
     minima known) and on 45 further rows (seed 5): the new minima against the old.
    python3 -B search_check.py      # writes search_check.json"""
import importlib.util, json, math, sys, time, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
_argv = sys.argv; sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("ih", HERE / "inverse_higgs.py"); ih = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ih)
_spec2 = importlib.util.spec_from_file_location("sms", HERE / "sm_search.py"); sms = importlib.util.module_from_spec(_spec2)
_spec2.loader.exec_module(sms)
sys.argv = _argv
st = np.load(HERE / "channel_store_two_higgs.npz"); U, H = st["U"], st["H"]
I = json.loads((HERE / "channel_store_two_higgs_index.json").read_text()); tasks = I["tasks"]; HORS = I["hors"]
old = json.loads((HERE / "inverse_sm_all_two_higgs.json").read_text())
out = {"P1 planted": [], "P2 rows": []}

rng = np.random.default_rng(4)
t0 = time.time()
for n in range(12):
    p = int(rng.integers(0, len(tasks))); h_ = int(rng.integers(0, 2)); Uh = U[p, :, h_]
    if n < 6:
        t = complex(*rng.normal(size=2)); r = 10 ** rng.uniform(-4, -1); ph = rng.uniform(0, 2 * math.pi)
        h0 = np.array([2 * t, 1 - t * t, 1j * (1 + t * t)]); h0 /= np.linalg.norm(h0)
        hp = h0 + r * np.exp(1j * ph) * np.conj(h0)
    else:
        z = rng.normal(size=6); hp = z[:3] + 1j * z[3:]
    hp /= np.linalg.norm(hp)
    Tp = sms.nine_batch(Uh, hp[None], ih.T9, ih.SIG)[0][0]
    g, (c, x) = sms.search(Uh, H[p], Tp, ih.SIG)
    out["P1 planted"].append({"p": p, "hor": HORS[h_], "kind": "near the conic" if n < 6 else "uniform",
                              "|h.h| planted": float(abs(hp @ hp)), "grid min": g, "found": c})
out["P1 seconds per row"] = (time.time() - t0) / 12

rows = []
for r in old["the 15 lowest rows"]:
    k, re_t, im_t = r["point"]
    p = next(i for i, t in enumerate(tasks) if t[0] == k and abs(t[1] - re_t) < 1e-9 and abs(t[2] - im_t) < 1e-9)
    rows.append((p, HORS.index(r["hor"]), r["min chi2_nine"]))
rng = np.random.default_rng(5)
for _ in range(45):
    rows.append((int(rng.integers(0, len(tasks))), int(rng.integers(0, 2)), None))
t0 = time.time()
for p, h_, o in rows:
    Uh = U[p, :, h_]
    g, (c, x) = sms.search(Uh, H[p], ih.T9, ih.SIG)
    hb = sms.vec(x); L, c9, V = sms.nine_batch(Uh, hb[None], ih.T9, ih.SIG)
    out["P2 rows"].append({"p": p, "point": tasks[p], "hor": HORS[h_], "old min": o, "grid min": g, "new min": c,
                           "model/data": [round(float(q), 4) for q in np.exp(L[0] - ih.T9)], "|V_ud|": float(V[0, 0, 0]), "|h.h|": float(abs(hb @ hb))})
out["P2 seconds per row"] = (time.time() - t0) / len(rows)
(HERE / "search_check.json").write_text(json.dumps(out, indent=1, default=float) + "\n")
print("written")
