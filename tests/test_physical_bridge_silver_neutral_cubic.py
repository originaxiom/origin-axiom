"""Live same-domain neutral and central cubic safeguards, not transcript assertions."""
import importlib.util
from functools import lru_cache
from pathlib import Path

import pytest

BASE = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_neutral_cubic_2026_10_11'


def module(name, prefix='test'):
    spec = importlib.util.spec_from_file_location(prefix+'_neutral_'+name, BASE/(name+'.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@lru_cache(None)
def both():
    return [module(name).run() for name in ('probe', 'reference')]


def test_actual_neutral_spaces_agree_not_only_counts():
    a, b = both()
    assert a['neutral'] == b['neutral']
    assert a['neutral']['connecting_dimension'] == a['neutral']['physical_H1'] == 6
    assert a['neutral']['allowed_absolute_H1'] == 0
    assert not a['neutral']['state_deleted']


def test_equal_restriction_is_a_real_opposing_domain():
    for result in both():
        assert result['neutral']['equal_line_physical_H1'] == 12
        assert result['neutral']['equal_line_absolute_H1'] == 6
        assert result['neutral']['parallel_primitive_dimension'] == 6


def test_central_pair_same_actual_planes_and_exact_zero():
    a, b = both()
    assert a['boundary_plane_sha256'] == b['boundary_plane_sha256']
    assert a['central_pair']['shape'] == b['central_pair']['shape'] == [2, 1]
    assert a['central_pair']['polynomial_degree_bound'] == b['central_pair']['polynomial_degree_bound']
    assert a['central_pair']['zero'] and b['central_pair']['zero']
    assert a['central_pair']['coordinate_polynomials'] == ['0', '0']
    assert len(set(b['central_pair']['distinct_points'])) == b['central_pair']['polynomial_degree_bound']+1


def test_actual_nonzero_central_control_agrees():
    a, b = both()
    assert a['central_free_control'] == b['central_free_control']
    assert a['central_free_control'] is not None
    assert all(a['facts'].values()) and all(b['facts'].values())


def test_complete_necessary_catalogue_is_not_singlet_multiplicity():
    a, b = both()
    assert a['center_allowed_types'] == b['center_allowed_types']
    assert len(a['center_allowed_types']) == 6
    assert ['Hu', 'N', 'weak'] in a['center_allowed_types']
    assert ['N', 'N', 'N'] in a['center_allowed_types']
    assert a['center_constraints_are_only_necessary'] and b['center_constraints_are_only_necessary']


def test_zero_contraction_mutation_fails_its_bound_nonzero_control():
    for name in ('probe', 'reference'):
        mod = module(name, 'mutated')
        mod.central_vertex = lambda f, g, dual_meridian: 0
        with pytest.raises(AssertionError, match='actual_central_contraction_nonzero_opposite'):
            mod.run()


def test_charge_omission_is_detected_by_actual_catalogue():
    for name in ('probe', 'reference'):
        mod = module(name, 'catalogue')
        valid = mod.center_catalog()
        invalid = mod.center_catalog(False)
        assert len(invalid) > len(valid)
        assert ['e', 'e', 'e'] in invalid and ['e', 'e', 'e'] not in valid


def test_all_seven_neutrals_preserved_and_no_higher_completion_claim():
    for result in both():
        assert result['neutral_chirals'] == 7
        assert result['neutral']['tangential_trace_zero']
        assert result['structure_neutral_mixed_zero'] and result['neutral_self_zero']
        for key in ('boundary_changed', 'higher_physical_operators_computed', 'normalized_values',
                    'generated_selection', 'outside_review', 'full_goal_achieved'):
            assert not result[key]
