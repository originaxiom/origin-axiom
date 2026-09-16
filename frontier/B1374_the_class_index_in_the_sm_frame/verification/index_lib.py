#!/usr/bin/env python3
"""B1374 -- the one-cusped index I = n(V) - n(V*) (main's B1297 definition: n = a_1 - r_1, the interior classes) on reducible
non-split modules Sym^m(rho_chi) (x) psi, computed with this seat's own code over prime fields GF(p).  Ranks over GF(p) can only fall
below the characteristic-zero ranks (never rise), so agreement of every dimension over three primes with the exact record is the check;
a disagreement on one prime is a rank drop, on all three a genuine difference.
Conventions (own derivation).  A 1-cocycle f: pi -> V obeys f(gh) = f(g) + rho(g) f(h), so f(w) = sum_g D_g(w) f(g) with the Fox
derivative D_g(w) evaluated in rho (D_g(g) = 1, D_g(g^-1) = -rho(g^-1), D_g(uv) = D_g(u) + rho(u) D_g(v)).  H^0 = invariants;
H^1 = Z^1 / B^1 with Z^1 = the cocycles vanishing on the relators and B^1 = {(rho(g) v - v)_g}.  On the cusp torus T = <mu, lambda>:
Z^1(T) = {(u, w): (rho(mu) - 1) w = (rho(lambda) - 1) u}, B^1(T) = {((rho(mu) - 1) v, (rho(lambda) - 1) v)}; r_1 = rank of the
restriction H^1(pi) -> H^1(T); t_0 = dim H^0(T); n = a_1 - r_1; I = n(V) - n(V*); the identities I = (a_0 - a_0*) + t_0* - r_1 and
r_1 + r_1* = t_1 (B1297 section 2) are asserted on every module as a self-test.
rho_chi(g) = [[chi(g), c(g)], [0, chi(g)^-1]] is a representation iff ct := c chi is a 1-cocycle for the action of chi^2
(ct(gh) = chi(g)^2 ct(h) + ct(g)); non-split iff ct is not a coboundary; such ct exists iff H^1(pi; chi^2) != 0 (Fox calculus)."""
import itertools, math

class GF:
    def __init__(self, p):
        self.p = p
        self.g = self._primitive_root()
    def _primitive_root(self):
        p = self.p; n = p - 1; f = []; m = n; d = 2
        while d * d <= m:
            if m % d == 0:
                f.append(d)
                while m % d == 0: m //= d
            d += 1
        if m > 1: f.append(m)
        for g in range(2, p):
            if all(pow(g, n // q, p) != 1 for q in f): return g
        raise ValueError
    def root_of_unity(self, n):
        assert (self.p - 1) % n == 0, (self.p, n)
        return pow(self.g, (self.p - 1) // n, self.p)
    def inv(self, a): return pow(a % self.p, self.p - 2, self.p)
    def sqrt(self, a):
        a %= self.p
        for x in range(self.p):
            if x * x % self.p == a: return x
        return None
    # ---- matrices: lists of lists of ints mod p
    def eye(self, n): return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    def zeros(self, n, m): return [[0] * m for _ in range(n)]
    def mul(self, A, B):
        p = self.p; n, k, m = len(A), len(B), len(B[0])
        return [[sum(A[i][l] * B[l][j] for l in range(k)) % p for j in range(m)] for i in range(n)]
    def add(self, A, B): return [[(x + y) % self.p for x, y in zip(r, s)] for r, s in zip(A, B)]
    def sub(self, A, B): return [[(x - y) % self.p for x, y in zip(r, s)] for r, s in zip(A, B)]
    def scale(self, c, A): return [[c * x % self.p for x in r] for r in A]
    def T(self, A): return [list(r) for r in zip(*A)]
    def vstack(self, *Ms): return [list(r) for M in Ms for r in M]
    def hstack(self, *Ms): return [sum((list(M[i]) for M in Ms), []) for i in range(len(Ms[0]))]
    def rref(self, A):
        """row-reduce a copy; returns (rows, pivot columns)"""
        p = self.p; R = [list(r) for r in A]; piv = []; r = 0
        ncol = len(R[0]) if R else 0
        for c in range(ncol):
            if r >= len(R): break
            k = next((i for i in range(r, len(R)) if R[i][c] % p), None)
            if k is None: continue
            R[r], R[k] = R[k], R[r]; iv = self.inv(R[r][c]); R[r] = [x * iv % p for x in R[r]]
            for i in range(len(R)):
                if i != r and R[i][c] % p:
                    f = R[i][c]; R[i] = [(x - f * y) % p for x, y in zip(R[i], R[r])]
            piv.append(c); r += 1
        return R, piv
    def rank(self, A):
        if not A or not A[0]: return 0
        return len(self.rref(A)[1])
    def nullspace(self, A, ncols):
        """basis of {x : A x = 0} (as row vectors of length ncols)"""
        if not A: return [[1 if i == j else 0 for j in range(ncols)] for i in range(ncols)]
        R, piv = self.rref(A); free = [c for c in range(ncols) if c not in piv]; out = []
        for fc in free:
            v = [0] * ncols; v[fc] = 1
            for i, pc in enumerate(piv): v[pc] = (-R[i][fc]) % self.p
            out.append(v)
        return out
    def inverse(self, A):
        n = len(A); R, piv = self.rref(self.hstack(A, self.eye(n)))
        assert piv == list(range(n)), "singular"
        return [r[n:] for r in R]

class Rep:
    """a representation of a finitely presented group over GF(p): generator letters -> matrices; inverses cached"""
    def __init__(self, F, gens, mats):
        self.F = F; self.gens = list(gens); self.d = len(mats[gens[0]])
        self.M = dict(mats)
        for g in gens: self.M[g.upper()] = F.inverse(mats[g])
    def word(self, w):
        R = self.F.eye(self.d)
        for ch in w: R = self.F.mul(R, self.M[ch])
        return R
    def fox(self, w):
        """{g: D_g(w)} evaluated in the representation (left convention f(gh) = f(g) + rho(g) f(h))"""
        F = self.F; d = self.d; D = {g: F.zeros(d, d) for g in self.gens}; pre = F.eye(d)
        for ch in w:
            g = ch.lower()
            if ch.islower(): D[g] = F.add(D[g], pre)
            else: D[g] = F.sub(D[g], F.mul(pre, self.M[ch]))     # D_g(g^-1) = -rho(g^-1), then times the prefix
            pre = F.mul(pre, self.M[ch])
        return D
    def dual(self):
        return Rep(self.F, self.gens, {g: self.F.T(self.F.inverse(self.M[g])) for g in self.gens})
    def check_relators(self, rels):
        I = self.F.eye(self.d)
        return all(self.word(r) == I for r in rels)

def cohomology_data(rep, rels, mu, lam):
    """(a0, a1, t0, t1, r1): dims of H^0(pi;V), H^1(pi;V), H^0(T;V), H^1(T;V), rank(H^1(pi;V) -> H^1(T;V))"""
    F = rep.F; d = rep.d; gens = rep.gens; I = F.eye(d)
    d0 = F.vstack(*[F.sub(rep.M[g], I) for g in gens])                       # (#gens d) x d
    rk0 = F.rank(d0); a0 = d - rk0
    d1 = F.vstack(*[F.hstack(*[rep.fox(r)[g] for g in gens]) for r in rels]) if rels else []   # (#rels d) x (#gens d)
    Z1 = F.nullspace(d1, len(gens) * d)                                        # basis of the cocycles, as vectors
    a1 = len(Z1) - rk0
    Wm, Wl = rep.word(mu), rep.word(lam)
    Am, Al = F.sub(Wm, I), F.sub(Wl, I)
    BT = F.vstack(Am, Al)                                                      # coboundaries on T: v -> ((Wm-1)v, (Wl-1)v)
    rkBT = F.rank(BT); t0 = d - rkBT
    ZT = F.hstack(F.scale(F.p - 1, Al), Am)                                    # cocycle condition on T: (Wm-1) w - (Wl-1) u = 0 on (u, w)
    t1 = 2 * d - F.rank(ZT) - rkBT
    Dm, Dl = rep.fox(mu), rep.fox(lam)
    Rm = F.hstack(*[Dm[g] for g in gens]); Rl = F.hstack(*[Dl[g] for g in gens])
    Res = F.vstack(Rm, Rl)                                                     # restriction: f -> (f(mu), f(lambda)), a 2d x (#gens d) matrix
    if Z1:
        cols = F.mul(Res, F.T(Z1))                                             # 2d x dim Z^1
        r1 = F.rank(F.hstack(cols, BT)) - rkBT
    else: r1 = 0
    return a0, a1, t0, t1, r1

def index(rep, rels, mu, lam, check=True):
    """I(V) = n(V) - n(V*), n = a_1 - r_1; returns (I, data V, data V*)"""
    a0, a1, t0, t1, r1 = cohomology_data(rep, rels, mu, lam)
    b0, b1, s0, s1, q1 = cohomology_data(rep.dual(), rels, mu, lam)
    n, nd = a1 - r1, b1 - q1; I = n - nd
    if check:
        assert r1 + q1 == t1 == s1, ("annihilator identity", (r1, q1, t1, s1))
        assert I == (a0 - b0) + s0 - r1, ("B1297 identity", I, a0, b0, s0, r1)
    return I, (a0, a1, t0, r1), (b0, b1, s0, q1)

# ---------------------------------------------------------------- characters, cocycles, the reducible representation, Sym^m
def abelian_exponents(word, gens):
    v = {g: 0 for g in gens}
    for ch in word: v[ch.lower()] += 1 if ch.islower() else -1
    return v
def characters(F, gens, rels, N):
    """all homomorphisms pi -> mu_N(GF(p)) as dicts gen -> exponent k (value zeta^k)"""
    ex = [abelian_exponents(r, gens) for r in rels]; out = []
    for ks in itertools.product(range(N), repeat=len(gens)):
        if all(sum(e[g] * k for g, k in zip(gens, ks)) % N == 0 for e in ex): out.append(dict(zip(gens, ks)))
    return out
def char_value(F, zeta, chi, word):
    v = 1
    for ch in word:
        k = chi[ch.lower()]; v = v * pow(zeta, k if ch.islower() else -k, F.p) % F.p
    return v
def char_matrix(F, zeta, chi, gens, power=1):
    return {g: [[pow(zeta, power * chi[g] % (F.p - 1), F.p)]] for g in gens}
def h1_and_cocycle(F, gens, rels, mu, lam, scalar):
    """for a 1-dim module given by generator values (dict), h^1 and a non-coboundary cocycle (dict gen -> value) or None"""
    rep = Rep(F, gens, {g: [[scalar[g] % F.p]] for g in gens})
    d1 = F.vstack(*[F.hstack(*[rep.fox(r)[g] for g in gens]) for r in rels]) if rels else []
    Z = F.nullspace(d1, len(gens)); b = [(scalar[g] - 1) % F.p for g in gens]
    rb = 1 if any(b) else 0; h1 = len(Z) - rb
    if h1 <= 0: return h1, None
    for z in Z:
        if rb == 0 or F.rank([b, z]) == 2: return h1, dict(zip(gens, z))
    return h1, None
def reducible_rep(F, gens, chi_val, ct):
    """chi_val: gen -> value in GF(p); ct: the chi^2-cocycle; rho(g) = [[chi, ct/chi], [0, 1/chi]]"""
    return {g: [[chi_val[g], ct[g] * F.inv(chi_val[g]) % F.p], [0, F.inv(chi_val[g])]] for g in gens}
def sym_power(F, A, m):
    """Sym^m of the 2x2 matrix A on the basis x^{m-j} y^j, A x = a x + c y, A y = b x + d y (columns)"""
    p = F.p; a, b = A[0]; c, d = A[1]
    def poly_pow(coeffs, k):        # coeffs of a linear form (alpha x + beta y)^k as list by power of y
        al, be = coeffs; out = []
        for i in range(k + 1): out.append(math.comb(k, i) * pow(al, k - i, p) * pow(be, i, p) % p)
        return out
    def poly_mul(u, v):
        out = [0] * (len(u) + len(v) - 1)
        for i, x in enumerate(u):
            for j, y in enumerate(v): out[i + j] = (out[i + j] + x * y) % p
        return out
    cols = []
    for j in range(m + 1):
        cols.append(poly_mul(poly_pow((a, c), m - j), poly_pow((b, d), j)))     # image of x^{m-j} y^j
    return [[cols[j][i] for j in range(m + 1)] for i in range(m + 1)]
def module(F, gens, rho, m, psi_val):
    """Sym^m(rho) (x) psi as generator matrices"""
    return {g: F.scale(psi_val[g], sym_power(F, rho[g], m)) for g in gens}
