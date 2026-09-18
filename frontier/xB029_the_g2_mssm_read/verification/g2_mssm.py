"""xB029 -- the G2-MSSM (arXiv:0801.0478) read at source.  SEALED at 9150fe94.

G1  the source's own arithmetic, recomputed
G3  the Ray-Singer torsion lead: |Tor H_1| on the object's tower, cusped AND closed
"""
import json
import math
import os
import sys
import warnings

warnings.filterwarnings("ignore")
from mpmath import mp

mp.dps = 40
R = {}


# ---------------------------------------------------------------- G1
def G1():
    print("\nG1       THE SOURCE'S OWN ARITHMETIC, RECOMPUTED")
    ok = True

    # (a) eq. (8):  P_eff = 28(Q-P) / (3(Q-P) - 8)
    def peff_eq8(d):
        den = 3 * d - 8
        return None if den == 0 else 28 * d / den
    a3, a4 = peff_eq8(3), peff_eq8(4)
    print(f"  (a) eq.(8) P_eff = 28(Q-P)/(3(Q-P)-8)")
    print(f"      Q-P = 3 -> {a3}   source's text: 84")
    print(f"      Q-P = 4 -> {a4}   source's text: 28")
    a_ok = (a3 == 84.0 and a4 == 28.0)
    print(f"      reproduces BOTH numbers the source states: {a_ok}")
    ok &= a_ok
    tbl = {d: peff_eq8(d) for d in range(3, 9)}
    print(f"      the whole family: {tbl}")
    print(f"      monotone decreasing in Q-P (the source's sentence): "
          f"{all(tbl[d] > tbl[d+1] for d in range(3, 8))}")

    # (b) eq. (A9)/(A12) on the source's worked example
    P, Q, M, lam, k, V7 = 15, 18, 10, 80, 99, 50
    G = P + M + 1
    T_O = -math.log(k)
    T_lam = math.log(4 * math.sin(G * math.pi * lam / k) ** 2)
    peff = -T_O - M * T_lam
    print(f"  (b) worked example P={P} Q={Q} M={M} lambda={lam} k={k}, G=P+M+1={G}")
    print(f"      T_O   = -log k            = {T_O:.6f}")
    print(f"      T_lam = log(4 sin^2(G pi lambda / k)) = {T_lam:.6f}")
    print(f"      P_eff = -T_O - M T_lam    = {peff:.4f}     source's text: 58")
    b_ok = abs(peff - 58.0) < 2.0
    print(f"      reproduces the source's 58 (tol 2): {b_ok}")
    print(f"      note where the size comes from: log k contributes {-T_O:.3f},")
    print(f"      the tuned flat connection contributes {-M*T_lam:.3f} "
          f"({100*(-M*T_lam)/peff:.1f}% of the total)")
    frac = (G * lam / k) % 1.0
    print(f"      the tuning, made explicit: G*lambda/k = {G*lam/k:.6f}, fractional part "
          f"{frac:.6f} -- it must sit close to an INTEGER for 4 sin^2 to be small")
    ok &= b_ok

    # (c) moduli-count bound  N < 14 Q / ((3(Q-P) - 8) pi)
    def nbound(Qv, d):
        return 14 * Qv / ((3 * d - 8) * math.pi)
    c = {d: nbound(18, d) for d in range(3, 7)}
    print(f"  (c) N < 14Q/((3(Q-P)-8)pi), at Q=18: {({d: round(v,2) for d, v in c.items()})}")
    c_ok = all(c[d] > c[d + 1] for d in range(3, 6))
    print(f"      shrinks as Q-P grows -- the source's reason for discarding Q-P>3: {c_ok}")
    ok &= c_ok

    R["G1"] = {"eq8": {"Q-P=3": a3, "Q-P=4": a4, "family": tbl, "ok": bool(a_ok)},
               "example": {"P": P, "Q": Q, "M": M, "lambda": lam, "k": k, "G": G,
                           "T_O": T_O, "T_lambda": T_lam, "P_eff": peff,
                           "source_states": 58, "ok": bool(b_ok),
                           "share_from_tuned_connection": -M * T_lam / peff},
               "n_bound": c, "ok": bool(ok)}
    print(f"G1 {'PASS' if ok else 'FAIL'}")
    return ok


# ---------------------------------------------------------------- G3
def lucas(m):
    a, b = 2, 1                      # L_0 = 2, L_1 = 1
    for _ in range(m):
        a, b = b, a + b
    return a


def G3(NMAX=120):
    print("\nG3       THE TORSION LEAD -- |Tor H_1| on the object's tower")
    print("         Appendix A: P_eff = -T_O - M T_lambda, with T_O = -log k = -log|H_1(S^3/Z_k)|.")
    print("         Read at natural generality: the FIRST term is log|Tor H_1(Qhat)| and needs")
    print("         NO tuned flat connection.  Measured here on b++(LR)^n, xB027's driver.")
    import snappy
    alpha = (3 + mp.sqrt(5)) / 2
    logalpha = mp.log(alpha)
    print(f"         sealed constants: alpha = (3+sqrt5)/2 = {mp.nstr(alpha, 12)}, "
          f"log alpha = {mp.nstr(logalpha, 10)}")

    rows = []
    bad = []
    grew = False
    for n in range(1, NMAX + 1):
        try:
            Mn = snappy.Manifold("b++" + "LR" * n)
            H = Mn.homology()
            tor = 1
            for d in H.elementary_divisors():
                if d:
                    tor *= d
        except Exception as e:
            bad.append((n, f"err {type(e).__name__}"))
            break
        pred = lucas(2 * n) - 2
        if tor != pred:
            bad.append((n, tor, pred))
        if tor > 1:
            grew = True
        rows.append((n, tor, pred, float(mp.log(tor)) if tor > 1 else 0.0))
        if n <= 8 or n % 20 == 0:
            print(f"           n={n:3d}  |Tor H_1| = {str(tor)[:34]:34s}  "
                  f"L_{2*n}-2 = {str(pred)[:34]:34s}  match {tor == pred}")
    nrun = len(rows)
    print(f"         ran n = 1..{nrun}; closed-form mismatches: {len(bad)}  {bad[:4]}")
    print(f"         VACUITY CONTROL -- torsion actually grows: {grew}; "
          f"n=1 torsion-free (H_1(m004) = Z): {rows[0][1] == 1}")

    # growth constant, measured
    n_hi = rows[-1][0]
    meas = rows[-1][3] / n_hi
    dev = abs(meas - float(logalpha)) / float(logalpha)
    print(f"         measured growth: log|Tor|/n at n={n_hi} is {meas:.9f}")
    print(f"         sealed prediction log alpha = {float(logalpha):.9f}; "
          f"relative deviation {dev:.3e}  (<1% required: {dev < 0.01})")

    # the crossing
    cross = next((r[0] for r in rows if r[3] >= 84.0), None)
    volm004 = float(snappy.Manifold("m004").volume())
    print(f"         FIRST n with log|Tor H_1| >= 84: {cross}   (sealed prediction: 88)")
    if cross:
        print(f"           n={cross-1}: log|Tor| = {rows[cross-2][3]:.4f}   "
              f"n={cross}: log|Tor| = {rows[cross-1][3]:.4f}")
        print(f"           cusped volume there = {cross} x {volm004:.6f} = {cross*volm004:.2f}")
    bv = 84 * 6 * math.pi
    print(f"         under the Bergeron-Venkatesh closed rate 1/(6pi) the same 84 would need")
    print(f"           volume {bv:.1f} -- a factor {bv/(cross*volm004):.2f} more" if cross else "")

    # ---- FENCE 2, MEASURED: the closed side
    print("         FENCE 2, MEASURED -- Qhat must be COMPACT and the tower is CUSPED.")
    print("         The closed counterpart is the n-fold cyclic BRANCHED cover: fill the")
    print("         knot's meridian first, then take the cyclic cover.")
    closed = []
    K = snappy.Manifold("4_1")
    for n in range(2, 13):
        try:
            K.dehn_fill((1, 0))
            cv = K.covers(n, cover_type="cyclic")
            if not cv:
                closed.append((n, "no cover")); continue
            c0 = cv[0]
            H = c0.homology()
            tor = 1
            for d in H.elementary_divisors():
                if d:
                    tor *= d
            vol = None
            try:
                vol = float(c0.volume())
            except Exception:
                pass
            closed.append((n, str(H), tor, lucas(2 * n) - 2, c0.num_cusps(), vol))
        except Exception as e:
            closed.append((n, f"err {type(e).__name__}: {e}"))
    for row in closed:
        print(f"           branched n={row[0]}: {row[1:]}")
    match_closed = [r for r in closed if len(r) > 3 and r[2] == r[3]]
    print(f"         closed side matches L_2n - 2 on {len(match_closed)} of "
          f"{len([r for r in closed if len(r) > 3])} computed")

    R["G3"] = {"n_run": nrun, "closed_form_mismatches": bad,
               "rows_head": rows[:8], "rows_tail": rows[-3:],
               "measured_growth_per_degree": meas,
               "sealed_log_alpha": float(logalpha), "rel_dev": dev,
               "crossing_n": cross, "sealed_crossing": 88,
               "cusped_volume_at_crossing": (cross * volm004) if cross else None,
               "bv_volume_for_84": bv, "grew": bool(grew),
               "closed_branched": [list(map(str, r)) for r in closed]}
    ok = (not bad) and grew and dev < 0.01 and cross == 88
    print(f"G3 {'PASS' if ok else 'FAIL'}  (all four sealed conditions; content is the verdict above)")
    return ok


if __name__ == "__main__":
    only = sys.argv[1:] or None
    cells = {"G1": G1, "G3": G3}
    res = {}
    for k, f in cells.items():
        if only and k not in only:
            continue
        try:
            res[k] = bool(f())
        except Exception as e:
            print(f"{k} EXCEPTION {type(e).__name__}: {e}")
            res[k] = False
    print("\n" + "=" * 78)
    print("ALL SEALED CONDITIONS MET" if all(res.values()) else "NOT ALL CELLS PASSED")
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "g2_mssm.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump({"cells": res, "results": R}, fh, indent=1, default=str)
