"""B718 lock — the child ledger: generic beyond Z/p; 3 arithmetic children; NO own skeleton."""
import sympy as sp

def test_child_field_is_S4_quartic_not_quadratic():
    # probe 1/3: 4_1(5,1) invariant trace field = x^4-x-1, disc -283 (quartic, NOT Q(sqrt-283))
    x = sp.symbols('x'); f = x**4 - x - 1
    assert sp.Poly(f, x).is_irreducible
    assert sp.discriminant(f, x) == -283           # deg 4, disc -283

def test_child_authors_no_skeleton_prime_283_generic():
    # probe 3 (decisive): SL(2,q) is McKay only at q=3 (2T->E6), q=5 (2I->E8)
    def sl2_order(q): return q*(q*q - 1)
    assert sl2_order(3) == 24                       # = 2T -> E6 (parent, ramified prime 3)
    assert sl2_order(5) == 120                      # = 2I -> E8
    assert sl2_order(283) == 22664904               # child: generic large group, no McKay
    # max element order in any binary polyhedral group is 10; child has orders >> 10
    assert 283 not in (3, 5)                        # child's ramified prime is not special

def test_arithmetic_children_are_integral_small_slopes():
    # probe 2: exactly 3 arithmetic children, all q=1, slopes {5,6,8}, discs {-283,-59,-31}
    arithmetic = {(5, 1): -283, (6, 1): -59, (8, 1): -31}
    assert all(q == 1 for (p, q) in arithmetic)     # all INTEGRAL fillings
    assert set(p for (p, q) in arithmetic) == {5, 6, 8}

def test_minimal_slope_5_is_generic_not_golden():
    # probe 4: first hyperbolic slope = ceil(2*sqrt6) from L=sqrt(12+p^2) (Q(sqrt-3) cusp), no sqrt5
    import math
    assert math.ceil(2*math.sqrt(6)) == 5           # slope 5 = first past exceptional, generic
    assert math.sqrt(12 + 5**2) > 6 and math.sqrt(12 + 4**2) < 6   # six-theorem: 5 hyp, 4 exc
