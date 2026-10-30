"""Second pre-seal review (data-free; aggregates only): the refined census plan's two symmetry premises, at RELATIVE precision.

The plan computes Re tau in [0, 1/2] only, and gets every other Re tau from
  (i)  the mirror  (x + iy, (a, b)) <-> (-x + iy, (a, -b)),  J -> -J   (REFINED_CENSUS_PLAN section 2), and
  (ii) T-periodicity of the menu: (tau + 1, (a, b + a)) == (tau, (a, b)) in this evaluator's convention
       w = a*tau - b (b1656_funcs.line_w); B1724's law, checked on record for the DR section only (B1741 C1(ii)).
       Tested INSIDE the strip only (x + 1/2 against x - 1/2): the evaluator's F_a use mpmath's jtheta(2, 0, q) with
       q = exp(i pi tau), whose principal q^(1/4) equals the analytic theta_2 only for |Re tau| < 1
       (t_period_diagnostic.py shows the sign error beyond).
The plan's own check (re_symmetry_check_200.py) rounds every output to 5 DECIMAL PLACES (absolute), so it cannot see a
difference in any output below ~1e-5 (the smallest mass ratios, |V_ub|-sized moduli, J).  This script compares every
output in log10 (relative), J with its sign, row by row (same reading) and as best-assignment multisets per
(direction, radius) group, and also the up-to-sign identification (a, b) ~ (-a, -b) the menu assumes.

It evaluates the frame's own outputs at fresh random configurations (no census file is opened, no measured value is
used) and prints only maxima and counts.  Writes sym_check_relative.json beside itself.
    nice -n 10 python3 -B sym_check_relative.py [n_configs] [workers]
"""
# B1821 (2026-10-30): committed from the audit room as the census's instrument; the only change is the import path, set to this folder.
import json, math, os, pathlib, random, sys
from multiprocessing import Pool
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "frontier").is_dir() and (p / "GENESIS.md").is_file())
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))


FLOOR = 1e-12      # outputs at or below this are compared as 'degenerate' (both must be)


def vec(r):
    return list(r["up"]) + list(r["down"]) + list(r["lepton"]) + list(r["V"])


def row_dev(ra, rb, jsign):
    """max |log10 a - log10 b| over the nine positive outputs (mixing only if both defined), and the J deviation
    relative to max(|J|, 1e-300); returns (dlog, dJrel, degenerate_mismatch, vdef_mismatch)"""
    va, vb = vec(ra), vec(rb)
    both_v = ra["V defined"] and rb["V defined"]
    n = 9 if both_v else 6
    dl, degmis = 0.0, 0
    for x, y in zip(va[:n], vb[:n]):
        if x <= FLOOR or y <= FLOOR:
            if (x <= FLOOR) != (y <= FLOOR): degmis += 1
            continue
        dl = max(dl, abs(math.log10(x) - math.log10(y)))
    dj = 0.0
    if both_v:
        ja, jb = ra["J"], jsign * rb["J"]
        sc = max(abs(ja), abs(jb))
        dj = abs(ja - jb) / sc if sc >= 1e-12 else 0.0          # |J| below 1e-12 on both sides: numerical zero, not compared
    return dl, dj, degmis, int(ra["V defined"] != rb["V defined"])


def compare(A, B, jsign):
    from scipy.optimize import linear_sum_assignment
    import numpy as np
    keyA = {(r["direction"], r["radius"], r["reading"]): r for r in A}
    keyB = {(r["direction"], r["radius"], r["reading"]): r for r in B}
    same = {"dlog": 0.0, "dJ": 0.0, "deg": 0, "vdef": 0}
    for k, ra in keyA.items():
        dl, dj, dg, vd = row_dev(ra, keyB[k], jsign)
        same["dlog"] = max(same["dlog"], dl); same["dJ"] = max(same["dJ"], dj); same["deg"] += dg; same["vdef"] += vd
    groups = {}
    for r in A: groups.setdefault((r["direction"], r["radius"]), [[], []])[0].append(r)
    for r in B: groups.setdefault((r["direction"], r["radius"]), [[], []])[1].append(r)
    best = {"dlog": 0.0, "dJ": 0.0, "deg": 0, "vdef": 0, "perm_identity_groups": 0, "groups": len(groups)}
    for g, (ga, gb) in groups.items():
        C = np.zeros((len(ga), len(gb)))
        for i, ra in enumerate(ga):
            for j, rb in enumerate(gb):
                dl, dj, dg, vd = row_dev(ra, rb, jsign)
                C[i, j] = dl + min(dj, 1.0) + dg + vd
        ri, ci = linear_sum_assignment(C)
        if all(ga[i]["reading"] == gb[j]["reading"] for i, j in zip(ri, ci)): best["perm_identity_groups"] += 1
        for i, j in zip(ri, ci):
            dl, dj, dg, vd = row_dev(ga[i], gb[j], jsign)
            best["dlog"] = max(best["dlog"], dl); best["dJ"] = max(best["dJ"], dj); best["deg"] += dg; best["vdef"] += vd
    return {"row_by_row": same, "best_assignment": best}


def check(arg):
    import cm_zero_line as Z
    from fractions import Fraction as F
    N, a, b, x, y = arg
    a, b = F(a), F(b)
    out = {"order": N}
    try:
        A = Z.rows_at(complex(x, y), (a, b))
        M = Z.rows_at(complex(-x, y), (a, (-b) % 1))
        # T inside the strip |Re tau| < 1 (the evaluator's theta_2 is mpmath's principal branch, exact only there):
        # (x + 1/2, (a, b)) against (x - 1/2, (a, b - a)) in this evaluator's convention w = a*tau - b
        A_T = Z.rows_at(complex(x + 0.5, y), (a, b))
        T = Z.rows_at(complex(x - 0.5, y), (a, (b - a) % 1))
        S = Z.rows_at(complex(x, y), ((-a) % 1, (-b) % 1))
    except Exception as ex:
        out["error"] = repr(ex)[:120]; return out
    out["mirror"] = compare(A, M, -1)
    out["T_shift"] = compare(A_T, T, +1)
    out["sign"] = compare(A, S, +1)
    out["n_small_outputs"] = sum(1 for r in A for v in vec(r)[:6] if 0 < v < 1e-5)
    return out


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    import rigid_census_full_menu as M
    rnd = random.Random(20261030)
    jobs = []
    for _ in range(n):
        m = rnd.choice(M.MENU)
        jobs.append((m[0], str(m[1]), str(m[2]), round(rnd.uniform(0.01, 0.49), 4), round(rnd.uniform(1.0, 4.0), 4)))
    with Pool(workers) as P:
        res = P.map(check, jobs, chunksize=1)
    agg = {}
    for test in ("mirror", "T_shift", "sign"):
        ok = [r[test] for r in res if test in r]
        agg[test] = {
            "configs": len(ok),
            "row_by_row_max_dlog10": max(o["row_by_row"]["dlog"] for o in ok),
            "row_by_row_max_dJ_rel": max(o["row_by_row"]["dJ"] for o in ok),
            "row_by_row_degenerate_mismatches": sum(o["row_by_row"]["deg"] for o in ok),
            "row_by_row_vdefined_mismatches": sum(o["row_by_row"]["vdef"] for o in ok),
            "best_assignment_max_dlog10": max(o["best_assignment"]["dlog"] for o in ok),
            "best_assignment_max_dJ_rel": max(o["best_assignment"]["dJ"] for o in ok),
            "best_assignment_degenerate_mismatches": sum(o["best_assignment"]["deg"] for o in ok),
            "best_assignment_vdefined_mismatches": sum(o["best_assignment"]["vdef"] for o in ok),
            "groups_matched_with_identity_reading_map": "%d of %d" % (sum(o["best_assignment"]["perm_identity_groups"] for o in ok), sum(o["best_assignment"]["groups"] for o in ok)),
            "configs_with_best_assignment_dlog10_above_1e-6": sum(1 for o in ok if o["best_assignment"]["dlog"] > 1e-6),
            "configs_with_row_by_row_dlog10_above_1e-6": sum(1 for o in ok if o["row_by_row"]["dlog"] > 1e-6),
        }
        agg[test]["orders_failing_best_assignment_1e-6"] = sorted({r["order"] for r in res if test in r and r[test]["best_assignment"]["dlog"] > 1e-6})
    summary = {"seed": 20261030, "n": n, "errors": sum(1 for r in res if "error" in r),
               "outputs_below_1e-5_in_the_six_across_sampled_rows": sum(r.get("n_small_outputs", 0) for r in res),
               "aggregates": agg,
               "note": "aggregates only; no census file opened; no measured value used; outputs compared in log10, J signed"}
    (HERE / "sym_check_relative.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    print(json.dumps(summary, indent=1))
