"""New controls replace, but do not rewrite, two preserved small-step failures."""
from reports.physical_bridge_2026_09_05 import higgs_control_repair as r


def test_full_Hessian_polynomial_identity_and_step_sweep():
    result = r.primitive_checks()
    errors = result["Hessian_derivative_step_errors"]
    assert errors["1.0"]["second"] < 1e-10
    assert errors["0.01"]["second"] < 3e-7
    assert errors["0.001"]["second"] < 3e-7


def test_unchanged_compact_covariance_and_parameter_controls():
    result = r.primitive_checks()
    assert result["complex_compact_covariance"]
    assert result["detuned_offset_scalar_kernel"] == 77
    assert result["omitted_cubic_scalar_kernel"] == 89
