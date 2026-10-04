"""R95 LIVE tensor, field and variational checks; no physical-value claim."""
import importlib.util
from pathlib import Path
import sympy as sp

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05'
spec=importlib.util.spec_from_file_location('r95_trace_parent',BASE/'trace_parent.py')
native=importlib.util.module_from_spec(spec);spec.loader.exec_module(native)


def test_even_symmetric_tensor_group_map_and_its_lost_lifts():
    a=sp.Matrix([[2,1],[1,1]]);b=sp.Matrix([[1,2],[0,1]])
    assert native.symmetric(a*b)==native.symmetric(a)*native.symmetric(b)
    assert native.symmetric(-a)==native.symmetric(a)
    assert native.symmetric(-sp.eye(2))==sp.eye(5)
    assert native.symmetric(-sp.eye(2),3)!=sp.eye(4)


def test_complete_E8_roster_and_trace_not_just_dimension():
    r=native.roots_roster()
    assert r['actual']==r['expected'] and r['actual']!=r['wrong']
    assert len(r['roots'])==240 and sum(r['actual'].values())==248
    assert sp.expand(r['trace_root']-60*r['trace5'])==0


def test_actual_hyperbolic_background_all_residuals_and_positive_norm():
    g=native.geometry()
    assert all(native.zero(x) for x in g['curvature'])
    assert native.zero(g['div']+g['bracket'])
    assert not native.zero(g['div']) and not native.zero(g['flat_moment'])
    assert g['norm']==30 and native.geometry(3)['norm']==15


def test_full_centralizer_kernels_reject_rank_five_surrogate():
    assert native.sector_kernels()==(0,0,0)
    fake=native.sector_kernels(3,True)
    assert 24+20*fake[0]+10*fake[1]+fake[2]==55


def test_positive_operator_duality_includes_the_adjoint():
    g=native.geometry();J=g['J']
    assert J.H*J==sp.eye(5) and J.T==J
    for C in g['C']:
        assert native.zero(J*C+C.T*J)
        assert native.zero(J*C.H+C.conjugate()*J)


def test_same_parent_trace_and_cubic_variation_coefficients():
    values=native.checks()
    assert all(v for k,v in values.items() if k.startswith(('trace20_','trace1200_','CS_cubic_')))
    assert values['Goldman_trace_gradient'] and values['derived_boundary_scale4800']
    assert values['wrong_Goldman_half_factor_rejected']


def test_nonlinear_registered_relation_retained_with_actual_sign():
    values=native.checks()
    for k in ('same_nonlinear_generating_primitive','scaled_registered_first_variation',
              'unflipped_registered_relation_rejected','nonreal_geometric_chart_0','nonreal_geometric_chart_1'):
        assert values[k]
    for i in range(3):assert values['actual_R94_trace_map_'+str(i)]


def test_separate_fraction_tensor_metric_root_and_kernel_route():
    s=importlib.util.spec_from_file_location('r95_reference_live',BASE/'trace_parent_reference.py')
    module=importlib.util.module_from_spec(s);s.loader.exec_module(module)
    d=module.report()
    assert d['checks'] and d['failed']==[] and all(d['checks'].values())
