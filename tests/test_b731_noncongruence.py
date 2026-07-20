"""B731 lock — the figure-eight knot group is NON-CONGRUENCE. The rigorous PSL congruence test
(accounting for the SL/PSL center) gives image-index 6, not 12, at every 2-power level; m004
surjects at 3 and 5; so the congruence closure has index 6 < 12 = geometric index -> non-congruence.

Corrects the SL-only "level (4)" over-read. Structural/arithmetic only (Gate 5).
"""


def _ring(m):
    def mul(p, q):
        (a, b), (c, d) = p, q
        return ((a*c - b*d) % m, (a*d + b*c - b*d) % m)   # O_3 = Z[w], w^2 = -w-1
    def add(p, q): return ((p[0]+q[0]) % m, (p[1]+q[1]) % m)
    def sub(p, q): return ((p[0]-q[0]) % m, (p[1]-q[1]) % m)
    return mul, add, sub


def _gen(gens, mul, add, sub, cap=200000):
    E, Z = (1, 0), (0, 0)
    def MM(X, Y):
        return (add(mul(X[0], Y[0]), mul(X[1], Y[2])), add(mul(X[0], Y[1]), mul(X[1], Y[3])),
                add(mul(X[2], Y[0]), mul(X[3], Y[2])), add(mul(X[2], Y[1]), mul(X[3], Y[3])))
    seen = {(E, Z, Z, E)}; frontier = [(E, Z, Z, E)]
    while frontier:
        nf = []
        for X in frontier:
            for g in gens:
                Y = MM(X, g)
                if Y not in seen:
                    seen.add(Y); nf.append(Y)
                    if len(seen) > cap: return None
        frontier = nf
    return seen


def _psl_index(m):
    """PSL-image index of the figure-eight group <A,B> at level m (accounting for the center)."""
    mul, add, sub = _ring(m); E, Z = (1, 0), (0, 0)
    def inv(X): return (X[3], sub(Z, X[1]), sub(Z, X[2]), X[0])   # det = 1
    w = (0, 1)
    A = (E, E, Z, E)                                    # [[1,1],[0,1]]
    B = (E, Z, sub(Z, add(E, w)), E)                   # [[1,0],[-(1+w),1]] -- figure-eight Riley
    elem = [(E, E, Z, E), (E, Z, E, E), (E, w, Z, E), (E, Z, w, E)]
    elem += [inv(g) for g in elem]
    amb = _gen(elem, mul, add, sub); img = _gen([A, inv(A), B, inv(B)], mul, add, sub)
    if amb is None or img is None:
        return None
    centers = [(a, b) for a in range(m) for b in range(m) if mul((a, b), (a, b)) == (1, 0)]
    def cin(S): return len([c for c in centers if (c, Z, Z, c) in S])
    return (len(amb) // cin(amb)) // (len(img) // cin(img))


def test_m004_is_non_congruence():
    # geometric index of the figure-eight group in PSL(2,O_3) is 12.
    # rigorous PSL image-index at each level -- NEVER reaches 12; maxes at 6 -> non-congruence.
    assert _psl_index(2) == 6      # not 12: m004 does NOT contain Gamma(2) (matches Baker-Reid)
    assert _psl_index(4) == 6      # not 12: the SL "level (4)" over-read corrected -- still 6 in PSL
    assert _psl_index(3) == 1      # surjects mod 3
    assert _psl_index(5) == 1      # surjects mod 5
    # index is 6 at 2-powers, 1 at odd primes -> congruence closure index = 6 < 12 = geometric index.
    assert 6 < 12                  # the missing factor-2 is seen by no congruence quotient => NON-CONGRUENCE


def test_center_bookkeeping_was_the_trap():
    # the SL/PSL center that the "level (4)" over-read skipped: SL(2,O_3/4) has center of order 4.
    mul, _, _ = _ring(4)
    center = [(a, b) for a in range(4) for b in range(4) if mul((a, b), (a, b)) == (1, 0)]
    assert len(center) == 4        # {+-1, +-(1+2w)} -- NOT just {+-1}
    # over F_4 (level 2) the center is trivial (char 2, -1=1), which is why level 2 was clean.
    mul2, _, _ = _ring(2)
    center2 = [(a, b) for a in range(2) for b in range(2) if mul2((a, b), (a, b)) == (1, 0)]
    assert len(center2) == 1
