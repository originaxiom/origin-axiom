"""B1547 -- the library: sm:B1515's frame on N45 at members nu of the cover's own group, in two routes.

A member here is a character nu of pi_1(N45) of order 8, trivial on every cusp, with nu^4 = chi one of the order-2 characters
whose line supply is n(chi) = 3.  The frame is W1(c) = [[nu rho, c L], [0, L]] with L = nu^-4 = chi and c a class of
H^1(N; nu^5 rho) (the cocycle of the off-diagonal entry is c L, as in sm:B1536's route R).

  route R: sm:B1544's floor_lib.RCover (route_r on N45's own Reidemeister-Schreier presentation, p_R).  The characters are
           integer vectors on the Schreier generators: the integer kernel of [relators; peripheral words] (the free part,
           Hom(H_1(N)/peripheral, Z) = Z^4) and its GF(2) complement (the order-2 torsion).  The modules are built on the
           Schreier generators directly; the reading is sm:B1536's route_r.reading body, applied to them.
  route F: sm:B1544's floor_lib.FCover (route_f on the lifted 2-complex of <a, t | ttATAAATA>, p_F).  The characters are
           integer vectors on the cover's edges, gauge-fixed on a spanning tree; the systems are the edge transports twisted
           by nu; the reading is route_f.count's body, applied to them.
The two routes share no code beyond the cover's permutation data; each finds its own characters, members and classes."""
import importlib.util
import itertools
import sys
from collections import deque
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
FLP = ROOT / "frontier" / "B1544_the_floor_at_the_cup_kernel" / "verification" / "floor_lib.py"


def _load(alias, path):
    if alias not in sys.modules:
        spec = importlib.util.spec_from_file_location(alias, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[alias] = mod
        spec.loader.exec_module(mod)
    return sys.modules[alias]


FL = _load("b1547_floor_lib", FLP)


# ============================================================================================ exact helpers
def null_gf2(A):
    """the nullspace (rows) of A over GF(2)"""
    A = [[int(x) % 2 for x in r] for r in A]
    rows = len(A)
    cols = len(A[0]) if rows else 0
    piv, r = [], 0
    for c in range(cols):
        pr = next((i for i in range(r, rows) if A[i][c]), None)
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        for i in range(rows):
            if i != r and A[i][c]:
                A[i] = [x ^ y for x, y in zip(A[i], A[r])]
        piv.append(c)
        r += 1
    out = []
    for f in [c for c in range(cols) if c not in piv]:
        v = [0] * cols
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = A[i][f]
        out.append(v)
    return out


def rank_gf2(rows):
    """the rank over GF(2) of a list of vectors"""
    return len(rows) - len(null_gf2(np.array(rows).T)) if rows else 0


def int_kernel(M):
    """a Z-basis (rows) of the integer kernel of M (saturation asserted)"""
    ns = sp.Matrix(np.asarray(M).tolist()).nullspace()
    out = []
    for v in ns:
        den = sp.ilcm(*[sp.fraction(x)[1] for x in v])
        w = [int(x * den) for x in v]
        g = 0
        for x in w:
            g = sp.igcd(g, x)
        out.append([x // g for x in w])
    from sympy.matrices.normalforms import smith_normal_form
    snf = smith_normal_form(sp.Matrix(out).T, domain=sp.ZZ)
    assert all(abs(snf[i, i]) == 1 for i in range(len(out))), "the integer kernel basis is not saturated"
    return np.array(out, dtype=np.int64)


def split_torsion(Ffree, Ared):
    """two GF(2) solutions of Ared f = 0 completing Ffree mod 2 (the order-2 torsion characters)"""
    base = [list(np.array(w) % 2) for w in Ffree]
    tors = []
    for v in null_gf2(Ared):
        if rank_gf2(base + tors + [v]) > len(base) + len(tors):
            tors.append(v)
    return np.array(tors, dtype=np.int64)


def members(Ffree, T, f0):
    """the 1024 cusp-trivial members over chi = (-1)^f0: exponent vectors mod 8, f0 + 2 sum a_i F_i + 4 sum b_i T_i,
    with a in (Z/4)^4 and b in (Z/2)^2, in this order"""
    out = []
    for a in itertools.product(range(4), repeat=Ffree.shape[0]):
        for b in itertools.product(range(2), repeat=T.shape[0]):
            e = (f0 + 2 * sum(ai * Ffree[i] for i, ai in enumerate(a)) + 4 * sum(bi * T[i] for i, bi in enumerate(b))) % 8
            out.append(((tuple(a), tuple(b)), e))
    return out


def galois_classes(mem, Ffree, T, f0):
    """the Galois orbits nu -> nu^k (k = 1, 3, 5, 7) of the members, as lists of indices; nu^k's exponent vector is k e mod 8,
    identified with a member by its coordinates (a, b) over the lattice (solved mod 2 and mod 4 from k e - f0)"""
    index = {tuple(int(x) for x in e): i for i, (_, e) in enumerate(mem)}
    out, seen = [], set()
    for i, (_, e) in enumerate(mem):
        if i in seen:
            continue
        orb = []
        for k in (1, 3, 5, 7):
            j = index.get(tuple(int(x) for x in (k * e) % 8))
            orb.append(j)
        orb = sorted({j for j in orb if j is not None})
        seen.update(orb)
        out.append(orb)
    return out


# ================================================================================ the members, named alike in both routes
def inv_word(w):
    return "".join(c.swapcase() for c in reversed(w))


def common_loops(perms):
    """based loops at sheet 0 that generate pi_1 of the cover, as words in a and t, from the permutations alone: a breadth-first
    tree over a, t and their inverses, and one loop per edge off it.  Each route evaluates its characters on these loops, so a
    character's values on them (its key) name it in either route."""
    P = {g: list(perms[g]) for g in ("a", "t")}
    d = len(P["a"])
    Pinv = {g: [0] * d for g in P}
    for g in P:
        for x in range(d):
            Pinv[g][P[g][x]] = x
    rep, tree, order, i = {0: ""}, set(), [0], 0
    while i < len(order):
        x = order[i]
        i += 1
        for g in ("a", "t"):
            y = P[g][x]
            if y not in rep:
                rep[y] = rep[x] + g
                tree.add((x, g))
                order.append(y)
            z = Pinv[g][x]
            if z not in rep:
                rep[z] = rep[x] + g.upper()
                tree.add((z, g))
                order.append(z)
    assert len(rep) == d
    return [rep[x] + g + inv_word(rep[P[g][x]]) for x in range(d) for g in ("a", "t") if (x, g) not in tree]


def room3(CH, loops):
    """the fifteen order-2 characters (-1)^f, f a non-zero 0/1 combination of the free lattice's basis, in either route: the
    room-3 ones (n = 3) sorted by their values on the loops mod 2, [(key, f)], and the n of all fifteen, sorted"""
    out, ns = [], []
    for coeffs in itertools.product([0, 1], repeat=CH.F.shape[0]):
        if not any(coeffs):
            continue
        f = sum(a * CH.F[i] for i, a in enumerate(coeffs))
        n = CH.n_of(f)
        ns.append(n)
        if n == 3:
            out.append((CH.values(f, loops, 2), f))
    return sorted(out, key=lambda t: t[0]), sorted(ns)


def population(CH, loops):
    """chi0 (the room-3 character with the least key) and the members over it, sorted by key: (chi0's key, [(key, e)])"""
    r3, _ = room3(CH, loops)
    k0, f0 = r3[0]
    mem = sorted(((CH.values(e, loops, 8), e) for _, e in members(CH.F, CH.T, f0)), key=lambda t: t[0])
    return k0, mem


def galois_rep(key):
    """the least key in the Galois class of a member's key (exponents mod 8): nu -> nu^k, k = 1, 3, 5, 7"""
    return min(tuple((k * x) % 8 for x in key) for k in (1, 3, 5, 7))


def subsets(labels, most=2):
    """the sets U of cusp labels with |U| <= most, in a fixed order (by size, then lexicographically)"""
    return [U for size in range(most + 1) for U in itertools.combinations(sorted(labels), size)]


def ukey(U):
    return ",".join(str(x) for x in U)


def strata(M):
    """X_U for every set U of at most two cusp labels, at a member M of either route: {ukey(U): (dim modulo coboundaries,
    basis)}"""
    out = {}
    for U in subsets(M.labels()):
        X = M.stratum(U)
        out[ukey(U)] = (M.dim_mod(X), X)
    return out


def distinct_strata(dims):
    """the U whose X_U is not X_U' for any U' strictly inside U (X_U' lies in X_U, so a larger dimension), with dim X_U > 0"""
    out = []
    for U, dim in dims.items():
        Us = tuple(int(x) for x in U.split(",")) if U else ()
        inner = [ukey(V) for size in range(len(Us)) for V in itertools.combinations(Us, size)]
        if dim > 0 and all(dim > dims[V] for V in inner):
            out.append(U)
    return out


# ============================================================================================ route R
class RChars:
    """N45's cusp-trivial characters in route R: the free lattice F (rows, on the Schreier generators), the torsion T"""

    def __init__(self, rc):
        cov, p, ng = rc.cov, rc.p, rc.ng
        Rm = np.zeros((len(cov.rels), ng), dtype=np.int64)
        for i, r in enumerate(cov.rels):
            for g, e in r:
                Rm[i, g] += e
        P = np.array(rc.CL.R, dtype=np.int64) % p
        P = np.where(P > p // 2, P - p, P)
        self.Rm, self.P = Rm, P
        A = np.vstack([Rm, P])
        self.F = int_kernel(A)
        self.T = split_torsion(self.F, A)
        self.rc = rc

    def chi(self, f):
        """the line module of (-1)^f"""
        rc = self.rc
        return rc.R.CMod([np.array([[(-1) ** int(x) % rc.p]], dtype=np.int64) for x in f], rc.p)

    def nu(self, e):
        """nu's values on the Schreier generators from an exponent vector mod 8"""
        rc = self.rc
        z8 = rc.root(8)
        return [pow(z8, int(x) % 8, rc.p) for x in e]

    def values(self, e, loops, m):
        """the character's values on the based loops (exponents mod m), by the cover's own rewriting"""
        cov = self.rc.cov
        out = []
        for w in loops:
            ws, end = cov.rewrite(0, w)
            assert end == 0
            out.append(sum(s * int(e[i]) for i, s in ws) % m)
        return tuple(out)

    def n_of(self, f):
        rc = self.rc
        return int(rc.R.Coh(rc.cov, self.chi(np.asarray(f) % 2)).n)

    def tau(self):
        """the deck group on the free lattice: the integer matrix of tau* in the basis F (columns are images)"""
        rc = self.rc
        one = {g: np.eye(1, dtype=np.int64) for g in rc.rho}
        TL = FL.N45L().deck_R_matrix(rc.cov, one, rc.tau, rc.p, e=1)
        Fm = sp.Matrix(self.F.tolist()).T
        cols = []
        for i in range(self.F.shape[0]):
            w = rc.R.mm(TL, (self.F[i] % rc.p).reshape(-1, 1), rc.p).ravel()
            w = np.where(w > rc.p // 2, w - rc.p, w)
            assert not np.any(self.Rm @ w) and not np.any(self.P @ w)
            sol = Fm.gauss_jordan_solve(sp.Matrix(w.tolist()))[0]
            cols.append([int(v) for v in sol])
        return np.array(cols, dtype=np.int64).T


class RMember:
    """route R's frame at a member nu (values on the Schreier generators)"""

    def __init__(self, rc, nu):
        R, p, ng, cov = rc.R, rc.p, rc.ng, rc.cov
        self.rc, self.R, self.p, self.ng, self.cov, self.nu = rc, R, p, ng, cov, [int(x) for x in nu]
        self.Lv = [pow(int(x), (-4) % (p - 1), p) for x in nu]
        self.Vnu = R.CMod([(rc.V.M[j] * self.nu[j]) % p for j in range(ng)], p)
        self.Cmod = R.CMod([(rc.V.M[j] * pow(self.nu[j], 5, p)) % p for j in range(ng)], p)
        self.Lmod = R.CMod([np.array([[self.Lv[j]]], dtype=np.int64) for j in range(ng)], p)
        self.CC = R.Coh(cov, self.Cmod, keep=True)
        self.CL = R.Coh(cov, self.Lmod, keep=True)
        self.CV = R.Coh(cov, self.Vnu, keep=True)
        FV = np.vstack([R.fox(self.Vnu, r, ng) for r in cov.rels]) % p
        self.Q = R.pnull(FV.T % p, p, FV.shape[0])
        self.BC = np.vstack([np.concatenate([((self.Cmod.M[j] - np.eye(4, dtype=np.int64)) % p)[:, kk] for j in range(ng)])
                             for kk in range(4)]) % p
        self.BL = np.concatenate([((self.Lmod.M[j] - np.eye(1, dtype=np.int64)) % p)[:, 0]
                                  for j in range(ng)]).reshape(1, -1) % p
        self.Cs = self.class_basis(self.CC.Zrows, self.BC)
        self.Ys = self.class_basis(self.CL.Zrows, self.BL)
        I = self.interior()
        self.Cint = self.class_basis(I, self.BC) if I.shape[0] else I
        self._K0 = None

    def class_basis(self, Zrows, B):
        R, p = self.R, self.p
        keep, cur = [], B % p
        r = R.prank(cur, p)
        for i in range(Zrows.shape[0]):
            cand = np.vstack([cur, Zrows[i:i + 1] % p])
            rc_ = R.prank(cand, p)
            if rc_ > r:
                cur, r = cand, rc_
                keep.append(i)
        return Zrows[keep] % p

    def interior(self):
        R, p, C, cov = self.R, self.p, self.CC, self.cov
        e, nc = 4, len(cov.cusps)
        RZ = R.mm(C.R, C.Zrows.T, p)
        A = np.zeros((2 * e * nc, C.Zrows.shape[0] + e * nc), dtype=np.int64)
        for T in range(nc):
            A[2 * e * T:2 * e * (T + 1), :C.Zrows.shape[0]] = RZ[2 * e * T:2 * e * (T + 1)]
            A[2 * e * T:2 * e * (T + 1), C.Zrows.shape[0] + e * T:C.Zrows.shape[0] + e * (T + 1)] = \
                (-C.BP[2 * e * T:2 * e * (T + 1), e * T:e * (T + 1)]) % p
        K = R.pnull(A, p, A.shape[1])
        if K.shape[0] == 0:
            return C.Zrows[:0]
        return R.mm(K[:, :C.Zrows.shape[0]], C.Zrows, p)

    def w_mats(self, c):
        p = self.p
        Ws = []
        for j in range(self.ng):
            W = np.zeros((5, 5), dtype=np.int64)
            W[:4, :4] = self.Vnu.M[j]
            W[:4, 4] = (np.asarray(c[j * 4:(j + 1) * 4], dtype=np.int64) * self.Lv[j]) % p
            W[4, 4] = self.Lv[j]
            Ws.append(W % p)
        return Ws

    def cup(self, c):
        R, p, ng = self.R, self.p, self.ng
        E = R.CMod(self.w_mats(c), p)
        FW = np.vstack([R.fox(E, r, ng) for r in self.cov.rels]) % p
        cols = []
        for y in self.Ys:
            psi = np.zeros(5 * ng, dtype=np.int64)
            psi[4::5] = y
            v = R.mm(FW, psi.reshape(-1, 1), p).ravel()
            cols.append(np.concatenate([v[kk * 5:kk * 5 + 4] for kk in range(len(self.cov.rels))]))
        if not cols:
            return np.zeros((self.Q.shape[0], 0), dtype=np.int64)
        return R.mm(self.Q, np.stack(cols, axis=1) % p, p)

    def cup_rank(self, c):
        M = self.cup(c)
        return int(self.R.prank(M, self.p)) if M.size else 0

    def K0(self):
        if self._K0 is None:
            R, p = self.R, self.p
            if self.Cs.shape[0] == 0 or self.Ys.shape[0] == 0:
                self._K0 = self.Cs
            else:
                T = np.stack([self.cup(self.Cs[i]).reshape(-1) for i in range(self.Cs.shape[0])], axis=1) % p
                a = R.pnull(T, p, T.shape[1])
                self._K0 = R.mm(a, self.Cs, p) if a.shape[0] else self.Cs[:0]
        return self._K0

    def dim_mod(self, M):
        if M.shape[0] == 0:
            return 0
        R, p = self.R, self.p
        return int(R.prank(np.vstack([self.BC, M % p]), p) - R.prank(self.BC, p))

    def k0_interior(self):
        """a spanning set (rows) of K0^nu's interior part"""
        R, p = self.R, self.p
        K = self.K0()
        if K.shape[0] == 0 or self.Cint.shape[0] == 0:
            return K[:0]
        A = np.vstack([K, (-self.Cint) % p, self.BC]) % p
        N = R.pnull(A.T % p, p, A.shape[0])
        if N.shape[0] == 0:
            return K[:0]
        return self.class_basis(R.mm(N[:, :K.shape[0]], K, p), self.BC)

    def labels(self):
        return [min(T["orbit"]) for T in self.cov.cusp_list]

    def vanishing(self, idx):
        """the cocycles (rows) whose restriction to each cusp of idx (positions in the cusp list) is a coboundary there"""
        R, p, C = self.R, self.p, self.CC
        e, nz = 4, self.CC.Zrows.shape[0]
        if not idx:
            return C.Zrows % p
        RZ = R.mm(C.R, C.Zrows.T, p)
        A = np.zeros((2 * e * len(idx), nz + e * len(idx)), dtype=np.int64)
        for j, T in enumerate(idx):
            A[2 * e * j:2 * e * (j + 1), :nz] = RZ[2 * e * T:2 * e * (T + 1)]
            A[2 * e * j:2 * e * (j + 1), nz + e * j:nz + e * (j + 1)] = \
                (-C.BP[2 * e * T:2 * e * (T + 1), e * T:e * (T + 1)]) % p
        K = R.pnull(A, p, A.shape[1])
        if K.shape[0] == 0:
            return C.Zrows[:0]
        return R.mm(K[:, :nz], C.Zrows, p)

    def stratum(self, U):
        """X_U: a basis (rows, modulo coboundaries) of K0^nu's classes that vanish on every cusp outside U (cusp labels)"""
        R, p = self.R, self.p
        idx = [i for i, lab in enumerate(self.labels()) if lab not in U]
        K = self.K0()
        Vb = self.vanishing(idx)
        Vb = self.class_basis(Vb, self.BC) if Vb.shape[0] else Vb
        if K.shape[0] == 0 or Vb.shape[0] == 0:
            return K[:0]
        A = np.vstack([K, (-Vb) % p, self.BC]) % p
        N = R.pnull(A.T % p, p, A.shape[0])
        if N.shape[0] == 0:
            return K[:0]
        return self.class_basis(R.mm(N[:, :K.shape[0]], K, p), self.BC)

    def structure(self):
        k0 = self.K0()
        k0i = self.k0_interior()
        return {"h1(nu^5 rho)": int(self.CC.h1), "n(nu^5 rho)": int(self.CC.n), "h1(L)": int(self.CL.h1), "n(L)": int(self.CL.n),
                "dim K0": self.dim_mod(k0), "dim K0 interior": self.dim_mod(k0i)}

    def draw(self, B, rng):
        p = self.p
        a = np.array([[rng.randrange(1, p) for _ in range(B.shape[0])]], dtype=np.int64)
        return self.R.mm(a, B, p).ravel() % p

    def support(self, c):
        R, p, C, e = self.R, self.p, self.CC, 4
        rcv = R.mm(C.R, c.reshape(-1, 1) % p, p)
        labels = [min(T["orbit"]) for T in self.cov.cusp_list]
        out = []
        for i, lab in enumerate(labels):
            BPi = C.BP[2 * e * i:2 * e * (i + 1), e * i:e * (i + 1)]
            if R.prank(np.hstack([BPi, rcv[2 * e * i:2 * e * (i + 1)]]), p) > R.prank(BPi, p):
                out.append(lab)
        return sorted(out)

    def reading(self, c):
        """sm:B1536's route_r.reading at the member's frame (its body, applied to the modules built on the cover)"""
        R, p, cov = self.R, self.p, self.cov
        Ws = self.w_mats(c)
        E = R.CMod(Ws, p)
        L2 = R.CMod([R.wedge2_tensor(W, p) for W in Ws], p)
        Es = E.dual().sub([4, 0, 1, 2, 3])
        L2s = L2.dual().sub(list(range(6, 10)) + list(range(6)))
        mods = {"E": (E, list(range(4)), [4]), "E*": (Es, [0], [1, 2, 3, 4]),
                "L2": (L2, list(range(6)), list(range(6, 10))), "L2*": (L2s, [0, 1, 2, 3], [4, 5, 6, 7, 8, 9])}
        C = {}
        for nm, (md, sub, quo) in mods.items():
            C[nm] = R.Coh(cov, md)
            for part, idx in (("S", sub), ("Q", quo)):
                C[nm + "." + part] = R.Coh(cov, md.sub(idx))
        dual = {"E": "E*", "E*": "E", "L2": "L2*", "L2*": "L2"}
        pd = {("E", "S"): ("E*", "Q"), ("E", "Q"): ("E*", "S"), ("L2", "S"): ("L2*", "Q"), ("L2", "Q"): ("L2*", "S")}
        pd.update({v: k for k, v in pd.items()})

        def ident(A, B):
            Iv = A.n - B.n
            return Iv, (Iv == (A.a0 - B.a0) + B.t0 - A.r1 and A.r1 + B.r1 == A.t0 + B.t0 == A.h1P == B.h1P and
                        Iv == B.h1 - A.h1 + 2 * (A.a0 - B.a0) + B.t0 - A.t0)
        I, ok = {}, True
        for nm in mods:
            I[nm], o = ident(C[nm], C[dual[nm]])
            ok = ok and o
        pieces = {}
        for nm in mods:
            pieces[nm] = []
            for part in ("S", "Q"):
                dn, dp = pd[(nm, part)]
                v, o = ident(C[nm + "." + part], C[dn + "." + dp])
                pieces[nm].append(v)
                ok = ok and o
        les = {}
        for nm in mods:
            S_, Q_, X_ = C[nm + ".S"], C[nm + ".Q"], C[nm]
            rk0 = S_.a0 + Q_.a0 - X_.a0
            les[nm] = {"rk d0": rk0, "rk d1": S_.h1 + Q_.h1 - X_.h1 - rk0, "rk d0_P": S_.t0 + Q_.t0 - X_.t0}
        k, nQ2s, nV, nL, b0 = les["L2"]["rk d0_P"], C["L2*.S"].n, C["E.S"].n, C["E.Q"].n, les["E"]["rk d0"]
        checks = {
            "identities (B1297, annihilator, Lemma E) on every module and piece": ok,
            "I(dual) = -I": I["E*"] == -I["E"] and I["L2*"] == -I["L2"],
            "I(S) = I(Q) = 0 for every piece": all(v == [0, 0] for v in pieces.values()),
            "I(L2) = k - rk d1(L2*)": I["L2"] == k - les["L2*"]["rk d1"],
            "W: rk d1(E*) <= k + n(L)": les["E*"]["rk d1"] <= k + nL,
            "I(E) = -b0 + k + rk d1(E) - rk d1(E*)": I["E"] == -b0 + k + les["E"]["rk d1"] - les["E*"]["rk d1"],
            "cap: -n((VL)*) <= I(L2) <= 0": -nQ2s <= I["L2"] <= 0,
            "cap: I(E) >= -b0 - n(L)": I["E"] >= -b0 - nL,
        }
        return {"count": [int(I["E"]), int(I["L2"])], "k": int(k), "b0": int(b0), "n(V)": int(nV), "n(L)": int(nL),
                "n((VL)*)": int(nQ2s), "rk d1": {nm: int(les[nm]["rk d1"]) for nm in les},
                "rk delta1_W": self.cup_rank(c), "support": self.support(c),
                "all": bool(all(checks.values())), "failed": [kk for kk, v in checks.items() if not v]}


# ============================================================================================ route F
class FChars:
    """N45's cusp-trivial characters in route F: the free lattice F (rows, on the cover's edges, zero on a spanning tree),
    the torsion T"""

    def __init__(self, fc):
        Fm, p, cov = FL.F(), fc.p, fc.cov
        C = fc.CL

        def sym(M):
            M = np.array(M, dtype=np.int64) % p
            return np.where(M > p // 2, M - p, M)
        one = {(x, g): np.eye(1, dtype=np.int64) for x in range(cov.d) for g in cov.gens}
        D1 = np.zeros((cov.d, 2 * cov.d), dtype=np.int64)
        for x in range(cov.d):
            row, _ = Fm.Coh.path_row(cov, one, one, cov.S.R, x, p)
            D1[x:x + 1, :] = row
        D1, Rr = sym(D1), sym(C.R)
        tree, seen, q = set(), {0}, deque([0])
        while q:
            x = q.popleft()
            for g in cov.gens:
                y = cov.P[g][x]
                if y not in seen:
                    seen.add(y)
                    tree.add(cov.edge(x, g))
                    q.append(y)
                for z in range(cov.d):
                    if cov.P[g][z] == x and z not in seen:
                        seen.add(z)
                        tree.add(cov.edge(z, g))
                        q.append(z)
        assert len(seen) == cov.d and len(tree) == cov.d - 1
        nontree = [e for e in range(2 * cov.d) if e not in tree]
        A = np.vstack([D1, Rr])[:, nontree]
        Fr, Tr = int_kernel(A), None
        Tr = split_torsion(Fr, A)
        self.F = np.zeros((Fr.shape[0], 2 * cov.d), dtype=np.int64)
        self.F[:, nontree] = Fr
        self.T = np.zeros((Tr.shape[0], 2 * cov.d), dtype=np.int64)
        self.T[:, nontree] = Tr
        self.D1, self.Rr, self.fc, self.tree = D1, Rr, fc, tree

    def chi_system(self, f):
        fc = self.fc
        cov, p = fc.cov, fc.p
        return {(x, g): np.array([[(-1) ** int(f[cov.edge(x, g)]) % p]], dtype=np.int64) for x in range(cov.d) for g in cov.gens}

    def nu(self, e):
        fc = self.fc
        cov, p = fc.cov, fc.p
        z8 = FL.F().root_of_order(p, 8)
        return {(x, g): pow(z8, int(e[cov.edge(x, g)]) % 8, p) for x in range(cov.d) for g in cov.gens}

    def values(self, e, loops, m):
        """the character's values on the based loops (exponents mod m), by walking the cover's edges"""
        cov = self.fc.cov
        out = []
        for w in loops:
            x, tot = 0, 0
            for c in w:
                g = c.lower()
                if c.islower():
                    tot += int(e[cov.edge(x, g)])
                    x = cov.P[g][x]
                else:
                    z = cov.P[c][x]
                    tot -= int(e[cov.edge(z, g)])
                    x = z
            assert x == 0
            out.append(tot % m)
        return tuple(out)

    def n_of(self, f):
        fc = self.fc
        return int(FL.F().Coh(fc.cov, self.chi_system(np.asarray(f) % 2), fc.p).n)

    def tau(self):
        """the deck group on the free lattice (columns are images of the F_i, modulo the vertex coboundaries)"""
        fc = self.fc
        Fm, p, cov = FL.F(), fc.p, fc.cov
        D0 = np.array(fc.CL.D0, dtype=np.int64) % p
        D0 = np.where(D0 > p // 2, D0 - p, D0)
        cols = []
        basis = sp.Matrix(np.hstack([self.F.T, D0]).tolist())
        for i in range(self.F.shape[0]):
            w = Fm.deck(self.F[i].reshape(-1), fc.tau, cov.d, 1)
            w = np.asarray(w, dtype=np.int64)
            assert not np.any(self.D1 @ w) and not np.any(self.Rr @ w)
            sol = basis.gauss_jordan_solve(sp.Matrix(w.tolist()))[0]
            cols.append([int(sol[j].subs({s: 0 for s in sol.free_symbols})) for j in range(self.F.shape[0])])
        return np.array(cols, dtype=np.int64).T


class FMember:
    """route F's frame at a member nu (values on the cover's edges)"""

    def __init__(self, fc, nuE):
        Fm = FL.F()
        self.Fm, self.fc, self.cov, self.p, self.mats = Fm, fc, fc.cov, fc.p, fc.mats
        p, cov = self.p, self.cov
        self.nuE = {k: int(v) for k, v in nuE.items()}
        self.Lv = {k: pow(v, (-4) % (p - 1), p) for k, v in self.nuE.items()}
        self.SV = {(x, g): (self.mats[g] * self.nuE[(x, g)]) % p for x in range(cov.d) for g in cov.gens}
        self.SC = {(x, g): (self.mats[g] * pow(self.nuE[(x, g)], 5, p)) % p for x in range(cov.d) for g in cov.gens}
        self.SL = {(x, g): np.array([[self.Lv[(x, g)]]], dtype=np.int64) for x in range(cov.d) for g in cov.gens}
        self.CC = Fm.Coh(cov, self.SC, p, keep=True)
        self.CL = Fm.Coh(cov, self.SL, p, keep=True)
        self.CV = Fm.Coh(cov, self.SV, p, keep=True)
        self.Q = Fm.nullspace(self.d1(self.SV).T % p, p).T % p
        self.Y = self.class_basis(self.CL.Z, self.CL.D0)
        self.Call = self.class_basis(self.CC.Z, self.CC.D0)
        I = self.interior()
        self.Cint = self.class_basis(I, self.CC.D0) if I.shape[1] else I
        self._K0 = None

    def d1(self, A):
        Fm, p, cov = self.Fm, self.p, self.cov
        e = next(iter(A.values())).shape[0]
        Ainv = {kk: Fm.minv(v, p) for kk, v in A.items()}
        D1 = np.zeros((e * cov.d, e * 2 * cov.d), dtype=np.int64)
        for x in range(cov.d):
            row, _ = Fm.Coh.path_row(cov, A, Ainv, cov.S.R, x, p)
            D1[x * e:(x + 1) * e, :] = row
        return D1

    def class_basis(self, Z, D0):
        """the columns of Z independent modulo span(D0), chosen left to right: the pivot columns of [D0 | Z] past D0's (one
        reduction; the same columns as adding them one at a time while the rank grows)"""
        Fm, p = self.Fm, self.p
        if Z.shape[1] == 0:
            return Z
        _, piv = Fm.rref(np.hstack([D0 % p, Z % p]), p)
        n0 = D0.shape[1]
        return Z[:, [c - n0 for c in piv if c >= n0]]

    def interior(self):
        Fm, p, C, cov = self.Fm, self.p, self.CC, self.cov
        Z, e, nc = C.Z, 4, len(cov.cusps)
        RZ = Fm.mm(C.R, Z, p)
        A = np.zeros((2 * e * nc, Z.shape[1] + e * nc), dtype=np.int64)
        for T in range(nc):
            A[2 * e * T:2 * e * (T + 1), :Z.shape[1]] = RZ[2 * e * T:2 * e * (T + 1)]
            A[2 * e * T:2 * e * (T + 1), Z.shape[1] + e * T:Z.shape[1] + e * (T + 1)] = \
                (-C.BP[2 * e * T:2 * e * (T + 1), e * T:e * (T + 1)]) % p
        K = Fm.nullspace(A, p)[:Z.shape[1]]
        return Fm.mm(Z, K, p)

    def w_system(self, c):
        p, cov = self.p, self.cov
        A = {}
        for x in range(cov.d):
            for gi, g in enumerate(cov.gens):
                W = np.zeros((5, 5), dtype=np.int64)
                W[:4, :4] = self.SV[(x, g)]
                W[:4, 4] = (np.asarray(c[(x * 2 + gi) * 4:(x * 2 + gi + 1) * 4], dtype=np.int64) * self.Lv[(x, g)]) % p
                W[4, 4] = self.Lv[(x, g)]
                A[(x, g)] = W % p
        return A

    def cup(self, c):
        Fm, p, d = self.Fm, self.p, self.cov.d
        D1W = self.d1(self.w_system(c))
        cols = []
        for j in range(self.Y.shape[1]):
            psi = np.zeros(5 * 2 * d, dtype=np.int64)
            psi[4::5] = self.Y[:, j]
            v = Fm.mm(D1W, psi.reshape(-1, 1), p).ravel()
            cols.append(np.concatenate([v[x * 5:x * 5 + 4] for x in range(d)]))
        if not cols:
            return np.zeros((self.Q.shape[0], 0), dtype=np.int64)
        return Fm.mm(self.Q, np.stack(cols, axis=1) % p, p)

    def cup_rank(self, c):
        M = self.cup(c)
        return int(self.Fm.rank(M, self.p)) if M.size else 0

    def K0(self):
        if self._K0 is None:
            Fm, p = self.Fm, self.p
            if self.Call.shape[1] == 0 or self.Y.shape[1] == 0:
                self._K0 = self.Call
            else:
                T = np.hstack([self.cup(self.Call[:, i]).reshape(-1, 1) for i in range(self.Call.shape[1])]) % p
                N = Fm.nullspace(T, p)
                self._K0 = Fm.mm(self.Call, N, p) if N.shape[1] else self.Call[:, :0]
        return self._K0

    def dim_mod(self, M):
        if M.shape[1] == 0:
            return 0
        Fm, p = self.Fm, self.p
        D0 = self.CC.D0
        return int(Fm.rank(np.hstack([D0, M % p]), p) - Fm.rank(D0, p))

    def k0_interior(self):
        Fm, p = self.Fm, self.p
        K = self.K0()
        if K.shape[1] == 0 or self.Cint.shape[1] == 0:
            return K[:, :0]
        A = np.hstack([K, (-self.Cint) % p, self.CC.D0]) % p
        N = Fm.nullspace(A, p)
        if N.shape[1] == 0:
            return K[:, :0]
        return self.class_basis(Fm.mm(K, N[:K.shape[1]], p), self.CC.D0)

    def labels(self):
        return [min(T["orbit"]) for T in self.cov.cusps]

    def vanishing(self, idx):
        """the cocycles (columns) whose restriction to each cusp of idx (positions in the cusp list) is a coboundary there"""
        Fm, p, C = self.Fm, self.p, self.CC
        Z, e = C.Z, 4
        nz = Z.shape[1]
        if not idx:
            return Z % p
        RZ = Fm.mm(C.R, Z, p)
        A = np.zeros((2 * e * len(idx), nz + e * len(idx)), dtype=np.int64)
        for j, T in enumerate(idx):
            A[2 * e * j:2 * e * (j + 1), :nz] = RZ[2 * e * T:2 * e * (T + 1)]
            A[2 * e * j:2 * e * (j + 1), nz + e * j:nz + e * (j + 1)] = \
                (-C.BP[2 * e * T:2 * e * (T + 1), e * T:e * (T + 1)]) % p
        K = Fm.nullspace(A, p)[:nz]
        return Fm.mm(Z, K, p)

    def stratum(self, U):
        """X_U: a basis (columns, modulo coboundaries) of K0^nu's classes that vanish on every cusp outside U (cusp labels)"""
        Fm, p = self.Fm, self.p
        idx = [i for i, lab in enumerate(self.labels()) if lab not in U]
        K = self.K0()
        Vb = self.vanishing(idx)
        Vb = self.class_basis(Vb, self.CC.D0) if Vb.shape[1] else Vb
        if K.shape[1] == 0 or Vb.shape[1] == 0:
            return K[:, :0]
        A = np.hstack([K, (-Vb) % p, self.CC.D0]) % p
        N = Fm.nullspace(A, p)
        if N.shape[1] == 0:
            return K[:, :0]
        return self.class_basis(Fm.mm(K, N[:K.shape[1]], p), self.CC.D0)

    def structure(self):
        k0 = self.K0()
        k0i = self.k0_interior()
        return {"h1(nu^5 rho)": int(self.CC.h1), "n(nu^5 rho)": int(self.CC.n), "h1(L)": int(self.CL.h1), "n(L)": int(self.CL.n),
                "dim K0": self.dim_mod(k0), "dim K0 interior": self.dim_mod(k0i)}

    def draw(self, B, rng):
        Fm, p = self.Fm, self.p
        a = np.array([[rng.randrange(1, p)] for _ in range(B.shape[1])], dtype=np.int64)
        return Fm.mm(B, a, p).ravel() % p

    def support(self, c):
        Fm, p, C, e = self.Fm, self.p, self.CC, 4
        rcv = Fm.mm(C.R, c.reshape(-1, 1) % p, p)
        labels = [min(T["orbit"]) for T in self.cov.cusps]
        out = []
        for i, lab in enumerate(labels):
            BPi = C.BP[2 * e * i:2 * e * (i + 1), e * i:e * (i + 1)]
            if Fm.rank(np.hstack([BPi, rcv[2 * e * i:2 * e * (i + 1)]]), p) > Fm.rank(BPi, p):
                out.append(lab)
        return sorted(out)

    def reading(self, c):
        """route_f.count's body at the member's frame: the supplies n of W, W*, L2W, L2W* and the count"""
        Fm, p, cov = self.Fm, self.p, self.cov
        A = self.w_system(c)
        As = {k: Fm.minv(v, p).T.copy() for k, v in A.items()}
        L2 = {k: Fm.wedge2(v, p) for k, v in A.items()}
        L2s = {k: Fm.wedge2(v, p) for k, v in As.items()}
        n = {nm: int(Fm.Coh(cov, sys_, p).n) for nm, sys_ in (("W", A), ("W*", As), ("L2", L2), ("L2*", L2s))}
        return {"count": [n["W"] - n["W*"], n["L2"] - n["L2*"]], "n": n, "rk delta1_W": self.cup_rank(c),
                "support": self.support(c)}
