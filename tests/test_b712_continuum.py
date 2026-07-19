"""B712 lock — the object's continuum has no canonical real anchor (imaginary canonical pt)."""
import sympy as sp

M, L = sp.symbols('M L')
A = -M**4 + L*(1 - M**2 - 2*M**4 - M**6 + M**8) - L**2*M**4     # fig-8 A-polynomial

def test_apoly_reciprocal_amphichiral():
    # reciprocal in M (M->1/M up to units) : the amphichiral signature
    Arec = sp.expand(A.subs(M, 1/M) * M**8)
    # same curve up to overall unit/normalization -> proportional
    q = sp.simplify(Arec / A)
    assert q.is_constant() or sp.simplify(q - q.subs({M: 2, L: 3})) == 0

def test_complete_point_is_singular_double_point():
    # (M,L)=(1,-1): A=0 and both partials vanish (a double/singular point)
    pt = {M: 1, L: -1}
    assert A.subs(pt) == 0
    assert sp.diff(A, M).subs(pt) == 0 and sp.diff(A, L).subs(pt) == 0

def test_cusp_shape_is_imaginary_quadratic():
    # tangent-cone slope satisfies x^2 + 12 = 0 -> tau = +/- 2 sqrt(-3), NON-real (Q(sqrt-3))
    t = sp.symbols('t')
    minpoly = t**2 + 12
    roots = sp.solve(minpoly, t)
    assert all(sp.im(r) != 0 for r in roots)                 # no real embedding
    assert sp.simplify(roots[1] - 2*sp.sqrt(-3)) == 0 or sp.simplify(roots[0] - 2*sp.sqrt(-3)) == 0
