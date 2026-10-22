#!/usr/bin/env python3
"""EXPLORATORY, labelled (step 1 of chat1's plan of 2026-10-22; no cell, no seal): main's fibre frame with a second flat
Wilson line, along B - L (the SM seat's relay 66, P-084), added to the hypercharge line.  Each field of hypercharge
charge q = 6Y and B - L charge q' = 3(B - L) (Q 1, u^c -1, d^c -1, L -3, e^c 3; the Higgs 0) is twisted by
q*w + q'*w', w = a tau + b the record's line and w' = a' tau + b' the B - L line.  Every Yukawa bilinear is B - L
neutral, so the line is allowed; at first order in w' the leptons' twists are -3 times the down quarks' (the
Georgi-Jarlskog ratio, here from the charges).  Everything else is main's B1720 instrument at 3412bf09d, unchanged
(imported through two_ingredients_census, which extracts and hash-checks it); every sector with every Higgs reading.
Points: the sealed census's best six-row (tau = 0.4 + 2.7i on (2/5, 1/10)) and best nine-row ((2/5, 1/2)), and the
tick's exact d = e line (2/5, 4/5) at tau = 1/2 + 3.1i; at each, w' on the grid a', b' in {-0.30, -0.28, ..., 0.30}.
Model values only; the read-out is a separate script.
    python3 -B bl_line_scan.py [--workers 2]      # writes bl_line_scan.jsonl (checkpointed)"""
import importlib.util, json, math, sys, time, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("tic", HERE.parent / "chat1_2026-10-22_selection_map" / "two_ingredients_census.py")
tic = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(tic)
B, TC, te, mp = tic.B, tic.TC, tic.te, tic.mp
BL3 = {"Q": 1, "u": -1, "d": -1, "L": -3, "e": 3, "H": 0}
OUTL = HERE / "bl_line_scan.jsonl"
POINTS = [("six_best", 0.4, 2.7, 2 / 5, 1 / 10), ("nine_best", 0.4, 2.7, 2 / 5, 1 / 2), ("tick_d_eq_e", 0.5, 3.1, 2 / 5, 4 / 5)]
GRID = [round(-0.30 + 0.02 * k, 2) for k in range(31)]
TASKS = [(name, a2, b2) for name, *_ in POINTS for a2 in GRID for b2 in GRID]
_S = {}


def higgs(re_t, im_t):
    key = (re_t, im_t)
    if key not in _S:
        av = [complex(te.ev(cc, mp.mpc(re_t, im_t))) for cc in te.B[1]]
        S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
        _S[key] = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T, "conjS": np.conj(S)}
    return _S[key]


def evaluate_bl(re_t, im_t, a, b, a2, b2):
    t = complex(re_t, im_t); w = a * t + b; w2 = a2 * t + b2
    readings = higgs(re_t, im_t)
    res, Y = {}, {}
    for sec, (lf, rf) in TC.SECT.items():
        x = B.twist_of(B.SIXY[lf] * w + BL3[lf] * w2, t); yy = B.twist_of(B.SIXY[rf] * w + BL3[rf] * w2, t)
        R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
        for which in ("L_max", "L_2"):
            L = TC.L_of(t.imag, which)
            u = {kk: (math.sqrt(2 * math.pi * L + c[kk]) * R[kk] if c[kk] is not None and 2 * math.pi * L + c[kk] > 0 else 0) for kk in B.UNITS}
            M = B.weighted_M(u)
            for rn, SS in readings.items():
                Ym = B.coupling(SS, M); Y[(sec, which, rn)] = Ym
                sv = np.linalg.svd(Ym, compute_uv=False)
                res[f"{sec}|{which}|{rn}"] = [float(sv[1] / sv[0]), float(sv[2] / sv[0])]
    for which in ("L_max", "L_2"):
        for ru in readings:
            for rd in readings:
                res[f"ckm|{which}|{ru}|{rd}"] = tic.ckm_left(Y[("up", which, ru)], Y[("down", which, rd)])
    return res


def run(task):
    name, a2, b2 = task
    _n, re_t, im_t, a, b = [p for p in POINTS if p[0] == name][0]
    r = evaluate_bl(re_t, im_t, a, b, a2, b2)
    r.update({"point": name, "a2": a2, "b2": b2})
    return r


if __name__ == "__main__":
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 2
    done = set()
    if OUTL.exists():
        for line in OUTL.read_text().splitlines():
            if line.strip():
                r = json.loads(line); done.add((r["point"], r["a2"], r["b2"]))
    todo = [t for t in TASKS if t not in done]
    print(f"{len(TASKS)} points; {len(done)} done; {len(todo)} to do", flush=True)
    t0 = time.time(); n = 0
    with Pool(nw) as P, open(OUTL, "a") as fh:
        for r in P.imap_unordered(run, todo, chunksize=4):
            fh.write(json.dumps(r) + "\n"); fh.flush(); n += 1
    print(f"wrote {n} in {time.time() - t0:.0f} s", flush=True)
