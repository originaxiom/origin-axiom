"""B1839 look: THE END CARD's one look, sealed in ../PREREGISTRATION.md before it runs.

Builds, data-free, the six's frame ratios at the 59 318 (apex, line) pairs x 23 ends (the 22 levels of census.py's norms.npz
and the cusp limit), every sector in S and S~, through the web seat's instrument's ratios() with the Higgs DR at each
reduced apex. Then, with B1741's compare.py loaded unchanged (sha256 asserted): C0, C3, P1, D and the read-outs, once.
The measure is the referee's c-choosing chi2 of B1798 (cnull.py), the same arithmetic: four quark logs over sigma, the
lepton pair with +-k, k = ln c, c continuous in [1/3, 5] (decisive), the nine scanned values, or {1, 3}; minimum over the
rows and B1741's two SEAT triples. The null: B1741's draws() on fresh seeds, a KD screen on the free-c lower bound and the
exact chi2 on every row inside the screen's ball (which holds every row that can reach the data's minimum).
    python3 -B look.py --workers 8      -> look.json, look_run.txt ("look exit 0")
Importing computes nothing."""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys, json, math, gzip, hashlib, time, pathlib, importlib.util
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
CMP = ROOT / "frontier" / "B1741_tau_from_the_thread_rule_the_line_free" / "verification" / "compare.py"
CMP_SHA = "6308ed93e53ab99522cf654a85250f1299e9fa334ce13f92a74334cd7812f3bd"
R71 = ROOT / "frontier" / "B1798_the_six_graded_under_the_class_choosing_null" / "verification"
SEEDS_D = (31001, 31250)
SEEDS_R = (31001, 31050)
SEEDS_C3 = (5001, 5010)
KLO, KHI = math.log(1 / 3), math.log(5.0)
SET9 = tuple(math.log(float(Fr(x))) for x in ("1/3", "1/2", "2/3", "1", "3/2", "2", "3", "4", "5"))
SEATK = (0.0, math.log(3))
MODES = ("bounded", "set9", "seat")
# the web seat's sealed E2 (relays/chat1_2026-10-28_exact_end/exact_end_look.json at 4aa66ca45, sha256 7f1502d9...):
# row -> (tau, b on the line (2/5, b), E2 = chi2_six at the exact norms at L_max, the seat menu)
E2 = {"A": (complex(0.23536090850830077, 3.0233101844787598), Fr(23, 30), 30.66437209071375),
      "B": (complex(0.3153997421264647, 3.0348918914794902), Fr(1, 10), 39.148931481419496),
      "C": (complex(0.409680215176195, 3.0652901595458397), Fr(23, 25), 53.700282165605884),
      "D": (complex(0.303170394897461, 3.055126190185547), Fr(11, 25), 40.83065599893084)}
C3_REF = R71 / "referee" / "cnull_b1753_all_5001_5010_c0.333_5.json"
_G = {}


def CEN():
    if "cen" not in _G:
        sp = importlib.util.spec_from_file_location("b1839_census", HERE / "census.py")
        m = importlib.util.module_from_spec(sp); sys.modules["b1839_census"] = m; sp.loader.exec_module(m); _G["cen"] = m
    return _G["cen"]


def CMPM():
    if "cmp" not in _G:
        assert hashlib.sha256(CMP.read_bytes()).hexdigest() == CMP_SHA
        sp = importlib.util.spec_from_file_location("b1839_compare", CMP)
        m = importlib.util.module_from_spec(sp); sys.modules["b1839_compare"] = m; sp.loader.exec_module(m); _G["cmp"] = m
    return _G["cmp"]


def _norms():
    if "norms" not in _G:
        _G["norms"] = np.load(HERE / "norms.npz")["norms"]; _G["acc"] = CEN().load_acc()
    return _G["norms"], _G["acc"]


def sector_ratios(ee, rd, R, Nv):
    """the instrument's ratios() with the instrument's zeroing of a channel whose residue vanishes"""
    N = {s: (float(Nv[q]) if abs(R[s]) > 1e-12 else 0.0) for q, s in enumerate(("1", "i", "j", "k"))}
    r = ee.ratios(rd, R, N)
    return r["S"], r["St"]


def apex_features(i):
    """(266 lines, 23 ends, 2 readings S/S~, 2 ratios m2/m3, m1/m3) per sector, at apex i; data-free"""
    cen = CEN(); M = cen.mods(); ee = M["ee"]
    arr, acc = _norms(); r = acc[i]; tau = complex(*r["tau"]); n = r["n"]; rd = ee.higgs(tau)
    keys, idx, reps = cen.classes(); nd = len(cen.DELTAS) + 1
    out = {s: np.zeros((len(M["LINES"]), nd, 2, 2)) for s in ("up", "down", "lep")}
    for k, line in enumerate(M["LINES"]):
        ln = cen.red_line(line, n)
        for sec in ("up", "down", "lep"):
            x, yy, R = cen.twists(tau, ln, sec)
            for j in range(nd):
                Nv = arr[i, idx[k], j] if j < nd - 1 else np.ones(4)
                S, St = sector_ratios(ee, rd, R, Nv)
                out[sec][k, j, 0] = S; out[sec][k, j, 1] = St
    lg = lambda x: np.log(np.maximum(x, 1e-300))
    return i, lg(out["up"]), lg(out["down"]), lg(out["lep"])


class Measure:
    """the referee's chi2 (B1798 cnull.py), same arithmetic, over an arbitrary row set"""
    def __init__(self, U, Dn, E, s6):
        self.s6 = s6; self.s45 = math.sqrt(s6[4] ** 2 + s6[5] ** 2); self.blocks = []
        C = CMPM()
        for (a, b, l) in C.SEAT:
            Q = np.concatenate([U[:, a] / s6[0:2], Dn[:, b] / s6[2:4]], axis=1)
            self.blocks.append((Q, E[:, l, 0], E[:, l, 1]))
        self.m = len(U)

    def chi2(self, T, mode, rows=None):
        """T (t x 6) -> (t,) min, and per target (block, row, k) of the minimum; rows: optional index array per block"""
        s6 = self.s6; tq = T[:, 0:4] / s6[0:4]
        best = np.full(len(T), np.inf); arg = [(None, None, None)] * len(T)
        for bi, (Q, ea, eb) in enumerate(self.blocks):
            if rows is not None:
                ri = rows[bi]
                if len(ri) == 0: continue
                Q, ea, eb = Q[ri], ea[ri], eb[ri]
            else:
                ri = None
            qq = (Q ** 2).sum(1)[:, None] - 2 * Q @ tq.T + (tq ** 2).sum(1)[None, :]
            u0 = ea[:, None] - T[None, :, 4]; v0 = eb[:, None] - T[None, :, 5]
            if mode == "bounded":
                k = np.clip((s6[4] ** 2 * v0 - s6[5] ** 2 * u0) / (s6[4] ** 2 + s6[5] ** 2), KLO, KHI)
                lep = (u0 + k) ** 2 / s6[4] ** 2 + (v0 - k) ** 2 / s6[5] ** 2; kk = k
            else:
                ks = SET9 if mode == "set9" else SEATK
                L = np.array([(u0 + q) ** 2 / s6[4] ** 2 + (v0 - q) ** 2 / s6[5] ** 2 for q in ks])
                ia = L.argmin(0); lep = np.take_along_axis(L, ia[None], 0)[0]; kk = np.array(ks)[ia]
            tot = qq + lep; j = tot.argmin(0); v = tot[j, np.arange(len(T))]
            for t in np.flatnonzero(v < best):
                arg[t] = (bi, int(j[t] if ri is None else ri[j[t]]), float(kk[j[t], t]))
            best = np.minimum(best, v)
        return best, arg

    def free_points(self):
        return np.concatenate([np.concatenate([Q, ((ea + eb) / self.s45)[:, None]], axis=1) for Q, ea, eb in self.blocks], axis=0)

    def free_targets(self, T):
        return np.concatenate([T[:, 0:4] / self.s6[0:4], ((T[:, 4] + T[:, 5]) / self.s45)[:, None]], axis=1)


def null(meas, obs, seeds, log, tag, rows_label=None, max_pairs=12_000_000):
    """hits per mode: random hierarchies whose minimum over the same rows and menu is <= the data's (B1741's draws).
    Screen: the free-c lower bound (the referee's) on a KD tree; every row inside the ball of radius sqrt(max obs) is
    evaluated exactly (the referee's arithmetic, per (target, row) pair), so a target is a hit iff some row reaches obs."""
    from scipy.spatial import cKDTree
    from scipy.stats import beta
    C = CMPM(); t0 = time.time(); s6 = meas.s6
    Qa = np.stack([b[0] for b in meas.blocks]); Ea = np.stack([b[1] for b in meas.blocks]); Eb = np.stack([b[2] for b in meas.blocks])
    tree = cKDTree(meas.free_points()); rad = math.sqrt(max(obs.values()) + 1e-9) + 1e-9
    n = 0; hits = {m: 0 for m in MODES}; cands = 0; pairs_tot = 0; hit_rows = []

    def evaluate(T, owners, flat):
        blk = flat // meas.m; row = flat % meas.m
        Qp = Qa[blk, row]; tq = T[owners, 0:4] / s6[0:4]
        qq = (Qp ** 2).sum(1) - 2 * (Qp * tq).sum(1) + (tq ** 2).sum(1)
        u0 = Ea[blk, row] - T[owners, 4]; v0 = Eb[blk, row] - T[owners, 5]
        out = {}
        for m in MODES:
            if m == "bounded":
                k = np.clip((s6[4] ** 2 * v0 - s6[5] ** 2 * u0) / (s6[4] ** 2 + s6[5] ** 2), KLO, KHI)
                lep = (u0 + k) ** 2 / s6[4] ** 2 + (v0 - k) ** 2 / s6[5] ** 2
            else:
                ks = SET9 if m == "set9" else SEATK
                lep = np.min([(u0 + q) ** 2 / s6[4] ** 2 + (v0 - q) ** 2 / s6[5] ** 2 for q in ks], axis=0)
            out[m] = qq + lep
        return out, row
    for s in range(seeds[0], seeds[1] + 1):
        d6, _ = C.draws(s); T = np.array(d6); n += len(T)
        tf = meas.free_targets(T)
        dist, _i = tree.query(tf, k=1, distance_upper_bound=rad)
        cand = np.flatnonzero(np.isfinite(dist)); cands += len(cand)
        if not len(cand): continue
        cnt = tree.query_ball_point(tf[cand], rad, return_length=True)
        st = 0
        while st < len(cand):
            en = st; acc = 0
            while en < len(cand) and (acc == 0 or acc + cnt[en] <= max_pairs):
                acc += cnt[en]; en += 1
            cb = cand[st:en]; balls = tree.query_ball_point(tf[cb], rad)
            sizes = np.array([len(L) for L in balls]); flat = np.concatenate([np.asarray(L, dtype=np.int64) for L in balls])
            owners = np.repeat(cb, sizes); pairs_tot += len(flat)
            vals, row = evaluate(T, owners, flat)
            starts = np.concatenate([[0], np.cumsum(sizes)[:-1]])
            for m in MODES:
                mn = np.minimum.reduceat(vals[m], starts); h = mn <= obs[m] + 1e-9; hits[m] += int(h.sum())
                if m == "bounded" and rows_label is not None and h.any():
                    for g in np.flatnonzero(h):
                        seg = vals[m][starts[g]:starts[g] + sizes[g]]; hit_rows.append(int(row[starts[g] + int(seg.argmin())]))
            st = en
    out = {"n": n, "candidates": cands, "pairs": int(pairs_tot), "seconds": time.time() - t0}
    for m in MODES:
        h = hits[m]; r = float(beta.ppf(0.975, h + 1, n - h))
        out[m] = {"obs": obs[m], "hits": h, "frac": h / n, "r97.5": r}
        log("  %s [%s] c %-7s obs %.6f  targets %d  hits %d  frac %.4e  r97.5 %.4e" % (tag, "%d-%d" % seeds, m, obs[m], n, h, h / n, r))
    log("  %s: %d candidates, %d (target, row) pairs evaluated, %.0f s" % (tag, cands, pairs_tot, time.time() - t0))
    if rows_label is not None:
        out["hit_delta_index"] = [int(rows_label[q]) for q in hit_rows]
    return out


def small_cut_census():
    """B1798's committed small-cut census (B1753's 48 lines + the two extension files), deduplicated by (apex, line) with
    equality, as the referee's direct_null.my_rows(); arrays as its build(): rows (apex, line, horocycle)"""
    ps = [ROOT / "frontier" / "B1753_the_six_on_the_five_ality_lines" / "verification" / "census.jsonl",
          R71 / "b1753_all266" / "census_ext.jsonl.gz", R71 / "b1753_all266" / "census_ext_tail.jsonl.gz"]
    seen = {}
    for p in ps:
        txt = gzip.open(p, "rt", encoding="utf-8").read() if p.suffix == ".gz" else p.read_text(encoding="utf-8")
        for l in txt.split("\n"):
            if not l.strip(): continue
            r = json.loads(l); k = (r["apex"], r["line"])
            if k in seen: assert seen[k] == r; continue
            seen[k] = r
    C = CMPM(); lg = lambda x: np.log(np.maximum(np.array(x, dtype=float), 1e-300))
    U, Dn, E = [], [], []
    for r in sorted(seen.values(), key=lambda r: (r["apex"], r["line"])):
        for h in ("L_max", "L_2"):
            U.append([lg(r[f"up|{h}|{a}"]) for a in C.RD]); Dn.append([lg(r[f"down|{h}|{a}"]) for a in C.RD])
            E.append([lg(r[f"lep|{h}|{a}"]) for a in C.RD])
    return np.array(U), np.array(Dn), np.array(E), len(seen)


def c0(log, T6, s6):
    """the web seat's E2 through this card's path: B1667's accessory and geometry at each row's tau, the split quadrature
    at L_max with the down sector's twists (the class cache's route), every sector's ratios with its own residues"""
    cen = CEN(); M = cen.mods(); ee, C = M["ee"], M["C"]; Cm = CMPM()
    c = C.track(ee.CONTROL); c, _ = C.solve_accessory(ee.CONTROL, c); tp = ee.CONTROL; dev = 0.0; rows = {}
    for name, (tau, b, ref) in E2.items():
        c, _ = C.newton_walk(tp, c, tau); tp = tau; G = ee.geometry(tau, c); rd = ee.higgs(tau)
        line = (Fr(2, 5), b); x, yy, R = cen.twists(tau, line, "down")
        nodes, _ = cen.cell_nodes(tau, G["al"], G["be"], G["L_max"]); N = cen.kernel_norms(nodes, x, yy, R, tau)
        Nv = [N[s] for s in ("1", "i", "j", "k")]
        lgr = []
        for sec in ("up", "down", "lep"):
            xs, ys, Rs = cen.twists(tau, line, sec); S, St = sector_ratios(ee, rd, Rs, Nv); lgr.append([S, St])
        lgr = np.log(np.array(lgr, dtype=float)); best = np.inf
        for (a, bb, l) in Cm.SEAT:
            for k in SEATK:
                xv = np.array([lgr[0, a][0], lgr[0, a][1], lgr[1, bb][0], lgr[1, bb][1], lgr[2, l][0] + k, lgr[2, l][1] - k])
                best = min(best, float(np.sum(((xv - T6) / s6) ** 2)))
        rows[name] = best; dev = max(dev, abs(best / ref - 1))
    ok = dev < 1e-6
    log("C0 (the web seat's E2 through this path): %s; max rel dev %.1e -> %s" % ({k: round(v, 6) for k, v in rows.items()}, dev, "HOLDS" if ok else "FAILS"))
    return {"holds": ok, "rows": rows, "max_rel_dev": dev}


def main():
    from multiprocessing import get_context
    t0 = time.time(); outl = []

    def log(s):
        print(s, flush=True); outl.append(s)
    w = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 8
    cen = CEN(); M = cen.mods(); nd = len(cen.DELTAS) + 1; nl = len(M["LINES"]); na = len(M["AP"])
    idx = json.loads((HERE / "norms_index.json").read_text(encoding="utf-8"))
    arr = np.load(HERE / "norms.npz")["norms"]
    assert hashlib.sha256(np.ascontiguousarray(arr).tobytes()).hexdigest() == idx["norms_sha256"]
    log("norms.npz: shape %s, sha256 of the array bytes %s (as census_run.txt)" % (arr.shape, idx["norms_sha256"]))
    # 1. the frame's ratios (data-free)
    U = np.zeros((na, nl, nd, 2, 2)); Dn = np.zeros_like(U); E = np.zeros_like(U)
    with get_context("spawn").Pool(w) as P:
        for k, (i, u, d, e) in enumerate(P.imap_unordered(apex_features, range(na), chunksize=1)):
            U[i], Dn[i], E[i] = u, d, e
            if (k + 1) % 25 == 0: log("  features: %d / %d apexes (%.0f s)" % (k + 1, na, time.time() - t0))
    lab_a, lab_l, lab_d = np.meshgrid(np.arange(na), np.arange(nl), np.arange(nd), indexing="ij")
    lab_a, lab_l, lab_d = lab_a.ravel(), lab_l.ravel(), lab_d.ravel()
    U, Dn, E = U.reshape(-1, 2, 2), Dn.reshape(-1, 2, 2), E.reshape(-1, 2, 2)
    fin = bool(np.all(np.isfinite(U)) and np.all(np.isfinite(Dn)) and np.all(np.isfinite(E)))
    fsha = hashlib.sha256(np.ascontiguousarray(np.stack([U, Dn, E])).tobytes()).hexdigest()
    log("features: %d rows (%d apexes x %d lines x %d ends); all finite %s; sha256 %s" % (len(U), na, nl, nd, fin, fsha))
    # 2. the data and the measure
    C = CMPM()
    v = json.loads(C.DATA.read_text(encoding="utf-8"))["masses_GeV"]["value"]
    T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
    s6, _ = C.sigmas()
    res = {"features_sha256": fsha, "rows": int(len(U))}
    res["C0"] = c0(log, T6, s6)
    # 3. C3: the null code on B1798's small-cut census
    Us, Ds, Es, npairs = small_cut_census(); ms = Measure(Us, Ds, Es, s6)
    ob = {m: float(ms.chi2(T6[None, :], m)[0][0]) for m in MODES}
    ref = json.loads(C3_REF.read_text(encoding="utf-8"))
    log("C3: B1798's small-cut census, %d pairs, %d rows; data obs bounded %.9f (ref %.9f), seat %.9f (ref %.9f)" % (
        npairs, len(Us), ob["bounded"], ref["obs_bounded"], ob["seat"], ref["obs_seat"]))
    n3 = null(ms, ob, SEEDS_C3, log, "C3")
    c3 = (abs(ob["bounded"] - ref["obs_bounded"]) < 1e-9 and abs(ob["seat"] - ref["obs_seat"]) < 1e-9
          and n3["bounded"]["hits"] == ref["hits_bounded"] and n3["seat"]["hits"] == ref["hits_seat"] and n3["n"] == ref["n"])
    log("C3 (the referee's hits reproduced: bounded %d vs %d, seat %d vs %d) -> %s" % (
        n3["bounded"]["hits"], ref["hits_bounded"], n3["seat"]["hits"], ref["hits_seat"], "HOLDS" if c3 else "FAILS"))
    res["C3"] = {"holds": c3, "obs": ob, "null": n3}
    del ms, Us, Ds, Es
    # 4. the look: P1 and D
    meas = Measure(U, Dn, E, s6)
    obs = {}; best = {}
    for m in MODES:
        vv, aa = meas.chi2(T6[None, :], m); obs[m] = float(vv[0]); best[m] = aa[0]
    p1 = obs["bounded"] < 16.75
    log("P1: the data's minimum chi2_six, c continuous %.6f (nine values %.6f, {1,3} %.6f) -> %s" % (
        obs["bounded"], obs["set9"], obs["seat"], "HOLDS" if p1 else "FAILS"))
    nD = null(meas, obs, SEEDS_D, log, "D", rows_label=lab_d)
    dd = nD["bounded"]["r97.5"] < 0.01
    log("D (THE DECISIVE CELL): r97.5 %.4e (c continuous) -> %s" % (nD["bounded"]["r97.5"], "HOLDS" if dd else "FAILS"))
    res.update(P1={"holds": p1, "obs": obs}, D={"holds": dd, "null": {k: v for k, v in nD.items() if k != "hit_delta_index"}})
    # 5. read-outs
    deltas = list(cen.DELTAS) + ["inf"]
    hist = np.bincount(np.array(nD["hit_delta_index"], dtype=int), minlength=nd).tolist() if nD["hit_delta_index"] else [0] * nd
    log("read-out 6, delta among D's hits: %s" % {str(d): h for d, h in zip(deltas, hist)})
    res["readout_hit_delta"] = dict(zip(map(str, deltas), hist))
    ro = {}
    five = set(M["B53"].five_lines())
    for name, sel in (("delta_0_alone", np.flatnonzero(lab_d == 0)), ("delta_inf_alone", np.flatnonzero(lab_d == nd - 1)),
                      ("five_ality_lines_alone", np.flatnonzero(np.isin(lab_l, sorted(five))))):
        mr = Measure(U[sel], Dn[sel], E[sel], s6); o = {m: float(mr.chi2(T6[None, :], m)[0][0]) for m in MODES}
        log("read-out %s: %d rows; data obs %s" % (name, len(sel), {m: round(x, 6) for m, x in o.items()}))
        ro[name] = {"rows": int(len(sel)), "obs": o, "null": null(mr, o, SEEDS_R, log, name)}
        del mr
    res["readouts"] = ro
    prof = []
    for j in range(nd):
        sel = np.flatnonzero(lab_d == j); mr = Measure(U[sel], Dn[sel], E[sel], s6); vv, aa = mr.chi2(T6[None, :], "bounded")
        bi, rw, kk = aa[0]; g = sel[rw]
        prof.append({"delta": str(deltas[j]), "min_chi2": float(vv[0]), "apex": int(lab_a[g]), "line": int(lab_l[g]), "seat": bi, "c": math.exp(kk)})
        del mr
    log("read-out 5, the data's minimum per end (c continuous): %s" % [(p["delta"], round(p["min_chi2"], 3)) for p in prof])
    res["readout_profile"] = prof
    acc = CEN().load_acc(); tops = []
    for m in MODES:
        bi, rw, kk = best[m]; a = int(lab_a[rw]); l = int(lab_l[rw]); j = int(lab_d[rw]); ln = M["LINES"][l]
        sa, sb, sl = C.SEAT[bi]
        x = np.array([U[rw, sa, 0], U[rw, sa, 1], Dn[rw, sb, 0], Dn[rw, sb, 1], E[rw, sl, 0] + kk, E[rw, sl, 1] - kk])
        tops.append({"mode": m, "chi2": obs[m], "apex": a, "tau0": acc[a]["tau0"], "line": [str(ln[0]), str(ln[1])], "delta": str(deltas[j]),
                     "seat": [sa, sb, sl], "c": math.exp(kk), "model_over_measured": np.exp(x - T6).tolist()})
        log("read-out 5/7, best row (%s): chi2 %.4f at apex %d tau0 %s line (%s, %s) delta %s seat %s c %.4f; model/measured %s" % (
            m, obs[m], a, acc[a]["tau0"], ln[0], ln[1], deltas[j], (sa, sb, sl), math.exp(kk), ["%.3f" % q for q in np.exp(x - T6)]))
    res["readout_best_rows"] = tops
    cc = json.loads((HERE / "census_controls.json").read_text(encoding="utf-8"))
    log("read-out 8 (C1's per-sector maximum, census): %s" % cc["C1"]["per_sector_max_rel"])
    res["cells"] = {"C0": res["C0"]["holds"], "C1": cc["C1"]["holds"], "C2": cc["C2"]["holds"], "C3": c3, "P1": p1, "D": dd}
    log("cells: " + " | ".join("%s %s" % (k, "HOLDS" if v else "FAILS") for k, v in res["cells"].items()))
    (HERE / "look.json").write_text(json.dumps(res, indent=1, default=str), encoding="utf-8")
    log("look exit 0 (%.0f s)" % (time.time() - t0))
    (HERE / "look_run.txt").write_text("\n".join(outl) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
