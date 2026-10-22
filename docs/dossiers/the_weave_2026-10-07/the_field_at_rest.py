#!/usr/bin/env python3
"""W130 — GENESIS PF1 on the field's rest state (the rule: W130_RULE.md, committed and pushed before this script, with
its dated correction to H4's phase).

  H0  Hitchin's equation for the uniformizing bundle on the upper half plane, exactly (sympy): F_h, [Phi, Phi*_h], |c|^2
  H1  which forced flat data force a non-zero field at rest: the geometry at (3, 3, 3), its images under every word of
      length <= 6 in the moves' automorphisms and their inverses, five other Fuchsian points (mpmath, 40 digits); the
      quaternion point; W = rho_Q (x) chi_p; the triplet's image group (order 96)
  H2  the size: |Phi| pointwise; the modular torus's area (six modular triangles; the index of <A, B> mod 6); the
      parabolic degree (i/2pi) int F against int |Phi|^2
  H3  the control with the hole closed: the flat metric forces c = 0; an abelian Phi has no floor
  H4  the doublet: the nilpotent cone as C^2/+-1, with eps(h, v) = b v1 - a v2; the uniformizing field's square root
  H5  the read-out

    python3 -B the_field_at_rest.py      # writes the_field_at_rest.json beside itself
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
OUT = HERE / "the_field_at_rest.json"
mp.mp.dps = 40
X = sp.symbols("x", real=True)
Y = sp.symbols("y", real=True, positive=True)
N = sp.Matrix([[0, 0], [1, 0]])


def d_z(f):
    return (sp.diff(f, X) - sp.I * sp.diff(f, Y)) / 2


def d_zb(f):
    return (sp.diff(f, X) + sp.I * sp.diff(f, Y)) / 2


def curvature(h):
    """the Chern curvature of a line with metric h, as the coefficient of dzbar ^ dz: dbar d log h"""
    return sp.simplify(d_zb(d_z(sp.log(h))))


def bracket(H, Phi0):
    """[Phi, Phi*_h] for Phi = Phi0 dz (c = 1), as the coefficient of dzbar ^ dz: M Phi0 - Phi0 M,
    with M = H^-1 Phi0^dag H"""
    M = sp.simplify(H.inv() * Phi0.H * H)
    return sp.simplify(M * Phi0 - Phi0 * M)


# ------------------------------------------------------------------ H0
def H0():
    h1, h2 = Y, 1 / Y
    F = sp.diag(curvature(h1), curvature(h2))
    B = bracket(sp.diag(h1, h2), N)
    a = sp.symbols("a", nonnegative=True)                     # |c|^2
    eqs = [sp.simplify((F + a * B)[i, i] * Y ** 2) for i in range(2)]
    sol = [sp.solve(e, a) for e in eqs]
    lam = 1 / Y ** 2
    K = sp.simplify(-(sp.diff(sp.log(lam), X, 2) + sp.diff(sp.log(lam), Y, 2)) / (2 * lam))
    c = {"the metric 1/y^2 has curvature -1": K == -1,
         "F_h = diag(-1, 1)/(4y^2)": sp.simplify(F - sp.diag(-1, 1) / (4 * Y ** 2)) == sp.zeros(2),
         "[Phi, Phi*_h] = |c|^2 diag(1, -1)/y^2": sp.simplify(B - sp.diag(1, -1) / Y ** 2) == sp.zeros(2),
         "Hitchin's equation holds iff |c|^2 = 1/4": sol == [[sp.Rational(1, 4)], [sp.Rational(1, 4)]],
         "Phi = 0 is not a solution (F_h is not 0)": F != sp.zeros(2)}
    return {"checks": c, "F_h": str(F), "bracket per |c|^2": str(B), "|c|^2": str(sol)}, all(c.values())


# ------------------------------------------------------------------ H1
def mul(P, Q):
    return ((P[0][0] * Q[0][0] + P[0][1] * Q[1][0], P[0][0] * Q[0][1] + P[0][1] * Q[1][1]),
            (P[1][0] * Q[0][0] + P[1][1] * Q[1][0], P[1][0] * Q[0][1] + P[1][1] * Q[1][1]))


def inv(P):
    return ((P[1][1], -P[0][1]), (-P[1][0], P[0][0]))


def tr(P):
    return P[0][0] + P[1][1]


def kappa(A, B):
    return tr(mul(mul(A, B), mul(inv(A), inv(B))))


MOVES = {"lam": lambda a, b: (a, mul(a, b)), "rho": lambda a, b: (mul(a, b), b),
         "lam^-1": lambda a, b: (a, mul(inv(a), b)), "rho^-1": lambda a, b: (mul(a, inv(b)), b)}


def H1():
    A, B = ((1, 1), (1, 2)), ((1, -1), (-1, 2))
    census, worst_trace, kap_ok, triples = 0, 10 ** 9, True, set()
    for n in range(0, 7):
        for word in itertools.product(MOVES, repeat=n):
            a, b = A, B
            for w in word:
                a, b = MOVES[w](a, b)
            t = (tr(a), tr(b), tr(mul(a, b)))
            worst_trace = min(worst_trace, min(t))
            kap_ok &= kappa(a, b) == -2
            triples.add(tuple(sorted(t)))
            census += 1
    C = mul(mul(A, B), mul(inv(A), inv(B)))
    U = ((-C[0][0], -C[0][1]), (-C[1][0], -C[1][1]))
    U_minus_I = ((U[0][0] - 1, U[0][1]), (U[1][0], U[1][1] - 1))
    unipotent = mul(U_minus_I, U_minus_I) == ((0, 0), (0, 0)) and U != ((1, 0), (0, 1))
    fuchs = []
    for (x, y) in [(3, 4), (mp.mpf("2.5"), 5), (mp.mpf("3.5"), mp.mpf("3.5")), (4, 4), (3, 10)]:
        x, y = mp.mpf(x), mp.mpf(y)
        z = (x * y + mp.sqrt(x * x * y * y - 4 * (x * x + y * y))) / 2
        lam = (x + mp.sqrt(x * x - 4)) / 2
        p = (z - y / lam) / (lam - 1 / lam)
        s = y - p
        Am = mp.matrix([[lam, 0], [0, 1 / lam]])
        Bm = mp.matrix([[p, 1], [p * s - 1, s]])
        Cm = Am * Bm * Am ** -1 * Bm ** -1
        fuchs.append({"x, y, z": [mp.nstr(v, 12) for v in (x, y, z)],
                      "|tr[A, B] + 2|": mp.nstr(abs(Cm[0, 0] + Cm[1, 1] + 2), 3),
                      "det B - 1": mp.nstr(abs(mp.det(Bm) - 1), 3),
                      "all traces real and > 2": bool(min(x, y, z) > 2)})
    qa, qb = sp.Matrix([[sp.I, 0], [0, -sp.I]]), sp.Matrix([[0, 1], [-1, 0]])
    qc = sp.simplify(qa * qb * qa.inv() * qb.inv())
    unitary = lambda M: sp.simplify(M * M.H) == sp.eye(2)
    W_ok = all(unitary(ea * qa) and unitary(eb * qb) and sp.simplify((ea * qa) * (eb * qb) * (ea * qa).inv()
                                                                      * (eb * qb).inv()) == -sp.eye(2)
               for ea in (1, -1) for eb in (1, -1))
    with contextlib.redirect_stdout(io.StringIO()):
        import the_consistency_route as W128                    # W128's exact image group of rho
        G, _, _ = W128.image_group()
    w8 = np.exp(1j * np.pi / 4)
    G_unitary = all(np.allclose((w8 ** k * Q) @ (w8 ** k * Q).conj().T, np.eye(3), atol=1e-12) for (k, Q) in G)
    c = {"the geometry: every image of (3, 3, 3) under words of length <= 6 has traces > 2 and tr[A, B] = -2":
             worst_trace > 2 and kap_ok,
         "the geometry's puncture holonomy is -1 times a unipotent other than I": bool(unipotent),
         "five other Fuchsian points: tr[A, B] = -2 to 1e-30 and every trace real and > 2": all(
             mp.mpf(f["|tr[A, B] + 2|"]) < mp.mpf(10) ** -30 and f["all traces real and > 2"] for f in fuchs),
         "the quaternion point is unitary with [a, b] = -I (trace -2)":
             unitary(qa) and unitary(qb) and qc == -sp.eye(2),
         "W = rho_Q (x) chi_p is unitary, with the same commutator, for all four characters": bool(W_ok),
         "the triplet's image group has order 96 and is unitary": len(G) == 96 and G_unitary}
    return {"checks": c, "words": census, "least trace over the words": worst_trace,
            "distinct sorted trace triples": len(triples), "Fuchsian points": fuchs,
            "the geometry's [A, B]": [list(r) for r in C]}, all(c.values())


# ------------------------------------------------------------------ H2
def H2():
    h1, h2 = Y, 1 / Y
    c2 = sp.Rational(1, 4)
    dz_norm2 = Y ** 2                                            # the norm of dz in the metric |dz|^2/y^2
    phi2 = sp.simplify(c2 * (h2 / h1) * dz_norm2)
    inner = sp.integrate(1 / Y ** 2, (Y, sp.sqrt(1 - X ** 2), sp.oo))
    tri = sp.integrate(inner, (X, -sp.Rational(1, 2), sp.Rational(1, 2)))
    gens = [((1, 1), (1, 2)), ((1, -1), (-1, 2))]
    gens = gens + [inv(g) for g in gens]
    red = lambda P: tuple(tuple(v % 6 for v in r) for r in P)
    norm = lambda P: min(red(P), red(((-P[0][0], -P[0][1]), (-P[1][0], -P[1][1]))))
    seen, frontier = {norm(((1, 0), (0, 1)))}, [((1, 0), (0, 1))]
    while frontier:
        nxt = []
        for P in frontier:
            for g in gens:
                Q = tuple(tuple(v % 6 for v in r) for r in mul(P, g))
                if norm(Q) not in seen:
                    seen.add(norm(Q))
                    nxt.append(Q)
        frontier = nxt
    psl6 = set()
    for a, b, cc, d in itertools.product(range(6), repeat=4):
        if (a * d - b * cc) % 6 == 1:
            psl6.add(norm(((a, b), (cc, d))))
    index = sp.Rational(len(psl6), len(seen))
    area = sp.simplify(index * tri)
    deg = sp.simplify(area / (4 * sp.pi))
    int_phi2 = sp.simplify(c2 * area)
    c = {"|Phi| = 1/2 pointwise, with no x, y or tau in it": phi2 == c2,
         "the modular triangle has area pi/3": sp.simplify(tri - sp.pi / 3) == 0,
         "<A, B> has index 6 in PSL(2, Z) (by its image mod 6)": index == 6,
         "the fibre's area is 2 pi = -2 pi chi with chi = -1": sp.simplify(area - 2 * sp.pi) == 0,
         "the parabolic degree (i/2pi) int F = Area/(4pi) = 1/2 = -chi/2": deg == sp.Rational(1, 2),
         "int |Phi|^2 dA = Area/4 = pi deg = pi/2": sp.simplify(int_phi2 - sp.pi * deg) == 0
                                                     and sp.simplify(int_phi2 - sp.pi / 2) == 0}
    return {"checks": c, "|PSL(2, Z/6)|": len(psl6), "|image of <A, B>|": len(seen), "area": str(area),
            "degree": str(deg), "int |Phi|^2": str(int_phi2)}, all(c.values())


# ------------------------------------------------------------------ H3
def H3():
    flat = sp.eye(2)
    B = bracket(flat, N)
    a = sp.symbols("a", nonnegative=True)
    sol = sp.solve(sp.simplify(a * B[0, 0]), a)                   # F = 0, so a [N, N*] = 0
    D = sp.diag(1, -1)
    BD = bracket(flat, D)
    c = {"flat metric: F = 0 and [N, N*] = diag(1, -1) is not 0, so c = 0": B == sp.diag(1, -1) and sol == [0],
         "an abelian Phi = a diag(1, -1) dz solves it for every a (no floor)": BD == sp.zeros(2)}
    return {"checks": c}, all(c.values())


# ------------------------------------------------------------------ H4
def H4():
    a, b = sp.symbols("a b")
    hmat = sp.Matrix([[a * b, -a ** 2], [b ** 2, -a * b]])         # h (x) eps(h, .), eps(h, v) = b v1 - a v2
    phi = -hmat
    nil = sp.simplify(phi * phi) == sp.zeros(2) and sp.simplify(phi.trace()) == 0
    sols = sp.solve(list(phi - N), [a, b], dict=True)
    general = True
    for a0, b0 in ((1, 2), (2 + sp.I, -1), (sp.I, 3 - sp.I), (-2, 1 + 2 * sp.I), (3, -sp.I)):
        target = phi.subs({a: a0, b: b0})
        s = sp.solve(list(phi - target), [a, b], dict=True)
        general &= len(s) == 2 and sp.simplify(s[0][a] + s[1][a]) == 0 and sp.simplify(s[0][b] + s[1][b]) == 0
    root = sp.sqrt(sp.Rational(1, 2))
    hs = [(sp.simplify(root * s_[a]), sp.simplify(root * s_[b])) for s_ in sols]
    norms = [sp.simplify(abs(u) ** 2 + abs(v) ** 2) for (u, v) in hs]    # the O summand's metric is h1 h2 = 1
    c = {"-h (x) eps(h, .) is nilpotent and traceless": bool(nil),
         "the uniformizing N has exactly two square roots, h = (0, +-i)": sorted(str(s_[b]) for s_ in sols) == [
             "-I", "I"] and all(s_[a] == 0 for s_ in sols),
         "every non-zero nilpotent has exactly two square roots, negatives of each other (five cases)": bool(general),
         "sqrt(c) h = (0, +-i/sqrt 2): nowhere zero, |sqrt(c) h|^2 = |c| = |Phi| = 1/2": all(n == sp.Rational(1, 2)
                                                                                           for n in norms)}
    return {"checks": c, "square roots of N": [{str(k): str(v) for k, v in s_.items()} for s_ in sols],
            "sqrt(c) h": [[str(u), str(v)] for (u, v) in hs]}, all(c.values())


def main():
    h0, ok0 = H0()
    h1, ok1 = H1()
    h2, ok2 = H2()
    h3, ok3 = H3()
    h4, ok4 = H4()
    rd = {"the forced data": {
        "the geometry (every Fuchsian point, every move)": "not unitary: the field at rest is not 0",
        "the quaternion common point": "unitary: the field at rest is 0 (its puncture holonomy is -I, semisimple)",
        "W = rho_Q (x) chi_p": "unitary: 0", "the triplet's image group": "unitary: 0"},
        "the forced field": "the uniformizing Higgs field, |Phi| = 1/2 in curvature units at every point and tau; "
                            "int |Phi|^2 = pi times the parabolic degree -chi/2",
        "the hole closed": "the field must vanish",
        "the doublet": "Phi = -h (x) eps(h, .), h = (0, +-i): nowhere zero, unique up to sign, of the fibre's SL(2)",
        "open": "the dictionary between the fibre's SL(2) and the weak SU(2); the coupling to the chiral three"}
    cells = {"H0": ok0, "H1": ok1, "H2": ok2, "H3": ok3, "H4": ok4}
    out = {"arc": "W130", "rule": "W130_RULE.md", "status": "one run", "H0": h0, "H1": h1, "H2": h2, "H3": h3,
           "H4": h4, "H5 (read-out)": rd, "cells": {k: bool(v) for k, v in cells.items()},
           "every cell holds": bool(all(cells.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every cell holds:", out["every cell holds"])


if __name__ == "__main__":
    main()
