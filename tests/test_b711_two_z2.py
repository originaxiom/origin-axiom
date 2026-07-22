"""B711 lock — the two-Z/2 are orthogonal (V4); golden point = Galois-fixed real end."""
import sympy as sp

x, y = sp.symbols('x y')
CURVE = y**2 - (x**2 - 1)*y + (x**2 - 1)      # X(4_1) non-abelian char-variety curve

def test_geometric_point_in_Qsqrt_minus3():
    # x=2 -> y = (3 +/- sqrt(-3))/2 : the being field
    sols = sp.solve(CURVE.subs(x, 2), y)
    vals = set(sp.nsimplify(s) for s in sols)
    assert vals == {sp.Rational(3, 2) + sp.sqrt(-3)/2, sp.Rational(3, 2) - sp.sqrt(-3)/2}

def test_amphichiral_involution_swaps_the_conjugates():
    """REWIRED 2026-07-22 (fourth-pass audit): the original hardcoded yg and never
    consulted CURVE -- true by arithmetic for ANY yg with Re = 3/2 (MB12 class).
    Now: the involution j2:(x,y)->(x, x^2-1-y) must (a) preserve CURVE as a set
    (verified symbolically on the curve), and (b) swap the two GEOMETRIC roots
    obtained FROM the curve at x = 2."""
    # (a) j2 preserves the curve: substituting y -> x^2-1-y maps CURVE to itself
    j2_curve = sp.expand(CURVE.subs(y, (x**2 - 1) - y))
    assert sp.simplify(j2_curve - CURVE) == 0
    # (b) at x = 2, j2 swaps the curve's own two roots
    sols = sp.solve(CURVE.subs(x, 2), y)
    assert len(sols) == 2
    mapped = {sp.nsimplify(sp.expand((2**2 - 1) - s)) for s in sols}
    assert mapped == {sp.nsimplify(s) for s in sols}
    assert all(sp.simplify((2**2 - 1) - s - s) != 0 for s in sols)   # genuinely swapped, not fixed

def test_galois_fixed_points_only_at_x2_in_1_5():
    # disc_y of the curve in y = (x^2-1)^2 - 4(x^2-1) = (x^2-1)(x^2-5)
    disc = sp.discriminant(CURVE, y)
    assert sp.expand(disc - (x**2 - 1)*(x**2 - 5)) == 0
    # roots x^2 in {1,5}: x^2=5 is the GOLDEN point (sqrt5) = the hearing field's real fixed end
    assert set(sp.solve(disc, x)) == {-1, 1, -sp.sqrt(5), sp.sqrt(5)}
