"""Law-harvest R32-9 — three arcs that carried unregistered results (B534, B533, B120).

Each is re-verified here rather than trusted from the arc's own FINDINGS.
Strength labels differ and are respected: B534/B533 are proved in-arc (THEOREM);
B120 carries no proof tag, so it banks as a LAW (exact on every computed instance).
"""
from sympy import Matrix, eye, lucas, fibonacci, sqrt, simplify


def test_b534_all_n_lucas_identity():
    """det(A^n - I) = 2 - L(2n) with A = [[2,1],[1,1]], and the parity split."""
    A = Matrix([[2, 1], [1, 1]])
    for n in range(1, 16):
        assert (A ** n - eye(2)).det() == 2 - lucas(2 * n)
    for n in range(1, 16, 2):                       # odd
        assert lucas(2 * n) - 2 == lucas(n) ** 2
    for n in range(2, 16, 2):                       # even
        assert lucas(2 * n) - 2 == 5 * fibonacci(n) ** 2


def test_b533_sqrt_phi_and_beta_identities():
    phi = (1 + sqrt(5)) / 2
    tau = sqrt(phi)
    assert simplify(tau ** 4 - tau ** 2 - 1) == 0    # tau is a root of x^4 - x^2 - 1
    beta = 1 / (tau - 1)
    assert simplify(beta * (tau - 1) - 1) == 0       # beta = 1/(sqrt(phi) - 1)


def _cnt(n, h):
    """B120 height count. The h == n clause PRECEDES the h in {1,2} clause; the two
    overlap only at n = 2, where mis-ordering produces a spurious mismatch."""
    if h == 0:
        return n - 1
    if h == n:
        return 2
    if h in (1, 2):
        return 2 * (n - 2)
    if 3 <= h <= n - 1:
        return 2 * (n - h)
    return 0


def test_b120_height_counts_sum_to_n_squared_minus_one():
    for n in range(2, 14):
        assert sum(_cnt(n, h) for h in range(0, n + 1)) == n * n - 1


def test_b120_clause_precedence_is_load_bearing_at_n_equals_two():
    """Guard the exact transcription error cc made: with the wrong clause order, n=2 fails."""
    def wrong(n, h):
        if h == 0: return n - 1
        if h in (1, 2): return 2 * (n - 2)
        if h == n: return 2
        if 3 <= h <= n - 1: return 2 * (n - h)
        return 0
    assert sum(wrong(2, h) for h in range(0, 3)) != 3     # the false mismatch
    assert sum(_cnt(2, h) for h in range(0, 3)) == 3      # correct order
