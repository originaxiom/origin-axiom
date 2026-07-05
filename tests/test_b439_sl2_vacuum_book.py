"""Locks for B439 (C3) -- the child's SL(2,C) vacuum book (figure-eight core + slope control)."""
import os, sys
HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B439_sl2_vacuum_book")
sys.path.insert(0, HERE)
import vacuum_book as V
import sympy as sp


def test_child_slope5_spectrum():
    Q, facs = V.irreducible_factor_data(5)
    # exactly one reducible (t+2) and one irreducible quartic of disc -283 = the child trace field
    degs = sorted((deg, disc) for _, deg, disc in facs)
    assert degs == [(1, None), (4, -283)]


def test_reproduce_gate_vacuum_quartic_is_child_trace_field():
    assert V.quartic_is_child_trace_field() is True


def test_slope7_control_differs():
    Q, facs = V.irreducible_factor_data(7)
    degs = sorted((deg, disc) for _, deg, disc in facs)
    # 6 vacua, disc 50173 = 131*383 -- different count AND field from the child
    assert degs == [(1, None), (6, 50173)]
    assert 50173 == 131 * 383


def test_trace_poly_reduces_from_cooper_long():
    # the reciprocal M-polynomial really came from CL(M, M^-p): re-derive Q_5's leading data
    Q5 = V.vacuum_trace_poly(5)
    assert Q5.as_expr() == sp.sympify("t**5 - t**4 - 5*t**3 + 5*t**2 + 5*t - 2")
