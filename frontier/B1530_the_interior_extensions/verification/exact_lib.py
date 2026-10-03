#!/usr/bin/env python3
"""B1530 -- route E: exact arithmetic over Q(zeta_24).  Nothing sealed is computed on import.

THE FIELD.  K = Q(zeta), zeta = e^{2 pi i / 24}, with minimal polynomial x^8 - x^4 + 1.  It holds every number the arc needs:
i = zeta^6, zeta_8 = zeta^3, sqrt 2 = zeta^3 + zeta^21, zeta_3 = zeta^8, sqrt 3 = zeta^2 + zeta^22, and every character value of
order dividing 24.  An element is an integer vector on 1, zeta, ..., zeta^7 over one positive denominator, in lowest terms.  The
inverse is the product of the seven other Galois conjugates over the norm, which is rational.

COHOMOLOGY, as main's class index (B1297) needs it.  Fox calculus with left cocycles, z(gh) = z(g) + g z(h):
  - Z^1 is the kernel of the relators' Fox matrix, B^1 the image of v -> ((g - 1) v)_g, h^0 the common fixed space;
  - the restriction to the peripheral subgroup P = <p1, p2> sends z to (z(p1), z(p2)), modulo B^1(P);
  - n(E) = h^1 - r1 and I(E) = n(E) - n(E*).
Three identities are asserted at every reading:
  - B1297: I = (a0 - b0) + s0 - r1;
  - the annihilator: r1(E) + r1(E*) = t0 + s0 = h^1(P; E);
  - sm:B1527's Lemma E: I = h^1(E*) - h^1(E) + 2 (a0 - b0) + s0 - t0.

THE MECHANISM (PREREGISTRATION section 3), for a module V on a word state Gamma = F x| <t'>:
  - S0 on C = H^1(F; V) = V^2 / B^1(F), (S0 z)(g) = V(t')^-1 z(phi'(g)), with t' g t'^-1 = phi'(g).  With V(t') taken with its
    character, H^1(Gamma; V) = ker(S0 - 1) (H^0(F; V) = 0), and the cup product with the fibration class x is the map
    ker(S0 - 1) -> coker(S0 - 1) (Wang), so x cup c = 0 iff c|_F lies in im(S0 - 1);
  - mu: the restriction to P of a lift of an interior class c_int of V to H^1(Lambda^2 W1), W1 = [[V, c_int], [0, 1]], read in
    H^1(P; Lambda^2 V) after the splitting e4' = e4 - w (c_int(p) = (V(p) - 1) w on P), and tested against Lambda_A, the
    restriction image of H^1(Gamma; Lambda^2 V).

New code for B1530.  It shares nothing with route N (sm:B1527's cusp_lib at 60 digits) except the group presentations
(sm:B1527's family_lib.word_group) and, for m135, the exact holonomy read by sm:B1529's post_run_exact_m135.exact_sl2.  That
holonomy is checked there in exact arithmetic: the relators hold in PGL(2, Q(i))."""
from fractions import Fraction
from math import gcd

DEG = 8                              # [Q(zeta_24) : Q]
_GAL = (5, 7, 11, 13, 17, 19, 23)    # the Galois group (Z/24)^* without 1


# ============================================================================================ the field
def _norm(c, d):
    g = d
    for x in c:
        if x:
            g = gcd(g, x)
    if g > 1:
        c = tuple(x // g for x in c)
        d //= g
    return c, d


class K:
    """sum_k c[k] zeta^k / d, zeta = e^{2 pi i / 24}, exact"""
    __slots__ = ("c", "d")

    def __init__(self, c, d=1):
        if d < 0:
            c, d = tuple(-x for x in c), -d
        c = tuple(int(x) for x in c)
        if not any(c):
            self.c, self.d = (0,) * DEG, 1
        else:
            self.c, self.d = _norm(c, int(d))

    @staticmethod
    def of(x):
        if isinstance(x, K):
            return x
        f = Fraction(x)
        return K((f.numerator,) + (0,) * (DEG - 1), f.denominator)

    def __add__(self, o):
        o = K.of(o)
        if self.d == o.d:
            return K(tuple(a + b for a, b in zip(self.c, o.c)), self.d)
        return K(tuple(a * o.d + b * self.d for a, b in zip(self.c, o.c)), self.d * o.d)

    __radd__ = __add__

    def __neg__(self):
        return K(tuple(-a for a in self.c), self.d)

    def __sub__(self, o):
        return self + (-K.of(o))

    def __rsub__(self, o):
        return K.of(o) - self

    def __mul__(self, o):
        o = K.of(o)
        conv = [0] * (2 * DEG - 1)
        for i, a in enumerate(self.c):
            if a:
                for j, b in enumerate(o.c):
                    if b:
                        conv[i + j] += a * b
        for k in range(2 * DEG - 2, DEG - 1, -1):          # x^8 = x^4 - 1
            v = conv[k]
            if v:
                conv[k - 4] += v
                conv[k - 8] -= v
        return K(conv[:DEG], self.d * o.d)

    __rmul__ = __mul__

    def is_zero(self):
        return not any(self.c)

    def __eq__(self, o):
        return (self - K.of(o)).is_zero()

    def __hash__(self):
        return hash((self.c, self.d))

    def sigma(self, k):
        """the Galois automorphism zeta -> zeta^k (k prime to 24)"""
        out = [0] * DEG
        for i, a in enumerate(self.c):
            if a:
                v = X[(i * k) % 24]
                for j in range(DEG):
                    out[j] += a * v[j]
        return K(out, self.d)

    def conj(self):
        return self.sigma(23)

    def rational(self):
        """the value as a Fraction, or None if it is not rational"""
        if any(self.c[1:]):
            return None
        return Fraction(self.c[0], self.d)

    def inv(self):
        assert not self.is_zero(), "division by zero"
        p = K.of(1)
        for k in _GAL:
            p = p * self.sigma(k)
        n = (self * p).rational()
        assert n is not None and n != 0
        return p * K.of(1 / n)

    def __truediv__(self, o):
        return self * K.of(o).inv()

    def __rtruediv__(self, o):
        return K.of(o) * self.inv()

    def num(self, mp):
        z = mp.expjpi(mp.mpf(1) / 12)
        return sum((mp.mpf(a) * z ** i for i, a in enumerate(self.c) if a), mp.mpc(0)) / self.d

    def __repr__(self):
        return f"K({self.c}/{self.d})"


def _powers():
    out, v = [], [1] + [0] * (DEG - 1)
    for _ in range(24):
        out.append(tuple(v))
        w = [0] + v[:-1]                                    # multiply by x
        top = v[-1]
        if top:                                             # x^8 = x^4 - 1
            w[4] += top
            w[0] -= top
        v = w
    return out


X = _powers()                                               # X[m] = zeta^m on the basis 1, ..., zeta^7
ZERO, ONE = K.of(0), K.of(1)


def zeta(m):
    return K(X[m % 24], 1)


I_UNIT = zeta(6)
SQRT2 = zeta(3) + zeta(21)
SQRT3 = zeta(2) + zeta(22)
OMEGA = zeta(8)                                             # e^{2 pi i / 3}


def root_of_unity(fr):
    """e^{2 pi i fr} for fr in (1/24) Z"""
    k = Fraction(fr) * 24
    assert k.denominator == 1, fr
    return zeta(int(k))


def sqrt_rational(q):
    """sqrt(q) for a rational q > 0 whose square-free part is 1, 2, 3 or 6"""
    q = Fraction(q)
    assert q > 0
    for m, root in ((1, ONE), (2, SQRT2), (3, SQRT3), (6, SQRT2 * SQRT3)):
        r = q / m
        n, d = r.numerator, r.denominator
        rn, rd = round(n ** 0.5), round(d ** 0.5)
        for a in (rn - 1, rn, rn + 1):
            for b in (rd - 1, rd, rd + 1):
                if a > 0 and b > 0 and a * a == n and b * b == d:
                    return root * K.of(Fraction(a, b))
    raise ValueError(f"sqrt({q}) is not in Q(zeta_24)")


def from_z8(x):
    """an element of sm:B1529's Q(zeta_8) class (c0 + c1 z + c2 z^2 + c3 z^3, z = zeta_8 = zeta_24^3)"""
    out = ZERO
    for i, a in enumerate(x.c):
        if a:
            out = out + zeta(3 * i) * K.of(a)
    return out


# ============================================================================================ matrices over K
def mat(rows):
    return [[K.of(x) for x in r] for r in rows]


def zeros(n, m):
    return [[ZERO] * m for _ in range(n)]


def eye(n):
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


def mmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    out = []
    for i in range(n):
        Ai = A[i]
        row = []
        for j in range(p):
            s = ZERO
            for k in range(m):
                a = Ai[k]
                if not a.is_zero():
                    b = B[k][j]
                    if not b.is_zero():
                        s = s + a * b
            row.append(s)
        out.append(row)
    return out


def madd(A, B, s=1):
    s = K.of(s)
    return [[A[i][j] + B[i][j] * s for j in range(len(A[0]))] for i in range(len(A))]


def scal(A, s):
    s = K.of(s)
    return [[x * s for x in r] for r in A]


def transpose(A):
    return [list(r) for r in zip(*A)]


def is_identity(A):
    return all((A[i][j] == (ONE if i == j else ZERO)) for i in range(len(A)) for j in range(len(A)))


def mvec(A, v):
    return [sum((A[i][k] * v[k] for k in range(len(v)) if not A[i][k].is_zero() and not v[k].is_zero()), ZERO)
            for i in range(len(A))]


def rref(A, ncols):
    """(the reduced rows, the pivot columns)"""
    M = [list(r) for r in A]
    piv, r = [], 0
    for c in range(ncols):
        p = next((i for i in range(r, len(M)) if not M[i][c].is_zero()), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pinv = M[r][c].inv()
        M[r] = [x * pinv for x in M[r]]
        for i in range(len(M)):
            if i != r and not M[i][c].is_zero():
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        piv.append(c)
        r += 1
        if r == len(M):
            break
    return M[:r], piv


def rank(A, ncols=None):
    if not A:
        return 0
    return len(rref(A, ncols if ncols is not None else len(A[0]))[1])


def rank_vectors(vs, length):
    return rank([list(v) for v in vs], length) if vs else 0


def nullspace(A, ncols):
    """a basis of {x : A x = 0}"""
    if not A:
        return [[ONE if i == k else ZERO for i in range(ncols)] for k in range(ncols)]
    R, piv = rref(A, ncols)
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [ZERO] * ncols
        v[fc] = ONE
        for k, pc in enumerate(piv):
            v[pc] = -R[k][fc]
        basis.append(v)
    return basis


def minv(A):
    n = len(A)
    M = [list(A[i]) + eye(n)[i] for i in range(n)]
    R, piv = rref(M, n)
    assert piv == list(range(n)), "singular matrix"
    return [r[n:] for r in R]


def in_span(v, vs, length):
    return rank_vectors(list(vs) + [v], length) == rank_vectors(list(vs), length)


def charpoly(A):
    """Faddeev-LeVerrier: coefficients of det(s - A), highest first"""
    n = len(A)
    coeffs = [ONE]
    Mk = zeros(n, n)
    for k in range(1, n + 1):
        Mk = madd(mmul(A, Mk), eye(n), coeffs[-1])
        AM = mmul(A, Mk)
        coeffs.append(sum((AM[i][i] for i in range(n)), ZERO) * K.of(Fraction(-1, k)))
    return coeffs


def jordan_partition(T, lam):
    """the sizes of the Jordan blocks of T at the eigenvalue lam, from the ranks of (T - lam)^k"""
    n = len(T)
    N = madd(T, eye(n), -K.of(lam))
    dims, P = [0], eye(n)
    while True:
        P = mmul(P, N)
        dims.append(n - rank(P, n))
        if dims[-1] == dims[-2]:
            break
    # number of blocks of size >= k is dims[k] - dims[k-1]
    ge = [dims[k] - dims[k - 1] for k in range(1, len(dims))]
    sizes = []
    for k in range(len(ge)):
        exactly = ge[k] - (ge[k + 1] if k + 1 < len(ge) else 0)
        sizes += [k + 1] * exactly
    return sorted(sizes, reverse=True)


def wedge2(M):
    n = len(M)
    idx = [(i, j) for i in range(n) for j in range(i + 1, n)]
    W = zeros(len(idx), len(idx))
    for a, (i, j) in enumerate(idx):
        for b, (k, m) in enumerate(idx):
            W[a][b] = M[i][k] * M[j][m] - M[i][m] * M[j][k]
    return W


def wedge_index(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def wedge_vec(u, v):
    """u ^ v in the basis e_i ^ e_j, i < j"""
    n = len(u)
    return [u[i] * v[j] - u[j] * v[i] for (i, j) in wedge_index(n)]


# ============================================================================================ groups and modules
class Group:
    def __init__(self, gens, rels, cusp, name=""):
        self.gens, self.rels, self.cusp, self.name = list(gens), list(rels), tuple(cusp), name


class Module:
    """matrices for the generators (lower case); a word is evaluated left to right, an upper-case letter is the inverse"""

    def __init__(self, gens, mats):
        self.gens = list(gens)
        self.M = {g: mats[g] for g in self.gens}
        self.d = len(self.M[self.gens[0]])
        self.Mi = {g: minv(self.M[g]) for g in self.gens}

    def mat_of(self, c):
        return self.M[c] if c.islower() else self.Mi[c.lower()]

    def word(self, w):
        X_ = eye(self.d)
        for c in w:
            X_ = mmul(X_, self.mat_of(c))
        return X_

    def dual(self):
        return Module(self.gens, {g: transpose(self.Mi[g]) for g in self.gens})

    def wedge2(self):
        return Module(self.gens, {g: wedge2(self.M[g]) for g in self.gens})

    def twist(self, chi):
        """chi (x) V, chi given by its values on the generators"""
        return Module(self.gens, {g: scal(self.M[g], chi[g]) for g in self.gens})

    def check(self, rels):
        return all(is_identity(self.word(r)) for r in rels)


def line(gens, chi):
    return Module(gens, {g: [[K.of(chi[g])]] for g in gens})


def fox_blocks(mod, w):
    """z(w) = sum_g Kb[g] z(g) for left cocycles; also the matrix of w"""
    d = mod.d
    Kb = {g: zeros(d, d) for g in mod.gens}
    P = eye(d)
    for c in w:
        g = c.lower()
        if c.islower():
            Kb[g] = madd(Kb[g], P)
            P = mmul(P, mod.M[g])
        else:
            P = mmul(P, mod.Mi[g])
            Kb[g] = madd(Kb[g], P, -1)
    return Kb, P


def cocycle_at(mod, z, w):
    """the value z(w) of the cocycle with generator values z (one vector of length d per generator, concatenated)"""
    Kb, _ = fox_blocks(mod, w)
    d = mod.d
    out = [ZERO] * d
    for gi, g in enumerate(mod.gens):
        zg = z[gi * d:(gi + 1) * d]
        out = [a + b for a, b in zip(out, mvec(Kb[g], zg))]
    return out


class Cohomology:
    """H^0, Z^1, B^1, H^1 representatives and the restriction to the cusp, for one module"""

    def __init__(self, G, mod):
        self.G, self.mod = G, mod
        d, gens = mod.d, G.gens
        assert gens == mod.gens
        self.d, self.ng = d, len(gens)
        rows = []
        for r in G.rels:
            Kb, P = fox_blocks(mod, r)
            assert is_identity(P), "a relator is not the identity in " + G.name
            for i in range(d):
                rows.append(sum((Kb[g][i] for g in gens), []))
        self.Z = nullspace(rows, d * self.ng)
        Id = eye(d)
        Dg = [madd(mod.M[g], Id, -1) for g in gens]
        self.a0 = d - rank(sum(Dg, []), d)
        self.Bvecs = [sum(([Dg[gi][i][j] for i in range(d)] for gi in range(self.ng)), []) for j in range(d)]
        self.dimB = rank_vectors(self.Bvecs, d * self.ng)
        assert self.dimB == d - self.a0
        self.h1 = len(self.Z) - self.dimB
        # H^1 representatives: extend a basis of B^1 to Z^1
        basis = []
        for v in self.Bvecs:
            if rank_vectors(basis + [v], d * self.ng) > len(basis):
                basis.append(v)
        self.reps = []
        for z in self.Z:
            if rank_vectors(basis + [z], d * self.ng) > len(basis):
                basis.append(z)
                self.reps.append(z)
        assert len(self.reps) == self.h1
        # the cusp
        self.Kp, self.Pm = [], []
        for p in G.cusp:
            Kb, P = fox_blocks(mod, p)
            self.Kp.append(Kb)
            self.Pm.append(P)
        Dp = [madd(P, Id, -1) for P in self.Pm]
        self.t0 = d - rank(sum(Dp, []), d)
        self.BP = [sum(([Dp[k][i][j] for i in range(d)] for k in range(len(Dp))), []) for j in range(d)]
        self.rBP = rank_vectors(self.BP, 2 * d)
        # Z^1(P): (u1, u2) with (P1 - 1) u2 = (P2 - 1) u1
        eq = [[-x for x in Dp[1][i]] + list(Dp[0][i]) for i in range(d)]
        self.h1P = len(nullspace(eq, 2 * d)) - self.rBP
        self.r1 = rank_vectors(self.BP + [self.restrict(z) for z in self.Z], 2 * d) - self.rBP
        self.n = self.h1 - self.r1

    def restrict(self, z):
        d = self.d
        out = []
        for Kb in self.Kp:
            v = [ZERO] * d
            for gi, g in enumerate(self.G.gens):
                v = [a + b for a, b in zip(v, mvec(Kb[g], z[gi * d:(gi + 1) * d]))]
            out += v
        return out

    def interior(self):
        """a basis of the interior classes (combinations of self.reps whose restriction lies in B^1(P)), as coefficient vectors"""
        d, k = self.d, len(self.reps)
        if k == 0:
            return []
        R = [self.restrict(z) for z in self.reps]
        # unknowns (x_1..x_k, v): sum x_i R_i - BP v = 0, BP v = ((P_j - 1) v)_j
        rows = []
        for r in range(2 * d):
            rows.append([R[i][r] for i in range(k)] + [-self.BP[j][r] for j in range(d)])
        sol = nullspace(rows, k + d)
        xs = []
        for s in sol:
            x = s[:k]
            if any(not c.is_zero() for c in x) and rank_vectors(xs + [x], k) > len(xs):
                xs.append(x)
        assert len(xs) == self.n, (len(xs), self.n)
        return xs

    def combine(self, x):
        """the cocycle sum x_i reps_i"""
        out = [ZERO] * (self.d * self.ng)
        for c, z in zip(x, self.reps):
            if not c.is_zero():
                out = [a + c * b for a, b in zip(out, z)]
        return out

    def is_coboundary(self, z):
        return in_span(z, self.Bvecs, self.d * self.ng)

    def coboundary_on_P(self, z):
        """a vector w with z(p) = (P - 1) w for both cusp generators, or None"""
        d = self.d
        r = self.restrict(z)
        rows = [[self.BP[j][i] for j in range(d)] + [-r[i]] for i in range(2 * d)]
        sol = nullspace(rows, d + 1)
        for s in sol:
            if not s[d].is_zero():
                return [x / s[d] for x in s[:d]]
        return None


def class_index(G, mod):
    A, B = Cohomology(G, mod), Cohomology(G, mod.dual())
    I = A.n - B.n
    a0, b0, t0, s0 = A.a0, B.a0, A.t0, B.t0
    checks = {
        "B1297 I = (a0 - b0) + s0 - r1": I == (a0 - b0) + s0 - A.r1,
        "annihilator r1 + r1* = t0 + s0 = h1(P)": A.r1 + B.r1 == t0 + s0 == A.h1P == B.h1P,
        "Lemma E I = h1* - h1 + 2(a0 - b0) + s0 - t0": I == B.h1 - A.h1 + 2 * (a0 - b0) + s0 - t0,
    }
    assert all(checks.values()), (G.name, checks, (a0, b0, t0, s0, A.h1, B.h1, A.r1, B.r1, A.h1P))
    return {"I": I, "a0": a0, "b0": b0, "t0": t0, "s0": s0, "h1": A.h1, "h1*": B.h1, "r1": A.r1, "r1*": B.r1,
            "n": A.n, "n*": B.n, "range (Proposition E)": [a0 - b0 - t0, a0 - b0 + s0]}


# ============================================================================================ extensions
def extension(V, c, L=None):
    """W1 = [[V, c L], [0, L]]: c a cocycle of V (x) L^-1 (values on the generators, concatenated); L a line (None: trivial)"""
    d = V.d
    mats = {}
    for gi, g in enumerate(V.gens):
        lg = L.M[g][0][0] if L is not None else ONE
        W = zeros(d + 1, d + 1)
        for i in range(d):
            for j in range(d):
                W[i][j] = V.M[g][i][j]
            W[i][d] = c[gi * d + i] * lg
        W[d][d] = lg
        mats[g] = W
    return Module(V.gens, mats)


# ============================================================================================ the mechanism
def fibre_C(V, phi_prime, tprime):
    """S0 on C = H^1(F; V|F) = V^2 / B^1(F), F = <a, b>, as a matrix on a complement of B^1(F); returns (S0 on C, the map
    V^2 -> C coordinates) so that the class of a cocycle's (z(a), z(b)) can be placed in C"""
    d = V.d
    Ff = Module(["a", "b"], {g: V.M[g] for g in "ab"})
    Vt_inv = minv(V.word(tprime))
    S = zeros(2 * d, 2 * d)
    for gi, g in enumerate("ab"):
        Kb, _ = fox_blocks(Ff, phi_prime[g])
        for hi, h in enumerate("ab"):
            blk = mmul(Vt_inv, Kb[h])
            for i in range(d):
                for j in range(d):
                    S[gi * d + i][hi * d + j] = blk[i][j]
    Id = eye(d)
    Bcols = transpose(madd(V.M["a"], Id, -1) + madd(V.M["b"], Id, -1))
    full = []
    for v in Bcols:
        if rank_vectors(full + [v], 2 * d) > len(full):
            full.append(v)
    m = len(full)
    for k in range(2 * d):
        e = [ONE if i == k else ZERO for i in range(2 * d)]
        if rank_vectors(full + [e], 2 * d) > len(full):
            full.append(e)
    P = transpose(full)
    Pi = minv(P)
    SP = mmul(mmul(Pi, S), P)
    for i in range(m, 2 * d):
        for j in range(m):
            assert SP[i][j].is_zero(), "B^1(F) is not S0-invariant"
    Q = [row[m:] for row in SP[m:]]
    coords = Pi[m:]                          # rows: V^2 -> the complement coordinates
    return Q, coords


def cup_with_fibration_class_vanishes(V, z, phi_prime, tprime):
    """x cup [z] = 0 in H^2(Gamma; V) iff the class of z|F in C lies in im(S0 - 1) (Wang)"""
    Q, coords = fibre_C(V, phi_prime, tprime)
    n = len(Q)
    zf = z[:2 * V.d]                          # the values on a and b (the generators are ordered a, b, t)
    cz = mvec(coords, zf)
    N = madd(Q, eye(n), -1)
    cols = transpose(N)
    return in_span(cz, cols, n), Q


def mu_test(G, V, c, L=None, y=None):
    """W1 = [[V, c L], [0, L]] with c an interior class of V_eta = V (x) L^-1 (so W1 splits on P: c(p) = (V(p) - 1) w; L is
    trivial on P), and y an interior class of V (x) L (default: y = c, the case L = 1).  Lambda^2 W1 has the submodule
    Lambda^2 V and the quotient V ^ e_d = V (x) L.  mu is the restriction to P of a lift of y to H^1(Lambda^2 W1), read in
    H^1(P; Lambda^2 V) after the splitting e_d' = e_d - w; it is defined modulo Lambda_A + B^1(P; Lambda^2 V), Lambda_A the
    restriction image of H^1(Gamma; Lambda^2 V).  Returns (mu in Lambda_A + B^1(P), dim Lambda_A, mu in B^1(P), y lifts)."""
    d = V.d
    Lv = {g: (L.M[g][0][0] if L is not None else ONE) for g in V.gens}
    Linv = {g: Lv[g].inv() for g in V.gens}
    Veta = V.twist(Linv) if L is not None else V
    VL = V.twist(Lv) if L is not None else V
    y = c if y is None else y
    for g in G.cusp:
        assert all((x == ONE) for x in sum(line(V.gens, Lv).word(g), [])), "L is not trivial on P"
    W1 = extension(V, c, L)
    L2W = W1.wedge2()
    CW, CL, CQ, CE = Cohomology(G, L2W), Cohomology(G, V.wedge2()), Cohomology(G, VL), Cohomology(G, Veta)
    idx = wedge_index(d + 1)
    sub = [a for a, (i, j) in enumerate(idx) if j < d]           # Lambda^2 V inside Lambda^2 W1
    quo = [a for a, (i, j) in enumerate(idx) if j == d]          # e_i ^ e_d, i = 0..d-1: the quotient V (x) L
    assert [idx[a][0] for a in quo] == list(range(d))
    dw, ng = L2W.d, len(G.gens)
    # a cocycle Z of Lambda^2 W1 whose quotient part is y + (a coboundary of V (x) L)
    rows = []
    for gi in range(ng):
        for i in range(d):
            r = [Zc[gi * dw + quo[i]] for Zc in CW.Z]
            r += [-CQ.Bvecs[j][gi * d + i] for j in range(d)]
            r += [-y[gi * d + i]]
            rows.append(r)
    sol = nullspace(rows, len(CW.Z) + d + 1)
    pick = next((s_ for s_ in sol if not s_[-1].is_zero()), None)
    if pick is None:
        return None, None, None, False
    coef = [x / pick[-1] for x in pick[:len(CW.Z)]]
    Zl = [ZERO] * (dw * ng)
    for k_, Zc in zip(coef, CW.Z):
        if not k_.is_zero():
            Zl = [a + k_ * b for a, b in zip(Zl, Zc)]
    w = CE.coboundary_on_P(c)
    assert w is not None, "c is not interior"
    # restrict Zl to P; e_i ^ e_d = e_i ^ e_d' + e_i ^ w
    mu, qvs = [], []
    for Kb in CW.Kp:
        val = [ZERO] * dw
        for gi, g in enumerate(G.gens):
            val = [a + b for a, b in zip(val, mvec(Kb[g], Zl[gi * dw:(gi + 1) * dw]))]
        qv = [val[a] for a in quo]
        lam_part = [val[a] for a in sub]
        mu += [a + b for a, b in zip(lam_part, wedge_vec(qv, w))]
        qvs += qv
    assert in_span(qvs, CQ.BP, 2 * d), "y is not interior: its quotient part is not a coboundary on P"
    LamA = [CL.restrict(z) for z in CL.Z]
    dimLamA = rank_vectors(CL.BP + LamA, 2 * CL.d) - CL.rBP
    in_lamA = in_span(mu, CL.BP + LamA, 2 * CL.d)
    is_cob = in_span(mu, CL.BP, 2 * CL.d)
    return in_lamA, dimLamA, is_cob, True
