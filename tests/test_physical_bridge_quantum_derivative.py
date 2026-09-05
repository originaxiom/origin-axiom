"""Post-first-result, pre-derivative-run locks and independent matrix controls."""
import numpy as np
import pytest

from reports.physical_bridge_2026_09_05 import quantum_derivative as d


def test_exact_polynomial_trace_not_only_sampled_points():
    result = d.exact_fourth_trace_identity()
    assert result["scalar"]["remainder"] == result["vector"]["remainder"] == "0"


def test_analytic_and_finite_derivatives_agree_without_assuming_sign():
    result = d.analytic_curvatures()
    for mode in result.values():
        assert max(abs(x) for x in mode["finite_minus_analytic"]) < 5e-6


def test_nondegenerate_scalar_toy_with_nonzero_curvature():
    # x(t)=2+3t+2t^2; exact f' x''+f'' (x')^2.
    constant = 1.5
    slope, second = d.trace_function_derivatives([[2]], [[3]], [[4]], constant)
    fp = 2*(2*np.log(2)-2*constant+1)
    fpp = 2*np.log(2)-2*constant+3
    np.testing.assert_allclose([slope, second], [3*fp, 4*fp+9*fpp], atol=1e-12)
    assert abs(second) > .1


def test_rotation_and_degenerate_eigenvalue_controls():
    m = np.diag([2., 3.])
    r = np.array([[0., -1.], [1., 0.]])
    first = r@m-m@r
    second = r@first-first@r
    np.testing.assert_allclose(d.trace_function_derivatives(m, first, second, 1.5), [0, 0], atol=1e-12)
    # Splitting a degenerate pair is nontrivial: x=2 +/- t.
    _, value = d.trace_function_derivatives(2*np.eye(2), np.diag([1., -1.]), np.zeros((2, 2)), 1.5)
    assert abs(value-4*np.log(2)) < 1e-12


def test_emerging_zero_mass_and_invalid_linear_kernel():
    assert d.trace_function_derivatives([[0]], [[0]], [[2]], 1.5) == (0, 0)
    with pytest.raises(ValueError):
        d.trace_function_derivatives([[0]], [[1]], [[0]], 1.5)
