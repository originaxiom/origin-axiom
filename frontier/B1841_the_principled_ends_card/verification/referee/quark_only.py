"""B1841 third opinion (3), POST HOC, labelled: on order-5 lines the lepton ratios ARE the down ratios (order5_identity.py),
so the six's lepton half at B1841's best row tests the data's Georgi-Jarlskog structure with c fitted. This read-out asks
whether the frame's QUARK four alone (ln c/t, u/t, s/b, d/b) are significant: the minimum over B1841's same 237 272 rows and
the same (up, down) readings of the seat menu, against B1741's same random hierarchies (their quark four), seeds 51001-51250.
Also the same per end, and the full six's sealed D for comparison. One look at the six (the quark four), post hoc; no held-out
target is touched."""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys, json, math, pathlib, importlib.util, time
import numpy as np
from scipy.spatial import cKDTree
from scipy.stats import beta
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "GENESIS.md").is_file()); H41 = ROOT / "frontier/B1841_the_principled_ends_card/verification"
OUT = pathlib.Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location("b1841_look", H41 / "look.py"); L41 = importlib.util.module_from_spec(sp); sys.modules["b1841_look"] = L41; sp.loader.exec_module(L41)
def main():
    from multiprocessing import get_context
    t0 = time.time(); L = L41.L39(); M = L41.C41().C39().mods(); nl = len(M["LINES"]); na = len(M["AP"])
    cache = OUT / "features_b1841.npz"
    if cache.exists():
        z = np.load(cache); U, Dn = z["U"], z["D"]
    else:
        ne = np.load(H41 / "norms.npz")["norms"].shape[2]
        U = np.zeros((na, nl, ne, 2, 2)); Dn = np.zeros_like(U); E = np.zeros_like(U)
        with get_context("spawn").Pool(5) as P:
            for i, u, d, e in P.imap_unordered(L41.apex_features, range(na), chunksize=1): U[i], Dn[i], E[i] = u, d, e
        np.savez(cache, U=U, D=Dn, E=E)
    ne = U.shape[2]; lab_e = np.broadcast_to(np.arange(ne)[None, None, :], U.shape[:3]).ravel()
    U, Dn = U.reshape(-1, 2, 2), Dn.reshape(-1, 2, 2)
    print("features %s (%.0f s)" % (U.shape, time.time() - t0), flush=True)
    C = L.CMPM(); v = json.loads(C.DATA.read_text(encoding="utf-8"))["masses_GeV"]["value"]
    T4 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"]])); s6, _ = C.sigmas(); s4 = s6[:4]
    pairs = sorted({(a, b) for (a, b, l) in C.SEAT})
    print("seat menu's (up, down) reading pairs: %s" % pairs, flush=True)
    res = {"label": "POST HOC third-opinion read-out (B1841): the quark four alone", "pairs": [list(p) for p in pairs]}
    for tag, sel in [("all_ends", np.arange(len(U)))] + [("end_%d" % j, np.flatnonzero(lab_e == j)) for j in range(ne)]:
        pts = np.concatenate([np.concatenate([U[sel, a], Dn[sel, b]], axis=1) / s4 for (a, b) in pairs])
        ok = np.all(np.isfinite(pts), axis=1); tree = cKDTree(pts[ok])
        d0, i0 = tree.query(T4 / s4); obs = float(d0 ** 2)
        hits = 0; n = 0
        for s in range(51001, 51251):
            d6, _ = C.draws(s); T = np.array(d6)[:, :4] / s4; n += len(T)
            dd, _ = tree.query(T, k=1, distance_upper_bound=math.sqrt(obs) + 1e-12); hits += int(np.sum(dd ** 2 <= obs + 1e-9))
        r975 = float(beta.ppf(0.975, hits + 1, n - hits)) if hits < n else 1.0
        res[tag] = {"obs_chi2_quark4": obs, "hits": hits, "n": n, "rate": hits / n, "r97.5": r975}
        print("%-9s quark-four minimum chi2 %.6f; null hits %d / %d = %.4e (r97.5 %.4e) (%.0f s)" % (tag, obs, hits, n, hits / n, r975, time.time() - t0), flush=True)
    (OUT / "quark_only.json").write_text(json.dumps(res, indent=1) + "\n", encoding="utf-8")
    print("quark_only exit 0 (%.0f s)" % (time.time() - t0))
if __name__ == "__main__":
    main()
