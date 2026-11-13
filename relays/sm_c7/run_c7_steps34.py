#!/usr/bin/env python3
"""SM-C7 steps 3 and 4 (released by main, M19), with three planted controls, on B1737's population.

For every character c (the thread's line u = Jc, and its channels u_s = Jc + h_s, h = 0, (0,1/2), (1/2,0), (1/2,1/2)):
  3a  B1656's own c_s at the thread's apex (the record's apex: the highest lift, reduced) against
      F_{u_s} + pi log Im tau + C, C = -2 pi (gamma + log pi); F_u the u-shifted Kronecker limit (sm_c7_lib.F_shift)
  3b  the line part's average <F_u> along one period of the geodesic, for two windows (canonical when u is fixed);
      the frame's c_s averaged on the representative's semicircle, for the same two windows (not canonical)
  3c  the line part at the apex against its average
  3d  the shifted Hecke formula at s = 2, one character per level (cone side by brute force)
  3e  <F_Jc> against step 2's twisted Kronecker coefficient (pi/2l) Z_tot(1, chi_c): the best affine fit per level
  4   the table: per thread, line and channel, every value above; compared with nothing
  plants  P5 a wrong channel's shift; P6 the pi log Im tau term dropped; P7 c in place of Jc
Data-free.  Usage: python3 run_c7_steps34.py [population.json] [results_steps12.json] [out.json]"""
import sys, json, math, time, pathlib
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import sm_c7_lib as L, b1656_kernel as B

C0 = -2 * math.pi * (float(L.mp.euler) + math.log(math.pi))
HALF = {"1": (Fr(0), Fr(0)), "i": (Fr(0), Fr(1, 2)), "j": (Fr(1, 2), Fr(0)), "k": (Fr(1, 2), Fr(1, 2))}
NODES = 48


def fixed_u(M, u):
    (a, b), (c, d) = M
    return ((a * u[0] + b * u[1] - u[0]) % 1, (c * u[0] + d * u[1] - u[1]) % 1) == (0, 0)


def frame_cs(tau, ucoords):
    """B1656's c_s (all four channels) at modulus tau for the line whose summed twist has real coordinates ucoords"""
    a1, a2 = float(ucoords[0]), float(ucoords[1])
    w = B.line_w(a1, -a2, tau)
    x, y = B.sector_twists(w, tau, 1, 0); R = B.residues(x, y, tau)
    return B.cA(x, y, tau, R)


def transport(u, g):
    gi = L.ginv(g)
    return (u[0] * gi[0][0] + u[1] * gi[1][0], u[0] * gi[0][1] + u[1] * gi[1][1])


def window_avgs(geo, u, t0):
    t, h = geo.nodes(NODES, t0=t0)
    F = np.array([L.F_shift_reduced(u, geo.z(tt)) for tt in t])
    ly = np.array([math.log(geo.z(tt).imag) for tt in t])
    return float(np.mean(F)), float(np.mean(F + math.pi * ly + C0))


def main():
    pop = json.load(open(sys.argv[1] if len(sys.argv) > 1 else HERE / "population.json"))
    s12 = json.load(open(sys.argv[2] if len(sys.argv) > 2 else HERE / "sm_c7_results.json"))
    out_path = pathlib.Path(sys.argv[3]) if len(sys.argv) > 3 else HERE / "sm_c7_steps34_results.json"
    z1 = {(tuple(r["level"]), r["i"], r["j"]): r["step2"]["b_s1"]["Ztot1"][0] for r in s12["rows"]}
    levels = {}
    for o in pop:
        levels.setdefault(tuple(o["level"]), []).append(o)
    rows, lev_rows, t00 = [], [], time.time()
    for lev, chars in levels.items():
        M = chars[0]["M"]; geo = L.Geodesic(M)
        ts, tauA, hA, gA = L.apex(geo)
        t0a, t0b = -geo.ell / 2, -geo.ell / 2 + 0.37 * geo.ell
        for n, o in enumerate(chars):
            i, j, N = o["i"], o["j"], o["N"]
            c = (Fr(i, N), Fr(j, N)); Jc = (-c[1], c[0])
            uA = transport(Jc, gA)                        # the line's coordinates at the reduced apex
            fc = frame_cs(tauA, uA)
            row = {"level": list(lev), "N": N, "i": i, "j": j, "apex": [tauA.real, tauA.imag], "channels": {}}
            for s, hs in HALF.items():
                us = (Jc[0] + hs[0], Jc[1] + hs[1])
                usA = (uA[0] + hs[0], uA[1] + hs[1])
                FA = L.F_shift(usA, tauA)
                ident = None if fc[s] is None else abs(fc[s] - (FA + math.pi * math.log(tauA.imag) + C0))
                fixed = fixed_u(M, us)
                ch = {"fixed": fixed, "frame_cs_apex": fc[s], "F_apex": FA, "identity_resid": ident}
                if fixed:
                    Fa, ca = window_avgs(geo, us, t0a); Fb, cb = window_avgs(geo, us, t0b)
                    ch.update({"F_avg": Fa, "F_avg_window_diff": abs(Fa - Fb), "frame_avg_window_a": ca,
                               "frame_avg_window_b": cb, "frame_avg_window_diff": abs(ca - cb), "apex_minus_avg": abs(FA - Fa)})
                # plants
                if fc[s] is not None:
                    wrong = {"1": "i", "i": "1", "j": "k", "k": "j"}[s]
                    hw = HALF[wrong]
                    ch["P5"] = abs(fc[s] - (L.F_shift((uA[0] + hw[0], uA[1] + hw[1]), tauA) + math.pi * math.log(tauA.imag) + C0))
                    ch["P6"] = abs(fc[s] - (FA + C0))
                    cA_ = transport(c, gA)
                    ch["P7"] = abs(fc[s] - (L.F_shift((cA_[0] + hs[0], cA_[1] + hs[1]), tauA) + math.pi * math.log(tauA.imag) + C0))
                row["channels"][s] = ch
            row["Ztot1"] = z1.get((lev, i, j))
            rows.append(row)
        # 3d: the shifted Hecke formula at s = 2 for the level's first character
        o = chars[0]; c = (Fr(o["i"], o["N"]), Fr(o["j"], o["N"])); Jc = (-c[1], c[0])
        t, h = geo.nodes(NODES); lhs = h * sum(L.E_shift_reduced(Jc, geo.z(tt), 2) for tt in t)
        Gc = M if geo.tr > 0 else [[-M[0][0], -M[0][1]], [-M[1][0], -M[1][1]]]
        rhs = 0.0
        for same in (True, False):
            w = L.cone_vectors(geo, same)[0]
            rhs += L.shifted_cone_brute(geo, w, Gc, Jc, 2)[0] + L.shifted_cone_brute(geo, w, Gc, (-Jc[0], -Jc[1]), 2)[0]
        rhs *= L.H(2)
        # 3e: <F_Jc> against (pi/2l) Z_tot(1, chi_c), best affine fit
        lr = [r for r in rows if tuple(r["level"]) == lev and r["channels"]["1"].get("F_avg") is not None]
        X = np.array([math.pi / (2 * geo.ell) * r["Ztot1"] for r in lr]); Yv = np.array([r["channels"]["1"]["F_avg"] for r in lr])
        if len(lr) >= 4:
            A = np.vstack([X, np.ones_like(X)]).T; coef, *_ = np.linalg.lstsq(A, Yv, rcond=None)
            resid = float(np.max(np.abs(A @ coef - Yv)))
        else:
            coef, resid = [None, None], None
        lev_rows.append({"level": list(lev), "ell": geo.ell, "apex_t": ts, "apex": [tauA.real, tauA.imag], "apex_height": hA,
                         "hecke_s2": {"lhs": lhs, "rhs": rhs, "rel": abs(lhs - rhs) / abs(lhs)},
                         "affine_fit_F_on_Z1": {"slope": None if coef[0] is None else float(coef[0]),
                                                "intercept": None if coef[1] is None else float(coef[1]), "max_resid": resid, "n": len(lr)}})
        print(lev, len(chars), "characters", round(time.time() - t00, 1), "s", flush=True)
    allch = [(r, s, ch) for r in rows for s, ch in r["channels"].items()]
    fx = [ch for (_, _, ch) in allch if ch["fixed"]]
    def mx(key, pool): v = [ch[key] for ch in pool if ch.get(key) is not None]; return (max(v) if v else None, len(v))
    def over(key, pool, thr=1e-6): v = [ch[key] for ch in pool if ch.get(key) is not None]; return (sum(x > thr for x in v), len(v))
    lv_frame_diff = {}
    for (r, s, ch) in allch:
        if ch.get("frame_avg_window_diff") is not None:
            k = tuple(r["level"]); lv_frame_diff[k] = max(lv_frame_diff.get(k, 0), ch["frame_avg_window_diff"])
    summary = {
        "characters": len(rows), "channel_entries": len(allch), "fixed_entries": len(fx), "C": C0,
        "3a_max_identity_resid": mx("identity_resid", [ch for (_, _, ch) in allch]),
        "3b_max_F_avg_window_diff": mx("F_avg_window_diff", fx),
        "3b_levels_where_frame_avg_moves_>1e-6": [sum(v > 1e-6 for v in lv_frame_diff.values()), len(lv_frame_diff)],
        "3c_apex_differs_from_avg_>1e-6": over("apex_minus_avg", fx),
        "3d_max_hecke_s2_rel": max(l["hecke_s2"]["rel"] for l in lev_rows),
        "3e_affine_fit_resid_by_level": {" ".join(map(str, l["level"])): l["affine_fit_F_on_Z1"]["max_resid"] for l in lev_rows},
        "plants": {"P5 wrong channel shift": over("P5", [ch for (_, _, ch) in allch]),
                   "P6 pi log Im dropped": over("P6", [ch for (_, _, ch) in allch]),
                   "P7 c for Jc": over("P7", [ch for (_, _, ch) in allch])}}
    exp = json.load(open(HERE / "expectations_steps34.json"))
    e = exp["expect"]
    fitres = [v for v in summary["3e_affine_fit_resid_by_level"].values() if v is not None]
    def frac_ok(t, q): return t[1] > 0 and t[0] >= q * t[1]
    summary["against_expectations"] = {
        "3a": summary["3a_max_identity_resid"][0] <= e["3a_identity"],
        "3b_canonical": summary["3b_max_F_avg_window_diff"][0] <= e["3b_F_window"],
        "3b_frame_moves": summary["3b_levels_where_frame_avg_moves_>1e-6"][0] == summary["3b_levels_where_frame_avg_moves_>1e-6"][1],
        "3c": frac_ok(summary["3c_apex_differs_from_avg_>1e-6"], 0.99),
        "3d": summary["3d_max_hecke_s2_rel"] <= e["3d_hecke_s2"],
        "3e": all(v > e["3e_fit_resid"] for v in fitres),
        "P5": frac_ok(summary["plants"]["P5 wrong channel shift"], 0.99),
        "P6": frac_ok(summary["plants"]["P6 pi log Im dropped"], 0.99),
        "P7": frac_ok(summary["plants"]["P7 c for Jc"], 0.99)}
    json.dump({"summary": summary, "levels": lev_rows, "rows": rows}, open(out_path, "w"), indent=1,
              default=lambda o: o.item() if hasattr(o, "item") else str(o))
    print(json.dumps(summary, indent=1, default=lambda o: o.item() if hasattr(o, "item") else str(o)))


if __name__ == "__main__":
    main()
