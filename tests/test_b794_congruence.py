"""B794 — locks on cc3's two congruence theorems (independently re-derived).

THEOREM 1: Gamma_41 is a congruence subgroup of level exactly (4).
THEOREM 2: every Gamma_41 trace norm is == 0 or 3 (mod 4), never 1.
Plus the structural corollary that explains B791's coset-image order 1920.
"""

def _ring():
    def radd(x, y): return ((x[0] + y[0]) % 4, (x[1] + y[1]) % 4)
    def rsub(x, y): return ((x[0] - y[0]) % 4, (x[1] - y[1]) % 4)
    def rmul(x, y):
        a, b = x; c, d = y
        return ((a * c - b * d) % 4, (a * d + b * c - b * d) % 4)
    return radd, rsub, rmul


ONE, ZERO = (1, 0), (0, 0)
I = ((ONE, ZERO), (ZERO, ONE))


def _ops():
    radd, rsub, rmul = _ring()
    def mmul(M, N):
        return tuple(tuple(radd(rmul(M[i][0], N[0][j]), rmul(M[i][1], N[1][j]))
                           for j in range(2)) for i in range(2))
    def det(M): return rsub(rmul(M[0][0], M[1][1]), rmul(M[0][1], M[1][0]))
    def closure(gens):
        seen, fr = {I}, [I]
        while fr:
            nx = []
            for M in fr:
                for g in gens:
                    P = mmul(M, g)
                    if P not in seen: seen.add(P); nx.append(P)
            fr = nx
        return seen
    return mmul, det, closure, radd


def test_sl2_mod_pmI_order_is_1920_explaining_the_bank_coset_image():
    """1920 is not a coincidence: it IS |SL(2,Z[w]/4)/{+-I}|. 2 is inert, so |Z[w]/4| = 16.

    NAMING CORRECTED 2026-07-29 (Chat-1's catch): this is NOT PSL(2,Z[w]/4). The centre of
    SL(2,Z[w]/4) has order 4 -- lambda^2 = 1 has FOUR solutions (1, 1+2w, 3, 3+2w) -- so the
    true PSL has order 960. PSL(2,O_3) maps into SL/{+-I} because O_3 is a domain whose only
    square roots of 1 are +-1; the extra central elements do not come from O_3. Both cc and
    cc3 used the right group under the wrong name.
    """
    _, det, _, _ = _ops()
    _, _, rmul = _ring()
    R = [(a, b) for a in range(4) for b in range(4)]
    assert len(R) == 16
    SL = [((a, b), (c, d)) for a in R for b in R for c in R for d in R
          if det(((a, b), (c, d))) == ONE]
    assert len(SL) == 3840                    # the bank's ambient_order
    assert len(SL) // 2 == 1920               # |SL/{+-I}| -- the bank's coset-image order
    # and the true centre has order 4, so the TRUE PSL is 960 -- the distinction that
    # resolves B731's index 6 (= 960/160) against our 12 (= 1920/160). Both correct, in
    # different groups; ours is the one PSL(2,O_3) actually maps to.
    sq1 = [l for l in R if rmul(l, l) == ONE]
    assert len(sq1) == 4                      # 1, 1+2w, 3, 3+2w
    assert len(SL) // len(sq1) == 960          # the TRUE |PSL(2,Z[w]/4)|


def test_theorem1_gamma41_is_congruence_of_level_exactly_4():
    mmul, det, closure, _ = _ops()
    A = ((ONE, ONE), (ZERO, ONE))
    B = ((ONE, ZERO), ((0, 3), ONE))          # -w mod 4
    H = closure([A, B])
    minusI = (((3, 0), ZERO), (ZERO, (3, 0)))
    assert len(H) == 320 and minusI in H
    Hbar = len(H) // 2
    assert Hbar == 160
    assert 1920 // Hbar == 12                 # == [PSL(2,O_3) : Gamma_41] => Gamma(4) <= Gamma_41
    # surjectivity of the reduction, so the index comparison is legitimate
    T = ((ONE, ONE), (ZERO, ONE))
    U = ((ONE, (0, 1)), (ZERO, ONE))
    S = ((ZERO, (3, 0)), (ONE, ZERO))
    assert len(closure([T, U, S])) == 3840
    # level is EXACTLY 4: the mod-2 image is proper, of index 6 != 12, so Gamma(2) is not inside
    def to2(M):
        return tuple(tuple((M[i][j][0] % 2, M[i][j][1] % 2) for j in range(2)) for i in range(2))
    H2 = {to2(M) for M in H}
    assert len(H2) == 10                       # D_5 inside SL(2,F_4) = A_5
    assert 60 // len(H2) == 6 != 12


def test_theorem2_trace_norms_avoid_1_mod_4():
    mmul, det, closure, radd = _ops()
    A = ((ONE, ONE), (ZERO, ONE))
    B = ((ONE, ZERO), ((0, 3), ONE))
    H = closure([A, B])
    def norm(x): a, b = x; return (a * a - a * b + b * b) % 4
    norms = {norm(radd(M[0][0], M[1][1])) for M in H}
    assert norms == {0, 3}
    assert 1 not in norms


def test_cc_mod4_hint_is_refuted_by_the_theorem():
    """cc's H-B788-NORMSPLIT claimed m004-only norms are all == 0 mod 4. The real law is
    {0,3}; the odd norms that refute it are all == 3, hence consistent with the theorem."""
    for x in (7, 103, 127, 175, 367):
        assert x % 4 == 3
        assert x % 4 != 0                      # refutes the narrower claim
