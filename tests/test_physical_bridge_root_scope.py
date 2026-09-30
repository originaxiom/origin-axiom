"""Exact scope controls; no text-only proof acceptance or physics promotion."""
import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / 'reports/physical_bridge_2026_09_05/root_scope.py'
spec = importlib.util.spec_from_file_location('r57_root_scope', path)
rs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rs)


def test_conditional_root_and_general_trace_increments():
    assert all(rs.core_checks().values())


def test_inverse_legality_and_orientation_are_distinct_inputs():
    assert all(rs.admission_checks().values())


def test_no_selector_does_not_forbid_equivariant_quotient():
    assert all(rs.quotient_checks().values())


def test_free_group_control_does_not_silently_abelianize():
    assert rs.reduce_word((1, 2, -1, -2)) != ()
    assert rs.reduce_word((1, 2, -2, -1)) == ()
    assert rs.reduce_word((1, 2)) != rs.reduce_word((2, 1))


def test_symmetric_law_can_have_nonsymmetric_solutions():
    assert all(rs.symmetry_checks().values())


def test_descent_requires_slope_holonomy_not_arbitrary_transport():
    assert all(rs.descent_checks().values())


def test_no_physics_or_global_classification_promoted():
    result = rs.run()
    assert result['all_checks_pass'] and result['total'] == 23
    for key in ('full_architecture_completeness_proved', 'physical_root_selected',
                'physical_chirality_derived', 'foreign_geometry_or_index_recertified'):
        assert result[key] is False
