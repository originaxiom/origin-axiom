#!/usr/bin/env python3
"""Own implementation of the one-cusped index I = n(V) - n(V*), n = a_1 - r_1, over GF(p).
Derivations used (written out so the code is checkable):
  cocycle convention f(gh) = f(g) + rho(g) f(h)  =>  f(w) = sum_g D_g(w) f(g), D accumulated over letters with a prefix.
  H^0(pi;V) = ker(stack_g (rho(g)-1)); a0 = d - rank.
  Z^1 = ker(Fox Jacobian of the relators); B^1 has dim d - a0; a1 = dim Z^1 - (d - a0).
  cusp torus T = Z^2 = <mu,lam>:  H^0: t0 = d - rank[[A_mu],[A_lam]];
     Z^1(T) = {(u,w): A_lam u = A_mu w}  (from mu lam = lam mu),  B^1(T) = {(A_mu v, A_lam v)};
     t1 = (2d - rank[A_lam | -A_mu]) - rank[[A_mu],[A_lam]].
  r_1 = rank of H^1(pi;V) -> H^1(T;V), computed as rank([res(Z^1) | B^1(T)]) - rank(B^1(T)).
  rho_chi(g) = [[chi(g), c(g)],[0, chi(g)^{-1}]] is a homomorphism iff ct := c*chi is a 1-cocycle for chi^2.
Self-tests asserted on every module: r1(V) + r1(V*) = t1,  I = (a0 - a0*) + t0* - r1(V)."""
import itertools, math

def rank_and_null(rows, ncols, p, want_null=False):
    R = [list(r) for r in rows]; piv = []; rk = 0
    for c in range(ncols):
        k = None
        for i in range(rk, len(R)):
            if R[i][c] % p: k = i; break
        if k is None: continue
        R[rk], R[k] = R[k], R[rk]
        iv = pow(R[rk][c], p - 2, p); R[rk] = [x * iv % p for x in R[rk]]
        for i in range(len(R)):
            if i != rk and R[i][c] % p:
                f = R[i][c]; R[i] = [(x - f * y) % p for x, y in zip(R[i], R[rk])]
        piv.append(c); rk += 1
    if not want_null: return rk, None
    free = [c for c in range(ncols) if c not in piv]; NS = []
    for fc in free:
        v = [0] * ncols; v[fc] = 1
        for i, pc in enumerate(piv): v[pc] = (-R[i][fc]) % p
        NS.append(v)
    return rk, NS

def mmul(A, B, p):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum(A[i][l] * B[l][j] for l in range(k)) % p for j in range(m)] for i in range(n)]
def msub(A, B, p): return [[(x - y) % p for x, y in zip(r, s)] for r, s in zip(A, B)]
def eye(n): return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
def zeros(n, m): return [[0] * m for _ in range(n)]
def minv(A, p):
    n = len(A); aug = [list(A[i]) + [1 if i == j else 0 for j in range(n)] for i in range(n)]
    rk, _ = rank_and_null(aug, n, p)     # reduce on the first n columns only
    # redo reduction keeping the augmented part
    R = [list(r) for r in aug]; rk = 0
    for c in range(n):
        k = None
        for i in range(rk, n):
            if R[i][c] % p: k = i; break
        assert k is not None, "singular"
        R[rk], R[k] = R[k], R[rk]
        iv = pow(R[rk][c], p - 2, p); R[rk] = [x * iv % p for x in R[rk]]
        for i in range(n):
            if i != rk and R[i][c] % p:
                f = R[i][c]; R[i] = [(x - f * y) % p for x, y in zip(R[i], R[rk])]
        rk += 1
    return [r[n:] for r in R]
def mT(A): return [list(r) for r in zip(*A)]

class Mod:
    def __init__(self, gens, mats, p):
        self.gens = list(gens); self.p = p; self.d = len(mats[gens[0]])
        self.M = dict(mats)
        for g in gens: self.M[g.upper()] = minv(mats[g], p)
    def word(self, w):
        R = eye(self.d)
        for ch in w: R = mmul(R, self.M[ch], self.p)
        return R
    def fox(self, w):
        p = self.p; d = self.d; D = {g: zeros(d, d) for g in self.gens}; pre = eye(d)
        for ch in w:
            g = ch.lower()
            if ch.islower():
                D[g] = [[(x + y) % p for x, y in zip(r, s)] for r, s in zip(D[g], pre)]
                pre = mmul(pre, self.M[ch], p)
            else:
                pre = mmul(pre, self.M[ch], p)
                D[g] = msub(D[g], pre, p)
        return D
    def dual(self):
        return Mod(self.gens, {g: mT(minv(self.M[g], self.p)) for g in self.gens}, self.p)
    def ok(self, rels):
        I = eye(self.d)
        return all(self.word(r) == I for r in rels)

def cohom(V, rels, mu, lam):
    p = V.p; d = V.d; gens = V.gens; I = eye(d)
    D0 = [row for g in gens for row in msub(V.M[g], I, p)]
    rk0, _ = rank_and_null(D0, d, p); a0 = d - rk0
    J = []
    for r in rels:
        F = V.fox(r)
        for i in range(d): J.append([F[g][i][j] for g in gens for j in range(d)])
    rkJ, Z1 = rank_and_null(J, len(gens) * d, p, want_null=True)
    dimZ = len(gens) * d - rkJ; a1 = dimZ - rk0
    Am = msub(V.word(mu), I, p); Al = msub(V.word(lam), I, p)
    BT = [list(Am[i]) for i in range(d)] + [list(Al[i]) for i in range(d)]   # 2d x d : v -> (Am v, Al v)
    rkBT, _ = rank_and_null(BT, d, p); t0 = d - rkBT
    ZT = [[(-Al[i][j]) % p for j in range(d)] + [Am[i][j] for j in range(d)] for i in range(d)]
    rkZT, _ = rank_and_null(ZT, 2 * d, p); t1 = (2 * d - rkZT) - rkBT
    Dm = V.fox(mu); Dl = V.fox(lam)
    Rm = [[Dm[g][i][j] for g in gens for j in range(d)] for i in range(d)]
    Rl = [[Dl[g][i][j] for g in gens for j in range(d)] for i in range(d)]
    Res = Rm + Rl                                                  # 2d x (ngens d)
    cols = []
    for z in Z1: cols.append([sum(Res[i][k] * z[k] for k in range(len(z))) % p for i in range(2 * d)])
    BTcols = [[BT[i][j] for i in range(2 * d)] for j in range(d)]  # columns of BT as vectors of length 2d
    allc = cols + BTcols
    rk_all, _ = rank_and_null(allc, 2 * d, p)                      # rows = vectors, rank = dim span
    rkB, _ = rank_and_null(BTcols, 2 * d, p)
    r1 = rk_all - rkB
    return a0, a1, t0, t1, r1

def index(V, rels, mu, lam, check=True):
    a0, a1, t0, t1, r1 = cohom(V, rels, mu, lam)
    b0, b1, s0, s1, q1 = cohom(V.dual(), rels, mu, lam)
    I = (a1 - r1) - (b1 - q1)
    if check:
        assert r1 + q1 == t1 == s1, ("annihilator", r1, q1, t1, s1)
        assert I == (a0 - b0) + s0 - r1, ("B1297 identity", I, a0, b0, s0, r1)
    return I, (a0, a1, t0, r1), (b0, b1, s0, q1)
