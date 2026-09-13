"""B1402 — the three arithmetic cuts of the metallic family are one decomposition."""
import math
import numpy as np

PHI = (1 + 5 ** 0.5) / 2
R3 = np.array([[1, 1], [0, 1]], dtype=int)
L3 = np.array([[1, 0], [1, 1]], dtype=int)

# the theta-even forced values on the ear-independent branch, from B1349 addendum 2
LAM = {3: 0.5, 5: 0.0, 6: -1 / (2 * PHI), 9: -1 / (2 * PHI), 10: 0.0, 12: 0.5, 15: 1.0}


def _mp(M, k, n=3):
    P = np.eye(2, dtype=int)
    for _ in range(k):
        P = (P @ M) % n
    return P


def _order(gens, n=3):
    seen = {tuple((np.eye(2, dtype=int) % n).flatten())}
    frontier = [np.eye(2, dtype=int) % n]
    while frontier:
        nxt = []
        for X in frontier:
            for g in gens:
                Y = (X @ g) % n
                k = tuple(Y.flatten())
                if k not in seen:
                    seen.add(k); nxt.append(Y)
        frontier = nxt
    return len(seen)


def test_b996_criterion_reproduces():
    """B996's own stated list for m=1..7 is 24,24,1,24,24,1,24, and the shadow degenerates
    exactly when 3 | m."""
    orders = {m: _order([_mp(R3, m), _mp(L3, m)]) for m in range(1, 16)}
    assert [orders[m] for m in range(1, 8)] == [24, 24, 1, 24, 24, 1, 24]
    for m in range(1, 16):
        assert (orders[m] == 1) == (m % 3 == 0), m
        assert orders[m] in (1, 24), (m, orders[m])
    # CONTROL: |SL(2,Z/3)| really is 24, so "full" means full
    all_sl2 = _order([R3, L3])
    assert all_sl2 == 24, all_sl2


def test_the_decomposition():
    """gcd(m,15) > 1  <=>  (3|m) or (5|m)  <=>  (B996-degenerate) or (5|m)."""
    for m in range(1, 200):
        assert (math.gcd(m, 15) > 1) == (m % 3 == 0 or m % 5 == 0), m
    # and on the period, ear-independence is exactly that set
    assert sorted(LAM) == [m for m in range(1, 16) if math.gcd(m, 15) > 1]


def test_the_two_parts_carry_different_readouts():
    """3|m only -> the NONTRIVIAL values; 5|m only -> silent; both -> trivial 1."""
    only3 = [m for m in LAM if m % 3 == 0 and m % 5 != 0]
    only5 = [m for m in LAM if m % 5 == 0 and m % 3 != 0]
    both = [m for m in LAM if m % 15 == 0]
    assert only3 == [3, 6, 9, 12] and only5 == [5, 10] and both == [15]
    assert all(abs(LAM[m]) > 1e-9 for m in only3), "the B996-degenerate part must be non-silent"
    assert all(abs(LAM[m]) < 1e-9 for m in only5), "the 5-part must be silent"
    assert abs(LAM[15] - 1.0) < 1e-12
    assert sorted({round(LAM[m], 9) for m in only3}) == sorted({round(v, 9) for v in (-1 / (2 * PHI), 0.5)})


def test_golden_within_the_three_part_is_B997s_prime():
    """Within 3|m, the value is golden exactly when 5 | m^2+4, i.e. m = ±1 mod 5."""
    for m in (3, 6, 9, 12):
        golden = abs(LAM[m] + 1 / (2 * PHI)) < 1e-9
        assert golden == ((m * m + 4) % 5 == 0), m
        assert golden == (m % 5 in (1, 4)), m
    assert [m for m in (3, 6, 9, 12) if abs(LAM[m] + 1 / (2 * PHI)) < 1e-9] == [6, 9]


def test_the_mirror_speaks_where_mckay_access_dies():
    """The reading, as arithmetic: every m whose mod-3 shadow is the FULL 2T is ear-DEPENDENT
    (branch B, dead on two gates); the forced values live only where the shadow degenerates
    or the 5-part silences it."""
    for m in range(1, 16):
        full_2T = _order([_mp(R3, m), _mp(L3, m)]) == 24
        ear_independent = math.gcd(m, 15) > 1
        if full_2T and m % 5 != 0:
            assert not ear_independent, f"m={m}: full 2T must be ear-dependent"
    # the golden word itself: full 2T, and on the dead branch
    assert _order([_mp(R3, 1), _mp(L3, 1)]) == 24
    assert math.gcd(1, 15) == 1
    assert 1 * 1 + 4 == 5, "the golden's shadow modulus, prime -- B997's condition"
