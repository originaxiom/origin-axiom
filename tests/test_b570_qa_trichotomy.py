"""B570 Lane C, Q-A — locks: the trichotomy decided (see QA_RESULT.md).

  (1) rho-bar !~ rho: the geometric character is the Galois pair (5 +- sqrt(-3))/2,
      min poly t^2 - 5t + 7, disc -3 (non-real);
  (2) 'rho-bar ~ theta o rho' was never a separate branch: the F4-principal
      nilpotent is regular in E6 — Jordan type (17,9,1) on the 27 from BOTH
      gradings — so theta fixes a principal embedding pointwise;
  (3) sigma acts as the object's own mirror phi (Mostow + amphichirality);
  (4) the tangent real structure conj o theta fixes (theta-even)_R + i(theta-odd)_R:
      the theta-odd sector (C3's alive block) is the imaginary axes of sigma.
"""
import importlib.util
import os

import sympy as sp

_spec = importlib.util.spec_from_file_location(
    "qamod", os.path.join(os.path.dirname(__file__), "..",
                          "frontier", "B570_allowed_plays", "qa_trichotomy.py"))
qa = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(qa)


def test_galois_pair_kills_inner_equivalence():
    t, mp = qa.galois_pair()
    x = sp.Symbol('x')
    assert sp.expand(t - (5 + sp.sqrt(-3)) / 2) == 0
    assert sp.expand(mp.as_expr() - (x**2 - 5 * x + 7)) == 0
    assert sp.discriminant(mp) == -3
    assert sp.im(t) != 0                                   # non-real => rho-bar !~ rho
    assert sp.expand(t + sp.conjugate(t) - 5) == 0         # the Galois pair sums to 5
    assert sp.expand(t * sp.conjugate(t) - 7) == 0         # and multiplies to 7


def test_f4_principal_is_e6_regular():
    e6, f4 = qa.jordan_types()
    assert e6 == [17, 9, 1]
    assert f4 == [17, 9, 1]                                # F4-principal = E6-regular on the 27
    # => a principal sl2 lies inside F4 = E6^theta; theta fixes iota pointwise;
    #    'rho-bar ~ theta o rho' <=> 'rho-bar ~ rho' — both killed by the non-real trace.


def test_tangent_real_structure():
    # conj o theta on H^1 = C^6, theta = diag(1,1,1,1,-1,-1):
    # fixed points: theta-even coords real, theta-odd coords purely imaginary.
    th = sp.diag(1, 1, 1, 1, -1, -1)
    xs = sp.symbols('x0:6', real=True)
    ys = sp.symbols('y0:6', real=True)
    v = sp.Matrix([xs[i] + sp.I * ys[i] for i in range(6)])
    eqs = sp.expand(th * v.conjugate() - v)
    cons = set()
    for e in eqs:
        for part in (sp.re(e), sp.im(e)):
            if part != 0:
                cons.add(part)
    # even coords (0..3): -2*I*y_i pieces -> y_i = 0; odd coords (4,5): -2*x_i -> x_i = 0
    assert cons == {-2 * ys[0], -2 * ys[1], -2 * ys[2], -2 * ys[3], -2 * xs[4], -2 * xs[5]}
