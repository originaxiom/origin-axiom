#!/usr/bin/env python3
"""The 2T Wilson line, per quotient: B1263 found 48 surjections pi_1(m004) -> 2T in TWO Aut(2T)
classes.  For every surjection (enumerated here independently, in this bench's own presentation
< a, b | a w b^-1 w^-1 >, w = b a^-1 b^-1 a) compute the twisted Betti numbers of the 2T-irreps
that occur in 78|_2T and 27|_2T -- the trivial 1, the two characters omega, omega-bar (through
2T -> Z/3), and the 3-dimensional irrep (through 2T -> A4 acting on P^1(F3)) -- and hence the
4d spectrum of the Acharya-Witten reading with the 2T holonomy, for each quotient.

Everything exact (Fractions / roots of unity as Q(omega) pairs), Fox calculus, ranks over Q(omega).
"""
from __future__ import annotations
import os, sys, itertools, collections
from fractions import Fraction as F
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..',
                                'B1265_spectrum_law_rebuilt', 'verification'))   # the rebuilt 27-instrument
import e6_instrument as E
import spectrum_law as S
import transport as T

Qw, ONE, ZERO, OMEGA = E.Qw, E.ONE, E.ZERO, E.OMEGA

# ------------------------------------------------------------ SL(2, F_3) = 2T, exact enumeration
def sl2f3():
    out = []
    for p, q, r, s in itertools.product(range(3), repeat=4):
        if (p * s - q * r) % 3 == 1:
            out.append((p, q, r, s))
    return out


def mul(A, B):
    p, q, r, s = A
    t, u, v, w = B
    return ((p * t + q * v) % 3, (p * u + q * w) % 3, (r * t + s * v) % 3, (r * u + s * w) % 3)


def inv(A):
    p, q, r, s = A
    return (s % 3, (-q) % 3, (-r) % 3, p % 3)


ID = (1, 0, 0, 1)


def word_value(word, ga, gb):
    cur = ID
    for L in word:
        g = ga if abs(L) == 1 else gb
        cur = mul(cur, g if L > 0 else inv(g))
    return cur


def generated(gens):
    seen = {ID}
    frontier = [ID]
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = mul(x, g)
                if y not in seen:
                    seen.add(y)
                    nxt.append(y)
        frontier = nxt
    return seen


# ------------------------------------------------------------ the coefficient systems
def perm_matrix(g):
    """A4 = PSL(2,3) acting on P^1(F3) = {0,1,2,oo}: the 4x4 permutation matrix of g (exact)."""
    pts = [0, 1, 2, 'oo']
    p, q, r, s = g

    def mob(x):
        if x == 'oo':
            return 'oo' if r % 3 == 0 else (p * pow(r, -1, 3)) % 3
        num, den = (p * x + q) % 3, (r * x + s) % 3
        return 'oo' if den == 0 else (num * pow(den, -1, 3)) % 3
    P = np.zeros((4, 4), dtype=object)
    P[:] = F(0)
    for j, x in enumerate(pts):
        P[pts.index(mob(x)), j] = F(1)
    return P


def z3_character(g):
    """2T -> Z/3 = 2T / Q8: the abelianisation character; computed as the class of the element's
    image in the quotient by the normal Sylow-2 subgroup Q8 (the elements of order 1, 2, 4)."""
    # order of g
    o, cur = 1, g
    while cur != ID:
        cur = mul(cur, g)
        o += 1
    return o


def h1_qw(mats, invs, gens, relators):
    R = S.Rep(mats, invs)
    return S.h0_h1(R, gens, relators)


def main():
    G = sl2f3()
    assert len(G) == 24
    homs = [(a, b) for a in G for b in G if word_value(S.REL, a, b) == ID]
    surj = [(a, b) for (a, b) in homs if len(generated([a, b])) == 24]
    print(f"homomorphisms pi_1(m004) -> 2T: {len(homs)}; surjective: {len(surj)}   (B1263: 72 / 48)")
    # Q8 = the elements of order 1, 2, 4; the Z/3 character: coset of <Q8> -- compute via the
    # quotient map: pick omega-value from the order-3 part: g^8 has order dividing 3 (24 = 8*3)
    def z3_value(g):
        # g -> g^8 lies in the unique Sylow-3 subgroup's conjugates... use: the quotient 2T/Q8 = Z/3
        # is the abelianisation; compute via the class of g modulo Q8 by listing Q8 explicitly.
        Q8 = {x for x in G if z3_character(x) in (1, 2, 4)}
        assert len(Q8) == 8
        # cosets: g Q8
        cos = frozenset(mul(g, x) for x in Q8)
        return cos
    Q8 = {x for x in G if z3_character(x) in (1, 2, 4)}
    cosets = {}
    for g in G:
        cos = frozenset(mul(g, x) for x in Q8)
        cosets.setdefault(cos, len(cosets))
    assert len(cosets) == 3
    # a generator element of order 3 or 6 fixes which coset is omega; choose one order-3 element c0
    c0 = next(x for x in G if z3_character(x) == 3)
    cos_id = frozenset(Q8)
    cos_w = frozenset(mul(c0, x) for x in Q8)
    cos_w2 = frozenset(mul(mul(c0, c0), x) for x in Q8)
    def chi(g):
        cos = frozenset(mul(g, x) for x in Q8)
        return ONE if cos == cos_id else (OMEGA if cos == cos_w else OMEGA.conj())

    results = collections.Counter()
    detail = []
    for (a, b) in surj:
        # 3-dim irrep through A4: permutation rep minus trivial
        PA, PB = perm_matrix(a), perm_matrix(b)
        h0p, h1p = T.h1_frac_rep({1: PA, 2: PB}, {1: PA.T.copy(), 2: PB.T.copy()}, [1, 2], [S.REL])
        # trivial
        h1_triv = 1
        h1_3 = h1p - h1_triv
        # the two characters
        ca, cb = chi(a), chi(b)
        mats = {1: np.array([[ca]], dtype=object), 2: np.array([[cb]], dtype=object)}
        invs = {1: np.array([[ca.inv()]], dtype=object), 2: np.array([[cb.inv()]], dtype=object)}
        _, h1_w, _, _ = h1_qw(mats, invs, [1, 2], [S.REL])
        mats2 = {1: np.array([[ca.conj()]], dtype=object), 2: np.array([[cb.conj()]], dtype=object)}
        invs2 = {1: np.array([[ca.conj().inv()]], dtype=object), 2: np.array([[cb.conj().inv()]], dtype=object)}
        _, h1_wb, _, _ = h1_qw(mats2, invs2, [1, 2], [S.REL])
        key = (h1_3, h1_w, h1_wb, z3_character(a), z3_character(b))
        results[key] += 1
        detail.append((a, b, key))
    print("per surjection: (h1(3), h1(omega), h1(omega-bar), ord a, ord b) -> count")
    for k, v in sorted(results.items()):
        print("   ", k, "->", v)
    # the 4d spectrum of the AW reading with this holonomy (78 = 4.1 + 7w + 7wb + 20.3; 27 = 3.1+3w+3wb+6.3)
    for k in sorted(results):
        h3, hw, hwb = k[:3]
        n78 = 4 * 1 + 7 * hw + 7 * hwb + 20 * h3
        n27 = 3 * 1 + 3 * hw + 3 * hwb + 6 * h3
        print(f"   class {k[:3]}: chiral multiplets from the 78: {n78} (4 neutral + {n78-4} charged, in +-pairs);"
              f" if a 27 were a field on Q: h1(27) = h1(27bar) = {n27}")


if __name__ == "__main__":
    main()
