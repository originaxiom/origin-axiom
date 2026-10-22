#!/usr/bin/env python3
"""W133 — the web seat's PF1-W, its reading of GENESIS PF1, on the Higgs (the rule: W133_RULE.md, committed and pushed
before this script).

  P0  the instrument (exact series in x = q^(1/8), W123's and W127's): the line-to-parity change on R against theta
      quotients; theta2 theta3 theta4 = 2 eta^3; N'(R) = l_1 (l_3^2 - l_7^2) = 2 eta^-3, so N(R) = (i/4) N'(R) =
      (i/2) eta^-3 and N(eta^4 R) = (i/2) eta^9; main's det Y(a) = (a.R)(a.a)(R.R) as an identity (sympy); R.R = 0
  P1  the obstruction: prod of rho's entries (= det rho . sgn) on S and T against chi_eta^21, exactly; which allowed r
      give chi_eta^(21 + 3r) = chi_eta^9; the x-exponent classes of every section's lines and of eta^(9 - 3r)
  P2  the admissible sections, exactly: over a basis of h(r, n) (W127's kernel_form, N = 6) for (r, n) in (4, 0),
      (4, 1), (12, 1), (20, 1), the cubic system N'(g) = eta^(9 - 3r), coefficient by coefficient up to x^(3 - r)
      and two orders beyond; its Groebner basis over Q (grevlex); the number of solutions with multiplicity; whether
      the multiples of R solve it
  P3  the read-out: the admissible sections and W127's chiral counts at their end data

    python3 -B the_zero_free_higgs.py      # writes the_zero_free_higgs.json beside itself
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
from sympy.polys.orderings import monomial_key

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_field_at_the_end as W127  # noqa: E402  (W127's exact route: kernel_form, h_exact; W123's series)

HR, L, NT = W127.HR, W127.L, W127.NT
EXPS, ALLOWED = W127.EXPS, W127.ALLOWED
OUT = HERE / "the_zero_free_higgs.json"
UPTO = 60
NBOUND = 6
CASES = ((4, 0), (4, 1), (12, 1), (20, 1))
E1, E3, E7 = Fr(1, 8), Fr(3, 8), Fr(7, 8)


def co(s, k):
    return W127.coef(s, k)


def same(a, b, upto=UPTO):
    lo = min(a.v, b.v)
    return all(co(a, k) == co(b, k) for k in range(lo, upto))


def eta_pow(m):
    """eta^m = x^(m/3) prod (1 - x^(8n))^m, for m divisible by 3"""
    assert m % 3 == 0
    c = [Fr(0)] * NT
    c[0] = Fr(1)
    P = L(0, c)
    for n in range(1, NT // 8 + 1):
        if 8 * n < NT:
            f = [Fr(0)] * NT
            f[0], f[8 * n] = Fr(1), Fr(-1)
            P = P * L(0, f)
    base = P if m >= 0 else P.inv()
    out = L(0, c)
    for _ in range(abs(m)):
        out = out * base
    return L(m // 3, out.c)


_KF = {}


def basis(r, n):
    """W127's kernel_form at N = 6, kept once per (r, n)"""
    if (r, n) not in _KF:
        _KF[(r, n)] = W127.kernel_form(r, n, NBOUND)
    return _KF[(r, n)]


def nprime(l1, l3, l7):
    return l1 * (l3 * l3 + (l7 * l7).neg())


# ------------------------------------------------------------------ P0
def P0():
    comps, lines, _, _ = HR.the_R_series()
    t2, t3, t4 = HR.theta2(), HR.theta34(1), HR.theta34(-1)
    prod = t2 * t3 * t4
    inv = prod.inv()
    Fi = lines[E1]
    Fj = (lines[E3] + lines[E7]).scale(Fr(1, 2))
    Fk_over_i = (lines[E3] + lines[E7].neg()).scale(Fr(1, 2))
    w127 = all(same(W127.R_LINES[e], lines[e]) for e in EXPS)
    c = {"W127's R lines are W123's": bool(w127),
         "F_i = -th2^2 / (th2 th3 th4)": same(Fi, (t2 * t2 * inv).neg()),
         "F_j = -th4^2 / (th2 th3 th4)": same(Fj, (t4 * t4 * inv).neg()),
         "F_k = i th3^2 / (th2 th3 th4)": same(Fk_over_i, t3 * t3 * inv),
         "th2 th3 th4 = 2 eta^3": same(prod, eta_pow(3).scale(Fr(2)))}
    Np = nprime(lines[E1], lines[E3], lines[E7])
    c["N'(R) = 2 eta^-3, so N(R) = (i/2) eta^-3"] = same(Np, eta_pow(-3).scale(Fr(2)))
    c["N'(eta^4 R) = eta^12 N'(R) = 2 eta^9, so N(eta^4 R) = (i/2) eta^9"] = same(eta_pow(12) * Np,
                                                                                   eta_pow(9).scale(Fr(2)))
    A, B, C = (t2 * t2 * inv), (t4 * t4 * inv), (t3 * t3 * inv)
    c["R.R = th2^4 + th4^4 - th3^4 over (th2 th3 th4)^2 = 0 to x^60"] = all(
        co(A * A + B * B + (C * C).neg(), k) == 0 for k in range(-4, UPTO))
    a = sp.symbols("a1:4")
    R = sp.symbols("R1:4")
    av, Rv = sp.Matrix(a), sp.Matrix(R)
    aR = (av.T * Rv)[0]
    Y = av * Rv.T + Rv * av.T - aR * sp.eye(3)
    c["det Y(a) = (a.R)(a.a)(R.R), an identity"] = sp.expand(Y.det() - aR * (av.T * av)[0] * (Rv.T * Rv)[0]) == 0
    return {"checks": c, "N'(R) leading terms": [str(co(Np, k)) for k in range(Np.v, Np.v + 24)]}, all(c.values())


# ------------------------------------------------------------------ P1
def P1():
    z = sp.exp(sp.I * sp.pi / 4)
    Pm = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    Li = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
    rS, rT = z * Pm, z * Li
    num = lambda M: np.array([[complex(x) for x in row] for row in M.evalf().tolist()])
    ident = max(float(np.abs(num(rS) - HR.rS).max()), float(np.abs(num(rT) - HR.rT).max()))
    entries = lambda M: sp.prod([M[i, j] for i in range(3) for j in range(3) if M[i, j] != 0])
    perm_sign = lambda M: sp.Matrix(3, 3, lambda i, j: 1 if M[i, j] != 0 else 0).det()
    chi = lambda m: (sp.exp(-sp.I * sp.pi * m / 4), sp.exp(2 * sp.pi * sp.I * m / 24))
    eq = lambda u, v: sp.simplify(sp.expand_complex(u - v)) == 0
    on_N = (entries(rS), entries(rT))
    detsgn = (rS.det() * perm_sign(rS), rT.det() * perm_sign(rT))
    good_r = [r for r in ALLOWED if all(eq(u, v) for u, v in zip(chi(21 + 3 * r), chi(9)))]
    classes, eta_cls = {}, {}
    ok_classes = True
    for r in ALLOWED:
        for n in (0, 1):
            if W127.h_exact(r, n, NBOUND) == 0:
                continue
            forms = basis(r, n)
            cls = {str(e): sorted({k % 8 for f in forms for k in range(f[e].v, f[e].v + NT - 16) if co(f[e], k)})
                   for e in EXPS}
            classes[f"r={r} n={n}"] = cls
            ok_classes &= all(cls[str(e)] == [int(8 * e)] for e in EXPS)
        ep = eta_pow(9 - 3 * r)
        eta_cls[str(r)] = sorted({k % 8 for k in range(ep.v, ep.v + NT) if co(ep, k)})
    c = {"rho(S), rho(T) are W123's matrices": ident < 1e-12,
         "N's character on S and T: prod of entries = det rho . sgn": all(eq(u, v) for u, v in zip(on_N, detsgn)),
         "det rho . sgn = chi_eta^21 on S and T": all(eq(u, v) for u, v in zip(detsgn, chi(21))),
         "chi_eta^(21 + 3r) = chi_eta^9 iff r = 4 mod 8": good_r == [4, 12, 20],
         "every section's line l_e has x-exponents in 8e mod 8, so N' lies in 7 mod 8": bool(ok_classes),
         "eta^(9 - 3r) lies in 3 - r mod 8, which is 7 iff r = 4 mod 8": all(
             eta_cls[str(r)] == [(3 - r) % 8] for r in ALLOWED) and [r for r in ALLOWED if (3 - r) % 8 == 7] == [
             4, 12, 20]}
    return {"checks": c, "line classes by (r, n)": classes, "eta^(9 - 3r) classes": eta_cls,
            "r with the matching character": good_r}, all(c.values())


# ------------------------------------------------------------------ P2
def cubic_system(r, n):
    forms = basis(r, n)
    d = len(forms)
    cols = W127.columns(r, NBOUND)
    U = {e: min(col[e].v for col in cols) + NT - 8 for e in EXPS}           # a conservative end of every series
    V = {e: min(f[e].v for f in forms) for e in EXPS}
    target = eta_pow(9 - 3 * r)
    K_hi = (3 - r) + 16
    Vm = min(V[E3], V[E7])
    K_lo = V[E1] + 2 * Vm
    assert K_hi - 2 * Vm < U[E1] and K_hi - V[E1] - Vm < min(U[E3], U[E7]), "series too short"
    a = sp.symbols(f"a1:{d + 1}")
    lin = {e: {k: [co(f[e], k) for f in forms] for k in range(V[e], U[e])} for e in EXPS}
    eqs, stated = [], []
    for K in range(K_lo, K_hi + 1):
        T = {}
        zero = [Fr(0)] * d
        for k1 in range(V[E1], K - 2 * Vm + 1):
            l1 = lin[E1].get(k1, zero)
            if not any(l1):
                continue
            for k2 in range(Vm, K - k1 - Vm + 1):
                k3 = K - k1 - k2
                a3, b3 = lin[E3].get(k2, zero), lin[E3].get(k3, zero)
                a7, b7 = lin[E7].get(k2, zero), lin[E7].get(k3, zero)
                for i, j, m in itertools.product(range(d), repeat=3):
                    if not l1[i]:
                        continue
                    v = a3[j] * b3[m] - a7[j] * b7[m]
                    if v:
                        T[(i, j, m)] = T.get((i, j, m), Fr(0)) + l1[i] * v
        poly = sum((sp.Rational(v.numerator, v.denominator) * a[i] * a[j] * a[m] for (i, j, m), v in T.items()),
                   sp.Integer(0))
        t = co(target, K)
        e = sp.expand(poly - sp.Rational(t.numerator, t.denominator))
        if e != 0:
            eqs.append(e)
            stated.append(K)
    return forms, a, eqs, stated, (K_lo, K_hi)


def standard_count(G, gens):
    key = monomial_key("grevlex")                                   # this sympy takes an ordering, not its name
    lms = [max(sp.Poly(g, *gens).monoms(), key=key) for g in G.exprs]
    pure = {}
    for m in lms:
        nz = [i for i, x in enumerate(m) if x]
        if len(nz) == 1:
            pure[nz[0]] = min(pure.get(nz[0], 10 ** 9), m[nz[0]])
    if len(pure) < len(gens):
        return None
    box = itertools.product(*[range(pure[i]) for i in range(len(gens))])
    return sum(1 for mon in box if not any(all(mon[i] >= lm[i] for i in range(len(gens))) for lm in lms))


def coords_of_R(forms):
    """R in the basis (exact), from the lines' coefficients"""
    rows, rhs = [], []
    for e in EXPS:
        lo = min(f[e].v for f in forms)
        for k in range(min(lo, W127.R_LINES[e].v), lo + 40):
            rows.append([co(f[e], k) for f in forms])
            rhs.append(co(W127.R_LINES[e], k))
    M = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in rows])
    b = sp.Matrix([sp.Rational(x.numerator, x.denominator) for x in rhs])
    try:
        sol, params = M.gauss_jordan_solve(b)
    except ValueError:                                                      # R is not in the span
        return None
    return list(sol) if params.shape[0] == 0 else None


def P2():
    rows, ok = {}, True
    t = sp.symbols("t")
    for (r, n) in CASES:
        forms, a, eqs, stated, (K_lo, K_hi) = cubic_system(r, n)
        G = sp.groebner(eqs, *a, order="grevlex", domain=sp.QQ)
        empty = list(G.exprs) == [1]
        zd = (not empty) and G.is_zero_dimensional
        count = standard_count(G, a) if zd else (0 if empty else None)
        cR = coords_of_R(forms) if r == 4 else None
        R_solves = None
        if cR is not None:
            R_solves = all(sp.rem(sp.expand(g.subs(dict(zip(a, [t * x for x in cR])))), 2 * t ** 3 - 1, t) == 0
                           for g in G.exprs)
        rows[f"r={r} n={n}"] = {"dim h": len(forms), "equations (x-exponents)": stated,
                                "window": [K_lo, K_hi], "Groebner basis": [str(g) for g in G.exprs],
                                "empty (no section)": bool(empty), "zero-dimensional": bool(zd),
                                "solutions with multiplicity": count,
                                "R's coordinates": [str(x) for x in cR] if cR is not None else None,
                                "t R with 2 t^3 = 1 solves it": R_solves}
    want = {"r=4 n=0": (3, True), "r=4 n=1": (3, True), "r=12 n=1": (0, None), "r=20 n=1": (0, None)}
    for key, (cnt, rs) in want.items():
        ok &= rows[key]["solutions with multiplicity"] == cnt and rows[key]["t R with 2 t^3 = 1 solves it"] == rs
    dims_ok = [rows[k]["dim h"] for k in want] == [1, 4, 3, 3]
    return {"checks": {"dims 1, 4, 3, 3 (W127)": dims_ok,
                       "exactly the multiples of eta^4 R, three points in h(4, 0) and in h(4, 1); none in h(12, 1), "
                       "h(20, 1)": bool(ok)}, "cases": rows}, bool(ok and dims_ok)


def main():
    p0, ok0 = P0()
    p1, ok1 = P1()
    p2, ok2 = P2()
    w127 = json.loads((HERE / "the_field_at_the_end.json").read_text(encoding="utf-8"))
    I = w127["the index I(cond, r, n)"]
    rd = {"the admissible sections": "as P2 found them",
          "W127's chiral index at r = 4": {cd: {nn: I[cd]["4"][nn] for nn in ("0", "1")} for cd in I},
          "the fork": "named in the record, by hand"}
    cells = {"P0": ok0, "P1": ok1, "P2": ok2}
    out = {"arc": "W133", "rule": "W133_RULE.md", "status": "one run", "P0": p0, "P1": p1, "P2": p2,
           "P3 (read-out)": rd, "cells": {k: bool(v) for k, v in cells.items()},
           "every cell holds": bool(all(cells.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every cell holds:", out["every cell holds"])


if __name__ == "__main__":
    main()
