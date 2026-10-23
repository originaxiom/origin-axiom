#!/usr/bin/env python3
"""W143 — P-345 on this seat's W133: which zero-free Higgs lines GENESIS PF1-W admits that are led at the cusp by the
non-null eigenline, both sign families on own code, and W133's open multiplicities (the rule: W143_RULE.md, committed
and pushed before this script).

  C0  the instrument: at eps = -1 the lines below equal W133's post hoc theta_power_lines coefficient by coefficient
      up to x^(v + NT - 8) (the series' exact range: where th3^a - th4^a cancels at x^0 the two routes truncate at
      different orders beyond it), at every a scanned; the eps = -1 members and their multiplicities against W133's
      committed post hoc JSON
  H1  membership, exact, both signs: F_a = eta^(3 - a) (eps th2^a, eps th4^a, i th3^a), a = 2 (mod 4),
      eps = i^((a + 2)/2), twist r = 2a (mod 24), -30 <= a <= 42; on the lines l_1 = eps th2^a,
      l_3 = eps th4^a + th3^a, l_7 = eps th4^a - th3^a, times eta^(3 - a - r); W133's coords over h(r, n), and the
      agreement to x^60; whether t F_a with 2^(a+2) t^3 = 1 solves W133's system (normal forms on its Groebner basis);
      the members' count against the number of lines (distinct values of a linear form, over 3)
  H2  the multiplicity each member carries (the characteristic polynomial's squarefree factors, W133's posthoc3), on
      two linear forms
  H3  the leading behaviour at the cusp: each member's three components' valuations in x = q^(1/8) and the part at the
      least valuation; proportional to e_1 = (1, 0, 0) (square 1) or to (0, eps, i) (square eps^2 - 1 = 0)
  H4  read-outs: W127's index I(cond, r, n) at each space (W127's committed JSON); B1740's F_-2 = eta^5 (th2^-2,
      th4^-2, i th3^-2) as the member a = -2, eps = +1
  R1  a read-out added with the script (not in the rule; no prediction): the opposite sign -eps at every a scanned

    python3 -B the_zero_free_higgs_signs.py      # writes the_zero_free_higgs_signs.json beside itself
"""
import collections
import contextlib
import io
import json
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import flint
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_zero_free_higgs_posthoc as PH  # noqa: E402  (W133's first post hoc: coords, power, theta_power_lines)
    import the_zero_free_higgs_posthoc3 as PH3  # noqa: E402  (W133's third post hoc: mult_matrix, FORMS)

W133, HR = PH.W133, PH.HR
E1, E3, E7, EXPS = W133.E1, W133.E3, W133.E7, W133.EXPS
OUT = HERE / "the_zero_free_higgs_signs.json"
CASES = ((4, 0), (4, 1), (12, 1), (20, 1))
A_RANGE = range(-30, 43)
EXPECTED = {(4, 0): {2}, (4, 1): {2, 26, -10, 14}, (12, 1): {-6, 18, 6}, (20, 1): {10, -2, 22}}
THREE_GEN = ((12, 1), (20, 1))
NONNULL_EXPECTED = {(4, 0): set(), (4, 1): {-10}, (12, 1): {-6}, (20, 1): {-2}}
LINES_RECORDED = {(4, 0): 1, (4, 1): 4, (12, 1): 3, (20, 1): 3}                 # W133's posthoc3 record
MARGIN = 8
Q3KEY = "Q3 theta-power vectors F_a (a = 2 mod 8, 2a = r mod 24, -30 <= a <= 42)"          # W133's post hoc record


def eps_of(a):
    """i^((a + 2)/2) for a = 2 (mod 4): +1 when (a + 2)/2 = 0 (mod 4), -1 when it is 2 (mod 4)"""
    k = (a + 2) // 2
    assert a % 4 == 2 and k % 2 == 0
    return 1 if k % 4 == 0 else -1


_TP = {}


def theta_powers(a):
    if a not in _TP:
        t2, t3, t4 = HR.theta2(), HR.theta34(1), HR.theta34(-1)
        _TP[a] = (PH.power(t2, a), PH.power(t3, a), PH.power(t4, a))
    return _TP[a]


def parts(a, r):
    """the components' rational parts th2^a, th4^a, th3^a, each times eta^(3 - a - r) (g = F_a / eta^r); the
    constants eps, eps, i multiply them"""
    A, C, D = theta_powers(a)
    e = W133.eta_pow(3 - a - r)
    return A * e, D * e, C * e


def lines(a, r, eps):
    P1, P4, P3 = parts(a, r)
    s = Fr(eps)
    return {E1: P1.scale(s), E3: P4.scale(s) + P3, E7: P4.scale(s) + P3.neg()}


def agree(s, u):
    """coefficient by coefficient from the lower valuation up to x^(v + NT - MARGIN)"""
    lo = min(s.v, u.v)
    return W133.same(s, u, upto=lo + HR.NT - MARGIN)


def rat(x):
    return sp.Rational(x.numerator, x.denominator)


def leading(a, r, eps):
    ps = parts(a, r)
    consts = (sp.Integer(eps), sp.Integer(eps), sp.I)
    ev = W133.eta_pow(3 - a - r).v
    vals = [p.v for p in ps]
    vmin = min(vals)
    lead = [sp.expand(consts[k] * rat(W133.co(ps[k], vmin))) for k in range(3)]
    sq = sp.expand(sum(z ** 2 for z in lead))
    is_e1 = lead[0] != 0 and lead[1] == 0 and lead[2] == 0
    is_null_line = lead[0] == 0 and lead[1] != 0 and sp.expand(sp.I * lead[1] - eps * lead[2]) == 0
    return {"valuations of the theta parts (th2^a, th4^a, th3^a)": [v - ev for v in vals],
            "valuations of g's components": vals, "least valuation": vmin,
            "leading part": [str(z) for z in lead], "its square": str(sq),
            "proportional to e_1 (non-null)": bool(is_e1),
            "proportional to (0, eps, i) (null)": bool(is_null_line)}


def multiplicity(p, c, a, form):
    _, facs = p.factor_squarefree()
    lv = sum(sp.Rational(k) * x for k, x in zip(form, c))
    v = lv ** 3 / sp.Integer(2) ** (a + 2)
    cubic = flint.fmpq_poly([flint.fmpq(-int(v.p), int(v.q)), 0, 0, 1])
    return [k for f, k in facs if f.gcd(cubic).degree() == 3], str(v)


def line_count(p):
    g = p.gcd(p.derivative())
    _, facs = p.factor_squarefree()
    by = collections.Counter()
    for f, k in facs:
        by[k] += f.degree()
    return p.degree(), p.degree() - g.degree(), {str(k): d // 3 for k, d in sorted(by.items())}


def main():
    t0 = time.time()
    t = sp.symbols("t")
    rec1 = json.loads((HERE / "the_zero_free_higgs_posthoc.json").read_text(encoding="utf-8"))
    rec3 = json.loads((HERE / "the_zero_free_higgs_posthoc3.json").read_text(encoding="utf-8"))
    index = json.loads((HERE / "the_field_at_the_end.json").read_text(encoding="utf-8"))["the index I(cond, r, n)"]
    out, members, mults, leads, c0 = {}, {}, {}, {}, {}
    for (r, n) in CASES:
        forms, avars, eqs, _, _ = W133.cubic_system(r, n)
        G = sp.groebner(eqs, *avars, order="grevlex", domain=sp.QQ)
        fms = [PH3.FORMS[k][:len(avars)] for k in range(2)]
        cps = [PH3.mult_matrix(G, avars, f).charpoly() for f in fms]
        scan, opposite, mem = {}, {}, {}
        c0_lines = []
        for a in A_RANGE:
            if a % 4 != 2 or (2 * a - r) % 24:
                continue
            eps = eps_of(a)
            if eps == -1:
                ref = PH.theta_power_lines(a, r)
                c0_lines.append(all(agree(lines(a, r, -1)[e], ref[e]) for e in EXPS))
            ls = lines(a, r, eps)
            c = PH.coords(forms, ls)
            ls_op = lines(a, r, -eps)
            opposite[str(a)] = PH.coords(forms, ls_op) is not None
            if c is None:
                scan[str(a)] = {"eps": eps, "in h": False}
                continue
            comb = {e: None for e in EXPS}
            for e in EXPS:
                s = None
                for ci, f in zip(c, forms):
                    term = f[e].scale(Fr(int(ci.p), int(ci.q)))
                    s = term if s is None else s + term
                comb[e] = s
            agree60 = all(W133.same(comb[e], ls[e], upto=60) for e in EXPS)
            two = sp.Integer(2) ** (a + 2)
            solves = all(sp.rem(sp.expand(g.subs(dict(zip(avars, [t * x for x in c])))), two * t ** 3 - 1, t) == 0
                         for g in G.exprs)
            ms = [multiplicity(cps[k], c, a, fms[k]) for k in range(2)]
            lead = leading(a, r, eps)
            mem[a] = {"eps": eps, "coords": [str(x) for x in c], "agrees to x^60": bool(agree60),
                      "t F_a with 2^(a+2) t^3 = 1 solves the system": bool(solves),
                      "multiplicity (form 1, form 2)": [m for m, _ in ms],
                      "the form's cube on the line (form 1)": ms[0][1], "leading behaviour": lead}
            scan[str(a)] = {"eps": eps, "in h": True}
        counts = [line_count(cps[k]) for k in range(2)]
        nlines = counts[0][1] // 3
        cubes = {mem[a]["the form's cube on the line (form 1)"] for a in mem}
        members[(r, n)] = set(mem)
        mults[(r, n)] = {}
        for a in mem:
            m1, m2 = mem[a]["multiplicity (form 1, form 2)"]
            mults[(r, n)][a] = m1[0] if m1 == m2 and len(m1) == 1 else None
        leads[(r, n)] = {a: mem[a]["leading behaviour"] for a in mem}
        rec_q3 = rec1.get(f"r={r} n={n}", {}).get(Q3KEY)
        rec_m = rec3[f"r={r} n={n}"]["the multiplicity of each theta-power line"]
        minus = {a for a in mem if mem[a]["eps"] == -1}
        c0[f"r={r} n={n}"] = {
            "eps = -1 lines equal W133's theta_power_lines to x^(v + NT - 8) at every a scanned": bool(all(c0_lines)),
            "a scanned with eps = -1": len(c0_lines),
            "eps = -1 members equal W133's Q3 record": (
                None if rec_q3 is None else minus == {int(k) for k, v in rec_q3.items() if v != "not in h"}),
            "eps = -1 multiplicities equal W133's posthoc3 record": all(
                [mults[(r, n)][a]] == rec_m.get(str(a)) for a in minus) and set(rec_m) == {str(a) for a in minus}}
        out[f"r={r} n={n}"] = {
            "scan (a: eps, in h)": scan, "members": {str(a): mem[a] for a in sorted(mem)},
            "the characteristic polynomial (form 1, form 2): degree, distinct values, lines by multiplicity": counts,
            "number of lines": nlines, "members on distinct lines": len(cubes) == len(mem),
            "R1 the opposite sign -eps lies in h (read-out, not in the rule)": opposite,
            "H4 W127's index I(cond, r, n)": {cd: index[cd][str(r)][str(n)] for cd in index}}
    # ---------------------------------------------------------------- the cells
    h1 = {}
    for (r, n) in CASES:
        o = out[f"r={r} n={n}"]
        mem = o["members"]
        h1[f"r={r} n={n}"] = {
            "members": sorted(members[(r, n)]), "expected": sorted(EXPECTED[(r, n)]),
            "members as expected": members[(r, n)] == EXPECTED[(r, n)],
            "every member solves": all(m["t F_a with 2^(a+2) t^3 = 1 solves the system"] for m in mem.values()),
            "every member agrees to x^60": all(m["agrees to x^60"] for m in mem.values()),
            "members = lines": len(mem) == o["number of lines"] and o["members on distinct lines"],
            "lines as W133 recorded (1, 4, 3, 3)": o["number of lines"] == LINES_RECORDED[(r, n)],
            "the two forms count the same lines": o["the characteristic polynomial (form 1, form 2): degree, distinct "
                                                    "values, lines by multiplicity"][0][1:] ==
            o["the characteristic polynomial (form 1, form 2): degree, distinct values, lines by multiplicity"][1][1:]}
    H1 = all(v["members as expected"] and v["every member solves"] and v["every member agrees to x^60"]
             and v["members = lines"] and v["lines as W133 recorded (1, 4, 3, 3)"]
             and v["the two forms count the same lines"] for v in h1.values())
    m41, m121, m201 = mults[(4, 1)], mults[(12, 1)], mults[(20, 1)]
    h2 = {"F_6 in h(12, 1)": m121.get(6), "F_-10, F_14 in h(4, 1)": [m41.get(-10), m41.get(14)],
          "F_-2, F_22 in h(20, 1)": [m201.get(-2), m201.get(22)],
          "every multiplicity has its line (members' multiplicities = the polynomial's lines by multiplicity)": {}}
    for (r, n) in CASES:
        o = out[f"r={r} n={n}"]
        want = o["the characteristic polynomial (form 1, form 2): degree, distinct values, lines by multiplicity"][0][2]
        have = collections.Counter(str(m) for m in mults[(r, n)].values())
        h2["every multiplicity has its line (members' multiplicities = the polynomial's lines by multiplicity)"][
            f"r={r} n={n}"] = dict(have) == want
    H2 = (m121.get(6) == 4 and sorted([m41.get(-10) or 0, m41.get(14) or 0]) == [6, 8]
          and sorted([m201.get(-2) or 0, m201.get(22) or 0]) == [1, 4]
          and all(h2["every multiplicity has its line (members' multiplicities = the polynomial's lines by "
                     "multiplicity)"].values()))
    h3, ok3 = {}, True
    for (r, n) in CASES:
        row = {}
        for a, ld in leads[(r, n)].items():
            want_theta = [a, 0, 0]
            good = (ld["valuations of the theta parts (th2^a, th4^a, th3^a)"] == want_theta
                    and ((a < 0 and ld["proportional to e_1 (non-null)"] and sp.sympify(ld["its square"]) != 0)
                         or (a > 0 and ld["proportional to (0, eps, i) (null)"] and sp.sympify(ld["its square"]) == 0)))
            ok3 = ok3 and bool(good)
            row[str(a)] = {"non-null-led": ld["proportional to e_1 (non-null)"], "as predicted": bool(good)}
        nonnull = {a for a, ld in leads[(r, n)].items() if ld["proportional to e_1 (non-null)"]}
        row["the non-null-led members"] = sorted(nonnull)
        row["as predicted (set)"] = nonnull == NONNULL_EXPECTED[(r, n)]
        ok3 = ok3 and nonnull == NONNULL_EXPECTED[(r, n)]
        h3[f"r={r} n={n}"] = row
    H3 = ok3 and all(len([a for a in leads[c] if leads[c][a]["proportional to e_1 (non-null)"]]) == 1
                     for c in THREE_GEN)
    h4 = {"B1740's F_-2 is the member a = -2 of h(20, 1) with eps = +1": -2 in members[(20, 1)] and eps_of(-2) == 1,
          "W127's index I(cond, r, n) at each space": {k: out[k]["H4 W127's index I(cond, r, n)"] for k in out}}
    res = {"arc": "W143", "rule": "W143_RULE.md",
           "C0 the instrument and the record": c0,
           "cells": {"H1": bool(H1), "H2": bool(H2), "H3": bool(H3), "H4": "read-out"},
           "H1": h1, "H2": h2, "H3": h3, "H4": h4, "per space": out,
           "seconds": round(time.time() - t0, 1)}
    OUT.write_text(json.dumps(res, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps({"cells": res["cells"], "C0": c0, "seconds": res["seconds"]}, indent=1, default=str))


if __name__ == "__main__":
    main()
