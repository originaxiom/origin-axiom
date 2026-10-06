"""B1544 -- the library: the cup map's kernel K0 and readings at its classes, in two routes.

The cup map of sm:B1515's frame at a class c of H^1(N; rho) (trivial character) is delta1_W(c): H^1(N; C) -> H^2(N; rho),
y -> c u y, the connecting map of 0 -> V -> W1(c) -> L -> 0.  It is linear in c.  K0 is its kernel: the classes c with
c u y = 0 in H^2(N; rho) for every y.  sm:B1543's floor I(W) >= -b0 reads, at such a class, as
    I(W) = -1 + k - rk d1(W*):
the cup map gives the count nothing, and the floor needs the dual term to give nothing either.

The cochain formula (both routes): lift a line cocycle y to the W-cochain (0, y) and apply W's coboundary; the V-part is a
2-cochain representing c u y, read modulo the image of V's coboundary.  The W-coboundary's (V, L) block is linear in c.
Checked against the long exact sequence's rank, h1(V) + h1(L) - h1(W) - 1, in controls.py (K2).

  route F: sm:B1541's route_f.py (numpy and the standard library only) on the lifted 2-complex of <a, t | ttATAAATA>, at a
           prime p = 1 mod 120 in (2^25, 2^26).  A class is a 1-cocycle of the base-gauge four (edge-major).
  route R: sm:B1536's route_r.py on the cover's own Reidemeister-Schreier presentation (through sm:B1542's ncyc.py and
           sm:B1541's n45.py, loaded by path), at its prime near 2^31.  A class is a list of values on the Schreier generators.
The two routes share no code; each computes its own K0 and its own eigenspaces (the deck group tau of the cyclic cover).

The cusps: both routes read a cusp as an orbit of the base cusp group <l, t'> on the cover's points, and the orbits coincide as
point sets (control K5), so a cusp is labelled by the least point of its orbit in both.  K0(S), for a set S of cusp labels,
is the part of K0 whose restriction to every cusp outside S is a cusp coboundary; S is a closed support when K0(S) is non-zero
on every cusp of S.  A reading records the class's support (the cusps where it is not a coboundary) and Lemma F's ingredients:
h^0(dN; W*), the rank r1(W) of H^1(N; W)'s restriction to the boundary, and h^1(dN; W)."""
import importlib.util
import itertools
import json
import sys
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1541V = ROOT / "frontier" / "B1541_the_count_on_the_room" / "verification"
B1542V = ROOT / "frontier" / "B1542_the_count_at_the_eisenstein_order" / "verification"
COVERS = ("N45", "d10.13", "d10.16", "d10.36", "d10.40")
PSI = ((Fr(0), Fr(0)), Fr(1, 6))


def _load(alias, path):
    if alias not in sys.modules:
        spec = importlib.util.spec_from_file_location(alias, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[alias] = mod
        spec.loader.exec_module(mod)
    return sys.modules[alias]


# ============================================================================================ route F
def F():
    return _load("b1544_route_f", B1541V / "route_f.py")


def f_inputs():
    """cover -> (state data, perms, tau, k)"""
    n45 = json.loads((B1541V / "route_f_input_n45.json").read_text())
    d60 = json.loads((B1542V / "route_f_input_degree60.json").read_text())
    st60 = {k: d60[k] for k in ("gens", "rels", "cusp", "holonomy")}
    out = {"N45": (n45, n45["perms"], n45["tau"], n45["k"])}
    for cid, cd in d60["covers"].items():
        out[cid] = (st60, cd["perms"], cd["tau"], d60["k"])
    return out


class FCover:
    """route F on one cover at one prime: the four's and the line's cohomology, the cup map, K0 and its eigen-parts"""

    def __init__(self, cid, p):
        Fm = F()
        sd, perms, tau, k = f_inputs()[cid]
        self.cid, self.p, self.tau, self.k = cid, p, tau, k
        self.S = Fm.State(sd)
        self.cov = Fm.Cover(self.S, perms)
        self.mats = self.S.four(p, Fm.root_of_order(p, 24))
        assert all(self.S.checks(self.mats, p).values())
        one = {g: np.eye(1, dtype=np.int64) for g in "abt"}
        self.CV = Fm.Coh(self.cov, Fm.base_system(self.cov, self.mats), p, keep=True)
        self.CL = Fm.Coh(self.cov, Fm.base_system(self.cov, one), p, keep=True)
        self.D1V = self.d1(Fm.base_system(self.cov, self.mats))
        self.Q = Fm.nullspace(self.D1V.T % p, p).T % p            # functionals on C^2(V) killing V's coboundaries
        self.Y = self.class_basis(self.CL.Z, self.CL.D0)
        self.Call = self.class_basis(self.CV.Z, self.CV.D0)
        self.Cint = self.class_basis(self.interior(), self.CV.D0)
        self.zk = Fm.root_of_order(p, k)
        self._K0 = None

    def d1(self, A):
        Fm, p, cov = F(), self.p, self.cov
        e = next(iter(A.values())).shape[0]
        Ainv = {kk: Fm.minv(v, p) for kk, v in A.items()}
        D1 = np.zeros((e * cov.d, e * 2 * cov.d), dtype=np.int64)
        for x in range(cov.d):
            row, _ = Fm.Coh.path_row(cov, A, Ainv, cov.S.R, x, p)
            D1[x * e:(x + 1) * e, :] = row
        return D1

    def class_basis(self, Z, D0):
        Fm, p = F(), self.p
        cols, cur = [], D0 % p
        r = Fm.rank(cur, p)
        for i in range(Z.shape[1]):
            cand = np.hstack([cur, Z[:, i:i + 1]])
            rc = Fm.rank(cand, p)
            if rc > r:
                cur, r = cand, rc
                cols.append(i)
        return Z[:, cols]

    def interior(self):
        Fm, p, C, cov = F(), self.p, self.CV, self.cov
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
                W[:4, :4] = self.mats[g]
                W[:4, 4] = c[(x * 2 + gi) * 4:(x * 2 + gi + 1) * 4]
                W[4, 4] = 1
                A[(x, g)] = W % p
        return A

    def cup(self, c):
        """the matrix of delta1_W(c) in H^2(V)'s dual coordinates: Q (V-part of W's coboundary on (0, y)) for y in Y"""
        Fm, p, d = F(), self.p, self.cov.d
        D1W = self.d1(self.w_system(c))
        cols = []
        for j in range(self.Y.shape[1]):
            psi = np.zeros(5 * 2 * d, dtype=np.int64)
            psi[4::5] = self.Y[:, j]
            v = Fm.mm(D1W, psi.reshape(-1, 1), p).ravel()
            cols.append(np.concatenate([v[x * 5:x * 5 + 4] for x in range(d)]))
        return Fm.mm(self.Q, np.stack(cols, axis=1) % p, p)

    def rk_cup(self, c):
        return int(F().rank(self.cup(c), self.p))

    def rk_les(self, c):
        """h1(V) + h1(L) - h1(W) - 1 (route F's own cohomology of W1(c))"""
        Fm = F()
        return int(self.CV.h1 + self.CL.h1 - Fm.Coh(self.cov, self.w_system(c), self.p).h1 - 1)

    def K0(self):
        """cocycles (columns) spanning the cup map's kernel on H^1(N; rho)"""
        if self._K0 is None:
            Fm, p = F(), self.p
            T = np.hstack([self.cup(self.Call[:, i]).reshape(-1, 1) for i in range(self.Call.shape[1])]) % p
            self._K0 = Fm.mm(self.Call, Fm.nullspace(T, p), p)
        return self._K0

    def dim_mod(self, M):
        """the dimension of the span of the cocycles M modulo coboundaries"""
        Fm, p = F(), self.p
        if M.shape[1] == 0:
            return 0
        return int(Fm.rank(np.hstack([M, self.CV.D0]), p) - Fm.rank(self.CV.D0, p))

    def eig(self, B, j):
        """the projection of the cocycles B onto tau's eigenvalue zk^j"""
        Fm, p = F(), self.p
        if B.shape[1] == 0:
            return B
        return np.stack([Fm.project(B[:, i], self.tau, self.cov.d, 4, j, self.k, self.zk, p) for i in range(B.shape[1])],
                        axis=1)

    def subspace(self, name):
        """'K0', 'K0 j=<j>' or 'S=<labels>' (K0(S)): cocycles spanning it"""
        K0 = self.K0()
        if name == "K0":
            return K0
        if name.startswith("S="):
            return self.stratum(parse_s(name), K0)
        j = int(name.split("j=")[1])
        return self.eig(K0, j)

    def draw(self, B, rng):
        Fm, p = F(), self.p
        a = np.array([[rng.randrange(1, p)] for _ in range(B.shape[1])], dtype=np.int64)
        return Fm.mm(B, a, p).ravel()

    # ---- the cusps (labels), the strata of K0, the support of a class, Lemma F's ingredients
    @property
    def labels(self):
        return [min(T["orbit"]) for T in self.cov.cusps]

    def stratum(self, S, B):
        """the columns of span(B) whose restriction to every cusp with label outside S is a cusp coboundary"""
        Fm, p, C = F(), self.p, self.CV
        out = [i for i, lab in enumerate(self.labels) if lab not in S]
        if not out or B.shape[1] == 0:
            return B
        e = 4
        RB = Fm.mm(C.R, B, p)
        A = np.zeros((2 * e * len(out), B.shape[1] + e * len(out)), dtype=np.int64)
        for i, T in enumerate(out):
            A[2 * e * i:2 * e * (i + 1), :B.shape[1]] = RB[2 * e * T:2 * e * (T + 1)]
            A[2 * e * i:2 * e * (i + 1), B.shape[1] + e * i:B.shape[1] + e * (i + 1)] = \
                (-C.BP[2 * e * T:2 * e * (T + 1), e * T:e * (T + 1)]) % p
        K = Fm.nullspace(A, p)[:B.shape[1]]
        return Fm.mm(B, K, p) if K.shape[1] else B[:, :0]

    def support(self, c):
        """the labels of the cusps where the cocycle c does not restrict to a cusp coboundary"""
        Fm, p, C, e = F(), self.p, self.CV, 4
        rc = Fm.mm(C.R, c.reshape(-1, 1) % p, p)
        out = []
        for i, lab in enumerate(self.labels):
            BPi = C.BP[2 * e * i:2 * e * (i + 1), e * i:e * (i + 1)]
            if Fm.rank(np.hstack([BPi, rc[2 * e * i:2 * e * (i + 1)]]), p) > Fm.rank(BPi, p):
                out.append(lab)
        return sorted(out)

    def w_dual_system(self, c):
        Fm, p = F(), self.p
        return {kk: Fm.minv(v, p).T.copy() for kk, v in self.w_system(c).items()}

    def lemma_f(self, c):
        """h^0(dN; W*), h^0(dN; W), r1(W) and h^1(dN; W) = sum over the cusps of h^0(T; W) + h^0(T; W*) (route F's own Coh)"""
        Fm, p, e = F(), self.p, 5
        CW = Fm.Coh(self.cov, self.w_system(c), p, keep=True)
        CWs = Fm.Coh(self.cov, self.w_dual_system(c), p, keep=True)
        nc = len(self.cov.cusps)

        def h0s(Cc):
            return [e - Fm.rank(Cc.BP[2 * e * i:2 * e * (i + 1), e * i:e * (i + 1)], p) for i in range(nc)]
        hW, hWs = h0s(CW), h0s(CWs)
        return {"m": nc, "h0(dN;W*)": int(sum(hWs)), "h0(dN;W)": int(sum(hW)), "r1(W)": int(CW.r1),
                "h1(dN;W)": int(sum(hW) + sum(hWs))}

    def reading(self, c):
        Fm = F()
        cnt, n = Fm.count(self.cov, self.mats, c, self.p)
        return {"count": [int(x) for x in cnt], "rk delta1_W": self.rk_cup(c), "n": {k: int(v) for k, v in n.items()},
                "support": self.support(c), "lemma F": self.lemma_f(c)}


# ============================================================================================ route R
def NC():
    return _load("b1544_ncyc", B1542V / "ncyc.py")          # loads sm:B1536's route_r and allocates PARI's stack


def N45L():
    NC()
    return _load("b1544_n45", B1541V / "n45.py")


class RCover:
    """route R on one cover: the cover's own presentation at its prime, the cup map, K0 and its eigen-parts"""

    def __init__(self, cid):
        L = NC()
        R = L.R
        self.R = R
        if cid == "N45":
            st, perms, pts, tau = N45L().build()
            k = 5
        else:
            st, perms, pts, tau = L.build("m003", cid, PSI[0], PSI[1], 6)
            k = 6
        self.cid, self.tau, self.k = cid, tau, k
        G = st["G"]
        self.cov = R.PCover(G, perms)
        _, _, Nroot, _ = L.POP.characters(st, perms)
        p = L.GF.primes_1_mod(Nroot, 1 << 31, 1)[0]
        assert (p - 1) % k == 0
        self.p = p
        B = L.N.Base(st, L.GF.GF(p, Nroot))
        self.rho = {g: np.asarray(B.rho[g], dtype=np.int64) % p for g in G.gens}
        self.chi = B.character((Fr(0), Fr(0)), Fr(0))
        self.V = R.lift(self.cov, self.rho, p)
        self.Lm = R.lift(self.cov, {g: np.eye(1, dtype=np.int64) for g in G.gens}, p)
        self.CV = R.Coh(self.cov, self.V, keep=True)
        self.CL = R.Coh(self.cov, self.Lm, keep=True)
        self.ng = ng = len(self.cov.sgens)
        FV = np.vstack([R.fox(self.V, r, ng) for r in self.cov.rels]) % p
        self.Q = R.pnull(FV.T % p, p, FV.shape[0])
        self.BV = np.vstack([np.concatenate([((self.V.M[j] - np.eye(4, dtype=np.int64)) % p)[:, kk] for j in range(ng)])
                             for kk in range(4)]) % p
        BL = np.concatenate([((self.Lm.M[j] - np.eye(1, dtype=np.int64)) % p)[:, 0] for j in range(ng)]).reshape(1, -1) % p
        self.Ys = self.class_basis(self.CL.Zrows, BL)
        self.Cs = self.class_basis(self.CV.Zrows, self.BV)
        self.Cint = self.class_basis(self.interior(), self.BV)
        deck = L.deck_R_matrix if cid != "N45" else N45L().deck_R_matrix
        self.T = deck(self.cov, self.rho, tau, p)
        self.zk = self.root(k)
        self._K0 = None

    def root(self, k):
        p = self.p
        for a in range(2, p):
            z = pow(a, (p - 1) // k, p)
            if all(pow(z, k // q, p) != 1 for q in (2, 3, 5) if k % q == 0):
                return z
        raise ValueError(k)

    def class_basis(self, Zrows, B):
        R, p = self.R, self.p
        keep, cur = [], B % p
        r = R.prank(cur, p) if cur.shape[0] else 0
        for i in range(Zrows.shape[0]):
            cand = np.vstack([cur, Zrows[i:i + 1]]) if cur.shape[0] else Zrows[i:i + 1]
            rc = R.prank(cand, p)
            if rc > r:
                cur, r = cand, rc
                keep.append(i)
        return Zrows[keep]

    def interior(self):
        R, p, C, cov = self.R, self.p, self.CV, self.cov
        e, nc = 4, len(cov.cusps)
        RZ = R.mm(C.R, C.Zrows.T, p)
        A = np.zeros((2 * e * nc, C.Zrows.shape[0] + e * nc), dtype=np.int64)
        for T in range(nc):
            A[2 * e * T:2 * e * (T + 1), :C.Zrows.shape[0]] = RZ[2 * e * T:2 * e * (T + 1)]
            A[2 * e * T:2 * e * (T + 1), C.Zrows.shape[0] + e * T:C.Zrows.shape[0] + e * (T + 1)] = \
                (-C.BP[2 * e * T:2 * e * (T + 1), e * T:e * (T + 1)]) % p
        K = R.pnull(A, p, A.shape[1])[:, :C.Zrows.shape[0]]
        return R.mm(K, C.Zrows, p)

    def w_module(self, c):
        R, p = self.R, self.p
        Ws = []
        for j in range(self.ng):
            W = np.zeros((5, 5), dtype=np.int64)
            W[:4, :4] = self.V.M[j]
            W[:4, 4] = c[j * 4:(j + 1) * 4]
            W[4, 4] = 1
            Ws.append(W % p)
        return R.CMod(Ws, p)

    def cup(self, c):
        R, p, ng = self.R, self.p, self.ng
        E = self.w_module(c)
        FW = np.vstack([R.fox(E, r, ng) for r in self.cov.rels]) % p
        cols = []
        for y in self.Ys:
            psi = np.zeros(5 * ng, dtype=np.int64)
            psi[4::5] = y
            v = R.mm(FW, psi.reshape(-1, 1), p).ravel()
            cols.append(np.concatenate([v[kk * 5:kk * 5 + 4] for kk in range(len(self.cov.rels))]))
        return R.mm(self.Q, np.stack(cols, axis=1) % p, p)

    def rk_cup(self, c):
        return int(self.R.prank(self.cup(c), self.p))

    def rk_les(self, c):
        return int(self.CV.h1 + self.CL.h1 - self.R.Coh(self.cov, self.w_module(c)).h1 - 1)

    def K0(self):
        """rows spanning the cup map's kernel"""
        if self._K0 is None:
            R, p = self.R, self.p
            T = np.stack([self.cup(self.Cs[i]).reshape(-1) for i in range(self.Cs.shape[0])], axis=1) % p
            a = R.pnull(T, p, T.shape[1])
            self._K0 = R.mm(a, self.Cs, p) if a.shape[0] else np.zeros((0, self.Cs.shape[1]), dtype=np.int64)
        return self._K0

    def dim_mod(self, M):
        R, p = self.R, self.p
        if M.shape[0] == 0:
            return 0
        return int(R.prank(np.vstack([M, self.BV]), p) - R.prank(self.BV, p))

    def eig(self, Brows, j):
        """rows projected onto the deck action's eigenvalue zk^j: (1/k) sum_i zk^(-j i) T^i"""
        R, p, k = self.R, self.p, self.k
        if Brows.shape[0] == 0:
            return Brows
        out = np.zeros_like(Brows)
        cur = Brows.T % p
        for i in range(k):
            out = (out + pow(self.zk, (-j * i) % k, p) * cur.T) % p
            cur = R.mm(self.T, cur, p)
        return out * pow(k, -1, p) % p

    def subspace(self, name):
        K0 = self.K0()
        if name == "K0":
            return K0
        if name.startswith("S="):
            return self.stratum(parse_s(name), K0)
        return self.eig(K0, int(name.split("j=")[1]))

    def draw(self, Brows, rng):
        R, p = self.R, self.p
        a = np.array([[rng.randrange(1, p) for _ in range(Brows.shape[0])]], dtype=np.int64)
        return R.mm(a, Brows, p).ravel()

    # ---- the cusps (labels), the strata of K0, the support of a class, Lemma F's ingredients
    @property
    def labels(self):
        return [min(T["orbit"]) for T in self.cov.cusp_list]

    def stratum(self, S, Brows):
        """the rows of span(Brows) whose restriction to every cusp with label outside S is a cusp coboundary"""
        R, p, C = self.R, self.p, self.CV
        out = [i for i, lab in enumerate(self.labels) if lab not in S]
        if not out or Brows.shape[0] == 0:
            return Brows
        e = 4
        RB = R.mm(C.R, Brows.T, p)
        A = np.zeros((2 * e * len(out), Brows.shape[0] + e * len(out)), dtype=np.int64)
        for i, T in enumerate(out):
            A[2 * e * i:2 * e * (i + 1), :Brows.shape[0]] = RB[2 * e * T:2 * e * (T + 1)]
            A[2 * e * i:2 * e * (i + 1), Brows.shape[0] + e * i:Brows.shape[0] + e * (i + 1)] = \
                (-C.BP[2 * e * T:2 * e * (T + 1), e * T:e * (T + 1)]) % p
        K = R.pnull(A, p, A.shape[1])
        if K.shape[0] == 0:
            return Brows[:0]
        return R.mm(K[:, :Brows.shape[0]], Brows, p)

    def support(self, c):
        R, p, C, e = self.R, self.p, self.CV, 4
        rc = R.mm(C.R, c.reshape(-1, 1) % p, p)
        out = []
        for i, lab in enumerate(self.labels):
            BPi = C.BP[2 * e * i:2 * e * (i + 1), e * i:e * (i + 1)]
            if R.prank(np.hstack([BPi, rc[2 * e * i:2 * e * (i + 1)]]), p) > R.prank(BPi, p):
                out.append(lab)
        return sorted(out)

    def lemma_f(self, c):
        """h^0(dN; W*), h^0(dN; W), r1(W), h^1(dN; W) by sm:B1536's Coh on the frame's modules"""
        R, p = self.R, self.p
        c_vals = [list(int(x) for x in c[j * 4:(j + 1) * 4]) for j in range(self.ng)]
        mods = R.frame(self.cov, self.rho, self.chi, c_vals, p)
        CE, CEs = R.Coh(self.cov, mods["E"][0]), R.Coh(self.cov, mods["E*"][0])
        return {"m": len(self.cov.cusps), "h0(dN;W*)": int(CEs.t0), "h0(dN;W)": int(CE.t0), "r1(W)": int(CE.r1),
                "h1(dN;W)": int(CE.h1P)}

    def reading(self, c):
        R, p = self.R, self.p
        c_vals = [list(int(x) for x in c[j * 4:(j + 1) * 4]) for j in range(self.ng)]
        r = R.reading(self.cov, self.rho, self.chi, c_vals, p)
        out = {"count": [int(r["I(W)"]), int(r["I(L2W)"])], "rk delta1_W": self.rk_cup(c), "k": int(r["k"]), "b0": int(r["b0"]),
               "rk d1": {kk: int(v) for kk, v in r["rk d1"].items()}, "n(L)": int(r["n(L)"]), "n(V)": int(r["n(V)"]),
               "n((VL)*)": int(r["n((VL)*)"]), "all": bool(r["all"]),
               "failed": [kk for kk, v in r["checks"].items() if not v],
               "support": self.support(c), "lemma F": self.lemma_f(c)}
        return out


def parse_s(name):
    """'S=0,1,3' -> {0, 1, 3}; 'S=' -> the empty set"""
    body = name.split("S=", 1)[1]
    return {int(x) for x in body.split(",") if x != ""}


def s_name(S):
    return "S=" + ",".join(str(x) for x in sorted(S))


def closed_supports(Cv):
    """[(S, dim K0(S))] for every closed support S of K0 (K0(S) non-zero on every cusp of S), and dim K0(S) for every S"""
    lab = sorted(Cv.labels)
    K0 = Cv.K0()
    dims = {}
    for r in range(len(lab) + 1):
        for S in itertools.combinations(lab, r):
            dims[S] = Cv.dim_mod(Cv.stratum(set(S), K0))
    closed = []
    for S, d in dims.items():
        if d and all(dims[tuple(x for x in S if x != T)] < d for T in S):
            closed.append((S, d))
    return sorted(closed, key=lambda x: (len(x[0]), x[0])), dims


def tau_on_cusps(Cv):
    """the deck transformation's permutation of the cusps, by label: the orbit of x goes to the orbit of tau(x)"""
    orbits = [T["orbit"] for T in (Cv.cov.cusps if isinstance(Cv, FCover) else Cv.cov.cusp_list)]
    where = {x: min(o) for o in orbits for x in o}
    return {int(min(o)): int(where[Cv.tau[min(o)]]) for o in orbits}


def structure(Cv):
    """the structure both routes must agree on (control K1)"""
    k = Cv.k
    K0 = Cv.K0()
    is_f = isinstance(Cv, FCover)
    Cint = Cv.Cint
    if is_f:
        both = Cv.dim_mod(np.hstack([K0, Cint]))
    else:
        both = Cv.dim_mod(np.vstack([K0, Cint]))
    dK0, dint = Cv.dim_mod(K0), Cv.dim_mod(Cint)
    closed, _ = closed_supports(Cv)
    return {"h1(rho)": int(Cv.CV.h1), "n(rho)": int(Cv.CV.n), "h1(C)": int(Cv.CL.h1), "n(1)": int(Cv.CL.n),
            "dim K0": dK0, "K0 meets the interior in": dK0 + dint - both,
            "K0 by eigenspace": [Cv.dim_mod(Cv.eig(K0, j)) for j in range(k)],
            "cusp labels": sorted(int(x) for x in Cv.labels), "tau on the cusps": tau_on_cusps(Cv),
            "closed supports of K0 [S, dim K0(S)]": [[list(S), d] for S, d in closed]}
