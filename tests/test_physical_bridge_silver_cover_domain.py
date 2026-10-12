"""Actual global gauge, neutral/charged maps; no transcript-matching lock."""
import importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_cover_domain_2026_10_12'
def load(name):
    spec=importlib.util.spec_from_file_location('cover_domain_test_'+name,BASE/(name+'.py'))
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
p,r=load('probe'),load('reference')

def test_global_gauge_not_two_independent_cusp_gauges():
    a,b=p.run(),r.run()
    for tag in a['gauge']:
        for sector in ('plus','minus'):
            assert {k:a['gauge'][tag][sector][k] for k in b['gauge'][tag][sector]}==b['gauge'][tag][sector]
        assert a['gauge'][tag]['plus']['H'][0]==1 and a['gauge'][tag]['minus']['H'][0]==0

def test_sum_response_keeps_opposite_nonzero_flux():
    assert p.run()['facts']['opposite_nonzero_sheet_flux_is_allowed']
    assert p.run()['facts']['same_sheet_flux_is_rejected']
    assert r.run()['checks']['opposite_flux_is_allowed_not_two_neumann_laws']

def test_all_neutral_degrees_reconstructed_characteristic_zero():
    a,b=p.run(),r.run();assert a['neutral']==b['neutral']
    assert set(a['neutral'])=={'plus','minus'}
    for row in a['neutral'].values():
        assert row['H'][0]==row['H'][3]==0 and row['H'][1]==row['H'][2]
        assert row['boundary_H']==[6,12,6] and row['union_rank']==12

def test_nonisotropic_plane_controls_on_both_actual_neutral_sectors():
    for sector in ('plus','minus'):
        assert p.run()['facts'][sector+'_nonisotropic_same_dimension_plane_rejected']
        assert r.run()['checks'][sector+'_nonisotropic_control_kept']

def test_neutral_planes_actually_transport_to_log_kinetic_coordinates():
    for sector in ('plus','minus'):
        assert p.run()['facts'][sector+'_actual_log_harmonic_plane_transport']
        assert r.run()['checks'][sector+'_independent_literal_log_transport']

def test_charged_three_and_actual_duals_survive_this_same_full_boundary():
    a,b=p.run(),r.run();assert a['charged']==b['charged']
    for row in a['charged'].values():assert row['H']==[0,3,0,0]

def test_phase_and_full_gauge_root_roster_not_a_double_gauge_copy():
    assert p.run()['facts']['broken_gauge_even_A0_to_A1_and_odd_A1_to_A2_both_acyclic']
    assert p.run()['facts']['full_gauge_roots_and_Cartan_all_retained']
    assert r.run()['checks']['SM_twelve_generators_not_deck_doubled']

def test_induce_each_coefficient_before_counting_fields():
    assert p.run()['facts']['wrong_end_of_pushforward_rank_rejected']
    assert r.run()['checks']['End0_of_induced_is_not_induced_End0']

def test_complete_linear_roster_keeps_extra_physical_modes():
    a,b=p.run(),r.run();assert a['physical_linear_roster']==b['physical_linear_roster']
    row=a['physical_linear_roster'];assert row['charged_component_chirals']==45
    assert row['neutral_singlet_chirals']>0 and row['unbroken_adjoint_chirals']>0
    assert row['independent_vector_sectors']==1 and row['SM_vector_generators']==12
    assert row['left_chiral_components']>45

def test_live_checks_do_not_imply_selection_or_quantum_acceptance():
    for name in ('probe','reference'):
        a=(p if name=='probe' else r).run();checks=a['facts'] if name=='probe' else a['checks']
        assert all(checks.values()) and len(checks)==a['exact_predicates']
        assert a['whole_boundary_conditional']
        for key in ('generated_boundary','normalized_interactions','global_quantum_anomaly','outside_review','full_goal_achieved'):
            assert not a[key]
