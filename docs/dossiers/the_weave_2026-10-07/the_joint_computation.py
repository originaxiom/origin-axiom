#!/usr/bin/env python3
"""W135 — the joint computation: every piece imposed at once on the weave's surface (the rule: W135_RULE.md,
committed and pushed before this script).

  K0  E8 from the moves (B1270's icosians, exact over Q(sqrt5)): 240 roots and the Gram determinant of a Z-basis;
      2I's order-3 elements, their subgroups and conjugacy; each subgroup's frame (A2, E6 = 72 orthogonal roots, six
      classes of 27); conjugation by 2I on the frames
  K1  the two threes: <R, L> mod 5 = 2I with g = -R L^-1 sent to an order-3 icosian g_q (B1270's construction);
      left multiplication by g_q on the six classes; rho(g) = rho(S)^2 rho(T) rho(S) rho(T) rho(S)^-1 on the triplet
      (W123's matrices, sympy); the equivariant identifications of the parities with the family 3's weights
  K2  the anomaly of the full 27 in rho (x) eps_r (x) chi_eta^m, with W101's weights extended to the 10 and the
      singlet, for every allowed r and |m| <= 24, against W134's condition m = 5 - r mod 8
  K3  the couplings: Gamma' = the image of rho' = rho (x) chi_eta^k, k in {5, 13, 21} (exact, as phases mod 24 times
      signed permutations); its order and element orders; E8's lambda = eps and its symmetric part; the invariants of
      Sym^3 rho' and Lambda^3 rho' (character averages)
  K4  the read-out: the joint survivors (W134's twelve data with three chiral 27s, each checked anomaly-free here);
      Sym^3 rho' against the one-dimensional characters and rho', rho'-bar of Gamma'; the Higgs

    python3 -B the_joint_computation.py      # writes the_joint_computation.json beside itself
"""
import collections
import contextlib
import io
import itertools
import json
import sys
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "frontier" / "B1270_e6_from_the_two_faces" / "verification"))
with contextlib.redirect_stdout(io.StringIO()):
    import e6_from_the_two_faces as B  # noqa: E402  (B1270: Q5, the icosians, bil, qmul)
    import the_bridge_e6_su3 as W134  # noqa: E402  (W134: rho exact, the admissible data, the index)

OUT = HERE / "the_joint_computation.json"
ALLOWED = (0, 4, 8, 12, 16, 20)
MS = range(-24, 25)
Q5, qmul, qconj, bil, key = B.Q5, B.qmul, B.qconj, B.bil, B.key
ONE = (Q5(1), Q5(0), Q5(0), Q5(0))


# ------------------------------------------------------------------ K0
def order(u):
    p, n = u, 1
    while key(p) != key(ONE):
        p = qmul(p, u)
        n += 1
    return n


def qinv(u):
    return qconj(u)                                           # the inverse of a unit quaternion


def gram_det_basis(roots):
    from sympy.matrices.normalforms import hermite_normal_form
    coords = sp.Matrix([[sp.Rational(c.x) for c in r] + [sp.Rational(c.y) for c in r] for r in roots])
    Z = (coords * 4).applyfunc(lambda v: sp.Integer(v))                  # every coordinate is in Z/4
    assert Z == coords * 4
    Hn = hermite_normal_form(Z.T)
    basis = [tuple(B.Q5(B.F(int(Hn[k, j]), 4), B.F(int(Hn[4 + k, j]), 4)) for k in range(4))
             for j in range(Hn.shape[1])]
    G = sp.Matrix([[sp.Rational(bil(a, b)) for b in basis] for a in basis])
    return len(basis), G.det()


def frame(w, roots):
    perp = [r for r in roots if bil(r, ONE) == 0 and bil(r, w) == 0]
    a2 = {key(x) for x in (ONE, w, qmul(w, w))}
    a2 |= {key(tuple(-c for c in x)) for x in (ONE, w, qmul(w, w))}
    rest = [r for r in roots if key(r) not in a2 and not (bil(r, ONE) == 0 and bil(r, w) == 0)]
    cls = collections.Counter((bil(r, ONE), bil(r, w)) for r in rest)
    return perp, rest, cls


def K0():
    units = B.unit_icosians()
    roots = B.e8_roots(units)
    nb, det = gram_det_basis(roots)
    order3 = [u for u in units if order(u) == 3]
    subgroups = {frozenset({key(u), key(qmul(u, u))}) for u in order3}
    rep = order3[0]
    cls_of = {key(qmul(qmul(v, rep), qinv(v))) for v in units}
    one_class = cls_of == {key(u) for u in order3}
    frames = {}
    ok_frames = True
    for sg in subgroups:
        w = next(u for u in order3 if key(u) in sg)
        perp, rest, cls = frame(w, roots)
        ok_frames &= len(perp) == 72 and len(rest) == 162 and sorted(cls.values()) == [27] * 6
        frames[sg] = {key(r) for r in perp}
    e6_sets = list(frames.values())
    perp0, _, _ = frame(rep, roots)
    conj_imgs = set()
    for v in units:
        conj_imgs.add(frozenset(key(qmul(qmul(v, r), qinv(v))) for r in perp0))
    transitive = conj_imgs == {frozenset(s) for s in e6_sets}
    c = {"240 roots of norm 2": len(roots) == 240 and all(bil(r, r) == 2 for r in roots),
         "a Z-basis of 8 vectors with Gram determinant 1 (E8)": nb == 8 and det == 1,
         "2I has 20 elements of order 3, in one conjugacy class": len(order3) == 20 and bool(one_class),
         "they form 10 subgroups": len(subgroups) == 10,
         "each subgroup's frame: 72 orthogonal roots, six classes of 27": bool(ok_frames),
         "the 10 frames are distinct": len({frozenset(s) for s in e6_sets}) == 10,
         "conjugation by 2I permutes the 10 frames transitively": bool(transitive)}
    return {"checks": c, "Gram determinant": str(det)}, all(c.values()), units, roots


# ------------------------------------------------------------------ K1
def iso_sl2f5(units):
    """B1270's construction: R, L mod 5 to two order-5 unit icosians, extended along words and checked"""
    def mul5(A, Bm):
        p, q, r, s_ = A
        t, u, v, w_ = Bm
        return ((p * t + q * v) % 5, (p * u + q * w_) % 5, (r * t + s_ * v) % 5, (r * u + s_ * w_) % 5)
    R5, L5, I5 = (1, 1, 0, 1), (1, 0, 1, 1), (1, 0, 0, 1)
    ord5 = [u for u in units if order(u) == 5]
    for r in ord5:
        for l in ord5:
            img, frontier, good = {I5: ONE}, [I5], True
            while frontier and good:
                nxt = []
                for M in frontier:
                    for gm, gi in ((R5, r), (L5, l)):
                        P, Qq = mul5(M, gm), qmul(img[M], gi)
                        if P in img:
                            if key(img[P]) != key(Qq):
                                good = False
                                break
                        else:
                            img[P] = Qq
                            nxt.append(P)
                    if not good:
                        break
                frontier = nxt
            if good and len(img) == 120 and len({key(v) for v in img.values()}) == 120:
                g5 = tuple((-x) % 5 for x in mul5(R5, (1, 0, 4, 1)))       # g = -R L^-1
                return img, g5
    return None, None


def K1(units, roots):
    iso, g5 = iso_sl2f5(units)
    gq = iso[g5]
    _, rest, _ = frame(gq, roots)
    cls = {key(r): (bil(r, ONE), bil(r, gq)) for r in rest}
    maps = collections.defaultdict(set)
    for r in rest:
        maps[cls[key(r)]].add(cls[key(qmul(gq, r))])
    perm = {a: next(iter(b)) for a, b in maps.items()}
    well_defined = all(len(b) == 1 for b in maps.values())
    three = [(1, 0), (-1, 1), (0, -1)]
    three_b = [(0, 1), (1, -1), (-1, 0)]
    cyc = lambda S: all(perm[x] in S for x in S) and len({perm[x] for x in S}) == 3 and all(
        perm[perm[perm[x]]] == x and perm[x] != x for x in S)
    rS, rT = W134.rho_exact()
    rg = sp.simplify(rS ** 2 * rT * rS * rT * rS.inv())
    pattern = [[1 if rg[i, j] != 0 else 0 for j in range(3)] for i in range(3)]
    sigma = [row.index(1) for row in pattern] if all(sum(row) == 1 for row in pattern) else None
    is3cycle = sigma is not None and all(sigma[i] != i for i in range(3))
    cube = sp.simplify(rg ** 3)
    scalar = cube.is_diagonal() and all(sp.simplify(cube[i, i] - cube[0, 0]) == 0 for i in range(3))
    ev = [complex(x) for x in np.linalg.eigvals(np.array(rg.evalf().tolist(), dtype=complex))]
    ratios = sorted(round((np.angle(e / ev[0]) / (2 * np.pi)) % 1.0 * 3) % 3 for e in ev)
    # the equivariant identifications: bijections parities -> weights of the 3 intertwining sigma and perm
    idents = 0
    for phi in itertools.permutations(three):
        if all(perm[phi[i]] == phi[sigma[i]] for i in range(3)) if sigma else False:
            idents += 1
    c = {"g = -R L^-1 mod 5 has order 3 and maps to an order-3 icosian": order(gq) == 3,
         "left multiplication by g_q is well defined on the six classes": bool(well_defined),
         "it cycles the 3's three weights and the 3-bar's": cyc(three) and cyc(three_b),
         "rho(g) is monomial with a 3-cycle pattern": bool(is3cycle),
         "rho(g)^3 is a scalar": bool(scalar),
         "the eigenvalue ratios are (1, omega, omega^2)": ratios == [0, 1, 2],
         "exactly 3 equivariant identifications of the parities with the weights": idents == 3}
    return {"checks": c, "rho(g)": str(rg), "rho(g)^3": str(cube), "g_q": [str(x) for x in gq]}, all(c.values())


# ------------------------------------------------------------------ K2
FIELDS27 = {"Q": (2, 3, 6), "u": (1, 0, 3), "d": (1, 0, 3), "L": (0, 1, 2), "e": (0, 0, 1), "nu": (0, 0, 1),
            "Hu": (0, 1, 2), "Hd": (0, 1, 2), "D": (1, 0, 3), "Dc": (1, 0, 3), "S": (0, 0, 1)}
SM16 = ("Q", "u", "d", "L", "e", "nu")


def anomalies(r, m, fields):
    c = 9 + 3 * r + 3 * m
    return tuple(sum(FIELDS27[f][g] for f in fields) * c % 24 for g in range(3))


def K2():
    sums = tuple(sum(v[g] for v in FIELDS27.values()) for g in range(3))
    sums16 = tuple(sum(FIELDS27[f][g] for f in SM16) for g in range(3))
    full = all((anomalies(r, m, FIELDS27) == (0, 0, 0)) == W134.admissible(r, m) for r in ALLOWED for m in MS)
    sm = all((anomalies(r, m, SM16) == (0, 0, 0)) == (m % 2 == 1) for r in ALLOWED for m in MS)
    formula = lambda r, m: ((18 * (3 + r + m)) % 24, (18 * (3 + r + m)) % 24, (81 * (3 + r + m)) % 24)
    form = all(anomalies(r, m, FIELDS27) == formula(r, m) for r in ALLOWED for m in MS)
    w101 = {"Q": (2, 3, 6), "u": (1, 0, 3), "d": (1, 0, 3), "L": (0, 1, 2), "e": (0, 0, 1), "nu": (0, 0, 1)}
    from_w128 = all(tuple(W134_weights()[g].get(f, 0) for g in ("SU3", "SU2", "grav")) == w101[f] for f in SM16)
    c = {"the 27's weight sums are (6, 6, 27), the 16's (4, 4, 16)": sums == (6, 6, 27) and sums16 == (4, 4, 16),
         "the SM fields' weights are W101's": bool(from_w128),
         "n_SU3 = n_SU2 = 18(3 + r + m), n_grav = 81(3 + r + m) mod 24": bool(form),
         "the full 27 is anomaly-free iff m = 5 - r mod 8 (W134's condition)": bool(full),
         "the 16 alone needs only m odd": bool(sm)}
    return {"checks": c}, all(c.values())


def W134_weights():
    with contextlib.redirect_stdout(io.StringIO()):
        import the_consistency_route as W128  # W101's weights as W128 states them
    return W128.WEIGHTS


# ------------------------------------------------------------------ K3
PM = ((0, 1, 0), (1, 0, 0), (0, 0, 1))
LI = ((1, 0, 0), (0, 0, 1), (0, -1, 0))


def gmul(a, b):
    pa, Ma = a
    pb, Mb = b
    M = tuple(tuple(sum(Ma[i][k] * Mb[k][j] for k in range(3)) for j in range(3)) for i in range(3))
    return ((pa + pb) % 24, M)


def gamma(k):
    S = ((3 - 3 * k) % 24, PM)
    T = ((3 + k) % 24, LI)
    e = (0, ((1, 0, 0), (0, 1, 0), (0, 0, 1)))

    def norm(x):                                              # fold an overall sign into the phase
        p, M = x
        f = [v for row in M for v in row if v]
        return ((p + 12) % 24, tuple(tuple(-v for v in row) for row in M)) if f[0] < 0 else x
    gens = [norm(S), norm(T)]
    seen, frontier = {norm(e)}, [norm(e)]
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = norm(gmul(x, g))
                if y not in seen:
                    seen.add(y)
                    nxt.append(y)
        frontier = nxt
    return sorted(seen)


def as_complex(x):
    p, M = x
    return np.exp(2j * np.pi * p / 24) * np.array(M, dtype=complex)


def invariants(G):
    chi = lambda g: complex(np.trace(g))
    mats = [as_complex(x) for x in G]
    sym3 = lambda g: (chi(g) ** 3 + 3 * chi(g @ g) * chi(g) + 2 * chi(g @ g @ g)) / 6
    alt3 = lambda g: (chi(g) ** 3 - 3 * chi(g @ g) * chi(g) + 2 * chi(g @ g @ g)) / 6
    n = len(mats)
    avg = lambda f: sum(f(g) for g in mats) / n
    return mats, avg, sym3, alt3


def eorder(g):
    M, n = g, 1
    while not np.allclose(M, np.eye(3)):
        M, n = M @ g, n + 1
    return n


def K3():
    rows, ok = {}, True
    for k in (5, 13, 21):
        G = gamma(k)
        mats, avg, sym3, alt3 = invariants(G)
        dS = avg(lambda g: sym3(g))
        dA = avg(lambda g: alt3(g))
        real = all(np.allclose(g.imag, 0) for g in mats)
        rot = real and all(abs(np.linalg.det(g) - 1) < 1e-9 for g in mats)
        orders = dict(sorted(collections.Counter(eorder(g) for g in mats).items()))
        rows[str(k)] = {"order": len(G), "real rotations": bool(rot), "element orders": orders,
                        "dim Sym^3 invariants": round(dS.real, 9), "dim Lambda^3 invariants": round(dA.real, 9)}
    eps = sp.LeviCivita
    sym_eps = all(sum(eps(*p) for p in itertools.permutations((i, j, k_))) == 0
                  for i in range(3) for j in range(3) for k_ in range(3))
    c = {"k = 21: the cube's rotation group (order 24, real, det 1; orders 1, 2^9, 3^8, 4^6)":
             rows["21"]["order"] == 24 and rows["21"]["real rotations"]
             and rows["21"]["element orders"] == {1: 1, 2: 9, 3: 8, 4: 6},
         "k = 5, 13: order 72": rows["5"]["order"] == 72 and rows["13"]["order"] == 72,
         "E8's lambda = eps has symmetric part 0": bool(sym_eps),
         "Sym^3 has no invariant for every k": all(abs(rows[k]["dim Sym^3 invariants"]) < 1e-9 for k in rows),
         "Lambda^3 has one invariant for every k": all(abs(rows[k]["dim Lambda^3 invariants"] - 1) < 1e-9
                                                      for k in rows)}
    return {"checks": c, "per k": rows}, all(c.values())


# ------------------------------------------------------------------ K4
def K4():
    w134 = json.loads((HERE / "the_bridge_e6_su3.json").read_text(encoding="utf-8"))
    threes = [tuple(x) for x in w134["E3"]["|I| = 3 among the admissible data"]]
    free = all(anomalies(r, m, FIELDS27) == (0, 0, 0) for (r, m, _) in threes)
    G = gamma(21)
    mats, avg, sym3, _ = invariants(G)
    chi = lambda g: complex(np.trace(g))
    perm_sign = lambda g: round(np.linalg.det(np.abs(g)).real)        # the sign of the underlying permutation
    test = {"trivial": lambda g: 1, "the sign of the permutation": perm_sign, "rho'": chi,
            "rho' (x) sign": lambda g: chi(g) * perm_sign(g)}
    mult = {name: round(avg(lambda g, f=f: sym3(g) * np.conj(f(g))).real, 9) for name, f in test.items()}
    norm2 = round(avg(lambda g: abs(sym3(g)) ** 2).real, 9)
    return {"the joint survivors (W134's twelve, r, m, condition)": [list(x) for x in threes],
            "each is anomaly-free for the full 27": bool(free),
            "Sym^3 rho' (k = 21) against Gamma's characters": mult,
            "<Sym^3, Sym^3> (the sum of squared multiplicities)": norm2,
            "the Higgs": "three doublet pairs, one per family, in the same 27s (a READING)"}


def main():
    k0, ok0, units, roots = K0()
    k1, ok1 = K1(units, roots)
    k2, ok2 = K2()
    k3, ok3 = K3()
    k4 = K4()
    cells = {"K0": ok0, "K1": ok1, "K2": ok2, "K3": ok3}
    out = {"arc": "W135", "rule": "W135_RULE.md", "status": "one run", "K0": k0, "K1": k1, "K2": k2, "K3": k3,
           "K4 (read-out)": k4, "cells": {k: bool(v) for k, v in cells.items()},
           "every cell holds": bool(all(cells.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every cell holds:", out["every cell holds"])


if __name__ == "__main__":
    main()
