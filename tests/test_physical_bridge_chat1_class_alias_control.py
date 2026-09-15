"""Same mathematical predicates on the separately resolved negative-control name."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from copy import deepcopy
import pytest

SOURCE = Path(__file__).resolve().parents[1] / 'reports/physical_bridge_2026_09_05/chat1_class_alias_control.py'
SPEC = spec_from_file_location('chat1_alias_control', SOURCE)
control = module_from_spec(SPEC)
SPEC.loader.exec_module(control)
m = control.ORIGINAL


@pytest.fixture(scope='module')
def result():
    return control.exact_run()


def test_exact_parent_matrices_act_on_actual_tetrahedron(result):
    g = result['parent']
    assert m.mul(m.Z, m.Z) == (-1, 1)
    assert g['matrix_count'] == 24 and g['projective_count'] == 12
    assert g['all_vertex_permutations_even'] and g['all_determinants_one']
    assert g['center'] == sorted([m.IDENTITY, tuple(m.neg(x) for x in m.IDENTITY)])


@pytest.mark.parametrize('index,expected', [(0, 12), (1, 24), (2, 36)])
def test_proposed_indices_require_shape_and_subgroup_checks(result, index, expected):
    r = result['manifolds'][index]
    assert r['face_inverses'] and r['regular_shape_certificate']
    assert r['coloring']['components'] == 1 and r['coloring']['two_colorable']
    assert r['psl_cover_index'] == expected and r['pgl_cover_index'] == 2*expected


def test_rejector_uses_published_signature_and_does_not_fake_psl_cover(result):
    r = result['manifolds'][-1]
    assert r['name'] == 'otet06_0000'
    assert r['constructor_input'] == 'gLLPQccdfeefqjsqqjj'
    assert result['alias_control']['original_first_run_succeeded'] is False
    assert r['regular_shape_certificate'] and r['pgl_cover_index'] == 72
    assert r['coloring']['conflicts'] and r['psl_cover_index'] is None


def test_equal_dimensions_do_not_hide_the_different_anomalies(result):
    r = result['representation']
    assert r['grade_dimension'] == r['fundamental_dimension'] == 27
    assert r['grade_cubic_trace'] == -54 and r['dual_grade_cubic_trace'] == 54
    assert r['grade_anomaly'] == 9
    assert r['fundamental_cubic_trace'] == r['paired_grade_cubic_trace'] == 0
    assert 0 not in r['grade_color_weights'] and r['fundamental_color_weights'][0] == 9


def test_damaged_geometry_is_still_rejected(result):
    assert m.coloring([[1], [0]])['two_colorable']
    assert not m.coloring([[1, 2], [0, 2], [0, 1]])['two_colorable']
    assert not m.coloring([[0]])['two_colorable']
    with pytest.raises(ValueError):
        m.coloring([[2]])
    r = result['manifolds'][0]
    equations = deepcopy(r['gluing_equations'])
    equations[-1][0] += 1
    assert not m.regular_log_certificate(equations, r['tetrahedra'], r['cusps'])
    data = deepcopy(r['face_data'])
    data[0][1][0] = [0, 0, 0, 0]
    assert not m.inverse_faces(data)


def test_all_original_predicates_survive_and_dispatch_restores(result):
    assert len(result['checks']) == 10 and all(result['checks'].values())
    assert result['all_checks_pass']
    assert m.triangulation_row.__name__ == 'triangulation_row'
