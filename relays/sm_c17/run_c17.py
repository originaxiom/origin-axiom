#!/usr/bin/env python3
"""SM-C17: the record's action (B1088, S = -k CS - sigma Vol) as a phase on B1928's threads (card
relays/cards/SM_C17_the-action-as-a-phase.md, pushed before this run).  Value-free: volumes, Chern-Simons invariants and
heights only.
    python3 run_c17.py MAIN_CHECKOUT"""
import json
import math
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "sm_c16"))
sys.argv = [sys.argv[0], sys.argv[1]]
import run_c16 as C16               # noqa: E402  SM-C16's threads, words and thread() (B1928's, verbatim)
import snappy                       # noqa: E402


def coh(ph):
    return float(abs(np.mean(np.exp(1j * ph)))) if len(ph) else float("nan")


def main():
    out = {}
    M = snappy.Manifold("b++LR")
    out["C1"] = {"CS(LR)": float(M.chern_simons()), "Vol(LR)": float(M.volume())}
    W = C16.words()
    vol, cs, f2, f3 = [], [], [], []
    for k, w in enumerate(W):
        T = snappy.Manifold("b++" + w)
        vol.append(float(T.volume())); cs.append(float(T.chern_simons()))
        pts, _ = C16.thread(w)
        f2.append(float(np.mean(pts[:, 1] > 2))); f3.append(float(np.mean(pts[:, 1] > 3)))
        if k % 1000 == 0:
            print("thread", k, flush=True)
    vol, cs, f2, f3 = map(np.array, (vol, cs, f2, f3))
    order = np.argsort(-f3, kind="stable")
    cusp = order[: len(W) // 10]
    bulk = order[len(W) // 2:]
    out["bins"] = {"cusp-heavy n": int(len(cusp)), "bulk n": int(len(bulk)),
                   "mean f3 cusp-heavy": float(f3[cusp].mean()), "mean f3 bulk": float(f3[bulk].mean()),
                   "Vol spread (sd) cusp-heavy": float(vol[cusp].std()), "Vol spread (sd) bulk": float(vol[bulk].std())}
    rng = np.random.default_rng(17)
    rows = {}
    for kk in (0, 1, 2):
        for sig in (0.0, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0):
            ph = -(2 * math.pi * kk * cs + sig * vol)
            fl_c, fl_b = [], []
            for _ in range(200):
                p = rng.permutation(ph)
                fl_c.append(coh(p[cusp])); fl_b.append(coh(p[bulk]))
            z = np.exp(1j * ph)
            share = float(abs((z * f3).sum()) / max(abs(z.sum()), 1e-300))
            rows["k=%d sigma=%g" % (kk, sig)] = {
                "C cusp-heavy": coh(ph[cusp]), "C bulk": coh(ph[bulk]),
                "floor95 cusp-heavy": float(np.percentile(fl_c, 95)), "floor95 bulk": float(np.percentile(fl_b, 95)),
                "C all": coh(ph), "effective cusp share f3": share}
            r = rows["k=%d sigma=%g" % (kk, sig)]
            print("k=%d sigma=%-4g C cusp %.3f (floor %.3f)  C bulk %.3f (floor %.3f)  share %.4f" % (
                kk, sig, r["C cusp-heavy"], r["floor95 cusp-heavy"], r["C bulk"], r["floor95 bulk"], share), flush=True)
    out["uniform f3"] = float(f3.mean())
    out["rows"] = rows
    out["1/sqrt(n)"] = {"cusp-heavy": 1 / math.sqrt(len(cusp)), "bulk": 1 / math.sqrt(len(bulk))}
    (HERE / "c17_results.json").write_text(json.dumps(out, indent=1))
    print(json.dumps({k: out[k] for k in ("C1", "bins", "uniform f3", "1/sqrt(n)")}, indent=1))


if __name__ == "__main__":
    main()
