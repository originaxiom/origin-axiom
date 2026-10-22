#!/usr/bin/env python3
"""W133, POST HOC (after the one run's read-out, which found P2 failed as predicted: the cubic system has 81, 27 and
27 solutions with multiplicity in h(4, 1), h(12, 1) and h(20, 1)). Nothing here was in the rule.

  Q1  the distinct solutions: the multiplication matrix of a fixed linear form on the quotient ring of W133's
      Groebner basis (sympy normal forms), its eigenvalues at 100 digits (mpmath); the number of distinct values
  Q2  each eigenvector point is a section whose joint coupling is c eta^9: N'(g) / eta^(9 - 3r) at three tau with
      Im tau >= 1.4, from the exact series, against 1
  Q3  the theta-power family, found by hand after the read: F_a = eta^(3 - a) (-th2^a, -th4^a, i th3^a), a = 2 mod 8,
      has N(F_a) = i 2^a eta^9 and twist r = 2a mod 24 (a = 2 is 2 eta^4 R); which F_a lie in h(r, 1), exactly, and
      whether their cube-root multiples solve W133's system
  Q4  W127's index at r = 4, 12 and 20 for n = 1

    python3 -B the_zero_free_higgs_posthoc.py      # writes the_zero_free_higgs_posthoc.json beside itself
"""
import contextlib
import io
import itertools
import json
import sys
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_zero_free_higgs as W133  # noqa: E402  (W133's system, W127's basis and series)

HR, L = W133.HR, W133.L
E1, E3, E7, EXPS = W133.E1, W133.E3, W133.E7, W133.EXPS
OUT = HERE / "the_zero_free_higgs_posthoc.json"
CASES = ((4, 1), (12, 1), (20, 1))
mp.mp.dps = 100
TAUS = (mp.mpc(0, "1.5"), mp.mpc("0.3", "1.4"), mp.mpc("-0.45", "1.6"))
FORM = (3, -2, 5, 7)                                                      # the fixed linear form's coefficients


def standard_monomials(G, gens):
    key = W133.monomial_key("grevlex")
    lms = [max(sp.Poly(g, *gens).monoms(), key=key) for g in G.exprs]
    pure = {}
    for m in lms:
        nz = [i for i, x in enumerate(m) if x]
        if len(nz) == 1:
            pure[nz[0]] = min(pure.get(nz[0], 10 ** 9), m[nz[0]])
    box = itertools.product(*[range(pure[i]) for i in range(len(gens))])
    return [mon for mon in box if not any(all(mon[i] >= lm[i] for i in range(len(gens))) for lm in lms)]


def points(G, gens):
    """the eigenvalues of the multiplication matrix of a fixed linear form (one per solution, with multiplicity),
    their number of distinct values, and the points read off the eigenvectors of its transpose"""
    B = standard_monomials(G, gens)
    idx = {b: k for k, b in enumerate(B)}
    mono = lambda b: sp.prod([g ** e for g, e in zip(gens, b)])
    ell = sum(c * g for c, g in zip(FORM, gens))
    M = mp.matrix(len(B), len(B))
    for k, b in enumerate(B):
        _, rem = G.reduce(sp.expand(ell * mono(b)))
        for (cmon, cf) in sp.Poly(rem, *gens).terms():
            cf = sp.Rational(cf)
            M[idx[cmon], k] = mp.mpf(cf.p) / cf.q
    ev, vr = mp.eig(M.T)
    scale = max(abs(x) for x in ev)
    distinct = []
    for x in ev:
        if all(abs(x - y) > mp.mpf("1e-40") * scale for y in distinct):
            distinct.append(x)
    one = idx[tuple([0] * len(gens))]
    lin = [idx[tuple(1 if j == i else 0 for j in range(len(gens)))] for i in range(len(gens))]
    pts = [[vr[j, k] / vr[one, k] for j in lin] for k in range(len(B))]
    gap = min((abs(ev[i] - ev[j]) / scale for i in range(len(B)) for j in range(i)), default=None)
    return pts, len(B), len(distinct), float(gap) if gap is not None else None


def eta_mp(tau, m):
    q = mp.exp(2j * mp.pi * tau)
    pr, n = mp.mpf(1), 1
    while abs(q ** n) > mp.mpf("1e-110"):
        pr *= 1 - q ** n
        n += 1
    return (mp.exp(2j * mp.pi * tau / 24) * pr) ** m


_EV = {}


def ratio(forms, p, r, tau):
    for i, f in enumerate(forms):
        for e in EXPS:
            if (r, i, e, tau) not in _EV:
                _EV[(r, i, e, tau)] = f[e].ev(tau)
    lines = {e: sum(pi * _EV[(r, i, e, tau)] for i, pi in enumerate(p)) for e in EXPS}
    Np = lines[E1] * (lines[E3] ** 2 - lines[E7] ** 2)
    return Np / eta_mp(tau, 9 - 3 * r)


def power(s, k):
    one = L(0, [Fr(1)] + [Fr(0)] * (W133.NT - 1))
    base = s if k >= 0 else s.inv()
    out = one
    for _ in range(abs(k)):
        out = out * base
    return out


def theta_power_lines(a, r):
    """g = F_a / eta^r, line by line: l_1 = -th2^a, l_3 = th3^a - th4^a, l_7 = -th3^a - th4^a, times eta^(3 - a - r)"""
    t2, t3, t4 = HR.theta2(), HR.theta34(1), HR.theta34(-1)
    e = W133.eta_pow(3 - a - r)
    A, C, D = power(t2, a), power(t3, a), power(t4, a)
    return {E1: (A * e).neg(), E3: (C + D.neg()) * e, E7: (C + D).neg() * e}


def coords(forms, lines):
    rows, rhs = [], []
    for e in EXPS:
        lo = min(f[e].v for f in forms)
        for k in range(min(lo, lines[e].v), lo + 40):
            rows.append([W133.co(f[e], k) for f in forms])
            rhs.append(W133.co(lines[e], k))
    M = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in rows])
    b = sp.Matrix([sp.Rational(x.numerator, x.denominator) for x in rhs])
    try:
        sol, params = M.gauss_jordan_solve(b)
    except ValueError:                                                      # not in the span
        return None
    return list(sol) if params.shape[0] == 0 else None


def main():
    out, t = {}, sp.symbols("t")
    I = json.loads((HERE / "the_field_at_the_end.json").read_text(encoding="utf-8"))["the index I(cond, r, n)"]
    for (r, n) in CASES:
        forms, a, eqs, _, _ = W133.cubic_system(r, n)
        G = sp.groebner(eqs, *a, order="grevlex", domain=sp.QQ)
        pts, nB, nd, gap = points(G, a)
        ratios = [max(abs(ratio(forms, p, r, tau) - 1) for tau in TAUS) for p in pts]
        fam = {}
        for aa in range(-30, 43):
            if aa % 8 != 2 or (2 * aa - r) % 24:
                continue
            c = coords(forms, theta_power_lines(aa, r))
            if c is None:
                fam[str(aa)] = "not in h"
                continue
            two = sp.Integer(2) ** (aa + 2)
            solves = all(sp.rem(sp.expand(g.subs(dict(zip(a, [t * x for x in c])))), two * t ** 3 - 1, t) == 0
                         for g in G.exprs)
            fam[str(aa)] = {"in h": True, "t F_a with 2^(a+2) t^3 = 1 solves the system": bool(solves)}
        out[f"r={r} n={n}"] = {
            "Q1 solutions with multiplicity (W133)": nB, "Q1 distinct eigenvalues": nd,
            "Q1 least relative gap between eigenvalues": gap,
            "Q2 max |N'(g) / eta^(9-3r) - 1| over the eigenvector points and three tau": float(max(ratios)),
            "Q3 theta-power vectors F_a (a = 2 mod 8, 2a = r mod 24, -30 <= a <= 42)": fam,
            "Q4 W127's index I(cond, r, n)": {cd: I[cd][str(r)][str(n)] for cd in I}}
    OUT.write_text(json.dumps({"arc": "W133", "status": "POST HOC, after the read-out", **out}, indent=1,
                              default=str) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
