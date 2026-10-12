"""LIVE operator/rank/dual/cover tests; no transcript-match certification."""
import importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_cover_families_2026_10_12'
def load(name):
    spec=importlib.util.spec_from_file_location('cover_family_test_'+name,BASE/(name+'.py'))
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
p,r=load('probe'),load('reference')

def test_cover_population_and_actual_section_map():
    a,b=p.run(),r.run()
    assert a['cover_characters']==b['cover_characters']
    assert len(a['cover_characters'])==3 and a['bulk']==b['bulk']
    assert a['facts']['nonperipheral_character_control']
    assert all(a['facts'].values()) and all(b['checks'].values())

def test_all_dimension_menu_live_and_independent():
    a,b=p.run(),r.run()
    assert a['menu']==b['menu'] and len(a['menu'])==1225
    assert a['common_indices']==b['common_indices']==list(range(-4,5))

def test_inherited_domain_is_not_a_hidden_odd_count():
    for row in p.run()['menu']:
        if row['ell'][0]==row['ell'][1] and row['ell'][2]==row['ell'][3]:
            assert all(j%2==0 for j in row['J'])

def test_three_kernel_and_actual_dual_not_index_only():
    a,b=p.run(),r.run()
    assert a['models']==b['models']
    for row in a['models'].values():
        assert row['H']==[0,3,0,0] and row['dual_H']==[0,0,3,0]
        assert row['rank'] in (10,20) and row['sector_J']==[1,2]
        assert row['dual_rank']==row['rank']-3
        assert row['dual_rank']<row['rank']

def test_all_three_witnesses_and_conjugate_opposing_cases():
    a=p.run();assert len(a['common_three_dimension_choices'])==8
    for row in a['menu']:
        if row['J']==[3,3]:assert row['W']==row['F']==[0,3,0,0]
    assert any(row['J']==[0,0] and row['W'][1]*row['W'][2]>0 for row in a['menu'])

def test_gauge_coefficient_not_exterior_of_induced_rank_ten():
    assert p.run()['facts']['exterior_before_pushforward_rank_control']
    assert r.run()['checks']['induction_exterior_noncommutation_detected']

def test_parent_interactions_not_decoupled_copies():
    assert p.run()['facts']['parent_deck_multiplication_keeps_cross_sector_vertices']
    assert p.run()['facts']['decoupled_copy_control_rejected']
    assert r.run()['checks']['actual_parent_multiplication_cross_parities_not_copies']

def test_kernel_match_does_not_hide_domain_and_selection_duties():
    # These flags grade the result; the live mathematical tests above are
    # the evidence, not these status declarations.
    for a in (p.run(),r.run()):
        assert a['charged_transfer_conditional']
        for key in ('complete_cover_domain_verified','boundary_selected','actual_zero_profile_Yukawas','outside_review','full_goal_achieved'):
            assert a[key] is False
