"""Route F -- an independent re-derivation of the frame's counts (I(W), I(L2W)) at classes of H^1(N; rho), for the audit that
NO NEGATIVE FROM A BUG (WORKING_RULES 2026-10-01) requires before a NEGATIVE is banked, and the load-bearing rule of 2026-10-06.

Separate code.  It imports numpy and the standard library only: nothing from sm:B1536's routes or libraries, sm:B1530's exact
library, sm:B1527's family library, this arc's n45.py, PARI or FLINT (a lock asserts this).  What it takes as data, and checks
itself before using:
  - the state's presentation <a, b, t | r0, r1> with its cusp words (l, t');
  - the holonomy: three 2 x 2 matrices with entries in Q(zeta_24), as coefficient vectors on 1, zeta, ..., zeta^7;
  - the cover: the permutation action of a, b, t on X (x^g, a right action) and the deck permutation tau.

A different method: a second presentation.  The generator b is eliminated by r0 (Tietze), so the state is <a, t | R> with one
relator, and the cover is read on the lifted presentation complex of that two-generator presentation: vertices X, edges (x, g)
for g in {a, t}, faces (x, R).  A local system is a transport matrix on each edge.  rho itself is carried in the base gauge (the
matrix of g on every edge labelled g), and W = [[rho, z], [0, 1]] carries a 1-cocycle z of the complex on its corner.  No Schreier
tree and no rewriting is used.
  - H^1 = ker d1 / im d0, with (d0 f)(x, g) = A(x, g) f(x^g) - f(x) and (d1 psi)(x, R) the transported sum of psi along R from x.
  - n(E) = h1(E) - r1(E): r1 is the rank of the joint restriction to the cusps, each cusp T read on two loops m1, m2 at a point of
    T that generate T's stabiliser lattice in <l, t'> (computed here by a Hermite normal form), modulo the cusp's coboundaries
    ((H1 - 1) v, (H2 - 1) v).
  - I(E) = n(E) - n(E*), E* with transports (A^-1)^T; Lambda^2 by own minors.
The four: rho(g) H = g H g^* / |det g| on Hermitian H in the coordinates (x1, x2, x3, x4) of [[x1, x3 + i x4], [x3 - i x4, x2]],
computed mod p from the exact entries (|det g| from the exact norm, by its square class).
Arithmetic: own Gaussian elimination mod p, at primes p = 1 mod 120 in (2^25, 2^26), so that every product of two residues and
every short sum of them fits int64 exactly."""
from fractions import Fraction
from math import gcd, isqrt

import numpy as np

DEG = 8                                   # [Q(zeta_24) : Q]; zeta^8 = zeta^4 - 1


# ============================================================================================ words
def inv_word(w):
    return "".join(c.swapcase() for c in reversed(w))


def free_reduce(w):
    out = []
    for c in w:
        if out and out[-1] == c.swapcase():
            out.pop()
        else:
            out.append(c)
    return "".join(out)


def substitute(w, sub):
    """replace each letter by its word (inverse letters by the inverse word) and reduce"""
    out = []
    for c in w:
        lo = c.lower()
        if lo in sub:
            out.append(sub[lo] if c.islower() else inv_word(sub[lo]))
        else:
            out.append(c)
    return free_reduce("".join(out))


def eliminate(rel, x):
    """the word for generator x from a relator containing x exactly once: rel = u x^e v = 1 gives x^e = u^-1 v^-1"""
    pos = [i for i, c in enumerate(rel) if c.lower() == x]
    assert len(pos) == 1, ("the relator does not contain the generator exactly once", rel, x)
    i = pos[0]
    u, v = rel[:i], rel[i + 1:]
    w = free_reduce(inv_word(u) + inv_word(v))
    return w if rel[i] == x else inv_word(w)


def act(perms, w, x):
    """x^w for the right action; perms has every generator and its inverse"""
    for c in w:
        x = perms[c][x]
    return x


def with_inverses(perms):
    out = {}
    for g, p in perms.items():
        out[g] = list(p)
        q = [0] * len(p)
        for i, y in enumerate(p):
            q[y] = i
        out[g.upper()] = q
    return out


# ============================================================================================ exact Q(zeta_24), for norms
def _qmul(a, b):
    conv = [Fraction(0)] * (2 * DEG - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    conv[i + j] += x * y
    for k in range(2 * DEG - 2, DEG - 1, -1):          # zeta^8 = zeta^4 - 1
        v = conv[k]
        if v:
            conv[k - 4] += v
            conv[k - 8] -= v
            conv[k] = Fraction(0)
    return conv[:DEG]


def _power_basis():
    """zeta^m on the basis 1, ..., zeta^7, m = 0..23"""
    out, cur = [], [Fraction(1)] + [Fraction(0)] * (DEG - 1)
    z = [Fraction(0), Fraction(1)] + [Fraction(0)] * (DEG - 2)
    for _ in range(24):
        out.append(cur)
        cur = _qmul(cur, z)
    return out


_ZP = _power_basis()


def _qconj(a):
    """zeta -> zeta^-1 = zeta^23"""
    out = [Fraction(0)] * DEG
    for i, x in enumerate(a):
        if x:
            v = _ZP[(23 * i) % 24]
            for j in range(DEG):
                out[j] += x * v[j]
    return out


def _qsub(a, b):
    return [x - y for x, y in zip(a, b)]


# the square roots in Q(zeta_24): sqrt2 = zeta^3 + zeta^21, sqrt3 = zeta^2 + zeta^22 (both positive reals)
_SQRT = {1: [Fraction(1)] + [Fraction(0)] * (DEG - 1),
         2: [a + b for a, b in zip(_ZP[3], _ZP[21])],
         3: [a + b for a, b in zip(_ZP[2], _ZP[22])]}
_SQRT[6] = _qmul(_SQRT[2], _SQRT[3])


def abs_det(m):
    """|det m| for a 2 x 2 matrix over Q(zeta_24) given exactly, as an element of Q(zeta_24): sqrt(det conj(det)), the norm
    being rational and its square class 1, 2, 3 or 6 (asserted)"""
    d = _qsub(_qmul(m[0][0], m[1][1]), _qmul(m[0][1], m[1][0]))
    nrm = _qmul(d, _qconj(d))
    assert all(x == 0 for x in nrm[1:]) and nrm[0] > 0, "the norm of det is not a positive rational"
    q = nrm[0]
    for s in (1, 2, 3, 6):
        r = q / s
        a, b = isqrt(r.numerator), isqrt(r.denominator)
        if a * a == r.numerator and b * b == r.denominator:
            return [Fraction(a, b) * x for x in _SQRT[s]]
    raise AssertionError(("the norm's square class is not 1, 2, 3 or 6", q))


# ============================================================================================ arithmetic mod p
def primes(count, lo=1 << 25, hi=1 << 26, mod=120):
    """the largest primes p = 1 mod `mod` below hi (and above lo)"""
    out, p = [], hi - 1
    p -= (p - 1) % mod
    while len(out) < count and p > lo:
        if p > 1 and all(p % q for q in range(2, isqrt(p) + 1)):
            out.append(p)
        p -= mod
    assert len(out) == count
    return out


def root_of_order(p, k):
    """the root of unity of order exactly k mod p with the smallest base a (z = a^((p-1)/k))"""
    assert (p - 1) % k == 0
    fac = [q for q in range(2, k + 1) if k % q == 0 and all(q % r for r in range(2, q))]
    for a in range(2, p):
        z = pow(a, (p - 1) // k, p)
        if all(pow(z, k // q, p) != 1 for q in fac):
            return z
    raise ValueError((p, k))


def to_p(x, z, p):
    """an element of Q(zeta_24) (eight Fractions) mod p, zeta -> z"""
    v = 0
    for i, c in enumerate(x):
        if c:
            v = (v + (c.numerator % p) * pow(c.denominator, -1, p) % p * pow(z, i, p)) % p
    return v


def mm(A, B, p):
    """A B mod p, exact: residues below 2^26, so each product is below 2^52; the inner sum is taken in chunks of 512"""
    A, B = np.asarray(A, dtype=np.int64) % p, np.asarray(B, dtype=np.int64) % p
    n = A.shape[1]
    out = np.zeros((A.shape[0], B.shape[1]), dtype=np.int64)
    for s in range(0, n, 512):
        out = (out + A[:, s:s + 512] @ B[s:s + 512, :]) % p
    return out


def rref(M, p):
    """reduced row echelon form mod p: (R, pivot columns)"""
    A = np.array(M, dtype=np.int64) % p
    rows, cols = A.shape
    piv, r = [], 0
    for c in range(cols):
        if r == rows:
            break
        nz = np.nonzero(A[r:, c])[0]
        if len(nz) == 0:
            continue
        i = r + nz[0]
        if i != r:
            A[[r, i]] = A[[i, r]]
        A[r] = A[r] * pow(int(A[r, c]), -1, p) % p
        col = A[:, c].copy()
        col[r] = 0
        nzr = np.nonzero(col)[0]
        if len(nzr):
            A[nzr] = (A[nzr] - (col[nzr, None] * A[r][None, :]) % p) % p
        piv.append(c)
        r += 1
    return A[:r], piv


def rank(M, p):
    M = np.asarray(M)
    if M.size == 0:
        return 0
    return len(rref(M, p)[1])


def nullspace(M, p):
    """a basis of {v : M v = 0 mod p}, as the columns of the returned matrix"""
    M = np.asarray(M, dtype=np.int64)
    n = M.shape[1]
    if M.shape[0] == 0:
        return np.eye(n, dtype=np.int64)
    R, piv = rref(M, p)
    free = [c for c in range(n) if c not in set(piv)]
    out = np.zeros((n, len(free)), dtype=np.int64)
    for k, f in enumerate(free):
        out[f, k] = 1
        for i, c in enumerate(piv):
            out[c, k] = (-R[i, f]) % p
    return out


def minv(A, p):
    A = np.asarray(A, dtype=np.int64) % p
    n = A.shape[0]
    R, piv = rref(np.hstack([A, np.eye(n, dtype=np.int64)]), p)
    assert piv[:n] == list(range(n)), "singular"
    return R[:n, n:] % p


def wedge2(A, p):
    """Lambda^2 A on the basis e_i ^ e_j (i < j), by 2 x 2 minors"""
    n = A.shape[0]
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    out = np.zeros((len(pairs), len(pairs)), dtype=np.int64)
    for c, (k, l) in enumerate(pairs):
        for r, (i, j) in enumerate(pairs):
            out[r, c] = (A[i, k] * A[j, l] - A[i, l] * A[j, k]) % p
    return out


# ============================================================================================ the state and the four
class State:
    """the two-generator presentation <a, t | R> of a state given as <a, b, t | r0, r1> (b eliminated by r0), its cusp words,
    and the four mod p"""

    def __init__(self, data):
        gens, rels, (l, tp) = data["gens"], data["rels"], data["cusp"]
        assert list(gens) == ["a", "b", "t"] and len(rels) == 2
        self.b_word = eliminate(rels[0], "b")
        self.R = substitute(rels[1], {"b": self.b_word})
        self.cusp = (substitute(l, {"b": self.b_word}), substitute(tp, {"b": self.b_word}))
        self.gens = ["a", "t"]
        self.hol = {g: [[[Fraction(c) for c in data["holonomy"][g][i][j]] for j in range(2)] for i in range(2)]
                    for g in "abt"}
        self.absdet = {g: abs_det(self.hol[g]) for g in "abt"}

    def four(self, p, z):
        """the four's matrices for a, b, t mod p (zeta_24 -> z): rho(g) H = g H g^* / |det g|"""
        zi = pow(z, -1, p)
        iu = pow(z, 6, p)                                     # i = zeta^6
        out = {}
        for g in "abt":
            m = [[to_p(self.hol[g][i][j], z, p) for j in range(2)] for i in range(2)]
            mc = [[to_p(self.hol[g][j][i], zi, p) for j in range(2)] for i in range(2)]     # conjugate transpose
            ad = pow(to_p(self.absdet[g], z, p), -1, p)
            basis = [[[1, 0], [0, 0]], [[0, 0], [0, 1]], [[0, 1], [1, 0]], [[0, iu], [(-iu) % p, 0]]]
            cols = []
            for H in basis:
                Hn = mm(mm(m, H, p), mc, p) * ad % p
                x3 = (Hn[0, 1] + Hn[1, 0]) * pow(2, -1, p) % p
                x4 = (Hn[0, 1] - Hn[1, 0]) * pow(2 * iu, -1, p) % p
                cols.append([Hn[0, 0], Hn[1, 1], x3, x4])
            out[g] = np.array(cols, dtype=np.int64).T % p
        return out

    def word_matrix(self, mats, w, p):
        e = next(iter(mats.values())).shape[0]
        inv = {g: minv(mats[g], p) for g in mats}
        M = np.eye(e, dtype=np.int64)
        for c in w:
            M = mm(M, mats[c] if c.islower() else inv[c.lower()], p)
        return M

    def checks(self, mats, p):
        """the four is a representation of <a, t | R>, agrees with b's matrix on b's word, and is unipotent on the cusp"""
        I4 = np.eye(4, dtype=np.int64)
        out = {"R is 1": bool(np.array_equal(self.word_matrix(mats, self.R, p), I4)),
               "b is its word": bool(np.array_equal(self.word_matrix(mats, self.b_word, p), mats["b"] % p))}
        P1, P2 = (self.word_matrix(mats, w, p) for w in self.cusp)
        out["the cusp words commute"] = bool(np.array_equal(mm(P1, P2, p), mm(P2, P1, p)))
        for nm, P in (("l", P1), ("t'", P2)):
            D = (P - I4) % p
            out[nm + " unipotent, not 1"] = bool(not np.any(mm(mm(D, D, p), D, p)) and np.any(D))
        return out


# ============================================================================================ the cover
class Cover:
    """the lifted presentation complex of <a, t | R> on X: edges (x, g), faces (x, R); the cusps as loops"""

    def __init__(self, state, perms):
        self.S = state
        self.d = len(perms["a"])
        P = with_inverses({g: perms[g] for g in ("a", "b", "t")})
        assert all(act(P, state.R, x) == x for x in range(self.d)), "R does not act trivially"
        assert all(act(P, state.b_word, x) == P["b"][x] for x in range(self.d)), "b's permutation is not its word's"
        self.P = {g: P[g] for g in ("a", "A", "t", "T")}
        self.gens = ["a", "t"]
        self.cusps = self._cusps()

    def edge(self, x, g):
        return x * 2 + self.gens.index(g)

    def _cusps(self):
        """orbits of <l, t'> on X; for each, a point, its orbit, and two loop words generating its stabiliser lattice"""
        l, tp = self.S.cusp
        moves = ((l, (1, 0)), (inv_word(l), (-1, 0)), (tp, (0, 1)), (inv_word(tp), (0, -1)))
        out, done = [], set()
        for x in range(self.d):
            if x in done:
                continue
            coord, todo, rel = {x: (0, 0)}, [x], []
            while todo:
                y = todo.pop()
                for w, (di, dj) in moves:
                    zz = act(self.P, w, y)
                    c = (coord[y][0] + di, coord[y][1] + dj)
                    if zz in coord:
                        if coord[zz] != c:
                            rel.append((c[0] - coord[zz][0], c[1] - coord[zz][1]))
                    else:
                        coord[zz] = c
                        todo.append(zz)
            basis = _hnf2(rel)
            assert abs(basis[0][0] * basis[1][1] - basis[0][1] * basis[1][0]) == len(coord), "orbit size != lattice index"
            words = []
            for (i, j) in basis:
                w = (l * i if i >= 0 else inv_word(l) * (-i)) + (tp * j if j >= 0 else inv_word(tp) * (-j))
                assert act(self.P, w, x) == x
                words.append(w)
            out.append({"x": x, "orbit": sorted(coord), "loops": words})
            done |= set(coord)
        return out


def _hnf2(vectors):
    """a basis ((a, b), (0, c)) of the lattice in Z^2 spanned by the vectors, a, c > 0 and 0 <= b < c (own Hermite form)"""
    rows = [[int(v[0]), int(v[1])] for v in vectors if (v[0], v[1]) != (0, 0)]
    while sum(1 for r in rows if r[0]) > 1:                    # Euclid on the first coordinates, by unimodular row steps
        i = min((k for k, r in enumerate(rows) if r[0]), key=lambda k: abs(rows[k][0]))
        a0, b0 = rows[i]
        for k, r in enumerate(rows):
            if k != i and r[0]:
                q = r[0] // a0
                rows[k] = [r[0] - q * a0, r[1] - q * b0]
    first = [r for r in rows if r[0]]
    assert len(first) == 1, "the lattice has rank below two"
    a, b = first[0]
    if a < 0:
        a, b = -a, -b
    c = 0
    for r in rows:
        if not r[0]:
            c = gcd(c, abs(r[1]))
    assert c > 0, "the lattice has rank below two"
    return [(a, b % c), (0, c)]


# ============================================================================================ cohomology of a local system
class Coh:
    """H^0, H^1 and the interior supply n = h1 - r1 of the local system with transports A[(x, g)] (e x e) on the cover"""

    def __init__(self, cov, A, p, keep=False):
        d, e = cov.d, next(iter(A.values())).shape[0]
        self.e = e
        nE = 2 * d                                          # edges
        Ainv = {k: minv(v, p) for k, v in A.items()}
        D0 = np.zeros((e * nE, e * d), dtype=np.int64)
        for x in range(d):
            for g in cov.gens:
                r = cov.edge(x, g) * e
                y = cov.P[g][x]
                D0[r:r + e, y * e:(y + 1) * e] = (D0[r:r + e, y * e:(y + 1) * e] + A[(x, g)]) % p
                D0[r:r + e, x * e:(x + 1) * e] = (D0[r:r + e, x * e:(x + 1) * e] - np.eye(e, dtype=np.int64)) % p
        D1 = np.zeros((e * d, e * nE), dtype=np.int64)
        for x in range(d):
            row, _ = self.path_row(cov, A, Ainv, cov.S.R, x, p)
            D1[x * e:(x + 1) * e, :] = row
        assert not np.any(mm(D1, D0, p)), "d1 d0 != 0"
        rD0 = rank(D0, p)
        self.a0 = e * d - rD0
        Z = nullspace(D1, p)
        self.h1 = Z.shape[1] - rD0
        Rs, BPs = [], []
        for T in cov.cusps:
            rows, Hs = [], []
            for w in T["loops"]:
                row, H = self.path_row(cov, A, Ainv, w, T["x"], p)
                rows.append(row)
                Hs.append((H - np.eye(e, dtype=np.int64)) % p)
            Rs.append(np.vstack(rows))
            BPs.append(np.vstack(Hs))
        nc = len(cov.cusps)
        R = np.vstack(Rs)
        BP = np.zeros((2 * e * nc, e * nc), dtype=np.int64)
        for i, b in enumerate(BPs):
            BP[2 * e * i:2 * e * (i + 1), e * i:e * (i + 1)] = b
        rBP = rank(BP, p)
        RZ = mm(R, Z, p)
        self.r1 = rank(np.hstack([BP, RZ]), p) - rBP
        self.n = self.h1 - self.r1
        if keep:
            self.Z, self.D0, self.R, self.BP = Z, D0, R, BP

    @staticmethod
    def path_row(cov, A, Ainv, w, x, p):
        """the e x (e * edges) matrix giving psi's transported sum along the word w read from x, and the transport around it"""
        e = next(iter(A.values())).shape[0]
        row = np.zeros((e, e * 2 * cov.d), dtype=np.int64)
        Pre = np.eye(e, dtype=np.int64)
        y = x
        for c in w:
            g = c.lower()
            if c.islower():
                k = cov.edge(y, g) * e
                row[:, k:k + e] = (row[:, k:k + e] + Pre) % p
                Pre = mm(Pre, A[(y, g)], p)
                y = cov.P[g][y]
            else:
                y2 = cov.P[g.upper()][y]                    # y2^g = y
                Pre = mm(Pre, Ainv[(y2, g)], p)
                k = cov.edge(y2, g) * e
                row[:, k:k + e] = (row[:, k:k + e] - Pre) % p
                y = y2
        return row, Pre


def base_system(cov, mats):
    """rho in the base gauge: the matrix of g on every edge labelled g"""
    return {(x, g): mats[g] for x in range(cov.d) for g in cov.gens}


def deck(z, tau, d, e):
    """(tau psi)(x, g) = psi(tau^-1 x, g) on a 1-cochain of the base-gauge system"""
    out = np.zeros_like(z)
    for x in range(d):
        tx = tau[x]
        for gi in range(2):
            out[(tx * 2 + gi) * e:(tx * 2 + gi + 1) * e] = z[(x * 2 + gi) * e:(x * 2 + gi + 1) * e]
    return out


def project(z, tau, d, e, j, k, zk, p):
    """(1/k) sum_i zk^(-j i) tau^i z"""
    out = np.zeros_like(z)
    cur = z % p
    for i in range(k):
        out = (out + pow(zk, (-j * i) % k, p) * cur) % p
        cur = deck(cur, tau, d, e)
    return out * pow(k, -1, p) % p


def count(cov, mats, z, p):
    """(I(W), I(L2W)) at the class of the 1-cocycle z of the base-gauge four (trivial character)"""
    A = {}
    for x in range(cov.d):
        for gi, g in enumerate(cov.gens):
            W = np.zeros((5, 5), dtype=np.int64)
            W[:4, :4] = mats[g]
            W[:4, 4] = z[(x * 2 + gi) * 4:(x * 2 + gi + 1) * 4]
            W[4, 4] = 1
            A[(x, g)] = W % p
    As = {k: minv(v, p).T.copy() for k, v in A.items()}
    L2 = {k: wedge2(v, p) for k, v in A.items()}
    L2s = {k: wedge2(v, p) for k, v in As.items()}
    n = {nm: Coh(cov, sys_, p).n for nm, sys_ in (("W", A), ("W*", As), ("L2", L2), ("L2*", L2s))}
    return [n["W"] - n["W*"], n["L2"] - n["L2*"]], n
