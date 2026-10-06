"""Live cubic-boundary controls, not acceptance of a complete physical TOE."""
import importlib.util
from pathlib import Path

import sympy as s

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_nonlinear_boundary_2026_10_06'


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec);spec.loader.exec_module(out);return out


n=load('silver_nonlinear_native',BASE/'probe.py')
r=load('silver_nonlinear_reference',BASE/'reference.py')


def test_doublet_differential_and_Euler_on_complete_bound():
    a,na=n.super_checks();b,nb=r.polynomial_controls()
    assert na==nb and na>100
    assert all(a.values()) and all(b.values())


def test_odd_sign_is_mathematical_not_boolean_label():
    assert n.mul(n.odd(0),n.odd(1))==n.scale(n.mul(n.odd(1),n.odd(0)),-1)
    assert n.mul(n.odd(0),n.odd(0))=={}
    assert r.product(r.variable(0,True),r.variable(0,True))=={}


def test_nonzero_cubic_is_exact_with_required_sign():
    F=n.scale(n.mul(n.even(0),n.mul(n.even(1),n.even(2))),-s.Rational(1,2))
    cubic=n.scale(n.delta(F),-1)
    actual,remaining=n.primitive(cubic)
    assert cubic and actual==F and remaining=={}
    assert n.add(cubic,n.delta(actual))=={}
    assert n.add(cubic,n.delta(n.scale(actual,-1)))!={}


def test_mixed_harmonic_legs_are_not_counted_in_Euler_denominator():
    F=n.mul(n.odd(3),n.mul(n.odd(4),n.even(0)))
    cubic=n.delta(F);sol,rem=n.primitive(cubic)
    assert cubic and rem=={} and n.add(cubic,n.delta(sol))=={}
    assert all(n.number(key)==1 for key in cubic)


def test_harmonic_obstruction_is_preserved_not_misreported_as_solved():
    obs=n.mul(n.odd(3),n.mul(n.even(3),n.even(3)))
    solution,remaining=n.primitive(obs)
    assert obs and n.delta(obs)=={} and solution=={} and remaining==obs


def test_disabled_pair_differential_cannot_cancel_actual_cubic():
    F=n.mul(n.even(0),n.mul(n.even(1),n.even(2)))
    cubic=n.delta(F)
    assert cubic and n.add(cubic,{})!={}
    assert n.add(cubic,n.delta(n.scale(F,-1)))=={}


def test_actual_nonabelian_CS_three_mode_coefficients_and_compact_control():
    a,means=n.trigonometric_controls();b,other=r.fourier_controls()
    assert means==other==['1/2']*3
    assert a['compact_SU5_generators'] and b['SU5_compact_matrices']
    assert a['bulk_cubic_survives'] and b['nonzero_bulk_trace']


def test_nonlinear_curvature_cancellation_not_erasure_of_old_escape():
    a,_=n.trigonometric_controls();b,_=r.fourier_controls()
    assert a['gauge_orbit_curvature_quadratic'] and a['gauge_orbit_curvature_cubic']
    assert b['quadratic_curvature_cancels'] and b['cubic_curvature_cancels']
    assert a['linear_flat_space_escape_preserved'] and b['old_linear_escape_not_deleted']


def test_counterterm_is_a_nonzero_cost_with_wrong_sign_control():
    a,_=n.trigonometric_controls();b,_=r.fourier_controls()
    assert a['graph_primitive_not_automatically_zero'] and b['graph_primitive_nonzero']
    assert a['priced_graph_counterterm_cancels'] and b['counterterm_cancels']
    assert a['wrong_counterterm_sign_detected'] and b['opposite_counterterm_fails']


def test_two_algorithms_agree_on_all_declared_profiles():
    a=n.run();b=r.run()
    assert a['failed']==b['failed']==[] and a['profile']==b['profile']
    assert all(a['checks'].values()) and all(b['checks'].values())


def test_degree_bound_includes_constants_and_harmonic_only_rows():
    rows=list(n.monomials())
    assert ((0,0,0,0),()) in rows
    assert ((0,0,0,2),(3,)) in rows
    assert ((1,1,1,0),()) in rows
    assert len(set(rows))==len(rows)
