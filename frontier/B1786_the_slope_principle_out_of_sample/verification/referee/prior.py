"""Referee (B1786): the class-chosen-on-prior-data null.  Each random target chooses its slope class as the argmin of the
seat-menu chi2_six over the PRIOR lines at the same 125 apexes (B1749: orders 1-12; B1755: orders 13, 14, 15, 20) -- the way
the data chose 2/5 -- and the event is then tested at orders 25 and 30 with the sealed cell's thresholds."""
import sys, json, math, pathlib, importlib.util
import numpy as np
from fractions import Fraction as Fr
from scipy.stats import beta
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import null
R = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()) / "frontier"
D = pathlib.Path(__file__).resolve().parent
f = np.load(D / "features.npz"); s6 = f["s6"]; T6 = f["T6"]; cl25 = list(f["classes"])
LC3 = math.log(3); SEAT = ((1, 0, 0), (1, 1, 1)); RD = ("S", "St")


def load_prior():
    sp = importlib.util.spec_from_file_location("b1726_census", R / "B1726_the_two_ingredients_replicated/verification/census.py")
    K = importlib.util.module_from_spec(sp); sys.modules["b1726_census"] = K; sp.loader.exec_module(K); L26 = K.lines()
    lg = lambda x: np.log(np.maximum(np.array(x, dtype=float), 1e-300))
    U, Dn, E, al, src = [], [], [], [], []
    for tag, p in (("B1749", R / "B1749_the_six_at_fresh_apexes/verification/census.jsonl"), ("B1755", R / "B1755_the_six_on_the_lines_of_order_13_to_20/verification/census.jsonl")):
        for l in open(p, encoding="utf-8"):
            if not l.strip(): continue
            r = json.loads(l)
            a = str(Fr(L26[r["line"]][0])) if tag == "B1749" else r["alpha"]
            for h in ("L_max", "L_2"):
                U.append([lg(r[f"up|{h}|{x}"]) for x in RD]); Dn.append([lg(r[f"down|{h}|{x}"]) for x in RD]); E.append([lg(r[f"lep|{h}|{x}"]) for x in RD])
                al.append(a); src.append(tag)
    U, Dn, E = np.array(U), np.array(Dn), np.array(E)
    Xs = []
    for (a, b, l) in SEAT:
        for k in (0.0, LC3):
            Xs.append(np.concatenate([U[:, a] / s6[0:2], Dn[:, b] / s6[2:4], ((E[:, l, 0] + k) / s6[4])[:, None], ((E[:, l, 1] - k) / s6[5])[:, None]], axis=1))
    return np.stack(Xs), np.array(al), np.array(src)


def classmin_prior(X, cid, ncls, T):
    t = T / s6; out = np.full((ncls, len(T)), np.inf)
    order = np.argsort(cid, kind="stable"); c = cid[order]; st = np.r_[0, np.flatnonzero(np.diff(c)) + 1]
    for k in range(X.shape[0]):
        Xk = X[k][order]; x2 = (Xk ** 2).sum(1)
        for s0 in range(0, len(T), 200):
            tt = t[s0:s0 + 200]; m = Xk @ tt.T; m *= -2; m += x2[:, None]; m += (tt ** 2).sum(1)[None, :]
            out[:, s0:s0 + 200] = np.minimum(out[:, s0:s0 + 200], np.minimum.reduceat(m, st, axis=0))
    return out


if __name__ == "__main__":
    X, al, src = load_prior()
    pcl = sorted(set(al), key=lambda s: float(Fr(s))); cid = np.array([pcl.index(a) for a in al])
    data_p = classmin_prior(X, cid, len(pcl), T6[None, :])[:, 0]
    # validation against the published minima
    for tag in ("B1749", "B1755"):
        m = src == tag; t = T6 / s6
        print(tag, "seat chi2_six min over its census: %.4f" % min(((X[k][m] - t) ** 2).sum(1).min() for k in range(4)))
    print("data: prior argmin class", pcl[int(np.argmin(data_p))], "%.3f; runner-up %s %.3f" % (np.sort(data_p)[0], pcl[int(np.argsort(data_p)[1])], np.sort(data_p)[1]))
    data25 = null.classmin(T6[None, :])[:, 0]; i25 = cl25.index("2/5"); obs = data25[i25]
    null._init(); C = null._G["C"]
    for tag in ("valid", "fresh160k", "fresh10M"):
        k = np.load(D / ("kd_%s.npz" % tag)); n = int(k["n"]); M = k["classmin"]
        T = []
        for s in np.unique(k["cand_seed"]):
            d6, _ = C.draws(int(s)); d6 = np.array(d6); T.append(d6[k["cand_idx"][k["cand_seed"] == s]])
        T = np.concatenate(T) if T else np.zeros((0, 6))
        P = classmin_prior(X, cid, len(pcl), T)
        chosen = [pcl[i] for i in P.argmin(0)]
        ev = np.zeros(M.shape[1], bool)
        for j, c in enumerate(chosen):
            if c not in cl25: continue
            ci = cl25.index(c)
            ev[j] = M[ci, j] <= obs + 1e-9 and np.delete(M[:, j], ci).min() >= 16.75
        h = int(ev.sum()); r = beta.ppf(0.975, h + 1, n - h)
        anyhit = M.min(0) <= obs + 1e-9
        print("\n== %s (%d targets): PRIOR-CHOSEN-CLASS null: hits %d frac %.3e r97.5 %.3e m*r(41) %.4f m*r(73) %.4f" % (tag, n, h, h / n, r, 41 * r, 73 * r))
        print("   of the any-class hits at 25/30 (%d): prior choice = the 25/30 carrying class in %d; chosen classes of the event hits: %s"
              % (anyhit.sum(), sum(1 for j in np.flatnonzero(anyhit) if chosen[j] == cl25[int(M[:, j].argmin())]),
                 {c: chosen.count(c) for c in set(chosen[j] for j in np.flatnonzero(ev))}))
