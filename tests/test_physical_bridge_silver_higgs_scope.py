"""Scoped full-slot and actual-plane facts, not transcript assertions."""
import importlib.util
from pathlib import Path
from functools import lru_cache

ROOT=Path(__file__).resolve().parents[1]

@lru_cache(None)
def result(name):
    path=ROOT/'reports/physical_bridge_2026_09_05/silver_higgs_scope_2026_10_11'/name
    spec=importlib.util.spec_from_file_location('higgs_scope_test_'+name.replace('.','_'),path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m.run()

def test_all_six_slots_have_only_the_claimed_invariants():
    d=result('probe.py')['full_SM_invariants']
    assert d=={'structure24':24,'gauge24':1,'10_W':0,'bar10_Wdual':0,'5_Fdual':0,'bar5_F':0}

def test_hypercharge_is_a_load_bearing_opposing_control():
    assert result('probe.py')['without_hypercharge_commutant_dimension']==35
    assert result('reference.py')['without_hypercharge_commutant_dimension']==35

def test_native_and_fraction_reconstruct_the_same_actual_planes():
    assert result('probe.py')['F_planes']==result('reference.py')['F_planes']

def test_exception_is_preserved_not_turned_into_higgs_absence():
    row=result('probe.py')['F_planes']['exceptional']
    assert row['H']==[0,2,1,0] and row['dual_H']==[0,1,2,0]
    assert row['scaled_ranks']=={'-2':9,'3':9}

def test_generic_pair_removal_also_removes_the_doublet_pair():
    row=result('probe.py')['F_planes']['protected']
    assert row['H']==[0,1,0,0] and row['scaled_ranks']=={'-2':10,'3':10}

def test_new_selective_assignment_does_not_silently_pass_old_gauge_law():
    f=result('probe.py')['facts']
    assert f['selective_bar5_space_SM_stable']
    assert f['selective_bar5_space_NOT_OLD_full_k_stable']
    assert result('reference.py')['facts']['OLD_SU5_stability_fails']

def test_linear_zero_modes_do_not_imply_joint_unobstructed_moduli():
    f=result('probe.py')['facts']
    assert f['joint_complex_modes_need_not_be_moduli'] and f['quartic_countercontrol_not_quadratic_lifting']
    assert result('reference.py')['facts']['noncommuting_complex_quartic_control']

def test_controls_are_not_a_complete_physical_theory_certificate():
    d=result('probe.py')
    assert d['conditional_adjoints_persist']==12
    assert not d['new_physical_boundary_constructed']
    assert not d['generated_selection'] and not d['full_goal_achieved']
