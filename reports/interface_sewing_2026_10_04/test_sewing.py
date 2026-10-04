import importlib.util
from pathlib import Path

import sympy as sp

spec = importlib.util.spec_from_file_location("interface_sewing",Path(__file__).with_name("verify_sewing.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_cylinder_matching_and_wrong_sign_controls():
    assert all(m.cylinder_checks()["checks"].values())


def test_every_frozen_signed_cycle():
    result = m.graph_checks()
    assert len(result["rows"]) == 56
    assert all(all(row["checks"].values()) for row in result["rows"])
    assert result["gauge_covariance_checks"] == 64


def test_no_kinetic_form_or_unrelaxed_square_substitution():
    assert all(m.graph_checks()["controls"].values())


def test_residual_minimum_by_direct_gradient():
    L = m.cycle_matrix((1,1,1))
    x, u, v = sp.symbols("x u v",real=True)
    parameters = sp.Matrix([u,x,v])
    residual = L*parameters
    action = (residual.T*residual)[0]
    optimum = sp.solve(sp.diff(action,x),x)[0]
    R,Q,*_ = m.eliminate(L,[0,2])
    assert sp.expand(action.subs(x,optimum)-(sp.Matrix([u,v]).T*Q*sp.Matrix([u,v]))[0]) == 0
    assert sp.diff(action,x).subs(x,optimum) == 0
    assert Q != R and Q != R*R


def test_boundary_jump_is_not_zero_from_equal_values():
    a,b = sp.Rational(2),sp.Rational(3)
    values = sp.Matrix([0,1])
    jump = (m.response(a,0)+m.response(b,0))*values
    assert jump == sp.Matrix([-sp.Rational(5,6),sp.Rational(5,6)])
    assert jump != sp.zeros(2,1)
    assert (m.response(a,0)-m.response(a,0))*values == sp.zeros(2,1)
