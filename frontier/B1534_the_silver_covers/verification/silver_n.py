#!/usr/bin/env python3
"""B1534 -- route N for the silver covers: the same terms at 60 digits with sm:B1527's cusp_lib (banked; ranks by singular
values, the B1297, annihilator and Lemma E identities checked at every index), on the four from sm:B1527's family_lib (a
numerical solve, not route E's exact reader).  Nothing sealed is computed on import.

- Route E's classes (c_b, c_int, or the one class) are carried to route N's frame by the conjugator X, X rho_E X^-1 = rho_N
  (sm:B1530's run_a.conjugator and transport).  A class c_s = c_b + s c_int is carried to X c_b + s X c_int, so both routes
  share the coordinate s.
- Route N computes its own pencils: H^1(Q) from its own Fox kernel (projected off B^1), H^2(S) as the cokernel of its own Fox
  matrix (a numerical left kernel), and delta^1 as the S-part of the Fox coboundary of the lifted Q-cocycles.  Its special s are
  found numerically and compared with route E's exact ones.
- At a special s that is a root of an irreducible quadratic over K, route N reads the module directly at each complex root
  (no restriction of scalars)."""
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1530V = ROOT / "frontier" / "B1530_the_interior_extensions" / "verification"
if str(B1530V) not in sys.path:
    sys.path.insert(0, str(B1530V))
import exact_states as S  # noqa: E402
import route_n as N  # noqa: E402

mp.mp.dps = 60
SPECIAL_TOL = mp.mpf(10) ** -40          # a pencil's smallest singular value counts as zero below this (relative)


def run_a():
    return S.load(B1530V, "run_a", "b1530_run_a")


def setup(sign, word, rhoE):
    mats = N.four_mats(sign, word)
    G, img, chars, D = N.group(sign, word)
    X, xinfo = run_a().conjugator(rhoE, mats)
    return {"sign": sign, "word": word, "mats": mats, "G": G, "X": X, "xinfo": xinfo}


def char(stn, w, k):
    return N.char_values(stn["sign"], (Fraction(w[0]), Fraction(w[1])), Fraction(k))


def member_V(stn, u, k):
    ch = char(stn, u, k)
    V = N.module(stn["mats"], ch)
    lval = N.char_power(ch, -4)
    trivial_L = all(abs(v - 1) < mp.mpf(10) ** -40 for v in lval.values())
    return V, (None if trivial_L else lval)


def carry(stn, c):
    return run_a().transport(c, stn["X"], stn["G"].gens)


def term(stn, V, lval, z, chi):
    """(I(W1 (x) chi), I(Lambda^2 W1 (x) chi)) at the carried class z (a column), with checks and margins"""
    L = N.lib()
    W1 = N.extension(V, z, stn["G"].gens, lval)
    a = L.class_index(stn["G"], L.scaled(W1, chi))
    b = L.class_index(stn["G"], L.scaled(L.wedge2_module(W1), chi))
    ok = all(a["checks"].values()) and all(b["checks"].values())
    return (a["I"], b["I"]), {"checks": ok, "margins": [a["margins"], b["margins"]],
                              "residuals": [a["relator residual"], b["relator residual"]]}


# ============================================================================================ the pencils, numerically
def _perm(L, mod, order):
    return L.Module({g: mp.matrix([[mod.M[g][i, j] for j in order] for i in order]) for g in mod.gens()})


def four_modules(stn, V, lval, z, chi):
    L = N.lib()
    W1 = N.extension(V, z, stn["G"].gens, lval)
    Ew = L.scaled(W1, chi)
    L2 = L.scaled(L.wedge2_module(W1), chi)
    idx = [(i, j) for i in range(5) for j in range(i + 1, 5)]
    sub2 = [a for a, (i, j) in enumerate(idx) if j < 4]
    quo2 = [a for a, (i, j) in enumerate(idx) if j == 4]
    return {"E": (Ew, 4), "E*": (_perm(L, Ew.dual(), [4, 0, 1, 2, 3]), 1), "L2E": (_perm(L, L2, sub2 + quo2), 6),
            "(L2E)*": (_perm(L, L2.dual(), quo2 + sub2), 4)}


def _sub(L, mod, lo, hi):
    return L.Module({g: mp.matrix([[mod.M[g][i, j] for j in range(lo, hi)] for i in range(lo, hi)]) for g in mod.gens()})


def pencil(stn, V, lval, zb, zi, chi, which):
    """(P_b, P_int) as mp matrices (h^2(S) x h^1(Q)), with the lower-left block's size checked"""
    L = N.lib()
    G = stn["G"]
    Mb, dS = four_modules(stn, V, lval, zb, chi)[which]
    Mi, _ = four_modules(stn, V, lval, zi, chi)[which]
    d = Mb.d
    for g in G.gens:
        for i in range(dS, d):
            for j in range(dS):
                assert abs(Mb.M[g][i, j]) < mp.mpf(10) ** -45, "not block upper-triangular"
    Smod, Qmod = _sub(L, Mb, 0, dS), _sub(L, Mb, dS, d)
    mg = L.Margins()
    # H^1(Q): Z^1 off B^1
    CQ = N.Classes(G, Qmod)
    PQ = CQ.off_B(CQ.Z)
    r, U, s = CQ._rank_abs(PQ)
    Y = mp.matrix(PQ.rows, r)
    for k in range(r):
        for i in range(PQ.rows):
            Y[i, k] = U[i, k]
    # H^2(S): the left kernel of S's Fox matrix
    JS = L.vstack(*[L.fox_row(rr, Smod, G.gens) for rr in G.rels])
    F = L.kernel(JS.T, mg)                               # columns f with f^T JS = 0
    dQ = d - dS

    def phi(M, y):
        out = mp.matrix(dS * len(G.rels), 1)
        for ri, rr in enumerate(G.rels):
            Fx = L.fox(rr, M, G.gens)
            for gi, g in enumerate(G.gens):
                for i in range(dS):
                    acc = mp.mpc(0)
                    for j in range(dQ):
                        acc += Fx[g][i, dS + j] * y[gi * dQ + j]
                    out[ri * dS + i, 0] += acc
        return out
    Pb = mp.matrix(F.cols, r)
    Pi = mp.matrix(F.cols, r)
    for j in range(r):
        y = [Y[i, j] for i in range(Y.rows)]
        vb, vi = phi(Mb, y), phi(Mi, y)
        for a in range(F.cols):
            Pb[a, j] = sum(F[i, a] * vb[i, 0] for i in range(F.rows))
            Pi[a, j] = sum(F[i, a] * vi[i, 0] for i in range(F.rows))
    return Pb, Pi, {"h1(Q)": r, "h2(S)": F.cols, "margins": mg.as_dict()}


def _sv(A):
    if A.rows == 0 or A.cols == 0:
        return []
    Sv = mp.svd_c(A, compute_uv=False)
    return sorted([abs(Sv[i]) for i in range(min(A.rows, A.cols))], reverse=True)


def pencil_rank(Pb, Pi, s):
    A = Pb + s * Pi
    sv = _sv(A)
    if not sv:
        return 0, sv
    scale = max(max(_sv(Pb) or [0]), max(_sv(Pi) or [0]), mp.mpf(1))
    return sum(1 for x in sv if x > SPECIAL_TOL * scale), sv


def special_points(Pb, Pi):
    """route N's own special s: the roots of the pencil's minors, kept where the rank drops"""
    if Pb.rows == 0 or Pb.cols == 0:
        return {"generic rank": 0, "special": []}
    rg = max(pencil_rank(Pb, Pi, mp.mpf(s.numerator) / s.denominator)[0]
             for s in (Fraction(7, 3), Fraction(-5, 11), Fraction(13, 2), Fraction(-17, 7)))
    out = {"generic rank": rg, "special": []}
    if rg == 0:
        return out
    cands = []
    nr, nc = Pb.rows, Pb.cols
    if rg == 1:
        for i in range(nr):
            for j in range(nc):
                if abs(Pi[i, j]) > mp.mpf(10) ** -30:
                    cands.append(-Pb[i, j] / Pi[i, j])
    elif rg == 2:
        import itertools
        for rows in itertools.combinations(range(nr), 2):
            for cols in itertools.combinations(range(nc), 2):
                (i1, i2), (j1, j2) = rows, cols
                a = [Pb[i1, j1], Pi[i1, j1]]
                b = [Pb[i1, j2], Pi[i1, j2]]
                c = [Pb[i2, j1], Pi[i2, j1]]
                d = [Pb[i2, j2], Pi[i2, j2]]
                c0 = a[0] * d[0] - b[0] * c[0]
                c1 = a[0] * d[1] + a[1] * d[0] - b[0] * c[1] - b[1] * c[0]
                c2 = a[1] * d[1] - b[1] * c[1]
                if abs(c2) > mp.mpf(10) ** -30:
                    disc = mp.sqrt(c1 * c1 - 4 * c2 * c0)
                    cands += [(-c1 + disc) / (2 * c2), (-c1 - disc) / (2 * c2)]
                elif abs(c1) > mp.mpf(10) ** -30:
                    cands.append(-c0 / c1)
    else:
        raise AssertionError(("a pencil of generic rank > 2", rg))
    for s in cands:
        rk, sv = pencil_rank(Pb, Pi, s)
        if rk < rg and not any(abs(s - t) < mp.mpf(10) ** -30 for t in out["special"]):
            out["special"].append(s)
    return out
