"""B1546 -- the library: N45's cup map in the deck grading, its low-rank interior classes, in two routes.

The deck group tau (order 5) grades both sides: H^1(N; C) = sum_m E_m and H^1(N; rho) = sum_j V_j over tau's eigenvalues
zeta^m, zeta^j, and the cup product c_j u y_m lands in the zeta^(j+m) part of H^2(N; rho).  For c in V_j the cup map is the
sum of its blocks B_jm(c) = c u . on E_m.

Proposition L (PREREGISTRATION.md section 3; prop_l.py checks it in each route): every interior class of cup rank <= 2 lies
in the 10-dimensional space Kc0 = V_0^int + sum_(j != 0) (K_0 cap K_-j)^int, where K_m = {c : c u E_m = 0}, and on Kc0 the
cup map is a symmetric 4 x 4 matrix S(c) in disguise (rank delta1_W(c) = rank S(c)).  So the rank-1 interior classes are the
squares S(c) = l l^T, found here by solving delta1_W(c) = v (x) phi for a vector v of the cup map's 4-dimensional image.

  route F: sm:B1544's floor_lib.FCover (route_f, numpy; columns are cocycles); the line's eigen-parts by route_f.project.
  route R: sm:B1544's floor_lib.RCover (route_r on N45's own presentation; rows are cocycles); the line's eigen-parts by
           sm:B1541's deck_R_matrix on the trivial line (e = 1).
The two routes share no code beyond the cover's permutation data; each computes its own eigen-parts, spaces and classes."""
import importlib.util
import itertools
import sys
from pathlib import Path

import numpy as np

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


FL = _load("b1546_floor_lib", FLP)


class Graded:
    """one route's graded cup map on N45: line eigen-parts E[m], four eigen-parts V[j], the block maps, strata, interior"""

    def __init__(self, Cv):
        self.Cv = Cv
        self.F = isinstance(Cv, FL.FCover)
        self.p, self.k = Cv.p, Cv.k
        self.E = {m: self._line_eig(m) for m in range(self.k)}
        self.V = {j: self._cls(Cv.eig(Cv.Call if self.F else Cv.Cs, j)) for j in range(self.k)}
        self.K0 = Cv.K0()

    # ---------------------------------------------------------------- basics in each route's orientation
    def _cls(self, B):
        """a basis of span(B) modulo the four's coboundaries, in the route's orientation"""
        Cv = self.Cv
        if self.F:
            return Cv.class_basis(B % self.p, Cv.CV.D0) if B.shape[1] else B
        return Cv.class_basis(B % self.p, Cv.BV) if B.shape[0] else B

    def _line_eig(self, m):
        Cv, p, k = self.Cv, self.p, self.k
        if self.F:
            Fm = FL.F()
            Y = Cv.Y
            P = np.stack([Fm.project(Y[:, i], Cv.tau, Cv.cov.d, 1, m, k, Cv.zk, p) for i in range(Y.shape[1])], axis=1) % p
            return Cv.class_basis(P, Cv.CL.D0)
        R = Cv.R
        if not hasattr(self, "_TL"):
            N45L = FL.N45L()
            one = {g: np.eye(1, dtype=np.int64) for g in Cv.rho}
            self._TL = N45L.deck_R_matrix(Cv.cov, one, Cv.tau, p, e=1)
            self._BL = np.concatenate([((Cv.Lm.M[j] - np.eye(1, dtype=np.int64)) % p)[:, 0] for j in range(Cv.ng)]).reshape(1, -1) % p
        Yr = Cv.Ys
        out = np.zeros_like(Yr)
        cur = Yr.T % p
        for i in range(k):
            out = (out + pow(Cv.zk, (-m * i) % k, p) * cur.T) % p
            cur = R.mm(self._TL, cur, p)
        P = out * pow(k, -1, p) % p
        keep, curm = [], self._BL % p
        r = R.prank(curm, p)
        for i in range(P.shape[0]):
            cand = np.vstack([curm, P[i:i + 1]])
            rc = R.prank(cand, p)
            if rc > r:
                curm, r = cand, rc
                keep.append(i)
        return P[keep]

    def n(self, B):
        """number of classes in B (route orientation)"""
        return B.shape[1] if self.F else B.shape[0]

    def col(self, B, i):
        return B[:, i] if self.F else B[i]

    def combine(self, B, a):
        """the class sum_i a_i B_i"""
        p = self.p
        a = np.asarray(a, dtype=np.int64).reshape(-1, 1)
        if self.F:
            return FL.F().mm(B, a, p).ravel()
        return self.Cv.R.mm(a.T, B, p).ravel()

    def cupmat(self, c, Ylines):
        """the matrix of y -> c u y on the line classes Ylines (route orientation), in H^2(rho)'s dual coordinates"""
        Cv, p = self.Cv, self.p
        if self.F:
            Fm = FL.F()
            D1W = Cv.d1(Cv.w_system(c))
            d = Cv.cov.d
            cols = []
            for jj in range(Ylines.shape[1]):
                psi = np.zeros(5 * 2 * d, dtype=np.int64)
                psi[4::5] = Ylines[:, jj]
                v = Fm.mm(D1W, psi.reshape(-1, 1), p).ravel()
                cols.append(np.concatenate([v[x * 5:x * 5 + 4] for x in range(d)]))
            return Fm.mm(Cv.Q, np.stack(cols, axis=1) % p, p)
        R = Cv.R
        E = Cv.w_module(c)
        FW = np.vstack([R.fox(E, r, Cv.ng) for r in Cv.cov.rels]) % p
        cols = []
        for y in Ylines:
            psi = np.zeros(5 * Cv.ng, dtype=np.int64)
            psi[4::5] = y
            v = R.mm(FW, psi.reshape(-1, 1), p).ravel()
            cols.append(np.concatenate([v[kk * 5:kk * 5 + 4] for kk in range(len(Cv.cov.rels))]))
        return R.mm(Cv.Q, np.stack(cols, axis=1) % p, p)

    def rank(self, M):
        return int(FL.F().rank(M, self.p)) if self.F else int(self.Cv.R.prank(M, self.p))

    def Yall(self):
        if self.F:
            return np.hstack([self.E[m] for m in range(self.k)])
        return np.vstack([self.E[m] for m in range(self.k)])

    def cup_rank(self, c):
        return self.rank(self.cupmat(c, self.Yall()))

    def nullspace_coeffs(self, A):
        """coefficient vectors a (columns) with A a = 0"""
        p = self.p
        if self.F:
            return FL.F().nullspace(A % p, p)
        N = self.Cv.R.pnull(A % p, p, A.shape[1])
        return N.T if N.shape[0] else np.zeros((A.shape[1], 0), dtype=np.int64)

    def stratum(self, j, S):
        """L_jS: classes c in V_j with c u E_m = 0 for every m outside S (route orientation)"""
        V = self.V[j]
        nv = self.n(V)
        rows = []
        for m in range(self.k):
            if m in S or self.n(self.E[m]) == 0:
                continue
            rows.append(np.hstack([self.cupmat(self.col(V, i), self.E[m]).reshape(-1, 1) for i in range(nv)]))
        A = np.vstack(rows) % self.p if rows else np.zeros((0, nv), dtype=np.int64)
        N = self.nullspace_coeffs(A) if A.shape[0] else np.eye(nv, dtype=np.int64)
        if N.shape[1] == 0:
            return V[:, :0] if self.F else V[:0]
        if self.F:
            return FL.F().mm(V, N, self.p)
        return self.Cv.R.mm(N.T, V, self.p)

    def dim_mod(self, B):
        return self.Cv.dim_mod(B) if self.n(B) else 0

    def stack(self, *Bs):
        return np.hstack(Bs) if self.F else np.vstack(Bs)

    def meet(self, X, Y):
        return self.dim_mod(X) + self.dim_mod(Y) - self.dim_mod(self.stack(X, Y))

    def intersect(self, X, Y):
        """a spanning set of span(X) ∩ span(Y) modulo coboundaries (route orientation)"""
        p = self.p
        if self.F:
            D0 = self.Cv.CV.D0
            A = np.hstack([X, (-Y) % p, D0]) % p
            N = FL.F().nullspace(A, p)
            return FL.F().mm(X, N[:X.shape[1]], p) if N.shape[1] else X[:, :0]
        R, BV = self.Cv.R, self.Cv.BV
        A = np.vstack([X, (-Y) % p, BV]) % p                      # rows; we want row combinations: left null
        N = R.pnull(A.T % p, p, A.shape[0])
        if N.shape[0] == 0:
            return X[:0]
        return R.mm(N[:, :X.shape[0]], X, p)

    def interior_line(self, L):
        """L ∩ (the interior classes)"""
        return self.intersect(L, self.Cv.Cint)


    # ---------------------------------------------------------------- Proposition L's spaces and the low-rank classes
    COLS = {0: [0], 1: [1, 2], 2: [3, 4], 3: [5, 6], 4: [7, 8]}       # the line classes' columns of Yall, by eigenvalue

    def reduce(self, B):
        """a basis of span(B) modulo the four's coboundaries (route orientation)"""
        Cv, p = self.Cv, self.p
        if self.n(B) == 0:
            return B
        if self.F:
            return Cv.class_basis(B % p, Cv.CV.D0)
        return Cv.class_basis(B % p, Cv.BV)

    def vint(self, j):
        """V_j's interior part"""
        if not hasattr(self, "_vint"):
            self._vint = {}
        if j not in self._vint:
            self._vint[j] = self.reduce(self.interior_line(self.V[j]))
        return self._vint[j]

    def zero_on(self, B, ms):
        """the classes c of span(B) with c u E_m = 0 for every m in ms (route orientation)"""
        nb = self.n(B)
        rows = [np.hstack([self.cupmat(self.col(B, i), self.E[m]).reshape(-1, 1) for i in range(nb)]) for m in ms]
        if not rows:
            return B
        A = np.vstack(rows) % self.p
        N = self.nullspace_coeffs(A)
        if N.shape[1] == 0:
            return B[:, :0] if self.F else B[:0]
        if self.F:
            return FL.F().mm(B, N, self.p)
        return self.Cv.R.mm(N.T, B, self.p)

    def named(self):
        """the ten eigen-lines of Kc0: u_j (c u E_m = 0 for m != 2j), w_j (m in {0, -j, 2j}), v_a (m in {2, 3}), v_b (m in
        {1, 4}); each a 1-class basis (route orientation)"""
        if not hasattr(self, "_named"):
            out = {}
            for j in range(1, 5):
                out[f"u{j}"] = self.zero_on(self.vint(j), [m for m in range(5) if m != (2 * j) % 5])
                out[f"w{j}"] = self.zero_on(self.vint(j), sorted({0, (-j) % 5, (2 * j) % 5}))
            out["va"] = self.zero_on(self.vint(0), [2, 3])
            out["vb"] = self.zero_on(self.vint(0), [1, 4])
            self._named = out
        return self._named

    def kappa0(self):
        """Kc0's basis (route orientation): v_a, v_b, u_1, w_1, ..., u_4, w_4"""
        nm = self.named()
        return self.stack(*[nm[x] for x in ["va", "vb"] + [f"{a}{j}" for j in range(1, 5) for a in "uw"]])

    def mats(self, B):
        """the cup matrices M(b) = c u Yall (H^2 coordinates x 9) of the basis classes b of B"""
        Y = self.Yall()
        return [self.cupmat(self.col(B, i), Y) % self.p for i in range(self.n(B))]

    def image4(self):
        """a column basis of the cup map's image on Kc0 (sealed: dimension 4)"""
        if not hasattr(self, "_img"):
            Ms = self.mats(self.kappa0())
            A = np.hstack(Ms) % self.p
            self._img = _colbasis(A, self.p)
            self._Mk = Ms
        return self._img

    def rank1(self, v):
        """the rank-1 class c of Kc0 with delta1_W(c) = v (x) phi for some phi (unique up to scale; asserted)"""
        p = self.p
        self.image4()
        Ms = self._Mk
        h, ny = Ms[0].shape
        nk = len(Ms)
        A = np.zeros((h * ny, nk + ny), dtype=np.int64)
        for i, Mi in enumerate(Ms):
            A[:, i] = Mi.reshape(-1)
        for y in range(ny):
            A[np.arange(h) * ny + y, nk + y] = (-np.asarray(v, dtype=np.int64)) % p
        N = _null(A % p, p)
        assert N.shape[1] == 1, ("rank-1 solution space", N.shape[1])
        return self.combine(self.kappa0(), N[:nk, 0])

    def line_interior(self):
        """the line's interior classes (route orientation): restriction to every cusp a cusp coboundary (Lemma M's input)"""
        Cv, p = self.Cv, self.p
        C = Cv.CL
        nc = len(Cv.cov.cusps) if self.F else len(Cv.cov.cusp_list)
        Z = C.Z if self.F else C.Zrows.T
        if self.F:
            RZ = FL.F().mm(C.R, Z, p)
        else:
            RZ = Cv.R.mm(C.R, Z, p)
        A = np.zeros((2 * nc, Z.shape[1] + nc), dtype=np.int64)
        for T in range(nc):
            A[2 * T:2 * T + 2, :Z.shape[1]] = RZ[2 * T:2 * T + 2]
            A[2 * T:2 * T + 2, Z.shape[1] + T:Z.shape[1] + T + 1] = (-C.BP[2 * T:2 * T + 2, T:T + 1]) % p
        K = _null(A % p, p)[:Z.shape[1]]
        if self.F:
            return Cv.class_basis(FL.F().mm(Z, K, p), Cv.CL.D0)
        X = Cv.R.mm(K.T, C.Zrows, p)
        BL = np.concatenate([((Cv.Lm.M[j] - np.eye(1, dtype=np.int64)) % p)[:, 0] for j in range(Cv.ng)]).reshape(1, -1) % p
        return Cv.class_basis(X, BL)

    def draw_v(self, rng):
        I4 = self.image4()
        a = np.array([[rng.randrange(1, self.p)] for _ in range(I4.shape[1])], dtype=object)
        return (np.array(I4, dtype=object).dot(a) % self.p).astype(np.int64).ravel()


def low_rank_strata(G):
    """the strata L_jS (|S| <= 2) of dimension above K0's part, with their interior parts: the rank-1 lines (twisted j) and the
    rank-2 lines (j = 0).  Returns {j: [(S, L, Lint)]}, the least S for each distinct stratum."""
    out = {}
    for j in range(G.k):
        K0j = G.Cv.eig(G.K0, j)
        k0 = G.dim_mod(K0j)
        seen = []
        for r in range(0, 3):
            for S in itertools.combinations(range(G.k), r):
                L = G.stratum(j, S)
                if G.dim_mod(L) <= k0:
                    continue
                if any(G.dim_mod(L) == G.dim_mod(L2) == G.meet(L, L2) for _, L2, _ in seen):
                    continue
                seen.append((list(S), L, G.interior_line(L)))
        out[j] = seen
    return out


def _null(A, p):
    """the nullspace (columns) of A mod p, exact (python integers)"""
    A = [[int(x) % p for x in r] for r in A]
    rows = len(A)
    cols = len(A[0]) if rows else 0
    piv, r = [], 0
    for c in range(cols):
        pr = next((i for i in range(r, rows) if A[i][c]), None)
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        inv = pow(A[r][c], p - 2, p)
        A[r] = [(x * inv) % p for x in A[r]]
        for i in range(rows):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [(x - f * y) % p for x, y in zip(A[i], A[r])]
        piv.append(c)
        r += 1
    free = [c for c in range(cols) if c not in piv]
    N = np.zeros((cols, len(free)), dtype=np.int64)
    for k, fcol in enumerate(free):
        N[fcol, k] = 1
        for i, c in enumerate(piv):
            N[c, k] = (-A[i][fcol]) % p
    return N


def _rank(A, p):
    A = np.asarray(A)
    if A.size == 0:
        return 0
    return A.shape[1] - _null(A, p).shape[1]


def _colbasis(A, p):
    """a basis of A's column space, chosen among its columns"""
    keep, cur = [], np.zeros((A.shape[0], 0), dtype=np.int64)
    r = 0
    for i in range(A.shape[1]):
        cand = np.hstack([cur, A[:, i:i + 1] % p])
        rc = _rank(cand, p)
        if rc > r:
            cur, r = cand, rc
            keep.append(i)
    return A[:, keep] % p
