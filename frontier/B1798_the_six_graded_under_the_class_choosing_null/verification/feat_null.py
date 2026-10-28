"""R71-1 draft (adapted from B1786's referee prep.py / null_kd.py; the committed files are not modified).

Seat-menu chi2_six features built by B1741's own chi2_features('seat', False) on a census; per-LINE minima for the data and
for every KD-screened candidate target (B1741's expansion x2 - 2 X t + t2), so any class partition can be read afterwards.

    python3 -B feat_null.py prep  ARC                     -> feat_ARC.npz   (features, line ids, data per-line minima)
    python3 -B feat_null.py valid ARC                     -> the sealed seeds: direct min_chi2 count and the KD count
    python3 -B feat_null.py null  ARC LO HI --workers K    -> kd_ARC_LO_HI.npz (candidates' per-line minima)
ARC: b1749 (its census, all 266 lines, its compare.py loaded unchanged), b1753_48 (its census, its compare.py loaded
unchanged), b1753_all (its census + this draft's census_ext.jsonl: all 266 lines at its 223 apexes; B1749's loader with
the row count 59 318)."""
import sys, json, math, hashlib, pathlib, importlib.util
from fractions import Fraction as Fr
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
HERE = pathlib.Path(__file__).resolve().parent
FR = ROOT / "frontier"
V49 = FR / "B1749_the_six_at_fresh_apexes/verification"
V53 = FR / "B1753_the_six_on_the_five_ality_lines/verification"
EXT = HERE / "b1753_all266/census_ext.jsonl"
MARGIN = 0.5
SEALED = {"b1749": (list(range(1769, 1789)), 3.573708662392164, 16), "b1753_48": (list(range(1789, 1809)), 2.739034460748371, 7)}
_G = {}


def _load_module(name, path):
    if name not in sys.modules:
        sp = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(sp)
        sys.modules[name] = m; sp.loader.exec_module(m)
    return sys.modules[name]


def C_for(arc):
    """B1741's compare module, re-pointed exactly as the arc's own compare.py re-points it"""
    if arc == "b1749":
        M = _load_module("b1749_compare", V49 / "compare.py"); return M.C
    if arc == "b1753_48":
        M = _load_module("b1753_compare", V53 / "compare.py"); return M.C
    if arc in ("b1753_all", "b1753_part"):
        M = _load_module("b1749_compare", V49 / "compare.py"); C = M.C   # B1749's loader, re-pointed below
        def _load(path=None):
            assert hashlib.sha256(C.DATA.read_bytes()).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
            assert hashlib.sha256(C.CKMDATA.read_bytes()).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
            v = json.loads(C.DATA.read_text(encoding="utf-8"))["masses_GeV"]["value"]; K = json.loads(C.CKMDATA.read_text(encoding="utf-8"))["ckm_abs"]["value"]
            T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
            rows, seen, bad, dup = [], {}, 0, 0
            for p in (V53 / "census.jsonl", EXT, EXT.parent / "census_ext_tail.jsonl"):
                for l in p.read_text(encoding="utf-8").splitlines():
                    if not l.strip(): continue
                    try: r = json.loads(l)
                    except json.JSONDecodeError: bad += 1; continue        # a line cut by stopping a writer
                    key = (r["line"], r["Re_tau"], r["Im_tau"])
                    if key in seen:
                        q = seen[key]; dup += 1
                        assert all(q[k] == r[k] for k in r if k.startswith(("up|", "down|", "lep|", "ckm|"))), key
                        continue
                    seen[key] = r; rows.append(r)
            print("loader: %d rows, %d duplicates (checked equal), %d cut lines skipped" % (len(rows), dup, bad))
            assert len(rows) == len({(r["line"], r["Re_tau"], r["Im_tau"]) for r in rows})
            if arc == "b1753_all": assert len(rows) == 59318, len(rows)    # b1753_part: an interim lower bound only
            rows.sort(key=lambda r: (r["line"], r["Re_tau"], r["Im_tau"]))
            lg = lambda x: np.log(np.maximum(np.array(x, dtype=float), 1e-300))
            U, Dn, E, Kk, Jm, lab = [], [], [], [], [], []
            for r in rows:
                for h in ("L_max", "L_2"):
                    U.append([lg(r[f"up|{h}|{a}"]) for a in C.RD]); Dn.append([lg(r[f"down|{h}|{a}"]) for a in C.RD])
                    E.append([lg(r[f"lep|{h}|{a}"]) for a in C.RD])
                    Kk.append([[lg(r[f"ckm|{h}|{a}|{b}"][:3]) for b in C.RD] for a in C.RD]); Jm.append([[r[f"ckm|{h}|{a}|{b}"][3] for b in C.RD] for a in C.RD])
                    lab.append((r["line"], r["Re_tau"], r["Im_tau"], h))
            C._A.clear()
            C._A.update(U=np.array(U), Dn=np.array(Dn), E=np.array(E), K=np.array(Kk), J=np.array(Jm), lab=lab, T6=T6,
                        T9=np.concatenate([T6, np.log(np.array([K[0][1], K[1][2], K[0][2]]))]))
        C._load = _load
        return C
    raise SystemExit("unknown arc " + arc)


def line_table():
    K = _load_module("b1726_census", FR / "B1726_the_two_ingredients_replicated/verification/census.py")
    L = K.lines(); assert len(L) == 266
    alpha = [str(a) for a, b in L]; off = [str(b) for a, b in L]
    order = [math.lcm(Fr(a).denominator, Fr(b).denominator) for a, b in L]
    return alpha, off, order


def per_line_min(Xs, x2s, line_idx, nlines, T):
    """B1741's expansion; per target (columns) the minimum over each line's rows and the four seat configurations"""
    out = np.full((nlines, len(T)), np.inf)
    order = np.argsort(line_idx, kind="stable"); li = line_idx[order]
    starts = np.r_[0, np.flatnonzero(np.diff(li)) + 1]; present = li[starts]
    for s0 in range(0, len(T), 200):
        t = T[s0:s0 + 200]; t2 = (t ** 2).sum(1)
        acc = np.full((len(starts), len(t)), np.inf)
        for X, x2 in zip(Xs, x2s):
            c = x2[:, None] - 2 * X @ t.T + t2[None, :]
            acc = np.minimum(acc, np.minimum.reduceat(c[order], starts, axis=0))
        out[present, s0:s0 + 200] = acc
    return out


def prep(arc):
    C = C_for(arc); A = C.arrays(); F = C.chi2_features("seat", False); s6, _ = C.sigmas()
    for X, f in F: assert np.allclose(f(A["T6"][None, :]), A["T6"][None, :] / s6)
    Xs = np.stack([X for X, f in F]); lines = np.array([l[0] for l in A["lab"]])
    t = (A["T6"] / s6)[None, :]
    dmin = per_line_min(list(Xs), [(X ** 2).sum(1) for X in Xs], lines, 266, t)[:, 0]
    obs_sealed = float(C.min_chi2(F, A["T6"][None, :])[0])
    alpha, off, order = line_table()
    np.savez(HERE / ("feat_%s.npz" % arc), X=Xs, s6=s6, T6=A["T6"], line=lines, data_line_min=dmin, obs_minchi2=obs_sealed,
             alpha=np.array(alpha), off=np.array(off), order=np.array(order))
    print(arc, "rows", len(lines), "lines present", len(set(lines.tolist())), "data min (min_chi2) %.9f, per-line min %.9f" % (obs_sealed, np.nanmin(dmin)))


def _init(arc):
    if _G.get("arc") == arc: return
    from scipy.spatial import cKDTree
    f = np.load(HERE / ("feat_%s.npz" % arc)); X = f["X"]
    _G.clear(); _G.update(arc=arc, X=list(X), x2=[(x ** 2).sum(1) for x in X], line=f["line"], s6=f["s6"], tree=cKDTree(X.reshape(-1, 6)))
    _G["obs"] = float(SEALED["b1753_48"][1] if arc.startswith("b1753") else SEALED["b1749"][1])
    _G["C"] = _load_module("b1741_compare_plain", FR / "B1741_tau_from_the_thread_rule_the_line_free/verification/compare.py")


def run(job):
    arc, seed = job; _init(arc)
    d6, _ = _G["C"].draws(seed); T = np.array(d6); t = T / _G["s6"]
    dist, _i = _G["tree"].query(t, k=1, distance_upper_bound=float(np.sqrt(_G["obs"] + MARGIN)))
    cand = np.flatnonzero(np.isfinite(dist))
    plm = per_line_min(_G["X"], _G["x2"], _G["line"], 266, t[cand]) if len(cand) else np.zeros((266, 0))
    return seed, len(T), cand, plm, dist[cand] ** 2


def valid(arc):
    seeds, obs, want = SEALED["b1753_48" if arc.startswith("b1753") else arc]
    if arc == "b1753_all": raise SystemExit("validation is on the sealed census (b1753_48)")
    C = C_for(arc); A = C.arrays(); F = C.chi2_features("seat", False)
    obs_now = float(C.min_chi2(F, A["T6"][None, :])[0])
    Cp = _load_module("b1741_compare_plain", FR / "B1741_tau_from_the_thread_rule_the_line_free/verification/compare.py")
    direct = 0; kd = 0
    for s in seeds:
        d6, _ = Cp.draws(s); T = np.array(d6)
        direct += int((C.min_chi2(F, T) <= obs_now + 1e-9).sum())
        _s, n, cand, plm, _d = run((arc, s)); kd += int((plm.min(0) <= obs + 1e-9).sum())
    print("%s: data min %.9f (sealed %.9f); sealed seeds %d-%d: direct min_chi2 hits %d, KD+per-line hits %d, sealed %d" % (arc, obs_now, obs, seeds[0], seeds[-1], direct, kd, want))


if __name__ == "__main__":
    cmd, arc = sys.argv[1], sys.argv[2]
    if cmd == "prep": prep(arc)
    elif cmd == "valid": valid(arc)
    elif cmd == "null":
        from multiprocessing import Pool
        lo, hi = int(sys.argv[3]), int(sys.argv[4])
        nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
        with Pool(nw) as P:
            res = sorted(P.imap_unordered(run, [(arc, s) for s in range(lo, hi + 1)], chunksize=4))
        n = sum(r[1] for r in res)
        np.savez(HERE / ("kd_%s_%d_%d.npz" % (arc, lo, hi)), n=n, seeds=np.array([r[0] for r in res]),
                 cand_seed=np.concatenate([np.full(len(r[2]), r[0]) for r in res]), cand_idx=np.concatenate([r[2] for r in res]),
                 plm=np.concatenate([r[3] for r in res], axis=1), kd_chi2=np.concatenate([r[4] for r in res]))
        print(arc, "targets", n, "candidates", sum(len(r[2]) for r in res)); print("null exit 0")
