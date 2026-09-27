import sympy as sp
import pytest
from verify_bridge import (
    actual_point, anchored_control, frame_control, moment_control,
    projection_control, torus_control,
)


def test_anchored_primitive_and_norm_weight_discrimination():
    row = anchored_control()
    assert row["anchored_identity"] and row["constant_primitive_is_L2"]
    assert row["stationary_tangential_period_is_not_L2"]
    assert row["young_kernel_L1"] == 1


def test_frame_change_transforms_metric_and_unbounded_case_is_excluded():
    row = frame_control()
    assert row["wrong_norm_rejected"] and row["chain_conjugacy_sign"]
    assert row["unbounded_frame_counterexample_norm"] == "1/(2*a)"


def test_hodge_projection_retains_H0_and_removes_exact_classes():
    row = projection_control()
    assert row["kernel_dimension"] == 1 and row["reduced_inverse_identity"]
    assert row["exact_class_removed"] and row["wrong_sign_rejected"]
    assert row["norm_squared"] > 0


def test_noncommuting_moment_identity_and_nonzero_residual():
    assert all(moment_control().values())


def test_peripheral_invariant_and_acyclic_channels_both_present():
    row = torus_control()
    assert row["invariant_channel_H0_H1"] == [1, 2]
    assert row["nontrivial_unitary_mu_H0_H1"] == [0, 0]


@pytest.mark.parametrize("seed", [0, 1])
@pytest.mark.parametrize("point", ["one", "minus_one", "i", "two", "primitive_fifth"])
def test_actual_charged_inputs_duals_and_full_degree_accounting(seed, point):
    row = actual_point(seed, point)
    for name, coefficient in row["coefficients"].items():
        degrees = coefficient["conditional_harmonic_degrees"]
        assert degrees[0] == degrees[3]
        assert degrees[1]+degrees[3]-degrees[0]-degrees[2] == coefficient["ordinary"]["I"]
    if point == "one":
        assert row["coefficients"]["E"]["conditional_harmonic_degrees"] == (1, 1, 1, 1)
