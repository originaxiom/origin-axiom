"""Live algebraic locks, not asserted outcome strings."""
import importlib.util
from functools import lru_cache
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_charged_cubic_2026_10_11'
@lru_cache(None)
def both():
    out=[]
    for name in ('probe','reference'):
        sp=importlib.util.spec_from_file_location('test_charged_cubic_'+name,BASE/(name+'.py'))
        m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);out.append(m.run())
    return out
def test_actual_constant_boundary_planes_agree_not_just_dimensions():
    a,b=both();assert a['boundary_plane_sha256']==b['boundary_plane_sha256']
    assert len(a['boundary_plane_sha256'])==4
    assert a['boundary_plane_sha256']['Fcolor']!=a['boundary_plane_sha256']['Fweak']
def test_two_exact_methods_classify_all_charged_channels():
    a,b=both();assert a['channel_ranks']==b['channel_ranks']
    assert set(a['channel_ranks'])=={'up','down','lepton','udd'}
def test_actual_polynomial_profiles_satisfy_whole_pencil_and_plane():
    a,b=both()
    for name in ('Q','u','e','d','weak','Hu'):
        assert a['facts'][name+'_whole_pencil_kernel']
        assert a['facts'][name+'_actual_fixed_trace_plane']
        assert a['facts'][name+'_closed_trace']
        assert b['facts'][name+'_degree_one_rank_certificate_and_actual_kernel']
def test_zero_coefficients_have_degree_certificates_not_sampling_nulls():
    a,b=both()
    for k,c in b['zero_certificates'].items():
        assert len(c['distinct_points'])==c['degree_bound']+1
        assert c['zero_certified']==(a['channel_ranks'][k]==0)
def test_exchange_and_single_generation_udd_are_retained():
    for x in both():
        assert x['channel_ranks']['udd']==0
        assert x['channel_ranks']['lepton'] in (0,2)
def test_transgression_verifiers_recover_nonzero_and_reject_phase_omission():
    a,b=both()
    assert a['facts']['nonzero_transgression_recovery_and_phase_omission']
    assert b['facts']['nonzero_exterior_dictionary_transgression_recovery']
    assert b['facts']['phase_omission_opposing_control']
    assert b['facts']['zero_certificate_needs_degree_plus_one']
def test_positive_kinetic_Gram_is_not_discarded():
    a,b=both();assert a['facts']['weak_vector_norm_carries_positive_kinetic_Gram']
    assert not a['absolute_normalized_Yukawas'] and not b['absolute_normalized_Yukawas']
def test_no_spectrum_basis_is_silently_declared_Higgs_selection():
    a,b=both();assert a['facts']['weak_space_is_not_a_marked_Higgs_line']
    assert b['facts']['no_Higgs_line_selected_from_weak_dimension']
def test_no_full_potential_or_ToE_promotion():
    for a in both():
        assert all(a['facts'].values())
        for k in ('neutral_cubic_computed','complete_light_potential','generated_selection','outside_review','global_PDE_solved','full_goal_achieved'):
            assert not a[k]
