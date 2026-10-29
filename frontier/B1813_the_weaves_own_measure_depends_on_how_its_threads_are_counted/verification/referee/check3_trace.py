"""Check 3: the trace ordering.
(a) Completeness, independent of the draft's DFS: every SL(2,Z) matrix with non-negative entries, trace t <= T, both
    off-diagonal entries >= 1 (a, d >= 1, bc = ad - 1), factored into L, R by Euclid's descent, rotated to its least
    rotation, kept if primitive.  Class counts at T = 12, 18, 24, 30 against the draft's 29, 60, 96, 151; also the
    prime-geodesic-theorem scale T^2 / (2 ln T).
(b) The length-weighted height tail at T = 18, 24, 30 (draft's table) and at T = 50, 100, 200, 400 (convergence to
    hyperbolic area, 3/(pi Y)), by the excursion formula (exact for Y >= 1) cross-checked by reduced sampling at T <= 30.
(c) Per-class-normalised weights (each class mass 1) beside length weights."""
import math, sys, os, json
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from refcore import runs, cf_forward, segments_from_runs, reduce_vec, hyp_tail


def word_of(a, b, c, d):
    w = []
    while (a, b, c, d) != (1, 0, 0, 1):
        if a >= c and b >= d: w.append("L"); a, b = a - c, b - d
        else: w.append("R"); c, d = c - a, d - b
        assert min(a, b, c, d) >= 0
    return "".join(w)


def classes_upto(T):
    out = {}
    for t in range(3, T + 1):
        for a in range(1, t):
            d = t - a; n = a * d - 1
            if n < 1: continue
            for b in range(1, n + 1):
                if n % b: continue
                c = n // b; w = word_of(a, b, c, d)
                k = len(w); cw = min(w[i:] + w[:i] for i in range(k))
                if any(cw == cw[:p] * (k // p) for p in range(1, k) if k % p == 0): continue
                out[cw] = t
    return out


def excursion_tail(classes, Ys, norm=False):
    num = {Y: 0.0 for Y in Ys}; den = 0.0
    for w, t in classes.items():
        a = runs(w); n = len(a); ell = 2 * math.acosh(t / 2); wt = 1.0 / ell if norm else 1.0
        den += wt * ell
        for i in range(n):
            x = cf_forward(a, i); y = 1.0 / cf_forward([a[(i - 1 - k) % n] for k in range(n)], 0)
            rho = (x + y) / 2
            for Y in Ys:
                if rho > Y: num[Y] += wt * 2 * math.acosh(rho / Y)
    return {str(Y): round(num[Y] / den, 4) for Y in Ys}


Ys = [1.5, 2.0, 3.0, 4.0, 6.0]
out = {"hyperbolic area": {str(Y): round(hyp_tail(Y), 4) for Y in Ys}}
draft_counts = {12: 29, 18: 60, 24: 96, 30: 151}
for T in (12, 18, 24, 30, 50, 100, 200, 400):
    cl = classes_upto(T)
    row = {"classes": len(cl), "draft": draft_counts.get(T), "T^2/(2 ln T)": round(T * T / (2 * math.log(T)), 1),
           "length-weighted": excursion_tail(cl, Ys), "per-class mass 1": excursion_tail(cl, Ys, norm=True)}
    if T <= 30:
        H, W = [], []
        for w in cl:
            z, wt, _ = segments_from_runs(runs(w)); H.append(reduce_vec(z).imag); W.append(wt)
        H, W = np.concatenate(H), np.concatenate(W)
        row["sampled (reduced)"] = {str(Y): round(float(W[H > Y].sum() / W.sum()), 4) for Y in Ys}
    out[T] = row; print(T, json.dumps(row), flush=True)
print("hyperbolic", out["hyperbolic area"])
json.dump(out, open(os.path.join(os.path.dirname(__file__), "check3_trace.json"), "w"), indent=1)
