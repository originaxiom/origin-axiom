"""B1814 (P-437, stage 3): the sealed comparison.  Is the measured world a typical draw from the weave's own measure, in
today's frame, and under which clock?  Reads census.jsonl (this arc's draws, both arms); scores them by B1741's sealed
measure, loaded unchanged with its sha256 asserted before execution (its data, its sigmas s6 and s9, its random
hierarchies).  Nothing else of B1741 is used.

The observables: the six mass log-ratios log(c/t, u/t, s/b, d/b, mu/tau, e/tau) (the nine add log|V_us|, |V_cb|, |V_ub|).
A draw above Im tau = YCAP was not computed (census.py): its ratios are below 1e-12 (control C1e).

The conditioning (the pre-seal review's B3): every reference is the arm's RESOLVED draws -- those whose six ratios all
exceed FLOOR = 1e-12, the instrument's precision -- and every target must be resolved too (the data's ratios all exceed
1e-6).  Floored values form atoms that dominate unconditioned statistics (the review: 5.8% of A1's draws at the all-six
floor set A1's 95th percentile of Fisher's statistic).  Unconditioned statistics are read-outs.

The configurations:
    unforced    per draw, the horocycle and each sector's reading drawn uniformly (seed 18142, the same sequence for
                both arms), c = 1: nothing put in by hand
    hand        (S~, S, S) and c = 3 (B1726's two ingredients), the horocycle drawn by the same sequence
    fixed       any reading triple, c and horocycle ("drawn", "L_max", "L_2"): the free null's menu and the read-outs
The statistics (W57's, so the comparison is like for like, and one that needs no metric):
    p_nn   the target's nearest-draw distance (max over the numbers of |x - t| / sigma, B1741's s6) against each
           reference draw's own nearest distance among the others: (1 + #{at least as far}) / (N + 1)
    p_F    Fisher's -2 sum log p_k of the two-sided marginal mid-ranks, the target's against each reference draw's own
           (leave one out): (1 + #{as large}) / (N + 1)
The arms: A0 (the move clock), A1 (the geometric clock), N (anarchy: independent complex Gaussian Yukawas, W57's null;
4 000 draws, seed 18143).
    OPENBLAS_NUM_THREADS=1 nice -n 10 python3 -B compare.py      # writes comparison.json beside itself
Importing computes nothing."""
import sys, json, math, random, hashlib, importlib.util, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
B1741 = (ROOT / "frontier" / "B1741_tau_from_the_thread_rule_the_line_free" / "verification" / "compare.py",
         "6308ed93e53ab99522cf654a85250f1299e9fa334ce13f92a74334cd7812f3bd")
CENSUS = HERE / "census.jsonl"
FLOOR, YCAP, NDRAW, NANARCHY = 1e-12, 60.0, 4000, 4000
LF, LC3, LRAW = math.log(FLOOR), math.log(3), math.log(1e-300)
FLOORS_READOUT = (1e-16, 1e-8)
SEEDS = list(range(1741, 1761)); NFREE = 1000          # the free null: the first 1 000 six-targets of each seed
M_LOOKS = 53
RD = ("S", "St"); HS = ("L_max", "L_2")
READINGS = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
_C = {}


def C():
    if "C" not in _C:
        path, sha = B1741
        assert hashlib.sha256(path.read_bytes()).hexdigest() == sha
        sp = importlib.util.spec_from_file_location("b1741_compare", path); m = importlib.util.module_from_spec(sp)
        sys.modules["b1741_compare"] = m; sp.loader.exec_module(m); _C["C"] = m
    return _C["C"]


def lg(x): return np.log(np.maximum(np.array(x, dtype=float), 1e-300))


def load():
    good = []
    for l in CENSUS.read_text(encoding="utf-8").splitlines():
        if l.strip(): good.append(json.loads(l))
    rows = good
    assert len(rows) == 2 * NDRAW == len({(r["arm"], r["i"]) for r in rows})
    out = {}
    for arm in ("A0", "A1"):
        rs = sorted((r for r in rows if r["arm"] == arm), key=lambda r: r["i"]); assert [r["i"] for r in rs] == list(range(NDRAW))
        n = len(rs); S = {k: np.full((n, 2, 2, 2), LRAW) for k in ("up", "down", "lep")}; K = np.full((n, 2, 2, 2, 3), np.nan)
        cap = np.array([r["Im_tau"] > YCAP for r in rs])
        for j, r in enumerate(rs):
            if cap[j]: assert "up|L_2|S" not in r; continue
            for hi, h in enumerate(HS):
                for ai, a in enumerate(RD):
                    for sec in S: S[sec][j, hi, ai] = lg(r["%s|%s|%s" % (sec, h, a)])
                    for bi, b in enumerate(RD): K[j, hi, ai, bi] = lg(r["ckm|%s|%s|%s" % (h, a, b)][:3])
        for sec in S: assert np.isfinite(S[sec]).all()
        assert np.isfinite(K[~cap]).all()
        out[arm] = {"S": S, "K": K, "cap": cap, "im": np.array([r["Im_tau"] for r in rs]), "rows": rs,
                    "warned": int(sum(1 for r in rs if r.get("warnings")))}
    return out


def configs(seed=18142):
    rng = random.Random(seed)
    return [(rng.randrange(2), rng.randrange(2), rng.randrange(2), rng.randrange(2)) for _ in range(NDRAW)]   # h, up, down, lep


def features(A, cf, mode="unforced", reading=None, c=1, horo="drawn", lf=LF):
    """X6 (n x 6), X9 (n x 9; NaN where capped), resolved (n,): every one of the six above the floor, and not capped"""
    S, K = A["S"], A["K"]; n = len(A["cap"]); X6 = np.zeros((n, 6)); X9 = np.full((n, 9), np.nan)
    if mode == "hand": reading, c = (1, 0, 0), 3
    for j in range(n):
        h, ru, rdn, rl = cf[j]
        if reading is not None: ru, rdn, rl = reading
        if horo != "drawn": h = HS.index(horo)
        x = np.concatenate([S["up"][j, h, ru], S["down"][j, h, rdn], S["lep"][j, h, rl]])
        x = x + np.array([0, 0, 0, 0, math.log(c), -math.log(c)])
        X6[j] = x
        if not A["cap"][j]: X9[j] = np.concatenate([X6[j], np.maximum(K[j, h, ru, rdn], lf)])
    res = (X6 > lf).all(1) & ~A["cap"]
    return np.maximum(X6, lf), X9, res


def anarchy(seed=18143):
    rng = np.random.default_rng(seed); X6, X9 = np.zeros((NANARCHY, 6)), np.zeros((NANARCHY, 9))
    for j in range(NANARCHY):
        Ys = [(rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))) / math.sqrt(2) for _ in range(3)]
        r = []; Us = []
        for Y in Ys:
            U, sv, _ = np.linalg.svd(Y); r += [sv[1] / sv[0], sv[2] / sv[0]]; Us.append(U[:, ::-1])
        V = np.conj(Us[0].T) @ Us[1]
        X6[j] = lg(r); X9[j] = np.concatenate([X6[j], lg([abs(V[0, 1]), abs(V[1, 2]), abs(V[0, 2])])])
    return X6, X9


def dmin(X, T, sig, self_exclude=False, block=256):
    """for each target row of T, the max-norm (sigma units) distance to its nearest row of X"""
    Xs = X / sig; out = np.empty(len(T))
    for s0 in range(0, len(T), block):
        t = T[s0:s0 + block] / sig; d = np.abs(Xs[None, :, :] - t[:, None, :]).max(2)
        if self_exclude: d[np.arange(len(t)), np.arange(s0, s0 + len(t))] = np.inf
        out[s0:s0 + block] = d.min(1)
    return out


def fisher(X, T, self_exclude=False):
    """-2 sum_k log p_k, p_k two-sided by mid-rank in X's k-th marginal (leave one out when T is X itself)"""
    n = len(X); phi = np.zeros(len(T))
    for k in range(X.shape[1]):
        xs = np.sort(X[:, k]); lo = np.searchsorted(xs, T[:, k], "left"); hi = np.searchsorted(xs, T[:, k], "right")
        if self_exclude: F = (lo + 0.5 * (hi - lo - 1) + 0.5) / n                  # the others: n - 1 values, + 1
        else: F = (lo + 0.5 * (hi - lo) + 0.5) / (n + 1)
        p = 2 * np.minimum(F, 1 - F); phi += -2 * np.log(p)
    return phi


class Ref:
    """a reference model: its draws, their own leave-one-out nearest distances and Fisher statistics (computed once)"""
    def __init__(self, X, sig):
        self.X, self.sig, self.n = X, sig, len(X)
        self.dX = np.sort(dmin(X, X, sig, True)); self.fX = np.sort(fisher(X, X, True))

    def score(self, t):
        t = np.atleast_2d(t); dt = dmin(self.X, t, self.sig); ft = fisher(self.X, t)
        p_nn = (1 + self.n - np.searchsorted(self.dX, dt, "left")) / (self.n + 1)
        p_F = (1 + self.n - np.searchsorted(self.fX, ft, "left")) / (self.n + 1)
        return p_nn, p_F, dt, ft

    def q95(self): return float(np.quantile(self.dX, 0.95))


def marginals(X, t):
    out = []
    for k in range(X.shape[1]):
        x = X[:, k]; F = (np.sum(x < t[k]) + 0.5 * np.sum(x == t[k]) + 0.5) / (len(x) + 1); out.append(float(2 * min(F, 1 - F)))
    return out


def nearest(X, t, sig, A=None, cf=None, idx=None):
    d = np.abs(X / sig - t / sig).max(1); j = int(np.argmin(d)); o = {"distance": float(d[j]), "per_number": (np.abs(X[j] - t) / sig).tolist()}
    if A is not None:
        jj = int(idx[j]); r = A["rows"][jj]
        o.update(draw=jj, tau=[r["Re_tau"], r["Im_tau"]], trace=r["trace"], word=r["word"][:40], line=[r["alpha"], r["b"]], order=r["order"],
                 configuration=list(cf[jj]))
    return o


def main():
    Cm = C(); s6, s9 = Cm.sigmas(); Ad = Cm.arrays(); T6, T9 = Ad["T6"], Ad["T9"]
    assert (T6 > LF).all() and (T9 > LF).all()
    D = load(); cf = configs(); out = {"N": NDRAW, "floor": FLOOR, "YCAP": YCAP, "m": M_LOOKS}
    ctrl = {"C2_chi2_six_seat_on_B1726": float(Cm.min_chi2(Cm.chi2_features("seat", False, Cm.B1726_CENSUS), Cm.arrays(Cm.B1726_CENSUS)["T6"][None, :])[0])}
    readout = {}
    for arm, ref in (("A0", 0.0346), ("A1", 0.315)):
        f = float(np.mean(D[arm]["im"] > 3)); se = math.sqrt(ref * (1 - ref) / NDRAW)
        readout["R_C4_height_" + arm] = {"P(Im tau > 3)": f, "B1813": ref, "z": (f - ref) / se}
    readout["capped"] = {arm: int(D[arm]["cap"].sum()) for arm in D}
    readout["draws with a numpy warning"] = {arm: D[arm]["warned"] for arm in D}
    readout["outside_[1,4]"] = {arm: float(np.mean((D[arm]["im"] < 1) | (D[arm]["im"] > 4))) for arm in D}
    # the decisive models, conditioned on resolved draws
    F = {}
    for arm in ("A0", "A1"):
        for mode in ("unforced", "hand"): F[(arm, mode)] = features(D[arm], cf, mode)
    a6, a9 = anarchy(); F[("N", "unforced")] = (np.maximum(a6, LF), np.maximum(a9, LF), (a6 > LF).all(1))
    REF = {k: Ref(v[0][v[2]], s6) for k, v in F.items()}
    res = {}
    for key, (X6, X9, ok) in F.items():
        ref = REF[key]; p_nn, p_F, dt, ft = ref.score(T6)
        q_nn, q_F, _, _ = Ref(X6, s6).score(T6)                       # unconditioned, a read-out
        k9 = ok & ~np.isnan(X9).any(1); n_nn, n_F, _, _ = Ref(X9[k9], s9).score(T9)
        idx = np.nonzero(ok)[0]
        res["%s|%s" % key] = {"resolved draws": int(ok.sum()),
                              "six": {"p_nn": float(p_nn[0]), "p_F": float(p_F[0]), "d_data": float(dt[0]), "phi_data": float(ft[0]),
                                      "resolution q95 of the draws' own nearest distance": ref.q95(),
                                      "marginal_p": marginals(X6[ok], T6), "nearest": nearest(X6[ok], T6, s6, D.get(key[0]), cf, idx),
                                      "unconditioned p_nn, p_F": [float(q_nn[0]), float(q_F[0])]},
                              "nine": {"p_nn": float(n_nn[0]), "p_F": float(n_F[0]), "draws": int(k9.sum())},
                              "three_deep (all m1/m3 < 1e-2)": float(np.mean(np.all(X6[:, [1, 3, 5]] < math.log(1e-2), axis=1))),
                              "six within a factor 10": float(np.mean(np.all(np.abs(X6 - T6) <= math.log(10), axis=1)))}
    A1u, A0u, A1h = res["A1|unforced"]["six"], res["A0|unforced"]["six"], res["A1|hand"]["six"]
    cells = {
        "D1_the_unforced_world_typical_under_the_geometric_clock": A1u["p_nn"] > 0.05,
        "D1h_by_hand_typical_under_the_geometric_clock": A1h["p_nn"] > 0.05,
        "D2_the_clock_depths_typical_under_A1_not_A0": A1u["p_F"] > 0.05 and A0u["p_F"] <= 0.05,
    }
    # specificity: B1741's random hierarchies scored by the same cells; D1h's null chooses its best configuration freely
    free = {}
    for rdg in READINGS:
        for c in (1, 3):
            X6, _, ok = features(D["A1"], cf, "fixed", rdg, c); free[(rdg, c)] = Ref(X6[ok], s6)
    spec = {"D1": [], "D1h": [], "D1h_free": [], "D2": [], "D2 A1 leg": [], "D2 A0 leg typical": []}
    for s in SEEDS:
        d6 = np.array(Cm.draws(s)[0]); assert (d6 > LF).all()
        a1u = REF[("A1", "unforced")].score(d6); a1h = REF[("A1", "hand")].score(d6); a0u = REF[("A0", "unforced")].score(d6)
        spec["D1"].append(float(np.mean(a1u[0] > 0.05))); spec["D1h"].append(float(np.mean(a1h[0] > 0.05)))
        spec["D2"].append(float(np.mean((a1u[1] > 0.05) & (a0u[1] <= 0.05))))
        spec["D2 A1 leg"].append(float(np.mean(a1u[1] > 0.05))); spec["D2 A0 leg typical"].append(float(np.mean(a0u[1] > 0.05)))
        best = np.max([r.score(d6[:NFREE])[0] for r in free.values()], axis=0); spec["D1h_free"].append(float(np.mean(best > 0.05)))
    r = {k: float(np.mean(v)) for k, v in spec.items()}
    grade = {"D1": r["D1"], "D1h (the free null, the grading)": r["D1h_free"], "D2": r["D2"]}
    grade = {k: (v, "PASSED-eligible" if v < 0.01 / M_LOOKS else "not specific (r >= 0.01/m)") for k, v in grade.items()}
    # read-outs: the horocycle by hand; the floors; held-out calibration; power
    horo = {}
    for h in HS:
        X6, _, ok = features(D["A1"], cf, "fixed", (1, 0, 0), 3, h); p = Ref(X6[ok], s6).score(T6)
        horo["A1 by hand, " + h] = {"p_nn": float(p[0][0]), "p_F": float(p[1][0]), "resolved": int(ok.sum())}
    floors = {}
    for fl in FLOORS_READOUT:
        for key in (("A1", "unforced"), ("A1", "hand"), ("A0", "unforced")):
            X6, _, ok = features(D[key[0]], cf, key[1], lf=math.log(fl)); ref = Ref(X6[ok], s6); p = ref.score(T6)
            d6 = np.array(Cm.draws(SEEDS[0])[0])[:NFREE]; pr = ref.score(d6)
            floors["%g|%s|%s" % ((fl,) + key)] = {"p_nn": float(p[0][0]), "p_F": float(p[1][0]), "resolved": int(ok.sum()),
                                                 "random hierarchies typical by p_nn, p_F (seed 1741, 1 000)": [float(np.mean(pr[0] > 0.05)), float(np.mean(pr[1] > 0.05))]}
    calib = {}
    for key in (("A0", "unforced"), ("A1", "unforced"), ("A1", "hand")):
        X6, _, ok = F[key]; Xr = X6[ok]; h = len(Xr) // 2; ref = Ref(Xr[:h], s6); p = ref.score(Xr[h:h + 500])
        calib["%s|%s" % key] = {"held-out at p_nn <= 0.05": float(np.mean(p[0] <= 0.05)), "at p_F <= 0.05": float(np.mean(p[1] <= 0.05))}
    power = {}
    for a, b in (("A1", "A0"), ("A0", "A1"), ("N", "A1"), ("N", "A0")):
        Xa = F[(a, "unforced")][0][F[(a, "unforced")][2]][:1000]; p = REF[(b, "unforced")].score(Xa)
        power["%s draws atypical under %s" % (a, b)] = {"p_nn <= 0.05": float(np.mean(p[0] <= 0.05)), "p_F <= 0.05": float(np.mean(p[1] <= 0.05))}
    cc = json.loads((HERE / "control.json").read_text(encoding="utf-8"))
    cells["C1_census_controls"] = (all(a == b for a, b in cc["C1a_trace_counts"].values()) and cc["C1a_move_count_14"][0] == cc["C1a_move_count_14"][1]
                                   and cc["C1b_reduction_max_rel_err"] < 1e-9 and cc["C1c_covariance_R_TS_max_log"] < 1e-9 and cc["C1c_least_Im_tau"] >= 0.31
                                   and cc["C1d_against_B1726_row"] < 1e-9 and cc["C1e_max_ratio_at_YCAP"] < FLOOR)
    cells["C2_control_chi2_reproduces_B1735"] = abs(ctrl["C2_chi2_six_seat_on_B1726"] - 3.0945633) < 1e-6
    out.update(cells=cells, results=res, specificity_r=r, specificity_per_seed=spec, grade_if_held=grade, horocycle_by_hand=horo,
               floors=floors, calibration=calib, power=power, readout=readout, control=ctrl, census_control=cc)
    (HERE / "comparison.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    for k, v in cells.items(): print(k, v)
    for k in res: print("%-14s six p_nn %.4f p_F %.4f d %.1f (q95 %.1f) | nine p_nn %.4f p_F %.4f" % (k, res[k]["six"]["p_nn"], res[k]["six"]["p_F"], res[k]["six"]["d_data"], res[k]["six"]["resolution q95 of the draws' own nearest distance"], res[k]["nine"]["p_nn"], res[k]["nine"]["p_F"]))
    print("specificity r:", r); print("power:", power); print("calibration:", calib)


if __name__ == "__main__":
    main()
