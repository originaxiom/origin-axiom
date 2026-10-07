#!/usr/bin/env python3
"""The Alexander polynomial of a one-cusped manifold with b1 = 1 by Fox calculus (no Sage): the abelianisation's free part
from the Smith normal form of the relator exponent matrix, the Fox matrix over Z[t, t^-1], Delta = gcd of the maximal minors
(up to units).  For a fibred manifold with one cusp, deg Delta = 2 g(fibre).  Usage: alexander.py <name or isosig> ..."""
import sys, sympy as sp, snappy
from sympy.matrices.normalforms import smith_normal_decomp
t = sp.symbols("t")


def abelian_free_map(G):
    gens = G.generators(); rows = [[sum((1 if ch.islower() else -1) for ch in r if ch.lower() == g) for g in gens] for r in G.relators()]
    E = sp.Matrix(rows) if rows else sp.zeros(0, len(gens)); S, U, V = smith_normal_decomp(E, sp.ZZ)   # S = U E V
    n = len(gens); d = [int(S[i, i]) if i < min(S.shape) else 0 for i in range(n)]
    free = [i for i in range(n) if d[i] == 0]; assert len(free) == 1, ("b1 != 1", d)
    i0 = free[0]; return gens, [int(V[j, i0]) for j in range(n)]        # exponent of t for generator j


def fox(word, gens, exps):
    """Fox derivatives of a word at the abelianisation g -> t^e(g): a row over Z[t, 1/t]"""
    row = [sp.Integer(0)] * len(gens); prefix = sp.Integer(1)
    for ch in word:
        j = gens.index(ch.lower())
        if ch.islower(): row[j] += prefix; prefix = prefix * t ** exps[j]
        else: prefix = prefix * t ** (-exps[j]); row[j] -= prefix
    return [sp.expand(x) for x in row]


def alexander(name):
    M = snappy.Manifold(name); G = M.fundamental_group(); gens, exps = abelian_free_map(G)
    A = sp.Matrix([fox(r, gens, exps) for r in G.relators()]); n = len(gens)
    # clear negative powers: multiply rows by a high power of t
    A = (A * t ** (4 * max(1, max(abs(e) for e in exps)) * 4)).applyfunc(sp.expand)
    minors = []
    for j in range(n):
        m = A[:, [k for k in range(n) if k != j]].det(method="berkowitz"); m = sp.factor(sp.expand(m))
        if m != 0: minors.append(sp.Poly(sp.expand(m), t))
    g = minors[0]
    for m in minors[1:]: g = sp.gcd(g, m)
    g = sp.Poly(g, t); # strip t^k factors
    coeffs = g.all_coeffs()
    while coeffs and coeffs[-1] == 0: coeffs.pop()
    p = sp.Poly(coeffs, t)
    return M, gens, exps, p


if __name__ == "__main__":
    for name in sys.argv[1:]:
        M, gens, exps, p = alexander(name)
        print(name[:30], "H1", M.homology(), "t-exponents", exps, "Delta =", p.as_expr(), "degree", p.degree(), "fibre genus (if fibred, one cusp) =", p.degree() / 2)
