"""Referee (B1786): every random target's prior-chosen class (argmin seat chi2_six over B1749 + B1755 lines at the same
apexes = the class of its nearest prior feature point), for the conditional null P(event | prior class present at 25/30)."""
import sys, pathlib
import numpy as np
from scipy.spatial import cKDTree
from fractions import Fraction as Fr
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
D = pathlib.Path(__file__).resolve().parent
_G = {}


def _init():
    if "tree" in _G: return
    d = np.load(D / "prior_features.npz"); X = d["X"]
    _G.update(tree=cKDTree(X.reshape(-1, 6)), nrow=X.shape[1], cid=d["cid"], s6=d["s6"])
    import null; null._init(); _G["C"] = null._G["C"]


def run(seed):
    _init(); d6, _ = _G["C"].draws(seed); T = np.array(d6) / _G["s6"]
    dist, idx = _G["tree"].query(T, k=1)
    return seed, _G["cid"][idx % _G["nrow"]].astype(np.int16), dist ** 2


if __name__ == "__main__":
    if sys.argv[1] == "prep":
        import prior
        X, al, src = prior.load_prior(); pcl = sorted(set(al), key=lambda s: float(Fr(s)))
        np.savez(D / "prior_features.npz", X=X, cid=np.array([pcl.index(a) for a in al]), classes=np.array(pcl), s6=prior.s6)
        print("prep done", X.shape); sys.exit()
    from multiprocessing import Pool
    lo, hi, tag = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    with Pool(12) as P:
        res = sorted(P.map(run, range(lo, hi + 1), chunksize=4))
    np.savez(D / ("prior_all_%s.npz" % tag), seeds=np.array([r[0] for r in res]), cls=np.stack([r[1] for r in res]), chi2=np.stack([r[2] for r in res]))
    print("prior_all exit 0")
