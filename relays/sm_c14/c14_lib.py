"""SM-C14 -- m000 and its tick levels in F-HE: the SM seat's own Fox calculus over GF(p).  Library: nothing sealed is
computed on import.

The tick sigma: a -> ab, b -> a (det -1).  Level n: G_n = <a, b, t | t x t^-1 = sigma^n(x)>, x = a, b (B1926).
G_1 is m000, G_2 is m004, level 2k is m004's M_k.  Scar lam = [a, b] = abAB; meridian mu = g_n^-1 t with
sigma^n(lam) = g_n lam^((-1)^n) g_n^-1; the cusp group is <mu, lam | mu lam mu^-1 lam^(-(-1)^n)>.

The geometric four rho_1 (m000's hyperbolic holonomy, exact over Q(sqrt -3), complexified Minkowski model on 2x2 matrices):
  A = [[1 + z, 1], [-1, 0]], B = [[zb, -zb], [-zb, 1]], z = (1 + sqrt-3)/2, zb its conjugate;
  t acts by X -> M X^T M^*, M = [[-zb, 0], [zb, 1]];  a, b act by X -> G X G^*.
Words: lower case a generator, upper case its inverse."""
from fractions import Fraction as Fr
from itertools import product
from math import gcd

# ================================================================================================ words
GENS = ["a", "b", "t"]


def inv(w):
    return "".join(c.swapcase() for c in reversed(w))


def red(w):
    out = []
    for c in w:
        if out and out[-1] == c.swapcase():
            out.pop()
        else:
            out.append(c)
    return "".join(out)


SIGMA = {"a": "ab", "b": "a"}


def sigma(w, k=1):
    for _ in range(k):
        w = red("".join(SIGMA[c] if c.islower() else inv(SIGMA[c.lower()]) for c in w))
    return w


LAM = "abAB"


def level(n):
    """presentation of G_n with its peripheral words; asserts B1926's identity sigma^n(lam) = g lam^(+-1) g^-1"""
    g = ""
    for k in range(1, n + 1):
        g = red(sigma("a", k - 1) + g)
    e = 1 if n % 2 == 0 else -1
    lam_e = LAM if e == 1 else inv(LAM)
    assert red(sigma(LAM, n)) == red(g + lam_e + inv(g)), "B1926's scar identity"
    rels = [red("t" + x + "T" + inv(sigma(x, n))) for x in ("a", "b")]
    mu = red(inv(g) + "t")
    prel = red("ml" + "M" + ("L" if e == 1 else "l"))       # in the letters m (mu) and l (lam)
    return {"n": n, "rels": rels, "mu": mu, "lam": LAM, "prel": prel, "orientable": n % 2 == 0}


def ab_matrix(n):
    """the abelianised sigma^n on exponent vectors of (a, b), as columns"""
    sa, sb = sigma("a", n), sigma("b", n)
    ex = lambda w, g: w.count(g) - w.count(g.upper())
    return [[ex(sa, "a"), ex(sb, "a")], [ex(sa, "b"), ex(sb, "b")]]


def torsion_order(n):
    m = ab_matrix(n)
    return abs((m[0][0] - 1) * (m[1][1] - 1) - m[0][1] * m[1][0])


# ================================================================================================ GF(p)
def lcm(a, b):
    return a * b // gcd(a, b)


def is_prime(p):
    if p < 2:
        return False
    i = 2
    while i * i <= p:
        if p % i == 0:
            return False
        i += 1
    return True


def primes_for(K, count, start=10 ** 4):
    out, p = [], (start // K + 1) * K + 1
    while len(out) < count:
        if is_prime(p):
            out.append(p)
        p += K
    return out


def primitive_root_of_unity(K, p):
    assert (p - 1) % K == 0
    fac, m, d = [], K, 2
    while d * d <= m:
        if m % d == 0:
            fac.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        fac.append(m)
    for g in range(2, p):
        z = pow(g, (p - 1) // K, p)
        if all(pow(z, K // q, p) != 1 for q in fac):
            return z
    raise ValueError


def sqrt_mod(a, p):
    a %= p
    for x in range(p):
        if x * x % p == a:
            return x
    raise ValueError("no square root")


class GF:
    def __init__(self, p, K):
        self.p, self.K = p, K
        self.zK = primitive_root_of_unity(K, p)
        self.s3 = sqrt_mod(-3, p)                 # one embedding of sqrt -3

    def root(self, k):
        return pow(self.zK, k % self.K, self.p)

    def q3(self, u, v):
        """u + v sqrt-3 with u, v rational"""
        p = self.p
        f = lambda r: r.numerator * pow(r.denominator, p - 2, p) % p
        return (f(Fr(u)) + f(Fr(v)) * self.s3) % p


# --------------------------------------------------------------------------------------------- matrices mod p
def mmul(A, B, p):
    n, m, k = len(A), len(B), len(B[0])
    out = [[0] * k for _ in range(n)]
    for i in range(n):
        Ai, oi = A[i], out[i]
        for l in range(m):
            a = Ai[l]
            if a:
                Bl = B[l]
                for j in range(k):
                    oi[j] = (oi[j] + a * Bl[j]) % p
    return out


def eye(d):
    return [[1 if i == j else 0 for j in range(d)] for i in range(d)]


def madd(A, B, p, sgn=1):
    return [[(a + sgn * b) % p for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def mscale(A, c, p):
    return [[a * c % p for a in r] for r in A]


def rref(M, p):
    M = [r[:] for r in M]
    rows, cols = len(M), (len(M[0]) if M else 0)
    piv, r = [], 0
    for c in range(cols):
        k = next((i for i in range(r, rows) if M[i][c] % p), None)
        if k is None:
            continue
        M[r], M[k] = M[k], M[r]
        iv = pow(M[r][c], p - 2, p)
        M[r] = [x * iv % p for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(x - f * y) % p for x, y in zip(M[i], M[r])]
        piv.append(c)
        r += 1
        if r == rows:
            break
    return M[:r], piv


def rank(M, p):
    if not M or not M[0]:
        return 0
    return len(rref(M, p)[1])


def nullspace(M, ncols, p):
    """basis of {x : M x = 0} as a list of column vectors (lists)"""
    if not M:
        return [[1 if i == j else 0 for i in range(ncols)] for j in range(ncols)]
    R, piv = rref(M, p)
    free = [c for c in range(ncols) if c not in piv]
    out = []
    for f in free:
        v = [0] * ncols
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-R[i][f]) % p
        out.append(v)
    return out


def minv(A, p):
    d = len(A)
    R, piv = rref([A[i] + eye(d)[i] for i in range(d)], p)
    assert piv[:d] == list(range(d)), "singular"
    return [r[d:] for r in R]


def det(A, p):
    A = [r[:] for r in A]
    d, s = len(A), 1
    for c in range(d):
        k = next((i for i in range(c, d) if A[i][c] % p), None)
        if k is None:
            return 0
        if k != c:
            A[c], A[k] = A[k], A[c]
            s = -s
        s = s * A[c][c] % p
        iv = pow(A[c][c], p - 2, p)
        for i in range(c + 1, d):
            if A[i][c]:
                f = A[i][c] * iv % p
                A[i] = [(x - f * y) % p for x, y in zip(A[i], A[c])]
    return s % p


def transpose(A):
    return [list(r) for r in zip(*A)]


def kron(A, B, p):
    return [[a * b % p for a in ra for b in rb] for ra in A for rb in B]


# ================================================================================================ representations
class Rep:
    """gen -> d x d matrix over GF(p); inverses cached"""

    def __init__(self, F, mats):
        self.F, self.p = F, F.p
        self.M = dict(mats)
        self.gens = [g for g in mats if g.islower()]
        self.d = len(next(iter(mats.values())))
        for g in list(mats):
            self.M[g.upper()] = minv(mats[g], self.p)

    def word(self, w):
        out = eye(self.d)
        for c in w:
            out = mmul(out, self.M[c], self.p)
        return out

    def fox(self, w):
        """{g: d(w)/dg} for the generators g of this rep (rho applied)"""
        p, d = self.p, self.d
        D = {g: [[0] * d for _ in range(d)] for g in self.M if g.islower()}
        pref = eye(d)
        for c in w:
            g = c.lower()
            if c.islower():
                D[g] = madd(D[g], pref, p)
                pref = mmul(pref, self.M[c], p)
            else:
                pref = mmul(pref, self.M[c], p)
                D[g] = madd(D[g], pref, p, -1)
        return D

    def check(self, rels):
        return all(self.word(r) == eye(self.d) for r in rels)

    def dual(self):
        return Rep(self.F, {g: transpose(minv(self.M[g], self.p)) for g in self.M if g.islower()})

    def tensor_char(self, chi):
        """V (x) chi, chi: gen -> GF(p) value"""
        return Rep(self.F, {g: mscale(self.M[g], chi[g], self.p) for g in self.M if g.islower()})


def char_rep(F, vals):
    return Rep(F, {g: [[v % F.p]] for g, v in vals.items()})


def wedge2(A, p):
    d = len(A)
    idx = [(i, j) for i in range(d) for j in range(i + 1, d)]
    return [[(A[i][k] * A[j][l] - A[i][l] * A[j][k]) % p for (k, l) in idx] for (i, j) in idx]


def sym2(A, p):
    """on the basis e_i e_j (i <= j): (A e_k)(A e_l)"""
    d = len(A)
    idx = [(i, j) for i in range(d) for j in range(i, d)]
    pos = {ij: n for n, ij in enumerate(idx)}
    out = [[0] * len(idx) for _ in idx]
    for c, (k, l) in enumerate(idx):
        for i in range(d):
            for j in range(d):
                v = A[i][k] * A[j][l] % p
                if v:
                    key = (i, j) if i <= j else (j, i)
                    out[pos[key]][c] = (out[pos[key]][c] + v) % p
    return out


def rep_apply(R, f):
    return Rep(R.F, {g: f(R.M[g], R.p) for g in R.M if g.islower()})


def ext_with_line(V, coc, L):
    """W = [[V, c L], [0, L]], c a cocycle of V (x) L^-1 given on the generators as a dict"""
    p, d = V.p, V.d
    out = {}
    for g in V.M:
        if not g.islower():
            continue
        lv = L.M[g][0][0]
        col = [coc[g][i] * lv % p for i in range(d)]
        out[g] = [V.M[g][i] + [col[i]] for i in range(d)] + [[0] * d + [lv]]
    return Rep(V.F, out)


# ================================================================================================ the geometric four
def q3_mat(F, M):
    return [[F.q3(*e) for e in r] for r in M]


def conj3(M):
    return [[(u, -v) for (u, v) in r] for r in M]


H = Fr(1, 2)
Z6 = (H, H)        # (1 + sqrt-3)/2
Z6B = (H, -H)
NEG = lambda e: (-e[0], -e[1])
A_SL2 = [[(1 + Z6[0], Z6[1]), (1, 0)], [(-1, 0), (0, 0)]]
B_SL2 = [[Z6B, NEG(Z6B)], [NEG(Z6B), (1, 0)]]
M_SL2 = [[NEG(Z6B), (0, 0)], [Z6B, (1, 0)]]
TRANSPOSE4 = [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]    # X -> X^T on (x11, x12, x21, x22)


def minkowski(F, G, anti=False):
    """X -> G X G^* (or G X^T G^*) on row-major vec(X): G (x) conj(G), times the transpose if anti"""
    K = kron(q3_mat(F, G), q3_mat(F, conj3(G)), F.p)
    return mmul(K, TRANSPOSE4, F.p) if anti else K


def rho1_m000(F):
    return {"a": minkowski(F, A_SL2), "b": minkowski(F, B_SL2), "t": minkowski(F, M_SL2, anti=True)}


def mpow(A, n, p):
    out = eye(len(A))
    for _ in range(n):
        out = mmul(out, A, p)
    return out


def rho1(F, n):
    r = rho1_m000(F)
    return Rep(F, {"a": r["a"], "b": r["b"], "t": mpow(r["t"], n, F.p)})


def w_char(F, n):
    return {"a": 1, "b": 1, "t": (-1) ** n % F.p}


# ================================================================================================ cohomology
def d1_matrix(R, rels):
    rows = []
    for r in rels:
        D = R.fox(r)
        blk = [sum((D[g][i] for g in R.gens), []) for i in range(R.d)]
        rows.extend(blk)
    return rows


def cohomology(R, rels):
    """(h0, Z1 basis as dicts gen -> vector, rank of B1, h1)"""
    p, d = R.p, R.d
    d0 = sum(([madd(R.M[g], eye(d), p, -1)[i] for i in range(d)] for g in R.gens), [])
    rk0 = rank(d0, p)
    Z = nullspace(d1_matrix(R, rels), len(R.gens) * d, p)
    Zd = [{g: z[k * d:(k + 1) * d] for k, g in enumerate(R.gens)} for z in Z]
    return d - rk0, Zd, rk0, len(Z) - rk0


def coboundary(R, v):
    p, d = R.p, R.d
    return {g: [(sum(R.M[g][i][j] * v[j] for j in range(d)) - v[i]) % p for i in range(d)] for g in R.gens}


def h1_classes(R, rels):
    """a basis of classes (cocycles independent modulo coboundaries)"""
    p, d = R.p, R.d
    _, Z, rk0, h1 = cohomology(R, rels)
    B = [sum((coboundary(R, [1 if i == j else 0 for i in range(d)])[g] for g in R.gens), []) for j in range(d)]
    cur = [b for b in B]
    base = rank(cur, p) if cur else 0
    out = []
    for z in Z:
        vec = sum((z[g] for g in R.gens), [])
        if rank(cur + [vec], p) > base:
            cur.append(vec)
            base += 1
            out.append(z)
    assert len(out) == h1
    return out


def restrict(R, z, word):
    """z(word) by Fox calculus"""
    p, d = R.p, R.d
    D = R.fox(word)
    out = [0] * d
    for g in R.gens:
        for i in range(d):
            out[i] = (out[i] + sum(D[g][i][j] * z[g][j] for j in range(d))) % p
    return out


def peripheral(R, lev):
    """h1(P; R), the rank r1 of H^1(G; R) -> H^1(P; R), and h0(P; R), on the torus or the Klein bottle"""
    p, d = R.p, R.d
    Mu, La = R.word(lev["mu"]), R.word(lev["lam"])
    P = Rep(R.F, {"m": Mu, "l": La})
    D = P.fox(lev["prel"])
    ZP = [D["m"][i] + D["l"][i] for i in range(d)]
    zp = len(nullspace(ZP, 2 * d, p))
    BP = [madd(Mu, eye(d), p, -1)[i] for i in range(d)] + [madd(La, eye(d), p, -1)[i] for i in range(d)]
    rkBP = rank(transpose(BP), p) if d else 0
    h0P = d - rkBP
    h1P = zp - rkBP
    _, Z, rk0, h1 = cohomology(R, lev["rels"])
    bp_vecs = transpose(BP)                              # d vectors of length 2d: the coboundaries of P
    cols = [restrict(R, z, lev["mu"]) + restrict(R, z, lev["lam"]) for z in Z]
    r1 = rank(bp_vecs + cols, p) - rkBP if cols else 0
    return {"h0P": h0P, "h1P": h1P, "r1": r1, "h1": h1, "h0": d - rk0, "n": h1 - r1}


def peripheral_torus_formula(R, lev):
    """plant P3: the torus cocycle condition used whatever the cusp is"""
    lev2 = dict(lev, prel="mlML")
    return peripheral(R, lev2)
