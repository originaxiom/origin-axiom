#!/usr/bin/env python3
"""W128 — is the field forced by consistency? (the rule: W128_RULE.md, committed and pushed before this script).

  C0  the instrument: rho = (e^{i pi/4} P, e^{i pi/4} L^-1)'s image group kept exactly as (k mod 8, signed
      permutation); its order and whether i.1 = rho(S)^2 is in it; B1674's character layer from
      n_G = 9 sum_f w_G(f) s_f mod 24 (W101's weights)
  C1  the gauge side, exact: one generation's anomaly-free hypercharges (sympy); the Yukawa bilinears' quantum numbers;
      the degenerate family; a Y + b (B - L) with nu^c
  C2  the flavour side, exact, with constant couplings: for each of the 64 assignments and a field in 1, T or T-bar,
      the invariants of each Yukawa bilinear by characters on the image group (exact in Z[zeta8])
  C3  the empirical bit: a READING by hand, recorded in W128's record, not here
  C4  the index-matching set I = f over W127's box (W47's index), per datum and for the field twisted by all six
      characters; W127's exact h at each matching datum
  C5  the read-out

    python3 -B the_consistency_route.py      # writes the_consistency_route.json beside itself
"""
import contextlib
import io
import itertools
import json
import sys
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_field_at_the_end as W127  # noqa: E402  (W127: UC = W47, EC = W46, the exact h)

UC, EC = W127.UC, W127.EC
OUT = HERE / "the_consistency_route.json"
TOL = 1e-9
FIELDS = ["Q", "u", "d", "L", "e", "nu"]
WEIGHTS = {"SU3": {"Q": 2, "u": 1, "d": 1}, "SU2": {"Q": 3, "L": 1},
           "grav": {"Q": 6, "u": 3, "d": 3, "L": 2, "e": 1, "nu": 1}}           # W101's
BILINEARS = {"Q u^c": ("Q", "u"), "Q d^c": ("Q", "d"), "L e^c": ("L", "e"), "L nu^c": ("L", "nu")}


# ------------------------------------------------------------------ C0. the image group, exactly
def image_group():
    Pm = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    Li = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]])                         # W123's L^-1

    def norm(k, Q):
        f = Q.flatten()
        return ((k + 4) % 8, -Q) if f[np.nonzero(f)[0][0]] < 0 else (k % 8, Q)

    def key(x):
        return (x[0], tuple(x[1].flatten()))

    gens = [norm(1, Pm), norm(1, Li), norm(-1, Pm.T), norm(-1, Li.T)]
    e = norm(0, np.eye(3, dtype=int))
    seen, frontier = {key(e): e}, [e]
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = norm(x[0] + g[0], x[1] @ g[1])
                if key(y) not in seen:
                    seen[key(y)] = y
                    nxt.append(y)
        frontier = nxt
    w8 = np.exp(1j * np.pi / 4)
    import the_higgs_route as HR                                               # W123's matrices, for the identification
    ident = max(float(np.abs(w8 * Pm - HR.rS).max()), float(np.abs(w8 * Li - HR.rT).max()))
    return list(seen.values()), (2, tuple(np.eye(3, dtype=int).flatten())) in seen, ident


def C0():
    G, has_i, ident = image_group()
    assign = [dict(zip(FIELDS, v)) for v in itertools.product((1, -1), repeat=6)]
    n_of = lambda Gn, s: (9 * sum(WEIGHTS[Gn].get(f, 0) * s[f] for f in FIELDS)) % 24
    su3 = [s for s in assign if n_of("SU3", s) == 0]
    su2 = sorted({n_of("SU2", s) for s in assign})
    grav = [s for s in su3 if n_of("grav", s) == 0]
    no_nu = [dict(zip(FIELDS[:5], v)) for v in itertools.product((1, -1), repeat=5)]
    grav_no_nu = [s for s in no_nu if (9 * sum(WEIGHTS["grav"].get(f, 0) * s[f] for f in FIELDS[:5])) % 24 == 0]
    c = {"the image group has order 96": len(G) == 96,
         "it contains i.1 = rho(S)^2": bool(has_i),
         "the generators are W123's matrices (max |difference|)": ident < 1e-12,
         "SU(3)-free = {s_u = s_d = -s_Q}, 16 of 64": su3 == [s for s in assign if s["u"] == s["d"] == -s["Q"]]
                                                       and len(su3) == 16,
         "SU(2) values {6, 12, 18}": su2 == [6, 12, 18],
         "gravity-free given SU(3)-free = {s_e = s_nu = -s_L}, 4 of 16": grav == [
             s for s in su3 if s["e"] == s["nu"] == -s["L"]] and len(grav) == 4,
         "none gravity-free without nu^c": len(grav_no_nu) == 0}
    return {"checks": c, "order": len(G), "identification residual": ident}, all(c.values()), G, assign, su3, grav


# ------------------------------------------------------------------ C1. the gauge side
def C1():
    yQ, yu, yd, yL, ye, ynu = sp.symbols("y_Q y_u y_d y_L y_e y_nu")
    eqs = [2 * yQ + yu + yd, 3 * yQ + yL, 6 * yQ + 3 * yu + 3 * yd + 2 * yL + ye,
           6 * yQ ** 3 + 3 * yu ** 3 + 3 * yd ** 3 + 2 * yL ** 3 + ye ** 3]
    lin = {yd: -2 * yQ - yu, yL: -3 * yQ, ye: 6 * yQ}                           # the three linear conditions
    assert all(sp.expand(q.subs(lin)) == 0 for q in eqs[:3])
    cubic = sp.factor(eqs[3].subs(lin))
    ratio = sp.simplify(cubic / (yQ * (yu - 2 * yQ) * (yu + 4 * yQ)))
    sm = {"Q": sp.Rational(1, 6), "u": sp.Rational(-2, 3), "d": sp.Rational(1, 3), "L": sp.Rational(-1, 2),
          "e": sp.Integer(1), "nu": sp.Integer(0)}
    relab = dict(sm, u=sp.Rational(1, 3), d=sp.Rational(-2, 3))
    on = lambda ch: all(sp.simplify(q.subs({yQ: ch["Q"], yu: ch["u"], yd: ch["d"], yL: ch["L"], ye: ch["e"]})) == 0
                        for q in eqs)
    s_ = sp.symbols("s")
    degenerate = {"Q": 0, "u": s_, "d": -s_, "L": 0, "e": 0}
    sols_at_sixth = sorted(str(r) for r in sp.solve(cubic.subs(yQ, sp.Rational(1, 6)), yu))
    colour = {"Q": 3, "u": -3, "d": -3, "L": 1, "e": 1, "nu": 1}
    su2 = {"Q": 2, "u": 1, "d": 1, "L": 2, "e": 1, "nu": 1}

    def needs(ch):
        rows = {}
        for b, (x, y) in BILINEARS.items():
            col = {1, 8} if {abs(colour[x]), abs(colour[y])} == {3} else {1}
            rows[b] = {"Y of the field": str(-(ch[x] + ch[y])), "SU(2)": 2 if 2 in (su2[x], su2[y]) else 1,
                       "colour allowed": sorted(col)}
        return rows

    sm_rows = needs(sm)
    absY = {abs(sp.Rational(v["Y of the field"])) for v in sm_rows.values()}
    colours = set.intersection(*[set(v["colour allowed"]) for v in sm_rows.values()])
    dg_abs = {sp.Abs(-(degenerate[x] + degenerate[y])) for b, (x, y) in BILINEARS.items() if b != "L nu^c"}
    a, b_ = sp.symbols("a b")
    BL = {"Q": sp.Rational(1, 3), "u": sp.Rational(-1, 3), "d": sp.Rational(-1, 3), "L": -1, "e": 1, "nu": 1}
    fam = {f: a * sm[f] + b_ * BL[f] for f in FIELDS}
    eqs_nu = [2 * fam["Q"] + fam["u"] + fam["d"], 3 * fam["Q"] + fam["L"],
              6 * fam["Q"] + 3 * fam["u"] + 3 * fam["d"] + 2 * fam["L"] + fam["e"] + fam["nu"],
              6 * fam["Q"] ** 3 + 3 * fam["u"] ** 3 + 3 * fam["d"] ** 3 + 2 * fam["L"] ** 3 + fam["e"] ** 3
              + fam["nu"] ** 3]
    fam_free = all(sp.expand(q) == 0 for q in eqs_nu)
    fam_bil = {bb: (sp.simplify(-(fam[x] + fam[y])), sp.simplify(-(BL[x] + BL[y]))) for bb, (x, y) in BILINEARS.items()}
    c = {"(a) after the linear conditions the cubic is a constant times y_Q (y_u - 2 y_Q)(y_u + 4 y_Q)": bool(
             ratio.is_number and ratio != 0),
         "(a) at y_Q = 1/6, y_u is -2/3 (the SM) or 1/3 (u/d relabelled), and both are solutions": sols_at_sixth == [
             "-2/3", "1/3"] and on(sm) and on(relab),
         "(a) at y_Q = 0: y_L = y_e = 0, y_u = -y_d, a family of solutions": on(degenerate),
         "(a) Witten's global anomaly: 3 + 1 = 4 doublets per generation, an even number": (3 + 1) % 2 == 0,
         "(b) every SM bilinear needs a doublet with |Y| = 1/2": absY == {sp.Rational(1, 2)} and all(
             v["SU(2)"] == 2 for v in sm_rows.values()),
         "(b) one field serves all: the colour singlet is forced by the leptons": colours == {1},
         "(c) the degenerate family needs |Y| = |s| and 0: two fields unless s = 0": dg_abs == {sp.Abs(s_), 0},
         "(d) a Y + b (B - L) is anomaly-free with nu^c": bool(fam_free),
         "(d) one doublet of charge a/2 and B - L 0 serves every bilinear": all(
             sp.Abs(y) == sp.Abs(a / 2) and bl == 0 for (y, bl) in fam_bil.values())}
    return {"checks": c, "the cubic after the linear conditions": str(cubic), "its ratio": str(ratio),
            "the SM bilinears": sm_rows,
            "a Y + b (B - L) bilinears (Y, B - L)": {k: [str(v[0]), str(v[1])] for k, v in fam_bil.items()}}, all(
        c.values())


# ------------------------------------------------------------------ C2. the flavour side
def zeta_sum(terms):
    """sum of c zeta8^j over (j, c); returns the coefficients on 1, zeta, zeta^2, zeta^3 (zeta^4 = -1)"""
    v = [0, 0, 0, 0]
    for j, c in terms:
        j %= 8
        v[j % 4] += c if j < 4 else -c
    return v


def invariants(G, parts):
    """the dimension of the invariants in a tensor product of T (+1), T-bar (-1) and the trivial field (0)"""
    terms = []
    for (k, Q) in G:
        t = int(np.trace(Q))
        j, c = 0, 1
        for p in parts:
            if p != 0:
                j += p * k
                c *= t
        terms.append((j, c))
    v = zeta_sum(terms)
    assert v[1] == v[2] == v[3] == 0 and v[0] % len(G) == 0, v
    return v[0] // len(G)


def C2(G, assign, su3, grav):
    tab, quark1, lepton1, all1, triplet_any = {}, [], [], [], False
    for s in assign:
        row = {}
        for sig_name, sig in (("1", 0), ("T", 1), ("T-bar", -1)):
            row[sig_name] = {b: invariants(G, (s[x], s[y], sig)) for b, (x, y) in BILINEARS.items()}
            if sig != 0:
                triplet_any |= any(v > 0 for v in row[sig_name].values())
        r1 = row["1"]
        if r1["Q u^c"] > 0 and r1["Q d^c"] > 0:
            quark1.append(s)
        if r1["L e^c"] > 0 and r1["L nu^c"] > 0:
            lepton1.append(s)
        if all(v > 0 for v in r1.values()):
            all1.append(s)
        tab["".join("+" if s[f] > 0 else "-" for f in FIELDS)] = row
    mult = invariants(G, (1, -1))
    c = {"(a) both quark bilinears with a singlet field iff the SU(3)-free set": quark1 == su3,
         "(a) both lepton bilinears iff s_e = s_nu = -s_L": lepton1 == [
             s for s in assign if s["e"] == s["nu"] == -s["L"]],
         "(a) all four iff the SU(3)- and gravity-free set, 4 of 64": all1 == grav and len(all1) == 4,
         "(a) the invariant's multiplicity in T (x) T-bar is 1": mult == 1,
         "(b) a T or T-bar field gives no invariant in any bilinear under any assignment": not triplet_any}
    return {"checks": c, "by assignment (Q u d L e nu; + = T)": tab}, all(c.values())


# ------------------------------------------------------------------ C4. index matching
def C4():
    C, K = EC.frame()
    (_, gL, gR) = EC.H.lift_choices()[0]
    R, _ = EC.reps(gL, gR, C, K)
    I = {(cd, r, n): UC.index(UC.twisted(R, r), cd, n) for cd in W127.CONDS for r in W127.ALLOWED for n in W127.BOX}
    t = {(cd, r): I[(cd, r, 0)] for cd in W127.CONDS for r in W127.ALLOWED}
    match = sorted(k for k, v in I.items() if abs(v - W127.FIBRE[k[0]]) < TOL)
    natural = [k for k in match if k[0] in ("0", "L6")]
    others = [k for k in match if k[0] in ("V2", "V4") and k[2] != 1]
    joint = {(cd, n): sum(I[(cd, r, n)] for r in W127.ALLOWED) for cd in W127.CONDS for n in W127.BOX}
    h = {k: W127.h_exact(k[1], k[2], W127.NS[-1]) for k in match}
    c = {"22 data match": len(match) == 22,
         "at 0 and L6, I = f iff n = 1 and t_r = 0": sorted(natural) == sorted(
             (cd, r, 1) for cd in ("0", "L6") for r in W127.ALLOWED if abs(t[(cd, r)]) < TOL),
         "the other solutions are (V2, 20, 0) and (V4, 4, 2)": sorted(others) == [("V2", 20, 0), ("V4", 4, 2)],
         "the joint index never equals 6 f": all(abs(v - 6 * W127.FIBRE[cd]) > TOL for (cd, n), v in joint.items())}
    return {"checks": c, "the matching set (cond, r, n)": [list(k) for k in match],
            "W127's exact h at each matching datum (canonical hand)": {str(k): v for k, v in h.items()},
            "the joint index, sum over the six twists": {f"{cd} n={n}": round(v, 9) for (cd, n), v in joint.items()}
            }, all(c.values())


def main():
    c0, ok0, G, assign, su3, grav = C0()
    c1, ok1 = C1()
    c2, ok2 = C2(G, assign, su3, grav)
    c4, ok4 = C4()
    cells = {"C0": ok0, "C1": ok1, "C2": ok2, "C4": ok4}
    out = {"arc": "W128", "rule": "W128_RULE.md", "status": "one run", "C0": c0, "C1": c1, "C2": c2,
           "C3": "a READING by hand, in W128's record", "C4": c4,
           "C5 (read-out)": {
               "the gauge side": "massive chiral matter needs a colour-singlet SU(2) doublet with |Y| = 1/2; one "
                                 "serves every mass (C1)",
               "the flavour side": "with the moves as a symmetry and constant couplings the field is a move singlet, "
                                   "consistent exactly at B1674's anomaly-free assignments; no triplet field couples "
                                   "(C2)",
               "index matching": "forces n = 1 with t_r = 0 at the natural conditions; never for the joint field (C4)"},
           "cells": {k: bool(v) for k, v in cells.items()}, "every cell holds": bool(all(cells.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every cell holds:", out["every cell holds"])


if __name__ == "__main__":
    main()
