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
    # j2:(x,y)->(x, x^2-1-y) sends rho_geom -> rho_geom-bar
    yg = sp.Rational(3, 2) + sp.sqrt(-3)/2
    j2y = (2**2 - 1) - yg
    assert sp.simplify(j2y - (sp.Rational(3, 2) - sp.sqrt(-3)/2)) == 0

def test_galois_fixed_points_only_at_x2_in_1_5():
    # disc_y of the curve in y = (x^2-1)^2 - 4(x^2-1) = (x^2-1)(x^2-5)
    disc = sp.discriminant(CURVE, y)
    assert sp.expand(disc - (x**2 - 1)*(x**2 - 5)) == 0
    # roots x^2 in {1,5}: x^2=5 is the GOLDEN point (sqrt5) = the hearing field's real fixed end
    assert set(sp.solve(disc, x)) == {-1, 1, -sp.sqrt(5), sp.sqrt(5)}
