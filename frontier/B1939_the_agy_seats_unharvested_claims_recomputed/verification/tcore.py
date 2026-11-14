"""Exact core: Q(zeta_5), Fox calculus under mu_5 characters, punctured-torus-bundle presentations.

Own code (main's verifier). Nothing imported from any seat.
An element of Q(zeta_5) is a tuple of 5 Fractions c[0..4] meaning sum c_i zeta^i, kept REDUCED (c[4] == 0) by
subtracting c4*(1+zeta+...+zeta^4) = 0.
"""
from fractions import Fraction as Fr
from itertools import product

N = 5


def red(c):
    c4 = c[4]
    return tuple(Fr(c[i]) - c4 for i in range(4)) + (Fr(0),)


def zpow(j):
    c = [Fr(0)] * 5
    c[j % 5] = Fr(1)
    return red(c)


ZERO = red([0] * 5)
ONE = zpow(0)


def add(x, y):
    return red([x[i] + y[i] for i in range(5)])


def neg(x):
    return red([-x[i] for i in range(5)])


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    c = [Fr(0)] * 5
    for i in range(5):
        if x[i] == 0:
            continue
        for j in range(5):
            if y[j] == 0:
                continue
            c[(i + j) % 5] += x[i] * y[j]
    return red(c)


def scal(q, x):
    return red([Fr(q) * x[i] for i in range(5)])


def is0(x):
    return all(v == 0 for v in red(x))


def gal(x, j):
    """sigma_j: zeta -> zeta^j (j in 1..4)."""
    c = [Fr(0)] * 5
    for i in range(5):
        c[(i * j) % 5] += x[i]
    return red(c)


def conj(x):
    return gal(x, 4)


def norm(x):
    p = x
    for j in (2, 3, 4):
        p = mul(p, gal(x, j))
    assert all(p[i] == 0 for i in (1, 2, 3)), p
    return p[0]


def inv(x):
    nx = norm(x)
    assert nx != 0
    p = ONE
    for j in (2, 3, 4):
        p = mul(p, gal(x, j))
    return scal(Fr(1) / nx, p)


def div(x, y):
    return mul(x, inv(y))


def real_pq(z):
    """z real (fixed by conj) in Q(sqrt5): return (p, q) with z = p + q*sqrt5."""
    z = red(z)
    assert is0(sub(z, conj(z))), z
    # reduced real element has c1 = 0 and c2 == c3; z = c0 + c2(zeta^2+zeta^3) = c0 + c2(-1-eta), eta=(sqrt5-1)/2
    assert z[1] == 0 and z[2] == z[3], z
    c0, c2 = z[0], z[2]
    return (c0 - c2 / 2, -c2 / 2)


def abs2(z):
    return real_pq(mul(z, conj(z)))


def to_complex(z):
    import cmath
    w = cmath.exp(2j * cmath.pi / 5)
    return sum(complex(float(z[i])) * w ** i for i in range(5))


def det(M):
    """Determinant over Q(zeta_5) by Gaussian elimination."""
    n = len(M)
    if n == 0:
        return ONE
    A = [list(r) for r in M]
    d = ONE
    for col in range(n):
        piv = None
        for r in range(col, n):
            if not is0(A[r][col]):
                piv = r
                break
        if piv is None:
            return ZERO
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
            d = neg(d)
        d = mul(d, A[col][col])
        ip = inv(A[col][col])
        for r in range(col + 1, n):
            if is0(A[r][col]):
                continue
            f = mul(A[r][col], ip)
            for c in range(col, n):
                A[r][c] = sub(A[r][c], mul(f, A[col][c]))
    return d


def rank(M):
    if not M:
        return 0
    A = [list(r) for r in M]
    nr, nc = len(A), len(A[0])
    rk = 0
    for col in range(nc):
        piv = None
        for r in range(rk, nr):
            if not is0(A[r][col]):
                piv = r
                break
        if piv is None:
            continue
        A[rk], A[piv] = A[piv], A[rk]
        ip = inv(A[rk][col])
        for r in range(nr):
            if r != rk and not is0(A[r][col]):
                f = mul(A[r][col], ip)
                for c in range(col, nc):
                    A[r][c] = sub(A[r][c], mul(f, A[rk][c]))
        rk += 1
    return rk


# ---------------- free groups ----------------
# a word is a tuple of (gen, sign), gen a string, sign +1/-1

def winv(w):
    return tuple((g, -s) for (g, s) in reversed(w))


def wred(w):
    out = []
    for x in w:
        if out and out[-1][0] == x[0] and out[-1][1] == -x[1]:
            out.pop()
        else:
            out.append(x)
    return tuple(out)


def wmul(*ws):
    r = ()
    for w in ws:
        r = r + tuple(w)
    return wred(r)


def parse(s):
    """'abA' -> word; uppercase = inverse."""
    return tuple((ch.lower(), 1 if ch.islower() else -1) for ch in s)


def subst(phi, w):
    """apply the endomorphism phi (dict gen -> word) to word w."""
    out = ()
    for g, s in w:
        img = phi.get(g, ((g, 1),))
        out = out + (img if s == 1 else winv(img))
    return wred(out)


def compose(phi, psi):
    """(phi o psi)(x) = phi(psi(x))."""
    return {g: subst(phi, psi[g]) for g in psi}


def expsum(w, e):
    """exponent of rho(w) for rho(g) = zeta^e[g]."""
    return sum(s * e[g] for g, s in w) % 5


def fox(w, x, e, planted_bad_inverse=False):
    """rho(d w / d x) in Q(zeta_5), rho(g) = zeta^e[g]."""
    c = [Fr(0)] * 5
    p = 0
    for g, s in w:
        if s == 1:
            if g == x:
                c[p % 5] += 1
            p += e[g]
        else:
            pold = p
            p -= e[g]
            if g == x:
                if planted_bad_inverse == 'sign':
                    c[p % 5] += 1         # PLANT: wrong sign, d(g^-1)/dg = +g^-1
                elif planted_bad_inverse:
                    c[pold % 5] -= 1      # PLANT: drops the factor g^-1
                else:
                    c[p % 5] -= 1         # d(g^-1)/dg = -g^-1
    return red(c)


# ---------------- punctured torus bundles ----------------
A, B = 'a', 'b'
COMM = parse('abAB')  # [a,b] = a b a^-1 b^-1

PHI = {
    # L_col = [[1,1],[0,1]] (columns = images of a, b in H_1): a -> a, b -> b a
    'L': {A: parse('a'), B: parse('ba')},
    # R_col = [[1,0],[1,1]]: a -> a b, b -> b
    'R': {A: parse('ab'), B: parse('b')},
}
# -I fixing [a,b] exactly: conjugate of (a -> a^-1, b -> b^-1) by ba
IOTA_FIX = {A: parse('bAB'), B: parse('baBAB')}
IOTA_NAIVE = {A: parse('A'), B: parse('B')}   # fixes [a,b] only up to conjugacy (plant P3)

IDENT = {A: parse('a'), B: parse('b')}


def phi_word(word, eps=1, naive_iota=False):
    """free-group automorphism for eps * W_col, W = word in 'L','R' (W_col = product in word order)."""
    phi = dict(IDENT)
    for ch in reversed(word):
        phi = compose(PHI[ch], phi)          # phi_{w1} o ... o phi_{wn}
    if eps == -1:
        phi = compose(IOTA_NAIVE if naive_iota else IOTA_FIX, phi)
    return phi


def abel(phi):
    """2x2 integer matrix, columns = images of a, b."""
    col = {}
    for g in (A, B):
        w = phi[g]
        col[g] = (sum(s for h, s in w if h == A), sum(s for h, s in w if h == B))
    return ((col[A][0], col[B][0]), (col[A][1], col[B][1]))


def mat_word(word, eps=1):
    L = ((1, 1), (0, 1))
    R = ((1, 0), (1, 1))
    M = ((1, 0), (0, 1))
    for ch in word:
        X = L if ch == 'L' else R
        M = tuple(tuple(sum(M[i][k] * X[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    return tuple(tuple(eps * v for v in r) for r in M)


def hnn(phi):
    """generators a, b, t; relators t x t^-1 phi(x)^-1."""
    gens = [A, B, 't']
    rels = [wmul(((('t', 1)),), ((g, 1),), (('t', -1),), winv(phi[g])) for g in (A, B)]
    return gens, rels


def characters(gens, rels):
    out = []
    for vals in product(range(5), repeat=len(gens)):
        e = dict(zip(gens, vals))
        if all(expsum(r, e) == 0 for r in rels):
            out.append(e)
    return out


def complex_data(gens, rels, e, planted_bad_inverse=False):
    J = [[fox(r, g, e, planted_bad_inverse) for g in gens] for r in rels]
    d1 = [sub(zpow(e[g]), ONE) for g in gens]
    # chain-complex check: sum_j J_ij (rho(x_j) - 1) = rho(r_i) - 1 = 0
    cc_ok = all(is0(add_all([mul(J[i][j], d1[j]) for j in range(len(gens))])) for i in range(len(rels)))
    rk2 = rank(J)
    rk1 = 0 if all(is0(x) for x in d1) else 1
    n, m = len(gens), len(rels)
    h = (1 - rk1, n - rk1 - rk2, m - rk2)
    return J, d1, h, cc_ok


def add_all(xs):
    s = ZERO
    for x in xs:
        s = add(s, x)
    return s


def wada(gens, rels, e, j=None, planted_bad_inverse=False):
    """Wada invariant det(J minus column j)/(rho(g_j)-1); returns (tau, j) or (None, None) if rho trivial.
    tau == ZERO means the complex is not acyclic (deficiency-one presentation)."""
    J = [[fox(r, g, e, planted_bad_inverse) for g in gens] for r in rels]
    cands = [i for i, g in enumerate(gens) if e[g] % 5 != 0]
    if not cands:
        return None, None
    if j is None:
        j = cands[-1]
    assert e[gens[j]] % 5 != 0
    minor = [[J[r][c] for c in range(len(gens)) if c != j] for r in range(len(rels))]
    return div(det(minor), sub(zpow(e[gens[j]]), ONE)), j


def unit_root(z):
    """if z = +-zeta^m return (sign, m) else None."""
    for s in (1, -1):
        for m in range(5):
            if is0(sub(z, scal(s, zpow(m)))):
                return (s, m)
    return None


def smith_tors(M):
    """torsion invariants of coker of integer 2x2 matrix M."""
    import math
    a, b = M[0]
    c, d = M[1]
    g = math.gcd(math.gcd(abs(a), abs(b)), math.gcd(abs(c), abs(d)))
    D = abs(a * d - b * c)
    if g == 0:
        return ('Z', 'Z')
    if D == 0:
        return ('Z', g)
    return (g, D // g)
