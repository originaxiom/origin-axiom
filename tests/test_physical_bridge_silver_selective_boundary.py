"""Mathematical locks on the explicitly changed selective boundary, not on prose."""
import importlib.util
from pathlib import Path
from functools import lru_cache
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'reports/physical_bridge_2026_09_05/silver_selective_boundary_2026_10_11'

@lru_cache(None)
def results():
    out=[]
    for name in ('probe','reference'):
        spec=importlib.util.spec_from_file_location('test_selective_'+name,BASE/(name+'.py'))
        m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);out.append(m.run())
    return out

def test_actual_selective_stabilizer_has_twelve_gauge_directions():
    a,b=results()
    assert a['maximal_boundary_gauge_dimension']==b['maximal_boundary_gauge_dimension']==12
    assert a['facts']['old_full_k_opposite_still_fails_selective_domain']

def test_protected_generation_and_exceptional_weak_pair_use_actual_duals():
    for a in results():
        assert a['charged']['W']['E']['H']==[0,1,0,0]
        assert a['charged']['Fcolor']['E']['H']==[0,1,0,0]
        assert a['charged']['Fweak']['E']['H']==[0,2,1,0]
        for v in a['charged'].values():
            assert v['dual']['H']==v['E']['H'][::-1]

def test_new_gauge_lines_do_not_drop_endpoints_or_all_abelian_modes():
    for a in results():
        assert a['gauge']['retained_nonabelian']==[1,0,0,1]
        assert a['gauge']['central']==[1,1,1,1]
        assert a['gauge']['excluded_offblock_small_phase']==[0,0,0,0]

def test_neutral_trace_partner_recomputed_not_omitted():
    for a in results():
        assert a['neutral']['H']==[0,6,6,0]
        assert a['neutral']['equal_restriction_H']==[0,12,12,0]
        assert a['neutral']['boundary_H']==[6,12,6]
        assert a['neutral']['restriction_rank']==6

def test_actual_neutral_cell_plane_is_transported_to_log_harmonics():
    a,b=results()
    assert a['neutral']['transported_log_plane_rank']==6
    assert a['facts']['neutral_cell_to_actual_log_harmonic_transport']
    assert a['neutral']['H']==b['neutral']['H']

def test_full_248_boundary_lagrangian_and_new_endpoint_dimension():
    for a in results():
        assert a['boundary_Ah']==[12,100,88]
        assert a['full_H']==[12,26,26,12]

def test_complete_physical_dof_does_not_count_H2_as_an_extra_particle():
    for a in results():
        assert a['chiral_components']==15+4+7
        assert a['vector_components']==12
        assert a['on_shell_real_dof']==76
        assert 2*(a['full_H'][1]+a['full_H'][2]+a['full_H'][3])!=76

def test_independent_anomaly_polynomials_and_weak_parity_controls():
    a,b=results()
    assert a['facts']['all_SM_Cartan_cubic_and_mixed_anomalies_zero']
    assert b['facts']['every_cubic_monomial_and_mixed_gravity']
    assert a['facts']['weak_mod2_counts_with_opposing_single_doublet']
    assert b['facts']['weak_global_parity_bookkeeping_opposite']

def test_no_goal_or_selection_promotion_from_a_supplied_boundary():
    for a in results():
        assert a['generation_count']==1 and a['neutral_chirals']==7
        assert a['new_boundary_supplied']
        assert not a['generated_selection'] and not a['EW_vacuum_derived']
        assert not a['normalized_overlaps'] and not a['global_PDE_solved']
        assert not a['outside_review'] and not a['full_goal_achieved']

def test_both_exact_algorithms_agree_on_all_pencils_roster_and_endpoints():
    a,b=results()
    for key in ('charged','gauge','maximal_boundary_gauge_dimension','full_H',
                'boundary_Ah','chiral_components','vector_components','on_shell_real_dof'):
        assert a[key]==b[key]
    assert all(a['facts'].values()) and all(b['facts'].values())
