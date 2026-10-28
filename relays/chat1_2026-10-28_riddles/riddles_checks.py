"""chat1, 2026-10-28: the three riddles' checks (exploratory and unsealed; data-free; no chi2, no measure).

This script reproduces in one file every number the relay cites that explore_ckm_and_bit.py does not, together with an
exact arithmetic check. Those numbers were first seen in unsealed exploratory runs on 2026-10-28. This run reproduces
them, so its output is not blind.

  A  exact arithmetic, no frame. On slope 2/5, does a line's T-orbit class contain a point the mirror fixes?
     Configuration (tau, alpha, b); T: (tau + 1, alpha, b - alpha); mirror: (-conj tau, -alpha, b); lines up to sign.
     "line (alpha, b) at Re tau = k/2 is mirror-fixed" iff (-alpha, b + k alpha) = +-(alpha, b) mod 1.
  B  the frame's J at Im tau 3.03, L_max, on CP-odd and CP-even classes, at Re tau 0, 1/4 and 1/2, every (up, down)
     reading pair, with the sector ratios.
  C  the six's best row (B1786: (2/5, 23/30) at 0.269 + 3.037i, L_max): the full |V| for each reading pair, and each
     sector's heaviest left-handed block under each reading.
  D  the 30 slope-2/5 lines of orders 25 and 30 at 0.3 + 3.03i and 0.6 + 3.03i, L_max: the ranges of every sector's
     m2/m3 and m1/m3 under each reading (the frame's values only).
  E  the channel constants c_s and the weights sqrt(2 pi L + c_s) at three of the six's rows, at both horocycles.
  F  B1667's exact channel norms on its 48 grid points: whether N_max - N_2 follows the asymptotic 2 pi (L_max - L_2),
     and the exact-to-asymptotic lift ratio at each horocycle.

Run:  python3 -B riddles_checks.py <main_checkout>   (main at 680d29e1c; B1726's compute(), B1667's json)"""
import sys, json, math, pathlib, itertools
from fractions import Fraction as Fr
from multiprocessing import Pool
ROOT = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification"))
import census as K
import numpy as np
import mpmath as mp
HERE = pathlib.Path(__file__).resolve().parent
A25 = Fr(2, 5)
CARRIERS_B1786 = [Fr(k, 25) for k in (3, 4, 11, 12, 17, 19, 21, 23)] + [Fr(1, 6), Fr(13, 30), Fr(23, 30), Fr(5, 6)]


def order(a, b):
    return math.lcm(a.denominator, b.denominator)


def mirror_fixed_ks(a, b, kmax=60):
    """the k in [0, kmax) for which the line (a, b) at Re tau = k/2 is mirror-fixed (lines up to sign)"""
    out = []
    for k in range(kmax):
        x, y = (-a) % 1, (b + k * a) % 1
        if (x, y) == (a % 1, b % 1) or (x, y) == ((-a) % 1, (-b) % 1): out.append(k)
    return out


def partA():
    by_order = {}
    for N in range(1, 61):
        for k in range(N):
            b = Fr(k, N)
            if order(A25, b) != N: continue
            fixed = bool(mirror_fixed_ks(A25, b))
            d = by_order.setdefault(N, {"lines": 0, "with_fixed_point": 0}); d["lines"] += 1; d["with_fixed_point"] += fixed
    rule = all(bool(mirror_fixed_ks(A25, Fr(k, N))) == (((2 * Fr(k, N)) % Fr(2, 5)) == 0 or ((2 * Fr(k, N) + 1) % Fr(2, 5)) == 0)
               for N in range(1, 61) for k in range(N))
    carriers = {str(b): {"order": order(A25, b), "fixed_ks": mirror_fixed_ks(A25, b), "partner_3/5-b": str((Fr(3, 5) - b) % 1)}
                for b in CARRIERS_B1786}
    tenths = {str(Fr(k, 10)): mirror_fixed_ks(A25, Fr(k, 10)) for k in (1, 3, 5, 7, 9)}
    return {"by_order": {N: v for N, v in by_order.items() if v["lines"]},
            "orders_with_a_fixed_point": sorted(N for N, v in by_order.items() if v["with_fixed_point"]),
            "rule_b_in_fifths_or_odd_tenths": rule, "B1786_carriers": carriers, "odd_tenths_fixed_ks": tenths}


def jtask(arg):
    re_t, a, b = arg
    r = K.compute(re_t, 3.03, a, b)
    return {"Re_tau": re_t, "line": [str(a), str(b)],
            "J": {k.split("|", 1)[1]: r[k][3] for k in r if k.startswith("ckm|L_max")},
            "ratios": {k: r[k] for k in r if "|L_max|" in k and not k.startswith("ckm")}}


def Ys(re_t, im_t, a, b, h="L_max"):
    M = K._modules(); B, te, col = M["B"], M["te"], M["col"]
    t = complex(re_t, im_t); w = float(a) * t + float(b)
    av = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
    S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    reading = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T}
    L = float(np.interp(im_t, [q[0] for q in col], [q[1] if h == "L_max" else q[2] for q in col]))
    Y = {}
    for sec, (lf, rf) in K.SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
        u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
        Mw = B.weighted_M(u)
        for rn in ("S", "St"): Y[(sec, rn)] = B.coupling(reading[rn], Mw)
    return Y


def partC():
    Y = Ys(0.269, 3.037, A25, Fr(23, 30)); out = {"heaviest_left_block (0 = QJ, 1 = QI, 2 = QK)": {}, "absV_rows_u_c_t_cols_d_s_b": {}}
    for key, Ym in Y.items():
        U = np.linalg.svd(Ym)[0]; out["heaviest_left_block (0 = QJ, 1 = QI, 2 = QK)"]["%s|%s" % key] = int(np.argmax(np.abs(U[:, 0])))
    for ru, rd in itertools.product(("S", "St"), repeat=2):
        Uu = np.linalg.svd(Y[("up", ru)])[0][:, ::-1]; Ud = np.linalg.svd(Y[("down", rd)])[0][:, ::-1]
        out["absV_rows_u_c_t_cols_d_s_b"]["%s|%s" % (ru, rd)] = np.abs(np.conj(Uu.T) @ Ud).round(4).tolist()
    return out


def dtask(arg):
    a, b, re_t = arg
    r = K.compute(re_t, 3.03, a, b)
    return {k: r[k] for k in r if "|L_max|" in k and not k.startswith("ckm")}


def lines_2_5():
    return [(A25, Fr(k, N)) for N in (25, 30) for k in range(N) if order(A25, Fr(k, N)) == N]


def partE():
    M = K._modules(); B, col = M["B"], M["col"]; out = []
    for (re_t, im_t, a, b) in [(0.269, 3.037, A25, Fr(23, 30)), (0.5, 3.03, A25, Fr(4, 25)), (0.763, 3.023, A25, Fr(5, 6))]:
        t = complex(re_t, im_t); w = float(a) * t + float(b)
        Lm = float(np.interp(im_t, [q[0] for q in col], [q[1] for q in col])); L2 = float(np.interp(im_t, [q[0] for q in col], [q[2] for q in col]))
        x, yy = B.sector_twists(w, t, B.SIXY["Q"], B.SIXY["d"]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
        cs = {s: float(np.real(c[s])) for s in B.UNITS if c[s] is not None}
        wm = {s: math.sqrt(2 * math.pi * Lm + v) for s, v in cs.items()}; w2 = {s: math.sqrt(2 * math.pi * L2 + v) for s, v in cs.items()}
        out.append({"tau": [re_t, im_t], "line": [str(a), str(b)], "2piL_max": 2 * math.pi * Lm, "2piL_2": 2 * math.pi * L2, "c_s": cs,
                    "weights_L_max": wm, "weights_L_2": w2, "max_over_min_L_max": max(wm.values()) / min(wm.values()),
                    "max_over_min_L_2": max(w2.values()) / min(w2.values())})
    return out


def partF():
    d = json.loads((ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json").read_text())
    grid = [p for p in d["points"] if p["where"] == "grid"]
    lift_max = [p["rho_max"] / (p["f"] / (2 * math.pi * p["L_max"])) for p in grid]
    lift_2 = [p["rho_2"] / (p["f"] / (2 * math.pi * p["L_2"])) for p in grid]
    dev_abs, dev_rel, worst = [], [], None
    for p in grid:
        dL = 2 * math.pi * (p["L_max"] - p["L_2"])
        for r in p["N_max"]:
            dv = (p["N_max"][r] - p["N_2"][r]) - dL; dev_abs.append(dv); rel = dv / p["N_max"][r]; dev_rel.append(rel)
            if worst is None or abs(rel) > abs(worst[0]): worst = (rel, p["tau"], r)
    p0 = min(grid, key=lambda p: abs(complex(*p["tau"]) - complex(0.05, 2.0)))
    return {"n_grid": len(grid), "exact_over_asymptotic_lift_L_max": [min(lift_max), max(lift_max)],
            "exact_over_asymptotic_lift_L_2": [min(lift_2), max(lift_2)],
            "deviation_of_Nmax_minus_N2_from_2pi_dL": [min(dev_abs), max(dev_abs)],
            "same_relative_to_N_max": [min(dev_rel), max(dev_rel)], "largest_relative": worst,
            "sample_point": {"tau": p0["tau"], "L_max": p0["L_max"], "L_2": p0["L_2"], "N_max": p0["N_max"], "N_2": p0["N_2"],
                             "asymptotic_at_L_max_from_N_2": {r: p0["N_2"][r] + 2 * math.pi * (p0["L_max"] - p0["L_2"]) for r in p0["N_2"]}}}


if __name__ == "__main__":
    res = {"A": partA()}
    print("A orders with a mirror-fixed point on slope 2/5 (N <= 60):", res["A"]["orders_with_a_fixed_point"], flush=True)
    print("A the rule 'b a fifth or an odd tenth' matches on every line to order 60:", res["A"]["rule_b_in_fifths_or_odd_tenths"])
    print("A B1786's carriers:", {b: (v["order"], v["fixed_ks"], v["partner_3/5-b"]) for b, v in res["A"]["B1786_carriers"].items()})
    print("A the odd tenths' fixed k:", res["A"]["odd_tenths_fixed_ks"], flush=True)
    jargs = [(0.5, A25, Fr(23, 30)), (0.5, A25, Fr(5, 6)), (0.5, A25, Fr(4, 25)), (0.5, A25, Fr(11, 25)), (0.5, A25, Fr(3, 10)),
             (0.5, A25, Fr(1, 6)), (0.0, A25, Fr(23, 30)), (0.0, A25, Fr(1, 6)), (0.0, A25, Fr(1, 2)), (0.25, A25, Fr(1, 2))]
    dargs = [(a, b, r) for a, b in lines_2_5() for r in (0.3, 0.6)]
    with Pool(2) as P:
        res["B"] = P.map(jtask, jargs, chunksize=1)
        res["D_rows"] = P.map(dtask, dargs, chunksize=1)
    for r in res["B"]:
        print("B Re %.2f line (%s, %s) J:" % (r["Re_tau"], *r["line"]), " ".join("%s %.2e" % (k, v) for k, v in r["J"].items()),
              "| up|St %s down|S %s" % (["%.3g" % x for x in r["ratios"]["up|L_max|St"]], ["%.3g" % x for x in r["ratios"]["down|L_max|S"]]), flush=True)
    res["C"] = partC()
    print("C heaviest left block:", res["C"]["heaviest_left_block (0 = QJ, 1 = QI, 2 = QK)"])
    for k, v in res["C"]["absV_rows_u_c_t_cols_d_s_b"].items(): print("C |V| (up|down) %-6s" % k, v)
    keys = sorted(res["D_rows"][0].keys()); res["D"] = {}
    for k in keys:
        m2 = [r[k][0] for r in res["D_rows"]]; m1 = [r[k][1] for r in res["D_rows"]]
        res["D"][k] = {"m2/m3": [min(m2), float(np.median(m2)), max(m2)], "m1/m3": [min(m1), float(np.median(m1)), max(m1)]}
        print("D %-14s m2/m3 min %.3g med %.3g max %.3g | m1/m3 min %.3g med %.3g max %.3g" % (k, *res["D"][k]["m2/m3"], *res["D"][k]["m1/m3"]))
    res["E"] = partE()
    for e in res["E"]:
        print("E tau %s line %s: 2piL_max %.3f 2piL_2 %.3f c_s %s; weight ratio max/min L_max %.3f, L_2 %.3f" % (
            e["tau"], e["line"], e["2piL_max"], e["2piL_2"], {s: round(v, 3) for s, v in e["c_s"].items()}, e["max_over_min_L_max"], e["max_over_min_L_2"]))
    res["F"] = partF(); F = res["F"]
    print("F grid points %d; exact/asymptotic lift at L_max %.3f-%.3f, at L_2 %.3f-%.3f" % (F["n_grid"], *F["exact_over_asymptotic_lift_L_max"], *F["exact_over_asymptotic_lift_L_2"]))
    print("F (N_max - N_2) - 2pi(L_max - L_2): %.3f to %.3f; relative to N_max %.3f to %.3f; largest %s" % (
        *F["deviation_of_Nmax_minus_N2_from_2pi_dL"], *F["same_relative_to_N_max"], F["largest_relative"]))
    print("F sample point:", F["sample_point"])
    (HERE / "riddles_checks.json").write_text(json.dumps(res, indent=1, default=str))
    print("riddles_checks exit 0")
