"""R55 finite rank/end controls, not independent analytic proof review."""
from pathlib import Path
import importlib.util
import pytest

path = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/neutral_census.py'
spec = importlib.util.spec_from_file_location('test_r55_census', path)
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


@pytest.mark.parametrize('middle,embedding', v.CASES)
def test_actual_global_meridian_kernel(middle, embedding):
    row = v.restriction(middle, embedding)
    assert all(row['checks'].values())
    assert row['ordinary_H1'] == 3 and row['kernel_dimension'] == 1


def test_positive_metric_kernel_and_cokernel_weights():
    assert all(v.cusp_controls().values())


def test_scalar_ordinary_class_does_not_survive_meridian():
    assert all(v.scalar_controls()['checks'].values())


def test_weight_and_endpoint_controls():
    assert all(v.weight_controls().values())


def test_conditional_parent_count_not_three_neutral_moduli():
    out = v.report()
    assert out['all_checks_pass']
    assert out['conditional_neutral_H1'] == 1
    assert out['conditional_parent_H1'] == 33
    assert not out['global_analytic_proof_machine_verified']
    assert not out['all_ordinary_classes_normalizable']
    assert not out['full_EFT_or_numerical_gap_derived']
    assert not out['physical_chirality_derived']
