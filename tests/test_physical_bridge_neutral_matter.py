"""R54 exact reception/join controls; no independent global analytic certificate."""
from pathlib import Path
import importlib.util
import pytest

path = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/neutral_matter.py'
spec = importlib.util.spec_from_file_location('test_r54_neutral_matter', path)
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


@pytest.mark.parametrize('middle,embedding,phase', v.CASES)
@pytest.mark.parametrize('dual', [False, True])
def test_actual_log_derivative_obstruction(middle, embedding, phase, dual):
    out = v.obstruction(middle, embedding, phase, dual)
    assert all(out['checks'].values())


def test_rank_jump_is_not_first_order_obstruction():
    checks = v.toy_controls()
    assert checks['same_isolated_rank_jump']
    assert checks['simple_zero_obstructs'] and checks['double_zero_first_derivative_vanishes']
    assert checks['zero_obstruction_not_nonlinear_survival']


def test_exact_relaxation_and_normalization_controls():
    checks = v.toy_controls()
    assert checks['mixed_residual_survives_exact_relaxation']
    assert checks['exact_source_can_be_removed'] and checks['unit_dual_overlap_positive']
    assert checks['nonzero_basis_rescaling_changes_coefficient']


def test_actual_parent_vertex_and_scalar_order_are_distinct():
    assert all(v.parent_controls().values())
