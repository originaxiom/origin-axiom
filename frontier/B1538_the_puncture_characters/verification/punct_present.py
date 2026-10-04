#!/usr/bin/env python3
"""B1538 route P -- the line's cohomology on the cover's own presentation, mod p.  Library; nothing sealed is computed on
import.

H = pi_1 N is presented by Reidemeister-Schreier from Gamma = <a, b, t | t g t^-1 = phi(g)>, with route P's own transversal: a
BFS of the coset graph on D with the letters tried in the order t, a, b, T, A, B (route W's transversal uses a, b only).
  - The generators are s'_(x,g) = u'_x g u'_(x^g)^-1 for the non-tree edges: 3|D| - (|D| - 1) = 2|D| + 1 of them.
  - The relators are Gamma's two relators rewritten from every coset.
  - chi's value on s'_(x,g) is read along the word's path (punct_covers.Cover.chi_exp, which defines chi from (zeta, s)).
Then, for chi of order dividing L, over GF(p) with p = 1 mod L (z_L -> a primitive L-th root of unity mod p):
  - Z^1 is the kernel of the relators' Fox matrix, and B^1 has dimension 1 - h^0, with h^0 = [chi = 1];
  - h^1 = #gens - rank(Fox) - (1 - h^0);
  - r1 is the rank of the restriction to the cusps where chi is trivial (their two peripheral elements u_x l^i t'^j u_x^-1
    rewritten, each giving the row of z -> z(h)), on Z^1: rank([Fox; rows]) - rank(Fox);
  - n = h^1 - r1.
A rank mod p can only drop below the rank over Q(z_L); two primes are read and must agree (route P's double read).

python-flint's nmod_mat for the ranks.  New code for B1538."""
from functools import lru_cache
from math import gcd

import punct_covers as F


def is_prime(n):
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


@lru_cache(maxsize=None)
def primes_1_mod(L, start, count):
    """the first count primes p = 1 mod L with p > start"""
    out, p = [], (start // L + 1) * L + 1
    while len(out) < count:
        if is_prime(p):
            out.append(p)
        p += L
    return tuple(out)


@lru_cache(maxsize=None)
def root_of_unity_mod(L, p):
    """a primitive L-th root of unity mod p (p = 1 mod L)"""
    assert (p - 1) % L == 0
    fac, n, q = [], p - 1, 2
    while q * q <= n:
        if n % q == 0:
            fac.append(q)
            while n % q == 0:
                n //= q
        q += 1
    if n > 1:
        fac.append(n)
    for g in range(2, p):
        if all(pow(g, (p - 1) // f, p) != 1 for f in fac):
            return pow(g, (p - 1) // L, p)
    raise ValueError


class Presentation:
    """route P's Reidemeister-Schreier presentation of H for one cover (independent of the characters)"""

    def __init__(self, C):
        self.C = C
        d = C.d
        perms, pinv = C.perms, C.pinv
        u = {0: ""}
        order, k = [0], 0
        while k < len(order):
            x = order[k]
            k += 1
            for g in "tabTAB":
                y = perms[g][x] if g.islower() else pinv[g.lower()][x]
                if y not in u:
                    u[y] = u[x] + g
                    order.append(y)
        assert len(u) == d
        self.u = [u[x] for x in range(d)]
        self.gens, self.gidx = [], {}
        for x in range(d):
            for g in "abt":
                word = F.free_reduce(self.u[x] + g + F.inv_word(self.u[perms[g][x]]))
                if word:
                    self.gidx[(x, g)] = len(self.gens)
                    self.gens.append((x, g, word))
        assert len(self.gens) == 2 * d + 1, (len(self.gens), d)
        self.rels = [self.rewrite(r, x) for x in range(d) for r in C.st.G.rels]
        self.periph = [[self.rewrite(h, 0) for h in pair] for pair in C.periph]

    def rewrite(self, word, start):
        cur, out = start, []
        perms, pinv = self.C.perms, self.C.pinv
        for c in word:
            g = c.lower()
            if c.islower():
                if (cur, g) in self.gidx:
                    out.append((self.gidx[(cur, g)], 1))
                cur = perms[g][cur]
            else:
                prev = pinv[g][cur]
                if (prev, g) in self.gidx:
                    out.append((self.gidx[(prev, g)], -1))
                cur = prev
        assert cur == start, ("not a closed path", word, start)
        return out

    def values(self, ez, es, L):
        """chi(s'_(x,g)) as exponents mod L"""
        vals = self.C.rs_values(ez, es, L)
        return [self.C.chi_exp(w, vals, L) for (_, _, w) in self.gens]


def _fox_row(word, vals, z, p, ngen):
    """the row of z -> z(word) for left cocycles, mod p (z[k] = z_L^k mod p)"""
    row = [0] * ngen
    pre = 0
    L = len(z)
    for j, e in word:
        if e == 1:
            row[j] = (row[j] + z[pre % L]) % p
            pre += vals[j]
        else:
            pre -= vals[j]
            row[j] = (row[j] - z[pre % L]) % p
    return row, pre % L


def read(Pr, ez, es, L, p):
    """route P at chi = (ez, es) mod L, over GF(p): h1, the trivial cusps, r1, n"""
    import flint
    vals = Pr.values(ez, es, L)
    g = root_of_unity_mod(L, p)
    z = [pow(g, k, p) for k in range(L)]
    ngen = len(Pr.gens)
    fox = []
    for R in Pr.rels:
        row, tot = _fox_row(R, vals, z, p, ngen)
        assert tot == 0, "a relator is not in ker chi"
        fox.append(row)
    rk = flint.nmod_mat(len(fox), ngen, [v for r in fox for v in r], p).rank()
    trivial = all(v % L == 0 for v in vals)
    h1 = ngen - rk - (0 if trivial else 1)
    cusp_rows, triv = [], []
    for k, (w1, w2) in enumerate(Pr.periph):
        r1_, t1 = _fox_row(w1, vals, z, p, ngen)
        r2_, t2 = _fox_row(w2, vals, z, p, ngen)
        if t1 == 0 and t2 == 0:
            triv.append(k)
            cusp_rows += [r1_, r2_]
    if cusp_rows:
        allr = fox + cusp_rows
        rk2 = flint.nmod_mat(len(allr), ngen, [v for r in allr for v in r], p).rank()
        r1 = rk2 - rk
    else:
        r1 = 0
    return {"h1": h1, "trivial cusps": len(triv), "r1": r1, "n": h1 - r1}


# ============================================================================================ modules (the four), route P4
def _matmul(A, B, p):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum(A[i][l] * B[l][j] for l in range(k)) % p for j in range(m)] for i in range(n)]


def _matinv(A, p):
    import flint
    n = len(A)
    M = flint.nmod_mat(n, n, [v % p for row in A for v in row], p)
    Mi = M.inv()
    return [[int(Mi[i, j]) for j in range(n)] for i in range(n)]


def _eye(e):
    return [[1 if i == j else 0 for j in range(e)] for i in range(e)]


class ModP:
    """a module on route P's generators: one e x e matrix over GF(p) per generator (and its inverse)"""

    def __init__(self, mats, p):
        self.p, self.M = p, [[[v % p for v in row] for row in m] for m in mats]
        self.e = len(self.M[0])
        self.Mi = [_matinv(m, p) for m in self.M]

    def word(self, w):
        X = _eye(self.e)
        for j, s in w:
            X = _matmul(X, self.M[j] if s == 1 else self.Mi[j], self.p)
        return X

    def dual(self):
        return ModP([[list(r) for r in zip(*mi)] for mi in self.Mi], self.p)


def _fox_block(mod, w, ngen):
    """z(w) = sum_j K_j z(s_j): an e x (ngen e) matrix over GF(p) (left cocycles)"""
    p, e = mod.p, mod.e
    out = [[0] * (ngen * e) for _ in range(e)]
    Pre = _eye(e)
    for j, s in w:
        if s == 1:
            for i in range(e):
                for k in range(e):
                    out[i][j * e + k] = (out[i][j * e + k] + Pre[i][k]) % p
            Pre = _matmul(Pre, mod.M[j], p)
        else:
            Pre = _matmul(Pre, mod.Mi[j], p)
            for i in range(e):
                for k in range(e):
                    out[i][j * e + k] = (out[i][j * e + k] - Pre[i][k]) % p
    return out


def _rank(rows, ncols, p):
    import flint
    if not rows:
        return 0
    return flint.nmod_mat(len(rows), ncols, [v % p for r in rows for v in r], p).rank()


def read_module(Pr, mod):
    """h^0, h^1, r1 and n of a module on H (route P's presentation), over GF(p)
    r1 = rank([BP | R Z]) - rank(BP): the image of Z^1 in the cusps' cocycles modulo their coboundaries"""
    import flint
    p, e = mod.p, mod.e
    ngen = len(Pr.gens)
    fox = []
    for R in Pr.rels:
        assert mod.word(R) == _eye(e), "a relator is not 1"
        fox += _fox_block(mod, R, ngen)
    rk = _rank(fox, ngen * e, p)
    dg = []
    for m in mod.M:
        dg += [[(m[i][k] - (1 if i == k else 0)) % p for k in range(e)] for i in range(e)]
    a0 = e - _rank(dg, e, p)
    dimZ = ngen * e - rk
    h1 = dimZ - (e - a0)
    # Z^1's basis: the nullspace of the Fox matrix
    if fox:
        F_ = flint.nmod_mat(len(fox), ngen * e, [v for r in fox for v in r], p)
        Z = F_.nullspace()[0]
        zcols = [[int(Z[i, j]) for i in range(ngen * e)] for j in range(dimZ)]
    else:
        zcols = [[1 if i == j else 0 for i in range(ngen * e)] for j in range(ngen * e)]
    rowsR, blocks = [], []
    for (w1, w2) in Pr.periph:
        rowsR += _fox_block(mod, w1, ngen) + _fox_block(mod, w2, ngen)
        P1, P2 = mod.word(w1), mod.word(w2)
        blocks.append([[(P1[i][k] - (1 if i == k else 0)) % p for k in range(e)] for i in range(e)] +
                      [[(P2[i][k] - (1 if i == k else 0)) % p for k in range(e)] for i in range(e)])
    nc = len(Pr.periph)
    BP = [[0] * (e * nc) for _ in range(2 * e * nc)]
    for c, b in enumerate(blocks):
        for i in range(2 * e):
            for k in range(e):
                BP[2 * e * c + i][e * c + k] = b[i][k]
    RZ = [[sum(r[t] * z[t] for t in range(ngen * e)) % p for z in zcols] for r in rowsR]
    rBP = _rank(BP, e * nc, p)
    both = [BP[i] + RZ[i] for i in range(2 * e * nc)]
    r1 = _rank(both, e * nc + dimZ, p) - rBP
    return {"h0": a0, "h1": h1, "r1": r1, "n": h1 - r1}
