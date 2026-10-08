"""Twenty focused controls for the full two-field bosonic complex."""
import importlib.util
from pathlib import Path
import sympy as s
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_two_neutral_index_2026_10_08'
def load(name):
    sp=importlib.util.spec_from_file_location('two_neutral_test_'+name,BASE/(name+'.py'))
    mod=importlib.util.module_from_spec(sp);sp.loader.exec_module(mod);return mod
p,r=load('probe'),load('reference')

def test_full_two_field_quadratic_expansion():
    q=p.quadratic();assert s.expand(q['actual']-q['expected'])==0
    assert p.run()['facts']['both_field_moment_remains_parallel']

def test_new_R_connection_and_commutator_terms_are_load_bearing():
    q=p.quadratic();assert s.expand((q['actual']-q['wrong']).subs(q['h'],1))!=0

def test_R_zero_recovers_previous_full_action_expansion():
    q=p.quadratic()
    assert s.expand(q['actual'].subs(q['h'],0)-p.neutral.quadratic_expansion()['actual'])==0

def test_zero_flux_is_nonnegative_full_squares():
    q=p.quadratic();assert s.expand(q['actual'].subs(q['n'],0)-q['squares'])==0

def test_three_actual_maps_compose_to_zero():
    assert p.complex_checks()['complex'] and r.run()['predicates']['separate_complex_compositions']

def test_noncommuting_substitute_breaks_complex():
    assert p.complex_checks()['noncommuting_fails'] and r.run()['predicates']['noncommuting_control_fails']

def test_positive_metrics_fix_the_gauge_adjoint():
    c=p.complex_checks();assert c['gauge_adjoint'] and c['wrong_C0_factor_fails']

def test_full_Hodge_norm_keeps_the_auxiliary_block():
    c=p.complex_checks();assert c['hodge_cross'] and c['physical_block']

def test_R_adjoint_component_is_pointwise_injective():
    assert p.complex_checks()['aux_injective']

def test_auxiliary_removal_is_not_assumed_at_d_zero():
    assert p.complex_checks()['aux_zero_control']

def test_flavor_symmetry_and_independent_profiles():
    f=p.flavor();assert f[0]==0 and f[1] and f[2]
    assert f[3]==s.Symbol('d')/2 and f[3].subs(s.Symbol('d'),1)!=0

def test_second_shifted_block_from_actual_coordinate_metrics():
    k=s.symbols('k',integer=True)
    for j in range(5):
        for row in p.blocks(j,k,1):
            if row['kind']=='pair':assert p.shifted_coordinates(j,row['m'],k)==(0,0,0)

def test_both_principal_homotopies_and_extremes():
    f=p.run()['facts']
    assert f['both_shifted_full_homotopy_blocks'] and f['every_extreme_retained_and_half_integral']
    assert f['both_shift_channel_counts_complete']

def test_auxiliary136_not_a_physical_field_population():
    assert p.populations()==r.population()=={'physical_C1':360,'auxiliary_C3':136,'h0':248,'h1':248,'total':496}

def test_exact_spin_power_index_and_endpoint():
    for b in range(-80,81):
        assert p.line_index(b)==r.line_index(b)
        assert p.line_index(-b)==-p.line_index(b)
    assert p.line_index(0)==0 and p.line_index(1)==1 and p.line_index(2)==-1

def test_full_root_and_tensor_populations_agree():
    assert p.old.weights()==r.weights() and sum(p.old.weights().values())==248

def test_charge_profiles_and_positive_lower_bound():
    expected={1:-6,2:6,3:4,4:-3,5:-6,6:-1}
    for n in (2,3,5):
        assert {q:p.charge_indices(n)[q] for q in range(1,7)}==expected
    assert p.charge_indices(1)[1]==0
    for n in (1,2,3,5):
        assert p.positive_bounds(n)=={'2':6,'3':4}
        assert p.positive_bounds(-n)=={'-3':4,'-2':6}
    assert all(v==0 for v in p.charge_indices(0).values())

def test_actual_weight_bound_underlies_all_integer_scope():
    assert all(m+2*abs(q)>=0 and m+4*abs(q)>0 for q,m in p.old.weights() if q)

def test_previous_negative_and_positive_controls_survive():
    f=p.run()['facts']
    for key in ('R_zero_stronger_bound_is_preserved','first_flux_essential_instability_control',
                'finite_neutral_terms_decay_on_same_end','physical_negative_path_margin'):
        assert f[key]

def test_two_routes_and_no_physical_or_universal_promotion():
    a,b=p.run(),r.run()
    assert all(a['facts'].values()) and all(b['predicates'].values())
    for key in ('line_index_table','index_profiles','positive_bounds','hodge_populations'):
        assert a[key]==b[key]
    assert not any(a[key] for key in ('auxiliary_is_physical_field','physical_Weyl_dictionary_derived',
        'full_Morse_count_computed','stable_nonzero_flux_phase_achieved',
        'all_stationary_phases_excluded','genesis_selection_derived','nonauthor_acceptance','physical_goal_achieved'))
