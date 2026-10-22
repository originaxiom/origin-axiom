#!/usr/bin/env python3
"""W134 — the bridge: the weave's flavour triplet as the family SU(3) of E8 > E6 x SU(3) (the rule: W134_RULE.md,
committed and pushed before this script).

  E0  the instrument: E8's 240 roots exactly (doubled coordinates); A2 spanned by e1 - e2 and e2 - e3; the roots
      orthogonal to it (E6) and the other roots' A2 weights; the generalized index against W47's K5 at m = 24n
  E1  the obstruction (exact, sympy): det(rho (x) eps_r) on S and T against chi_eta^(9+3r); the det-1 twists chi_eta^k
      of rho; their rho'(S)^2 and the weights it allows
  E2  the admissible data: the m (twenty-fourths of the cusp unit) with det(T (x) eps_r (x) chi_eta^m) = 1, |m| <= 24
  E3  the count, two routes: chi at the dressed weights (W45's formula through W47's chi_or_zero), and the closed form
      t_r - sum_T floor((24 lambda + m)/24) + sum_p sum floor((24 lambda + m)/24)
  E4  the read-out

    python3 -B the_bridge_e6_su3.py      # writes the_bridge_e6_su3.json beside itself
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
    import the_unit_at_the_weaves_cusp as UC  # noqa: E402  (W47: twisted, chi_or_zero, index; EC = W46, IW = W45)

EC, IW = UC.EC, UC.IW
OUT = HERE / "the_bridge_e6_su3.json"
ALLOWED = (0, 4, 8, 12, 16, 20)
CONDS = ("0", "V2", "V4", "L6")
MS = range(-24, 25)
PREDICTED_THREES = sorted([(4, 17, "0"), (4, -23, "L6"), (12, 17, "0"), (12, -23, "0"), (12, -23, "L6"),
                           (20, -23, "L6"), (0, 21, "0"), (0, 21, "L6"), (8, 21, "0"), (8, 21, "L6"), (8, -19, "0"),
                           (16, 21, "L6")])


def the_reps():
    C, K = EC.frame()
    (_, gL, gR) = EC.H.lift_choices()[0]
    R, _ = EC.reps(gL, gR, C, K)
    return R


# ------------------------------------------------------------------ E0
def e8_roots():
    """doubled coordinates: 2x for each root x"""
    roots = []
    for i, j in itertools.combinations(range(8), 2):
        for si, sj in itertools.product((2, -2), repeat=2):
            v = [0] * 8
            v[i], v[j] = si, sj
            roots.append(tuple(v))
    for signs in itertools.product((1, -1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.append(tuple(signs))
    return roots


def ip(x, y):
    return Fr(sum(a * b for a, b in zip(x, y)), 4)


def E0(R):
    roots = e8_roots()
    alpha, beta = (2, -2, 0, 0, 0, 0, 0, 0), (0, 2, -2, 0, 0, 0, 0, 0)
    labels = {r: (ip(r, alpha), ip(r, beta)) for r in roots}
    e6 = [r for r in roots if labels[r] == (0, 0)]
    a2 = [r for r in roots if all(r[k] == 0 for k in range(3, 8))]
    rest = [r for r in roots if r not in set(e6) | set(a2)]
    e6set = set(e6)
    closed = all(tuple(a + b for a, b in zip(x, y)) in e6set for x in e6 for y in e6 if ip(x, y) == -1)
    w3 = [(1, 0), (-1, 1), (0, -1)]
    w3b = [(0, 1), (1, -1), (-1, 0)]
    counts = {str(w): sum(1 for r in rest if labels[r] == w) for w in w3 + w3b}
    idx_ok = True
    for r in ALLOWED:
        for cd in CONDS:
            for n in (-1, 0, 1):
                idx_ok &= abs(index_m(R, r, cd, 24 * n) - UC.index(UC.twisted(R, r), cd, n)) < 1e-9
    c = {"240 roots, all of norm 2": len(roots) == 240 and all(ip(r, r) == 2 for r in roots),
         "72 roots orthogonal to A2 (E6), closed under the root sums": len(e6) == 72 and bool(closed),
         "A2's own 6 roots": len(a2) == 6,
         "the other 162 sit on the six weights of 3 + 3-bar, 27 each": len(rest) == 162 and set(counts.values()) == {
             27},
         "248 = 78 + 8 + 81 + 81": 72 + 6 + 8 + 162 == 248,
         "the generalized index is W47's at m = 24n": bool(idx_ok)}
    return {"checks": c, "weights and multiplicities": counts}, all(c.values())


# ------------------------------------------------------------------ E1
def rho_exact():
    z = sp.exp(sp.I * sp.pi / 4)
    Pm = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    Li = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
    return z * Pm, z * Li


def chi(k):
    return sp.exp(-sp.I * sp.pi * k / 4), sp.exp(2 * sp.pi * sp.I * k / 24)


def eq(u, v):
    return sp.simplify(sp.expand_complex(u - v)) == 0


def E1(R):
    rS, rT = rho_exact()
    num = lambda M: np.array([[complex(x) for x in row] for row in M.evalf().tolist()])
    ident = max(float(np.abs(num(rS) - np.array(R["T"][0])).max()),
                float(np.abs(num(rT) - np.array(R["T"][1])).max()))
    dets = {}
    ok_det, never = True, True
    for r in ALLOWED:
        cs, ct = chi(r)
        dS, dT = (cs ** 3) * rS.det(), (ct ** 3) * rT.det()
        ws, wt = chi(9 + 3 * r)
        ok_det &= eq(dS, ws) and eq(dT, wt)
        never &= not (eq(dS, 1) and eq(dT, 1))
        dets[str(r)] = [str(sp.nsimplify(sp.expand_complex(dS))), str(sp.nsimplify(sp.expand_complex(dT)))]
    det1 = [k for k in range(24) if eq((chi(k)[0] ** 3) * rS.det(), 1) and eq((chi(k)[1] ** 3) * rT.det(), 1)]
    squares = {}
    for k in det1:
        S2 = sp.simplify((chi(k)[0] * rS) ** 2)
        allowed = [str(w) for w in (Fr(0), Fr(1, 2), Fr(1), Fr(3, 2), Fr(2), Fr(5, 2), Fr(3))
                   if IW.allowed(w, num(chi(k)[0] * rS))]
        squares[str(k)] = {"rho'(S)^2 is 1": S2 == sp.eye(3), "allowed weights among 0..3": allowed}
    c = {"rho(S), rho(T) are the record's T": ident < 1e-12,
         "det(rho (x) eps_r) = chi_eta^(9+3r) on S and T": bool(ok_det),
         "never trivial for an allowed r": bool(never),
         "the det-1 twists are k = 5 mod 8": det1 == [5, 13, 21],
         "each has rho'(S)^2 = 1": all(v["rho'(S)^2 is 1"] for v in squares.values()),
         "so only even integral weights, never 3/2": all(v["allowed weights among 0..3"] == ["0", "2"]
                                                         for v in squares.values())}
    return {"checks": c, "det(rho (x) eps_r) on (S, T)": dets, "the det-1 twists": squares}, all(c.values())


# ------------------------------------------------------------------ E2
def admissible(r, m):
    return (9 + 3 * r + 3 * m) % 24 == 0


def E2(R):
    tab = {str(r): [m for m in MS if admissible(r, m)] for r in ALLOWED}
    rS, rT = rho_exact()
    det_one = lambda k: eq((chi(k)[0] ** 3) * rS.det(), 1) and eq((chi(k)[1] ** 3) * rT.det(), 1)
    exact_ok = all(admissible(r, m) == det_one(r + m) for r in ALLOWED for m in MS)
    weight_ok = all(IW.allowed(Fr(3, 2) + Fr(m, 2), UC.twisted(R, r + m)["T"][0]) for r in ALLOWED for m in MS)
    least = {str(r): min(tab[str(r)], key=lambda m: (abs(m), m)) for r in ALLOWED}
    c = {"admissible iff m = 5 - r mod 8": all(tab[str(r)] == [m for m in MS if (m - 5 + r) % 8 == 0]
                                                for r in ALLOWED),
         "the determinant check, exactly, for every r and m": bool(exact_ok),
         "every dressed T is allowed at its weight 3/2 + m/2": bool(weight_ok),
         "neither m = 0 nor m = +-24 is admissible": all(not admissible(r, m) for r in ALLOWED for m in (0, 24, -24)),
         "the least data: m = 1 (r = 4 mod 8), m = -3 (r = 0 mod 8)": all(
             least[str(r)] == (1 if r % 8 == 4 else -3) for r in ALLOWED)}
    return {"checks": c, "admissible m by r": tab, "the least admissible m": least}, all(c.values()), tab, least


# ------------------------------------------------------------------ E3
def index_m(R, r, cond, m):
    Rr = UC.twisted(R, r + m)
    v = -UC.chi_or_zero(Fr(3, 2) + Fr(m, 2), Rr["T"])
    for p in EC.CONDITIONS[cond]:
        v += UC.chi_or_zero(Fr(1) + Fr(m, 2), Rr[p])
    return v


def nums(R, r, piece):
    return [int(round(24 * x)) % 24 for x in EC.exps(UC.twisted(R, r)[piece][1])]


def closed_form(R, r, cond, m, t):
    fl = lambda piece: sum((a + m) // 24 for a in nums(R, r, piece))
    return t - fl("T") + sum(fl(p) for p in EC.CONDITIONS[cond])


def E3(R, tab, least):
    full, agree = {}, True
    for r in ALLOWED:
        full[str(r)] = {}
        for cd in CONDS:
            t = index_m(R, r, cd, 0)
            row = {}
            for m in MS:
                a = index_m(R, r, cd, m)
                b = closed_form(R, r, cd, m, round(t))
                agree &= abs(a - b) < 1e-9
                row[str(m)] = round(a, 9)
            full[str(r)][cd] = row
    adm = [(r, m, cd) for r in ALLOWED for m in tab[str(r)] if abs(m) < 24 for cd in CONDS]
    I = lambda r, m, cd: full[str(r)][cd][str(m)]
    at_least = max(abs(I(r, least[str(r)], cd)) for r in ALLOWED for cd in CONDS)
    upto16 = max(abs(I(r, m, cd)) for (r, m, cd) in adm if abs(m) <= 16)
    threes = sorted((r, m, cd) for (r, m, cd) in adm if abs(abs(I(r, m, cd)) - 3) < 1e-9)
    c = {"the two routes agree on every r, condition and m": bool(agree),
         "|I| <= 1 at the least admissible datum": at_least <= 1 + 1e-9,
         "|I| <= 2 for admissible |m| <= 16": upto16 <= 2 + 1e-9,
         "|I| = 3 at exactly the rule's twelve data": threes == PREDICTED_THREES}
    adm_tab = {str(r): {str(m): {cd: I(r, m, cd) for cd in CONDS} for m in tab[str(r)] if abs(m) < 24}
               for r in ALLOWED}
    return {"checks": c, "max |I| at the least datum": at_least, "max |I| for admissible |m| <= 16": upto16,
            "|I| = 3 among the admissible data": [list(x) for x in threes],
            "the index at the admissible data (r, m, condition)": adm_tab,
            "the full table I(r, condition, m)": full}, all(c.values()), threes


def main():
    R = the_reps()
    e0, ok0 = E0(R)
    e1, ok1 = E1(R)
    e2, ok2, tab, least = E2(R)
    e3, ok3, threes = E3(R, tab, least)
    rd = {"the chiral 27s": "the index at the admissible data, E3",
          "the least admissible data giving three": [list(x) for x in threes
                                                     if abs(x[1]) == min(abs(y[1]) for y in threes)] if threes else [],
          "a READING by hand (in the record, not here)": "the Yukawas"}
    cells = {"E0": ok0, "E1": ok1, "E2": ok2, "E3": ok3}
    out = {"arc": "W134", "rule": "W134_RULE.md", "status": "one run", "E0": e0, "E1": e1, "E2": e2, "E3": e3,
           "E4 (read-out)": rd, "cells": {k: bool(v) for k, v in cells.items()},
           "every cell holds": bool(all(cells.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every cell holds:", out["every cell holds"])


if __name__ == "__main__":
    main()
