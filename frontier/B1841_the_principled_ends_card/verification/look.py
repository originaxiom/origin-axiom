"""B1841 look: THE PRINCIPLED-ENDS CARD's one look, sealed in ../PREREGISTRATION.md before it runs.

Builds, data-free, the six's frame ratios at the 59 318 (apex, line) pairs x B1840's four ends from census.py's norms.npz,
through B1839's sealed look.py imported unchanged (its sector_ratios, Measure, null, small_cut_census, CMPM); then C3, P1,
D and the read-outs, once. Fresh seeds 51001-51250.
    python3 -B look.py --workers 8      -> look.json, look_run.txt ("look exit 0")
Importing computes nothing."""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys, json, math, hashlib, time, pathlib, importlib.util
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
B1839V = ROOT / "frontier" / "B1839_the_end_card" / "verification"
SEEDS_D = (51001, 51250)
SEEDS_R = (51001, 51050)
SEEDS_C3 = (5001, 5010)
_G = {}


def L39():
    if "l39" not in _G:
        sp = importlib.util.spec_from_file_location("b1839_look", B1839V / "look.py")
        m = importlib.util.module_from_spec(sp); sys.modules["b1839_look"] = m; sp.loader.exec_module(m); _G["l39"] = m
    return _G["l39"]


def C41():
    if "c41" not in _G:
        sp = importlib.util.spec_from_file_location("b1841_census", HERE / "census.py")
        m = importlib.util.module_from_spec(sp); sys.modules["b1841_census"] = m; sp.loader.exec_module(m); _G["c41"] = m
    return _G["c41"]


def _norms():
    if "norms" not in _G:
        _G["norms"] = np.load(HERE / "norms.npz")["norms"]; _G["acc"] = C41().C39().load_acc()
    return _G["norms"], _G["acc"]


def apex_features(i):
    """(266 lines, 4 ends, 2 readings, 2 ratios) per sector at apex i; data-free"""
    L = L39(); c39 = C41().C39(); M = c39.mods(); ee = M["ee"]
    arr, acc = _norms(); r = acc[i]; tau = complex(*r["tau"]); n = r["n"]; rd = ee.higgs(tau)
    keys, idx, reps = c39.classes(); ne = arr.shape[2]
    out = {s: np.zeros((len(M["LINES"]), ne, 2, 2)) for s in ("up", "down", "lep")}
    for k, line in enumerate(M["LINES"]):
        ln = c39.red_line(line, n)
        for sec in ("up", "down", "lep"):
            x, yy, R = c39.twists(tau, ln, sec)
            for j in range(ne):
                S, St = L.sector_ratios(ee, rd, R, arr[i, idx[k], j]); out[sec][k, j, 0] = S; out[sec][k, j, 1] = St
    lg = lambda x: np.log(np.maximum(x, 1e-300))
    return i, lg(out["up"]), lg(out["down"]), lg(out["lep"])


def main():
    from multiprocessing import get_context
    t0 = time.time(); outl = []

    def log(s):
        print(s, flush=True); outl.append(s)
    w = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 8
    L = L39(); c41 = C41(); M = c41.C39().mods(); nl = len(M["LINES"]); na = len(M["AP"])
    idx = json.loads((HERE / "norms_index.json").read_text(encoding="utf-8")); arr = np.load(HERE / "norms.npz")["norms"]
    assert hashlib.sha256(np.ascontiguousarray(arr).tobytes()).hexdigest() == idx["norms_sha256"]; ne = arr.shape[2]
    log("norms.npz: shape %s, sha256 %s" % (arr.shape, idx["norms_sha256"]))
    U = np.zeros((na, nl, ne, 2, 2)); Dn = np.zeros_like(U); E = np.zeros_like(U)
    with get_context("spawn").Pool(w) as P:
        for i, u, d, e in P.imap_unordered(apex_features, range(na), chunksize=1):
            U[i], Dn[i], E[i] = u, d, e
    lab_a, lab_l, lab_e = [x.ravel() for x in np.meshgrid(np.arange(na), np.arange(nl), np.arange(ne), indexing="ij")]
    U, Dn, E = U.reshape(-1, 2, 2), Dn.reshape(-1, 2, 2), E.reshape(-1, 2, 2)
    fin = bool(np.all(np.isfinite(U)) and np.all(np.isfinite(Dn)) and np.all(np.isfinite(E)))
    log("features: %d rows (%d apexes x %d lines x %d ends); all finite %s (%.0f s)" % (len(U), na, nl, ne, fin, time.time() - t0))
    C = L.CMPM()
    v = json.loads(C.DATA.read_text(encoding="utf-8"))["masses_GeV"]["value"]
    T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
    s6, _ = C.sigmas(); res = {"rows": int(len(U)), "all_finite": fin}
    Us, Ds, Es, npairs = L.small_cut_census(); ms = L.Measure(Us, Ds, Es, s6)
    ob = {m: float(ms.chi2(T6[None, :], m)[0][0]) for m in L.MODES}
    ref = json.loads(L.C3_REF.read_text(encoding="utf-8")); n3 = L.null(ms, ob, SEEDS_C3, log, "C3")
    c3 = (abs(ob["bounded"] - ref["obs_bounded"]) < 1e-9 and abs(ob["seat"] - ref["obs_seat"]) < 1e-9 and n3["bounded"]["hits"] == ref["hits_bounded"]
          and n3["seat"]["hits"] == ref["hits_seat"] and n3["n"] == ref["n"])
    log("C3 -> %s" % ("HOLDS" if c3 else "FAILS")); del ms, Us, Ds, Es
    meas = L.Measure(U, Dn, E, s6); obs = {}; best = {}
    for m in L.MODES:
        vv, aa = meas.chi2(T6[None, :], m); obs[m] = float(vv[0]); best[m] = aa[0]
    finite_obs = all(math.isfinite(x) for x in obs.values())
    p1 = obs["bounded"] < 16.75
    log("P1: minimum chi2_six, c continuous %.6f (nine %.6f, {1,3} %.6f); minima finite %s -> %s" % (obs["bounded"], obs["set9"], obs["seat"], finite_obs, "HOLDS" if p1 else "FAILS"))
    nD = L.null(meas, obs, SEEDS_D, log, "D", rows_label=lab_e); dd = nD["bounded"]["r97.5"] < 0.01
    log("D (THE DECISIVE CELL): r97.5 %.4e -> %s" % (nD["bounded"]["r97.5"], "HOLDS" if dd else "FAILS"))
    hist = np.bincount(np.array(nD.get("hit_delta_index", []), dtype=int), minlength=ne).tolist()
    res.update(C3={"holds": c3, "obs": ob}, P1={"holds": p1, "obs": obs, "finite": finite_obs},
               D={"holds": dd, "null": {k: v for k, v in nD.items() if k != "hit_delta_index"}, "hit_entry_histogram": hist})
    ENT = list(c41.ENTRIES); per = {}
    for j in range(ne):
        sel = np.flatnonzero(lab_e == j); mr = L.Measure(U[sel], Dn[sel], E[sel], s6)
        o = {m: float(mr.chi2(T6[None, :], m)[0][0]) for m in L.MODES}
        log("read-out 1, %s alone: data obs %s" % (ENT[j], {m: round(x, 6) for m, x in o.items()}))
        per[ENT[j]] = {"obs": o, "null": L.null(mr, o, SEEDS_R, log, ENT[j])}; del mr
    res["readout_per_entry"] = per
    acc = c41.C39().load_acc(); tops = []
    for m in L.MODES:
        bi, rw, kk = best[m]; a = int(lab_a[rw]); l = int(lab_l[rw]); j = int(lab_e[rw]); ln = M["LINES"][l]; sa, sb, sl = C.SEAT[bi]
        x = np.array([U[rw, sa, 0], U[rw, sa, 1], Dn[rw, sb, 0], Dn[rw, sb, 1], E[rw, sl, 0] + kk, E[rw, sl, 1] - kk])
        tops.append({"mode": m, "chi2": obs[m], "entry": ENT[j], "apex": a, "tau0": acc[a]["tau0"], "line": [str(ln[0]), str(ln[1])], "seat": [sa, sb, sl],
                     "c": math.exp(kk), "model_over_measured": np.exp(x - T6).tolist()})
        log("read-out 2/3, best row (%s): chi2 %.4f, %s, apex %d tau0 %s line (%s, %s) seat %s c %.4f; model/measured %s" % (
            m, obs[m], ENT[j], a, acc[a]["tau0"], ln[0], ln[1], (sa, sb, sl), math.exp(kk), ["%.3f" % q for q in np.exp(x - T6)]))
    res["readout_best_rows"] = tops
    cc = json.loads((HERE / "census_controls.json").read_text(encoding="utf-8"))
    void = not (fin and finite_obs)
    res["cells"] = {"C1": cc["C1"]["holds"], "C2": cc["C2"]["holds"], "C3": c3, "P1": p1, "D": dd, "VOID": void}
    log("cells: " + " | ".join("%s %s" % (k, ("HOLDS" if v else "FAILS") if k != "VOID" else ("VOID" if v else "not void")) for k, v in res["cells"].items()))
    (HERE / "look.json").write_text(json.dumps(res, indent=1, default=str), encoding="utf-8")
    log("look exit 0 (%.0f s)" % (time.time() - t0))
    (HERE / "look_run.txt").write_text("\n".join(outl) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
