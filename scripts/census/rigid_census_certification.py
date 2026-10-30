#!/usr/bin/env python3
"""The refined rigid census's certification, as aggregates only (THE FINAL ATTACK, Step B; P-521; REFINED_CENSUS_PLAN.md
sections 3, 6 and 7; main's rulings after the interpolant's diagnosis and on the fifth pre-seal review, 2026-10-30;
data-free).  REFUSED unless the manifest is committed and pushed (guard.require_pushed_manifest: the fifth review's B2), the
manifest's hash is the one given, and the directory holds exactly the files it lists.

The generator's continuous frame is the census interpolated cell by cell (STEP B's generator, cells.py: per row a
biquadratic through its 3 x 3 stencil, in the natural logs of the nine positive outputs and J SIGNED; a row whose stencil
is incomplete or carries a non-finite value is scored at its node).  This tool measures that frame against FRESH
evaluations by the census's own evaluator (B1821's cm_zero_line.rows_at) on a hash-chosen 5% of the cells (the cell's key
hashed with sha256, kept when the first byte is below 13: 13/256 = 5.1%), at a hash-chosen INTERIOR point of each (bytes
1-8 of the same hash: a typical tau, uniform on the cell's rectangle).

1. THE PLANTED GATE (the decision-relevant measure; it replaces the fourth review's pointwise gate F2, which fails wherever
   the frame has isolated zeros -- a log singularity no interpolant follows -- although the test's decisions are robust
   there: on the mini patch F2's q99 is 0.047 against 0.0217 log10, 2.0% of points above it).  At each chosen point Q,
   every row's fresh outputs are a planted world: the frame produces it, with chi2 = 0 at Q.  It is FOUND when the
   chosen cell alone reaches chi2 < T on the interpolant (decided by the generator's enclosure and branch-and-bound), or,
   for a node-only row, when its node does; other cells could also reach it, so the measured miss rate is an upper bound
   on the frame's.  sigma = ALLOW = 0.10 in natural log on every output (the smallest sigma the record allows: the
   strictest case).  An output below the roundoff floor 1e-12 at Q or at a node of the row's stencil (a structural zero:
   m1 = 0 where the coupling has rank 2, B1653; J = 0 where the CKM is real) is not a value the frame produces: the world
   is planted on its k remaining outputs at chi2_k's 0.99 quantile (k >= 6; without this rule the mini patch's miss rate
   was 12.8%, all of it roundoff); the removals are counted.  THE GATE: the larger of the miss rate's two-sided 95%
   Clopper-Pearson upper end and its 97.5% bootstrap quantile over cells (the 192 rows of a cell share one tau: the
   design effect) is at most 0.01 -- the numerical frame adds no more misses than the threshold's own 1%.
2. DETERMINISM: per file, the first chosen cell's NODE is re-evaluated at its stored tau; the census must equal it (largest
   |log10 difference| at most 1e-9; a structurally zero J, roundoff, is not compared).
3. B1824's duplicate: the largest difference between the a0 and F_-2 rows over the whole census, at most 1e-6 in log10.
4. Read-outs (never gating): the ten-output worlds' miss rate alone; the pointwise |log10 interpolant - log10 fresh| at Q,
   per output and overall, with the fraction above half of ALLOW (0.0217 log10); the planted worlds' best chi2 quantiles;
   the undecided searches; the node-only owners; the outputs the floor rule removed.
Output: counts and quantiles only; no row's value is printed or written.
    python3 -I scripts/census/rigid_census_certification.py <refined dir> <manifest.json> <manifest sha256> <out.json> [workers]"""
import gzip, hashlib, json, math, os, pathlib, sys
from fractions import Fraction as F
from multiprocessing import Pool

ROOT = pathlib.Path(__file__).resolve().parents[2]
EVAL = ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"
GEN = ROOT / "scripts" / "stepb"
TOL_LOG10 = 0.5 * 0.10 / math.log(10)          # 0.0217, a read-out's reference
FLOOR = 1e-12                                  # the roundoff floor (cells.FLOOR)
SIG = 0.10                                     # ALLOW, natural log
GATE_MISS = 0.01
BOOT = 2000
A0, FM2 = 1, 6
NAMES = ["c/t", "u/t", "s/b", "d/b", "mu/tau", "e/tau", "Vus", "Vcb", "Vub", "J"]


def manifest_ok(d, man_path, expected):
    man = json.loads(pathlib.Path(man_path).read_text(encoding="utf-8")); per = man["per_file"]
    h = hashlib.sha256("".join("%s  %s\n" % (v, n) for n, v in sorted(per.items())).encode()).hexdigest()
    if h != man["sha256_of_the_manifest"] or h != expected:
        return False, "the manifest is not the one given (%s)" % h
    have = sorted(p.name for p in d.glob("*.jsonl.gz"))
    if have != sorted(per):
        return False, "the directory's files are not the manifest's (%d against %d)" % (len(have), len(per))
    for n, v in per.items():
        if hashlib.sha256((d / n).read_bytes()).hexdigest() != v:
            return False, "%s does not match the manifest" % n
    return True, "%d files match" % len(per)


def _digest(key: str) -> bytes:
    return hashlib.sha256(key.encode()).digest()


def chosen(key: str) -> bool:
    return _digest(key)[0] < 13


def interior(key: str):
    """the cell's planted point in local coordinates (u, v) in [0, 1)^2, from bytes 1-8 of the cell key's sha256"""
    h = _digest(key)
    return int.from_bytes(h[1:5], "big") / 2 ** 32, int.from_bytes(h[5:9], "big") / 2 ** 32


def _census(records, C, reading_index, key):
    """a stepb_core.Census of the given records' rows (F_-2's dropped), all on the line `key`"""
    import numpy as np
    cfg, d, r, k, m, v, J, vd, L, tau = [], [], [], [], [], [], [], [], [], []
    for ci, rec in enumerate(records):
        L.append(key); tau.append(tuple(rec["tau"]))
        for x in rec["rows"]:
            if x[0] == FM2: continue
            cfg.append(ci); d.append(x[0]); r.append(x[1]); k.append(reading_index(x[2]))
            m.append([x[3], x[4], x[5]]); v.append(x[6]); J.append(x[7]); vd.append(bool(x[8]))
    return C.Census(cfg=np.array(cfg), d=np.array(d), r=np.array(r), k=np.array(k), m=np.array(m, float),
                    v=np.array(v, float), J=np.array(J, float), vdef=np.array(vd), lines=L, tau=np.array(tau, float))


def task(args):
    fname, d = args
    import sys as _s
    _s.path.insert(0, str(EVAL)); _s.path.insert(0, str(GEN))
    import numpy as np
    import cm_zero_line as Z
    import stepb_core as C
    from census_io import reading_index, line_key
    from assemble import Choices
    from cells import CellIndex
    from scipy.stats import chi2 as chi2d
    recs = []; a = b = None
    with gzip.open(pathlib.Path(d) / fname, "rt", encoding="utf-8") as fh:
        for line in fh:
            r = json.loads(line)
            if "error" in r: continue
            r["tau_raw"] = list(r["tau"]); r["tau"] = [round(r["tau"][0], 4), round(r["tau"][1], 4)]; recs.append(r)
            a, b = F(r["line"][0]), F(r["line"][1]); key = line_key(*r["line"])
    dup = 0.0
    for rec in recs:
        by = {(x[0], x[1], x[2]): x for x in rec["rows"]}
        for (dd, rr, lab), x in by.items():
            if dd == FM2:
                y = by[(A0, rr, lab)]; both = bool(x[8]) and bool(y[8])
                for p_, q_ in zip(list(x[3]) + list(x[4]) + list(x[5]) + (list(x[6]) if both else []),
                                  list(y[3]) + list(y[4]) + list(y[5]) + (list(y[6]) if both else [])):
                    if p_ > 0 and q_ > 0: dup = max(dup, abs(math.log10(p_) - math.log10(q_)))
    cen = _census(recs, C, reading_index, key); Fe = C.features(cen)
    pts = [tuple(rec["tau"]) for rec in recs]
    ch = Choices(cen, Fe, pts)
    ci = CellIndex(Fe, cen.J, pts, ch, np.full(10, SIG))
    kidx = {q[1:]: j for j, q in enumerate(ch.keys)}                      # (d, r, k) -> choice (one line per file)
    lf = math.log(FLOOR)
    cells = []                                     # per chosen cell: (planted, missed, planted10, missed10)
    undecided = node_only = removed = 0; best_x2 = []; perr = {k: [] for k in range(10)}; det = None
    for ni, node in enumerate(ci.gs.pts):
        ckey = "%s|%s|%s|%s" % (fname, node[0], node[1], "cell")
        if not chosen(ckey): continue
        x0, x1, y0, y1 = ci.cellr[ni]; u, v_ = interior(ckey)
        Q = (float(x0 + u * (x1 - x0)), float(y0 + v_ * (y1 - y0)))
        if det is None:                                                   # determinism: the node, fresh, at its stored tau
            rec = recs[pts.index(node)]
            fr = {(Z.DIRS.index(r["direction"]), ("L_max", "L_2").index(r["radius"]), r["reading"]): r for r in Z.rows_at(complex(*rec["tau_raw"]), (a, b))}
            det = 0.0
            for x in rec["rows"]:
                if x[0] == FM2: continue
                f_ = fr[(x[0], x[1], x[2])]
                js = [abs(x[7])] if abs(x[7]) > 1e-15 else []                  # a structurally zero J is roundoff
                jf = [abs(f_["J"])] if abs(x[7]) > 1e-15 else []
                for p_, q_ in zip(list(x[3]) + list(x[4]) + list(x[5]) + list(x[6]) + js,
                                  list(f_["up"]) + list(f_["down"]) + list(f_["lepton"]) + list(f_["V"]) + jf):
                    if p_ > 0 and q_ > 0: det = max(det, abs(math.log10(p_) - math.log10(q_)))
                    elif (p_ > 0) != (q_ > 0): det = math.inf
        fresh = Z.rows_at(complex(*Q), (a, b))
        frc = _census([{"tau": Q, "rows": [[Z.DIRS.index(r["direction"]), ("L_max", "L_2").index(r["radius"]), r["reading"],
                                            r["up"], r["down"], r["lepton"], r["V"], r["J"], r["V defined"]] for r in fresh]}], C, reading_index, key)
        Ff = C.features(frc)
        pc = mc = p10 = m10 = 0
        for i in range(len(frc.cfg)):
            if not frc.vdef[i]: continue
            q = (int(frc.d[i]), int(frc.r[i]), int(frc.k[i])); jc = kidx.get(q)
            if jc is None: continue
            rr = int(ch.R[jc, ni])
            if rr < 0: continue
            t = Ff[i]
            sts = ci.stencil_rows([rr])[0] if ci.ok[rr] else np.array([rr])
            ok_k = [k for k in range(10) if np.isfinite(t[k]) and t[k] >= lf and (Fe[sts[sts >= 0], k] >= lf).all()]
            removed += 10 - len(ok_k)
            comps = tuple(ok_k)
            if len(comps) < 6: continue
            T = float(chi2d.ppf(0.99, len(comps)))
            if ci.ok[rr]:
                v = float(ci._x2(ci.values_at(rr, [Q])[0], t, comps)); hit = v < T; bx = v
                if not hit:
                    st, v2, _, _ = ci.cell_min(rr, t, comps, T=T); bx = min(bx, v2)
                    hit = st == "below"; undecided += st == "undecided"
                f = ci.values_at(rr, [Q])[0]
                for k in comps:
                    if np.isfinite(f[k]) and np.isfinite(t[k]): perr[k].append(abs(f[k] - t[k]) / math.log(10))
            else:                                                         # node-only: the frame is its node on this cell
                node_only += 1
                bx = float(ci._x2(ci.feat(ci.coords([rr]))[0], t, comps)); hit = bx < T
            pc += 1; mc += not hit; best_x2.append(bx)
            if len(comps) == 10:
                p10 += 1; m10 += not hit
        cells.append((pc, mc, p10, m10))
    return fname, cells, undecided, node_only, removed, best_x2, perr, dup, (det if det is not None else 0.0)


def q(xs):
    if not xs: return {}
    s = sorted(xs); n = len(s)
    return {k: round(s[min(n - 1, int(p * (n - 1) + 0.5))], 6) for k, p in (("q50", .5), ("q90", .9), ("q99", .99), ("q999", .999), ("max", 1.0))}


def cp_upper(k, n, conf=0.975):
    from scipy.stats import beta
    return 1.0 if k >= n else float(beta.ppf(conf, k + 1, n - k))


def boot_upper(cells, B=BOOT, seed=20261030):
    """the 97.5% quantile of the miss rate under resampling the cells with replacement (the design effect)"""
    import numpy as np
    c = np.array([(p, m) for p, m, _, _ in cells if p], float)
    if not len(c): return None
    rng = np.random.default_rng(seed); out = []
    for _ in range(B):
        s = c[rng.integers(0, len(c), len(c))]; out.append(s[:, 1].sum() / s[:, 0].sum())
    return float(np.quantile(out, 0.975))


def main(d, man, expected, out, workers="8"):
    d = pathlib.Path(d)
    sys.path.insert(0, str(GEN))
    from guard import require_pushed_manifest
    require_pushed_manifest(man, expected)                               # the fifth review's B2: pushed, or refused
    ok, msg = manifest_ok(d, man, expected)
    if not ok: sys.exit("refused: " + msg)
    names = sorted(p.name for p in d.glob("*.jsonl.gz"))
    with Pool(int(workers)) as P:
        res = list(P.imap_unordered(task, [(n, str(d)) for n in names], chunksize=1))
    cells = [c for r in res for c in r[1]]
    planted = sum(c[0] for c in cells); miss = sum(c[1] for c in cells)
    p10 = sum(c[2] for c in cells); m10 = sum(c[3] for c in cells)
    allerr = [e for r in res for k in range(10) for e in r[6][k]]
    cpu = cp_upper(miss, planted) if planted else None; bu = boot_upper(cells)
    rep = {"manifest": msg, "files": len(res), "cells_checked": len(cells),
           "planted_worlds": planted, "missed": miss, "miss_rate": (miss / planted) if planted else None,
           "miss_rate_cp_upper": cpu, "miss_rate_bootstrap_upper": bu, "gate_miss": GATE_MISS,
           "readout_ten_output_worlds": p10, "readout_ten_output_missed": m10,
           "readout_ten_output_miss_rate": (m10 / p10) if p10 else None,
           "undecided_searches": sum(r[2] for r in res), "node_only_owners": sum(r[3] for r in res),
           "outputs_removed_by_the_floor": sum(r[4] for r in res),
           "planted_best_chi2_quantiles": q([x for r in res for x in r[5]]),
           "determinism_max_log10": max(r[8] for r in res), "a0_vs_F_minus2_max_log10": max(r[7] for r in res),
           "readout_pointwise_log10_all": q(allerr), "readout_tolerance_log10": round(TOL_LOG10, 5),
           "readout_fraction_above_tolerance": (sum(e > TOL_LOG10 for e in allerr) / len(allerr)) if allerr else None,
           "readout_pointwise_log10_by_output": {NAMES[k]: q([e for r in res for e in r[6][k]]) for k in range(10)},
           "readout_fraction_above_tolerance_by_output": {NAMES[k]: (lambda es: (sum(e > TOL_LOG10 for e in es) / len(es)) if es else None)(
               [e for r in res for e in r[6][k]]) for k in range(10)}}
    upper = max(x for x in (cpu, bu) if x is not None) if planted else None
    rep["gate_upper"] = upper
    rep["gate"] = "PASS" if (planted and upper <= GATE_MISS and rep["determinism_max_log10"] <= 1e-9
                             and rep["a0_vs_F_minus2_max_log10"] <= 1e-6) else "FAIL"
    pathlib.Path(out).write_text(json.dumps(rep, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(rep, indent=1))
    if rep["gate"] != "PASS":
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) not in (5, 6): sys.exit(__doc__)
    main(*sys.argv[1:])
