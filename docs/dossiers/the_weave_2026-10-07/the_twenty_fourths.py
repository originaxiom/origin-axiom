#!/usr/bin/env python3
"""W132 — the edge's twenty-fourths and the SU(2) remainder (the rule: W132_RULE.md, committed and pushed before this
script).

  G0  the instrument: B1674's per-copy layer from n_G = sum_f w_G(f) (9 s_f + 3 r_f) mod 24 (W101's weights, as in
      W128's C0); eta's transformation at three points (mpmath, 40 digits); Delta = eta^24's multiplier, exactly
  G1  the unit O(n delta) = eta^(-24 n) on any set of fields: the change in every n_G
  G2  copies: n n_G mod 24 for n = 1..8 on all 64 sign assignments, no absorber, no twist
  G3  twists: the exact census over 64 sign assignments x 6^6 allowed twists at n = 1; its structure; W47's t_r
      (recomputed through W127's import) for the twists used
  G4  tau's counterterm: chi_eta^m on S and T, exactly (sympy roots of unity)
  G5  a Higgs-like pair: two weak doublets with Y = +-1/2 and characters chi_eta^(m_u), chi_eta^(m_d), as fermions
  G6  the read-out: what closes at n = 1, per assignment and absorber; the least n with no absorber

    python3 -B the_twenty_fourths.py      # writes the_twenty_fourths.json beside itself
"""
import contextlib
import io
import itertools
import json
import sys
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_consistency_route as W128  # noqa: E402  (W101's weights; W127 -> W47's index)

W127 = W128.W127
UC, EC = W127.UC, W127.EC
OUT = HERE / "the_twenty_fourths.json"
mp.mp.dps = 40
FIELDS, WEIGHTS = W128.FIELDS, W128.WEIGHTS
GROUPS = ("SU3", "SU2", "grav")
ALLOWED = (0, 4, 8, 12, 16, 20)
CONDS = ("0", "V2", "V4", "L6")
COPIES = range(1, 9)
ASSIGN = [dict(zip(FIELDS, v)) for v in itertools.product((1, -1), repeat=6)]


def name(s):
    return " ".join(f"{f}{'+' if s[f] > 0 else '-'}" for f in FIELDS)


def n_G(G, s, r=None):
    r = r or {f: 0 for f in FIELDS}
    return sum(WEIGHTS[G].get(f, 0) * (9 * s[f] + 3 * r[f]) for f in FIELDS) % 24


def free(s, r=None, n=1):
    return {G: (n * n_G(G, s, r)) % 24 == 0 for G in GROUPS}


B1674 = [s for s in ASSIGN if s["u"] == s["d"] == -s["Q"] and s["e"] == s["nu"] == -s["L"]]


# ------------------------------------------------------------------ G0
def eta(tau):
    q = mp.exp(2j * mp.pi * tau)
    p, n = mp.mpf(1), 1
    while abs(q ** n) > mp.mpf("1e-48"):
        p *= 1 - q ** n
        n += 1
    return mp.exp(1j * mp.pi * tau / 12) * p


def G0():
    su3 = [s for s in ASSIGN if n_G("SU3", s) == 0]
    su2 = sorted({n_G("SU2", s) for s in ASSIGN})
    grav = [s for s in su3 if n_G("grav", s) == 0]
    taus = (mp.mpc(0, 1), mp.mpc("0.3", "1.2"), mp.mpc("-0.4", "0.95"))
    dT = max(abs(eta(t + 1) - mp.exp(1j * mp.pi / 12) * eta(t)) / abs(eta(t)) for t in taus)
    dS = max(abs(eta(-1 / t) - mp.sqrt(-1j * t) * eta(t)) / abs(eta(t)) for t in taus)
    chiS, chiT = sp.exp(-sp.I * sp.pi / 4), sp.exp(2 * sp.pi * sp.I / 24)
    c = {"SU(3)-free = {s_u = s_d = -s_Q}, 16 of 64": su3 == [s for s in ASSIGN if s["u"] == s["d"] == -s["Q"]]
                                                       and len(su3) == 16,
         "SU(2) values {6, 12, 18}": su2 == [6, 12, 18],
         "gravity-free among the SU(3)-free iff s_e = s_nu = -s_L, 4 of 16": grav == B1674 and len(grav) == 4,
         "eta(tau + 1) = e^(i pi/12) eta(tau) at three points": dT < 1e-30,
         "eta(-1/tau) = sqrt(-i tau) eta(tau) at three points": dS < 1e-30,
         "Delta = eta^24 has trivial multiplier": sp.simplify(chiS ** 24) == 1 and sp.simplify(chiT ** 24) == 1}
    return {"checks": c, "max eta defects (T, S)": [float(dT), float(dS)],
            "B1674's four": [name(s) for s in B1674]}, all(c.values())


# ------------------------------------------------------------------ G1
def G1():
    unit = lambda n: -24 * n                                    # O(n delta) = eta^(-24 n): its eta-exponent
    worst = 0
    for s in ASSIGN:
        for sub in itertools.product((0, 1), repeat=6):
            for n in COPIES:
                for G in GROUPS:
                    base = n_G(G, s)
                    dressed = (base + sum(WEIGHTS[G].get(f, 0) * unit(n) * d for f, d in zip(FIELDS, sub))) % 24
                    worst = max(worst, (dressed - base) % 24)
    chiS, chiT = sp.exp(-sp.I * sp.pi / 4), sp.exp(2 * sp.pi * sp.I / 24)
    mult = all(sp.simplify(chiS ** unit(n)) == 1 and sp.simplify(chiT ** unit(n)) == 1 for n in COPIES)
    c = {"dressing any set of fields by O(n delta), n = 1..8, changes no n_G": worst == 0,
         "O(n delta)'s multiplier is trivial on S and T": bool(mult)}
    return {"checks": c}, all(c.values())


# ------------------------------------------------------------------ G2
def least_n(s, r=None, upto=24):
    for n in range(1, upto + 1):
        if all(free(s, r, n).values()):
            return n
    return None


def G2():
    tab = {}
    for s in ASSIGN:
        tab[name(s)] = {"n_SU2": n_G("SU2", s), "SU(2) closes at n": [n for n in COPIES if free(s, None, n)["SU2"]]}
    want = lambda s: [n for n in COPIES if n % (2 if s["Q"] == s["L"] else 4) == 0]
    c = {"n_SU2 = 12 iff s_Q = s_L": all((n_G("SU2", s) == 12) == (s["Q"] == s["L"]) for s in ASSIGN),
         "SU(2) closes iff n even (s_Q = s_L) or n = 0 mod 4 (s_Q = -s_L)": all(
             tab[name(s)]["SU(2) closes at n"] == want(s) for s in ASSIGN),
         "n = 1 never closes SU(2)": all(not free(s)["SU2"] for s in ASSIGN),
         "on B1674's free sets SU(3) and gravity close for every n": all(
             free(s, None, n)["SU3"] and free(s, None, n)["grav"] for s in B1674 for n in COPIES)}
    least = {name(s): least_n(s) for s in ASSIGN}
    return {"checks": c, "per assignment": tab, "the least n closing all three, no absorber": least}, all(
        c.values()), least


# ------------------------------------------------------------------ G3
def t_table():
    C, K = EC.frame()
    (_, gL, gR) = EC.H.lift_choices()[0]
    R, _ = EC.reps(gL, gR, C, K)
    return {cd: {r: round(UC.index(UC.twisted(R, r), cd, 0), 9) for r in ALLOWED} for cd in CONDS}


def G3():
    rs = np.array(list(itertools.product(ALLOWED, repeat=6)), dtype=np.int64)      # 46656 x 6
    w = {G: np.array([WEIGHTS[G].get(f, 0) for f in FIELDS], dtype=np.int64) for G in GROUPS}
    census, patterns, eps12 = {}, {}, {}
    for s in ASSIGN:
        sv = np.array([s[f] for f in FIELDS], dtype=np.int64)
        ph = 9 * sv[None, :] + 3 * rs
        ok = np.ones(len(rs), dtype=bool)
        for G in GROUPS:
            ok &= (ph @ w[G]) % 24 == 0
        if ok.any():
            census[name(s)] = int(ok.sum())
            t = (rs[ok] % 8 == 4).astype(int)
            patterns[name(s)] = sorted({tuple(int(v) for v in row) for row in t})
            only12 = np.all(np.isin(rs[ok], (0, 12)), axis=1)
            eps12[name(s)] = sorted({tuple(int(v) for v in row) for row in (rs[ok][only12] % 8 == 4).astype(int)})
    predicted = [s for s in ASSIGN if s["Q"] == s["L"] and s["u"] == s["d"] and s["e"] == s["nu"]]

    def rule_t(s):
        out = []
        for t in itertools.product((0, 1), repeat=6):
            tQ, tu, td, tL, te, tn = t
            if (tQ + tL) % 2 == 1 and (tu + td) % 2 == int(s["u"] == s["Q"]) and (te + tn) % 2 == int(
                    s["e"] == s["L"]):
                out.append(t)
        return out

    tt = t_table()
    one12 = {}
    for s in B1674:
        hits = []
        for f in ("Q", "L"):
            r = {g: 0 for g in FIELDS}
            r[f] = 12
            hits.append(all(free(s, r).values()))
        one12[name(s)] = hits
    adds = [3 * r % 24 for r in ALLOWED]
    c = {"3r mod 24 is 12 for r = 4 mod 8 and 0 for r = 0 mod 8": adds == [0, 12, 0, 12, 0, 12],
         "fully free for exactly 8 sign assignments": len(census) == 8,
         "they are s_Q = s_L, s_u = s_d, s_e = s_nu": sorted(census) == sorted(name(s) for s in predicted),
         "none with s_Q = -s_L": all(s["Q"] == s["L"] for s in ASSIGN if name(s) in census),
         "the twist patterns are the rule's parities": all(patterns[name(s)] == rule_t(s) for s in predicted),
         "every pattern is reached with eps_12 alone": all(eps12[name(s)] == patterns[name(s)] for s in predicted),
         "t_12 = 0 at every condition": all(tt[cd][12] == 0 for cd in CONDS),
         "t_20 = 0 exactly at 0 and V4": [cd for cd in CONDS if tt[cd][20] == 0] == ["0", "V4"],
         "t_4 = 0 exactly at V2 and L6": [cd for cd in CONDS if tt[cd][4] == 0] == ["V2", "L6"],
         "B1674's two with s_Q = s_L become fully free with eps_12 on exactly one of Q, L": all(
             one12[name(s)] == [s["Q"] == s["L"]] * 2 for s in B1674)}
    return {"checks": c, "fully free (number of twist vectors)": census,
            "twist patterns (t_f = [r_f = 4 mod 8], order Q u d L e nu)": {k: [list(p) for p in v]
                                                                             for k, v in patterns.items()},
            "t_r(cond), recomputed": {cd: {str(r): v for r, v in tt[cd].items()} for cd in CONDS},
            "B1674's four with eps_12 on Q, on L": one12}, all(c.values()), census


# ------------------------------------------------------------------ G4
def G4():
    chi = lambda m: (sp.exp(-sp.I * sp.pi * m / 4), sp.exp(2 * sp.pi * sp.I * m / 24))
    trivial = [m for m in range(24) if all(sp.simplify(v - 1) == 0 for v in chi(m))]
    cancels = all(all(sp.simplify(a * b - 1) == 0 for a, b in zip(chi(n * n_G(G, s)), chi(-n * n_G(G, s))))
                  for s in ASSIGN for n in (1, 2, 3) for G in GROUPS)
    c = {"chi_eta^m is trivial on S and T only for m = 0 mod 24": trivial == [0],
         "eta^(-n_G) cancels n_G for every assignment, n and group": bool(cancels)}
    return {"checks": c}, all(c.values())


# ------------------------------------------------------------------ G5
def G5():
    wSU2, wgrav = WEIGHTS["SU2"]["L"], WEIGHTS["grav"]["L"]      # a weak doublet, colourless: as L
    yv = (sp.Rational(1, 2), sp.Rational(-1, 2))
    vectorlike = sum(yv) == 0 and sum(y ** 3 for y in yv) == 0
    rows = {}
    for s in B1674:
        ok = sorted({(mu + md) % 24 for mu in range(24) for md in range(24)
                     if (n_G("SU2", s) + wSU2 * (mu + md)) % 24 == 0
                     and (n_G("grav", s) + wgrav * (mu + md)) % 24 == 0})
        rows[name(s)] = ok
    c = {"the pair adds m_u + m_d to n_SU2 and 2 (m_u + m_d) to n_grav": (wSU2, wgrav) == (1, 2),
         "it is vector-like in Y": bool(vectorlike),
         "closes SU(2) and keeps gravity iff s_Q = s_L, with m_u + m_d = 12": all(
             rows[name(s)] == ([12] if s["Q"] == s["L"] else []) for s in B1674)}
    pair_all = {name(s): bool(free(s)["SU3"] and (n_G("grav", s) - 2 * n_G("SU2", s)) % 24 == 0) for s in ASSIGN}
    return {"checks": c, "m_u + m_d that close SU(2) and gravity, on B1674's four": rows}, all(c.values()), pair_all


def main():
    g0, ok0 = G0()
    g1, ok1 = G1()
    g2, ok2, least = G2()
    g3, ok3, census = G3()
    g4, ok4 = G4()
    g5, ok5, pair_all = G5()
    table = {}
    for s in ASSIGN:
        f = free(s)
        table[name(s)] = {"SU3, SU2, grav free at n = 1": [f[G] for G in GROUPS],
                          "fully free with a twist": name(s) in census,
                          "closed by tau's counterterm": True,
                          "fully closed by a Higgs-like pair": pair_all[name(s)],
                          "least n with no absorber": least[name(s)]}
    cells = {"G0": ok0, "G1": ok1, "G2": ok2, "G3": ok3, "G4": ok4, "G5": ok5}
    out = {"arc": "W132", "rule": "W132_RULE.md", "status": "one run", "G0": g0, "G1": g1, "G2": g2, "G3": g3,
           "G4": g4, "G5": g5, "G6 (read-out): per assignment at n = 1": table,
           "cells": {k: bool(v) for k, v in cells.items()}, "every cell holds": bool(all(cells.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every cell holds:", out["every cell holds"])


if __name__ == "__main__":
    main()
