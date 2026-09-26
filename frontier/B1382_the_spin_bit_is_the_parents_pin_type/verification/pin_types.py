#!/usr/bin/env python3
"""B1382 -- THE SPIN BIT IS THE PARENT'S PIN TYPE.  B1141 (T-SPIN-PAYMENT) found that the Gieseking beat extends over
exactly one of m004's two spin structures, and read it as "the last free discrete bit is assigned, not free".  B1175
harvested codex R021 (the Gieseking's Pin- structures all restrict to ONE spin structure) and queued the residual:
identify R021's image with B1141's lift ("needs a tangent-frame Pin- lift + the holonomy-convention comparison").
This does the comparison, in exact arithmetic over Q(w), w = e^(2 pi i/3).

The two double covers of Isom(H^3) = PSL(2,C) x| <c> (c = complex conjugation, an orientation-reversing isometry):
  G_eps = { (M, k) : M in SL(2,C), k in {0,1} },   (M1,k1)(M2,k2) = (M1 . conj^k1(M2) . eps^(k1 k2), k1 + k2 mod 2).
A reflection through a point lifts with square eps, so G_eps restricted to a point stabiliser O(3) is Pin^eps(3)
(Pin+ : reflections lift to involutions, obstructed by w2; Pin- : to elements of order 4, obstructed by w2 + w1^2).
A Pin^eps structure on N = Gamma\H^3 is a lift of Gamma to G_eps (the frame bundle of N is Gamma\Isom(H^3)).

Sections (each asserts; record pin_types_run.txt):
  S1 B1141's holonomy of m004 (A = [[1,1],[0,1]], B = [[1,0],[-w,1]]), the relator census, the beat
  S2 the intertwiner W conj(g) W^-1 = rho(beat g): exactly one-dimensional (exact rank over Q(w)); W conj(W) = mu' A with
     mu'^2 = |det W|^2, so the det-1 normalisation W0 = W/sqrt(det W) has W0 conj(W0) = sign(mu') A
  S3 G_eps: associativity, the centre, and reflections through j lifting with square eps (the tangent-frame reading)
  S4 the table: which spin lift extends to which G_eps -- every Gieseking relation checked (conjugations exactly with W;
     the square through the exact sign)
  S5 topology: H1(Gieseking) = Z, chi = 0 => H2(N; Z/2) = 0, so both Pin types exist, two each; p* = 0 on H^1(-;Z/2)
  S6 the lifts named by their cusp traces (meridian a; a longitude found by search), matching B921-6's rho_1, rho_2
Usage: python3 pin_types.py"""
import itertools
from fractions import Fraction as Fr


class Qw:
    """a + b w in Q(w), w^2 = -1 - w."""
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a, self.b = Fr(a), Fr(b)

    def __add__(self, o):
        o = o if isinstance(o, Qw) else Qw(o)
        return Qw(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self):
        return Qw(-self.a, -self.b)

    def __sub__(self, o):
        return self + (-(o if isinstance(o, Qw) else Qw(o)))

    def __mul__(self, o):
        o = o if isinstance(o, Qw) else Qw(o)
        return Qw(self.a * o.a - self.b * o.b, self.a * o.b + self.b * o.a - self.b * o.b)

    __rmul__ = __mul__

    def conj(self):                       # conj(w) = w^2 = -1 - w
        return Qw(self.a - self.b, -self.b)

    def norm(self):                       # |x|^2 = a^2 - a b + b^2 (rational, positive definite)
        return self.a * self.a - self.a * self.b + self.b * self.b

    def inv(self):
        n = self.norm()
        c = self.conj()
        return Qw(c.a / n, c.b / n)

    def __truediv__(self, o):
        return self * (o if isinstance(o, Qw) else Qw(o)).inv()

    def __eq__(self, o):
        o = o if isinstance(o, Qw) else Qw(o)
        return self.a == o.a and self.b == o.b

    def __hash__(self):
        return hash((self.a, self.b))

    def is_zero(self):
        return self.a == 0 and self.b == 0

    def __repr__(self):
        return "(%s%+s*w)" % (self.a, self.b) if self.b else str(self.a)


W_ = Qw(0, 1)
ZERO, ONE = Qw(0), Qw(1)


def mat(r):
    return tuple(tuple(x if isinstance(x, Qw) else Qw(x) for x in row) for row in r)


def mmul(X, Y):
    return tuple(tuple(X[i][0] * Y[0][j] + X[i][1] * Y[1][j] for j in range(2)) for i in range(2))


def mscale(s, X):
    return tuple(tuple(s * X[i][j] for j in range(2)) for i in range(2))


def mconj(X):
    return tuple(tuple(X[i][j].conj() for j in range(2)) for i in range(2))


def mdet(X):
    return X[0][0] * X[1][1] - X[0][1] * X[1][0]


def minv(X):
    d = mdet(X)
    return tuple(tuple(v / d for v in row) for row in ((X[1][1], -X[0][1]), (-X[1][0], X[0][0])))


def meq(X, Y):
    return all(X[i][j] == Y[i][j] for i in range(2) for j in range(2))


def mtrace(X):
    return X[0][0] + X[1][1]


I2 = mat([[1, 0], [0, 1]])
A = mat([[1, 1], [0, 1]])
B = mat([[1, 0], [-W_, 1]])
RELATOR = "abABaBAbaB"                   # B1141's relator (A = a^-1, B = b^-1)
BEAT = {"a": "a", "b": "BabAb"}          # beat(a) = a, beat(b) = b^-1 a b a^-1 b


def ev(word, a, b):
    M = I2
    table = {"a": a, "b": b, "A": minv(a), "B": minv(b)}
    for ch in word:
        M = mmul(M, table[ch])
    return M


def inv_word(word):
    return "".join({"a": "A", "b": "B", "A": "a", "B": "b"}[c] for c in reversed(word))


def sub(word, image):
    return "".join(image[ch] if ch in "ab" else inv_word(image[ch.lower()]) for ch in word)


def s1_holonomy():
    census = {(sa, sb): ev(RELATOR, mscale(sa, A), mscale(sb, B)) for sa in (1, -1) for sb in (1, -1)}
    assert meq(census[(1, 1)], I2) and meq(census[(-1, -1)], I2)
    assert meq(census[(-1, 1)], mscale(-1, I2)) and meq(census[(1, -1)], mscale(-1, I2))
    assert meq(ev(sub(RELATOR, BEAT), A, B), I2)                       # the beat respects the relator
    assert meq(ev(sub(BEAT["b"], BEAT), A, B), mmul(mmul(A, B), minv(A))) and sub(BEAT["a"], BEAT) == "a"
    parity = all(len(sub(x, BEAT)) % 2 == len(x) % 2 for x in ("a", "b"))
    assert parity
    return {k: "+I" if meq(v, I2) else "-I" for k, v in census.items()}


def solve_linear(rows):
    """Exact Gaussian elimination over Q(w): returns (rank, basis of the nullspace)."""
    rows = [list(r) for r in rows]
    n = len(rows[0])
    piv, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, len(rows)) if not rows[i][c].is_zero()), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        inv = rows[r][c].inv()
        rows[r] = [x * inv for x in rows[r]]
        for i in range(len(rows)):
            if i != r and not rows[i][c].is_zero():
                f = rows[i][c]
                rows[i] = [x - f * y for x, y in zip(rows[i], rows[r])]
        piv.append(c)
        r += 1
    free = [c for c in range(n) if c not in piv]
    basis = []
    for fcol in free:
        v = [ZERO] * n
        v[fcol] = ONE
        for i, pc in enumerate(piv):
            v[pc] = -rows[i][fcol]
        basis.append(v)
    return r, basis


def s2_intertwiner():
    """Unknowns W = [[x0,x1],[x2,x3]]: W conj(g) - rho(beat g) W = 0 for g = a, b (8 equations)."""
    rows = []
    for g in ("a", "b"):
        C = mconj(ev(g, A, B))
        D = ev(BEAT[g], A, B)
        for i in range(2):
            for j in range(2):
                row = [ZERO] * 4
                for k in range(2):                       # (W C)_ij = sum_k W_ik C_kj ; (D W)_ij = sum_k D_ik W_kj
                    row[2 * i + k] = row[2 * i + k] + C[k][j]
                    row[2 * k + j] = row[2 * k + j] - D[i][k]
                rows.append(row)
    rank, basis = solve_linear(rows)
    assert rank == 3 and len(basis) == 1
    v = basis[0]
    W = ((v[0], v[1]), (v[2], v[3]))
    for g in ("a", "b"):
        assert meq(mmul(mmul(W, mconj(ev(g, A, B))), minv(W)), ev(BEAT[g], A, B))
    d = mdet(W)
    sq = mmul(W, mconj(W))
    mu = sq[0][1]                                        # A = [[1,1],[0,1]]: W conj(W) = mu A
    assert meq(sq, mscale(mu, A)) and mu.b == 0 and mu.a * mu.a == d.norm()
    return W, d, mu


class G:
    """The double cover G_eps of Isom(H^3): elements (M, k), M in GL(2, Q(w)) up to the normalisation handled below."""
    def __init__(self, eps):
        self.eps = eps

    def mul(self, x, y):
        (M1, k1), (M2, k2) = x, y
        M = mmul(M1, mconj(M2) if k1 else M2)
        if k1 and k2:
            M = mscale(self.eps, M)
        return (M, (k1 + k2) % 2)

    def inv(self, x):
        M, k = x
        return (minv(M), 0) if k == 0 else (mscale(self.eps, minv(mconj(M))), 1)


def s3_the_double_covers():
    out = {}
    iw = Qw(1, 2)                                         # 1 + 2w = sqrt(-3); unit-free test elements below
    samples = [(A, 0), (B, 1), (mat([[2, 1], [1, 1]]), 1), (mat([[1, W_], [0, 1]]), 0), (mat([[W_, 0], [0, W_.conj()]]), 1)]
    for eps in (1, -1):
        g = G(eps)
        assoc = all(g.mul(g.mul(p, q), r) == g.mul(p, g.mul(q, r)) for p, q, r in itertools.product(samples, repeat=3))
        central = all(g.mul((mscale(-1, I2), 0), p) == g.mul(p, (mscale(-1, I2), 0)) for p in samples)
        refl_c = g.mul((I2, 1), (I2, 1))                                   # c : z -> conj(z) fixes j
        rot = mat([[W_, 0], [0, W_.conj()]])                              # diag(w, w^-1): z -> w^2 z, fixes j
        refl_2 = g.mul((rot, 1), (rot, 1))                                 # z -> w^2 conj(z): another reflection through j
        assert assoc and central and meq(refl_c[0], mscale(eps, I2)) and meq(refl_2[0], mscale(eps, I2))
        out[eps] = ("Pin+" if eps == 1 else "Pin-", "reflection lifts square to %+d" % eps)
    return out


def s4_table(W, mu):
    """sigma = +1: B1141's lift (a -> A, b -> B); sigma = -1: the other (-A, -B).  The lift of the Gieseking generator is
    t -> (lam W, 1) with lam^2 det W = 1; conjugation relations are independent of lam and checked exactly with W; the
    square (lam W, 1)^2 = (|lam|^2 eps W conj(W), 0) = (sign(mu) eps A, 0) since |lam|^2 = 1/|det W| = 1/|mu|."""
    sign_mu = 1 if mu.a > 0 else -1
    table = {}
    for sigma in (1, -1):
        a_l, b_l = (mscale(sigma, A), 0), (mscale(sigma, B), 0)
        for eps in (1, -1):
            g = G(eps)
            t = (W, 1)
            rel_a = g.mul(g.mul(t, a_l), g.inv(t))[0] == a_l[0]
            beat_b = ev(BEAT["b"], mscale(sigma, A), mscale(sigma, B))
            rel_b = meq(g.mul(g.mul(t, b_l), g.inv(t))[0], beat_b)
            rel_R = meq(ev(RELATOR, mscale(sigma, A), mscale(sigma, B)), I2)
            rel_sq = (sign_mu * eps == sigma)                              # t^2 = a in the lift
            table[(sigma, eps)] = (rel_a and rel_b and rel_R and rel_sq, (rel_a, rel_b, rel_R, rel_sq))
    assert table[(1, 1)][0] and table[(-1, -1)][0] and not table[(1, -1)][0] and not table[(-1, 1)][0]
    assert all(table[k][1][:3] == (True, True, True) for k in table)   # only the square discriminates
    return table, sign_mu


def s5_topology():
    import snappy
    N, Mt = snappy.Manifold("m000"), snappy.Manifold("m004")
    h1N, h1M = str(N.homology()), str(Mt.homology())
    b0, b1 = 1, 1                        # over Z/2 (H1 = Z); chi(compact core) = chi(Klein-bottle boundary)/2 = 0
    b2 = b1 - b0
    assert h1N == "Z" and h1M == "Z" and not N.is_orientable() and N.orientation_cover().is_isometric_to(Mt) and b2 == 0
    return h1N, h1M, b2


def s6_cusp_names(maxlen=8):
    """a is a meridian (A parabolic, fixes infinity).  A longitude: a reduced word of exponent sum 0 whose image fixes
    infinity, commutes with A, and is not a power of A (non-integral translation)."""
    letters = "abAB"
    found = None
    for n in range(2, maxlen + 1, 2):
        for tup in itertools.product(letters, repeat=n):
            word = "".join(tup)
            if any(word[i] == inv_word(word[i + 1]) for i in range(n - 1)):
                continue
            if word.count("a") != word.count("A") or word.count("b") != word.count("B"):
                continue
            M = ev(word, A, B)
            if not M[1][0].is_zero():
                continue
            if not meq(mmul(M, A), mmul(A, M)):
                continue
            x = M[0][1] / M[0][0]
            if x.b == 0:                                  # rational translation: a power of the meridian (or trivial)
                continue
            found = (word, M)
            break
        if found:
            break
    assert found is not None
    word, M = found
    names = {}
    for sigma in (1, -1):
        tr_mu = mtrace(mscale(sigma, A))
        tr_l = mtrace(ev(word, mscale(sigma, A), mscale(sigma, B)))
        names[sigma] = (int(tr_mu.a), int(tr_l.a))
        assert tr_mu.b == 0 and tr_l.b == 0
    assert names[1] == (2, -2) and names[-1] == (-2, -2)
    return word, names


if __name__ == "__main__":
    print("S1  relator census R(+-A, +-B):", s1_holonomy(), "| the beat respects the relator; beat^2 = conjugation by a;"
          " word-length parity preserved")
    W, d, mu = s2_intertwiner()
    print("S2  intertwiner space exactly 1-dimensional over Q(w): W =", W, "| det W =", d, "| W conj(W) =", mu, "* A,",
          "mu^2 = |det W|^2 -> W0 conj(W0) = %+d A (B1141: +A)" % (1 if mu.a > 0 else -1))
    print("S3  G_eps associative, -I central; reflections through j:", s3_the_double_covers())
    table, sign_mu = s4_table(W, mu)
    for (sigma, eps), (ok, parts) in sorted(table.items(), reverse=True):
        print("S4  spin lift %s into G_%s (%s): %s   [t a t^-1 = a, t b t^-1 = beat(b), relator, t^2 = a: %s]"
              % ("untwisted, B1141's (a -> +A)" if sigma == 1 else "twisted, the other (a -> -A)",
                 "+" if eps == 1 else "-", "Pin+" if eps == 1 else "Pin-", "EXTENDS" if ok else "does not extend", parts))
    h1N, h1M, b2 = s5_topology()
    print("S5  H1(Gieseking) = %s, H1(m004) = %s; dim H2(N;Z/2) = %d => w2 = w1^2 = 0: two Pin+ and two Pin- structures;"
          " p* = 0 on H^1(-;Z/2) (a = b = 2t, R021)" % (h1N, h1M, b2))
    word, names = s6_cusp_names()
    print("S6  meridian a, longitude %s; (tr mu, tr lambda): untwisted %s, twisted %s (B921-6's rho_1, rho_2)"
          % (word, names[1], names[-1]))
    print("DONE")
