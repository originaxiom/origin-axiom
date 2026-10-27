"""Referee null, fast and exact (B1786).  The seat menu's chi2_six over all 588 lines is the squared Euclidean distance from
a target's scaled point T/s6 to the 4 x 147 000 feature points.  A KD-tree finds every target whose nearest point lies within
chi2 <= OBS + MARGIN; for those candidates only, the per-class minima are computed with B1741's own expansion (null.classmin),
so every decision uses B1741's arithmetic.  No target with chi2 > OBS + MARGIN can carry an event (every event needs some
class <= OBS).
    python3 -B null_kd.py SEED_LO SEED_HI TAG [--workers 12]  -> kd_<TAG>.npz"""
import sys, pathlib
import numpy as np
from scipy.spatial import cKDTree
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import null
D = pathlib.Path(__file__).resolve().parent
MARGIN = 0.5
_G = {}


def _init():
    if "tree" in _G: return
    f = np.load(D / "features.npz"); X = f["X"]
    _G["tree"] = cKDTree(X.reshape(-1, 6)); _G["s6"] = f["s6"]
    cl = list(f["classes"]); _G["obs"] = null.classmin(f["T6"][None, :])[cl.index("2/5"), 0]
    null._init()


def run(seed):
    _init()
    d6, _ = null._G["C"].draws(seed); T = np.array(d6)
    dist, _i = _G["tree"].query(T / _G["s6"], k=1, distance_upper_bound=float(np.sqrt(_G["obs"] + MARGIN)))
    cand = np.flatnonzero(np.isfinite(dist))
    cm = null.classmin(T[cand]) if len(cand) else np.zeros((26, 0))
    return seed, len(T), cand, cm, dist[cand] ** 2


if __name__ == "__main__":
    from multiprocessing import Pool
    lo, hi, tag = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    with Pool(nw) as P:
        res = sorted(P.map(run, range(lo, hi + 1)))
    n = sum(r[1] for r in res)
    np.savez(D / ("kd_%s.npz" % tag), n=n, seeds=np.array([r[0] for r in res]),
             cand_seed=np.concatenate([np.full(len(r[2]), r[0]) for r in res]), cand_idx=np.concatenate([r[2] for r in res]),
             classmin=np.concatenate([r[3] for r in res], axis=1), kd_chi2=np.concatenate([r[4] for r in res]))
    print("targets", n, "candidates", sum(len(r[2]) for r in res)); print("null_kd exit 0")
