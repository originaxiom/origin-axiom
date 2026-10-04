#!/usr/bin/env python3
"""B1536 -- route N: a finite cover read on the BASE, by Shapiro and Mackey (PREREGISTRATION Lemma S'), over GF(p) with FLINT's
nmod_mat for every rank and kernel.  It shares no linear algebra with route R (route_r.py: the cover's own Reidemeister-Schreier
presentation, numpy elimination written for this arc).  Nothing is computed on import.

THE INDUCED MODULES.  For a cover with right action x^g on X = {0..d-1} (cover_lib), every module this route reads on the base is
BLOCK-MONOMIAL: generator g acts by the matrix whose (x, x^g) block is a local matrix A_x(g) and every other block is 0.
  - E (x) P for a base module E: A_x(g) = E(g) for every x (P(g)_{x,y} = [x^g = y]).
  - Ind of the cover's frame at its own class c (Lemma O): with c_hat in Z^1(base; V L^-1 (x) P) the Shapiro preimage of c,
    A_x(g) = F(W_x(g)), W_x(g) = [[V(g), c_hat(g)_x L(g)], [0, L(g)]], for F = the identity or Lambda^2.  The product rule
    W_x(g) W_{x^g}(h) = W_x(gh) is exactly c_hat's cocycle condition, and c(h) = c_hat(h)_0 for h in H = Stab(0) (Shapiro).
  Products of block-monomial matrices stay block-monomial: (s, A)(t, B) = (x -> t(s(x)), A_x B_{s(x)}); the dual is
  (s, (A_x^-1)^T).  Fox blocks are sums of such terms and are assembled into one matrix only for the rank computations.

COHOMOLOGY on the base (one cusp <p1, p2>; Mackey makes it every cusp of the cover): Fox Jacobian -> Z^1; B^1; h^0; the restriction
to the cusp modulo B^1(P) -> r1; n = h^1 - r1; t0 = h^0(P); h^1(P).  class_index asserts B1297, the annihilator identity and
sm:B1527's Lemma E at every call, as sm:B1530's exact_lib does."""
import numpy as np
import flint

P_BOUND = 1 << 24      # route N's primes: residues < 2^24, so every int64 product sum below (inner dimension < 2^14) is exact

# ============================================================================================ small matrices mod p
def mmul(A, B, p):
    return (A @ B) % p


def minv(A, p):
    n = A.shape[0]
    M = flint.nmod_mat(n, n, [int(x) for x in A.ravel()], p)
    Mi = M.inv()
    return np.array([[int(Mi[i, j]) for j in range(n)] for i in range(n)], dtype=np.int64)


def pairs_order(n):
    """sub first: pairs (i, j) with j < n - 1 (Lambda^2 of the first n - 1 coordinates), then (i, n - 1)"""
    sub = [(i, j) for j in range(n - 1) for i in range(j)]
    quo = [(i, n - 1) for i in range(n - 1)]
    return sub, quo


def wedge2_pairs(A, pairs, p):
    """(Lambda^2 A) in the basis {e_i ^ e_j : (i, j) in pairs}: column (k, l) is A e_k ^ A e_l, coordinate (i, j) the 2x2 minor"""
    m = len(pairs)
    out = np.zeros((m, m), dtype=np.int64)
    for c, (k, l) in enumerate(pairs):
        u, v = A[:, k], A[:, l]
        for r, (i, j) in enumerate(pairs):
            out[r, c] = (u[i] * v[j] - u[j] * v[i]) % p
    return out


# ============================================================================================ block-monomial modules
class BM:
    """a block-monomial matrix mod p: perm (array, x -> s(x)) and local blocks A[x] (e x e)"""
    __slots__ = ("s", "A", "p")

    def __init__(self, s, A, p):
        self.s, self.A, self.p = s, A, p

    def __mul__(self, o):
        return BM(o.s[self.s], np.einsum("xij,xjk->xik", self.A, o.A[self.s]) % self.p, self.p)

    def dense(self, p):
        d, e = len(self.s), self.A.shape[1]
        out = np.zeros((d * e, d * e), dtype=np.int64)
        for x in range(d):
            y = self.s[x]
            out[x * e:(x + 1) * e, y * e:(y + 1) * e] = self.A[x]
        return out


class Module:
    """generators -> BM, with inverses; index (x, i) -> x * e + i (cover point major)"""

    def __init__(self, gens, bms, p):
        self.gens, self.p = list(gens), p
        self.M = dict(bms)
        any_ = self.M[self.gens[0]]
        self.d, self.e = len(any_.s), any_.A.shape[1]
        self.D = self.d * self.e
        self.Mi = {g: self._inv(self.M[g]) for g in self.gens}

    def _inv(self, m):
        p = self.p
        sinv = np.empty_like(m.s)
        sinv[m.s] = np.arange(len(m.s))
        Ainv = np.stack([minv(m.A[x], p) for x in range(len(m.s))])
        # (s, A)^-1 = (s^-1, B) with B_y = (A_{s^-1 y})^-1
        return BM(sinv, Ainv[sinv], p)

    def letter(self, c):
        return self.M[c] if c.islower() else self.Mi[c.lower()]

    def identity(self):
        return BM(np.arange(self.d), np.broadcast_to(np.eye(self.e, dtype=np.int64), (self.d, self.e, self.e)).copy(), self.p)

    def word(self, w):
        X = self.identity()
        for c in w:
            X = X * self.letter(c)
        return X

    def dual(self):
        p = self.p
        out = {}
        for g in self.gens:
            Mi = self.Mi[g]
            # (M^-1)^T: M^-1 = (s^-1, B); its transpose has block (s^-1(y), y) = B_y^T at row s^-1(y) ... i.e. (s, C) with
            # C_x = B_{s(x)}^T
            m = self.M[g]
            C = np.transpose(Mi.A[m.s], (0, 2, 1)).copy()
            out[g] = BM(m.s.copy(), C % p, p)
        return Module(self.gens, out, p)

    def block(self, idx):
        """the module on the coordinates idx of each local block (a sub- or quotient module)"""
        idx = np.array(idx)
        return Module(self.gens, {g: BM(self.M[g].s.copy(), self.M[g].A[:, idx][:, :, idx].copy(), self.p)
                                  for g in self.gens}, self.p)

    def check(self, rels):
        for r in rels:
            X = self.word(r)
            if not (np.array_equal(X.s, np.arange(self.d)) and
                    all(np.array_equal(X.A[x] % self.p, np.eye(self.e, dtype=np.int64)) for x in range(self.d))):
                return False
        return True


def fox_dense(mod, w):
    """z(w) = sum_g K_g z(g) (left cocycles): the dense D x (ngens * D) matrix [K_g]_g"""
    p, D, e = mod.p, mod.D, mod.e
    out = np.zeros((D, len(mod.gens) * D), dtype=np.int64)
    gi = {g: i for i, g in enumerate(mod.gens)}
    Pre = mod.identity()
    for c in w:
        g = c.lower()
        if c.islower():
            term, sign = Pre, 1
            Pre = Pre * mod.M[g]
        else:
            Pre = Pre * mod.Mi[g]
            term, sign = Pre, -1
        off = gi[g] * D
        for x in range(mod.d):
            y = term.s[x]
            out[x * e:(x + 1) * e, off + y * e:off + (y + 1) * e] += sign * term.A[x]
    return out % p


def fl(M, p):
    r, c = M.shape
    return flint.nmod_mat(r, c, [int(v) for v in M.ravel()], p)


def rank(M, p):
    if M.size == 0:
        return 0
    return fl(M % p, p).rank()


def kernel(M, p):
    """a basis of {v : M v = 0} as the columns of a numpy array"""
    r, c = M.shape
    if r == 0:
        return np.eye(c, dtype=np.int64)
    X, nul = fl(M % p, p).nullspace()
    if nul == 0:
        return np.zeros((c, 0), dtype=np.int64)
    return np.array([[int(X[i, j]) for j in range(nul)] for i in range(c)], dtype=np.int64)


# ============================================================================================ cohomology
class Cohomology:
    def __init__(self, G, mod, keep=False):
        p, D, ng = mod.p, mod.D, len(mod.gens)
        assert list(G.gens) == mod.gens
        F = np.vstack([fox_dense(mod, r) for r in G.rels]) if G.rels else np.zeros((0, ng * D), dtype=np.int64)
        for r in G.rels:
            X = mod.word(r)
            assert np.array_equal(X.s, np.arange(mod.d)) and all(
                np.array_equal(X.A[x], np.eye(mod.e, dtype=np.int64)) for x in range(mod.d)), "a relator is not 1"
        self.dimZ = ng * D - rank(F, p)
        Dg = [mod.M[g].dense(p) - np.eye(D, dtype=np.int64) for g in mod.gens]
        self.a0 = D - rank(np.vstack(Dg), p)
        self.dimB = D - self.a0
        self.h1 = self.dimZ - self.dimB
        P1, P2 = mod.word(G.cusp[0]).dense(p), mod.word(G.cusp[1]).dense(p)
        BP = np.vstack([P1 - np.eye(D, dtype=np.int64), P2 - np.eye(D, dtype=np.int64)]) % p
        self.rBP = rank(BP, p)
        self.t0 = D - self.rBP
        eq = np.hstack([-(P2 - np.eye(D, dtype=np.int64)), P1 - np.eye(D, dtype=np.int64)]) % p
        self.h1P = (2 * D - rank(eq, p)) - self.rBP
        R = np.vstack([fox_dense(mod, G.cusp[0]), fox_dense(mod, G.cusp[1])])
        Zb = kernel(F, p)
        assert Zb.shape[1] == self.dimZ
        RZ = (R @ Zb) % p if Zb.shape[1] else np.zeros((2 * D, 0), dtype=np.int64)
        self.r1 = rank(np.hstack([BP, RZ]), p) - self.rBP
        self.n = self.h1 - self.r1
        if keep:
            self.F, self.Zb, self.Dg, self.R, self.BP = F, Zb, Dg, R, BP


def class_index(G, mod):
    A, B = Cohomology(G, mod), Cohomology(G, mod.dual())
    I = A.n - B.n
    a0, b0, t0, s0 = A.a0, B.a0, A.t0, B.t0
    checks = {
        "B1297 I = (a0 - b0) + s0 - r1": I == (a0 - b0) + s0 - A.r1,
        "annihilator r1 + r1* = t0 + s0 = h1(P)": A.r1 + B.r1 == t0 + s0 == A.h1P == B.h1P,
        "Lemma E I = h1* - h1 + 2(a0 - b0) + s0 - t0": I == B.h1 - A.h1 + 2 * (a0 - b0) + s0 - t0,
    }
    assert all(checks.values()), (checks, (a0, b0, t0, s0, A.h1, B.h1, A.r1, B.r1, A.h1P))
    return {"I": I, "a0": a0, "b0": b0, "t0": t0, "s0": s0, "h1": A.h1, "h1*": B.h1, "r1": A.r1, "r1*": B.r1,
            "n": A.n, "n*": B.n}


# ============================================================================================ the base, its characters and modules
class Base:
    """a state's group and the four mod p (from sm:B1530's exact holonomy, cover_lib.state)"""

    def __init__(self, st, F):
        self.st, self.F, self.p = st, F, F.p
        self.G, self.sign = st["G"], st["sign"]
        self.gens = list(self.G.gens)
        self.rho = {g: np.array([[F.K(x) for x in row] for row in st["rho"].M[g]], dtype=np.int64) for g in self.gens}

    def character(self, u, kappa):
        """nu(a), nu(b) from the fibre character u = (u_a, u_b) (turns), nu(t') = e^(2 pi i kappa); t' = t (+) or abt (-)"""
        F = self.F
        na, nb, k = F.root(u[0]), F.root(u[1]), F.root(kappa)
        lam = k if self.sign == "+" else k * F.inv(na * nb % self.p) % self.p
        return {"a": na, "b": nb, "t": lam}

    def cpow(self, chi, m):
        p = self.p
        return {g: pow(int(v), m, p) if m >= 0 else pow(F_inv(v, p), -m, p) for g, v in chi.items()}


def F_inv(v, p):
    return pow(int(v) % p, -1, p)


def perm_arrays(G, perms):
    return {g: np.array(perms[g], dtype=np.int64) for g in G.gens}


def tensor(base, small, pa):
    """E (x) P: generator g -> (x -> x^g, E(g) at every x)"""
    p = base.p
    out = {}
    for g in base.gens:
        s = pa[g]
        out[g] = BM(s.copy(), np.broadcast_to(small[g] % p, (len(s),) + small[g].shape).copy(), p)
    return Module(base.gens, out, p)


def local_module(base, pa, local):
    """generator g -> (x -> x^g, local[g][x])"""
    return Module(base.gens, {g: BM(pa[g].copy(), np.stack(local[g]) % base.p, base.p) for g in base.gens}, base.p)


def small_four(base, chi, m):
    """chi^m (x) rho"""
    p = base.p
    c = base.cpow(chi, m)
    return {g: base.rho[g] * c[g] % p for g in base.gens}


def small_line(base, chi, m):
    c = base.cpow(chi, m)
    return {g: np.array([[c[g]]], dtype=np.int64) for g in base.gens}


# ============================================================================================ classes
def cocycles(G, mod):
    """(Z^1 basis as columns, the coboundary matrix whose columns span B^1, H^1 representatives as columns)"""
    p, D, ng = mod.p, mod.D, len(mod.gens)
    F = np.vstack([fox_dense(mod, r) for r in G.rels])
    Zb = kernel(F, p)
    Bm = np.vstack([mod.M[g].dense(p) - np.eye(D, dtype=np.int64) for g in mod.gens]) % p
    rB = rank(Bm, p)
    reps, cur = [], Bm
    for j in range(Zb.shape[1]):
        cand = np.hstack([cur, Zb[:, j:j + 1]])
        if rank(cand, p) > rank(cur, p):
            reps.append(Zb[:, j])
            cur = cand
    return Zb, Bm, (np.stack(reps, axis=1) if reps else np.zeros((ng * D, 0), dtype=np.int64)), rB


def restrict_matrix(G, mod):
    """z -> (z(p1), z(p2)) as a 2D x (ngens D) matrix, and B^1(P) as 2D x D"""
    p, D = mod.p, mod.D
    R = np.vstack([fox_dense(mod, G.cusp[0]), fox_dense(mod, G.cusp[1])]) % p
    P1, P2 = mod.word(G.cusp[0]).dense(p), mod.word(G.cusp[1]).dense(p)
    BP = np.vstack([P1 - np.eye(D, dtype=np.int64), P2 - np.eye(D, dtype=np.int64)]) % p
    return R, BP


# ============================================================================================ the frame
SUB = [(i, j) for j in range(4) for i in range(j)]          # Lambda^2 V: e_i ^ e_j, i < j < 4  (6)
QUO = [(i, 4) for i in range(4)]                            # V ^ e_5 = V (x) L               (4)


def W_local(V, Lg, cg, p):
    """[[V, c L], [0, L]] (5 x 5) for one generator: V 4x4, Lg a scalar, cg the 4-vector c(g)"""
    W = np.zeros((5, 5), dtype=np.int64)
    W[:4, :4] = V
    W[:4, 4] = (np.array(cg, dtype=np.int64) * Lg) % p
    W[4, 4] = Lg
    return W % p


def frame_modules(base, pa, chi, c_local):
    """the four modules of the frame at the character chi, with W_x(g) built from c_local[g][x] (the 4-vector c_hat(g)_x),
    each with its sub/quotient split: name -> (module, sub coordinates, quotient coordinates)"""
    p = base.p
    V = small_four(base, chi, 1)
    Lc = base.cpow(chi, -4)
    d = len(pa[base.gens[0]])
    locW, locL2 = {}, {}
    for g in base.gens:
        Ws = [W_local(V[g], Lc[g], c_local[g][x], p) for x in range(d)]
        locW[g] = Ws
        locL2[g] = [wedge2_pairs(W, SUB + QUO, p) for W in Ws]
    E = local_module(base, pa, locW)
    L2 = local_module(base, pa, locL2)
    Es = E.dual().block([4, 0, 1, 2, 3])
    L2s = L2.dual().block(list(range(6, 10)) + list(range(6)))
    return {"E": (E, list(range(4)), [4]), "E*": (Es, [0], [1, 2, 3, 4]),
            "L2": (L2, list(range(6)), list(range(6, 10))), "L2*": (L2s, [0, 1, 2, 3], [4, 5, 6, 7, 8, 9])}


def reading(base, pa, chi, c_local, piece_cache=None):
    """Theorem C's quantities and identities, and the count, at one class (sm:B1535's cap_lib.reading, with dimensions over
    GF(p) on the base with the permutation module)"""
    G = base.G
    mods = frame_modules(base, pa, chi, c_local)
    C, I = {}, {}
    for nm, (md, sub, quo) in mods.items():
        C[nm] = Cohomology(G, md)
        for part, idx in (("S", sub), ("Q", quo)):
            key = (nm, part)
            if piece_cache is not None and key in piece_cache:
                C[nm + "." + part] = piece_cache[key]
            else:
                C[nm + "." + part] = Cohomology(G, md.block(idx))
                if piece_cache is not None:
                    piece_cache[key] = C[nm + "." + part]
    dual = {"E": "E*", "E*": "E", "L2": "L2*", "L2*": "L2"}
    pdual = {("E", "S"): ("E*", "Q"), ("E", "Q"): ("E*", "S"), ("L2", "S"): ("L2*", "Q"), ("L2", "Q"): ("L2*", "S")}
    pdual.update({v: k for k, v in pdual.items()})

    def ident(A, B):
        """B1297, the annihilator identity and Lemma E for a module A with dual B"""
        Ival = A.n - B.n
        return Ival, {"B1297": Ival == (A.a0 - B.a0) + B.t0 - A.r1,
                      "annihilator": A.r1 + B.r1 == A.t0 + B.t0 == A.h1P == B.h1P,
                      "Lemma E": Ival == B.h1 - A.h1 + 2 * (A.a0 - B.a0) + B.t0 - A.t0}
    idchecks = {}
    for nm in mods:
        I[nm], idchecks[nm] = ident(C[nm], C[dual[nm]])
    pieces = {}
    for nm in mods:
        pieces[nm] = []
        for part in ("S", "Q"):
            dn, dp = pdual[(nm, part)]
            val, ch = ident(C[nm + "." + part], C[dn + "." + dp])
            pieces[nm].append(val)
            idchecks[nm + "." + part] = ch
    les = {}
    for nm in mods:
        S_, Q_, X_ = C[nm + ".S"], C[nm + ".Q"], C[nm]
        rk0 = S_.a0 + Q_.a0 - X_.a0
        les[nm] = {"rk d0": rk0, "rk d1": S_.h1 + Q_.h1 - X_.h1 - rk0, "rk d0_P": S_.t0 + Q_.t0 - X_.t0}
    k = les["L2"]["rk d0_P"]
    nQ2s = C["L2*.S"].n
    nV, nL = C["E.S"].n, C["E.Q"].n
    b0 = les["E"]["rk d0"]
    checks = {
        "identities (B1297, annihilator, Lemma E) on every module and piece": all(all(v.values()) for v in idchecks.values()),
        "I(dual) = -I": I["E*"] == -I["E"] and I["L2*"] == -I["L2"],
        "I(S) = I(Q) = 0 for every piece": all(v == [0, 0] for v in pieces.values()),
        "L2: rk d0 = rk d0* = 0": les["L2"]["rk d0"] == 0 and les["L2*"]["rk d0"] == 0,
        "L2: rk d1 = 0": les["L2"]["rk d1"] == 0,
        "L2*: rk d0_P = 0": les["L2*"]["rk d0_P"] == 0,
        "I(L2) = k - rk d1(L2*)": I["L2"] == k - les["L2*"]["rk d1"],
        "k <= rk d1(L2*) <= k + n((VL)*)": k <= les["L2*"]["rk d1"] <= k + nQ2s,
        "W: rk d0(E*) = 0 and rk d0_P(E*) = 0": les["E*"]["rk d0"] == 0 and les["E*"]["rk d0_P"] == 0,
        "W: rk d0_P(E) = k": les["E"]["rk d0_P"] == k,
        "W: rk d1(E) <= n(V)": les["E"]["rk d1"] <= nV,
        "W: rk d1(E*) <= k + n(L)": les["E*"]["rk d1"] <= k + nL,
        "I(E) = -b0 + k + rk d1(E) - rk d1(E*)": I["E"] == -b0 + k + les["E"]["rk d1"] - les["E*"]["rk d1"],
        "cap: -n((VL)*) <= I(L2) <= 0": -nQ2s <= I["L2"] <= 0,
        "cap: I(E) >= -b0 - n(L)": I["E"] >= -b0 - nL,
    }
    return {"I(W)": I["E"], "I(L2W)": I["L2"], "k": k, "b0": b0, "n((VL)*)": nQ2s, "n(V)": nV, "n(L)": nL,
            "rk d1": {nm: les[nm]["rk d1"] for nm in les}, "rk d1(E*) bound": b0 - k + les["E*"]["rk d1"],
            "pieces": pieces, "checks": checks, "all": all(checks.values())}


def base_classes(base, Veta):
    """the classes the census reads on the base (sm:B1532's convention): one class 'c1' if h^1(V_eta) = 1; if h^1 = 2 with a
    one-dimensional interior line, the interior class 'int' and a generic class 'gen' = c_b + s c_int (s a fixed rational chosen
    off the special points with probability 1 - O(1/p)); returns {name: cocycle vector}"""
    G, p = base.G, base.p
    Zb, Bm, reps, rB = cocycles(G, Veta)
    if reps.shape[1] == 1:
        return {"c1": reps[:, 0] % p}
    assert reps.shape[1] == 2, ("h^1(V_eta) > 2 on a base", reps.shape)
    R, BP = restrict_matrix(G, Veta)
    D = Veta.D
    # x1 R z1 + x2 R z2 = BP v  ->  unknowns (x1, x2, v)
    A = np.hstack([(R @ reps) % p, (-BP) % p])
    K = kernel(A, p)
    xs = [K[:2, j] for j in range(K.shape[1]) if np.any(K[:2, j] % p)]
    assert xs, "no interior class"
    x = xs[0]
    cint = (reps @ x) % p
    for x2 in xs[1:]:
        assert rank(np.stack([x, x2], axis=1), p) == 1, "interior line is not one-dimensional"
    cb = reps[:, 0] if rank(np.stack([x, np.array([1, 0])], axis=1), p) == 2 else reps[:, 1]
    s = 3 * pow(7, -1, p) % p
    return {"int": cint, "gen": (cb + s * cint) % p}


# ============================================================================================ the supplies (Theorem C's caps)
def supplies(base, pa, chi):
    """at the pulled-back character chi on the cover: the class space h^1(V_eta), n(V_eta), b0 = h^0(L), n(L), and
    n((V L)*) -- Theorem C's caps capW = b0 + n(L), capL2 = n((V L)*) (computed on the dual module itself)"""
    G = base.G
    Ce = Cohomology(G, tensor(base, small_four(base, chi, 5), pa))
    Cl = Cohomology(G, tensor(base, small_line(base, chi, -4), pa))
    Cq = Cohomology(G, tensor(base, small_four(base, chi, -3), pa).dual())
    return {"h1(V_eta)": Ce.h1, "n(V_eta)": Ce.n, "b0": Cl.a0, "n(L)": Cl.n, "n((VL)*)": Cq.n,
            "capW": Cl.a0 + Cl.n, "capL2": Cq.n}


# ============================================================================================ the cover's own classes, by stratum
def class_space(base, pa, chi):
    """(Zb, R, BP) for V_eta (x) P: cocycles as columns, the restriction to the base cusp, B^1 of the cusp"""
    mod = tensor(base, small_four(base, chi, 5), pa)
    C = Cohomology(base.G, mod, keep=True)
    return mod, C.Zb, C.R, C.BP


def orbit_rows(cusp, e, D):
    """the rows of the restriction (z(p1) over D, then z(p2) over D) and the columns of B^1(P) that belong to one cusp"""
    xs = cusp["orbit"]
    rows = [x * e + i for x in xs for i in range(e)]
    return rows + [D + r for r in rows], rows


def stratum_basis(Zb, R, BP, cusps, kill, e, p):
    """a basis (columns, as combinations of Zb's columns) of the cocycles whose restriction to every cusp in `kill` is a
    coboundary there"""
    D = BP.shape[1]
    nz = Zb.shape[1]
    if not kill:
        return np.eye(nz, dtype=np.int64)
    blocks, vcols = [], 0
    rows_all = []
    for O in kill:
        r, c = orbit_rows(cusps[O], e, D)
        rows_all.append((r, c))
        vcols += len(c)
    A = np.zeros((sum(len(r) for r, _ in rows_all), nz + vcols), dtype=np.int64)
    RZ = (R @ Zb) % p
    ro, co = 0, nz
    for (r, c) in rows_all:
        A[ro:ro + len(r), :nz] = RZ[r]
        A[ro:ro + len(r), co:co + len(c)] = (-BP[np.ix_(r, c)]) % p
        ro += len(r)
        co += len(c)
    K = kernel(A, p)
    X = K[:nz] % p
    # independent columns
    keep, cur = [], np.zeros((nz, 0), dtype=np.int64)
    for j in range(X.shape[1]):
        cand = np.hstack([cur, X[:, j:j + 1]])
        if rank(cand, p) > cur.shape[1]:
            cur = cand
    return cur


def local_from(z, gens, d, e=4):
    """c_local[g][x] = c_hat(g)_x from a cocycle vector of V_eta (x) P (generator-major, then point, then coordinate)"""
    D = d * e
    return {g: [z[gi * D + x * e:gi * D + (x + 1) * e] for x in range(d)] for gi, g in enumerate(gens)}


def strata_readings(base, pa, chi, cusps, rng, draws=2, piece_cache=None, only=None):
    """for every subset S of the cusps where chi is trivial: two random classes of the stratum (cocycles that are coboundaries on
    the cusps of T \\ S), read; returns [(S, [reading, reading])]"""
    p = base.p
    d = len(pa[base.gens[0]])
    mod, Zb, R, BP = class_space(base, pa, chi)
    T = [i for i, cu in enumerate(cusps) if cu["trivial"]]
    out = []
    for size in range(len(T) + 1):
        for S in __import__("itertools").combinations(T, size):
            if only is not None and list(S) not in only:
                continue
            kill = [O for O in T if O not in S]
            Bs = stratum_basis(Zb, R, BP, cusps, kill, 4, p)
            if Bs.shape[1] == 0:
                continue
            reads = []
            for _ in range(draws):
                coeff = np.array([rng.randrange(1, p) for _ in range(Bs.shape[1])], dtype=np.int64)
                z = (Zb @ ((Bs @ coeff) % p)) % p
                reads.append(reading(base, pa, chi, local_from(z, base.gens, d), piece_cache))
            out.append((list(S), reads))
    return out
