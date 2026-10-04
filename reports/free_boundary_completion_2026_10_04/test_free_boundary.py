import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('free_boundary_verifier',HERE/'verify_free_boundary.py')
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


def test_nonlinear_covariance_and_Green_signs():
    assert all(v.covariance()['checks'].values())


def test_positive_complex_directions_and_boundary_penalty():
    assert all(v.fourier()['checks'].values())


def test_complete_silver_fermion_grading():
    result = v.full_degrees()
    assert result['h0_h3_omission_rejected']
    assert all(row['odd_minus_even']['absolute']==row['odd_minus_even']['relative']==0 for row in result['rows'])


def test_interior_positive_is_preserved_separately():
    for row in v.full_degrees()['rows']:
        assert row['odd_minus_even']['interior_image']==(-1 if row['order']=='E' else 1)
