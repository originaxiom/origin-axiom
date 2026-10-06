"""Actual-cusp cyclic hypotheses and negative controls, not physical TOE acceptance."""
import importlib.util
from pathlib import Path

import sympy as s

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_cyclic_transfer_2026_10_06'


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path);out=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(out);return out


n=load('cyclic_transfer_native_test',BASE/'probe.py')
r=load('cyclic_transfer_reference_test',BASE/'reference.py')


def test_actual_literal_coefficient_is_not_a_single_log_direction():
    _,_,_,p,q,a,b=n.literal()
    assert n.exp_nil(a)==p and n.exp_nil(b)==q
    assert n.rank(s.Matrix.hstack(s.Matrix(list(a)),s.Matrix(list(b))))==2
    assert not n.zero(a) and not n.zero(b) and n.zero(n.mm(a,b)-n.mm(b,a))


def test_dual_positive_metric_is_not_automatically_cyclic():
    *_,a,b=n.literal();E=n.sdr(a,b);D=n.sdr(-a.T,-b.T)
    assert all(n.cyclic_residual(E,D).values())
    bad=n.sdr(-a.T,-b.T,s.diag(1,2,3,4,5))
    assert n.zero(n.mm(bad['d'],bad['h'])+n.mm(bad['h'],bad['d'])-(s.eye(20)-bad['p']))
    assert not n.cyclic_residual(E,bad)['h']


def test_homotopy_sign_is_detected_on_the_actual_nontrivial_complex():
    *_,a,b=n.literal();E=n.sdr(a,b);d,h,p=E['d'],E['h'],E['p']
    assert not n.zero(d)
    assert n.zero(n.mm(d,h)+n.mm(h,d)-(s.eye(20)-p))
    assert not n.zero(n.mm(d,-h)+n.mm(-h,d)-(s.eye(20)-p))


def test_group_cell_and_log_cups_agree_on_all_closed_cocycles():
    *_,a,b=n.literal()
    for x,y in ((a,b),(n.exterior_lie(a),n.exterior_lie(b))):
        assert all(n.cell_comparison(x,y)['checks'].values())
    *_,ar,br=r.literal()
    for x,y in ((ar,br),(r.wedge_derivative(ar),r.wedge_derivative(br))):
        assert all(r.cell_checks(x,y).values())


def test_gauge_leaf_cases_cover_internal_and_root_propagators():
    assert n.gauge_case((None,(None,None)),0)=='root_propagator'
    assert n.gauge_case(((None,(None,None)),None),0)=='internal_propagator'
    assert n.gauge_case(((None,None),None),0)=='harmonic'
    assert set(r.parent_cases('(x(xx))'))=={'root_propagator','harmonic'}


def test_tree_enumeration_has_the_complete_catalan_counts():
    expected=[1,1,2,5,14,42,132]
    assert [len(n.trees(i)) for i in range(1,8)]==expected
    assert [len(r.words(i)) for i in range(1,8)]==expected
    assert all(len(r.parent_cases(x))==i for i in range(2,8) for x in r.words(i))


def test_complete_parent_degrees_and_polarization_are_retained():
    out=n.run();profile=out['profile']
    assert profile['full_coefficient_dimension']==248
    assert profile['full_H']==[100,200,100] and profile['Ah_dimensions']==[24,100,76]
    assert out['native_only_flag_dimensions_checked']=={'W':5,'F':7}
    assert profile['boundary_betti']['N']==[6,12,6]
    assert profile['boundary_betti']['W']==profile['boundary_betti']['Wdual']==[2,4,2]
    assert profile['boundary_betti']['F']==profile['boundary_betti']['Fdual']==[3,6,3]


def test_two_exact_algorithms_agree_without_physical_overclaim():
    a,b=n.run(),r.run()
    assert a['profile']==b['profile'] and a['failed']==b['failed']==[]
    assert a['checks'] and b['checks'] and all(a['checks'].values()) and all(b['checks'].values())
    for k in ('all_order_charged_physical_completion','physical_action_stationary',
              'genesis_boundary_selected','physical_goal_achieved','non_author_acceptance'):
        assert a[k] is b[k] is False


def test_nonunitary_neutral_trace_is_not_confused_with_positive_gram():
    basis=n.adjoint_basis();trace=s.Matrix([[s.trace(x*y) for y in basis] for x in basis]);metric=s.Matrix([[s.trace(x.T*y) for y in basis] for x in basis])
    assert trace!=metric and n.rank(trace)==n.rank(metric)==24
    assert metric==s.diag(s.eye(20),s.eye(4)+s.ones(4))
    *_,a,b=n.literal();N=n.sdr(n.adjoint_lie(a,basis),n.adjoint_lie(b,basis),metric)
    assert all(n.cyclic_residual(N,trace=trace).values())
