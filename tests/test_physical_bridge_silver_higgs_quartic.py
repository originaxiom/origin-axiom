"""Actual massive response, not replay of a saved output."""
import importlib.util
from functools import lru_cache
from pathlib import Path
import pytest
BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_higgs_quartic_2026_10_11'
def module(name,prefix='test'):
    sp=importlib.util.spec_from_file_location(prefix+'_quartic_'+name,BASE/(name+'.py'))
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
@lru_cache(None)
def both():return [module(k).run() for k in ('probe','reference')]
def test_actual_response_spaces_and_projection_agree():
    a,b=both();assert a['response_spaces']==b['response_spaces']
    assert a['boundary_plane_sha256']==b['boundary_plane_sha256']
def test_actual_quartic_characteristic_zero_certificate():
    a,b=both()
    for k in ('shape','degree_bound','rank','zero','canonical_frame_rows','points','samples_sha256','frames_sha256','first_values'):
        assert a['quartic'][k]==b['quartic'][k],k
    assert a['quartic']['degree_bound']==36
    assert len(set(b['quartic']['points']))==73
    assert all(a['facts'].values()) and all(b['facts'].values())
def test_actual_response_detector_recovers_nonzero():
    a,b=both();assert a['response_control']==b['response_control']
    assert a['response_control']['value_Qsqrt2']!=['0','0']
@pytest.mark.parametrize('name',['probe','reference'])
def test_zero_response_detector_rejected(name):
    m=module(name,'zero')
    m.quartic_detector=lambda x,S,P: m.s.zeros(x.cols) if name=='probe' else m.c.Z(len(x[0]))
    with pytest.raises(AssertionError,match='actual_response_nonzero_opposite'):m.run()
@pytest.mark.parametrize('name',['probe','reference'])
def test_zero_moment_map_rejected(name):
    m=module(name,'bracket')
    m.moment=lambda f,g:m.s.zeros(5) if name=='probe' else m.c.Z(5)
    with pytest.raises(AssertionError,match='full_moment_Ward'):m.run()
def test_physical_scope_and_remaining_duties():
    for a in both():
        assert a['same_boundary'] and a['actual_massive_trace_reduced']
        assert a['smooth_Green_hypotheses_conditional']
        for k in ('global_PDE_numerically_solved','all_quartics_computed','normalized_values','generated_selection','outside_review','full_goal_achieved'):
            assert not a[k]
