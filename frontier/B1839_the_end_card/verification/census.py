"""B1839 census (data-free): THE END CARD's frame quantities, sealed in ../PREREGISTRATION.md before this runs.

At B1753's 223 apexes (reduced to |Re tau| <= 1/2 by T^-1), the exact norm of each of B1656's four twisted channels over
B1667's Dirichlet cell minus the horoball at level L_max(tau) + delta, for every Higgs-twist class (+-3w mod the lattice)
of B1713's 266 lines and the 22 levels DELTAS. The web seat's instrument (B1838's byte-faithful exact_end_web_seat.py) is
loaded unchanged; its twisted_norms() is split here into cell_nodes() (geometry only: the horocycle solve, shared by every
line at one (tau, L_h)) and kernel_norms() (the sum, per class), the same arithmetic in the same order. One quadrature per
class, with the down sector's twists (its four channels); control C1 checks every sector and line against the instrument.
No data are read.
    python3 -B census.py --workers 8     -> accessory.jsonl, norms.npz, norms_index.json, census_run.txt ("census exit 0")
    python3 -B census.py --controls      -> C1, C2 only
Importing computes nothing."""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys, json, math, random, time, hashlib, pathlib, importlib.util
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
DELTAS = (0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50, 0.60, 0.70, 0.80, 1.0, 1.25, 1.5, 2.0, 2.5, 3.0, 4.0,
          6.0, 10.0)
NTH, NS = 40, 28
UNITS = ("1", "i", "j", "k")
ACC = HERE / "accessory.jsonl"
CKPT = HERE / "norms_ckpt.jsonl"
_M = {}


def mods():
    """the web seat's instrument (B1838), B1753's census (apexes) and B1726's lines, each loaded under its own name"""
    if not _M:
        argv = sys.argv
        sys.argv = [argv[0], str(ROOT)]
        sp = importlib.util.spec_from_file_location("b1839_ee", ROOT / "frontier" / "B1838_the_end" / "verification" / "exact_end_web_seat.py")
        ee = importlib.util.module_from_spec(sp); sp.loader.exec_module(ee)
        if "b1753_census" not in sys.modules:
            sp = importlib.util.spec_from_file_location("b1753_census", ROOT / "frontier" / "B1753_the_six_on_the_five_ality_lines" / "verification" / "census.py")
            m = importlib.util.module_from_spec(sp); sys.modules["b1753_census"] = m; sp.loader.exec_module(m)
        sys.argv = argv
        B53 = sys.modules["b1753_census"]
        lines = [(Fr(a), Fr(b)) for a, b in B53._K().lines()]
        _M.update(ee=ee, C=ee.C, B=ee.B, K=ee.K, B53=B53, LINES=lines, AP=B53.apexes())
    return _M


def hkey(a, b):
    """the Higgs-twist class of the line (a, b): +-(3a, 3b) mod 1, the smaller of the pair"""
    k1 = ((3 * a) % 1, (3 * b) % 1); k2 = ((-3 * a) % 1, (-3 * b) % 1)
    return min(k1, k2)


def classes():
    """the classes of the 266 unreduced lines (their order of first appearance) and each line's class index; reduction
    by T^-n maps classes to classes, so the partition is the same at every apex (checked by C1)"""
    L = mods()["LINES"]; keys, idx = [], []
    for a, b in L:
        k = hkey(a, b)
        if k not in keys: keys.append(k)
        idx.append(keys.index(k))
    reps = [idx.index(j) for j in range(len(keys))]
    return keys, idx, reps


def reduce(tau0):
    """T^-n to |Re tau| <= 1/2 (B1667's cell); a line (a, b) goes to (a, b + n a mod 1)"""
    tau, n = complex(tau0), 0
    while tau.real > 0.5: tau, n = tau - 1, n + 1
    while tau.real < -0.5: tau, n = tau + 1, n - 1
    return tau, n


def red_line(line, n):
    a, b = line
    return a, (b + n * a) % 1


def cell_nodes(tau, al, be, Lh, nth=NTH, ns=NS):
    """twisted_norms()'s geometry, unchanged: per Voronoi edge the angular nodes, the horocycle radius on each ray, the
    log-radial nodes and weights"""
    from numpy.polynomial.legendre import leggauss
    ee = mods()["ee"]; C = mods()["C"]
    br, rmaxf = C.voronoi(tau); xg, wg = leggauss(nth); xs, ws = leggauss(ns)
    nodes = []; margin = np.inf
    for a_, b_ in zip(br[:-1], br[1:]):
        th = 0.5 * (b_ - a_) * xg + 0.5 * (b_ + a_); wt = 0.5 * (b_ - a_) * wg
        rmax = rmaxf(th)
        rh = [C.horocycle_radius(al, be, Lh, t_, min(0.95, 1.1 * rm)) for t_, rm in zip(th, rmax)]
        if any(v is None for v in rh):
            raise RuntimeError("the horocycle does not close inside the cell at tau = %s" % tau)
        rh = np.array(rh, dtype=float); margin = min(margin, float(np.min(rmax - rh)))
        s_hi = np.log(rmax); s_lo = np.log(np.minimum(rh, rmax))
        s = 0.5 * (s_hi - s_lo)[:, None] * xs[None, :] + 0.5 * (s_hi + s_lo)[:, None]
        wsr = 0.5 * (s_hi - s_lo)[:, None] * ws[None, :]
        rr = np.exp(s); z = rr * np.exp(1j * th)[:, None]
        nodes.append((wt, wsr, rr, z))
    return nodes, margin


def kernel_norms(nodes, x, y, R, tau):
    """twisted_norms()'s sum, unchanged"""
    B = mods()["B"]
    tot = {s: 0.0 for s in B.UNITS}
    for wt, wsr, rr, z in nodes:
        P = B.pairs(x, y, z, tau)
        for sc in B.UNITS:
            if abs(R[sc]) > 1e-12:
                tot[sc] += float(np.sum(wt[:, None] * wsr * np.abs(P[sc] / R[sc]) ** 2 * rr ** 2))
    return tot


def twists(tau, line, sector):
    M = mods(); B, K = M["B"], M["K"]
    a, b = line; w = float(a) * tau + float(b); lf, rf = K.SECT[sector]
    x, yy = B.sector_twists(w, tau, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, tau)
    return x, yy, R


def accessory_all(log):
    """serial: the accessory parameter at every reduced apex, continued from the nearest solved point (B1667's
    newton_walk, which raises if the continuation is lost), and B1667's geometry there; checkpointed"""
    M = mods(); C, ee, AP = M["C"], M["ee"], M["AP"]
    done = {}
    if ACC.exists():
        for l in ACC.read_text(encoding="utf-8").splitlines():
            if l.strip():
                r = json.loads(l); done[r["apex"]] = r
    c0 = C.track(ee.CONTROL); c0, _ = C.solve_accessory(ee.CONTROL, c0)
    solved = [(ee.CONTROL, c0)] + [(complex(*r["tau"]), complex(*r["c"])) for r in done.values()]
    order = sorted(range(len(AP)), key=lambda i: (AP[i]["Im_tau"], reduce(complex(AP[i]["Re_tau"], AP[i]["Im_tau"]))[0].real))
    with ACC.open("a", encoding="utf-8") as fh:
        for i in order:
            if i in done: continue
            p = AP[i]; tau, n = reduce(complex(p["Re_tau"], p["Im_tau"]))
            t0, cc = min(solved, key=lambda q: abs(q[0] - tau))
            c, res = C.newton_walk(t0, cc, tau); solved.append((tau, c))
            G = ee.geometry(tau, c)
            r = {"apex": i, "tau0": [p["Re_tau"], p["Im_tau"]], "n": n, "tau": [tau.real, tau.imag], "c": [c.real, c.imag],
                 "residual": res, "L_max": G["L_max"], "L_2": G["L_2"], "cusp_area": G["cusp_area"]}
            fh.write(json.dumps(r) + "\n"); fh.flush(); done[i] = r
    log("accessory: %d apexes; max residual %.1e; L_max %.4f .. %.4f; L_2 %.4f .. %.4f" % (
        len(done), max(r["residual"] for r in done.values()), min(r["L_max"] for r in done.values()),
        max(r["L_max"] for r in done.values()), min(r["L_2"] for r in done.values()), max(r["L_2"] for r in done.values())))
    return [done[i] for i in range(len(AP))]


def load_acc():
    rows = {}
    for l in ACC.read_text(encoding="utf-8").splitlines():
        if l.strip():
            r = json.loads(l); rows[r["apex"]] = r
    return [rows[i] for i in range(len(rows))]


def apex_task(rec):
    """one apex: the 22 levels x the 170 classes, four channels each"""
    t0 = time.time(); M = mods(); ee = M["ee"]
    tau = complex(*rec["tau"]); c = complex(*rec["c"]); n = rec["n"]
    G = ee.geometry(tau, c)
    assert abs(G["L_max"] - rec["L_max"]) < 1e-12, (rec["apex"], G["L_max"], rec["L_max"])
    keys, idx, reps = classes()
    tw = [twists(tau, red_line(M["LINES"][k], n), "down") for k in reps]
    out = np.zeros((len(reps), len(DELTAS), 4)); margins = []
    for j, d in enumerate(DELTAS):
        nodes, margin = cell_nodes(tau, G["al"], G["be"], G["L_max"] + d); margins.append(margin)
        for q, (x, yy, R) in enumerate(tw):
            N = kernel_norms(nodes, x, yy, R, tau)
            out[q, j] = [N[s] for s in UNITS]
    return {"apex": rec["apex"], "norms": out.tolist(), "margins": margins, "seconds": time.time() - t0}


def run_census(workers, log):
    from multiprocessing import get_context
    acc = accessory_all(log)
    done = set()
    if CKPT.exists():
        for l in CKPT.read_text(encoding="utf-8").splitlines():
            if l.strip(): done.add(json.loads(l)["apex"])
    todo = [r for r in acc if r["apex"] not in done]
    log("census: %d apexes to do (%d done), %d classes x %d levels each, %d workers" % (len(todo), len(done), len(classes()[0]), len(DELTAS), workers))
    t0 = time.time()
    with get_context("spawn").Pool(workers) as P, CKPT.open("a", encoding="utf-8") as fh:
        for k, r in enumerate(P.imap_unordered(apex_task, todo, chunksize=1)):
            fh.write(json.dumps(r) + "\n"); fh.flush()
            if (k + 1) % 10 == 0 or k + 1 == len(todo):
                log("  %d / %d apexes (%.0f s; last apex %.0f s)" % (k + 1, len(todo), time.time() - t0, r["seconds"]))
    rows = {}
    for l in CKPT.read_text(encoding="utf-8").splitlines():
        if l.strip():
            r = json.loads(l); rows[r["apex"]] = r
    keys, idx, reps = classes()
    arr = np.array([rows[i]["norms"] for i in range(len(acc))], dtype=float)          # (apex, class, level, channel)
    mg = np.array([rows[i]["margins"] for i in range(len(acc))], dtype=float)
    np.savez_compressed(HERE / "norms.npz", norms=arr, margins=mg)
    index = {"DELTAS": list(DELTAS), "NTH_NS": [NTH, NS], "units": list(UNITS), "class_keys": [[str(k[0]), str(k[1])] for k in keys],
             "line_class": idx, "class_rep_line": reps, "apexes": len(acc), "shape": list(arr.shape),
             "norms_sha256": hashlib.sha256(np.ascontiguousarray(arr).tobytes()).hexdigest()}
    (HERE / "norms_index.json").write_text(json.dumps(index, indent=1), encoding="utf-8")
    log("norms: shape %s, sha256 of the array bytes %s; min horoball margin to the cell %.3e; all finite %s" % (
        arr.shape, index["norms_sha256"], float(mg.min()), bool(np.all(np.isfinite(arr)))))
    CKPT.unlink()


def controls(log):
    """C1: the class cache against the instrument, sector by sector, at 120 random (apex, line, sector, level);
    C2: the split against the instrument at (40, 28), and (40, 28) against (96, 64), at 24 random (apex, class, level)"""
    M = mods(); ee, B = M["ee"], M["B"]
    acc = load_acc(); Z = np.load(HERE / "norms.npz"); arr = Z["norms"]; keys, idx, reps = classes()
    rng = random.Random(18391); geo = {}

    def G_of(i):
        if i not in geo:
            r = acc[i]; geo[i] = ee.geometry(complex(*r["tau"]), complex(*r["c"]))
        return geo[i]
    worst = {s: 0.0 for s in ("up", "down", "lep")}
    for _ in range(120):
        i = rng.randrange(len(acc)); k = rng.randrange(len(M["LINES"])); sec = rng.choice(("up", "down", "lep")); j = rng.randrange(len(DELTAS))
        r = acc[i]; tau = complex(*r["tau"]); G = G_of(i)
        x, yy, R = twists(tau, red_line(M["LINES"][k], r["n"]), sec)
        Ni, _ = ee.twisted_norms(tau, G["al"], G["be"], G["L_max"] + DELTAS[j], x, yy, R, nth=NTH, ns=NS)
        cache = arr[i, idx[k], j]
        for q, s in enumerate(UNITS):
            if abs(R[s]) > 1e-12:
                worst[sec] = max(worst[sec], abs(cache[q] / Ni[s] - 1))
    c1 = bool(max(worst.values()) < 1e-12)
    log("C1 (the class cache = the instrument, per sector, 120 cases): max rel %s -> %s" % (
        {s: "%.1e" % v for s, v in worst.items()}, "HOLDS" if c1 else "FAILS"))
    e_split = e_quad = 0.0
    picks = [(rng.randrange(len(acc)), rng.randrange(len(keys)), j) for j in (DELTAS.index(6.0), DELTAS.index(10.0))]
    picks += [(rng.randrange(len(acc)), rng.randrange(len(keys)), rng.randrange(len(DELTAS))) for _ in range(22)]
    for i, q, j in picks:
        r = acc[i]; tau = complex(*r["tau"]); G = G_of(i); Lh = G["L_max"] + DELTAS[j]
        x, yy, R = twists(tau, red_line(M["LINES"][reps[q]], r["n"]), "down")
        nodes, _ = cell_nodes(tau, G["al"], G["be"], Lh); Ns = kernel_norms(nodes, x, yy, R, tau)
        Ni, _ = ee.twisted_norms(tau, G["al"], G["be"], Lh, x, yy, R, nth=NTH, ns=NS)
        Nh, _ = ee.twisted_norms(tau, G["al"], G["be"], Lh, x, yy, R)
        for s in UNITS:
            if abs(R[s]) > 1e-12:
                e_split = max(e_split, abs(Ns[s] / Ni[s] - 1)); e_quad = max(e_quad, abs(Ni[s] / Nh[s] - 1))
    c2 = bool(e_split < 1e-13 and e_quad < 1e-9)
    log("C2 (24 cases incl. delta 6, 10): split vs instrument at (40,28) %.1e; (40,28) vs (96,64) %.1e -> %s" % (
        e_split, e_quad, "HOLDS" if c2 else "FAILS"))
    return {"C1": {"holds": c1, "per_sector_max_rel": {k: float(v) for k, v in worst.items()}}, "C2": {"holds": c2, "split": float(e_split), "quadrature": float(e_quad)}}


def main():
    t0 = time.time(); out = []

    def log(s):
        print(s, flush=True); out.append(s)
    if "--controls" in sys.argv:
        res = controls(log)
    else:
        w = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 8
        run_census(w, log); res = controls(log)
    (HERE / "census_controls.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    log("census exit 0 (%.0f s)" % (time.time() - t0))
    if "--controls" not in sys.argv:
        (HERE / "census_run.txt").write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
