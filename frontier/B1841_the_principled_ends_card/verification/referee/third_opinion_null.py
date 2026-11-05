"""B1841 third opinion (2): (a) 30 random rows' frame ratios through B1842's independent per-sector instrument against the
sealed features; (b) a BRUTE-FORCE null (every target x every row, no KD screen; my own chi2) on seeds 51001-51010 against
the sealed null() on the same seeds, per mode; the data's minimum recomputed brute-force over all rows."""
import os, sys, math, json, pathlib, importlib.util, random, time
from fractions import Fraction as F
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "GENESIS.md").is_file()); H41 = ROOT / "frontier/B1841_the_principled_ends_card/verification"
sp = importlib.util.spec_from_file_location("b1841_look", H41 / "look.py"); L41 = importlib.util.module_from_spec(sp); sys.modules["b1841_look"] = L41; sp.loader.exec_module(L41)
def main():
    from multiprocessing import get_context
    t0 = time.time(); L = L41.L39(); c41 = L41.C41(); M = c41.C39().mods(); nl = len(M["LINES"]); na = len(M["AP"])
    arr = np.load(H41 / "norms.npz")["norms"]; ne = arr.shape[2]
    U = np.zeros((na, nl, ne, 2, 2)); Dn = np.zeros_like(U); E = np.zeros_like(U)
    with get_context("spawn").Pool(7) as P:
        for i, u, d, e in P.imap_unordered(L41.apex_features, range(na), chunksize=1): U[i], Dn[i], E[i] = u, d, e
    print("features rebuilt (sealed code) %.0f s" % (time.time() - t0), flush=True)
    # (a) independent spot check
    sys.path.insert(0, str(ROOT / "frontier/B1842_the_closure_instruments/verification")); import exact_card_instrument as X
    acc = c41.C39().load_acc(); rng = random.Random(41003); worst = 0.0
    ENDS = lambda r: [r["L_2"], math.log(2), r["L_max"], r["L_2"] - math.pi / 2]
    for _ in range(30):
        i = rng.randrange(na); k = rng.randrange(nl); j = rng.randrange(ne); r = acc[i]; a, b = M["LINES"][k]
        Y, info = X.yukawas_exact(r["tau0"][0], r["tau0"][1], a, b, ENDS(r)[j] - r["L_max"], ("up", "down", "lep"))
        for q, (sec, A) in enumerate((("up", U), ("down", Dn), ("lep", E))):
            for rn_i, rn in enumerate(("S", "St")):
                indep = np.log(X.ratios_of(Y[sec][rn])); sealed = A[i, k, j, rn_i]
                worst = max(worst, float(np.max(np.abs(indep - sealed))))
    print("(a) 30 random rows, independent per-sector instrument vs sealed features: max |delta ln ratio| %.2e" % worst, flush=True)
    U, Dn, E = U.reshape(-1, 2, 2), Dn.reshape(-1, 2, 2), E.reshape(-1, 2, 2)
    C = L.CMPM(); v = json.loads(C.DATA.read_text())["masses_GeV"]["value"]
    T6 = np.log([v["c"]/v["t"], v["u"]/v["t"], v["s"]/v["b"], v["d"]/v["b"], v["mu"]/v["tau"], v["e"]/v["tau"]]); s6, _ = C.sigmas()
    KLO, KHI = math.log(1/3), math.log(5); SET9 = L.SET9; SEATK = L.SEATK
    blocks = [(np.concatenate([U[:, a] / s6[0:2], Dn[:, b] / s6[2:4]], axis=1), E[:, l, 0], E[:, l, 1]) for (a, b, l) in C.SEAT]
    def brute(Tm, mode):
        out = np.full(len(Tm), np.inf)
        for Q, ea, eb in blocks:
            tq = Tm[:, :4] / s6[:4]
            for st in range(0, len(Tm), 64):
                tb = Tm[st:st+64]; d = ((Q[:, None, :] - tq[st:st+64][None, :, :]) ** 2).sum(2)
                u0 = ea[:, None] - tb[None, :, 4]; v0 = eb[:, None] - tb[None, :, 5]
                if mode == "bounded":
                    k = np.clip((s6[4]**2 * v0 - s6[5]**2 * u0) / (s6[4]**2 + s6[5]**2), KLO, KHI); lep = (u0 + k)**2 / s6[4]**2 + (v0 - k)**2 / s6[5]**2
                else:
                    ks = SET9 if mode == "set9" else SEATK; lep = np.min([(u0 + q)**2 / s6[4]**2 + (v0 - q)**2 / s6[5]**2 for q in ks], axis=0)
                out[st:st+64] = np.minimum(out[st:st+64], (d + lep).min(0))
        return out
    obs = {m: float(brute(T6[None, :], m)[0]) for m in L.MODES}
    print("(b) brute-force data minima %s (B1841: bounded 4.726887, set9 5.410482, seat 11.977974)" % {m: round(x, 6) for m, x in obs.items()}, flush=True)
    meas = L.Measure(U, Dn, E, s6); nK = L.null(meas, obs, (51001, 51010), lambda s: None, "kd")
    hits = {m: 0 for m in L.MODES}; n = 0
    for sd in range(51001, 51011):
        d6, _ = C.draws(sd); Tm = np.array(d6); n += len(Tm)
        for m in L.MODES: hits[m] += int((brute(Tm, m) <= obs[m] + 1e-9).sum())
        print("   seed %d done (%.0f s)" % (sd, time.time() - t0), flush=True)
    for m in L.MODES:
        print("(b) %-7s brute-force hits %d / %d  vs  sealed KD null %d -> %s" % (m, hits[m], n, nK[m]["hits"], "AGREE" if hits[m] == nK[m]["hits"] else "DIFFER"), flush=True)
    print("third opinion (2) exit 0 (%.0f s)" % (time.time() - t0))
if __name__ == "__main__":
    main()
