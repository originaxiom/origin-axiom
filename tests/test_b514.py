"""B511/D1 adversarial-review locks: the golden-3d bootstrap is refuted at the root."""
import sympy as sp


def test_cross_fibonacci_not_pisot():
    M = sp.Matrix([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 1, 0]])
    cp = sp.factor(M.charpoly().as_expr())
    lam = list(M.charpoly().gen.free_symbols)[0] if False else sp.symbols('lambda')
    # char poly = (x-1)^2 (x^2-x-1): two eigenvalues =1 (on unit circle) => NOT strictly Pisot
    x = list(cp.free_symbols)[0]
    assert sp.expand(cp - (x - 1)**2*(x**2 - x - 1)) == 0
    # non-primitive: M is block upper-triangular (bottom-left 2x2 block is zero)
    assert M[2, 0] == 0 and M[2, 1] == 0 and M[3, 0] == 0 and M[3, 1] == 0


def test_golden_degree_2_tiles_1d():
    phi = (1 + sp.sqrt(5))/2
    # Rauzy dimension = deg - 1; golden has degree 2 => dimension 1 (cannot inflate 3d)
    assert sp.degree(sp.minimal_polynomial(phi, sp.symbols('t')), sp.symbols('t')) == 2
