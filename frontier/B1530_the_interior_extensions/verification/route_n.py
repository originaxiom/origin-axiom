#!/usr/bin/env python3
"""B1530 -- route N: the readings at 60 digits with sm:B1527's cusp_lib (banked: ranks by singular values, every decision's
margin kept).  Nothing sealed is computed on import.  It shares nothing with route E (exact_lib) but the group presentations.

- The four at the hyperbolic point: sm:B1527's family_lib (sm:B1523's seeded route F at 60 digits, conjugated so that the cusp
  fixes infinity, in Ballas' paraboloid frame).  A level M_n of m004 is its bundle with t -> t^n.
- Classes.  Z^1 is the kernel of the Fox matrix.  The interior classes are the cocycles whose restriction to P is a coboundary
  there, modulo B^1: a numerical kernel, projected off B^1.  A boundary-type class is a Z^1 vector orthogonal to B^1 and to the
  interior class.
- W1 = [[V, c L], [0, L]] is built here: cusp_lib.extension covers only L = 1.  Lambda^2 is cusp_lib.wedge2_module and the
  index is cusp_lib.class_index, which checks the B1297, annihilator and Lemma E identities at every reading."""
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import exact_states as S  # noqa: E402

mp.mp.dps = 60


def lib():
    return S.load(S.B1527, "cusp_lib", "cusp_lib")


def group(sign, word):
    FL = S.family()
    G, img = FL.word_group(sign, word)
    chars, D = FL.torsion_characters(img)
    return G, img, chars, D


def four_mats(sign, word, level=1):
    """the four at the hyperbolic point of the word state (level n: t -> t^n), 60 digits"""
    FL = S.family()
    mp.mp.dps = 60
    A2, B2, T2, _ = FL.hyperbolic_sl2(sign, word)
    M2 = FL.to_cusp_frame(A2, B2, T2, sign, 0)
    rho = FL.paraboloid_module(M2)
    mats = {g: rho.M[g] for g in "abt"}
    if level != 1:
        Tn = mp.eye(4)
        for _ in range(level):
            Tn = Tn * mats["t"]
        mats["t"] = Tn
    return mats


def char_values(sign, u, kappa_turn=0):
    na, nb = mp.expjpi(2 * mp.mpf(u[0].numerator) / u[0].denominator), mp.expjpi(2 * mp.mpf(u[1].numerator) / u[1].denominator)
    k = mp.expjpi(2 * mp.mpf(kappa_turn.numerator) / kappa_turn.denominator) if kappa_turn else mp.mpc(1)
    lam = k if sign == "+" else k / (na * nb)
    return {"a": na, "b": nb, "t": lam}


def char_power(ch, m):
    return {g: v ** m for g, v in ch.items()}


def module(mats, ch):
    L = lib()
    return L.Module({g: ch[g] * mats[g] for g in "abt"})


def line_values(ch):
    return dict(ch)


class Classes:
    """Z^1, B^1 and the interior subspace for one module, numerically"""

    def __init__(self, G, mod):
        L = lib()
        self.L, self.G, self.mod = L, G, mod
        self.mg = L.Margins()
        d, gens = mod.d, G.gens
        self.d, self.ng = d, len(gens)
        J = L.vstack(*[L.fox_row(r, mod, gens) for r in G.rels])
        self.Z = L.kernel(J, self.mg)                                    # orthonormal columns
        self.B = L.vstack(*[mod.M[g] - mp.eye(d) for g in gens])         # coboundary columns
        self.rB = L.rank(self.B, self.mg)
        self.h1 = self.Z.cols - self.rB
        self.R = L.vstack(*[L.fox_row(p, mod, gens) for p in G.cusp])
        self.BD = L.vstack(*[mod.word(p) - mp.eye(d) for p in G.cusp])
        # the complement of B^1 in C^(d ng): an orthonormal basis of B^perp
        self.QB = L.kernel(self.B.H, self.mg)

    def off_B(self, z):
        return self.QB * (self.QB.H * z)

    def _rank_abs(self, P):
        """the rank of a matrix whose columns are projections of unit vectors: a singular value is zero below REL_TOL in
        absolute terms (a relative threshold would read rounding noise as rank when the matrix is zero; this was the dry
        run's finding, PREREGISTRATION section 6)"""
        if P.cols == 0:
            return 0, None, []
        U, Sv, Wh = mp.svd_c(P, full_matrices=False)
        s = sorted([abs(Sv[i]) for i in range(min(P.rows, P.cols))], reverse=True)
        r = sum(1 for x in s if x > self.L.REL_TOL)
        if s:
            # margins relative to 1, the scale of the unit vectors projected
            if r > 0:
                self.mg.kept = min(self.mg.kept, s[r - 1])
            if r < len(s):
                self.mg.dropped = max(self.mg.dropped, s[r])
        return r, U, s

    def interior(self):
        """an orthonormal basis (columns) of the interior classes, represented off B^1"""
        L = self.L
        A = L.hstack(self.R * self.Z, -self.BD)
        K = L.kernel(A, self.mg)
        X = K[:self.Z.cols, :]
        V = self.Z * X                                                    # cocycles restricting to coboundaries
        P = self.off_B(V)
        r, U, s = self._rank_abs(P)
        out = mp.matrix(P.rows, r)
        for k in range(r):
            for i in range(P.rows):
                out[i, k] = U[i, k]
        return out

    def boundary_type(self, ints):
        """an orthonormal basis of the classes off B^1 orthogonal to the interior ones"""
        L = self.L
        P = self.off_B(self.Z)
        if ints.cols:
            P = P - ints * (ints.H * P)
        r, U, s = self._rank_abs(P)
        out = mp.matrix(P.rows, r)
        for k in range(r):
            for i in range(P.rows):
                out[i, k] = U[i, k]
        return out


def cocycle_dict(z, d, gens):
    return {g: z[i * d:(i + 1) * d, 0] for i, g in enumerate(gens)}


def extension(V, z, gens, lval=None):
    """W1 = [[V, c L], [0, L]], c the cocycle of V (x) L^-1 given by its values z on the generators; lval the line's values"""
    L = lib()
    d = V.d
    c = cocycle_dict(z, d, gens)
    mats = {}
    for g in gens:
        lg = lval[g] if lval is not None else mp.mpc(1)
        W = mp.matrix(d + 1, d + 1)
        for i in range(d):
            for j in range(d):
                W[i, j] = V.M[g][i, j]
            W[i, d] = c[g][i] * lg
        W[d, d] = lg
        mats[g] = W
    return L.Module(mats)


def reading(G, W):
    """(I(W), I(Lambda^2 W)) with the checks and margins"""
    L = lib()
    a = L.class_index(G, W)
    b = L.class_index(G, L.wedge2_module(W))
    ok = all(a["checks"].values()) and all(b["checks"].values())
    return {"I(W)": a["I"], "I(L2W)": b["I"], "checks": ok,
            "W": {k: a["V"][k] for k in ("a0", "h1", "t0", "r1", "n")} | {"b0": a["V*"]["a0"], "s0": a["V*"]["t0"],
                                                                        "n*": a["V*"]["n"]},
            "L2W": {k: b["V"][k] for k in ("a0", "h1", "t0", "r1", "n")} | {"b0": b["V*"]["a0"], "s0": b["V*"]["t0"],
                                                                          "n*": b["V*"]["n"]},
            "margins": {"W": a["margins"], "L2W": b["margins"]},
            "relator residual": [a["relator residual"], b["relator residual"]]}
