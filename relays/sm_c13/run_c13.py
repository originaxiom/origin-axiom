#!/usr/bin/env python3
"""SM-C13: what separates the lepton rows from the down rows at level 5 (card
relays/cards/SM_C13_the-lepton-rows-at-level-5.md, pushed before this run).  Main's frame (B1724 covariance.py, with
B1723's b1656_funcs) imported unchanged from a checkout of main (first argument); the per-sector step of its frame() is
used with the charges passed explicitly, and checked first to reproduce frame() exactly (P3).
ONLY differences are written: max relative difference between two sectors' outputs; no output value is printed or saved.
    python3 run_c13.py MAIN_CHECKOUT [out.json]"""
import sys, io, math, json, pathlib, contextlib, importlib.util
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
MAIN = pathlib.Path(sys.argv[1]).resolve()
spec = importlib.util.spec_from_file_location("cov", MAIN / "frontier/B1724_the_readings_covariance/verification/covariance.py")
COV = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(COV)
SIX = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6}
MARK = (Fr(2, 5), Fr(4, 5))
ORDER5 = [MARK, (Fr(1, 5), Fr(0)), (Fr(0), Fr(1, 5)), (Fr(1, 5), Fr(2, 5)), (Fr(3, 5), Fr(1, 5)), (Fr(4, 5), Fr(3, 5))]
OTHER = [l for l in COV.LINES if math.lcm(l[0].denominator, l[1].denominator) != 5]
HALVES = [(MARK[0] / 2 + e1 / Fr(2), MARK[1] / 2 + e2 / Fr(2)) for e1 in (0, 1) for e2 in (0, 1)]


def order(p): return math.lcm(p[0].denominator, p[1].denominator)


def sector(t, a, b, ql, qr, Ls):
    """the per-sector step of B1724's frame(), verbatim, with the charges given: {(end, reading): [r1, r2]}"""
    M = COV._modules(); B = M["B"]
    c3 = COV.components(t); S = c3[0] * B.QI + c3[1] * B.QJ + c3[2] * B.QK
    reading = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T, "conjS": np.conj(S)}
    w = float(a) * t + float(b)
    x, yy = B.sector_twists(w, t, ql, qr); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
    out = {}
    for h in ("L_max", "L_2"):
        L = Ls[h]
        u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
        Mw = B.weighted_M(u)
        for rn in ("S", "St", "conjS"):
            sv = np.linalg.svd(B.coupling(reading[rn], Mw), compute_uv=False)
            out[(h, rn)] = np.array([sv[1] / sv[0], sv[2] / sv[0]])
    return out


def rel(x, y): return float(np.max(np.abs(x - y) / np.maximum(np.abs(y), 1e-12)))


def main():
    out_path = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "c13_results.json"
    res = {"points": {}, "P3": None}
    # P3: the explicit-charge sector reproduces frame() exactly (differences only)
    t0 = COV.TAUS[0]; Ls0 = COV.L_col(t0.imag); F = COV.frame(t0, MARK[0], MARK[1], Ls0)
    for sec, (lf, rf) in COV.SECT.items():
        mine = sector(t0, MARK[0], MARK[1], SIX[lf], SIX[rf], Ls0)
        res.setdefault("P3_reproduces_frame", {})[sec] = max(rel(np.array(F["%s|%s|%s" % (sec, h, rn)]), mine[(h, rn)]) for (h, rn) in mine)
    print("P3", res["P3_reproduces_frame"], flush=True)
    groups = [("order5", ORDER5), ("other_orders", OTHER), ("halves_of_mark", HALVES)]
    for gname, pts in groups:
        for p in pts:
            key = "%s (%s, %s) order %d" % (gname, p[0], p[1], order(p))
            row = {"group": gname, "order": order(p), "X1_same_reading": [], "X2_pairs": {}, "P1P2_lepton_as_down_transposed": [],
                   "P3_self": []}
            for t in COV.TAUS:
                Ls = COV.L_col(t.imag)
                dn = sector(t, p[0], p[1], SIX["Q"], SIX["d"], Ls)
                lp = sector(t, p[0], p[1], SIX["L"], SIX["e"], Ls)
                pl = sector(t, p[0], p[1], 2, 1, Ls)                              # P1 = P2: lepton charges (2, 1)
                for h in ("L_max", "L_2"):
                    for r in ("S", "St", "conjS"):
                        row["X1_same_reading"].append(rel(lp[(h, r)], dn[(h, r)]))
                        row["P1P2_lepton_as_down_transposed"].append(rel(pl[(h, r)], dn[(h, r)]))
                        row["P3_self"].append(rel(dn[(h, r)], dn[(h, r)]))
                        for r2 in ("S", "St", "conjS"):
                            row["X2_pairs"].setdefault("lep %s / down %s" % (r, r2), []).append(rel(lp[(h, r)], dn[(h, r2)]))
            row = {"group": row["group"], "order": row["order"],
                   "X1_max_rel_diff": max(row["X1_same_reading"]), "X1_min_rel_diff": min(row["X1_same_reading"]),
                   "X2_max_rel_diff_by_pair": {k: max(v) for k, v in row["X2_pairs"].items()},
                   "X2_min_rel_diff_by_pair": {k: min(v) for k, v in row["X2_pairs"].items()},
                   "P1P2_max_rel_diff": max(row["P1P2_lepton_as_down_transposed"]), "P3_self_max": max(row["P3_self"])}
            res["points"][key] = row
            print(key, "X1 min/max", "%.1e/%.1e" % (row["X1_min_rel_diff"], row["X1_max_rel_diff"]),
                  "P1P2 max %.1e" % row["P1P2_max_rel_diff"], flush=True)
    P = res["points"]
    eq = lambda v: v < 1e-9; dif = lambda v: v > 1e-6
    o5 = [r for r in P.values() if r["order"] == 5]; oth = [r for r in P.values() if r["group"] == "other_orders"]
    h10 = [r for r in P.values() if r["group"] == "halves_of_mark" and r["order"] == 10]
    res["summary"] = {
        "P3_reproduces_frame": all(v < 1e-12 for v in res["P3_reproduces_frame"].values()),
        "X1_equal_on_every_order5_point": all(eq(r["X1_max_rel_diff"]) for r in o5),
        "X2_diagonal_equal_at_order5": all(eq(r["X2_max_rel_diff_by_pair"]["lep %s / down %s" % (x, x)]) for r in o5 for x in ("S", "St", "conjS")),
        "X2_mixed_pairs_differing_at_order5": sorted({k for r in o5 for k, v in r["X2_min_rel_diff_by_pair"].items() if dif(v)}),
        "X3_differ_at_every_other_order": all(dif(r["X1_min_rel_diff"]) for r in oth),
        "X3_by_order": {r["order"]: (r["X1_min_rel_diff"] > 1e-6) for r in oth},
        "X4_differ_at_the_three_order10_halves": all(dif(r["X1_min_rel_diff"]) for r in h10) and len(h10) == 3,
        "P1P2_equal_everywhere": all(eq(r["P1P2_max_rel_diff"]) for r in P.values()),
        "P3_self_zero": all(r["P3_self_max"] == 0 for r in P.values())}
    # X5: code inspection of the frame's two sources for any colour-dependent ingredient
    import re
    srcs = [MAIN / "frontier/B1724_the_readings_covariance/verification/covariance.py",
            MAIN / "frontier/B1723_the_golden_valley/verification/b1656_funcs.py"]
    hits = {str(p.name): len(re.findall(r"colou?r|\bN_?c\b|SU\(3\)", p.read_text(encoding="utf-8"), flags=re.I)) for p in srcs}
    res["summary"]["X5_colour_tokens_in_frame_sources"] = hits
    res["summary"]["X5_no_colour_ingredient"] = all(v == 0 for v in hits.values())
    json.dump(res, open(out_path, "w"), indent=1, default=str)
    print(json.dumps(res["summary"], indent=1, default=str))


if __name__ == "__main__":
    main()
