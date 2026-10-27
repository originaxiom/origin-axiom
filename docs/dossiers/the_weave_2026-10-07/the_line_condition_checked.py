#!/usr/bin/env python3
"""W160 — the plan's stage 1, first part: the agy branch's line selection (B1761) and sector-blind norm (B1759) on
this seat's own code (the rule: W160_RULE.md, committed and pushed before this script).  It runs once, from the
repository root.  No data are read.

  L0  the instrument: the own line lists against B1726's and B1755's; own residues against main's at the probe
  L1  the zero law: R_i^up = 0 exactly where 5w or 3w is the half-period 1/2, R_i^down where 3w or w is, at four points
  L2  C1's survivors: the 10 lines (1/5, odd/10) and (2/5, odd/10) with B1761's clauses, 12 without a not in {0, 1/2}
  L3  the cutoff as an exponent law: I = 2 eps / (1 + eps^2), eps = exp(-pi (1 - 2 ||3a||) Im tau); 2/5 below 1/5
  L4  B1759 on own code: c_s(-3w) = c_s(3w)
  R   read-outs

The residues are W89's, R_s = c_s theta_s(pi ub) theta_s(pi dl) with ub = (qL + qR) w, dl = (qL - qR) w and
w = a tau + b (B1726's and B1761's convention), at 60 digits from W85's series.  Main's B1656 functions, its B1726 and
its B1755 census modules are read at REV into a temporary tree for L0 only.

    python3 -B docs/dossiers/the_weave_2026-10-07/the_line_condition_checked.py
"""
import contextlib
import hashlib
import importlib.util
import io
import json
import math
import platform
import subprocess
import sys
import tempfile
import time
import traceback
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_electrons_zero_checked as W89      # noqa: E402  (W89's residues and norms; W85's thetas under it)

mp.mp.dps = 60
REV = "3b9dda20d"                                   # origin/main as read for the rule
MAIN = {"funcs": "frontier/B1723_the_golden_valley/verification/b1656_funcs.py",
        "c26": "frontier/B1726_the_two_ingredients_replicated/verification/census.py",
        "c55": "frontier/B1755_the_six_on_the_lines_of_order_13_to_20/verification/census.py"}
OUT = HERE / "the_line_condition_checked.json"
RUNTXT = HERE / "the_line_condition_checked_run.txt"
PROBE = complex(0.3145, 3.0345)
POINTS = [PROBE, complex(0.13, 1.07), complex(0.05, 2.05), complex(0.85, 3.45), complex(0.5, 6.0)]
SECT = {"up": (1, -4), "down": (1, 2), "lep": (-3, 6)}
UNITS = ["1", "i", "j", "k"]
TH = W89.TH
ZERO = mp.mpf(10) ** -40
NONZERO = mp.mpf(10) ** -25
HALF = Fr(1, 2)
ODD10 = [Fr(k, 10) for k in (1, 3, 5, 7, 9)]
C1_PRED = sorted([(Fr(1, 5), b) for b in ODD10] + [(Fr(2, 5), b) for b in ODD10])
C1_PRED_NOCLAUSE = sorted(C1_PRED + [(Fr(0), Fr(1, 10)), (Fr(0), Fr(3, 10))])
LOG = []


def say(*a):
    s = " ".join(str(x) for x in a)
    LOG.append(s)
    print(s, flush=True)


def key(p):
    return f"{p[0]},{p[1]}"


# ============================================================================================ lines and arithmetic
def own_lines(orders):
    seen, out = set(), []
    for N in orders:
        for j in range(N):
            for k in range(N):
                if math.gcd(math.gcd(j, k), N) != 1:
                    continue
                a, b = Fr(j, N), Fr(k, N)
                kk = min((a, b), ((-a) % 1, (-b) % 1))
                if kk in seen:
                    continue
                seen.add(kk)
                out.append(kk)
    return out


LINES266 = own_lines(range(1, 8)) + own_lines(range(8, 13))
LINES396 = own_lines((13, 14, 15, 20))
ALL = LINES266 + LINES396


def order(p):
    return math.lcm(p[0].denominator, p[1].denominator)


def is_half(k, p):
    """k w = 1/2 modulo Z + Z tau, for w = a tau + b"""
    return (k * p[0]).denominator == 1 and (k * p[1] - HALF).denominator == 1


def zero_i_up(p):
    return is_half(5, p) or is_half(3, p)


def zero_i_down(p):
    return is_half(3, p) or is_half(1, p)


def dist(x):
    x = Fr(x) % 1
    return min(x, 1 - x)


# ============================================================================================ own residues
def tau_mp(t):
    return mp.mpc(str(t.real), str(t.imag))


def w_of(p, tm):
    return mp.mpf(p[0].numerator) / p[0].denominator * tm + mp.mpf(p[1].numerator) / p[1].denominator


def own_R(p, t, sector):
    tm = tau_mp(t)
    qL, qR = SECT[sector]
    w = w_of(p, tm)
    return W89.residues(tm, (qL + qR) * w, (qL - qR) * w)


def rel(R, s):
    tot = mp.sqrt(mp.fsum(abs(R[u]) ** 2 for u in UNITS))
    return abs(R[s]) / tot


def invariant(R):
    v = [R[u] for u in ("i", "j", "k")]
    return float(abs(mp.fsum(z * z for z in v)) / mp.fsum(abs(z) ** 2 for z in v))


def jk_over_1(R):
    return float(mp.sqrt(abs(R["j"]) ** 2 + abs(R["k"]) ** 2) / abs(R["1"]))


def closed_I(p, y):
    eps = math.exp(-math.pi * (1 - 2 * float(dist(3 * p[0]))) * y)
    return 2 * eps / (1 + eps * eps)


# ============================================================================================ main's code, read at REV
def main_tree(tmp):
    hashes = {}
    for name, path in MAIN.items():
        blob = subprocess.run(["git", "-C", str(ROOT), "show", f"{REV}:{path}"], capture_output=True,
                              check=True).stdout
        dest = Path(tmp) / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(blob)
        hashes[path] = hashlib.sha256(blob).hexdigest()
    (Path(tmp) / "GENESIS.md").write_text("temporary tree for W160's instrument check\n", encoding="utf-8")
    return hashes


def load(name, path):
    sp = importlib.util.spec_from_file_location(name, str(path))
    m = importlib.util.module_from_spec(sp)
    sys.modules[name] = m
    argv = sys.argv
    sys.argv = ["x"]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            sp.loader.exec_module(m)
    finally:
        sys.argv = argv
    return m


# ============================================================================================ the parts
def part_L0(tmp):
    out = {"main files (sha256)": main_tree(tmp)}
    c26 = load("w160_c26", Path(tmp) / MAIN["c26"])
    c55 = load("w160_c55", Path(tmp) / MAIN["c55"])
    B = load("w160_funcs", Path(tmp) / MAIN["funcs"])
    mp.mp.dps = 60                                  # main's module sets 20 digits on import; own code runs at 60
    m266, m396 = list(c26.lines()), list(c55.lines())
    out["(i) lists"] = {"own 266": len(LINES266), "own 396": len(LINES396), "main 266": len(m266),
                        "main 396": len(m396), "266 equal in order": LINES266 == m266,
                        "396 equal in order": LINES396 == m396}
    sample = sorted(set(C1_PRED) | set(ALL[::33]), key=ALL.index)
    worst_spread, worst_zero, bad = 0.0, 0.0, []
    t = PROBE
    for p in sample:
        w = float(p[0]) * t + float(p[1])
        for sec, (qL, qR) in SECT.items():
            Ro = own_R(p, t, sec)
            x, y = B.sector_twists(w, t, qL, qR)
            Rm = B.residues(x, y, t)
            tot_m = math.sqrt(sum(abs(Rm[s]) ** 2 for s in UNITS))
            ratios = []
            for s in UNITS:
                r_own = rel(Ro, s)
                if r_own < ZERO:
                    worst_zero = max(worst_zero, abs(Rm[s]) / tot_m)
                elif r_own > mp.mpf(10) ** -12:
                    ratios.append(complex(Rm[s]) / complex(Ro[s]))
            if ratios:
                spread = max(abs(r / ratios[0] - 1) for r in ratios)
                worst_spread = max(worst_spread, spread)
                if spread > 1e-7:
                    bad.append([key(p), sec, spread])
    out["(ii) residues at the probe"] = {"lines sampled": len(sample), "worst ratio spread": worst_spread,
                                         "worst main |R_s|/|R| where own is zero": worst_zero, "failing": bad}
    out["holds"] = bool(out["(i) lists"]["266 equal in order"] and out["(i) lists"]["396 equal in order"]
                        and worst_spread < 1e-7 and worst_zero < 1e-9 and not bad)
    return out


def scan(t):
    """R_i^up, R_j^up and R_i^down (relative) on all 662 lines at t, on own code"""
    rows = {}
    for p in ALL:
        Ru, Rd = own_R(p, t, "up"), own_R(p, t, "down")
        rows[p] = {"iu": rel(Ru, "i"), "ju": rel(Ru, "j"), "id": rel(Rd, "i")}
    return rows


def part_L1_L2(scans):
    L1, L2 = {}, {}
    ok1, ok2 = True, True
    for tl, rows in scans.items():
        mism, between = [], []
        for p, r in rows.items():
            for lab, pred in (("iu", zero_i_up(p)), ("id", zero_i_down(p))):
                v = r[lab]
                if ZERO <= v <= NONZERO:
                    between.append([key(p), lab, float(v)])
                elif (v < ZERO) != pred:
                    mism.append([key(p), lab, float(v), pred])
        L1[tl] = {"mismatches": mism, "values between 1e-40 and 1e-25": between,
                  "lines with R_i^up = 0": sum(1 for r in rows.values() if r["iu"] < ZERO),
                  "lines with R_i^down = 0": sum(1 for r in rows.values() if r["id"] < ZERO)}
        ok1 = ok1 and not mism and not between
        base = [p for p, r in rows.items() if r["iu"] < ZERO and r["ju"] > NONZERO and r["id"] > NONZERO]
        c1 = sorted(p for p in base if p[0] not in (Fr(0), HALF))
        L2[tl] = {"C1 survivors": [key(p) for p in c1], "count": len(c1),
                  "without the clause a not in {0, 1/2}": [key(p) for p in sorted(base)],
                  "count without the clause": len(base),
                  "survivors of order 13-20": [key(p) for p in base if order(p) >= 13]}
        ok2 = ok2 and c1 == C1_PRED and sorted(base) == C1_PRED_NOCLAUSE
    L1["holds"] = bool(ok1)
    L2["holds"] = bool(ok2)
    return L1, L2


def part_L3():
    out, ok_i, ok_ii = {}, True, True
    for t in POINTS:
        rows = {}
        for p in C1_PRED:
            Ru = own_R(p, t, "up")
            I = invariant(Ru)
            rows[key(p)] = {"I": I, "closed form": closed_I(p, t.imag), "|R_jk|/|R_1|": jk_over_1(Ru)}
        i25 = [rows[key(p)]["I"] for p in C1_PRED if p[0] == Fr(2, 5)]
        i15 = [rows[key(p)]["I"] for p in C1_PRED if p[0] == Fr(1, 5)]
        order_ok = max(i25) < min(i15)
        dev = max(abs(r["I"] / r["closed form"] - 1) for r in rows.values())
        c2 = [k for k, r in rows.items() if r["I"] < 0.05 and r["|R_jk|/|R_1|"] > 2.0]
        out[str(t)] = {"lines": rows, "2/5 below 1/5": order_ok, "worst |I / closed - 1|": dev,
                       "B1761's C1 + C2 survivors": c2}
        ok_ii = ok_ii and order_ok
        if t.imag >= 3.0:
            ok_i = ok_i and dev < 0.10
    out["(i) holds"] = bool(ok_i)
    out["(ii) holds"] = bool(ok_ii)
    return out


def part_L4():
    t, worst, rows = PROBE, 0.0, {}
    for p in C1_PRED:
        w = complex(float(p[0]) * t + float(p[1]))
        cu = {u: W89.norm(TH[u], t, -3 * w) for u in UNITS}
        cd = {u: W89.norm(TH[u], t, 3 * w) for u in UNITS}
        d = max(abs(cu[u] - cd[u]) / max(abs(cd[u]), 1e-300) for u in UNITS)
        worst = max(worst, d)
        rows[key(p)] = {"c(-3w)": cu, "c(3w)": cd}
    return {"lines": rows, "worst relative difference": worst, "holds": bool(worst < 1e-8)}


def part_R(scans):
    out = {}
    rows = scans[str(PROBE)]
    zl = [p for p, r in rows.items() if r["iu"] < ZERO]
    out["lines with R_i^up = 0 at the probe, by order"] = {
        str(N): [key(p) for p in zl if order(p) == N] for N in sorted({order(p) for p in zl})}
    out["R_i^lep / |R^lep| on the C1 lines at the probe"] = {
        key(p): float(rel(own_R(p, PROBE, "lep"), "i")) for p in C1_PRED}
    p = (Fr(1, 5), Fr(1, 10))
    lo, hi = 3.0, 9.0
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        if invariant(own_R(p, complex(PROBE.real, mid), "up")) < 0.05:
            hi = mid
        else:
            lo = mid
    out["Im tau where (1/5, 1/10) first has I < 0.05 (Re tau 0.3145)"] = 0.5 * (lo + hi)
    out["the hand value"] = math.log(1 / 0.025016) / (0.2 * math.pi)
    return out


def guarded(name, fn, *a):
    try:
        return fn(*a)
    except Exception:
        say("FAILED PART", name)
        return {"failed": True, "traceback": traceback.format_exc()}


def main():
    t0 = time.time()
    out = {"arc": "W160", "rule": "W160_RULE.md", "status": "one run; output committed before it is read",
           "rev": REV, "python": platform.python_version(), "numpy": np.__version__, "mpmath": mp.__version__,
           "machine": platform.machine()}
    with tempfile.TemporaryDirectory() as tmp:
        out["L0"] = guarded("L0", part_L0, tmp)
    say("L0 done", round(time.time() - t0, 1))
    scans = {}
    for t in POINTS[:4]:
        scans[str(t)] = guarded("scan " + str(t), scan, t)
        say("scan done", t, round(time.time() - t0, 1))
    if all("failed" not in s for s in scans.values()):
        res = guarded("L1_L2", part_L1_L2, scans)
        out["L1"], out["L2"] = res if isinstance(res, tuple) else (res, res)
    else:
        out["L1"] = out["L2"] = {"failed": True, "traceback": "a scan failed"}
    out["L3"] = guarded("L3", part_L3)
    say("L3 done", round(time.time() - t0, 1))
    out["L4"] = guarded("L4", part_L4)
    out["R"] = guarded("R", part_R, scans) if str(PROBE) in scans and "failed" not in scans[str(PROBE)] else {
        "failed": True}
    out["cells"] = {
        "L0": bool(out["L0"].get("holds", False)),
        "L1": bool(out["L1"].get("holds", False)),
        "L2": bool(out["L2"].get("holds", False)),
        "L3 (i)": bool(out["L3"].get("(i) holds", False)),
        "L3 (ii)": bool(out["L3"].get("(ii) holds", False)),
        "L4": bool(out["L4"].get("holds", False))}
    out["failed parts"] = [k for k in ("L0", "L1", "L2", "L3", "L4", "R") if out[k].get("failed")]
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=lambda o: str(o) if not isinstance(o, (float, int)) else o)
                   + "\n", encoding="utf-8")
    say("written", OUT.name, "failed parts:", out["failed parts"])
    say("the_line_condition_checked exit 0")
    RUNTXT.write_text("\n".join(LOG) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
