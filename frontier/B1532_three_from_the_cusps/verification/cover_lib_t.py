#!/usr/bin/env python3
"""B1532 -- THREE FROM THE CUSPS: route T, the twisted terms of a pulled-back member.  Library; nothing sealed is computed on
import.

The object.  On a level M_n of m004 take a member of sm:B1515's frame at the hyperbolic point, lam = 1: a fibre character nu of
T_n (trivial on the cusp), V = nu (x) rho_1, L = nu^-4, V_eta = nu^5 (x) rho_1, and W1(c) = [[V, c L], [0, L]] for a class
c in H^1(V_eta).  For a character chi of T_n (also trivial on the cusp) the TERM is
    T(nu, chi, c) = (I(W1(c) (x) chi), I(Lambda^2 W1(c) (x) chi)),
main's B1297 index of each module (sm:B1515's A.ix).  By Lemma S (PREREGISTRATION) the pulled-back member on the abelian cover
cut out by a subgroup B of T_n^ counts sum_{chi in B} T(nu, chi, c).  NB Lambda^2 W1 (x) chi, not Lambda^2 (W1 (x) chi).

The classes.  h^1(V_eta) is 1 or 2 at lam = 1 on M2-M6 (sm:B1515's banked census).
  - one-class members: c is unique up to scale and W1(c) does not depend on the scale; one term per chi.
  - two-class members (M6, 120 of them): H^1(V_eta) = <c_b, c_int>, c_int spanning the interior line (c_int|_P a peripheral
    coboundary), c_b any other class.  Every class other than c_int is c_s = c_b + s c_int up to scale.  Lemma J: off c_int the
    term is constant in s except at the SPECIAL points, where h^1 of one of E = W1(c) (x) chi, E*, Lambda^2 E, (Lambda^2 E)*
    jumps.  Each of the four is an extension 0 -> S -> M(c) -> Q -> 0 whose class is linear in c, and h^1(M(c)) =
    h^1(S) - rank delta0 + dim ker delta1_c, delta1_c : H^1(Q) -> coker d1_S, [y] -> [Phi(c) y], Phi(c) y the S-part of
    d1_M(c) (0, y).  So the special s are where the pencil delta1_{c_b} + s delta1_{c_int} drops rank: one linear condition, or
    (rank two) the common roots of its 2 x 2 minors, which may be a conjugate pair over GF(p^2).  Each special class is READ
    directly (a pair through the restriction of scalars to GF(p): R(E) has twice E's cohomology, so I(E) = I(R(E)) / 2).
  - The generic term is read at c_{s_g}, s_g a fixed hash-derived element avoiding that chi's special points.

Route T is sm:B1515's route T, imported unchanged: B1511's Reidemeister-Schreier presentation of M_n and its tower_lib, B1374's
index_lib over GF(p).  Route L (cover_lib_l.py) shares none of this code."""
import hashlib
import importlib.util
import os
from fractions import Fraction
from pathlib import Path

from sympy.ntheory.residue_ntheory import sqrt_mod
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("ORIGIN_AXIOM_ROOT", HERE.parents[2]))
_spec = importlib.util.spec_from_file_location("b1515_route_t", ROOT / "frontier/B1515_the_hyperbolic_point/verification/route_t.py")
RT = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(RT)
T = RT.T

PAIRS5 = [(i, j) for i in range(5) for j in range(i + 1, 5)]            # tower_lib.wedge2's basis order
FAMILIES = {
    "E": ([0, 1, 2, 3], [4]),                                            # sub V (x) chi, quotient L (x) chi
    "E*": ([4], [0, 1, 2, 3]),                                           # sub (L chi)*, quotient (V chi)*
    "L2E": ([k for k, (i, j) in enumerate(PAIRS5) if j < 4], [k for k, (i, j) in enumerate(PAIRS5) if j == 4]),
    "L2E*": ([k for k, (i, j) in enumerate(PAIRS5) if j == 4], [k for k, (i, j) in enumerate(PAIRS5) if j < 4]),
}


# ============================================================================================ small helpers
def hash_int(*parts):
    return int(hashlib.sha256(":".join(str(x) for x in parts).encode()).hexdigest(), 16)


def ints(M, p):
    return [[int(x) % p for x in row] for row in M.to_Matrix().tolist()] if M.shape[0] and M.shape[1] else []


def rank_mod(rows, p):
    A = [list(r) for r in rows]
    if not A or not A[0]:
        return 0
    r, ncols = 0, len(A[0])
    for c in range(ncols):
        pr = next((i for i in range(r, len(A)) if A[i][c] % p), None)
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        inv = pow(A[r][c], -1, p)
        A[r] = [x * inv % p for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] % p:
                f = A[i][c]
                A[i] = [(a - f * b) % p for a, b in zip(A[i], A[r])]
        r += 1
        if r == len(A):
            break
    return r


def poly_trim(f, p):
    f = [x % p for x in f]
    while f and f[-1] == 0:
        f.pop()
    return f


def poly_mod(f, g, p):
    f, g = poly_trim(f, p), poly_trim(g, p)
    inv = pow(g[-1], -1, p)
    while len(f) >= len(g):
        c, sh = f[-1] * inv % p, len(f) - len(g)
        for i, x in enumerate(g):
            f[sh + i] = (f[sh + i] - c * x) % p
        f = poly_trim(f, p)
    return f


def poly_gcd(f, g, p):
    f, g = poly_trim(f, p), poly_trim(g, p)
    while g:
        f, g = g, poly_mod(f, g, p)
    if f:
        inv = pow(f[-1], -1, p)
        f = [x * inv % p for x in f]
    return f


def nonresidue(p):
    return next(d for d in range(2, p) if pow(d, (p - 1) // 2, p) == p - 1)


def roots_low_degree(f, p):
    """the roots of a monic polynomial of degree <= 2 over GF(p): [('r', s), ...] or [('q', u, v)] for the conjugate pair
    u +- v w, w^2 = the least non-residue (v normalised to <= (p - 1) / 2)"""
    f = poly_trim(f, p)
    if len(f) <= 1:
        return []
    if len(f) == 2:
        return [("r", (-f[0]) * pow(f[1], -1, p) % p)]
    assert len(f) == 3, ("degree above two", f)
    c0, c1, c2 = f
    inv2a = pow(2 * c2, -1, p)
    disc = (c1 * c1 - 4 * c0 * c2) % p
    u = (-c1) * inv2a % p
    if disc == 0:
        return [("r", u)]
    if pow(disc, (p - 1) // 2, p) == 1:
        r = sqrt_mod(disc, p)
        return sorted([("r", (u + r * inv2a) % p), ("r", (u - r * inv2a) % p)])
    d0 = nonresidue(p)
    t = sqrt_mod(disc * pow(d0, -1, p) % p, p)                    # disc = t^2 d0, so sqrt(disc) = t w
    v = t * inv2a % p
    return [("q", u, min(v, p - v))]


def pencil_points(Db, Di, p, salt):
    """the special s of the pencil Db + s Di (k x m over GF(p)): where its rank is below the generic rank"""
    k = len(Db)
    m = len(Db[0]) if k else 0
    if k == 0 or m == 0:
        return 0, []
    trial = [hash_int("pencil", salt, t) % p for t in range(3)]
    r = max(rank_mod([[(Db[i][j] + s * Di[i][j]) % p for j in range(m)] for i in range(k)], p) for s in trial)
    if r == 0:
        return 0, []
    if r == 1:
        nz = [(i, j) for i in range(k) for j in range(m) if Di[i][j] % p]
        if not nz:
            return 1, []
        i0, j0 = nz[0]
        s = (-Db[i0][j0]) * pow(Di[i0][j0], -1, p) % p
        ok = all((Db[i][j] + s * Di[i][j]) % p == 0 for i in range(k) for j in range(m))
        return 1, ([("r", s)] if ok else [])
    assert r == 2, ("pencil rank above two", r)
    g = []
    for i in range(k):
        for i2 in range(i + 1, k):
            for j in range(m):
                for j2 in range(j + 1, m):
                    a, b = (Db[i][j], Di[i][j]), (Db[i2][j2], Di[i2][j2])
                    c, d = (Db[i][j2], Di[i][j2]), (Db[i2][j], Di[i2][j])
                    minor = [(a[0] * b[0] - c[0] * d[0]) % p, (a[0] * b[1] + a[1] * b[0] - c[0] * d[1] - c[1] * d[0]) % p,
                             (a[1] * b[1] - c[1] * d[1]) % p]
                    g = poly_gcd(g, minor, p) if g else poly_trim(minor, p)
    pts = roots_low_degree(g, p) if g else []
    for pt in pts:
        if pt[0] == "r":
            s = pt[1]
            assert rank_mod([[(Db[i][j] + s * Di[i][j]) % p for j in range(m)] for i in range(k)], p) < 2, "a root that is not a drop"
    return 2, pts


# ============================================================================================ the level
class LevelT:
    def __init__(self, n, p):
        self.n, self.p = n, p
        self.lev = RT.Level(n)
        self.N, self.K = self.lev.N, self.lev.K
        self.A = RT.Arith("gf", self.K, p)
        self.dom = self.A.dom
        self.rho = T.rs_rho(self.lev.cov, self.A.field)
        self.gens, self.rels, self.mu, self.lam = self.lev.cov["gens"], self.lev.rels, self.lev.mu, self.lev.lam
        self.chars = list(self.lev.chars)
        self._cache = {}

    def label(self, ab):
        return f"{Fraction(ab[0], self.N)},{Fraction(ab[1], self.N)}"

    def word_exponent(self, ex, w):
        return sum(ex[ch] if ch.islower() else -ex[ch.lower()] for ch in w)

    def exponents(self, ab):
        ex = self.lev.exponents(ab, 0)
        assert self.word_exponent(ex, self.mu) % self.K == 0 and self.word_exponent(ex, self.lam) % self.K == 0, \
            ("not trivial on the cusp", ab)
        return ex

    def twist(self, rep, ex):
        return T.DMRep(rep.gens, {g: rep.M[g] * self.A.unit(ex[g]) for g in rep.gens})

    def ix(self, rep):
        assert rep.check(self.rels), "a relator fails"
        return self.A.ix(rep, self.rels, self.mu, self.lam)

    def jacobian(self, rep):
        J = None
        for r in self.rels:
            D = rep.fox(r)
            blk = D[self.gens[0]].hstack(*[D[g] for g in self.gens[1:]])
            J = blk if J is None else J.vstack(blk)
        return J

    def key(self, rep):
        return tuple(tuple(int(x) % self.p for x in rep.M[g].to_Matrix()) for g in self.gens)

    def cached(self, kind, rep, fn):
        k = (kind, self.key(rep))
        if k not in self._cache:
            if len(self._cache) > 20000:
                self._cache.clear()
            self._cache[k] = fn(rep)
        return self._cache[k]


def compact(d):
    """main's B1297 index data of one module: [I, a0, a1, t0, r1, b0, b1, s0, q1]"""
    return [d["I"], d["a0"], d["a1"], d["t0"], d["r1"], d["b0"], d["b1"], d["s0"], d["q1"]]


def _d0(rep):
    I = DomainMatrix.eye(rep.d, rep.dom)
    out = None
    for g in rep.gens:
        blk = rep.M[g] - I
        out = blk if out is None else out.vstack(blk)
    return out


def restrict_rep(rep, idx):
    return T.DMRep(rep.gens, {g: rep.M[g].extract(idx, idx) for g in rep.gens})


# ============================================================================================ a member
class MemberT:
    def __init__(self, LT, ab):
        self.LT, self.ab = LT, ab
        self.label = LT.label(ab)
        self.ex = ex = LT.exponents(ab)
        lev, A, rho = LT.lev, LT.A, LT.rho
        self.V = lev.twisted(A, rho, ex, 1)
        self.Veta = lev.twisted(A, rho, ex, 5)
        self.L = lev.line(A, ex, -4)
        assert self.V.check(LT.rels) and self.Veta.check(LT.rels) and self.L.check(LT.rels)
        cls, h1 = T.h1_classes(self.Veta, LT.rels)
        self.h1 = h1
        if h1 == 1:
            self.kind, self.c_one = "one", cls[0]
        elif h1 == 2:
            self.kind = "two"
            self.c_int, self.c_b = self._interior(cls)
            self.s_gen = [1 + hash_int("B1532 generic", LT.n, self.label, LT.p, t) % (LT.p - 1) for t in range(4)]
        else:
            raise AssertionError(("h1(V_eta) outside {1, 2}", ab, h1))

    def _res(self, c):
        return RT.restrict(self.Veta, c, self.LT.mu).vstack(RT.restrict(self.Veta, c, self.LT.lam))

    def _interior(self, cls):
        LT, p = self.LT, self.LT.p
        BP = RT.peripheral_coboundaries(self.Veta, LT.lev)
        null = T.dm_nullspace(self._res(cls[0]).hstack(self._res(cls[1]), BP))
        proj = [[int(v[0, 0].element) % p, int(v[1, 0].element) % p] for v in null]
        assert rank_mod(proj, p) == 1, ("the interior line is not one-dimensional", self.ab)
        a0, a1 = next(x for x in proj if any(x))
        c_int = cls[0] * LT.dom.convert(a0) + cls[1] * LT.dom.convert(a1)
        c_b = cls[0] if a1 else cls[1]
        rB = T.dm_rank(BP)
        assert T.dm_rank(BP.hstack(self._res(c_int))) == rB, "c_int is not interior"
        assert T.dm_rank(BP.hstack(self._res(c_b))) == rB + 1, "c_b is interior"
        return c_int, c_b

    def cls_at(self, s):
        return self.c_b + self.c_int * self.LT.dom.convert(s)

    def W1(self, c):
        W = RT.ext_with_line(self.V, c, self.L, self.LT.gens)
        assert W.check(self.LT.rels)
        return W

    # ---------------------------------------------------------------------------------------- readings
    def term(self, c, exc):
        LT = self.LT
        W = self.W1(c)
        return [compact(LT.ix(LT.twist(W, exc))), compact(LT.ix(LT.twist(T.wedge2_rep(W), exc)))]

    def restricted(self, u, v, exc, d0):
        """the B1297 data of R(W1(c_b + (u + v w) c_int) (x) chi) and of R(Lambda^2 ...), w^2 = d0, over GF(p): the family is affine
        in s, M(u + v w) = M(u) + v w D with D = M(u + 1) - M(u), and R(X + Y w) = [[X, d0 Y], [Y, X]].  For d0 a non-residue this
        is the restriction of scalars from GF(p^2); for d0 a square it splits as M(u + v sqrt d0) (+) M(u - v sqrt d0) (control K9)"""
        LT, p, dom = self.LT, self.LT.p, self.LT.dom
        Wu, Wu1, Wu2 = (self.W1(self.cls_at((u + t) % p)) for t in range(3))
        Lu, Lu1, Lu2 = (T.wedge2_rep(W) for W in (Wu, Wu1, Wu2))
        for X, Y, Z in ((Wu, Wu1, Wu2), (Lu, Lu1, Lu2)):           # the family is affine in s (Lemma J)
            for g in LT.gens:
                assert T.dm_equal(Z.M[g] - Y.M[g], Y.M[g] - X.M[g]), "the family is not affine in s"

        def R(X, Y):
            out = {}
            for g in LT.gens:
                ch = LT.A.unit(exc[g])
                A0 = X.M[g] * ch
                vD = (Y.M[g] - X.M[g]) * ch * dom.convert(v)
                out[g] = A0.hstack(vD * dom.convert(d0)).vstack(vD.hstack(A0))
            return T.DMRep(LT.gens, out)
        return [compact(LT.ix(R(X, Y))) for X, Y in ((Wu, Wu1), (Lu, Lu1))]

    def term_quadratic(self, u, v, exc):
        """the term at the conjugate pair c_b + (u +- v w) c_int, w^2 = the least non-residue, read over GF(p) through the
        restriction of scalars: R(E) has twice E's cohomology, so every number halves"""
        out = []
        for c in self.restricted(u, v, exc, nonresidue(self.LT.p)):
            assert all(x % 2 == 0 for x in c), ("restriction of scalars: an odd dimension", c)
            out.append([x // 2 for x in c])
        return out

    # ---------------------------------------------------------------------------------------- the pencils (Lemma J)
    def family_modules(self, c, exc):
        LT = self.LT
        W = self.W1(c)
        E = LT.twist(W, exc)
        L2E = LT.twist(T.wedge2_rep(W), exc)
        return {"E": E, "E*": E.dual(), "L2E": L2E, "L2E*": L2E.dual()}

    def pencil(self, Mb, Mi, S_idx, Q_idx):
        LT, p = self.LT, self.LT.p
        d = Mb.d
        for M in (Mb, Mi):
            for g in LT.gens:
                assert M.M[g].extract(Q_idx, S_idx).is_zero_matrix, "not block upper triangular"
        Sb, Qb = restrict_rep(Mb, S_idx), restrict_rep(Mb, Q_idx)
        for g in LT.gens:
            assert T.dm_equal(Sb.M[g], Mi.M[g].extract(S_idx, S_idx)) and T.dm_equal(Qb.M[g], Mi.M[g].extract(Q_idx, Q_idx))
        ys = LT.cached("h1", Qb, lambda R: T.h1_classes(R, LT.rels)[0])

        def leftnull(R):
            J = LT.jacobian(R)
            return [w.transpose() for w in T.dm_nullspace(J.transpose())]
        Nrows = LT.cached("coker", Sb, leftnull)
        m, k = len(ys), len(Nrows)
        h0S, h0Q = (LT.cached("h0", R, lambda X: X.d - T.dm_rank(_d0(X))) for R in (Sb, Qb))
        if m == 0 or k == 0:
            return {"m": m, "k": k, "rank": 0, "points": [], "h0S": h0S, "h0Q": h0Q}
        N = Nrows[0].vstack(*Nrows[1:]) if k > 1 else Nrows[0]
        nr, dS, dQ = len(LT.rels), len(S_idx), len(Q_idx)
        rowsS = [r * d + i for r in range(nr) for i in S_idx]
        rowsQ = [r * d + i for r in range(nr) for i in Q_idx]

        def project(M):
            J = LT.jacobian(M)
            cols = []
            for y in ys:
                vals = [LT.dom.zero] * (len(LT.gens) * d)
                for gi in range(len(LT.gens)):
                    for qi, i in enumerate(Q_idx):
                        vals[gi * d + i] = y[gi * dQ + qi, 0].element
                Y = DomainMatrix([[x] for x in vals], (len(vals), 1), LT.dom)
                v = J * Y
                assert v.extract(rowsQ, [0]).is_zero_matrix, "the quotient part of d1 (0, y) is not zero"
                cols.append(N * v.extract(rowsS, [0]))
            return ints(cols[0].hstack(*cols[1:]) if len(cols) > 1 else cols[0], p)
        Db, Di = project(Mb), project(Mi)
        r, pts = pencil_points(Db, Di, p, salt=(LT.n, self.label, LT.p, tuple(S_idx)))
        return {"m": m, "k": k, "rank": r, "points": pts, "h0S": h0S, "h0Q": h0Q}

    def read_two(self, ab_chi, gen2=False):
        """a two-class member at one chi: the interior class, the generic class, every special class"""
        LT, p = self.LT, self.LT.p
        exc = LT.exponents(ab_chi)
        Fb, Fi = self.family_modules(self.c_b, exc), self.family_modules(self.c_int, exc)
        pencils, special = {}, {}
        for fam, (S_idx, Q_idx) in FAMILIES.items():
            pc = self.pencil(Fb[fam], Fi[fam], S_idx, Q_idx)
            pencils[fam] = [pc["m"], pc["k"], pc["rank"], [list(x) for x in pc["points"]], pc["h0S"], pc["h0Q"]]
            for pt in pc["points"]:
                special.setdefault(tuple(pt), []).append(fam)
        rational = {pt[1] for pt in special if pt[0] == "r"}
        s_g = next(s for s in self.s_gen if s not in rational)
        row = {"int": self.term(self.c_int, exc), "gen": [s_g, self.term(self.cls_at(s_g), exc)], "pencils": pencils,
               "special": []}
        if gen2:
            s2 = next(s for s in self.s_gen if s not in rational and s != s_g)
            row["gen2"] = [s2, self.term(self.cls_at(s2), exc)]
        for pt in sorted(special):
            if pt[0] == "r":
                rd = self.term(self.cls_at(pt[1]), exc)
            else:
                rd = self.term_quadratic(pt[1], pt[2], exc)
            row["special"].append([list(pt), sorted(special[pt]), rd])
        return row

    def read_one(self, ab_chi):
        return {"c": self.term(self.c_one, self.LT.exponents(ab_chi))}
