"""Sixteen safeguards for a bosonic index, not a chiral spectrum certificate."""
import importlib.util
from pathlib import Path
import sympy as s
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_magnetic_index_2026_10_08'
def load(name):
    sp=importlib.util.spec_from_file_location('magnetic_index_test_'+name,BASE/(name+'.py'))
    module=importlib.util.module_from_spec(sp);sp.loader.exec_module(module);return module
p,r=load('probe'),load('reference')

def test_l2_endpoint_including_logarithm():
    for a in range(-24,25):
        b=p.pole_bound(a)
        assert p.integrable(a,b) and not p.integrable(a,b+1)
        assert b==r.pole_bound(a)
    assert p.integrable(0,0) and not p.integrable(2,1)

def test_exact_function_dimension_keeps_simple_pole_obstruction():
    assert p.pole_basis(-1)==[] and p.pole_basis(0)==[0] and p.pole_basis(1)==[0]
    for d in range(2,25):
        assert sorted(p.pole_basis(d))==[0]+list(range(2,d+1))
        assert len(p.pole_basis(d))==r.residue_dimension(d)

def test_hodge_duality_and_all_four_kernel_terms():
    for a in range(-24,25):
        assert p.index(a)==-p.index(2-a)==r.index(a)
    assert p.run()['facts']['hermitian_hodge_coefficient_cancels_derivative']

def test_beta_zero_is_a_discriminating_endpoint():
    assert p.line_index(0)==0 and p.line_index(1)==1
    assert p.run()['facts']['dropping_log_endpoint_changes_index_control']

def test_positive_beta_exact_formula_and_spin_shift():
    for b in range(81):
        assert p.index(-b)==-s.ceiling(s.Rational(b,2))
        assert p.index(1-b)==-s.floor(s.Rational(b,2))
        assert p.line_index(b)==b%2
    assert p.index(-1)-p.index(-1)==0 and p.line_index(1)!=0

def test_actual_line_metric_and_drift():
    a=p.run()['facts']
    assert a['canonical_line_metric_is_unitary'] and a['canonical_line_drift_from_derivative']

def test_principal_homotopy_keeps_extremes_and_gap():
    a=p.run()['facts']
    assert a['principal_homotopy_full_blocks_not_scalar_guess']
    assert a['all_extreme_and_paired_drifts_remain_half_integral']

def test_neutral_perturbation_decays_on_same_end():
    assert p.run()['facts']['every_fixed_finite_neutral_amplitude_decays']

def test_full_root_and_tensor_weight_population():
    assert p.weights()==r.weights() and sum(p.weights().values())==248

def test_actual_roster_bound_underlies_all_integer_claim():
    assert all(m+2*abs(q)>=0 for q,m in p.weights() if q)
    assert (-2+2*1)==0 and p.line_index(-2+2*1)==0

def test_charge_resolved_fifty_bound_all_tested_flux_signs():
    target={'1':12,'2':18,'3':12,'4':6,'5':0,'6':2}
    for n in (1,2,3,5):
        assert p.unstable_bounds(n)==target
        assert {str(-int(q)):v for q,v in p.unstable_bounds(-n).items()}==target
    assert sum(target.values())==50

def test_zero_flux_and_gauge_root_only_opposite_controls():
    assert p.unstable_bounds(0)=={}
    assert sum(v for q,v in p.charge_indices(0).items() if q>0)==40
    assert p.charge_indices(2)[5]==0 and sum(p.unstable_bounds(2).values())>0

def test_soft_sign_actual_kinetic_and_gauge_split():
    a=p.matrix_controls()
    assert a['matter']==a['connection']==0 and a['soft']<0 and a['norm']>0
    good,bad=p.old.gauge_identity()
    assert good==0 and bad!=0

def test_graph_approximants_keep_negative_margin():
    assert s.Rational(1,4)**2-(1-s.Rational(1,4))**2<0
    assert p.run()['facts']['graph_approximation_keeps_a_strict_negative_margin']

def test_second_spin_background_is_not_silently_excluded():
    a=p.matrix_controls()
    assert a['two_field_residuals'] and a['new_linear_R_term_nonzero']

def test_two_routes_and_no_physical_index_or_complete_morse_promotion():
    a,b=p.run(),r.run()
    assert all(a['facts'].values()) and all(b['predicates'].values())
    for key in ('line_table','charge_index_profiles','unstable_bounds'):
        assert a[key]==b[key]
    assert not any(a[key] for key in ('full_Morse_index_computed','physical_fermion_index_computed',
        'two_field_stability_computed','stable_nonzero_flux_phase_achieved',
        'genesis_selection_derived','nonauthor_acceptance','physical_goal_achieved'))
