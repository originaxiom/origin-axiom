#!/usr/bin/env python3
"""W127 — is the field forced to exist? GENESIS PF1 read at the weave's cusp in three forms (the rule: W127_RULE.md,
committed and pushed before this script).

  P0    the record reproduced: W46's table at r = 0, W47's K2 exponents and K3 table, W123's exact h(0, n) and its
        single-line sections
  P1    F1, frustration: the commutator trace at the two forced fibre points; every cusp exponent under every allowed
        twist (W47's K2), neither depending on n
  P2    h(r, n) = dim M_{3/2+12n}(T (x) eps_r) exactly. F = eta^r g with g = c0 R + c1 DR + c2 D2R, c_j in
        Delta^-N C[E4, E6] (W123's exact route at weight 3/2 - r/2), the twist read as per-line units
        m_e = n + [e + r/24 >= 1]; at N = 5 and N = 6; Riemann-Roch against W45's chi, with the dual counted by W45's
        q-expansion dims at n = 0
  P2'   the r = 4, n = 0 kernel against R itself (so the form is eta^4 R), to x^60; its line orders
  P2''  the mirror: hbar(r, n) = chi_{1/2+12n}(T-bar (x) eps_r) + h(24 - r, -n); W45's dims at n = 0
  P3    F2: the index I(cond, r, n) on the box, per datum and summed over the six twists; the least non-cancelling
        data at each natural condition (least |n|, then least |I|)
  P4    F3: the least line-bundle datum (n = 1) and the least per-line data (one unit on one line, r = 0)
  P5    the read-out

    python3 -B the_field_at_the_end.py      # writes the_field_at_the_end.json beside itself
"""
import contextlib
import io
import json
import sys
from fractions import Fraction as Fr
from pathlib import Path

import flint
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_unit_at_the_weaves_cusp as UC  # noqa: E402  (W47: twisted, index, chi_or_zero, K2; EC = W46, IW = W45)
    import the_higgs_route as HR  # noqa: E402  (W123: exact Laurent series in x = q^(1/8), R and DR)

EC, IW = UC.EC, UC.IW
HR.NT = 140
L, NT = HR.L, HR.NT
OUT = HERE / "the_field_at_the_end.json"
TOL = 1e-9
ALLOWED = (0, 4, 8, 12, 16, 20)
BOX = (-1, 0, 1, 2)
CONDS = ("0", "V2", "V4", "L6")
FIBRE = UC.FIBRE
EXPS = [Fr(1, 8), Fr(3, 8), Fr(7, 8)]
NS = (5, 6)


# ------------------------------------------------------------------ the exact route (W123's, extended)
def sigma(n, k):
    return sum(d ** k for d in range(1, n + 1) if n % d == 0)


def eis(k, c):
    co = [Fr(0)] * NT
    co[0] = Fr(1)
    for n in range(1, NT // 8 + 1):
        if 8 * n < NT:
            co[8 * n] = Fr(c * sigma(n, k - 1))
    return L(0, co)


E4, E6 = eis(4, 240), eis(6, -504)
DELTA = (E4 * E4 * E4 + (E6 * E6).neg()).scale(Fr(1, 1728))
assert DELTA.v == 8 and DELTA.c[0] == 1                          # q = x^8
_, R_LINES, _, DR_LINES = HR.the_R_series()
_e2 = HR.E2()
D2R_LINES = {e: s.qdq() + (_e2 * s).scale(Fr(-1, 8)) for e, s in DR_LINES.items()}   # the Serre derivative at 3/2
BASIS = (R_LINES, DR_LINES, D2R_LINES)                           # weights -1/2, 3/2, 7/2
_POW, _COLS = {}, {}


def power(name, n):
    base = {"E4": E4, "E6": E6, "D": DELTA}[name]
    if (name, 0) not in _POW:
        c = [Fr(0)] * NT
        c[0] = Fr(1)
        _POW[(name, 0)] = L(0, c)
    k = max(j for (nm, j) in _POW if nm == name and j <= n)
    while k < n:
        _POW[(name, k + 1)] = _POW[(name, k)] * base
        k += 1
    return _POW[(name, n)]


def mbasis(w):
    return [(a, b) for a in range(w // 4 + 1) for b in range(w // 6 + 1) if 4 * a + 6 * b == w] if w >= 0 else []


def columns(r, N):
    """the weakly holomorphic forms g of T at weight 3/2 - r/2 with c_j of pole order <= N, line by line"""
    if (r, N) not in _COLS:
        dinv = power("D", N).inv()
        w2 = 3 - r                                               # twice the weight of g
        cols = []
        for j, off in enumerate((1, -3, -7)):                    # c_j has weight w + 1/2, w - 3/2, w - 7/2
            for (a, b) in mbasis((w2 + off) // 2 + 12 * N):
                c = power("E4", a) * power("E6", b) * dinv
                cols.append({e: c * BASIS[j][e] for e in EXPS})
        _COLS[(r, N)] = cols
    return _COLS[(r, N)]


def per_line(r, n):
    return [n + (1 if e + Fr(r, 24) >= 1 else 0) for e in EXPS]


def coef(s, k):
    return s.c[k - s.v] if 0 <= k - s.v < NT else Fr(0)


def system(r, m, N):
    cols = columns(r, N)
    rows = []
    for e, me in zip(EXPS, m):
        bound = 8 * (e - me)                                     # keep x^k with k >= bound on the line e
        assert all(col[e].v + NT > bound + 8 for col in cols), "series too short"
        ks = sorted({col[e].v + i for col in cols for i, a in enumerate(col[e].c) if a and col[e].v + i < bound})
        rows += [[coef(col[e], k) for col in cols] for k in ks]
    return cols, rows


def h_exact(r, n, N, m=None):
    cols, rows = system(r, per_line(r, n) if m is None else m, N)
    if not rows:
        return len(cols)
    M = flint.fmpq_mat(len(rows), len(cols), [flint.fmpq(x.numerator, x.denominator) for row in rows for x in row])
    return len(cols) - M.rank()


def kernel_form(r, n, N):
    cols, rows = system(r, per_line(r, n), N)
    ker = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in rows]).nullspace()
    forms = []
    for v in ker:
        f = {}
        for e in EXPS:
            acc = None
            for c, col in zip(v, cols):
                if c != 0:
                    q = sp.Rational(c)
                    t = col[e].scale(Fr(int(q.p), int(q.q)))
                    acc = t if acc is None else acc + t
            f[e] = acc
        forms.append(f)
    return forms


def equals_up_to_scale(f, g, upto=60):
    ratio = None
    for e in EXPS:
        a, b = f[e], g[e]
        for k in range(min(a.v, b.v), upto):
            ca, cb = coef(a, k), coef(b, k)
            if cb != 0 and ratio is None:
                ratio = Fr(ca) / Fr(cb)
            if ratio is None and ca != 0:
                return False, None
            if ratio is not None and Fr(ca) != ratio * Fr(cb):
                return False, ratio
    return ratio is not None and ratio != 0, ratio


# ------------------------------------------------------------------ the cells
def P0(R, Itab, H):
    w46 = json.loads((HERE / "the_end_conditions_on_the_weaves_surface.json").read_text(encoding="utf-8"))
    h5 = w46["the record's lifts"]["H5: the four-dimensional index, by condition and cusp units n"]
    w47 = json.loads((HERE / "the_unit_at_the_weaves_cusp.json").read_text(encoding="utf-8"))
    k3 = w47["K3: the twisted index"]["the twisted index at n = 0, by r and puncture condition"]
    k2 = w47["K2: the cusp exponents"]["the exponents times 24, by allowed r and piece"]
    w123 = json.loads((HERE / "the_higgs_route_exact.json").read_text(encoding="utf-8"))["d at N = 4"]
    mine_k2 = UC.K2(R, list(ALLOWED))["the exponents times 24, by allowed r and piece"]
    singles = {str(tuple(m)): h_exact(0, None, NS[-1], m=list(m)) for m in ((1, 0, 0), (0, 1, 0), (0, 0, 1))}
    c = {
        "W46's table at r = 0, n in {-1, 0, 1}": all(abs(Itab[cd]["0"][str(n)] - h5[cd][str(n)]) < TOL
                                                    for cd in CONDS for n in (-1, 0, 1)),
        "W47's K3 at n = 0 for every allowed r": all(abs(Itab[cd][str(r)]["0"] - k3[str(r)][cd]) < TOL
                                                     for cd in CONDS for r in ALLOWED),
        "W47's K2 exponents": mine_k2 == k2,
        "W123's exact h(0, 0) = 0, h(0, 1) = 3, h(0, 2) = 6": (H[(0, 0)], H[(0, 1)], H[(0, 2)]) == (
            w123["(0, 0, 0)"], w123["(1, 1, 1)"], w123["(2, 2, 2)"]) == (0, 3, 6),
        "W123's single-line sections, one each": all(singles[k] == w123[k] == 1 for k in singles),
    }
    return {"checks": c, "single-line h at r = 0": singles}, all(c.values())


def P1(R):
    A, B = sp.Matrix([[1, 1], [1, 2]]), sp.Matrix([[1, -1], [-1, 2]])
    tr = (A.trace(), B.trace(), (A * B).trace())
    markov = sum(x * x for x in tr) == tr[0] * tr[1] * tr[2]
    k_hyp = sp.simplify((A * B * A.inv() * B.inv()).trace())
    qa, qb = sp.Matrix([[sp.I, 0], [0, -sp.I]]), sp.Matrix([[0, 1], [-1, 0]])
    k_q = sp.simplify((qa * qb * qa.inv() * qb.inv()).trace())
    k2 = UC.K2(R, list(ALLOWED))
    nums = [x for row in k2["the exponents times 24, by allowed r and piece"].values() for v in row.values() for x in v]
    c = {"the hyperbolic fibre point is the Markov triple (3, 3, 3)": bool(markov and tr == (3, 3, 3)),
         "kappa = tr[a, b] = -2 there": k_hyp == -2,
         "kappa = -2 at the quaternion point": k_q == -2,
         "every cusp exponent under every allowed twist is an odd multiple of 1/24 (never 0)":
             bool(k2["every numerator is odd"]) and 0 not in nums}
    return {"checks": c, "kappa": [str(k_hyp), str(k_q)],
            "n-independence": "by construction: O(n delta) changes the bundle, not the local system, so neither "
                              "kappa nor any cusp exponent depends on n"}, all(c.values())


def P2(R, H, Hn):
    agree = all(Hn[NS[0]][k] == Hn[NS[1]][k] for k in Hn[NS[1]])
    want = {(r, n): (0 if n < 0 else 3 * n + (1 if r == 4 else 0)) for r in ALLOWED for n in BOX}
    rr, extra, rows = True, True, {}
    for r in ALLOWED:
        Rr = UC.twisted(R, r)
        for n in BOX:
            chi = UC.chi_or_zero(Fr(3, 2) + 12 * n, Rr["T"])
            row = {"h exact": H[(r, n)], "chi_{3/2+12n}": round(chi, 9)}
            if n >= 1:
                rr &= abs(H[(r, n)] - chi) < TOL
            if n == 0:
                M = IW.dims(*Rr["T"], Fr(3, 2))
                dual = (np.conj(Rr["T"][0]), np.conj(Rr["T"][1]))
                S = IW.dims(*dual, Fr(1, 2), cusp=True)
                row.update({"dims M_{3/2} numerically (null, gap)": M, "dims S_{1/2} of the dual (null, gap)": S})
                rr &= H[(r, 0)] - S[0] == round(chi)
                extra &= M[0] == H[(r, 0)]
            rows[f"r={r} n={n}"] = row
    c = {"h(r, n) as predicted on the box": all(H[k] == v for k, v in want.items()),
         "N = 5 and N = 6 agree": agree,
         "Riemann-Roch (n >= 1 exactly; n = 0 with the dual counted numerically)": bool(rr)}
    return {"checks": c, "table": rows,
            "reported, not a cell condition: W45's numerical M_{3/2} equals the exact h at n = 0": bool(extra),
            "auxiliary h(r, -2)": {str(r): H[(r, -2)] for r in ALLOWED}}, all(c.values())


def P2p():
    forms = kernel_form(4, 0, NS[-1])
    one = len(forms) == 1
    eq, ratio = equals_up_to_scale(forms[0], R_LINES) if one else (False, None)
    orders = {str(e): str(Fr(R_LINES[e].v, 8) + Fr(4, 24)) for e in EXPS}
    c = {"the kernel at r = 4, n = 0 is one-dimensional": one,
         "it is C R exactly (to x^60), so the form is eta^4 R": bool(eq),
         "eta^4 R has line orders 1/24, 7/24, 13/24": sorted(Fr(v) for v in orders.values()) == [
             Fr(1, 24), Fr(7, 24), Fr(13, 24)]}
    return {"checks": c, "ratio to R": str(ratio), "line orders of eta^4 R, by g's line": orders}, all(c.values())


def P2pp(R, H):
    hb, rows = {}, {}
    for r in ALLOWED:
        Rr = UC.twisted(R, r)
        for n in BOX:
            chi = UC.chi_or_zero(Fr(1, 2) + 12 * n, Rr["T-bar"])
            hb[(r, n)] = round(chi) + H[((24 - r) % 24, -n)]
            rows[f"r={r} n={n}"] = {"chi_{1/2+12n}(T-bar)": round(chi, 9), "h(24 - r, -n)": H[((24 - r) % 24, -n)],
                                    "hbar": hb[(r, n)]}
            if n == 0:
                rows[f"r={r} n={n}"]["dims M_{1/2}(T-bar) numerically (null, gap)"] = IW.dims(*Rr["T-bar"], Fr(1, 2))
    want = {(r, n): (0 if n <= 0 else 3 * n - (1 if r == 20 else 0)) for r in ALLOWED for n in BOX}
    c = {"hbar(r, 0) = 0 at every r; hbar(r, 1) = 3 except hbar(20, 1) = 2; hbar(r, -1) = 0":
             all(hb[(r, n)] == want[(r, n)] for r in ALLOWED for n in (-1, 0, 1)),
         "the numerical dims at n = 0 agree": all(
             rows[f"r={r} n=0"]["dims M_{1/2}(T-bar) numerically (null, gap)"][0] == hb[(r, 0)] for r in ALLOWED)}
    return {"checks": c, "table": rows, "hbar(r, 2)": {str(r): hb[(r, 2)] for r in ALLOWED}}, all(c.values()), hb


def P3(Itab):
    t = {cd: {r: Itab[cd][str(r)]["0"] for r in ALLOWED} for cd in CONDS}
    formula = all(abs(Itab[cd][str(r)][str(n)] - (n * FIBRE[cd] + t[cd][r])) < TOL
                  for cd in CONDS for r in ALLOWED for n in BOX)
    untwisted_empty = all(abs(Itab[cd]["0"]["0"]) < TOL for cd in CONDS)
    least = {}
    for cd in CONDS:
        cand = [(abs(n), abs(round(Itab[cd][str(r)][str(n)])), r, n) for r in ALLOWED for n in BOX
                if abs(Itab[cd][str(r)][str(n)]) > TOL]
        key = min(c[:2] for c in cand)
        least[cd] = [{"r": r, "n": n, "I": round(Itab[cd][str(r)][str(n)])} for (a, b, r, n) in cand if (a, b) == key]
    totals = {cd: {str(n): round(sum(Itab[cd][str(r)][str(n)] for r in ALLOWED), 9) for n in BOX} for cd in CONDS}
    c = {"I = n f + t_r on the whole box": bool(formula),
         "the untwisted empty end cancels at every condition": bool(untwisted_empty),
         "the least non-cancelling datum at 0 is unique: r = 4, n = 0, I = -1": least["0"] == [
             {"r": 4, "n": 0, "I": -1}],
         "the least non-cancelling datum at L6 is unique: r = 20, n = 0, I = -1": least["L6"] == [
             {"r": 20, "n": 0, "I": -1}],
         "the weave totals are 6 n f - 1": all(abs(totals[cd][str(n)] - (6 * n * FIBRE[cd] - 1)) < TOL
                                               for cd in CONDS for n in BOX)}
    return {"checks": c, "t_r(cond)": {cd: {str(r): round(v, 9) for r, v in t[cd].items()} for cd in CONDS},
            "the least non-cancelling data (least |n|, then least |I|)": least,
            "the weave totals, sum over the six twists": totals}, all(c.values()), least, totals


def P4(R, Itab, H, hb, singles):
    chi0 = UC.chi_or_zero(Fr(3, 2), R["T"])
    per_line_I = {k: -(round(chi0) + 1) for k in singles}
    c = {"n = 1: h = 3, I = -3 at 0 and +3 at L6, hbar = 3": (H[(0, 1)], round(Itab["0"]["0"]["1"]),
                                                             round(Itab["L6"]["0"]["1"]), hb[(0, 1)]) == (3, -3, 3, 3),
         "one unit on one line: h = 1 and I = -1 on each line": all(
             singles[k] == 1 and per_line_I[k] == -1 for k in singles)}
    return {"checks": c, "per-line I = -(chi_{3/2} + 1)": per_line_I}, all(c.values())


def P5(H, hb, least, totals, Itab):
    rd = {
        "F1 (frustration)": {"forbids the empty end": False,
                             "why": "kappa = -2 and no cusp exponent is an integer at every datum, the empty one "
                                    "included; F1 cannot see n"},
        "F2 per datum": {"forbids the untwisted empty end": all(abs(Itab[cd]["0"]["0"]) < TOL for cd in CONDS),
                         "the least non-cancelling datum": {cd: least[cd] for cd in ("0", "L6")},
                         "its Higgs space, canonical hand h(4, 0)": H[(4, 0)],
                         "its Higgs space, mirror hand hbar(20, 0)": hb[(20, 0)],
                         "non-cancelling data with no Higgs (canonical hand, condition 0)": [
                             f"r={r} n={n}" for r in ALLOWED for n in BOX
                             if abs(Itab["0"][str(r)][str(n)]) > TOL and H[(r, n)] == 0]},
        "F2 at weave level": {"the joint index at n = 0": {cd: totals[cd]["0"] for cd in CONDS},
                              "forbids the empty end": any(abs(totals[cd]["0"]) < TOL for cd in CONDS),
                              "the joint Higgs space at n = 0, canonical and mirror": [
                                  sum(H[(r, 0)] for r in ALLOWED), sum(hb[(r, 0)] for r in ALLOWED)]},
        "F3 (non-empty end)": {"forbids the empty end": "by definition (GENESIS FK10's unit restated)",
                               "least line-bundle datum n = 1": {"h": H[(0, 1)], "I at 0": Itab["0"]["0"]["1"]},
                               "least per-line datum": {"h": 1, "I": -1, "cost": "a chosen line (W123)"}}}
    return rd


def main():
    C, K = EC.frame()
    (_, gL, gR) = EC.H.lift_choices()[0]
    R, _ = EC.reps(gL, gR, C, K)
    Itab = {cd: {str(r): {str(n): round(UC.index(UC.twisted(R, r), cd, n), 9) for n in BOX} for r in ALLOWED}
            for cd in CONDS}
    Hn = {N: {(r, n): h_exact(r, n, N) for r in ALLOWED for n in (-2,) + BOX} for N in NS}
    H = Hn[NS[-1]]
    p0, ok0 = P0(R, Itab, H)
    p1, ok1 = P1(R)
    p2, ok2 = P2(R, H, Hn)
    p2p, ok2p = P2p()
    p2pp, ok2pp, hb = P2pp(R, H)
    p3, ok3, least, totals = P3(Itab)
    p4, ok4 = P4(R, Itab, H, hb, p0["single-line h at r = 0"])
    p5 = P5(H, hb, least, totals, Itab)
    cells = {"P0": ok0, "P1": ok1, "P2": ok2, "P2'": ok2p, "P2''": ok2pp, "P3": ok3, "P4": ok4}
    out = {"arc": "W127", "rule": "W127_RULE.md", "status": "one run",
           "the index I(cond, r, n)": Itab,
           "h(r, n) exact, by N": {str(N): {f"r={r} n={n}": v for (r, n), v in Hn[N].items()} for N in NS},
           "P0": p0, "P1": p1, "P2": p2, "P2'": p2p, "P2''": p2pp, "P3": p3, "P4": p4, "P5 (read-out)": p5,
           "cells": {k: bool(v) for k, v in cells.items()}, "every cell holds": bool(all(cells.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every cell holds:", out["every cell holds"])


if __name__ == "__main__":
    main()
