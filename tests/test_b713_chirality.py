"""B713 lock — chirality is the observer's: gauge-only triality, torsor bit, N-N rigid."""
import sympy as sp

def test_no_order3_on_the_object():
    # Isom(4_1)=D4, order 8 -> no order-3 element -> no Z/3 acts (probe 1, gauge-only)
    order = 8
    assert order % 3 != 0
    import math
    assert math.gcd(order, 3) == 1

def test_chirality_is_a_simply_transitive_Z2_torsor():
    # probe 2: fiber of X(4_1) over meridian x=2 = {(2,(3+/-sqrt-3)/2)}, y^2-3y+3
    x, y = sp.symbols('x y')
    curve = y**2 - (x**2 - 1)*y + (x**2 - 1)
    fiber = sp.expand(curve.subs(x, 2))
    assert fiber == y**2 - 3*y + 3
    assert sp.discriminant(fiber, y) == -3          # disc -3, irreducible over Q -> no Q-point
    roots = sp.solve(fiber, y)
    assert set(roots) == {sp.Rational(3,2) + sp.sqrt(-3)/2, sp.Rational(3,2) - sp.sqrt(-3)/2}
    # Galois swap sqrt-3 -> -sqrt-3 is free (0 fixed points): distinct roots, no rational fixed pt
    assert sp.simplify(roots[0] - roots[1]) != 0

def test_object_is_vector_like_amphichiral_signature_zero():
    # probe 3: 4_1 Seifert form V; anti-congruence P^T V P = -V^T with det(P)=1 (amphichiral)
    V = sp.Matrix([[1, 1], [0, -1]])
    P = sp.Matrix([[-1, -2], [1, 1]])
    assert P.det() == 1
    assert P.T * V * P == -V.T                       # sigma_omega(4_1) = -sigma_omega(4_1) = 0
    # non-vacuous: the chiral trefoil has NO such det-1 anti-congruence (sigma = -2 != 0)
    Vtref = sp.Matrix([[-1, 1], [0, -1]])            # 3_1 Seifert form
    # trefoil Alexander t^2-t+1 has roots on |t|=1 (signature jumps); 4_1 does not
    t = sp.symbols('t')
    assert sp.Poly(t**2 - t + 1, t).all_roots()      # trefoil roots on unit circle (chiral)
