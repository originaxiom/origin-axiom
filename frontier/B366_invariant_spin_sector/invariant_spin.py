"""B366 (first installment) -- the invariant-spin-sector lemmas: the gate's skeleton, exact.

Lemma 1 (the puncture): SL(2,Z) acting on the 2-torsion of T^2 fixes ONLY the origin; the three
nonzero points form one orbit (SL(2,Z/2) = S3). The puncture of the once-punctured fiber is the
unique MCG-invariant point.

Lemma 2 (the spin structures): under the classical action gamma:[a;b] -> [pa+rb+pr/2; qa+sb+qs/2]
(mod 1), the odd characteristic [1/2;1/2] is fixed by BOTH generators; the three even ones are
permuted transitively.

Identification (with B364/B365): the four level-30 spin-sector families are
   T+ = triangular            = [1/2, 0]   (T-multiplier verified in B364)
   T- = triangular x (-1)^n   = [1/2, 1/2] (THE ODD / invariant one)
   S+ = square                = [0, 0]
   S- = square x (-1)^n       = [0, 1/2]
Corollary (the forcing-shaped statement): the seam-bearing (a = 1/2, triangular/theta-lift) class
contains the unique invariant spin sector; the canonical (a = 0) class contains none (T swaps
[0,0] <-> [0,1/2]). Pre-registered prediction for the (properly-normalized) S-transformation
numerics: T- -> T-, S+ -> S+, T+ <-> S-.
"""
from fractions import Fraction as Fr


def sl2z2():
    seen = {(1, 0, 0, 1)}
    frontier = [(1, 0, 0, 1)]
    gens = [(1, 1, 0, 1), (0, 1, 1, 0)]
    while frontier:
        nxt = []
        for (a, b, c, d) in frontier:
            for (p, q, r, s) in gens:
                m = ((a * p + b * r) % 2, (a * q + b * s) % 2,
                     (c * p + d * r) % 2, (c * q + d * s) % 2)
                if m not in seen:
                    seen.add(m)
                    nxt.append(m)
        frontier = nxt
    return seen


def puncture_lemma():
    G = sl2z2()
    if len(G) != 6:
        return False
    orb0 = {((a * 0 + b * 0) % 2, (c * 0 + d * 0) % 2) for (a, b, c, d) in G}
    orb1 = {((a * 1 + b * 0) % 2, (c * 1 + d * 0) % 2) for (a, b, c, d) in G}
    return orb0 == {(0, 0)} and orb1 == {(1, 0), (0, 1), (1, 1)}


def act(gamma, ab):
    p, q, r, s = gamma
    a, b = ab
    return ((p * a + r * b + Fr(p * r, 2)) % 1, (q * a + s * b + Fr(q * s, 2)) % 1)


T = (1, 1, 0, 1)
S = (0, -1, 1, 0)
ODD = (Fr(1, 2), Fr(1, 2))
EVENS = [(Fr(0), Fr(0)), (Fr(0), Fr(1, 2)), (Fr(1, 2), Fr(0))]


def spin_lemma():
    odd_fixed = act(T, ODD) == ODD and act(S, ODD) == ODD
    # the three even characteristics are permuted transitively by <T, S>
    orbit = {EVENS[0]}
    frontier = [EVENS[0]]
    while frontier:
        nxt = []
        for ab in frontier:
            for g in (T, S):
                im = act(g, ab)
                if im not in orbit:
                    orbit.add(im)
                    nxt.append(im)
        frontier = nxt
    return odd_fixed and orbit == set(EVENS)


def forcing_shape():
    """the a=1/2 class contains the invariant sector; the a=0 class contains none."""
    a_half = [(Fr(1, 2), Fr(0)), (Fr(1, 2), Fr(1, 2))]
    a_zero = [(Fr(0), Fr(0)), (Fr(0), Fr(1, 2))]
    inv = [ab for ab in a_half + a_zero if act(T, ab) == ab and act(S, ab) == ab]
    return inv == [ODD] and ODD in a_half and ODD not in a_zero


if __name__ == "__main__":
    print("puncture lemma (unique invariant point):", puncture_lemma())
    print("spin lemma (odd unique invariant; evens one orbit):", spin_lemma())
    print("forcing shape (invariant sector lives in the a=1/2 / seam-bearing class):", forcing_shape())
