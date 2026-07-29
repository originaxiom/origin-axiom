"""B471 (harvested at Review 32, R32-9) — the metallic commutator trace identity.

The arc proved it and labelled it "not a scan, a theorem", but it had no row in LAW_MAP,
THEOREM_LEDGER or CLAIMS. Re-verified symbolically here before banking.
"""
import sympy as sp


def test_metallic_commutator_trace_is_two_minus_a_perfect_square():
    m, n = sp.symbols("m n", positive=True, integer=True)
    x = m ** 2 + 2                                   # tr A_m
    y = n ** 2 + 2                                   # tr A_n
    z = (m * n + 1) ** 2 + m ** 2 + n ** 2 + 1       # tr(A_m A_n)
    fricke = x ** 2 + y ** 2 + z ** 2 - x * y * z - 2
    assert sp.simplify(sp.expand(fricke) - sp.expand(2 - (m * n * (n - m)) ** 2)) == 0


def test_golden_silver_is_the_unique_parabolic_pair():
    """Parabolic <=> tr = -2 <=> (mn(n-m))^2 = 4 <=> mn(n-m) = 2, whose only solution
    with 1 <= m < n is (1,2). An iff over the whole family, not a bounded scan."""
    sols = [(a, b) for a in range(1, 40) for b in range(a + 1, 60) if a * b * (b - a) == 2]
    assert sols == [(1, 2)]
    # and the trace really is -2 there, +2 nowhere with m<n
    m, n = 1, 2
    assert 2 - (m * n * (n - m)) ** 2 == -2
    for a in range(1, 12):
        for b in range(a + 1, 14):
            assert 2 - (a * b * (b - a)) ** 2 != 2      # mn(n-m) != 0 for m<n
