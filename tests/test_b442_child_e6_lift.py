"""Locks for B442 (C4) — the E6 lift: composite data is -283-forced (Bin 3)."""
import os, sys
HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B442_child_e6_lift")
sys.path.insert(0, HERE)
import e6_lift as E
import sympy as sp


def test_e6_adjoint_decomposes_over_exponents():
    # Ad(78) = sum Sym^{2m_i}, m_i = E6 exponents -> meridian character degree 2*max = 22
    assert E.E6_EXPONENTS == [1, 4, 5, 7, 8, 11]
    assert sp.degree(E.e6_adjoint_char(), E.x) == 22


def test_e6_composite_data_in_neg283_field_both_knots():
    ch = E.e6_char_at_vacua(E.CHILD)
    fo = E.e6_char_at_vacua(E.FOREIGN)
    assert sp.degree(ch, E.x) <= 3 and sp.degree(fo, E.x) <= 3   # both in the -283 field
    assert ch != fo                                              # different values, same field


def test_galois_invariant_sum_rational():
    assert E.galois_invariant_sum(E.CHILD) == 5201
