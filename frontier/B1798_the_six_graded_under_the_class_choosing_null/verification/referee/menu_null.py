"""Referee B1798: the class-choosing null (all 266 lines at B1753's 223 apexes; = any class of any partition) under the
three menus B1741's compare.py defines -- seat (the decisive menu: readings (S~,S,S), (S~,S~,S~) x c in {1, 3}), cov (every
(up, down, lepton) reading assignment, 8, x c in {1, 3}: each random target chooses its reading as the data's reading rule
was chosen) and free (the seat's two readings, c continuous: each target chooses its lepton factor).  B1741's
chi2_features / draws unchanged; the census by this referee's own loader (direct_null.build's row reading).  For each menu
the data's own minimum is the obs (seat and cov 2.739034461; free lower).  KD screen (bound sqrt(obs + 0.5)), then the exact
minimum by B1741's expansion over every row and configuration for the candidates.
    python3 -B menu_null.py ARC SEED_LO SEED_HI"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1"); os.environ.setdefault("OPENBLAS_NUM_THREADS", "1"); os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")
import sys, json, pathlib
import numpy as np
from scipy.spatial import cKDTree
from scipy.stats import beta
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import direct_null as DN


def main():
    arc, lo, hi = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    C, Fseat, rows, lab = DN.build(arc)
    out = {}
    for menu in ("seat", "cov", "free"):
        F = C.chi2_features(menu, False)
        Xs = [X for X, f in F]; fs = [f for X, f in F]
        obs = float(C.min_chi2(F, C._A["T6"][None, :])[0])
        # all f in a menu are the same linear map (checked on the data and on random targets below)
        tree = cKDTree(np.concatenate(Xs, axis=0)); x2 = [(X ** 2).sum(1) for X in Xs]
        n = hits = cands = 0; chk = 0.0
        for s in range(lo, hi + 1):
            d6, _ = C.draws(s); T = np.array(d6); n += len(T)
            ts = [f(T) for f in fs]
            for t in ts[1:]: chk = max(chk, float(np.abs(t - ts[0]).max()))
            dist, _i = tree.query(ts[0], k=1, distance_upper_bound=float(np.sqrt(obs + 0.5)))
            cand = np.flatnonzero(np.isfinite(dist)); cands += len(cand)
            if len(cand):
                best = np.full(len(cand), np.inf)
                for X, xx, t in zip(Xs, x2, ts):
                    tc = t[cand]; c = xx[:, None] - 2 * X @ tc.T + (tc ** 2).sum(1)[None, :]
                    best = np.minimum(best, c.min(0))
                hits += int((best <= obs + 1e-9).sum())
        r = float(beta.ppf(0.975, hits + 1, n - hits))
        out[menu] = dict(obs=obs, configs=len(F), n=n, hits=hits, frac=hits / n, r975=r, mr39=39 * r, mr41=41 * r, cands=cands, fmap_check=chk)
        print("%-5s configs %2d  obs %.6f  targets %d  candidates %d  hits %d  frac %.4e  r97.5 %.4e  m*r(39) %.4f  m*r(41) %.4f  (f-map spread %.1e)"
              % (menu, len(F), obs, n, cands, hits, hits / n, r, 39 * r, 41 * r, chk), flush=True)
    json.dump(out, open(pathlib.Path(__file__).resolve().parent / ("menu_null_%s_%d_%d.json" % (arc, lo, hi)), "w"), indent=1)
    print("menu_null exit 0")


if __name__ == "__main__":
    main()
