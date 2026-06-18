"""B179 -- the metallic numbers unified (V173). Fast symbolic locks.

Every geometric/arithmetic metallic number is an exact function of lambda_m (root of x^2-mx-1):
alpha_m=1/lambda_m, the bundle trace m^2+2=lambda_m^2+alpha_m^2, the field discriminant m^2+4=(lambda_m+
alpha_m)^2, the Hurwitz constant 1/sqrt(m^2+4)=1/(lambda_m+alpha_m). Pure algebra; the do-not-conflate
boundary lives in metallic_unified.py.
"""
import sympy as sp

m, x = sp.symbols('m x', positive=True)
s = sp.sqrt(m**2 + 4)
lam = (m + s) / 2
alp = (s - m) / 2


def test_reciprocal_and_sum_difference():
    assert sp.simplify(lam * alp - 1) == 0          # alpha = 1/lambda
    assert sp.simplify(lam - alp - m) == 0          # difference = m
    assert sp.simplify(lam + alp - s) == 0          # sum = sqrt(m^2+4)


def test_characteristic_equations():
    assert sp.simplify(lam**2 - m * lam - 1) == 0
    assert sp.simplify(alp**2 + m * alp - 1) == 0


def test_bundle_trace_and_field_and_hurwitz():
    M = sp.Matrix([[m, 1], [1, 0]])
    assert M.trace() == m and M.det() == -1
    assert sp.simplify((M**2).trace() - (m**2 + 2)) == 0          # bundle trace
    assert sp.simplify(lam**2 + alp**2 - (m**2 + 2)) == 0
    assert sp.discriminant(sp.Poly(x**2 - m * x - 1, x)) == m**2 + 4   # field disc
    assert sp.simplify((lam + alp)**2 - (m**2 + 4)) == 0
    assert sp.simplify(1 / (lam + alp) - 1 / s) == 0             # Hurwitz constant


def test_golden_collapse():
    phi = (1 + sp.sqrt(5)) / 2
    assert sp.simplify(lam.subs(m, 1) - phi) == 0               # lambda_1 = phi
    assert sp.simplify(phi - 1 - 1 / phi) == 0                  # alpha_1 = 1/phi = phi-1
    assert sp.simplify(phi**2 - phi - 1) == 0                   # phi^2 = phi+1
