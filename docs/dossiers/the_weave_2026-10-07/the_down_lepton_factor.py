#!/usr/bin/env python3
"""W179 — the down–lepton factor at the points the principle marks (the rule: W179_RULE.md, committed and pushed before
this script).  It runs once, from the repository root, on four worker processes.

B1656's frame's own double ratios on every census line, from W178's frame unchanged:
  ln r2 = ln(m_s/m_b) - ln(m_mu/m_tau),  ln r1 = ln(m_d/m_b) - ln(m_e/m_tau),  ln D = ln r1 - ln r2
  Part A  the cusp: read from W178's committed output (the stored six at Im tau 6-48); finite where the down and lepton
          cusp exponents agree to 0.005, read at Im tau 48, running elsewhere
  Part B  tau = i: computed with W178's own point function (Re tau 0, Im tau 1, its two precisions, no cut)

  G0  the cusp limits converge: |ln r(48) - ln r(32)| <= 1e-3 for r2, r1 and D on every finite line and Re tau
  G1  the tie: |ln D| <= 1e-8 on every resolved line of order 1, 2 or 5, at every ladder height, both Re tau, and at i
  G2  no line's cusp D and no line's D at i within 3 sigma of P-094's 10.58 +- 0.11
  G3  no line, at the cusp or at i, with both r2 and r1 within a factor 1.25 of the data's
  R   read-outs

    python3 -B docs/dossiers/the_weave_2026-10-07/the_down_lepton_factor.py
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
T8, W58 = W178.T8, W178.W58
OUT = HERE / "the_down_lepton_factor.json"
LADDER = W178.LADDER
XS = W178.XS
AGREE = 0.005
CONV = 1e-3
TIE = 1e-8
TIE_ORDERS = (1, 2, 5)
SIGMAS = 3
FACTOR = 1.25
WORKERS = 4
DOWN2, DOWN1, LEP2, LEP1 = 2, 3, 4, 5        # positions in the six (up m2, up m1, down m2, down m1, lep m2, lep m1)


def doubles(six):
    """(ln r2, ln r1, ln D) from a six, or None if a needed feature is missing"""
    if any(six[i] is None for i in (DOWN2, DOWN1, LEP2, LEP1)):
        return None
    l2, l1 = six[DOWN2] - six[LEP2], six[DOWN1] - six[LEP1]
    return [l2, l1, l1 - l2]


def order(line):
    a, b = (Fr(v) for v in line)
    return math.lcm(a.denominator, b.denominator)


def run(out, pool):
    lines = T8.own_lines()
    files = {p: T8.git_bytes(ROOT, W58.REV, p) for p in W58.FILES}
    t6 = T8.targets(files)[0]
    ahs = json.loads((HERE / "received" / "AHS2026_double_ratio.json").read_text(encoding="utf-8"))["the double ratio"]
    data = {"ln r2": float(t6[DOWN2] - t6[LEP2]), "ln r1": float(t6[DOWN1] - t6[LEP1]),
            "D": float(ahs["value"]), "sigma D": float(ahs["sigma"])}
    data["ln D"] = math.log(data["D"])
    out["the data (read once)"] = data
    lo, hi = data["D"] - SIGMAS * data["sigma D"], data["D"] + SIGMAS * data["sigma D"]
    lf = math.log(FACTOR)
    w178 = json.loads((HERE / "the_six_at_the_cusp.json").read_text(encoding="utf-8"))
    # ---------------------------------------------------------------- Part B: tau = i, computed
    tasks = [(k, 0.0, 1.0, False) for k in range(len(lines))]
    t0 = time.time()
    at_i = {r["k"]: r for r in pool.imap_unordered(W178.point, tasks, chunksize=1)}
    out["Part B seconds"] = round(time.time() - t0, 1)
    out["Part B failed tasks"] = [[r["k"], r["failed"]] for r in at_i.values() if "failed" in r]
    # ---------------------------------------------------------------- per line
    per, conv_bad, tie_bad, g2_hits, g3_hits = [], [], [], [], []
    counts = {"cusp finite": 0, "cusp running": 0, "cusp excluded": 0, "i finite": 0, "i excluded": 0}
    for k, line in enumerate(lines):
        e = w178["per line"][k]
        assert e["line"] == [str(line[0]), str(line[1])]
        N = order(e["line"])
        entry = {"line": e["line"], "order": N, "cusp": [], "at i": None}
        for p in e["per Re tau"]:
            row = {"x": p["x"]}
            if p.get("failed") or p.get("zero channel") or p.get("unresolved feature"):
                row["status"] = "excluded"
                counts["cusp excluded"] += 1
                entry["cusp"].append(row)
                continue
            ladder = {y: doubles(p["six per height"][str(y)]) for y in LADDER}
            row["ln (r2, r1, D) per height"] = {str(y): v for y, v in ladder.items()}
            n = p["cusp pattern e(32,48)"]
            agree = abs(n[DOWN2] - n[LEP2]) <= AGREE and abs(n[DOWN1] - n[LEP1]) <= AGREE
            if N in TIE_ORDERS:
                worst = max(abs(v[2]) for v in ladder.values())
                row["tie |ln D| max over heights"] = worst
                if worst > TIE:
                    tie_bad.append([e["line"], p["x"], "ladder", worst])
            if agree:
                v48, v32 = ladder[48.0], ladder[32.0]
                row["status"] = "finite"
                row["cusp ln (r2, r1, D)"] = v48
                row["change 32 to 48"] = [abs(a - b) for a, b in zip(v48, v32)]
                counts["cusp finite"] += 1
                if max(row["change 32 to 48"]) > CONV:
                    conv_bad.append([e["line"], p["x"], max(row["change 32 to 48"])])
                if lo <= math.exp(v48[2]) <= hi:
                    g2_hits.append([e["line"], p["x"], "cusp", math.exp(v48[2])])
                if abs(v48[0] - data["ln r2"]) <= lf and abs(v48[1] - data["ln r1"]) <= lf:
                    g3_hits.append([e["line"], p["x"], "cusp", math.exp(v48[0]), math.exp(v48[1])])
            else:
                row["status"] = "running"
                row["down minus lepton cusp exponents"] = [n[DOWN2] - n[LEP2], n[DOWN1] - n[LEP1]]
                counts["cusp running"] += 1
            entry["cusp"].append(row)
        r = at_i[k]
        if "failed" in r or any(s != "resolved" for s in r["status"]):
            entry["at i"] = {"status": "excluded" if "failed" in r else r["status"]}
            counts["i excluded"] += 1
        else:
            v = doubles(r["six"])
            entry["at i"] = {"status": "finite", "six": r["six"], "ln (r2, r1, D)": v}
            counts["i finite"] += 1
            if N in TIE_ORDERS and abs(v[2]) > TIE:
                tie_bad.append([e["line"], 0.0, "i", abs(v[2])])
            if lo <= math.exp(v[2]) <= hi:
                g2_hits.append([e["line"], 0.0, "i", math.exp(v[2])])
            if abs(v[0] - data["ln r2"]) <= lf and abs(v[1] - data["ln r1"]) <= lf:
                g3_hits.append([e["line"], 0.0, "i", math.exp(v[0]), math.exp(v[1])])
        per.append(entry)
    out["per line"] = per
    out["counts"] = counts
    tie_lines = [e["line"] for e in per if e["order"] in TIE_ORDERS]
    out["G0"] = {"finite line-and-Re-tau pairs": counts["cusp finite"], "not settled": conv_bad,
                 "holds": bool(counts["cusp finite"] and not conv_bad)}
    out["G1"] = {"tie lines (orders 1, 2, 5)": len(tie_lines), "misses": tie_bad,
                 "holds": bool(tie_lines and not tie_bad)}
    out["G2"] = {"window": [lo, hi], "hits": g2_hits, "holds": bool(not g2_hits)}
    out["G3"] = {"factor": FACTOR, "hits": g3_hits, "holds": bool(not g3_hits)}
    # ---------------------------------------------------------------- read-outs
    pts = []
    for e in per:
        for row in e["cusp"]:
            if row.get("status") == "finite":
                pts.append(("cusp", e["line"], row["x"], row["cusp ln (r2, r1, D)"]))
        if e["at i"]["status"] == "finite":
            pts.append(("i", e["line"], 0.0, e["at i"]["ln (r2, r1, D)"]))
    for where in ("cusp", "i"):
        vals = sorted({round(math.exp(v[2]), 6) for w, _l, _x, v in pts if w == where})
        out[f"R: distinct D at {where} (to 1e-6)"] = {"count": len(vals), "values": vals[:200]}
        sp = [v[2] for w, _l, _x, v in pts if w == where]
        out[f"R: lines splitting d from e at {where} (|ln D| > 1e-8)"] = sum(1 for s in sp if abs(s) > TIE)
    near_d = sorted(pts, key=lambda q: abs(q[3][2] - data["ln D"]))[:10]
    out["R: ten nearest to the data's D"] = [[w, l, x, math.exp(v[2])] for w, l, x, v in near_d]
    near_p = sorted(pts, key=lambda q: max(abs(q[3][0] - data["ln r2"]), abs(q[3][1] - data["ln r1"])))[:10]
    out["R: ten nearest to the data's (r2, r1)"] = [[w, l, x, math.exp(v[0]), math.exp(v[1])] for w, l, x, v in near_p]
    out["R: slope-2/5 lines"] = [[w, l, x, math.exp(v[0]), math.exp(v[1]), math.exp(v[2])]
                                 for w, l, x, v in pts if l[0] == "2/5"]
    out["cells"] = {c: out[c]["holds"] for c in ("G0", "G1", "G2", "G3")}


def main():
    t0 = time.time()
    out = {"arc": "W179", "rule": "W179_RULE.md", "python": platform.python_version(), "workers": WORKERS,
           "frame": "W178's (the_six_at_the_cusp.py), unchanged"}
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        try:
            with mpc.get_context("fork").Pool(WORKERS, initializer=W178._init, initargs=(str(ROOT),)) as pool:
                run(out, pool)
        except Exception:  # noqa: BLE001  (a failed run still writes what it has)
            out["run_failed"] = W178.sanitize(traceback.format_exc()[-3000:])
    out["warnings"] = sorted({f"{w.category.__name__}: {w.message}" for w in caught})
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name, "in", out["seconds"], "s;", len(out["warnings"]), "distinct warnings")


if __name__ == "__main__":
    main()
