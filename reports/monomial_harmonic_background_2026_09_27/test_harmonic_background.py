import sympy as sp
from verify_harmonic_background import (
    cusp_controls, finite_hodge_control, gauge_controls,
    nonlinear_and_trace_controls, one_seed,
)


def test_positive_metric_and_nonzero_interior_class_both_seeds_and_covers():
    for i in range(2):
        result = one_seed(i)
        assert result["global_class_nonzero"]
        assert sp.Matrix(result["gram"]).det() == 5
        for row in result["covers"].values():
            assert row["ordinary"] == (0, 3, 2, 4, 2)
            assert row["d0_rank"] == 4 and row["adjoined_cocycle_rank"] == 5
            assert row["peripheral_periods_zero"] and row["positive_metric_preserved"]


def test_coboundary_and_invalid_cochain_are_discriminated():
    assert all(gauge_controls().values())


def test_nonidentity_gram_hodge_projection_sign_and_exact_class():
    result = finite_hodge_control()
    assert result["norm_squared"] > 0
    assert result["wrong_sign_rejected"] and result["exact_class_projects_to_zero"]


def test_scalar_gap_not_transferred_to_one_forms():
    result = cusp_controls()
    assert result["scalar_conjugated_operator"] == "-d_r^2+1"
    assert result["one_form_radial_operator"] == "-d_r^2"
    assert result["rayleigh_constant"] == 12
    assert result["laplacian_norm_constant"] == 504


def test_bessel_and_zero_mode_controls():
    result = cusp_controls()
    assert result["bessel_derivative_and_equation"]
    assert result["constant_scalar_L2_norm_squared"] == sp.Rational(1, 2)


def test_commuting_solution_and_noncommuting_counterexample():
    result = nonlinear_and_trace_controls()
    assert result["all_commutator_residuals_zero"]
    assert result["noncommuting_control_rejected"]


def test_parent_trace_and_kinetic_conventions():
    result = nonlinear_and_trace_controls()
    assert result["raw_E8_adjoint_trace_factor"] == 60
    assert result["complex_kinetic_real_split"]
