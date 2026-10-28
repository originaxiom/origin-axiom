"""THE HOROCYCLE AND THE HEIGHT: the script of the sealed rule HOROCYCLE_RULE.md (this directory; sealed and pushed before
this script was committed).  Two stages, each resumable:
    python3 -B horocycle.py --census [--workers 2] [--max-seconds 6600]
        the census: the grid G (40 lines x 130 points, both horocycles; the six's ratios and the CKM moduli), then the
        absorption searches at the 480 base points B, control (b) and controls (a), (c).  Chunks in chunks_horocycle/
        (git-ignored); when every task is done they are combined into horocycle_census.npz and horocycle_census.json.
        Prints progress counts only.
    python3 -B horocycle.py --cells [--workers 2] [--max-seconds 6600]
        C0 (a'), (a''), (d) and the stop rule; the data-free cells H1-H3; then the chi2 stage (H4's Nelder-Mead
        refinements, checkpointed in chunks_horocycle/; H5; the read-outs).  When every refinement is done it writes
        horocycle_cells.json and prints the cells (redirect to horocycle_cells_run.txt); a part stopped by its time limit
        prints progress counts only.
The frame: B1726's sealed compute() (B1656's frame at B1667's end), extracted from main at REV with B1786's pins; the
chi2: B1741's compare.py, loaded unchanged."""
import contextlib, hashlib, importlib.util, io, json, math, os, subprocess, sys, tempfile, time, pathlib, gzip
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
CH = HERE / "chunks_horocycle"
OUT_CENSUS, OUT_INDEX, OUT_CELLS = HERE / "horocycle_census.npz", HERE / "horocycle_census.json", HERE / "horocycle_cells.json"
REV = "5e1393631"
FILES = {
    "frontier/B1726_the_two_ingredients_replicated/verification/census.py": "185cf17d8b51c11559bf14650d5ad1dd12745eaa228fc40da0a8b9181d1986bf",
    "frontier/B1723_the_golden_valley/verification/b1656_funcs.py": "31f09c433c14312d9cee8cfa29a632a72ce13fc46ae838757bf9b22958f22528",
    "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/the_exponents.py": "a8d4ea9bae79dde894b192b7c3645685c1c97890665c96123be20ea6e9073aac",
    "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/qseries.py": "113b36d3da004a8a0b69d6f3fd8a38776f56ecbd14254e843c41232741ff1e6d",
    "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json": "688152749777970f21a85b3278a39ae33884b9ae99623d5eec541f41de34a774",
    "frontier/B1741_tau_from_the_thread_rule_the_line_free/verification/compare.py": "6308ed93e53ab99522cf654a85250f1299e9fa334ce13f92a74334cd7812f3bd",
    "frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json": "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f",
    "frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json": "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606",
    "frontier/B1786_the_slope_principle_out_of_sample/verification/census.jsonl.gz": "5acb140b473d5f93c0442b3408d3f71c46b55ba742fe46f19b9362ccea7b3bf9",
    "frontier/B1786_the_slope_principle_out_of_sample/verification/comparison.json": "6da874995663337e9255eeaa3223b3b73428619cd5e6ad252da6e68a5c59a1cb",
}
GUT_FILE = HERE.parent / "chat1_2026-10-23_attack" / "targets_unification.json"
GUT_SHA = "ea6af55b31c979588dbabcd98db6f11ac36a224328f30fde8943e7bae93cd301"
_G = {}

SECS, RDS, HORS = ("up", "down", "lep"), ("S", "St"), ("L_max", "L_2")
CONFIG = {"up": "St", "down": "S", "lep": "S"}                  # (S~, S, S): the data-free cells' configuration
NAMES = ("up2", "up1", "down2", "down1", "lep2", "lep1")
RE_G = tuple(round(0.05 + 0.1 * k, 2) for k in range(10))
IM_G = tuple(round(2.3 + 0.1 * k, 2) for k in range(13))
RE_B, IM_B = (0.25, 0.55, 0.75), (2.9, 3.0, 3.1, 3.2)
W_RE, W_IM = (-0.25, 0.25), (-1.4, 0.3)
FD, MAXIT, MAXHALF, STOP, RIDGE = 0.005, 6, 5, 1e-5, 1e-12
DELTA0 = complex(0.05, -0.35)
CB = tuple(25 * j for j in range(20))                             # control (b)'s base points: 20 lines, all 12 (Re, Im) pairs
NM_BOUNDS, NM_MAXFEV, NM_FATOL, NM_STEP = ((0.0, 1.0), (1.5, 3.6)), 80, 1e-3, 0.05
BAR6, BAR9 = 16.75, 21.67
B1786_BEST = (("23/30", 0.269230769), ("5/6", 0.730769231), 3.037487672558812)


def tree():
    """main's instruments at REV, extracted with B1786's pins into a private tree (a root marker for their ROOT search)"""
    if "tmp" not in _G:
        tmp = pathlib.Path(os.environ.get("HORO_TMP") or tempfile.mkdtemp())
        if not (tmp / "GENESIS.md").exists():
            for rel, sha in FILES.items():
                b = subprocess.run(["git", "show", "%s:%s" % (REV, rel)], cwd=ROOT, capture_output=True, check=True).stdout
                assert hashlib.sha256(b).hexdigest() == sha, rel
                p = tmp / rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(b)
            (tmp / "GENESIS.md").write_text("root marker for the imported instruments\n")
        os.environ["HORO_TMP"] = str(tmp)
        _G["tmp"] = tmp
    return _G["tmp"]


def K():
    """B1726's sealed census module (its compute), under its own name"""
    if "K" not in _G:
        t = tree(); rel = "frontier/B1726_the_two_ingredients_replicated/verification/census.py"
        sp = importlib.util.spec_from_file_location("b1726_census", t / rel); m = importlib.util.module_from_spec(sp)
        sys.modules["b1726_census"] = m
        with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(m)
        _G["K"] = m
    return _G["K"]


def C():
    """B1741's compare.py, unchanged"""
    if "C" not in _G:
        t = tree(); rel = "frontier/B1741_tau_from_the_thread_rule_the_line_free/verification/compare.py"
        sp = importlib.util.spec_from_file_location("b1741_compare", t / rel); m = importlib.util.module_from_spec(sp)
        sys.modules["b1741_compare"] = m; sp.loader.exec_module(m)
        _G["C"] = m
    return _G["C"]


def lines():
    out = [(Fr(2, 5), Fr(k, 10)) for k in range(10)]
    out += [(Fr(2, 5), Fr(k, 25)) for k in range(1, 25) if k % 5 != 0]
    out += [(Fr(2, 5), Fr(k, 30)) for k in range(1, 30) if math.gcd(k, 6) == 1]
    assert len(out) == 40 and len(set(out)) == 40
    return out


def point(re_t, im_t, li):
    """compute() at one point: the ratios (sector, horocycle, reading, generation) as (3, 2, 2, 2) and the CKM moduli
    (horocycle, up reading, down reading, [V_us, V_cb, V_ub]) as (2, 2, 2, 3)"""
    a, b = lines()[li]
    r = K().compute(re_t, im_t, a, b)
    rat = np.array([[[r["%s|%s|%s" % (s, h, rd)] for rd in RDS] for h in HORS] for s in SECS], dtype=float)
    ckm = np.array([[[r["ckm|%s|%s|%s" % (h, ru, rd)][:3] for rd in RDS] for ru in RDS] for h in HORS], dtype=float)
    return rat, ckm


def six(rat, h):
    """the six's logs in the configuration (S~, S, S) at horocycle index h, from a (3, 2, 2, 2) ratio array"""
    with np.errstate(divide="ignore"):
        lg = np.log(rat)
    return np.array([lg[i, h, RDS.index(CONFIG[s]), g] for i, s in enumerate(SECS) for g in (0, 1)])


def Lpair(im_t):
    col = K()._modules()["col"]
    return (float(np.interp(im_t, [q[0] for q in col], [q[1] for q in col])), float(np.interp(im_t, [q[0] for q in col], [q[2] for q in col])))


# ------------------------------------------------------------------------------------------------------------- the census
def chunk(name):
    return CH / name


def g_task(li):
    p = chunk("g_%02d.npz" % li)
    if p.exists(): return li
    arr = np.zeros((len(RE_G), len(IM_G), 3, 2, 2, 2)); ck = np.zeros((len(RE_G), len(IM_G), 2, 2, 2, 3))
    for i, re_t in enumerate(RE_G):
        for j, im_t in enumerate(IM_G):
            arr[i, j], ck[i, j] = point(re_t, im_t, li)
    tmp = p.with_suffix(".tmp.npz"); np.savez(tmp, r=arr, k=ck); os.replace(tmp, p)
    return li


def load_G():
    if "G" not in _G:
        z = [np.load(chunk("g_%02d.npz" % li)) for li in range(40)]
        _G["G"] = np.array([x["r"] for x in z]); _G["GK"] = np.array([x["k"] for x in z])
    return _G["G"]


def rms(x):
    return float(np.sqrt(np.mean(x ** 2))) if np.all(np.isfinite(x)) else float("inf")


def search(li, tp, y, h, Gr):
    """the rule's search: min over dtau in W of rms(v(li, tp + dtau, h) - y).  Start at the best G point inside tp + W, then
    Gauss-Newton: forward differences (backward at W's upper edges), normal equations with a 1e-12 ridge, clamped to W,
    a step that does not lower the rms halved at most five times, at most six iterations, stop when the rms changes by
    less than 1e-5.  Returns (A, dtau, flagged, iterations, evaluations, path, residual)"""
    best, start = float("inf"), None
    for i, re_t in enumerate(RE_G):
        for j, im_t in enumerate(IM_G):
            d = complex(re_t - tp.real, im_t - tp.imag)
            if not (W_RE[0] - 1e-12 <= d.real <= W_RE[1] + 1e-12 and W_IM[0] - 1e-12 <= d.imag <= W_IM[1] + 1e-12): continue
            e = rms(six(Gr[li, i, j], h) - y)
            if e < best: best, start = e, d
    if start is None or not np.isfinite(best):
        return float("inf"), None, True, 0, 0, [], None
    clampd = lambda d: complex(min(max(d.real, W_RE[0]), W_RE[1]), min(max(d.imag, W_IM[0]), W_IM[1]))
    ev = [0]

    def f(d):
        t = tp + d; ev[0] += 1
        return six(point(t.real, t.imag, li)[0], h) - y
    d = start; r = f(d); cur = rms(r); it = 0; path = [(d.real, d.imag, cur)]
    while it < MAXIT and np.isfinite(cur):
        it += 1
        sre, sim = (FD if d.real + FD <= W_RE[1] else -FD), (FD if d.imag + FD <= W_IM[1] else -FD)
        r1 = f(d + sre); r2 = f(d + 1j * sim)
        if not (np.all(np.isfinite(r1)) and np.all(np.isfinite(r2))): break
        Jm = np.stack([(r1 - r) / sre, (r2 - r) / sim], axis=1)
        step = -np.linalg.solve(Jm.T @ Jm + RIDGE * np.eye(2), Jm.T @ r)
        stepc = complex(step[0], step[1]); acc = False
        for _ in range(MAXHALF + 1):
            dn = clampd(d + stepc); rn = f(dn); en = rms(rn)
            if en < cur: acc = True; break
            stepc = stepc / 2
        if not acc: break
        change = cur - en; d, r, cur = dn, rn, en; path.append((d.real, d.imag, cur))
        if change < STOP: break
    flagged = abs(d.real - W_RE[0]) < 1e-9 or abs(d.real - W_RE[1]) < 1e-9 or abs(d.imag - W_IM[0]) < 1e-9 or abs(d.imag - W_IM[1]) < 1e-9
    return cur, d, bool(flagged), it, ev[0], path, [float(x) for x in r]


def b_points():
    return [(li, re_t, im_t) for li in range(40) for re_t in RE_B for im_t in IM_B]


def b_task(k):
    p = chunk("b_%03d.json" % k)
    if p.exists(): return k
    li, re_t, im_t = b_points()[k]
    Gr = load_G()
    y = six(Gr[li, RE_G.index(re_t), IM_G.index(im_t)], 0)                              # every base point is a point of G
    if not np.all(np.isfinite(y)):
        out = {"k": k, "excluded": "non-finite at L_max"}
    else:
        A, d, fl, it, ev, path, res = search(li, complex(re_t, im_t), y, 1, Gr)
        out = {"k": k, "A": A, "dtau": None if d is None else [d.real, d.imag], "flagged": fl, "iterations": it, "evaluations": ev,
               "path": path, "residual": res}
    tmp = p.with_suffix(".tmp"); tmp.write_text(json.dumps(out)); os.replace(tmp, p)
    return k


def cb_task(j):
    """control (b): the L_2 surface shifted by DELTA0 as the target, searched over the L_2 surface by the same procedure"""
    p = chunk("cb_%02d.json" % j)
    if p.exists(): return j
    li, re_t, im_t = b_points()[CB[j]]
    Gr = load_G(); tp = complex(re_t, im_t); t0 = tp + DELTA0
    y = six(point(t0.real, t0.imag, li)[0], 1)
    A, d, fl, it, ev, path, res = search(li, tp, y, 1, Gr)
    out = {"j": j, "k": CB[j], "A": A, "dtau": None if d is None else [d.real, d.imag], "flagged": fl, "iterations": it, "evaluations": ev + 1,
           "path": path, "recovered": bool(d is not None and A <= 1e-3 and abs(d - DELTA0) <= 0.01)}
    tmp = p.with_suffix(".tmp"); tmp.write_text(json.dumps(out)); os.replace(tmp, p)
    return j


def b1786_rows():
    """B1786's committed census: its best row, that row's mirror, its first row, and its slope-2/5 rows"""
    t = tree(); best = {k: None for k in B1786_BEST[:2]}; first = None; a25 = []
    with gzip.open(t / "frontier/B1786_the_slope_principle_out_of_sample/verification/census.jsonl.gz", "rt", encoding="utf-8") as fh:
        for l in fh:
            r = json.loads(l)
            if first is None: first = r
            if r.get("alpha") == "2/5":
                a25.append(r)
                for (b_, re_) in best:
                    if r.get("b") == b_ and abs(r["Re_tau"] - re_) < 1e-6 and abs(r["Im_tau"] - B1786_BEST[2]) < 1e-9: best[(b_, re_)] = r
    return [best[B1786_BEST[0]], best[B1786_BEST[1]], first], a25


def control_a():
    """control (a): three stored rows of B1786's census against compute(), every sector, reading and horocycle"""
    rows, _ = b1786_rows(); out = []
    assert all(r is not None for r in rows)
    for r in rows:
        c = K().compute(r["Re_tau"], r["Im_tau"], Fr(r["alpha"]), Fr(r["b"]))
        dev = max(abs(c[k][g] / r[k][g] - 1) for k in c if k.split("|")[0] in SECS for g in (0, 1) if r[k][g] != 0)
        out.append({"line": [r["alpha"], r["b"]], "tau": [r["Re_tau"], r["Im_tau"]], "worst_relative": dev})
    return {"rows": out, "holds": len(out) == 3 and all(o["worst_relative"] <= 1e-9 for o in out)}


def run_pool(fn, items, label, nw, t0, max_s):
    if not items: return True
    from multiprocessing import Pool
    n = 0
    with Pool(nw) as P:
        for _ in P.imap_unordered(fn, items):
            n += 1
            if n % 10 == 0: print("%s: %d done this part (%.0f s)" % (label, n, time.time() - t0), flush=True)
            if time.time() - t0 > max_s:
                print("part stopped by its time limit (%s, %d done this part)" % (label, n), flush=True); P.terminate(); return False
    return True


def census(nw, max_s):
    CH.mkdir(exist_ok=True); tree(); t0 = time.time()
    todo = [li for li in range(40) if not chunk("g_%02d.npz" % li).exists()]
    print("census: G (40 lines x 130 points); %d lines to do" % len(todo), flush=True)
    if not run_pool(g_task, todo, "G lines", nw, t0, max_s): return
    todo = [k for k in range(len(b_points())) if not chunk("b_%03d.json" % k).exists()]
    print("census: %d base-point searches to do" % len(todo), flush=True)
    if not run_pool(b_task, todo, "B searches", nw, t0, max_s): return
    todo = [j for j in range(len(CB)) if not chunk("cb_%02d.json" % j).exists()]
    if not run_pool(cb_task, todo, "control (b)", nw, t0, max_s): return
    ca = control_a()
    Gr = load_G()
    ims = set(IM_G)
    for k in range(len(b_points())):
        o = json.loads(chunk("b_%03d.json" % k).read_text())
        for (dr, di, _) in o.get("path", []): ims.add(round(b_points()[k][2] + di, 6))
    for j in range(len(CB)):
        o = json.loads(chunk("cb_%02d.json" % j).read_text()); im0 = b_points()[CB[j]][2]
        ims.add(round(im0 + DELTA0.imag, 6))
        for (dr, di, _) in o.get("path", []): ims.add(round(im0 + di, 6))
    cc = {"L_max_below_L_2_everywhere": all(a < b for a, b in (Lpair(x) for x in ims)), "Im_tau_range": [min(ims), max(ims)],
          "inside_column": bool(min(ims) >= 1.0 and max(ims) <= 4.0), "note": "the accepted points of every search, G and control (b)'s targets"}
    np.savez_compressed(OUT_CENSUS, G=Gr, GK=_G["GK"])
    OUT_INDEX.write_text(json.dumps({"rev": REV, "lines": [[str(a), str(b)] for a, b in lines()], "re_G": RE_G, "im_G": IM_G,
                                     "axes": {"G": "line, Re, Im, sector (up, down, lep), horocycle (L_max, L_2), reading (S, St), generation (m2/m3, m1/m3)",
                                              "GK": "line, Re, Im, horocycle, up reading, down reading, (V_us, V_cb, V_ub)"},
                                     "base_points": b_points(), "searches": [json.loads(chunk("b_%03d.json" % k).read_text()) for k in range(len(b_points()))],
                                     "control_b": [json.loads(chunk("cb_%02d.json" % j).read_text()) for j in range(len(CB))],
                                     "control_a": ca, "control_c": cc, "L_on_G": [Lpair(im) for im in IM_G]}, indent=0) + "\n")
    print("census complete: %s and %s written" % (OUT_CENSUS.name, OUT_INDEX.name))


# ------------------------------------------------------------------------------------------------------------- the cells
def targets():
    Cm = C(); v = json.loads(Cm.DATA.read_text(encoding="utf-8"))["masses_GeV"]["value"]
    T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
    Kc = json.loads(Cm.CKMDATA.read_text(encoding="utf-8"))["ckm_abs"]["value"]
    T9 = np.concatenate([T6, np.log(np.array([Kc[0][1], Kc[1][2], Kc[0][2]]))])
    s6, s9 = Cm.sigmas()
    gb = GUT_FILE.read_bytes(); assert hashlib.sha256(gb).hexdigest() == GUT_SHA
    g = json.loads(gb.decode("utf-8"))["GUT"]["tan beta 10"]
    TG = np.log(np.array(g["nine"][:6])); sG = np.sqrt(np.array(g["relative errors"][:6]) ** 2 + 0.1 ** 2)
    return T6, s6, T9, s9, TG, sG


def chi2_seat(rat, h, T, s, ckm=None):
    """B1741's seat measure at one row and horocycle: min over (S~, S, S), (S~, S~, S~) and c in {1, 3}; the nine when the
    CKM moduli (horocycle, up reading, down reading, 3) are given"""
    Cm = C(); best = float("inf")
    with np.errstate(divide="ignore"):
        lg = np.log(rat); lk = None if ckm is None else np.log(ckm)
    for (a, b, l) in Cm.SEAT:
        U, Dn, E = lg[0, h, a], lg[1, h, b], lg[2, h, l]
        for k in (0.0, Cm.LC3):
            x = [U[0], U[1], Dn[0], Dn[1], E[0] + k, E[1] - k] + ([] if lk is None else list(lk[h, a, b]))
            v = float(np.sum(((np.array(x) - T) / s) ** 2))
            if np.isfinite(v) and v < best: best = v
    return best


def stored(r):
    rat = np.array([[[r["%s|%s|%s" % (s, hh, rd)] for rd in RDS] for hh in HORS] for s in SECS], dtype=float)
    ckm = np.array([[[r["ckm|%s|%s|%s" % (hh, ru, rd)][:3] for rd in RDS] for ru in RDS] for hh in HORS], dtype=float)
    return rat, ckm


def nm_task(args):
    li, h, x0 = args
    p = chunk("nm_%02d_%d.json" % (li, h))
    if p.exists(): return json.loads(p.read_text())
    from scipy.optimize import minimize
    T6, s6 = targets()[:2]; ev = [0]

    def f(x):
        ev[0] += 1
        return chi2_seat(point(float(x[0]), float(x[1]), li)[0], h, T6, s6)
    x0 = np.array(x0, dtype=float)
    res = minimize(f, x0, method="Nelder-Mead", bounds=NM_BOUNDS,
                   options={"maxfev": NM_MAXFEV, "fatol": NM_FATOL, "xatol": np.inf,
                            "initial_simplex": np.array([x0, x0 + [NM_STEP, 0], x0 + [0, NM_STEP]])})
    out = {"line": li, "horocycle": HORS[h], "x0": list(x0), "x": [float(res.x[0]), float(res.x[1])], "chi2": float(res.fun), "evaluations": ev[0]}
    tmp = p.with_suffix(".tmp"); tmp.write_text(json.dumps(out)); os.replace(tmp, p)
    return out


def cells(nw, max_s):
    t0 = time.time()
    d = np.load(OUT_CENSUS); idx = json.loads(OUT_INDEX.read_text())
    Gr, GK = d["G"], d["GK"]; L = lines(); res = {}
    q = lambda x: [float(np.quantile(x, 0.1)), float(np.median(x)), float(np.quantile(x, 0.9))]
    # C0 and the stop rule, before any cell
    T6, s6, T9, s9, TG, sG = targets()
    ca, cc = idx["control_a"], idx["control_c"]
    cbr = [o["recovered"] for o in idx["control_b"]]
    v = np.array([[[[six(Gr[li, i, j], h) for h in (0, 1)] for j in range(len(IM_G))] for i in range(len(RE_G))] for li in range(40)])   # (40, 10, 13, 2, 6)
    fin = np.all(np.isfinite(v), axis=(-1, -2)); nonfinite = int((~fin).sum())
    rows, a25 = b1786_rows(); comp = json.loads((tree() / "frontier/B1786_the_slope_principle_out_of_sample/verification/comparison.json").read_text(encoding="utf-8"))
    six_min = nine_min = float("inf"); apex = {hn: float("inf") for hn in HORS}
    for r in a25:
        rat, ckm = stored(r)
        for h in (0, 1):
            c6 = chi2_seat(rat, h, T6, s6); c9 = chi2_seat(rat, h, T9, s9, ckm)
            six_min = min(six_min, c6); nine_min = min(nine_min, c9); apex[HORS[h]] = min(apex[HORS[h]], c6)
    res["C0"] = {"a": ca,
                 "a_prime": {"stored_least_chi2_six": comp["chi2"]["a2/5"]["six|seat"]["min"], "recomputed": six_min,
                             "holds": abs(six_min - comp["chi2"]["a2/5"]["six|seat"]["min"]) <= 1e-9},
                 "a_double_prime": {"stored_least_chi2_nine": comp["chi2"]["a2/5"]["nine|seat"]["min"], "recomputed": nine_min,
                                    "holds": abs(nine_min - comp["chi2"]["a2/5"]["nine|seat"]["min"]) <= 1e-9},
                 "b": {"recovered": int(sum(cbr)), "of": len(cbr), "holds": sum(cbr) >= 18},
                 "c": dict(cc, holds=bool(cc["L_max_below_L_2_everywhere"] and cc["inside_column"])),
                 "d": {"G points with a non-finite log": nonfinite, "of": int(fin.size), "holds": nonfinite <= 0.005 * fin.size}}
    stop = not (ca["holds"] and res["C0"]["c"]["holds"] and res["C0"]["d"]["holds"])
    stop_chi2 = not (res["C0"]["a_prime"]["holds"] and res["C0"]["a_double_prime"]["holds"])
    if stop:
        res["stopped"] = "control (a), (c) or (d) failed: no cell is read"
        OUT_CELLS.write_text(json.dumps(res, indent=1, default=str) + "\n"); print(json.dumps(res, indent=1, default=str)); return
    # H1, H3: the levers
    Lam = v[..., 0, :] - v[..., 1, :]; m = fin                                            # (40, 10, 13, 6)
    h1 = {SECS[s]: float((np.abs(Lam[..., 2 * s + 1]) > np.abs(Lam[..., 2 * s]))[m].mean()) for s in range(3)}
    res["H1"] = {"fraction_first_above_second": h1, "holds": all(x >= 0.9 for x in h1.values())}
    d1ud, d1ld = Lam[..., 1] - Lam[..., 3], Lam[..., 5] - Lam[..., 3]
    ok3 = (np.abs(d1ud) <= 0.1) & (np.abs(d1ld) <= 0.1)
    res["H3"] = {"fraction": float(ok3[m].mean()), "holds": float(ok3[m].mean()) >= 0.9,
                 "median_abs_d1_ud": float(np.median(np.abs(d1ud[m]))), "median_abs_d1_ld": float(np.median(np.abs(d1ld[m])))}
    res["readout_levers_q10_q50_q90"] = {NAMES[i]: q(Lam[..., i][m]) for i in range(6)}
    d2ud, d2ld = Lam[..., 0] - Lam[..., 2], Lam[..., 4] - Lam[..., 2]
    res["readout_second_generation_lever_differences"] = {"median_abs_ud": float(np.median(np.abs(d2ud[m]))), "median_abs_ld": float(np.median(np.abs(d2ld[m]))),
                                                          "fraction_both_within_0.1": float(((np.abs(d2ud) <= 0.1) & (np.abs(d2ld) <= 0.1))[m].mean())}
    # H2: flagged searches fail for both verdicts; control (b) guards NOT ABSORBED (a found distance is attained, so ABSORBED needs no guard)
    S = idx["searches"]; valid = [o for o in S if "A" in o]; n = len(valid)
    ok_abs = np.array([(not o["flagged"]) and np.isfinite(o["A"]) and o["A"] <= 0.05 for o in valid])
    ok_not = np.array([(not o["flagged"]) and np.isfinite(o["A"]) and o["A"] >= 0.15 for o in valid])
    absorbed = n > 0 and ok_abs.mean() >= 0.9
    notabs = n > 0 and ok_not.mean() >= 0.5 and res["C0"]["b"]["holds"]
    A_all = np.array([o["A"] for o in valid])
    lam0 = np.array([rms(six(Gr[b_points()[o["k"]][0], RE_G.index(b_points()[o["k"]][1]), IM_G.index(b_points()[o["k"]][2])], 1)
                         - six(Gr[b_points()[o["k"]][0], RE_G.index(b_points()[o["k"]][1]), IM_G.index(b_points()[o["k"]][2])], 0)) for o in valid])
    maxres = np.array([max(abs(x) for x in o["residual"]) if o["residual"] else np.inf for o in valid])
    res["H2"] = {"base_points": len(S), "searched": n, "excluded": len(S) - n, "flagged": int(sum(o["flagged"] for o in valid)),
                 "fraction_unflagged_A_le_0.05": float(ok_abs.mean()) if n else None, "fraction_unflagged_A_ge_0.15": float(ok_not.mean()) if n else None,
                 "A_q10_q50_q90": q(A_all[np.isfinite(A_all)]) if n else None,
                 "verdict": "ABSORBED" if absorbed else ("NOT ABSORBED" if notabs else "UNDETERMINED"),
                 "not_absorbed_readable": res["C0"]["b"]["holds"]}
    dt = np.array([o["dtau"] for o in valid if o["dtau"] is not None])
    res["readout_H2"] = {"rms_lever_at_zero_shift_q10_q50_q90": q(lam0[np.isfinite(lam0)]), "largest_single_residual_q10_q50_q90": q(maxres[np.isfinite(maxres)]),
                         "dRe_q10_q50_q90": q(dt[:, 0]) if len(dt) else None, "dIm_q10_q50_q90": q(dt[:, 1]) if len(dt) else None,
                         "flagged": [[str(L[b_points()[o["k"]][0]][0]), str(L[b_points()[o["k"]][0]][1]), b_points()[o["k"]][1], b_points()[o["k"]][2], o["A"], o["dtau"]] for o in valid if o["flagged"]]}
    # the chi2 stage
    if stop_chi2:
        res["stopped_chi2"] = "control (a') or (a'') failed: H4, H5 and the chi2 read-outs are not read"
    else:
        chiG = np.full((40, len(RE_G), len(IM_G), 2), np.inf); chi9 = np.full_like(chiG, np.inf); chiGUT = np.full_like(chiG, np.inf)
        for li in range(40):
            for i in range(len(RE_G)):
                for j in range(len(IM_G)):
                    for h in (0, 1):
                        chiG[li, i, j, h] = chi2_seat(Gr[li, i, j], h, T6, s6); chi9[li, i, j, h] = chi2_seat(Gr[li, i, j], h, T9, s9, GK[li, i, j])
                        chiGUT[li, i, j, h] = chi2_seat(Gr[li, i, j], h, TG, sG)
        tasks = []
        for li in range(40):
            for h in (0, 1):
                i, j = np.unravel_index(int(np.argmin(chiG[li, :, :, h])), chiG.shape[1:3]); tasks.append((li, h, [RE_G[i], IM_G[j]]))
        todo = [t for t in tasks if not chunk("nm_%02d_%d.json" % (t[0], t[1])).exists()]
        print("cells: %d refinements to do" % len(todo), flush=True)
        if not run_pool(nm_task, todo, "refinements", nw, t0, max_s): return
        nm = [json.loads(chunk("nm_%02d_%d.json" % (t[0], t[1])).read_text()) for t in tasks]

        def least(sel, hn):
            b = min((o for o in nm if o["line"] in sel and o["horocycle"] == hn), key=lambda o: o["chi2"])
            return {"chi2": b["chi2"], "line": [str(L[b["line"]][0]), str(L[b["line"]][1])], "tau": b["x"], "start": b["x0"]}
        out30, ten = list(range(10, 40)), list(range(10))
        h4 = {hn: least(out30, hn) for hn in HORS}
        res["H4"] = {"on_the_30_lines": h4, "L_max_clause_below": h4["L_max"]["chi2"] < BAR6, "L_2_clause_at_or_above": h4["L_2"]["chi2"] >= BAR6,
                     "holds": h4["L_max"]["chi2"] < BAR6 and h4["L_2"]["chi2"] >= BAR6}
        h5 = {hn: float(chi9[10:, :, :, HORS.index(hn)].min()) for hn in HORS}
        res["H5"] = {"least_chi2_nine_on_G_30_lines": h5, "passes": {hn: h5[hn] < BAR9 for hn in HORS}}
        res["readout_H4_on_the_ten_lines_2_5_k_10"] = {hn: least(ten, hn) for hn in HORS}
        res["readout_B1786_apex_grid_least_chi2_six_per_horocycle_30_lines"] = apex
        res["readout_gut_scale_G_minima"] = {hn: {"30_lines": float(chiGUT[10:, :, :, HORS.index(hn)].min()), "ten_lines": float(chiGUT[:10, :, :, HORS.index(hn)].min())} for hn in HORS}
        res["readout_nelder_mead"] = nm
    OUT_CELLS.write_text(json.dumps(res, indent=1, default=str) + "\n")
    C0 = res["C0"]
    print("C0: (a) %s; (a') %s; (a'') %s; (b) %s (%d of %d); (c) %s; (d) %s" % (C0["a"]["holds"], C0["a_prime"]["holds"], C0["a_double_prime"]["holds"],
          C0["b"]["holds"], C0["b"]["recovered"], C0["b"]["of"], C0["c"]["holds"], C0["d"]["holds"]))
    print("H1 holds %s: %s" % (res["H1"]["holds"], res["H1"]["fraction_first_above_second"]))
    print("H2 (THE DECISIVE CELL): %s; %s" % (res["H2"]["verdict"], {k: v for k, v in res["H2"].items() if k != "verdict"}))
    print("H3 holds %s: %s" % (res["H3"]["holds"], res["H3"]))
    if "H4" in res:
        print("H4 holds %s: %s" % (res["H4"]["holds"], res["H4"]["on_the_30_lines"]))
        print("H5: %s" % res["H5"])
        print("read-out, H4's statistic on the ten (2/5, k/10) lines (informed): %s" % res["readout_H4_on_the_ten_lines_2_5_k_10"])
        print("read-out, B1786's apex grid, least chi2_six per horocycle on the 30 lines: %s" % res["readout_B1786_apex_grid_least_chi2_six_per_horocycle_30_lines"])
        print("read-out, the unification scale (G minima, tan beta 10): %s" % res["readout_gut_scale_G_minima"])
    else:
        print(res["stopped_chi2"])
    print("read-out, levers (q10, q50, q90): %s" % res["readout_levers_q10_q50_q90"])
    print("read-out, second-generation lever differences: %s" % res["readout_second_generation_lever_differences"])
    print("read-out, H2: %s" % {k: v for k, v in res["readout_H2"].items() if k != "flagged"})
    print("read-out, flagged searches: %d" % len(res["readout_H2"]["flagged"]))
    print("horocycle cells exit 0")


if __name__ == "__main__":
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 2
    ms = float(sys.argv[sys.argv.index("--max-seconds") + 1]) if "--max-seconds" in sys.argv else 6600
    if "--census" in sys.argv:
        census(nw, ms)
    elif "--cells" in sys.argv:
        cells(nw, ms)
    else:
        print(__doc__)
