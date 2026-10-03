#!/usr/bin/env python3
"""B1532 -- THREE FROM THE CUSPS: route L, the twisted terms read independently.  Library; nothing sealed is computed on import.

The owner's rule (NO NEGATIVE FROM A BUG) asks for a second route that shares no code with route T (cover_lib_t.py).  Route L is
sm:B1515's route L, imported unchanged: the mapping-torus presentation G_n = <x, y, t | t g t^-1 = phi^n(g)> with the cusp
<t, ell>, Ballas' matrices built from sm:B1513's own audit backend, its own character enumeration ((a, b) in (Q/Z)^2 with
nu o phi^n = nu), its own GF(p) elimination (numpy), and the interior dimension from one joint linear system.  Here it reads
the same terms T(nu, chi, c) = (I(W1(c) (x) chi), I(Lambda^2 W1(c) (x) chi)) as route T, with its own choices throughout:
  - the interior class c_int: read from route L's joint system K = {(z, v) : d1 z = 0, z(t) = (E(t) - 1) v,
    z(ell) = (E(ell) - 1) v}, whose z-parts are the interior cocycles (route T instead solves the restriction modulo the
    peripheral coboundaries);
  - c_b: route L's own basis class outside the interior line, so route L's s-coordinate is an affine image of route T's;
  - the pencils of Lemma J on route L's own Fox Jacobian (word_map's affine composition) and cokernel;
  - the generic class from route L's own hash.
Only the labels of the characters are shared with route T, as sm:B1515's census compared them: nu(x) = exp(2 pi i a),
nu(y) = exp(2 pi i b), lam = nu(t) = 1, with x = n m^-1, y = m n m^-2 in both (the controls check the words)."""
import hashlib
import importlib.util
import os
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("ORIGIN_AXIOM_ROOT", HERE.parents[2]))
_spec = importlib.util.spec_from_file_location("b1515_route_l", ROOT / "frontier/B1515_the_hyperbolic_point/verification/route_l.py")
RL = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(RL)

LPAIRS5 = [(i, j) for i in range(5) for j in range(i + 1, 5)]           # sm:B1513's compound2 basis order
LFAMILIES = {
    "E": (list(range(4)), [4]),
    "E*": ([4], list(range(4))),
    "L2E": ([k for k, (i, j) in enumerate(LPAIRS5) if j < 4], [k for k, (i, j) in enumerate(LPAIRS5) if j == 4]),
    "L2E*": ([k for k, (i, j) in enumerate(LPAIRS5) if j == 4], [k for k, (i, j) in enumerate(LPAIRS5) if j < 4]),
}


def lhash(*parts):
    return int(hashlib.sha256(("route L:" + ":".join(str(x) for x in parts)).encode()).hexdigest(), 16)


# ============================================================================================ GF(p) polynomials (route L's own)
def _trim(f, p):
    f = [int(x) % p for x in f]
    while f and f[-1] == 0:
        f.pop()
    return f


def _pgcd(f, g, p):
    f, g = _trim(f, p), _trim(g, p)
    while g:
        inv = pow(g[-1], -1, p)
        r = list(f)
        while len(r) >= len(g):
            c, sh = r[-1] * inv % p, len(r) - len(g)
            for i, x in enumerate(g):
                r[sh + i] = (r[sh + i] - c * x) % p
            r = _trim(r, p)
        f, g = g, r
    if f:
        inv = pow(f[-1], -1, p)
        f = [x * inv % p for x in f]
    return f


def _sqrt(a, p):
    """Tonelli-Shanks (route L's own; a must be a non-zero square)"""
    a %= p
    q, s = p - 1, 0
    while q % 2 == 0:
        q, s = q // 2, s + 1
    z = next(z for z in range(2, p) if pow(z, (p - 1) // 2, p) == p - 1)
    m, c, t, r = s, pow(z, q, p), pow(a, q, p), pow(a, (q + 1) // 2, p)
    while t != 1:
        i, t2 = 0, t
        while t2 != 1:
            t2, i = t2 * t2 % p, i + 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c, t, r = i, b * b % p, t * b * b % p, r * b % p
    assert r * r % p == a
    return r


def least_nonresidue(p):
    return next(d for d in range(2, p) if pow(d, (p - 1) // 2, p) == p - 1)


def roots2(f, p):
    f = _trim(f, p)
    if len(f) <= 1:
        return []
    if len(f) == 2:
        return [("r", (-f[0]) * pow(f[1], -1, p) % p)]
    assert len(f) == 3
    c0, c1, c2 = f
    h = pow(2 * c2, -1, p)
    D = (c1 * c1 - 4 * c0 * c2) % p
    u = (-c1) * h % p
    if D == 0:
        return [("r", u)]
    if pow(D, (p - 1) // 2, p) == 1:
        r = _sqrt(D, p)
        return sorted([("r", (u + r * h) % p), ("r", (u - r * h) % p)])
    d0 = least_nonresidue(p)
    t = _sqrt(D * pow(d0, -1, p) % p, p)
    v = t * h % p
    return [("q", u, min(v, p - v))]


# ============================================================================================ the level
class LevelL:
    def __init__(self, n, p):
        self.n, self.p = n, p
        self.chars, self.D = RL.fibre_characters(n)
        self.K = RL.lcm(self.D, 12)
        assert (p - 1) % self.K == 0
        self.F = RL.ModP(p, f"GF({p})")
        self.U = RL.Units(self.F, self.K)
        self.rho = RL.rho1(self.F, n)
        assert self.rho.holds()
        self._cache = {}

    def label(self, ab):
        return f"{ab[0]},{ab[1]}"

    def vals(self, ab, power=1):
        v = RL.character_values(self.U, ab, 0, power)
        assert v["t"] % self.p == 1, "lam != 1"
        ell = RL.line(self.F, self.rho.gens, self.rho.rels, self.rho.peri, v).w(RL.IA.ELL)
        assert int(ell[0, 0]) % self.p == 1, "not trivial on ell"
        return v

    def key(self, rep):
        return tuple(int(x) for k in rep.gens for x in rep.g[k][0].ravel())

    def cached(self, kind, rep, fn):
        k = (kind, self.key(rep))
        if k not in self._cache:
            if len(self._cache) > 20000:
                self._cache.clear()
            self._cache[k] = fn(rep)
        return self._cache[k]


def lsig(ix):
    """route L's signature: [I, a0, h1, t0, n, b0, h1*, s0, n*]"""
    return [ix["I"]] + [ix["E"][k] for k in ("a0", "h1", "t0", "n")] + [ix["E*"][k] for k in ("a0", "h1", "t0", "n")]


def sub_rep(rep, idx):
    return rep.remake({k: rep.g[k][0][np.ix_(idx, idx)].copy() for k in rep.gens})


# ============================================================================================ a member
class MemberL:
    def __init__(self, LL, ab):
        self.LL, self.ab = LL, ab
        self.label = LL.label(ab)
        F, rho = LL.F, LL.rho
        self.V = rho.scaled(LL.vals(ab, 1))
        self.Veta = rho.scaled(LL.vals(ab, 5))
        self.L = RL.line(F, rho.gens, rho.rels, rho.peri, LL.vals(ab, -4))
        assert self.V.holds() and self.Veta.holds() and self.L.holds()
        basis = RL.h1_basis(self.Veta)
        self.h1 = len(basis)
        if self.h1 == 1:
            self.kind, self.c_one = "one", basis[0]
        elif self.h1 == 2:
            self.kind = "two"
            self.c_int, self.c_b = self._interior(basis)
            self.s_gen = [1 + lhash("generic", LL.n, self.label, LL.p, t) % (LL.p - 1) for t in range(4)]
        else:
            raise AssertionError(("h1(V_eta) outside {1, 2}", ab, self.h1))

    def _interior(self, basis):
        """the joint system: (z, v) with d1 z = 0 and z|_P = delta_P v; its z-parts modulo B^1 are the interior classes"""
        F, E = self.LL.F, self.Veta
        d, k = E.d, len(E.gens)
        D0, D1 = RL.d0(E), RL.d1(E)
        I = F.eye(d)
        Am, Xm = RL.word_map(E, E.peri[0])
        Al, Xl = RL.word_map(E, E.peri[1])
        J = F.vstack([F.hstack([D1, F.zeros(D1.shape[0], d)]),
                      F.hstack([Xm, F.smul(-1, F.sub(Am, I))]),
                      F.hstack([Xl, F.smul(-1, F.sub(Al, I))])])
        zs = [F.sub_block(w, 0, k * d, 0, 1) for w in F.nullspace(J)]
        r0 = F.rank(D0)
        inner = [z for z in zs if F.rank(F.hstack([D0, z])) > r0]
        assert inner, "no interior class"
        c_int = inner[0]
        assert F.rank(F.hstack([D0] + zs)) == r0 + 1, "the interior line is not one-dimensional"
        c_b = next(b for b in basis if F.rank(F.hstack([D0, c_int, b])) == r0 + 2)
        return c_int, c_b

    def cls_at(self, s):
        F = self.LL.F
        return F.add(self.c_b, F.smul(s, self.c_int))

    def W1(self, c):
        W = RL.ext_line(self.V, c, self.L)
        assert W.holds()
        return W

    def term(self, c, ab_chi):
        LL = self.LL
        chi = LL.vals(ab_chi, 1)
        W = self.W1(c)
        Wc, L2c = W.scaled(chi), W.wedge2().scaled(chi)
        assert Wc.holds() and L2c.holds()
        return [lsig(RL.index(Wc)), lsig(RL.index(L2c))]

    def restricted(self, u, v, ab_chi, d0):
        """route L's own R(M(u + v w)), w^2 = d0: [[X, d0 Y], [Y, X]] with M affine in s; the raw signatures (control K9 splits it
        at a square d0)"""
        LL, F, p = self.LL, self.LL.F, self.LL.p
        chi = LL.vals(ab_chi, 1)
        Ws = [self.W1(self.cls_at((u + t) % p)) for t in range(3)]
        Ls = [W.wedge2() for W in Ws]
        for fam in (Ws, Ls):
            for k in fam[0].gens:
                a, b, c = (X.g[k][0] for X in fam)
                assert F.is_zero(F.sub(F.sub(c, b), F.sub(b, a))), "not affine in s"

        def R(X, Y):
            mats = {}
            for k in X.gens:
                A0 = F.smul(chi[k], X.g[k][0])
                vD = F.smul(chi[k] * v % p, F.sub(Y.g[k][0], X.g[k][0]))
                mats[k] = F.vstack([F.hstack([A0, F.smul(d0, vD)]), F.hstack([vD, A0])])
            return X.remake(mats)
        out = []
        for X, Y in ((Ws[0], Ws[1]), (Ls[0], Ls[1])):
            Rm = R(X, Y)
            assert Rm.holds()
            out.append(lsig(RL.index(Rm)))
        return out

    def term_quadratic(self, u, v, ab_chi):
        out = []
        for sg in self.restricted(u, v, ab_chi, least_nonresidue(self.LL.p)):
            assert all(x % 2 == 0 for x in sg), ("restriction of scalars: an odd dimension", sg)
            out.append([x // 2 for x in sg])
        return out

    def family_modules(self, c, ab_chi):
        chi = self.LL.vals(ab_chi, 1)
        W = self.W1(c)
        E, L2E = W.scaled(chi), W.wedge2().scaled(chi)
        return {"E": E, "E*": E.dual(), "L2E": L2E, "L2E*": L2E.dual()}

    def pencil(self, Mb, Mi, S_idx, Q_idx):
        LL, F, p = self.LL, self.LL.F, self.LL.p
        d = Mb.d
        for M in (Mb, Mi):
            for k in M.gens:
                assert not np.any(M.g[k][0][np.ix_(Q_idx, S_idx)] % p), "not block upper triangular"
        Sb, Qb = sub_rep(Mb, S_idx), sub_rep(Mb, Q_idx)
        for k in Mb.gens:
            assert not np.any((Sb.g[k][0] - Mi.g[k][0][np.ix_(S_idx, S_idx)]) % p)
            assert not np.any((Qb.g[k][0] - Mi.g[k][0][np.ix_(Q_idx, Q_idx)]) % p)
        ys = LL.cached("h1", Qb, RL.h1_basis)
        coker = LL.cached("coker", Sb, lambda R: [F.T(w) for w in F.nullspace(F.T(RL.d1(R)))])
        m, kk = len(ys), len(coker)
        h0S, h0Q = (LL.cached("h0", R, lambda X: X.d - F.rank(RL.d0(X))) for R in (Sb, Qb))
        if m == 0 or kk == 0:
            return {"m": m, "k": kk, "rank": 0, "points": [], "h0S": h0S, "h0Q": h0Q}
        N = F.vstack(coker)
        nr, dQ = len(Mb.rels), len(Q_idx)
        rowsS = [r * d + i for r in range(nr) for i in S_idx]
        rowsQ = [r * d + i for r in range(nr) for i in Q_idx]
        ng = len(Mb.gens)

        def project(M):
            D1 = RL.d1(M)
            cols = []
            for y in ys:
                Y = np.zeros((ng * d, 1), dtype=np.int64)
                for gi in range(ng):
                    for qi, i in enumerate(Q_idx):
                        Y[gi * d + i, 0] = y[gi * dQ + qi, 0]
                v = F.mul(D1, Y)
                assert not np.any(v[rowsQ] % p), "the quotient part of d1 (0, y) is not zero"
                cols.append(F.mul(N, v[rowsS]))
            return [[int(x) % p for x in row] for row in np.hstack(cols).tolist()]
        Db, Di = project(Mb), project(Mi)
        return dict(m=m, k=kk, h0S=h0S, h0Q=h0Q, **self._points(Db, Di, (S_idx[0], len(S_idx))))

    def _points(self, Db, Di, salt):
        F, p = self.LL.F, self.LL.p
        k, m = len(Db), len(Db[0])
        A, B = np.array(Db, dtype=np.int64), np.array(Di, dtype=np.int64)
        trial = [lhash("pencil", self.LL.n, self.label, salt, t) % p for t in range(3)]
        r = max(F.rank((A + s * B) % p) for s in trial)
        if r == 0:
            return {"rank": 0, "points": []}
        if r == 1:
            idx = np.argwhere(B % p)
            if len(idx) == 0:
                return {"rank": 1, "points": []}
            i0, j0 = (int(x) for x in idx[0])
            s = (-int(A[i0, j0])) * pow(int(B[i0, j0]), -1, p) % p
            return {"rank": 1, "points": [("r", s)] if not np.any((A + s * B) % p) else []}
        assert r == 2, ("pencil rank above two", r)
        g = []
        for i in range(k):
            for i2 in range(i + 1, k):
                for j in range(m):
                    for j2 in range(j + 1, m):
                        # det [[A_ij + s B_ij, A_ij2 + s B_ij2], [A_i2j + s B_i2j, A_i2j2 + s B_i2j2]]
                        a1, b1 = int(A[i, j]), int(B[i, j])
                        a2, b2 = int(A[i2, j2]), int(B[i2, j2])
                        a3, b3 = int(A[i, j2]), int(B[i, j2])
                        a4, b4 = int(A[i2, j]), int(B[i2, j])
                        minor = [a1 * a2 - a3 * a4, a1 * b2 + b1 * a2 - a3 * b4 - b3 * a4, b1 * b2 - b3 * b4]
                        g = _pgcd(g, minor, p) if g else _trim(minor, p)
        pts = roots2(g, p) if g else []
        for pt in pts:
            if pt[0] == "r":
                assert F.rank((A + pt[1] * B) % p) < 2, "a root that is not a drop"
        return {"rank": 2, "points": pts}

    def read_two(self, ab_chi, gen2=False):
        Fb, Fi = self.family_modules(self.c_b, ab_chi), self.family_modules(self.c_int, ab_chi)
        pencils, special = {}, {}
        for fam, (S_idx, Q_idx) in LFAMILIES.items():
            pc = self.pencil(Fb[fam], Fi[fam], S_idx, Q_idx)
            pencils[fam] = [pc["m"], pc["k"], pc["rank"], [list(x) for x in pc["points"]], pc["h0S"], pc["h0Q"]]
            for pt in pc["points"]:
                special.setdefault(tuple(pt), []).append(fam)
        rational = {pt[1] for pt in special if pt[0] == "r"}
        s_g = next(s for s in self.s_gen if s not in rational)
        row = {"int": self.term(self.c_int, ab_chi), "gen": [s_g, self.term(self.cls_at(s_g), ab_chi)], "pencils": pencils,
               "special": []}
        if gen2:
            s2 = next(s for s in self.s_gen if s not in rational and s != s_g)
            row["gen2"] = [s2, self.term(self.cls_at(s2), ab_chi)]
        for pt in sorted(special):
            rd = self.term(self.cls_at(pt[1]), ab_chi) if pt[0] == "r" else self.term_quadratic(pt[1], pt[2], ab_chi)
            row["special"].append([list(pt), sorted(special[pt]), rd])
        return row

    def read_one(self, ab_chi):
        return {"c": self.term(self.c_one, ab_chi)}
