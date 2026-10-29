#!/usr/bin/env python3
"""W178 — the six's exponents at the cusp, exactly (the rule: W178_RULE.md, committed and pushed before this script).
It runs once, from the repository root, on four worker processes.

W174's frame six (B1656's frame as W162's point computes it: own residues, the kernel norms, the Higgs DR, the readings
(S~, S, S), L_max held at its Im tau = 4 value, the weighted M, W93's coupling, the singular values) on every one of the
266 census lines at Re tau 1/8 and 3/8, with every piece in working precision and the norms by W177's closed series:
  the tie     Im tau 3, 4, 5, 6 with the record's residue cut, against W174's stored six
  the ladder  Im tau 6, 8, 12, 16, 24, 32, 48 without the cut (the rule's one change)
Each point at two precisions p1 = 40 + ceil(8 pi y / ln 10) and p2 = p1 + 60 digits: a feature is resolved when the two
agree within 1e-6, zero at working precision when it lies within 30 digits of both floors, and otherwise the point is
repeated once at twice the digits; a feature still neither is unresolved.

  T0  the tie: every feature W174 stored above ln 1e-8 agrees within 1e-6
  T1  convergence: |e(32,48) - e(24,32)| <= 0.005 for all six, and the two Re tau within 0.005
  T2  W174's S1 on the cusp patterns e(32,48): no line passes at either Re tau
  R   read-outs

    python3 -B docs/dossiers/the_weave_2026-10-07/the_six_at_the_cusp.py

Fixed for the second launch (2026-10-29; the_six_at_the_cusp_first_launch_failed.txt).  The first launch ran to its
end with 258 failed tasks, all on the ladder (no cut) and all on the 20 lines of order dividing 6, where 3w is a
half-period and so ub lies on the zero of one theta_s.  There the channel's residue vanishes identically and its kernel
norm is undefined; the script still computed the norm, which divided by zero where the zero was hit exactly (and, where
rounding left it tiny, would give a huge norm times a tiny residue).  Its cells were not read.  Two changes, nothing
else: (1) a channel whose theta_s(ub) vanishes identically, decided exactly from the line's fractions, gets u_s = 0,
as the record's cut and W177's grid already treat it, and is counted per task; (2) failed tasks' tracebacks are written
with the repository and library paths removed.
"""
import contextlib
import io
import json
import math
import re
import multiprocessing as mpc
import platform
import sys
import time
import traceback
import warnings
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_census_window as W162            # noqa: E402  (W162: the frame's point; T8, W58 under it)
    import the_skeleton_census as W174          # noqa: E402  (W174: the skeleton test, its stored six)
    import the_twisted_norms_closed as W177     # noqa: E402  (W177: the kernel norms' closed series)
    import the_twisted_half_bound_checked as W93    # noqa: E402  (W93: the residues' closed form, the coupling)
T8, W58 = W162.T8, W162.W58
mp = W177.mp
OUT = HERE / "the_six_at_the_cusp.json"
XS = (0.125, 0.375)
TIE = (3.0, 4.0, 5.0, 6.0)
LADDER = (6.0, 8.0, 12.0, 16.0, 24.0, 32.0, 48.0)
CUT = 1e-12
AGREE = 1e-6
TIE_TOL, TIE_FLOOR = 1e-6, math.log(1e-8)
CONV = 0.005
WORKERS = 4
READ = (("up", "St"), ("down", "S"), ("lep", "S"))
_G = {}


def precisions(y):
    p1 = 40 + math.ceil(8 * math.pi * y / math.log(10))
    return p1, p1 + 60


# ============================================================================================ the frame in mp
def DR_mp(t, p):
    """T8.higgs_DR's formula (R = (-th2^2, -th4^2, i th3^2)/(th2 th3 th4), DR = q dR/dq + E2 R/24), at p digits"""
    y = float(mp.im(t))
    kmax = int(math.ceil(math.sqrt((p + 10) * math.log(10) / (math.pi * y)))) + 3
    nmax = int(math.ceil((p + 10) * math.log(10) / (2 * math.pi * y))) + 3
    e = lambda m: mp.exp(1j * mp.pi * t * m)
    h = [mp.mpf(2 * n + 1) / 2 for n in range(-kmax, kmax)]
    n3 = range(-kmax, kmax + 1)
    th2, d2 = mp.fsum(e(x * x) for x in h), mp.fsum(x * x / 2 * e(x * x) for x in h)
    th3, d3 = mp.fsum(e(n * n) for n in n3), mp.fsum(mp.mpf(n * n) / 2 * e(n * n) for n in n3)
    th4, d4 = mp.fsum((-1) ** n * e(n * n) for n in n3), mp.fsum((-1) ** n * mp.mpf(n * n) / 2 * e(n * n) for n in n3)
    E2 = 1 - 24 * mp.fsum(n * e(2 * n) / (1 - e(2 * n)) for n in range(1, nmax))
    l2, l3, l4 = d2 / th2, d3 / th3, d4 / th4
    R = [-th2 / (th3 * th4), -th4 / (th2 * th3), 1j * th3 / (th2 * th4)]
    dlog = [l2 - l3 - l4, l4 - l2 - l3, l3 - l2 - l4]
    return [R[i] * dlog[i] + E2 * R[i] / 24 for i in range(3)]


def mat_conj(A):
    return mp.matrix([[mp.conj(A[m, n]) for n in range(A.cols)] for m in range(A.rows)])


def six_at(line, x, y, p, cut):
    """the six [ln(s2/s1), ln(s3/s1)] for up, down, leptons at tau = x + iy, p digits; cut: the record's |R_s| cut"""
    a, b = line
    with mp.workdps(p):
        CM, EPSM, _BLK, EM = W93.units("mp")
        t = mp.mpc(mp.mpf(x), mp.mpf(y))
        dr = DR_mp(t, p)
        S = dr[0] * CM["i"] + dr[1] * CM["j"] + dr[2] * CM["k"]
        reads = {"S": S, "St": EPSM * mat_conj(S) * EPSM.T}
        Lv = mp.mpf(W162.L_of(_G["col"], y, "L_max"))
        out, lnr, zeroed = [], [], 0
        for sec, rd in READ:
            qL, qR = T8.charges(W93, sec)
            R = W93.residues((a, -b), sec, t)
            k = T8.kappa(qL, qR, a, b, t)
            ub = (qL + qR) * (mp.mpf(a.numerator) / a.denominator * t + mp.mpf(b.numerator) / b.denominator)
            M = mp.zeros(2, 2)
            for s in T8.UNITS:
                if theta_zero(W89TH[s], line, qL + qR):
                    zeroed += 1
                    continue
                Rs = k * R[s]
                if cut and abs(Rs) <= CUT:
                    continue
                w = 2 * mp.pi * Lv + W177.c_series(W89TH[s], ub, t)
                if w > 0:
                    M += mp.sqrt(w) * Rs * EM[s]
            Y = W93.coupling_mp(reads[rd], M)
            sv = sorted((abs(v) for v in mp.svd_c(Y, compute_uv=False)), reverse=True)
            for j in (1, 2):
                r = sv[j] / sv[0] if sv[0] > 0 else mp.mpf(0)
                lnr.append(r)
        for r in lnr:
            out.append(float(mp.log(r)) if r > 0 else -math.inf)
        return out, [float(mp.log10(r)) if r > 0 else -math.inf for r in lnr], zeroed


W89TH = {"1": 1, "i": 2, "j": 4, "k": 3}
ZEROS = {1: (Fr(0), Fr(0)), 2: (Fr(1, 2), Fr(0)), 3: (Fr(1, 2), Fr(1, 2)), 4: (Fr(0), Fr(1, 2))}


def theta_zero(s, line, qsum):
    """theta_s(ub) vanishes identically: ub = qsum (a tau + b) lies on theta_s's zero modulo the lattice (exact)"""
    a, b = line
    return ((qsum * b) % 1, (qsum * a) % 1) == ZEROS[s]


def sanitize(text):
    text = text.replace(str(ROOT) + "/", "")
    return re.sub(r"/[^\s\"']*/(site|dist)-packages/", "<packages>/", text)


def point(task):
    """(k, x, y, cut) -> the six resolved by two precisions (doubled once if needed), with per-feature status"""
    k, x, y, cut = task
    line = _G["lines"][k]
    t0 = time.time()
    try:
        p1, p2 = precisions(y)
        status = None
        for attempt in (1, 2):
            f1, l1, zeroed = six_at(line, x, y, p1, cut)
            f2, l2, _z = six_at(line, x, y, p2, cut)
            status = []
            for i in range(6):
                if math.isfinite(f1[i]) and math.isfinite(f2[i]) and abs(f1[i] - f2[i]) <= AGREE:
                    status.append("resolved")
                elif l1[i] <= -(p1 - 30) and l2[i] <= -(p2 - 30):      # at each precision's own floor
                    status.append("zero at working precision")
                else:
                    status.append("unresolved")
            if all(s != "unresolved" for s in status) or attempt == 2:
                break
            p1, p2 = 2 * p1, 2 * p2
        six = [f2[i] if status[i] == "resolved" else None for i in range(6)]
        return {"k": k, "x": x, "y": y, "cut": cut, "six": six, "status": status, "digits": [p1, p2],
                "theta-zero channels": zeroed, "seconds": round(time.time() - t0, 2)}
    except Exception:  # noqa: BLE001  (a failed task is kept and disclosed)
        return {"k": k, "x": x, "y": y, "cut": cut, "failed": sanitize(traceback.format_exc()[-1500:])}


def _init(root_str):
    root = Path(root_str)
    files = {p: T8.git_bytes(root, W58.REV, p) for p in W58.FILES}
    _G.update(col=T8.L_column(files), lines=T8.own_lines())


# ============================================================================================ read-outs per line
def slowest_rate(line):
    """per line: the least min(l+, l-) over the kernels of the three sectors (0 for an integer lambda), at Re tau 1/8"""
    a, b = line
    with mp.workdps(30):
        t = mp.mpc(mp.mpf(1) / 8, 6)
        best = None
        for sec, _rd in READ:
            qL, qR = T8.charges(W93, sec)
            ub = (qL + qR) * (mp.mpf(a.numerator) / a.denominator * t + mp.mpf(b.numerator) / b.denominator)
            for s in (1, 2, 3, 4):
                lam, _w = W177.lam_w(s, ub, t)
                lp = lam - mp.floor(lam)
                v = float(min(lp, 1 - lp)) if abs(lp) > 1e-20 and abs(lp - 1) > 1e-20 else 0.0
                best = v if best is None else min(best, v)
        return best


def run(out, pool):
    lines = T8.own_lines()
    files = {p: T8.git_bytes(ROOT, W58.REV, p) for p in W58.FILES}
    d = np.array(T8.targets(files)[0], dtype=float)
    stored = json.loads((HERE / "the_skeleton_census.json").read_text(encoding="utf-8"))
    unconv = {tuple(v) for v in stored["S0"]["unconverged lines"]}
    tasks = [(k, x, y, False) for y in sorted(LADDER, reverse=True) for k in range(len(lines)) for x in XS]
    tasks += [(k, x, y, True) for y in TIE for k in range(len(lines)) for x in XS]
    t0 = time.time()
    res = {}
    for j, r in enumerate(pool.imap_unordered(point, tasks, chunksize=1)):
        res[(r["k"], r["x"], r["y"], r["cut"])] = r
        if j % 500 == 0:
            print(f"point {j + 1}/{len(tasks)} at {time.time() - t0:.0f} s", flush=True)
    out["tasks"] = len(tasks)
    out["failed tasks"] = [[r["k"], r["x"], r["y"], r["cut"], r["failed"]] for r in res.values() if "failed" in r][:20]
    out["failed task count"] = sum(1 for r in res.values() if "failed" in r)
    out["theta-zero channels skipped (tasks with any, lines)"] = [
        sum(1 for r in res.values() if r.get("theta-zero channels")),
        len({r["k"] for r in res.values() if r.get("theta-zero channels")})]
    out["doubled-precision tasks"] = sum(1 for r in res.values()
                                         if "digits" in r and r["digits"][0] > precisions(r["y"])[0])
    # ---------------------------------------------------------------- T0: the tie
    worst, compared, misses = 0.0, 0, []
    for k, (a, b) in enumerate(lines):
        e = stored["per line"][k]
        assert e["line"] == [str(a), str(b)]
        for j, x in enumerate(XS):
            sp = e["per Re tau"][j]
            if sp.get("failed"):
                continue
            for y in TIE:
                r = res[(k, x, y, True)]
                if "failed" in r:
                    misses.append([str(a), str(b), x, y, "task failed"])
                    continue
                for i, v in enumerate(sp["six per height"][str(y)]):
                    if v > TIE_FLOOR:
                        compared += 1
                        if r["six"][i] is None:
                            misses.append([str(a), str(b), x, y, i, "not resolved here"])
                            continue
                        dv = abs(r["six"][i] - v)
                        worst = max(worst, dv)
                        if dv > TIE_TOL:
                            misses.append([str(a), str(b), x, y, i, dv])
    out["T0"] = {"features compared": compared, "worst |difference| in ln": worst, "misses": misses[:30],
                 "miss count": len(misses), "holds": bool(compared > 0 and not misses)}
    # ---------------------------------------------------------------- per line: the ladder, exponents, limits
    per, conv_rows, n_inf = [], [], {}
    for k, (a, b) in enumerate(lines):
        entry = {"line": [str(a), str(b)], "W174 S0": ("unconverged" if (str(a), str(b)) in unconv else "other"),
                 "slowest kernel min(l+, l-)": slowest_rate((a, b)), "per Re tau": []}
        for x in XS:
            rows = {y: res[(k, x, y, False)] for y in LADDER}
            pr = {"x": x}
            if any("failed" in r for r in rows.values()):
                pr["failed"] = True
                entry["per Re tau"].append(pr)
                continue
            pr["six per height"] = {str(y): rows[y]["six"] for y in LADDER}
            pr["status per height"] = {str(y): rows[y]["status"] for y in LADDER}
            zero = any(s == "zero at working precision" for r in rows.values() for s in r["status"])
            unres = any(s == "unresolved" for r in rows.values() for s in r["status"])
            pr["zero channel"], pr["unresolved feature"] = zero, unres
            if not zero and not unres:
                ex = {}
                for y1, y2 in zip(LADDER[:-1], LADDER[1:]):
                    ex[f"{y1:g},{y2:g}"] = [-(rows[y2]["six"][i] - rows[y1]["six"][i]) / (2 * math.pi * (y2 - y1))
                                           for i in range(6)]
                pr["local exponents"] = ex
                pr["cusp pattern e(32,48)"] = ex["32,48"]
                pr["|e(32,48) - e(24,32)| max"] = max(abs(u - v) for u, v in zip(ex["32,48"], ex["24,32"]))
                pr["intercepts at 48"] = [rows[48.0]["six"][i] + 2 * math.pi * 48 * ex["32,48"][i] for i in range(6)]
                n_inf[(k, x)] = ex["32,48"]
                w174 = stored["per line"][k]["per Re tau"][XS.index(x)].get("pattern n_i")
                if w174 and all(v is not None for v in w174):
                    pr["W174 pattern minus cusp pattern max"] = max(abs(u - v) for u, v in zip(w174, ex["32,48"]))
            entry["per Re tau"].append(pr)
        if all("cusp pattern e(32,48)" in p for p in entry["per Re tau"]):
            c1 = max(p["|e(32,48) - e(24,32)| max"] for p in entry["per Re tau"])
            c2 = max(abs(u - v) for u, v in zip(entry["per Re tau"][0]["cusp pattern e(32,48)"],
                                                entry["per Re tau"][1]["cusp pattern e(32,48)"]))
            entry["converged"] = bool(c1 <= CONV and c2 <= CONV)
            conv_rows.append((entry["line"], c1, c2, entry["converged"]))
        per.append(entry)
    out["per line"] = per
    nz = sum(1 for e in per if any(p.get("zero channel") for p in e["per Re tau"]))
    nu = sum(1 for e in per if any(p.get("unresolved feature") for p in e["per Re tau"]))
    out["T1"] = {"lines with every feature resolved at both Re tau": len(conv_rows),
                 "lines with a zero channel": nz, "lines with an unresolved feature": nu,
                 "converged": sum(1 for v in conv_rows if v[3]),
                 "not converged (line, max |e(32,48) - e(24,32)|, Re tau spread)":
                     [[v[0], v[1], v[2]] for v in conv_rows if not v[3]],
                 "holds": bool(conv_rows and all(v[3] for v in conv_rows))}
    # ---------------------------------------------------------------- T2: W174's S1 on the cusp patterns
    passing, near = [], []
    for (k, x), n in n_inf.items():
        iv = W174.interval(d, n)
        ex, s = W174.excess(d, W174.model_lin(n))
        near.append((ex, [str(v) for v in lines[k]], x, s))
        if iv:
            passing.append([[str(v) for v in lines[k]], x, list(iv), [-iv[1] / (2 * math.pi), -iv[0] / (2 * math.pi)]])
    near.sort(key=lambda v: v[0])
    out["T2"] = {"patterns tested": len(n_inf), "passing (line, Re tau, s interval, Im tau interval)": passing,
                 "closest ten (excess over ln 3, line, Re tau, s)": [list(v) for v in near[:10]],
                 "holds": bool(n_inf and not passing)}
    # ---------------------------------------------------------------- R: the null on the cusp patterns (W174's draws)
    rng = np.random.default_rng(W174.SEED)
    draws = np.empty((W174.NULL_N, 6))
    for t in range(W174.NULL_N):
        while True:
            z = d + rng.uniform(-W174.NULL_W, W174.NULL_W, 6)
            if z[1] < z[0] and z[3] < z[2] and z[5] < z[4] and (z < 0).all():
                break
        draws[t] = z
    hit = np.zeros(W174.NULL_N, dtype=bool)
    for n in n_inf.values():
        n = np.asarray(n, dtype=float)
        lo, hi, ok = np.full(W174.NULL_N, -np.inf), np.zeros(W174.NULL_N), np.ones(W174.NULL_N, dtype=bool)
        for i in range(6):
            if abs(n[i]) < 1e-12:
                ok &= np.abs(draws[:, i]) <= W174.LN3
                continue
            a_, b_ = (draws[:, i] - W174.LN3) / n[i], (draws[:, i] + W174.LN3) / n[i]
            lo, hi = np.maximum(lo, np.minimum(a_, b_)), np.minimum(hi, np.maximum(a_, b_))
        hit |= ok & (lo <= hi)
    out["R: null pass rate on the cusp patterns (W174's 20 000 draws)"] = float(hit.mean())
    # ---------------------------------------------------------------- R: the cut at 6; W174's S0 beside the rates
    diff6 = []
    for k in range(len(lines)):
        for x in XS:
            a_, b_ = res[(k, x, 6.0, True)], res[(k, x, 6.0, False)]
            if "failed" in a_ or "failed" in b_:
                continue
            for i in range(6):
                u, v = a_["six"][i], b_["six"][i]
                if u is not None and v is not None and abs(u - v) > 1e-6:
                    diff6.append([[str(z) for z in lines[k]], x, i, u, v])
    out["R: features changed at Im tau 6 by removing the cut (> 1e-6)"] = {"count": len(diff6), "first": diff6[:20]}
    out["R: W174's S0 beside the slowest kernel rate"] = sorted(
        [[e["line"], e["W174 S0"], e["slowest kernel min(l+, l-)"], e.get("converged")] for e in per],
        key=lambda v: (v[2], v[0]))
    big = []
    for e in per:
        for p in e["per Re tau"]:
            if "W174 pattern minus cusp pattern max" in p and p["W174 pattern minus cusp pattern max"] > 0.02:
                big.append([e["line"], p["x"], p["W174 pattern minus cusp pattern max"]])
    out["R: lines where W174's pattern differs from the cusp pattern by more than 0.02"] = {"count": len(big),
                                                                                            "rows": big}
    out["cells"] = {k: out[k]["holds"] for k in ("T0", "T1", "T2")}


def main():
    t0 = time.time()
    out = {"arc": "W178", "rule": "W178_RULE.md", "python": platform.python_version(), "mpmath": mp.__version__,
           "numpy": np.__version__, "workers": WORKERS, "ladder": list(LADDER), "tie heights": list(TIE)}
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        try:
            with mpc.get_context("fork").Pool(WORKERS, initializer=_init, initargs=(str(ROOT),)) as pool:
                run(out, pool)
        except Exception:  # noqa: BLE001  (a failed run still writes what it has)
            out["run_failed"] = sanitize(traceback.format_exc()[-3000:])
    out["warnings"] = sorted({f"{w.category.__name__}: {w.message}" for w in caught})
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name, "in", out["seconds"], "s;", len(out["warnings"]), "distinct warnings")


if __name__ == "__main__":
    main()
