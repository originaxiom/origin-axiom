"""LIVE exact comparison; authored analytic transfer and scope separate."""
from pathlib import Path
import importlib.util

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_charged_pair_lift_2026_10_11'

def load(name):
    spec=importlib.util.spec_from_file_location('charged_lift_test_'+name,BASE/(name+'.py'))
    out=importlib.util.module_from_spec(spec);spec.loader.exec_module(out);return out

p,r=load('probe'),load('reference')

def test_character_is_derived_and_parity_not_misused():
    assert p.run()['facts']['literal_primitive_character_not_parity']
    assert p.run()['facts']['literal_cusp_periods_0_1']
    assert r.run()['predicates']['primitive_time_character_and_wrong_parity_character']

def test_actual_two_direction_cusp_not_principal_model():
    assert p.run()['facts']['two_independent_actual_cusp_logs']
    assert r.run()['predicates']['two_actual_cusp_logs']

def test_generic_rank_certificate_and_nonacyclic_control():
    a,b=p.run(),r.run()
    for label in ('W','F'):
        assert a['facts'][label+'_bulk_generic_acyclic_exact']
        assert a['facts'][label+'_fiber_minor_leading_certificate']
        assert b['predicates'][label+'_fiber_minor_nonzero_leading_coefficient']
        assert a['blocks'][label]['bulk_H_controls']==b['blocks'][label]['bulk_H_controls']
        assert any(a['blocks'][label]['bulk_H_controls'][0])
    assert a['facts']['degree_bound_requires_n_plus_one_points']
    assert b['predicates']['five_bad_samples_but_sixth_detects_degree_five_polynomial']

def test_all_bounded_witnesses_and_actual_dual_planes_recomputed():
    a,b=p.run(),r.run()
    assert a['blocks']==b['blocks']
    assert a['blocks']['W']['witness_count']==16
    assert a['blocks']['F']['witness_count']==64
    assert all(row['H']==row['dual']['H'][::-1] for block in a['blocks'].values() for row in block['rows'])

def test_all_five_indices_have_protected_only_examples():
    a=p.run()
    assert a['common_generation_indices']==[-2,-1,0,1,2]
    for label,t0 in (('W',2),('F',3)):
        block=a['blocks'][label]
        for J in range(-2,3):
            chosen=block['protected_only_witnesses'][str(t0+J)]
            row=next(row for row in block['rows'] if row['subset']==chosen)
            assert row['H']==[0,max(J,0),max(-J,0),0]

def test_literal_family_first_mass_maps_not_raw_boundary_cup():
    a,b=p.run(),r.run()
    assert a['first_mass_maps']==b['first_mass_maps']
    assert len(a['first_mass_maps'])==8
    for label in ('W','F'):
        assert a['facts'][label+'_omitted_boundary_response_breaks_family_chain']
        assert a['facts'][label+'_frozen_cell_comparison_breaks_family_chain']
        for J in (1,2):
            assert a['first_mass_maps'][label+'_J'+str(J)]['first_mass_rank']==a['first_mass_maps'][label+'dual_J'+str(J)]['first_mass_rank']

def test_wrong_exterior_twist_changes_the_operator():
    assert p.run()['facts']['exterior_then_twist_not_exterior_of_twist']
    assert r.run()['predicates']['twist_after_exterior_is_not_squared']
    assert p.run()['facts']['all_SM_H_weights_nonzero']

def test_every_live_predicate_and_reference_independence():
    a,b=p.run(),r.run()
    assert all(a['facts'].values()) and all(b['predicates'].values())
    assert a['predicates_passed']==len(a['facts'])
    assert b['predicates_passed']==len(b['predicates'])
    assert b['new_native_imported'] is False and b['degree_bound_certificate'] is True

def test_conditional_phase_does_not_erase_physics_debts():
    for a in (p.run(),r.run()):
        assert a['conditional_small_v_charged_lift'] is True
        for key in ('actual_normalized_mass_values','global_PDE_solved','Higgs_complete','generated_selection','three_generations','outside_review','full_goal_achieved'):
            assert a[key] is False
