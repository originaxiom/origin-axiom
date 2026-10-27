"""Referee null (B1786): per random six-target (B1741's draws(seed), unchanged), the seat-menu chi2_six minimum within each
of the 26 slope classes of the 588 lines (orders 25, 30).  The chi2 expansion is B1741's min_chi2's (x2 - 2 X t + t2).
    python3 -B null.py SEED_LO SEED_HI [--workers 12]   -> classmin_<seed>.npy (26 x 4000, float64)"""
import os, sys, pathlib, importlib.util
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
OUT = pathlib.Path(__file__).resolve().parent / "classmin"
_G = {}


def _init():
    if "X" in _G: return
    d = np.load(ROOT / "audit/referee_b1786/features.npz")
    order = np.argsort(d["cid"], kind="stable"); cid = d["cid"][order]
    X = d["X"][:, order, :].copy()
    starts = np.r_[0, np.flatnonzero(np.diff(cid)) + 1]
    assert len(starts) == 26 and (cid[starts] == np.arange(26)).all()
    _G.update(X=X, x2=(X ** 2).sum(2), s6=d["s6"], starts=starts)
    spec = importlib.util.spec_from_file_location("b1741_compare", ROOT / "frontier/B1741_tau_from_the_thread_rule_the_line_free/verification/compare.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); _G["C"] = m


def classmin(T, block=250):
    _init(); X, x2, s6, st = _G["X"], _G["x2"], _G["s6"], _G["starts"]
    t_all = T / s6; out = np.full((26, len(T)), np.inf)
    for s0 in range(0, len(T), block):
        t = t_all[s0:s0 + block]; t2 = (t ** 2).sum(1)
        for k in range(X.shape[0]):
            c = X[k] @ t.T; c *= -2; c += x2[k][:, None]; c += t2[None, :]
            np.minimum(out[:, s0:s0 + block], np.minimum.reduceat(c, st, axis=0), out=out[:, s0:s0 + block])
    return out


def run(seed):
    _init(); p = OUT / ("classmin_%d.npy" % seed)
    if p.exists(): return seed
    d6, _ = _G["C"].draws(seed)
    np.save(p, classmin(np.array(d6)))
    return seed


if __name__ == "__main__":
    from multiprocessing import Pool
    OUT.mkdir(exist_ok=True)
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    with Pool(nw) as P:
        for s in P.imap_unordered(run, range(lo, hi + 1)): print("seed", s, flush=True)
    print("null exit 0")
