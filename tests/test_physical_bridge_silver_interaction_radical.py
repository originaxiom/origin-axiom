"""Live exact identities and independent field-method comparisons, not log strings."""
import importlib.util
from functools import lru_cache
from pathlib import Path

import pytest

BASE = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_interaction_radical_2026_10_11'


@lru_cache(None)
def both():
    out = []
    for name in ('probe', 'reference'):
        sp = importlib.util.spec_from_file_location('test_radical_'+name, BASE/(name+'.py'))
        mod = importlib.util.module_from_spec(sp)
        sp.loader.exec_module(mod)
        out.append(mod.run())
    return out


def test_same_actual_boundary_and_all_primitive_dimensions():
    a, b = both()
    assert a['boundary_plane_sha256'] == b['boundary_plane_sha256']
    assert len(a['boundary_plane_sha256']) == 4
    expected = dict(Q=1, u=1, e=1, d=1, weak=2, Hu=1)
    assert {k: v['primitive_dimension'] for k, v in a['profiles'].items()} == expected
    assert {k: v['primitive_dimension'] for k, v in b['profiles'].items()} == expected


def test_exact_constant_envelopes_agree_not_only_dimensions():
    a, b = both()
    for label, field in a['profiles'].items():
        for key in ('envelope_rank', 'envelope_sha256', 'meridian_image_rank',
                    'longitude_image_rank', 'e5_flag', 'meridian_e5_flag', 'longitude_e5_flag',
                    'V4_block', 'meridian_V4_block', 'longitude_V4_block'):
            assert field[key] == b['profiles'][label][key], (label, key)


def test_all_four_tensor_terms_are_classified_individually():
    a, b = both()
    assert set(a['channels']) == set(b['channels']) == {'up', 'down', 'lepton', 'udd'}
    for label, tensor in a['channels'].items():
        for key in ('first_term_zero', 'second_term_zero', 'difference_zero', 'classification'):
            assert tensor[key] == b['channels'][label][key], (label, key)
        assert tensor['difference_zero']


def test_reference_has_envelope_and_term_degree_certificates():
    _, b = both()
    for f in b['profiles'].values():
        assert len(set(f['distinct_points'])) == f['envelope_degree_bound']+1
    for t in b['channels'].values():
        assert len(set(t['distinct_points'])) == t['degree_bound']+1


def test_actual_log_nonzero_controls_agree_and_are_not_physical_modes():
    a, b = both()
    assert a['free_coordinate_controls'] == b['free_coordinate_controls']
    assert all(a['free_coordinate_controls'].values())
    assert all(a['facts'].values()) and all(b['facts'].values())


def test_boundary_parallel_line_is_not_a_bulk_invariant_section():
    for result in both():
        assert result['e5_boundary_parallel'] and not result['e5_bulk_parallel']


def test_no_boundary_retargeting_or_physical_completion_claim():
    # Original scope remains unchanged by the post-first-run block diagnosis.
    for result in both():
        for key in ('boundary_changed', 'neutral_cubic_computed',
                    'higher_physical_operators_computed', 'generated_selection',
                    'register_loss_causation', 'outside_review', 'full_goal_achieved'):
            assert not result[key]


def test_verified_four_plane_mechanism_is_not_the_false_e5_line_hypothesis():
    for result in both():
        for f in result['profiles'].values():
            assert f['V4_block'] and f['meridian_V4_block'] and f['longitude_V4_block']
            assert not f['e5_flag']
        assert result['facts']['proper_global_V4_submodule']
        assert all(t['first_term_zero'] and t['second_term_zero']
                   for t in result['channels'].values())


def test_zero_or_always_true_detector_mutations_fail_the_bound_control():
    for name in ('probe', 'reference'):
        sp = importlib.util.spec_from_file_location('mutated_radical_'+name, BASE/(name+'.py'))
        mod = importlib.util.module_from_spec(sp)
        sp.loader.exec_module(mod)
        if name == 'probe':
            original = mod.block_flag_map
            mod.block_flag_map = lambda label: mod.s.zeros(*original(label).shape)
        else:
            mod.block_flag_zero = lambda label, vector: True
        with pytest.raises(AssertionError, match='V4_vector_detector_two_sided'):
            mod.run()
