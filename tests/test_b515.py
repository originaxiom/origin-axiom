"""B515 locks — golden 3d is real: beta = phi(1+sqrt phi)."""
import sympy as sp

x = sp.symbols('x')
phi = (1 + sp.sqrt(5))/2


def test_beta_is_golden_derived():
    beta = phi*(1 + sp.sqrt(phi))
    assert sp.simplify(beta**2 - (2*phi*beta + phi)) == 0            # beta^2 = 2 phi beta + phi
    assert sp.expand(sp.minimal_polynomial(beta, x) - (x**4 - 2*x**3 - 5*x**2 - 4*x - 1)) == 0


def test_quartic_is_unimodular_pisot_golden():
    q = x**4 - 2*x**3 - 5*x**2 - 4*x - 1
    assert sp.Poly(q, x).is_irreducible
    assert q.subs(x, 0) == -1                                        # unimodular (unit)
    mags = sorted(abs(complex(sp.N(r, 20))) for r in sp.Poly(q, x).all_roots())
    assert mags[-1] > 1.0001 and mags[-2] < 0.9999                   # Pisot
    # contains sqrt5: factors over Q(sqrt5) into two quadratics
    degs = sorted(sp.degree(f, x) for f, _ in sp.factor_list(q, extension=sp.sqrt(5))[1])
    assert degs == [2, 2]
