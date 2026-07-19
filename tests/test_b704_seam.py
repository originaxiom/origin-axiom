"""B704 lock — the seam is an F_2-vector space (multiquadratic Galois + genus).
Pyenv-pure: the multiquadratic structure and the genus (disc-product) group law."""
import sympy as sp


def _squarefree(n):
    n = int(n); s = 1
    d = 2
    m = abs(n)
    while d * d <= m:
        while m % (d * d) == 0:
            m //= d * d
        d += 1
    s = m if n > 0 else -m
    return s


def test_stage_discriminants_and_genus_group_law():
    # stage p -> p* = (-1)^((p-1)/2) p (fiber-functor field disc, B700)
    star = {p: ((-1) ** ((p - 1) // 2)) * p for p in (3, 5, 7, 11, 13)}
    assert (star[3], star[5], star[7], star[11], star[13]) == (-3, 5, -7, -11, 13)
    # genus group law: p* * q* -> (pq)* up to squares (F_2-linear = disc multiplication)
    assert _squarefree(star[3] * star[5]) == -15    # being + hearing = meeting (B698/B699)
    assert _squarefree(star[3] * star[7]) == 21      # being + E6
    assert _squarefree(star[5] * star[7]) == -35     # hearing + E6
    assert _squarefree(star[3] * star[5] * star[7]) == 105  # the triple


def test_F2_vector_space_dimension():
    # k distinct multiquadratic generators -> Gal = (Z/2)^k, dim k over F_2
    # (verified in sage ref: Q(sqrt-3,sqrt5,sqrt-7) has degree 8 = 2^3)
    gens = [-3, 5, -7]
    assert len(gens) == 3
    # closure: the 2^3 = 8 elements are the subsets (F_2-span), 7 nonzero = the meetings
    from itertools import combinations
    meetings = set()
    for r in range(1, 4):
        for c in combinations(gens, r):
            p = 1
            for d in c:
                p *= d
            meetings.add(_squarefree(p))
    assert len(meetings) == 7  # 2^3 - 1 nonzero vectors


def test_audibility_types_the_basis():
    # a basis vector p* is audible <=> p* > 0 <=> p = 1 mod 4 (B702)
    for p in (3, 5, 7, 11, 13):
        star = ((-1) ** ((p - 1) // 2)) * p
        assert (star > 0) == (p % 4 == 1)
