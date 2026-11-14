"""Verifier's own core (written from scratch; nothing imported from the prior agent's tcore.py).

Arithmetic: Z[zeta_5] as the group ring Z[C_5] modulo the all-ones vector. An element is a 5-tuple of ints
(coefficients of zeta^0..zeta^4), NOT normalised; x == y iff x - y has all coefficients equal.
Real elements |x|^2 are converted to Q(sqrt5) as (p, q) meaning p + q sqrt5, with Fractions.
Free-group words: strings over a,b,t,... with UPPERCASE = inverse.
"""
from fractions import Fraction as Fr
from itertools import product as iprod

Z0 = (0, 0, 0, 0, 0)


def zp(j):
    v = [0] * 5
    v[j % 5] = 1
    return tuple(v)


ONE = zp(0)


def gadd(x, y):
    return tuple(x[i] + y[i] for i in range(5))


def gsub(x, y):
    return tuple(x[i] - y[i] for i in range(5))


def gmul(x, y):
    out = [0] * 5
    for i, xi in enumerate(x):
        if xi:
            for j, yj in enumerate(y):
                if yj:
                    out[(i + j) % 5] += xi * yj
    return tuple(out)


def gscale(c, x):
    return tuple(c * v for v in x)


def giszero(x):
    return len(set(x)) == 1


def geq(x, y):
    return giszero(gsub(x, y))


def gbar(x):
    return tuple(x[(-i) % 5] for i in range(5))


def real_to_q5(x):
    """x real in Z[C5]/(sum): return (p, q) with x = p + q sqrt5. zeta+zeta^4 = (sqrt5-1)/2, zeta^2+zeta^3 = (-1-sqrt5)/2."""
    # normalise so that x is symmetric: x real means x - bar(x) == 0 mod all-ones; symmetrise by averaging
    s = [Fr(x[i] + x[(-i) % 5], 2) for i in range(5)]
    assert giszero(gsub(x, gbar(x))), x
    c0, c1, c2 = s[0], s[1], s[2]
    return (c0 - c1 / 2 - c2 / 2, c1 / 2 - c2 / 2)


def abs2(x):
    return real_to_q5(gmul(x, gbar(x)))


def q5div(u, v):
    p1, q1 = u
    p2, q2 = v
    d = p2 * p2 - 5 * q2 * q2
    return ((p1 * p2 - 5 * q1 * q2) / d, (q1 * p2 - p1 * q2) / d)


def q5mul(u, v):
    return (u[0] * v[0] + 5 * u[1] * v[1], u[0] * v[1] + u[1] * v[0])


def q5float(u):
    return float(u[0]) + float(u[1]) * 5 ** 0.5


def unit_multiple(x, y):
    """is x = +-zeta^m * y ?  returns (s, m) or None"""
    for s in (1, -1):
        for m in range(5):
            if geq(x, gscale(s, gmul(zp(m), y))):
                return (s, m)
    return None


# ---------------- free groups (strings, uppercase = inverse)
def inv_letter(c):
    return c.lower() if c.isupper() else c.upper()


def finv(w):
    return ''.join(inv_letter(c) for c in reversed(w))


def fred(w):
    st = []
    for c in w:
        if st and st[-1] == inv_letter(c):
            st.pop()
        else:
            st.append(c)
    return ''.join(st)


def fsubst(phi, w):
    out = []
    for c in w:
        out.append(phi[c] if c.islower() else finv(phi[c.lower()]))
    return fred(''.join(out))


def fcompose(phi, psi):
    """(phi o psi)(x) = phi(psi(x))"""
    return {g: fsubst(phi, psi[g]) for g in psi}


def conjugator(w, c):
    """w (reduced) is a conjugate of the cyclically reduced word c: return g with g c g^-1 == w (reduced)."""
    u = ''
    while len(w) >= 2 and w[0] == inv_letter(w[-1]):
        u += w[0]
        w = w[1:-1]
    # now w is cyclically reduced, a rotation of c
    for i in range(len(c)):
        if c[i:] + c[:i] == w:
            g = fred(u + finv(c[:i]))
            return g
    return None


# ---------------- characters and Fox calculus
def expo(w, e):
    s = 0
    for c in w:
        s += e[c] if c.islower() else -e[c.lower()]
    return s % 5


def fox_rho(w, x, e, plant=None):
    """rho(dw/dx) in Z[C5], rho(g) = zeta^e[g]."""
    out = [0] * 5
    p = 0
    for c in w:
        g = c.lower()
        if c.islower():
            if g == x:
                out[p % 5] += 1
            p += e[g]
        else:
            p -= e[g]
            if g == x:
                if plant == 'sign':
                    out[p % 5] += 1          # PLANT Q3: d(g^-1)/dg = +g^-1
                else:
                    out[p % 5] -= 1
    return tuple(out)


def det2(m):
    return gsub(gmul(m[0][0], m[1][1]), gmul(m[0][1], m[1][0]))


def minors(J, drop):
    """determinant of J (n-1 x n) with column `drop` removed; n <= 3."""
    cols = [c for c in range(len(J[0])) if c != drop]
    sub = [[J[r][c] for c in cols] for r in range(len(J))]
    if len(sub) == 1:
        return sub[0][0]
    if len(sub) == 2:
        return det2(sub)
    raise ValueError('only n <= 3')


def rank_J(J):
    n = len(J[0])
    m = len(J)
    if m == 2 and n == 3:
        if any(not giszero(minors(J, d)) for d in range(3)):
            return 2
    if m == 1 and n == 2:
        pass
    return 1 if any(not giszero(x) for row in J for x in row) else 0


def twisted(gens, rels, e, plant=None):
    J = [[fox_rho(r, g, e, plant) for g in gens] for r in rels]
    d1 = [gsub(zp(e[g]), ONE) for g in gens]
    chain_ok = all(giszero(sum_g([gmul(J[i][j], d1[j]) for j in range(len(gens))])) for i in range(len(rels)))
    r2 = rank_J(J)
    r1 = 0 if all(giszero(x) for x in d1) else 1
    H = (1 - r1, len(gens) - r1 - r2, len(rels) - r2)
    return J, d1, H, chain_ok


def sum_g(xs):
    s = Z0
    for x in xs:
        s = gadd(s, x)
    return s


def chars(gens, rels):
    out = []
    for vals in iprod(range(5), repeat=len(gens)):
        e = dict(zip(gens, vals))
        if all(expo(r, e) == 0 for r in rels):
            out.append(e)
    return out


# ---------------- 2x2 integer matrices for words
def matw(word, eps=1):
    L = ((1, 1), (0, 1))
    R = ((1, 0), (1, 1))
    M = ((1, 0), (0, 1))
    for ch in word:
        X = L if ch == 'L' else R
        M = ((M[0][0] * X[0][0] + M[0][1] * X[1][0], M[0][0] * X[0][1] + M[0][1] * X[1][1]),
             (M[1][0] * X[0][0] + M[1][1] * X[1][0], M[1][0] * X[0][1] + M[1][1] * X[1][1]))
    return ((eps * M[0][0], eps * M[0][1]), (eps * M[1][0], eps * M[1][1]))


def eps_mark(M, v=(1, 2)):
    """eps with M^T v = eps v mod 5, else 0."""
    w = ((M[0][0] * v[0] + M[1][0] * v[1]) % 5, (M[0][1] * v[0] + M[1][1] * v[1]) % 5)
    if w == (v[0] % 5, v[1] % 5):
        return 1
    if w == ((-v[0]) % 5, (-v[1]) % 5):
        return -1
    return 0
