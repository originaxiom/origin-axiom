#!/usr/bin/env python3
"""W182 — the down–lepton factor on the centre lines, main's P-567 Q1 (the rule: W182_RULE.md, committed and pushed
before this script).  It runs once, from the repository root, on four worker processes.

B1656's frame as W178 computes it (its point function unchanged: W177's norms, no cut, the theta-zero rule, its two
precisions and status rule), on the 90 lines (2/5 + j/3 mod 1, k/30), j in {0, 1, 2}, k in {0, ..., 29}; W179's
double ratios ln r2 = f3 - f5, ln r1 = f4 - f6, ln D = ln r1 - ln r2:
  Part A  the cusp: W178's ladder Im tau 6-48 at Re tau 1/8 and 3/8; finite where the down and lepton exponents
          e(32, 48) agree within 0.005 for both features, read at Im tau 48; running elsewhere; excluded where a
          feature is zero or unresolved at some height or a point failed
  Part B  tau = i: W178's point function, and the absolute singular values of the down and lepton Yukawas (read-out)

  C0  the 10 census lines (2/5, m/10) tie W178's stored six (every height, both Re tau) and W179's six at i, 1e-6
  C1  |ln D| <= 1e-8 on the five order-5 lines at every height, both Re tau and at i; > 1e-8 at i on each new line
  C2  on each of the 80 new lines, at both Re tau, the down and lepton exponents differ by more than 0.005
  C3  no line at a finite cusp limit or at i has both r2 and r1 within a factor 1.25 of (1/3, 3)
  C4  no finite cusp D and no D at i in the data's 3-sigma window
  R   read-outs

    python3 -B docs/dossiers/the_weave_2026-10-07/the_centre_lines.py

Disclosed: a timing call on this script, after the rule was pushed and before this commit, ran W178's point on line 40
((11/15, 1/3)) at Re tau 1/8, Im tau 48, and the absolute singular values at tau = i on the same line, and printed only
the statuses, digits and seconds (all resolved; 3.5 s and 0.4 s; no failure).  No value was printed or read.
"""
import contextlib
import io
import json
import math
import multiprocessing as mpc
import platform
import sys
import time
import traceback
import warnings
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_six_at_the_cusp as W178          # noqa: E402  (W178: the frame, its point function, its output)
T8, W93, W162, W177, W58 = W178.T8, W178.W93, W178.W162, W178.W177, W178.W58
mp = W177.mp
OUT = HERE / "the_centre_lines.json"
LADDER = W178.LADDER
XS = W178.XS
AGREE = 0.005
CONV = 1e-3
TIE = 1e-8
TOL = 1e-6
SIGMAS = 3
FACTOR = 1.25
NEAR = 1.1
GJ = (1 / 3, 3.0)
WORKERS = 4
DOWN2, DOWN1, LEP2, LEP1 = 2, 3, 4, 5
CENTRE = [((Fr(2, 5) + Fr(j, 3)) % 1, Fr(k, 30)) for j in range(3) for k in range(30)]


def order(line):
    return math.lcm(line[0].denominator, line[1].denominator)


def tie_law(line):
    """the lepton's (q_L - q_R) w = -9w equals +-(the down's -w) modulo the lattice: 8w or 10w in the lattice"""
    a, b = line
    return any((n * a) % 1 == 0 and (n * b) % 1 == 0 for n in (8, 10))


def _init(root_str):
    W178._init(root_str)
    W178._G["lines"] = list(CENTRE)


def doubles(six):
    if six is None or any(six[i] is None for i in (DOWN2, DOWN1, LEP2, LEP1)):
        return None
    l2, l1 = six[DOWN2] - six[LEP2], six[DOWN1] - six[LEP1]
    return [l2, l1, l1 - l2]


# ============================================================================================ absolute values at i
def svs_at(line, x, y, p):
    """W178's six_at (no cut), returning the down and lepton Yukawas' singular values (descending), at p digits"""
    a, b = line
    with mp.workdps(p):
        CM, EPSM, _BLK, EM = W93.units("mp")
        t = mp.mpc(mp.mpf(x), mp.mpf(y))
        dr = W178.DR_mp(t, p)
        S = dr[0] * CM["i"] + dr[1] * CM["j"] + dr[2] * CM["k"]
        reads = {"S": S, "St": EPSM * W178.mat_conj(S) * EPSM.T}
        Lv = mp.mpf(W162.L_of(W178._G["col"], y, "L_max"))
        out = {}
        for sec, rd in W178.READ:
            if sec == "up":
                continue
            qL, qR = T8.charges(W93, sec)
            R = W93.residues((a, -b), sec, t)
            k = T8.kappa(qL, qR, a, b, t)
            ub = (qL + qR) * (mp.mpf(a.numerator) / a.denominator * t + mp.mpf(b.numerator) / b.denominator)
            M = mp.zeros(2, 2)
            for s in T8.UNITS:
                if W178.theta_zero(W178.W89TH[s], line, qL + qR):
                    continue
                w = 2 * mp.pi * Lv + W177.c_series(W178.W89TH[s], ub, t)
                if w > 0:
                    M += mp.sqrt(w) * k * R[s] * EM[s]
            Y = W93.coupling_mp(reads[rd], M)
            sv = sorted((abs(v) for v in mp.svd_c(Y, compute_uv=False)), reverse=True)
            out[sec] = [float(mp.log(v)) if v > 0 else -math.inf for v in sv]
        return out


def abs_point(k):
    """k -> ln sigma_g(e) - ln sigma_g(d), g = 3, 2, 1 (heaviest first), at tau = i, by two precisions"""
    line = W178._G["lines"][k]
    try:
        p1, p2 = W178.precisions(1.0)
        a1, a2 = svs_at(line, 0.0, 1.0, p1), svs_at(line, 0.0, 1.0, p2)
        r1 = [e - d for e, d in zip(a1["lep"], a1["down"])]
        r2 = [e - d for e, d in zip(a2["lep"], a2["down"])]
        ok = [math.isfinite(u) and math.isfinite(v) and abs(u - v) <= W178.AGREE for u, v in zip(r1, r2)]
        return {"k": k, "ln sigma_g(e)/sigma_g(d)": [v if o else None for v, o in zip(r2, ok)],
                "ln sigma (down, lepton)": [a2["down"], a2["lep"]]}
    except Exception:  # noqa: BLE001  (a failed task is kept and disclosed)
        return {"k": k, "failed": W178.sanitize(traceback.format_exc()[-1500:])}


def run_task(task):
    if task[0] == "abs":
        return ("abs", task[1], abs_point(task[1]))
    return ("pt", task[1], W178.point(task[1]))


# ============================================================================================ the analysis
def gj_near(v):
    return v is not None and abs(v[0] - math.log(GJ[0])) <= math.log(FACTOR) and \
        abs(v[1] - math.log(GJ[1])) <= math.log(FACTOR)


def single_near(lnv):
    return lnv is not None and min(abs(lnv - math.log(3)), abs(lnv + math.log(3))) <= math.log(NEAR)


def run(out, pool):
    lines = list(CENTRE)
    ords = sorted({order(l) for l in lines})
    out["lines"] = {"count": len(lines), "census (tie-law) lines": sum(tie_law(l) for l in lines),
                    "orders": {str(n): sum(1 for l in lines if order(l) == n) for n in ords}}
    tasks = [("pt", (k, x, y, False)) for k in range(len(lines)) for x in XS for y in LADDER]
    tasks += [("pt", (k, 0.0, 1.0, False)) for k in range(len(lines))]
    tasks += [("abs", k) for k in range(len(lines))]
    tasks.sort(key=lambda q: -(q[1][2] if q[0] == "pt" else 0.5))
    out["tasks"] = len(tasks)
    t0 = time.time()
    pts, absr, n = {}, {}, 0
    for kind, key, r in pool.imap_unordered(run_task, tasks, chunksize=1):
        if kind == "pt":
            pts[(key[0], key[1], key[2])] = r
        else:
            absr[key] = r
        n += 1
        if n % 100 == 1:
            print(f"task {n}/{len(tasks)} at {round(time.time() - t0)} s", flush=True)
    out["compute seconds"] = round(time.time() - t0, 1)
    out["failed tasks"] = [[str(k)] + [r["failed"]] for k, r in list(pts.items()) + list(absr.items()) if "failed" in r]
    out["doubled-precision tasks"] = sum(1 for r in pts.values() if "digits" in r
                                         and r["digits"][0] > W178.precisions(r["y"])[0])
    files = {p: T8.git_bytes(ROOT, W58.REV, p) for p in W58.FILES}
    t6 = T8.targets(files)[0]
    ahs = json.loads((HERE / "received" / "AHS2026_double_ratio.json").read_text(encoding="utf-8"))["the double ratio"]
    data = {"ln r2": float(t6[DOWN2] - t6[LEP2]), "ln r1": float(t6[DOWN1] - t6[LEP1]),
            "D": float(ahs["value"]), "sigma D": float(ahs["sigma"])}
    data["ln D"] = math.log(data["D"])
    out["the data (read once)"] = data
    lo, hi = data["D"] - SIGMAS * data["sigma D"], data["D"] + SIGMAS * data["sigma D"]
    w178 = json.loads((HERE / "the_six_at_the_cusp.json").read_text(encoding="utf-8"))
    w179 = json.loads((HERE / "the_down_lepton_factor.json").read_text(encoding="utf-8"))
    s178 = {tuple(e["line"]): e for e in w178["per line"]}
    s179 = {tuple(e["line"]): e for e in w179["per line"]}
    six = lambda k, x, y: pts.get((k, x, y), {}).get("six")
    per, c0_bad, c1_bad, c2_bad, c3_hits, c4_hits, singles, conv_bad = ([] for _ in range(8))
    c0_n = 0
    counts = {"cusp finite": 0, "cusp running": 0, "cusp excluded": 0, "i finite": 0, "i excluded": 0}
    vals_i, vals_cusp = [], []
    for k, line in enumerate(lines):
        key = (str(line[0]), str(line[1]))
        N = order(line)
        new = not tie_law(line)
        entry = {"line": list(key), "order": N, "new": new, "cusp": [], "at i": None}
        # C0 on the census lines
        if not new:
            e178 = s178[key]
            for xi, x in enumerate(XS):
                sp = e178["per Re tau"][xi]
                for y in LADDER:
                    mine, stored = six(k, x, y), sp["six per height"][str(y)]
                    if mine is None:
                        c0_bad.append([list(key), x, y, "no six"])
                        continue
                    for u, v in zip(mine, stored):
                        if u is not None and v is not None:
                            c0_n += 1
                            if abs(u - v) > TOL:
                                c0_bad.append([list(key), x, y, abs(u - v)])
            si = s179[key]["at i"].get("six")
            mine = six(k, 0.0, 1.0)
            if si is not None and mine is not None:
                for u, v in zip(mine, si):
                    if u is not None and v is not None:
                        c0_n += 1
                        if abs(u - v) > TOL:
                            c0_bad.append([list(key), "i", abs(u - v)])
        # Part A: the cusp
        for x in XS:
            rows = {y: pts.get((k, x, y), {}) for y in LADDER}
            row = {"x": x}
            if any("failed" in r for r in rows.values()) or any(
                    s != "resolved" for r in rows.values() for s in r.get("status", ["failed"])):
                row["status"] = "excluded"
                row["why"] = ("failed point" if any("failed" in r for r in rows.values()) else
                              "zero or unresolved feature")
                counts["cusp excluded"] += 1
                if new:
                    c2_bad.append([list(key), x, "excluded"])
                entry["cusp"].append(row)
                continue
            lad = {y: doubles(rows[y]["six"]) for y in LADDER}
            row["ln (r2, r1, D) per height"] = {str(y): v for y, v in lad.items()}
            ex = [-(rows[48.0]["six"][i] - rows[32.0]["six"][i]) / (2 * math.pi * 16) for i in range(6)]
            row["exponents e(32,48)"] = ex
            dif = [ex[DOWN2] - ex[LEP2], ex[DOWN1] - ex[LEP1]]
            row["down minus lepton exponent (m2, m1)"] = dif
            agree = abs(dif[0]) <= AGREE and abs(dif[1]) <= AGREE
            if N == 5:
                worst = max(abs(v[2]) for v in lad.values())
                row["tie |ln D| max over heights"] = worst
                if worst > TIE:
                    c1_bad.append([list(key), x, "ladder", worst])
            if agree:
                v48, v32 = lad[48.0], lad[32.0]
                row["status"] = "finite"
                row["cusp ln (r2, r1, D)"] = v48
                row["change 32 to 48"] = [abs(a - b) for a, b in zip(v48, v32)]
                counts["cusp finite"] += 1
                if max(row["change 32 to 48"]) > CONV:
                    conv_bad.append([list(key), x, max(row["change 32 to 48"])])
                vals_cusp.append((list(key), x, v48))
                if new:
                    c2_bad.append([list(key), x, "exponents agree", dif])
                if gj_near(v48):
                    c3_hits.append([list(key), x, "cusp", v48])
                if lo <= math.exp(v48[2]) <= hi:
                    c4_hits.append([list(key), x, "cusp", math.exp(v48[2])])
                for j, nm in ((0, "r2"), (1, "r1")):
                    if single_near(v48[j]):
                        singles.append([list(key), x, "cusp", nm, math.exp(v48[j])])
            else:
                row["status"] = "running"
                counts["cusp running"] += 1
            entry["cusp"].append(row)
        # Part B: tau = i
        r = pts.get((k, 0.0, 1.0), {})
        v = doubles(r.get("six")) if "six" in r else None
        ai = {"status": r.get("status"), "six": r.get("six"), "ln (r2, r1, D)": v}
        a_r = absr.get(k, {})
        ai["ln sigma_g(e)/sigma_g(d), g = 3, 2, 1"] = a_r.get("ln sigma_g(e)/sigma_g(d)")
        if v is None:
            counts["i excluded"] += 1
            if new:
                c1_bad.append([list(key), "i", "excluded"])
            if N == 5:
                c1_bad.append([list(key), "i", "excluded"])
        else:
            counts["i finite"] += 1
            vals_i.append((list(key), v))
            if N == 5 and abs(v[2]) > TIE:
                c1_bad.append([list(key), "i", abs(v[2])])
            if new and abs(v[2]) <= TIE:
                c1_bad.append([list(key), "i", "ties", abs(v[2])])
            if gj_near(v):
                c3_hits.append([list(key), "i", v])
            if lo <= math.exp(v[2]) <= hi:
                c4_hits.append([list(key), "i", math.exp(v[2])])
            for j, nm in ((0, "r2"), (1, "r1")):
                if single_near(v[j]):
                    singles.append([list(key), "i", nm, math.exp(v[j])])
        for g, lv in zip((3, 2, 1), ai["ln sigma_g(e)/sigma_g(d), g = 3, 2, 1"] or []):
            if single_near(lv):
                singles.append([list(key), "i", f"sigma_{g}(e)/sigma_{g}(d)", math.exp(lv)])
        entry["at i"] = ai
        per.append(entry)
    out["per line"] = per
    out["counts"] = counts
    out["C0"] = {"features compared": c0_n, "misses": c0_bad, "holds": bool(c0_n and not c0_bad)}
    out["C1"] = {"misses": c1_bad, "holds": bool(not c1_bad)}
    out["C2"] = {"new pairs": 2 * sum(1 for l in lines if not tie_law(l)), "misses": c2_bad, "holds": bool(not c2_bad)}
    out["C3"] = {"factor": FACTOR, "target (r2, r1)": list(GJ), "hits": c3_hits, "holds": bool(not c3_hits)}
    out["C4"] = {"window": [lo, hi], "hits": c4_hits, "holds": bool(not c4_hits)}
    out["R: finite cusp limits whose change 32 to 48 exceeds 1e-3"] = conv_bad
    out["R: single factors within 1.1 of 3 or 1/3"] = singles
    out["R: distinct D at i (to 1e-6)"] = sorted({round(math.exp(v[2]), 6) for _l, v in vals_i})
    out["R: distinct finite cusp D (to 1e-6)"] = sorted({round(math.exp(v[2]), 6) for _l, _x, v in vals_cusp})
    pts_all = [(l, "i", v) for l, v in vals_i] + [(l, x, v) for l, x, v in vals_cusp]
    dist = lambda v, t: math.hypot(v[0] - math.log(t[0]), v[1] - math.log(t[1]))
    out["R: ten nearest to (1/3, 3)"] = [[l, p, math.exp(v[0]), math.exp(v[1]), math.exp(v[2])] for l, p, v in
                                         sorted(pts_all, key=lambda q: dist(q[2], GJ))[:10]]
    td = (math.exp(data["ln r2"]), math.exp(data["ln r1"]))
    out["R: ten nearest to the data's (r2, r1)"] = [[l, p, math.exp(v[0]), math.exp(v[1]), math.exp(v[2])]
                                                     for l, p, v in sorted(pts_all, key=lambda q: dist(q[2], td))[:10]]
    out["R: ten nearest to the data's D"] = [[l, p, math.exp(v[2])] for l, p, v in
                                             sorted(pts_all, key=lambda q: abs(q[2][2] - data["ln D"]))[:10]]
    out["cells"] = {c: out[c]["holds"] for c in ("C0", "C1", "C2", "C3", "C4")}


def main():
    t0 = time.time()
    out = {"arc": "W182", "rule": "W182_RULE.md", "python": platform.python_version(), "workers": WORKERS,
           "frame": "W178's (the_six_at_the_cusp.py), its point function unchanged, on P-567's centre lines"}
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        try:
            with mpc.get_context("fork").Pool(WORKERS, initializer=_init, initargs=(str(ROOT),)) as pool:
                _init(str(ROOT))
                run(out, pool)
        except Exception:  # noqa: BLE001  (a failed run still writes what it has)
            out["run_failed"] = W178.sanitize(traceback.format_exc()[-3000:])
    out["warnings"] = sorted({f"{w.category.__name__}: {w.message}" for w in caught})
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name, "in", out["seconds"], "s;", len(out["warnings"]), "distinct warnings")


if __name__ == "__main__":
    main()
