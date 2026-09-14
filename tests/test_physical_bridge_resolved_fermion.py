"""R30 exact/domain controls; not global PDE or full physical certification."""
import importlib.util
from pathlib import Path

import pytest
import sympy as sp

PATH=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/resolved_fermion.py'
SPEC=importlib.util.spec_from_file_location('physical_bridge_resolved_fermion',PATH)
M=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def test_absolute_domain_is_maximal_isotropic_and_preserves_grading():
    for row in M.boundary_and_action()['boundaries']:
        assert row['rank']==row['annihilator_dimension']==4
        assert row['projector'] and row['isotropic'] and row['parity_preserved']


def test_full_transmission_not_just_tangential_pullback():
    d=M.boundary_and_action()
    assert d['full_transmission'] and d['transmission_annihilator']==8
    assert d['tangent_only_residual']!=0


def test_action_uses_actual_hermitian_odd_clifford_matrices():
    d=M.boundary_and_action()
    assert d['hermitian'] and d['odd']
    for i in range(3):
        assert d['gauge_current_matrices'][i]==-sp.I*d['q']*d['c'][i]
        assert d['higgs_current_matrices'][i]==d['q']*d['mass'][i]
        assert d['higgs_current_matrices'][i]!=sp.zeros(8)


def test_weighted_conjugacy_on_every_form_not_unweighted_isometry():
    rows=M.conjugacy()['rows']
    assert len(rows)==8 and all(r['identity'] for r in rows)
    assert any(r['wrong_sign_nonzero'] for r in rows)
    F=sp.symbols('F',real=True)
    assert sp.exp(-2*F)*sp.exp(F)**2==1
    assert sp.exp(F)**2!=1


def test_scalar_square_domain_has_witten_robin_condition():
    d=M.conjugacy()
    assert d['robin']==0
    assert d['undeformed_neumann']!=0 and d['wrong_robin']!=0


@pytest.mark.parametrize('k',range(5))
def test_exact_chain_homotopy_recovers_base_for_nonzero_attachment(k):
    d=M.contraction(k)
    assert all(d[key] for key in ('nilpotent','retract','chain0','chain1','homotopy0','homotopy1'))
    assert d['discarded_core_has_nonzero_homotopy']==(k>0)


@pytest.mark.parametrize('xy,base',[
    ((1,1),[1,2,1,0]),((-1,1),[0,0,0,0]),((sp.I,1),[0,0,0,0]),
    (((-3+sp.I*sp.sqrt(7))/4,)*2,[0,1,1,0]),
    (((-3-sp.I*sp.sqrt(7))/4,)*2,[0,1,1,0]),
])
def test_actual_fox_loci_have_distinct_absolute_kernels(xy,base):
    d=M.glued(*xy,3,1)
    assert d['base']==d['betti']==base
    A,B=d['d0'],d['d1']
    lap=[A.H*A,A*A.H+B.H*B,B*B.H]
    assert [H.rows-H.rank() for H in lap]==base[:3]


def test_generic_split_three_odd_and_three_even_then_none_at_finite_attachment():
    assert M.glued(-1,1,3,0)['betti']==[3,3,0,0]
    assert M.glued(-1,1,3,0)['relative']==[0,3,0,0]
    assert M.glued(-1,1,3,sp.Rational(1,2))['betti']==[0,0,0,0]


def test_nontrivial_c3_orbit_and_unitary_core_phases_do_not_change_resolved_count():
    z=(-1+sp.I*sp.sqrt(3))/2
    for x in (z,sp.conjugate(z)):
        assert M.glued(x,1,3,1)['betti']==[0,0,0,0]
    for t in (0,1):
        assert M.glued(-1,1,3,t,[1,sp.I,-1])['betti']==M.glued(-1,1,3,t)['betti']


def test_singular_attachment_retains_a_pair_so_gluing_test_can_fail():
    d=M.glued(-1,1,3,attachment=sp.diag(1,1,0))
    assert d['betti']==[1,1,0,0]
    assert d['betti']!=d['base']


def test_nonunitary_character_and_inexact_algebra_are_rejected():
    with pytest.raises(ValueError): M.glued(2,1)
    with pytest.raises(ValueError): M.glued(-1,1,t=.5)
    with pytest.raises(ValueError): M.glued(-1,1,k=-1)


@pytest.mark.parametrize('t',[.1,.3,1.])
def test_even_odd_positive_eigenvalues_pair_in_declared_cochain_metric(t):
    d=M.algebraic_spectrum(t)
    assert d['max_difference']<2e-9
    assert min(d['even'])>0 and len(d['even'])==5


def test_actual_hyperbolic_core_potential_and_zero_solution_sign():
    d=M.radial()
    assert d['core_derivative']==d['exterior_derivative']==d['join']==0
    assert d['local_zero']==0 and d['wrong_sign']!=0
    assert all(v==0 for v in d['primitive_residuals'].values())


@pytest.mark.parametrize('a',[1,2])
@pytest.mark.parametrize('eps',[.01,.003])
def test_transverse_norm_integrated_independently(eps,a):
    d=M.tail_norm(eps,.2,a)
    assert d['quadrature']>0 and d['relative_error']<3e-10


def test_strong_threshold_and_wrong_measure_are_discriminated():
    e=sp.symbols('epsilon',positive=True)
    # Direct primitives: no call to the comparator's closed formula.
    r=sp.symbols('r',positive=True)
    for a,expected in [(0,sp.Rational(1,2)),(sp.Rational(1,2),1),(1,sp.oo),(2,sp.oo),(-1,sp.Rational(1,4))]:
        correct=sp.integrate(r**(1-2*a),(r,e,1))
        assert sp.limit(correct,e,0,dir='+')==expected
    wrong=sp.integrate(r**(-1),(r,e,1))
    assert sp.limit(wrong,e,0,dir='+')==sp.oo
    assert M.flat_norm(sp.Rational(1,100),1,sp.Rational(1,2))==sp.Rational(99,100)


def test_axial_cutoff_cost_does_not_vanish_with_divergent_transverse_norm():
    d=M.axial_and_current()
    assert sp.simplify(d['axial_ratio']-sp.pi**2/d['L']**2)==0
    assert d['axial_ratio']!=0


def test_normalized_constant_gauge_coupling_does_not_follow_support_size():
    d=M.axial_and_current()
    assert d['overlap']==d['expected']
    assert d['normalization_residual']==0
    assert d['spinor_dimension']==d['left_linear']==16
    assert d['anomaly_pair']==[0,0] and d['mixed_pair']==sp.zeros(5)
    assert d['left_mixed']!=sp.zeros(5)
