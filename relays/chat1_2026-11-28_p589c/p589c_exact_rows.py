#!/usr/bin/env python3
"""P-589 (c): the law map's data-free rows 'at the canonical end' re-read at the exact horoball norms. Data-free:
nothing is compared with a measured number.

    python3 -B p589c_exact_rows.py <a checkout of main at 88a1e9474>      # writes p589c_exact_rows.json beside itself

It imports main's frame and B1667's geometry through B1838's instrument (frontier/B1838_the_end/verification/
exact_end_web_seat.py: geometry() and twisted_norms(), the exact norm of each of B1656's four twisted channels over
B1667's Dirichlet cell minus the horoball at L_max(tau) or L_2(tau)), and refuses a checkout at any other commit.

The law map's scope note (row 299, S297): main's frame takes the end through the small-cut norm 2 pi L + c_s, with L
from B1667's column at Re tau = 1/4; "a result 'at the canonical end' is a result of that formula". Here each tested
quantity is computed twice, with that small-cut norm ("small") and with the exact twisted norm at the same horocycle
("exact"), and the row's statement is read under both.

Rows re-read (the law map at 88a1e9474):
  315 B1701, the line-tied Higgs is degenerate: on the lines with 6w in the lattice whose tie p* = -3w is a
      half-period, with the Higgs the unit C_{p*} (B1701's tie), every sector's spectrum has a degenerate pair.
      Tested: the nine tied lines with alpha, b in {0, 1/2, ...} of B1701's list (all 27 if fewer), at tau = 1.6i and
      0.5 + 2.4i, every sector, both horocycles, readings S and S~ (and conj S for up): max |m2/m3 - 1| and max m1/m3,
      small against exact.
  313 B1703's dated notes (B1711, B1712): at the canonical end the order-9 lines' electron is lifted (B1711) and the
      order-12 lines' electron is exactly massless (B1712). Tested with the end-data Higgs (B1691's dR, readings S and
      S~): the leptons' m1/m3 on every order-12 line (up to sign) at tau = 3.1i and on every order-9 line at 3.5i.
  324 B1729, the leptons' coarser line: R2 = (m2/m3)_lep / (m2/m3)_down and R1 = (m1/m3)_down / (m1/m3)_lep, down and
      leptons in one reading, on lines of exact order N in {5, 10, 13, 15, 21, 24, 30} (up to 16 lines per order,
      seeded), at B1729's two tau moved into the cell by T (0.55 + 3.05i -> -0.45 + 3.05i, line (a, b) -> (a, b + a);
      0.35 + 2.75i unchanged), both horocycles. The median log R2 and log R1 for 3 | N against 3 not dividing N.
Rows not re-read here, with the reason (stated in the relay): 295 (B1657; its end statement is B1654's large-L
condition, where the small-cut norm is the exact norm's expansion), 312 (B1692) and 352 (B1807), whose canonical-end
statements come from section-by-section computations this script does not reproduce; and the data-facing rows.

Cells and expectations, written before the run (probabilities are this seat's):
  P0 control: at 0.25 + 3.0i the instrument's L_max, L_2 and B1667's untwisted horoball norms reproduce B1667's json
     to 1e-6 (98 %).
  P1 row 315: with the exact norms, max |m2/m3 - 1| and max m1/m3 over every tested tied line, sector, horocycle and
     reading equal the small-cut values to 1e-8, so the degeneracy is the coupling's, not the norm's (80 %).
  P2 row 313's notes: with the exact norms the leptons' m1/m3 is below 1e-12 on every order-12 line (both horocycles,
     both readings) (80 %), and above 1e-6 on every order-9 line, the electron lifted (75 %).
  P3 row 324: order-5 lines give R2 = R1 = 1 to 1e-10 with the exact norms (95 %); the exact norms move the median
     log R2 of the 3 | N lines, relative to the others, by less than 0.3 from its small-cut value, so B1729's NEGATIVE
     (no Georgi-Jarlskog factor, which needs log 3) stands (80 %).
"""
import contextlib
import io
import json
import math
import pathlib
import random
import subprocess
import sys
from fractions import Fraction as Fr

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
REV = "88a1e9474"


def load(main_dir):
    root = pathlib.Path(__file__).resolve().parent / "main_tree"  # [copy: loader replaced, see MANIFEST.md]
    with contextlib.redirect_stdout(io.StringIO()):
        import exact_end_web_seat as ee  # [copy: loader replaced, see MANIFEST.md]
    return ee, root


def at_tau(EE, tau):
    C = EE.C
    c = C.track(tau)
    c, res = C.solve_accessory(tau, c)
    G = EE.geometry(tau, c)
    col = EE.M["col"]
    Lcol = {"L_max": float(np.interp(tau.imag, [q[0] for q in col], [q[1] for q in col])),
            "L_2": float(np.interp(tau.imag, [q[0] for q in col], [q[2] for q in col]))}
    return G, Lcol, res


def sector_spectra(EE, tau, G, Lcol, w, sec, readings):
    """{(horocycle, which, reading): (m2/m3, m1/m3)} for one sector at one line."""
    B, K = EE.B, EE.K
    lf, rf = K.SECT[sec]
    x, yy = B.sector_twists(w, tau, B.SIXY[lf], B.SIXY[rf])
    R = B.residues(x, yy, tau)
    cs = B.cA(x, yy, tau, R)
    out = {}
    for h in ("L_max", "L_2"):
        Nx, _ = EE.twisted_norms(tau, G["al"], G["be"], G[h], x, yy, R)
        small = {s: (2 * math.pi * Lcol[h] + cs[s] if cs[s] is not None else None) for s in B.UNITS}
        for which, norms in (("small", small), ("exact", Nx)):
            u = {s: (math.sqrt(norms[s]) * R[s] if norms.get(s) is not None and norms[s] > 0 else 0) for s in B.UNITS}
            Mw = B.weighted_M(u)
            for rn, H in readings.items():
                sv = np.linalg.svd(B.coupling(H, Mw), compute_uv=False)
                out[(h, which, rn)] = (float(sv[1] / sv[0]), float(sv[2] / sv[0]))
    return out


def lines_of_order(N):
    seen, out = set(), []
    for j in range(N):
        for k in range(N):
            if math.gcd(math.gcd(j, k), N) != 1:
                continue
            key = min((j, k), ((-j) % N, (-k) % N))
            if key not in seen:
                seen.add(key)
                out.append((Fr(key[0], N), Fr(key[1], N)))
    return out


UNIT = {(Fr(1, 2), Fr(0)): "j", (Fr(0), Fr(1, 2)): "i", (Fr(1, 2), Fr(1, 2)): "k"}


def tied(a, b):
    return UNIT.get(((-3 * a) % 1, (3 * b) % 1))


def main():
    EE, root = load(sys.argv[1])
    B = EE.B
    res, out = {}, {}
    # P0
    tau0 = complex(0.25, 3.0)
    d = json.loads((root / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json")
                   .read_text())
    ref = min((p for p in d["points"] if p["where"] == "grid"), key=lambda p: abs(complex(*p["tau"]) - tau0))
    G0, _, _ = at_tau(EE, tau0)
    Nmax, _ = EE.C.horoball_norms(tau0, G0["al"], G0["be"], G0["L_max"])
    N2, _ = EE.C.horoball_norms(tau0, G0["al"], G0["be"], G0["L_2"])
    dev = max([abs(G0["L_max"] / ref["L_max"] - 1), abs(G0["L_2"] / ref["L_2"] - 1)]
              + [abs(Nmax[r] / ref["N_max"][str(r)] - 1) for r in (2, 3, 4)]
              + [abs(N2[r] / ref["N_2"][str(r)] - 1) for r in (2, 3, 4)])
    res["P0"] = dev < 1e-6
    print("P0 at %s: max relative deviation from B1667's json %.2e" % (tau0, dev), flush=True)
    # P1: row 315
    lines = [(Fr(j, 6), Fr(k, 6)) for j in range(6) for k in range(6) if tied(Fr(j, 6), Fr(k, 6))]
    lines = lines[:9]
    stat = {"small": [0.0, 0.0], "exact": [0.0, 0.0]}
    worst_diff = 0.0
    for tau in (complex(0, 1.6), complex(0.5, 2.4)):
        G, Lcol, r = at_tau(EE, tau)
        for (a, b) in lines:
            u = tied(a, b)
            av = [0, 0, 0]
            av["ijk".index(u)] = 1
            S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
            rd = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T, "conjS": np.conj(S)}
            w = float(a) * tau + float(b)
            for sec in ("up", "down", "lep"):
                sp = sector_spectra(EE, tau, G, Lcol, w, sec, rd if sec == "up" else {"S": S})
                for (h, which, rn), (m2, m1) in sp.items():
                    stat[which][0] = max(stat[which][0], abs(m2 - 1))
                    stat[which][1] = max(stat[which][1], m1)
                for (h, which, rn), (m2, m1) in sp.items():
                    if which == "exact":
                        s2, s1 = sp[(h, "small", rn)]
                        worst_diff = max(worst_diff, abs(abs(m2 - 1) - abs(s2 - 1)), abs(m1 - s1))
        print("P1 tau = %s done (accessory residual %.1e)" % (tau, float(np.max(np.abs(r)))), flush=True)
    res["P1"] = worst_diff < 1e-8
    out["P1"] = {"lines": [[str(a), str(b), tied(a, b)] for a, b in lines], "max": stat, "worst_diff": worst_diff}
    print("P1 row 315: max |m2/m3 - 1|, max m1/m3: small %s, exact %s; worst difference %.2e"
          % (["%.2e" % v for v in stat["small"]], ["%.2e" % v for v in stat["exact"]], worst_diff), flush=True)
    # P2: row 313's notes
    p2 = {}
    for N, tau in ((12, complex(0, 3.1)), (9, complex(0, 3.5))):
        G, Lcol, r = at_tau(EE, tau)
        rd = EE.higgs(tau)
        vals = {"small": [], "exact": []}
        for (a, b) in lines_of_order(N):
            sp = sector_spectra(EE, tau, G, Lcol, float(a) * tau + float(b), "lep", rd)
            for (h, which, rn), (m2, m1) in sp.items():
                vals[which].append(m1)
        p2[N] = {k: [min(v), max(v)] for k, v in vals.items()}
        print("P2 order %d at %s: %d lines; lepton m1/m3 small [%.2e, %.2e], exact [%.2e, %.2e]"
              % (N, tau, len(lines_of_order(N)), *p2[N]["small"], *p2[N]["exact"]), flush=True)
    res["P2"] = p2[12]["exact"][1] < 1e-12 and p2[9]["exact"][0] > 1e-6
    out["P2"] = {str(k): v for k, v in p2.items()}
    # P3: row 324
    rng = random.Random(1729)
    p3 = {"small": {"3|N": [], "other": []}, "exact": {"3|N": [], "other": []}}
    p3r1 = {"small": {"3|N": [], "other": []}, "exact": {"3|N": [], "other": []}}
    order5 = 0.0
    for tau, shift in ((complex(-0.45, 3.05), True), (complex(0.35, 2.75), False)):
        G, Lcol, r = at_tau(EE, tau)
        rd = EE.higgs(tau)
        for N in (5, 10, 13, 15, 21, 24, 30):
            ls = lines_of_order(N)
            if len(ls) > 16:
                ls = rng.sample(ls, 16)
            for (a, b) in ls:
                bb = b + a if shift else b
                w = float(a) * tau + float(bb)
                down = sector_spectra(EE, tau, G, Lcol, w, "down", rd)
                lep = sector_spectra(EE, tau, G, Lcol, w, "lep", rd)
                for key in down:
                    h, which, rn = key
                    R2 = lep[key][0] / down[key][0]
                    R1 = down[key][1] / lep[key][1] if lep[key][1] > 0 else float("inf")
                    if N == 5 and which == "exact":
                        order5 = max(order5, abs(R2 - 1), abs(R1 - 1))
                    cls = "3|N" if N % 3 == 0 else "other"
                    p3[which][cls].append(math.log(R2))
                    if math.isfinite(R1) and R1 > 0:
                        p3r1[which][cls].append(math.log(R1))
        print("P3 tau = %s done" % tau, flush=True)
    med = {w: {c: float(np.median(v)) for c, v in p3[w].items()} for w in p3}
    medr1 = {w: {c: float(np.median(v)) for c, v in p3r1[w].items()} for w in p3r1}
    shift_r2 = abs((med["exact"]["3|N"] - med["exact"]["other"]) - (med["small"]["3|N"] - med["small"]["other"]))
    res["P3"] = order5 < 1e-10 and shift_r2 < 0.3
    out["P3"] = {"median_log_R2": med, "median_log_R1": medr1, "order5_worst": order5, "shift": shift_r2}
    print("P3 row 324: order-5 worst |R - 1| (exact) %.2e; median log R2 small %s, exact %s; shift of the 3|N"
          " difference %.3f; median log R1 small %s, exact %s"
          % (order5, {k: round(v, 3) for k, v in med["small"].items()}, {k: round(v, 3) for k, v in med["exact"].items()},
             shift_r2, {k: round(v, 3) for k, v in medr1["small"].items()},
             {k: round(v, 3) for k, v in medr1["exact"].items()}))
    (HERE / "p589c_exact_rows.json").write_text(json.dumps(out, indent=1))
    print("\n" + ", ".join("%s %s" % (k, "holds" if v else "FAILS") for k, v in res.items()))


if __name__ == "__main__":
    main()
