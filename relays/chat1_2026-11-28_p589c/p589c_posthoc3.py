#!/usr/bin/env python3
"""POST HOC, third (written after the referee read of P-589 (c), which found the cause of the order-12 residue): on
Re tau = 0 B1667's track() and solve_accessory() do not fix the accessory parameter c, because the realness conditions
(Im tr A_a = Im tr A_b = 0) hold there for every real c; at_tau() kept c = 8.19e-4 at 1.6i, 3.1i and 3.5i alike. At
3.1i that gives L_max = 4508, a horoball radius at the bisection floor, and theta sums that lose digits. This check
re-reads P1's 1.6i half and both halves of P2 with c on its uniformising branch. Uses p589c_exact_rows.py's functions;
the same checkout rule. Data-free.

    python3 -B p589c_posthoc3.py <a checkout of main at 88a1e9474>      # writes p589c_posthoc3.json

The uniformising c on Re tau = 0, fixed here: c_eps = solve_accessory(eps + iy, track(eps + iy)) for eps = 0.01,
0.005 and 0.0025, and c* = Re c_0.0025 (the limit by continuity from Re tau > 0; the spread over eps is printed). The
geometry is B1838's geometry(iy, c*); its L_max and L_2 are printed beside B1667's column at Re tau = 1/4, and the
smallest horoball margin that twisted_norms returns is printed for each horocycle.

Re-read with that geometry, as p589c_exact_rows.py reads them (small-cut norms from the column, exact norms from the
geometry, the same lines, sectors and readings):
  Q0 control: with the stuck c at 3.1i, the largest exact order-12 lepton m1/m3 reproduces the committed 8.814e-10.
  Q1 P1's 1.6i half (row 315): max |m2/m3 - 1|, max m1/m3 and the worst small-exact difference.
  Q2 P2 at order 12, 3.1i, 48 lines (B1712's zero) and at order 9, 3.5i, 36 lines (B1711's lift).
Reading rule, stated before the run:
  - the order-12 zero holds at the exact norms if every exact m1/m3 is at most 1e-12 on all 48 lines, both horocycles
    and both readings; the committed residue is then the stuck accessory parameter's, and the lift is retracted;
    otherwise the lines above 1e-12 are named and the lift stands open;
  - the order-9 electron is lifted on every line if every exact m1/m3 exceeds 1e-12; P2's sealed 1e-6 is reported
    beside it;
  - P1's 1.6i half holds if the worst small-exact difference is below 1e-8.
"""
pass  # [copy: loader replaced, see MANIFEST.md]
import json
import math
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
import p589c_exact_rows as RW  # [copy: loader replaced, see MANIFEST.md]


def uniformising(EE, y):
    C = EE.C
    cs = {}
    for eps in (0.01, 0.005, 0.0025):
        t = complex(eps, y)
        c, r = C.solve_accessory(t, C.track(t))
        cs[eps] = complex(c)
    return cs[0.0025].real, cs


def spectra_with_margin(EE, tau, G, Lcol, w, sec, readings):
    """p589c_exact_rows.sector_spectra, also returning the smallest horoball margin of each horocycle"""
    B, K = EE.B, EE.K
    lf, rf = K.SECT[sec]
    x, yy = B.sector_twists(w, tau, B.SIXY[lf], B.SIXY[rf])
    R = B.residues(x, yy, tau)
    cs = B.cA(x, yy, tau, R)
    out, marg = {}, {}
    for h in ("L_max", "L_2"):
        Nx, m = EE.twisted_norms(tau, G["al"], G["be"], G[h], x, yy, R)
        marg[h] = float(m)
        small = {s: (2 * math.pi * Lcol[h] + cs[s] if cs[s] is not None else None) for s in B.UNITS}
        for which, norms in (("small", small), ("exact", Nx)):
            u = {s: (math.sqrt(norms[s]) * R[s] if norms.get(s) is not None and norms[s] > 0 else 0) for s in B.UNITS}
            Mw = B.weighted_M(u)
            for rn, H in readings.items():
                sv = np.linalg.svd(B.coupling(H, Mw), compute_uv=False)
                out[(h, which, rn)] = (float(sv[1] / sv[0]), float(sv[2] / sv[0]))
    return out, marg


def main():
    EE, root = RW.load(sys.argv[1])
    B = EE.B
    out = {}
    geo = {}
    for y in (1.6, 3.1, 3.5):
        cstar, cs = uniformising(EE, y)
        tau = complex(0, y)
        G = EE.geometry(tau, cstar)
        _, Lcol, _ = RW.at_tau(EE, tau)
        geo[y] = (G, Lcol)
        spread = max(abs(cs[a] - cs[0.0025]) for a in cs)
        print("tau = %si: c* = %.6f (eps 0.01, 0.005, 0.0025: %s; spread %.1e, largest |Im| %.1e); "
              "L_max %.4f, L_2 %.4f; column L_max %.4f, L_2 %.4f"
              % (y, cstar, ", ".join("%.6f" % cs[e].real for e in cs), spread,
                 max(abs(v.imag) for v in cs.values()), G["L_max"], G["L_2"], Lcol["L_max"], Lcol["L_2"]), flush=True)
        out["geometry_%s" % y] = {"c_star": cstar, "c_eps": {str(k): [v.real, v.imag] for k, v in cs.items()},
                                  "L_max": G["L_max"], "L_2": G["L_2"], "col": Lcol}
    # Q0: the stuck geometry reproduces the committed residue
    tau = complex(0, 3.1)
    Gs, Lcol, _ = RW.at_tau(EE, tau)
    rd = EE.higgs(tau)
    q0 = 0.0
    for (a, b) in RW.lines_of_order(12):
        sp = RW.sector_spectra(EE, tau, Gs, Lcol, float(a) * tau + float(b), "lep", rd)
        q0 = max(q0, max(v[1] for k, v in sp.items() if k[1] == "exact"))
    print("Q0: with the stuck c, the largest exact order-12 lepton m1/m3 is %.3e (committed: 8.814e-10)" % q0,
          flush=True)
    out["Q0"] = q0
    # Q1: P1's 1.6i half
    lines = [(RW.Fr(j, 6), RW.Fr(k, 6)) for j in range(6) for k in range(6) if RW.tied(RW.Fr(j, 6), RW.Fr(k, 6))][:9]
    tau = complex(0, 1.6)
    G, Lcol = geo[1.6]
    stat = {"small": [0.0, 0.0], "exact": [0.0, 0.0]}
    worst, mg = 0.0, {"L_max": np.inf, "L_2": np.inf}
    for (a, b) in lines:
        u = RW.tied(a, b)
        av = [0, 0, 0]
        av["ijk".index(u)] = 1
        S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
        rdp = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T, "conjS": np.conj(S)}
        w = float(a) * tau + float(b)
        for sec in ("up", "down", "lep"):
            sp, m = spectra_with_margin(EE, tau, G, Lcol, w, sec, rdp if sec == "up" else {"S": S})
            for h in m:
                mg[h] = min(mg[h], m[h])
            for (h, which, rn), (m2, m1) in sp.items():
                stat[which][0] = max(stat[which][0], abs(m2 - 1))
                stat[which][1] = max(stat[which][1], m1)
                if which == "exact":
                    s2, s1 = sp[(h, "small", rn)]
                    worst = max(worst, abs(abs(m2 - 1) - abs(s2 - 1)), abs(m1 - s1))
    q1 = worst < 1e-8
    print("Q1 (P1 at 1.6i): max |m2/m3 - 1|, max m1/m3: small %s, exact %s; worst difference %.2e; margins %s"
          % (["%.2e" % v for v in stat["small"]], ["%.2e" % v for v in stat["exact"]], worst,
             {h: round(v, 4) for h, v in mg.items()}), flush=True)
    out["Q1"] = {"max": stat, "worst_diff": worst, "margins": mg, "holds": q1}
    # Q2: P2 at the uniformising geometry
    q2 = {}
    for N, y in ((12, 3.1), (9, 3.5)):
        tau = complex(0, y)
        G, Lcol = geo[y]
        rd = EE.higgs(tau)
        vals = {"small": [], "exact": []}
        per_line, mg = {}, {"L_max": np.inf, "L_2": np.inf}
        for (a, b) in RW.lines_of_order(N):
            sp, m = spectra_with_margin(EE, tau, G, Lcol, float(a) * tau + float(b), "lep", rd)
            for h in m:
                mg[h] = min(mg[h], m[h])
            for (h, which, rn), (m2, m1) in sp.items():
                vals[which].append(m1)
            per_line["%s,%s" % (a, b)] = min(v[1] for k, v in sp.items() if k[1] == "exact"), \
                max(v[1] for k, v in sp.items() if k[1] == "exact")
        q2[N] = {k: [min(v), max(v)] for k, v in vals.items()}
        q2[N]["margins"] = mg
        q2[N]["per_line_exact_min_max"] = per_line
        print("Q2 order %d at %si: %d lines; lepton m1/m3 small [%.2e, %.2e], exact [%.2e, %.2e]; margins %s"
              % (N, y, len(per_line), *q2[N]["small"], *q2[N]["exact"], {h: round(v, 4) for h, v in mg.items()}),
              flush=True)
    zero12 = q2[12]["exact"][1] <= 1e-12
    lift9 = q2[9]["exact"][0] > 1e-12
    above = [k for k, v in q2[12]["per_line_exact_min_max"].items() if v[1] > 1e-12]
    out["Q2"] = {str(k): v for k, v in q2.items()}
    out["reading"] = {"order12_zero_holds": zero12, "order12_lines_above_1e-12": above, "order9_lifted": lift9,
                      "order9_above_1e-6_everywhere": q2[9]["exact"][0] > 1e-6, "P1_1.6i_holds": q1}
    print()
    print("reading: order-12 zero at the exact norms %s%s; order-9 electron lifted on every line %s (above 1e-6 "
          "everywhere %s); P1's 1.6i half %s" % (
              "HOLDS (the committed residue was the stuck accessory parameter's; the lift is retracted)" if zero12
              else "does not hold", "" if zero12 else " on %d lines: %s" % (len(above), "; ".join(above)),
              "yes" if lift9 else "no", "yes" if q2[9]["exact"][0] > 1e-6 else "no", "holds" if q1 else "FAILS"))
    json.dump(out, open("p589c_posthoc3.json", "w"), indent=1, default=str)


if __name__ == "__main__":
    main()
