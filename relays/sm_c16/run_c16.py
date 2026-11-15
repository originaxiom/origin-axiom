#!/usr/bin/env python3
"""SM-C16: the record's action (B1088, S = -Vol sigma) as the weight on B1928's threads (card
relays/cards/SM_C16_the-records-action-as-the-weight.md, pushed before this run).  Value-free: no frame output, no
measured number; only volumes, syllables and the geodesics' heights.
    python3 run_c16.py MAIN_CHECKOUT"""
import json
import math
import pathlib
import random
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
MAIN = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(next((MAIN / "frontier").glob("B1924_*")) / "verification"))
import thread_average as T          # noqa: E402  B1924's, as B1928's fiber_ergodic uses it
import snappy                       # noqa: E402


def reduce_pt(t):                   # B1928's fiber_ergodic.reduce_pt, verbatim
    tr, a, b, _ = T.reduce(t, 0.0, 0.0, {"x": 0.0})
    return tr


def thread(w, per_unit=10):         # B1928's fiber_ergodic.thread, verbatim
    beta, betap, ell, g = T.geodesic(w)
    zt = lambda s: complex((beta * 1j * math.exp(s) + betap) / (1j * math.exp(s) + 1))
    nodes = max(32, int(per_unit * abs(ell))); s0 = -ell / 2
    pts = np.array([[r.real, r.imag] for r in (reduce_pt(zt(s0 + ell * j / nodes)) for j in range(nodes))])
    return pts, abs(ell)


def words():
    rng = random.Random(1924)
    for _ in range(8):              # B1928's preliminary draws
        x = rng.uniform(-0.5, 0.5)
        rng.uniform(math.sqrt(1 - x * x) + 0.01, 3.0)
    out = []
    while len(out) < 3000:
        w = "".join(rng.choice("LR") for _ in range(40))
        if "L" in w and "R" in w:
            out.append(w)
    return out


def syllables(w):
    """runs of one letter, read cyclically"""
    n = sum(1 for i in range(len(w)) if w[i] != w[i - 1])
    return max(n, 1)


def longest_run(w):
    ww = w + w
    best = cur = 1
    for i in range(1, len(ww)):
        cur = cur + 1 if ww[i] == ww[i - 1] else 1
        best = max(best, cur)
    return min(best, len(w))


def spearman(x, y):
    rx = np.argsort(np.argsort(x)); ry = np.argsort(np.argsort(y))
    return float(np.corrcoef(rx, ry)[0, 1])


def wmean_jk(f, wts):
    R = float((wts * f).sum() / wts.sum())
    jk = []
    for bl in np.array_split(np.arange(len(f)), 30):
        m = np.ones(len(f), bool); m[bl] = False
        jk.append((wts[m] * f[m]).sum() / wts[m].sum())
    jk = np.array(jk)
    return R, float(np.sqrt((len(jk) - 1) * np.mean((jk - R) ** 2)))


def main():
    out = {}
    out["C1 vol(LR)"] = float(snappy.Manifold("b++LR").volume())
    W = words()
    vols, syl, run, fr = [], [], [], {2: [], 3: [], 6: []}
    for k, w in enumerate(W):
        M = snappy.Manifold("b++" + w)
        vols.append(float(M.volume()))
        syl.append(syllables(w)); run.append(longest_run(w))
        pts, _ = thread(w)
        for Y in fr:
            fr[Y].append(float(np.mean(pts[:, 1] > Y)))
        if k % 500 == 0:
            print("thread", k, flush=True)
    vols = np.array(vols); syl = np.array(syl); run = np.array(run)
    out["volume range"] = [float(vols.min()), float(vols.max())]
    out["E4"] = {"spearman(Vol, syllables)": spearman(vols, syl), "spearman(Vol, longest run)": spearman(vols, run)}
    out["E1"] = {str(Y): spearman(vols, np.array(fr[Y])) for Y in fr}
    out["weighted"] = {}
    v0 = vols - vols.mean()                       # centred, for numerical range only (cancels in the ratio)
    rng = np.random.default_rng(16)
    for Y in fr:
        f = np.array(fr[Y])
        u, ue = wmean_jk(f, np.ones(len(f)))
        rows = {"uniform": [u, ue]}
        for s in (+1, -1):
            for sig in (0.0, 0.05, 0.1, 0.2, 0.5, 1.0):
                R, e = wmean_jk(f, np.exp(s * sig * v0))
                rows["s=%+d sigma=%g" % (s, sig)] = [R, e, (R - u) / max(e, 1e-300)]
        sh = np.exp(+0.5 * rng.permutation(v0))
        R, e = wmean_jk(f, sh)
        rows["C3 shuffled, s=+1 sigma=0.5"] = [R, e, (R - u) / max(e, 1e-300)]
        out["weighted"][str(Y)] = rows
        print("Y", Y, "uniform %.4f" % u, {k: round(v[0], 4) for k, v in rows.items() if "0.5" in k}, flush=True)
    (HERE / "c16_results.json").write_text(json.dumps(out, indent=1))
    print(json.dumps({k: out[k] for k in ("C1 vol(LR)", "volume range", "E1", "E4")}, indent=1))


if __name__ == "__main__":
    main()
