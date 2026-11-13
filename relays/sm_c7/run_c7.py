#!/usr/bin/env python3
"""SM-C7 steps 1 and 2, with the four planted controls, on B1737's population (relays/sm_c7/population.json).

  step 1   s(chi) + #(-I)/2  against  P_u(Jc)/(4 pi^2), the period of the u-shifted weight-2 series along the geodesic
  step 2   (a) Hecke at s = 2; (b) Hecke at s = 1, the Kronecker coefficient: the integral of -2 pi log|g_Jc| against
           (pi/2) Z_tot(1); (c) the odd part at s = 1: the period of G_c against Z_same(1) - Z_opp(1), and its
           rationality over 4 pi^2; (d) Z_tot(0) = 0 and Z_tot'(0) = -l/2
  plants   P1 a wrong character, P2 a wrong geodesic (same trace), P3 the orientation reversed, P4 a factor 2
Conventions and expectations: STEP0_CONVENTIONS_AND_EXPECTATIONS.md, expectations.json (sealed first).
Data-free.  Usage: python3 run_c7.py [population.json] [out.json]"""
import sys, json, math, cmath, time, pathlib
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import sm_c7_lib as L

NODES = 48
H0, NC = 0.3, 16
CONTOUR = [H0 * cmath.exp(2j * math.pi * k / NC) for k in range(NC)]


def integrate_w0(geo, c, fn, n=NODES):
    t, h = geo.nodes(n)
    return h * sum(L.at_reduced(c, geo.z(tt), fn) for tt in t)


def period(geo, idx, kind, n=NODES, reverse=False, scale=1.0):
    t, h = geo.nodes(n)
    fn = L.G_v_fast if kind == "v" else L.G_u_fast
    sgn = geo.sigma * (-1 if reverse else 1)
    return scale * sgn * h * sum(L.w2_reduced(idx, geo.z(tt), fn, kind) * geo.dz(tt) for tt in t)


def fixed(M, i, j, N):
    (a, b), (c, d) = M
    return ((i * a + j * c - i) % N, (i * b + j * d - j) % N) == (0, 0)


def wrong_char(M, i, j, N):
    for di, dj in ((1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (1, 2), (2, 1)):
        if not fixed(M, (i + di) % N, (j + dj) % N, N):
            return ((i + di) % N, (j + dj) % N)
    return None


def main():
    pop = json.load(open(sys.argv[1] if len(sys.argv) > 1 else HERE / "population.json"))
    out_path = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "sm_c7_results.json"
    levels = {}
    for o in pop:
        levels.setdefault(tuple(o["level"]), []).append(o)
    rows, t0 = [], time.time()
    for lev, chars in levels.items():
        M = chars[0]["M"]; geo = L.Geodesic(M)
        tr = M[0][0] + M[1][1]
        Mp = [[tr - 1, 1], [tr - 2, 1]]; geop = L.Geodesic(Mp)
        keys = [(o["i"], o["j"], o["N"]) for o in chars]
        Z = L.level_zetas(geo, keys, [2, 1, 0] + CONTOUR)
        for o in chars:
            i, j, N = o["i"], o["j"], o["N"]
            c = (Fr(i, N), Fr(j, N)); Jc = (-c[1], c[0])
            V = o["s"][0] + o["nI"] / 2
            P48 = period(geo, Jc, "u"); P96 = period(geo, Jc, "u", n=96)
            z = Z[(i, j, N)]
            ztot2, ztot1, ztot0 = sum(z[2]), sum(z[1]), sum(z[0])
            dz0 = sum(sum(z[s]) / s for s in CONTOUR) / NC
            lhs2 = integrate_w0(geo, c, lambda cc, w: L.E_fast(cc, w, 2))
            lhs1 = integrate_w0(geo, c, L.kron)
            Pv = period(geo, c, "v")
            lodd = z[1][0] - z[1][1]
            rat = Fr(lodd.real / (4 * math.pi ** 2)).limit_denominator(24 * N * N)
            # plants
            wc = wrong_char(M, i, j, N)
            p1 = None
            if wc is not None:
                cw = (Fr(wc[0], N), Fr(wc[1], N)); p1 = period(geo, (-cw[1], cw[0]), "u") / (4 * math.pi ** 2)
            p2a = period(geop, Jc, "u") / (4 * math.pi ** 2)
            p2b = integrate_w0(geop, c, L.kron)
            p3 = -P48 / (4 * math.pi ** 2)
            p4a = 2 * P48 / (4 * math.pi ** 2)
            p4b = 2 * lhs1
            rows.append({
                "level": list(lev), "N": N, "i": i, "j": j, "V": V,
                "step1": {"P/4pi2": [P48.real / (4 * math.pi ** 2), P48.imag / (4 * math.pi ** 2)],
                          "diff": abs(V - P48 / (4 * math.pi ** 2)), "nodes_48_vs_96": abs(P48 - P96)},
                "step2": {"a_s2": {"lhs": lhs2.real, "rhs": (L.H(2) * ztot2).real, "rel": abs(lhs2 - L.H(2) * ztot2) / max(1, abs(lhs2))},
                          "b_s1": {"lhs": lhs1.real, "rhs": (L.H(1) * ztot1).real, "rel": abs(lhs1 - L.H(1) * ztot1) / max(1, abs(lhs1)),
                                   "Ztot1": [ztot1.real, ztot1.imag]},
                          "c_odd": {"period": [Pv.real, Pv.imag], "Lodd1": [lodd.real, lodd.imag], "diff": abs(Pv - lodd),
                                    "Lodd1/4pi2": [rat.numerator, rat.denominator],
                                    "rational_resid": abs(lodd.real / (4 * math.pi ** 2) - float(rat))},
                          "d_s0": {"Ztot0": abs(ztot0), "Zprime0+ell/2": abs(dz0 + geo.ell / 2)}},
                "plants": {"P1": None if p1 is None else abs(V - p1), "P2_step1": abs(V - p2a),
                           "P2_step2b": abs(p2b - L.H(1) * ztot1), "P3": abs(V - p3),
                           "P4_step1": abs(V - p4a), "P4_step2b": abs(p4b - L.H(1) * ztot1)}})
        print(lev, len(chars), "characters", round(time.time() - t0, 1), "s", flush=True)
    n = len(rows)
    big = [r for r in rows if abs(r["V"]) > 1e-6]
    kbig = [r for r in rows if abs(r["step2"]["b_s1"]["lhs"]) > 1e-6]
    def frac_over(key, sub, thr=1e-6, pool=None):
        pool = rows if pool is None else pool
        vals = [r["plants"][key] for r in pool if r["plants"][key] is not None]
        return sum(v > thr for v in vals), len(vals)
    summary = {
        "characters": n, "levels": len(levels),
        "step1_max_diff": max(r["step1"]["diff"] for r in rows),
        "step1_max_nodes_48_vs_96": max(r["step1"]["nodes_48_vs_96"] for r in rows),
        "step2a_max_rel": max(r["step2"]["a_s2"]["rel"] for r in rows),
        "step2b_max_rel": max(r["step2"]["b_s1"]["rel"] for r in rows),
        "step2c_max_diff": max(r["step2"]["c_odd"]["diff"] for r in rows),
        "step2c_max_rational_resid": max(r["step2"]["c_odd"]["rational_resid"] for r in rows),
        "step2d_max_Ztot0": max(r["step2"]["d_s0"]["Ztot0"] for r in rows),
        "step2d_max_Zprime0_plus_half_ell": max(r["step2"]["d_s0"]["Zprime0+ell/2"] for r in rows),
        "characters_with_|V|>1e-6": len(big),
        "plants_caught": {
            "P1 (miss > 1e-6)": frac_over("P1", None), "P2 step 1": frac_over("P2_step1", None),
            "P2 step 2b": frac_over("P2_step2b", None), "P3 (|V| > 1e-6)": frac_over("P3", None, pool=big),
            "P4 step 1 (|V| > 1e-6)": frac_over("P4_step1", None, pool=big), "P4 step 2b (Kronecker value > 1e-6)": frac_over("P4_step2b", None, pool=kbig)}}
    exp = json.load(open(HERE / "expectations.json"))
    s2 = exp["step2"]
    summary["against_expectations"] = {
        "step1": summary["step1_max_diff"] <= exp["step1"]["tol"] and summary["step1_max_nodes_48_vs_96"] <= exp["step1"]["node_agreement"],
        "step2a": summary["step2a_max_rel"] <= s2["a_hecke_s2"], "step2b": summary["step2b_max_rel"] <= s2["b_hecke_s1_kronecker"],
        "step2c": summary["step2c_max_diff"] <= s2["c_odd_s1"] and summary["step2c_max_rational_resid"] <= 1e-9,
        "step2d": summary["step2d_max_Ztot0"] <= s2["d_Z0"] and summary["step2d_max_Zprime0_plus_half_ell"] <= s2["d_Zprime0_plus_half_ell"],
        "P1": frac_over("P1", None)[0] >= 0.99 * frac_over("P1", None)[1],
        "P2": frac_over("P2_step1", None)[0] >= 0.99 * n and frac_over("P2_step2b", None)[0] >= 0.99 * n,
        "P3": frac_over("P3", None, pool=big)[0] == len(big),
        "P4": frac_over("P4_step1", None, pool=big)[0] == len(big) and frac_over("P4_step2b", None, pool=kbig)[0] == len(kbig)}
    json.dump({"summary": summary, "rows": rows}, open(out_path, "w"), indent=1, default=lambda o: o.item() if hasattr(o, "item") else str(o))
    print(json.dumps(summary, indent=1, default=lambda o: o.item() if hasattr(o, "item") else str(o)))


if __name__ == "__main__":
    main()
