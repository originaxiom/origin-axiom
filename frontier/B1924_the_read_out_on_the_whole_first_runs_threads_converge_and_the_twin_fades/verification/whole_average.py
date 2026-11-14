"""P-845's test: does the read-out on the whole converge in n? (the condition of 417a64e72, written before this run)

R_n = the length-weighted average, over allowed words of n moves (each move L or R equally likely; allowed = keeps the
mark), of each word's thread average of the frame's ratios at the mark with the invariant end. The frame uses the
channel norm by B1919's closed form (fast_norm; equal to the quadrature to 1.9e-12, outputs to 4e-14). Nodes per thread:
the trapezoid rule, 30 per unit of geodesic length, at least 64 (the golden thread converges to 1e-4 at 64, the run of
6 to 6e-4 at 128 and 192). Words sampled: 20 per n, by a fixed seed. PRINTED: structure only (sample sizes, the change of
R between successive n, the sampling error). VALUES: the json only. Nothing is compared with a measured number."""
import json, math, pathlib, random, sys
import numpy as np
import thread_average as T
import fast_norm as FN
import covariance as C
HERE = pathlib.Path(__file__).resolve().parent
C._modules()["B"].cA = lambda x, yy, t, R, **kw: FN.cA_fast(x, yy, t, R)


def thread_mean(w):
    beta, betap, ell, g = T.geodesic(w)
    zt = lambda s: complex((beta * 1j * math.exp(s) + betap) / (1j * math.exp(s) + 1))
    s0 = -ell / 2
    if abs(g(zt(s0)) - zt(s0 + ell)) > 1e-7 * (1 + abs(zt(s0))):
        ell = -ell
    nodes = max(64, int(30 * abs(ell)))
    acc = None
    for j in range(nodes):
        o = T.outputs(zt(s0 + ell * j / nodes))
        if acc is None:
            acc = {k: np.zeros(len(v)) for k, v in o.items()}
        for k in acc:
            acc[k] += np.array(o[k]) / nodes
    return acc, abs(ell), nodes


if __name__ == "__main__":
    rng = random.Random(845)
    out = {}
    prev = None
    for n in (8, 10, 12, 14, 16):
        words, seen = [], set()
        while len(words) < 20:
            w = "".join(rng.choice("LR") for _ in range(n))
            if "L" in w and "R" in w and T.keeps_mark(w):
                words.append(w)
        rows = []
        for w in words:
            A, ell, nodes = thread_mean(w)
            rows.append({"word": w, "length": ell, "nodes": nodes, "A": {k: v.tolist() for k, v in A.items()}})
        keys = rows[0]["A"].keys()
        wts = np.array([r["length"] for r in rows])
        R = {k: np.sum([wt * np.array(r["A"][k]) for wt, r in zip(wts, rows)], 0) / wts.sum() for k in keys}
        # the sampling error: the spread of the weighted mean by a jackknife over words
        jk = []
        for i in range(len(rows)):
            m = np.ones(len(rows), bool); m[i] = False
            jk.append({k: np.sum([wt * np.array(r["A"][k]) for wt, r, keep in zip(wts, rows, m) if keep], 0) / wts[m].sum() for k in keys})
        se = max(float(np.max(np.sqrt((len(rows) - 1) * np.mean([(j[k] - R[k]) ** 2 for j in jk], 0)))) for k in keys)
        change = None if prev is None else max(float(np.max(np.abs(R[k] - prev[k]))) for k in keys)
        print("n = %d: %d allowed words (geodesic lengths %.1f to %.1f); sampling error of R %.1e; change of R from the previous n %s"
              % (n, len(rows), min(wts), max(wts), se, "-" if change is None else "%.1e" % change), flush=True)
        out[str(n)] = {"rows": rows, "R": {k: v.tolist() for k, v in R.items()}, "sampling_error": se, "change": change}
        prev = R
        (HERE / "whole_average.json").write_text(json.dumps(out, indent=1))
