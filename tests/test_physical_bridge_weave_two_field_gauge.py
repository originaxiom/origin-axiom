"""Recompute the two-field equations, embedding and entire gauge centralizer."""
import importlib.util
from pathlib import Path
import sympy as s

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_two_field_gauge_2026_10_08'

def load(name):
    spec=importlib.util.spec_from_file_location('twofield_'+name,BASE/(name+'.py'))
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

p=load('probe');r=load('reference')

def test_two_root_enumerations_agree():
    assert p.roots()==r.weyl() and len(p.roots())==240

def test_same_regular_A2_and_peripheral():
    assert p.add(p.BETA,p.scale(p.DELTA,-1))==p.V
    assert p.run()['facts']['same_old_peripheral']

def test_both_spin_weights_and_commutation():
    x,y,k,h=p.fields()
    assert p.comm(h,x)==2*x and p.comm(h,y)==2*y
    assert p.comm(x,y)==s.zeros(3)
    assert p.comm(x,x.T)+p.comm(y,y.T)==k==3*h/2

def test_local_equations_and_failing_controls():
    a=p.run()['facts']
    assert a['moment_and_both_spin_residuals_zero']
    assert all(a[n] for n in ('flat_connection_control_fails','wrong_norm_control_fails','noncommuting_pair_control_fails'))

def test_compact_closure_is_not_a_single_sl2():
    x,y,k,h=p.fields()
    assert p.lie_dimension([x,y,x.T,y.T])==8

def test_cubic_lift_and_positive_norm():
    a=p.run()['facts']
    assert a['fractional_grading_needs_lift'] and a['spin_line_cancellation']
    assert a['finite_positive_total_Higgs_norm']

def test_full_trinification_root_branch():
    e6,parts,a,b,c,mixed,signs=p.frame(p.roots())
    assert len(e6)==72 and len(mixed)==54 and len(signs)==2
    assert p.run()['facts']['full_E6_tensor_branching']

def test_central_quotient_checked_on_every_root():
    a=p.run()['facts']
    assert a['center_correct_in_E6'] and a['unique_oriented_center_matches_all_E8']
    assert a['omitting_compensator_fails'] and a['inverting_compensator_fails']

def test_clock_shift_actual_unitary_commutator():
    w,d,t=p.clock_pair()
    assert p.zero(d*t*d.conjugate().T*t.T-w*s.eye(3))
    assert p.run()['facts']['clock_shift_unitary_det1']
    assert p.run()['facts']['central_commutator_exact']

def test_finite_group_and_all_summand_invariants():
    assert len(r.finite_group())==27
    assert r.fixed_tensor(1,-1)==1 and r.fixed_tensor(1,1)==0
    assert p.run()['gauge_profile']['adjoint_factor_invariants']==[0,0,8]
    assert p.run()['gauge_profile']['mixed_factor_invariants']==[3,3]

def test_G2_actual_roots_not_dimension_guess():
    long,short=p.color_vectors()
    assert len(long|short)==12
    assert {p.dot(z,z) for z in short}=={s.Rational(2,3)}
    assert p.run()['facts']['G2_reflection_closed']
    assert p.run()['facts']['G2_cartan_not_dimension_guess']

def test_full_gauge_rank_cannot_contain_SM():
    data=p.run()['gauge_profile']
    assert data['dimension']==14 and data['rank']==2<4

def test_old_pairing_control_and_new_dual_equations():
    x,y,k,h=p.fields()
    assert p.dual_dimension([x,y,x.T,y.T])==0
    assert p.run()['facts']['old_SO3_dual_map_positive_control']

def test_separate_exact_profiles_and_all_predicates():
    a,b=p.run(),r.run()
    assert all(a['facts'].values()) and all(b['predicates'].values())
    for key in ('root_profile','gauge_profile','phase_profile'):
        assert a[key]==b[key]

def test_no_chirality_or_universal_compensator_promotion():
    a=p.run()
    assert not any(a[key] for key in ('physical_chirality_achieved','fermion_gap_computed','genesis_selection_derived','all_compensators_classified','physical_goal_achieved','nonauthor_acceptance'))
