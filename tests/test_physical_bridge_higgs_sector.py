"""Pre-run R7 controls; no desired sign is imposed on quantum Higgs masses."""
import numpy as np
import pytest

from reports.physical_bridge_2026_09_05 import higgs_sector as h


def test_full_constraint_J_H_derivatives_and_complex_covariance():
    result = h.primitive_checks()
    assert result["full_H_first_error"] < 2e-9
    assert result["full_H_second_error"] < 3e-7


def test_complete_tree_spectrum_and_actual_doublet_actions():
    result = h.classical()
    assert result["real_scalars"] == 294
    assert result["physical_zero_modes"] == {"old_octet_triplet": 11, "new_Higgs_real": 8}
    assert result["new_positive_scalar_gap"] > 0


def test_parameter_controls_remove_or_restore_light_modes():
    result = h.primitive_checks()
    assert result["detuned_offset_scalar_kernel"] == 77
    assert result["omitted_cubic_scalar_kernel"] == 89


def test_projected_Yukawa_masses_use_the_actual_mixed_light_kernel():
    result = h.exact_yukawa_projection()
    assert result["old_kernel_dimension"] == 17
    assert result["combined_projected_rank"] == 16
    assert {name: block["rank"] for name, block in result["blocks"].items()} == {
        "up": 3, "down": 3, "charged_lepton": 1, "neutral": 2}


def test_extra_scalar_fourth_mass_traces_exactly_constant_on_norm_family():
    result = h.extra_fourth_trace_identity()
    assert set(result) == {"U", "D"}
    assert all(row["remainder"] == "0" for row in result.values())


def test_spectral_derivative_scalar_and_complex_rotating_controls():
    matrix = np.diag([1., 3.])
    generator = np.array([[0., 1.], [1., 0.]])
    first = 1j*(generator@matrix-matrix@generator)
    second = -(generator@generator@matrix-2*generator@matrix@generator+matrix@generator@generator)
    assert np.max(np.abs(first.imag)) > 1
    assert abs(h.SpectralTrace(matrix, 1.5, 1.).second(first, second)) < 1e-10
    scalar = h.SpectralTrace(np.diag([2.]), 1.5, 1.)
    fp, fpp = 2*(2*np.log(2)-2), 2*np.log(2)
    assert abs(scalar.first(np.diag([3.]))-3*fp) < 1e-12
    assert abs(scalar.second(np.diag([3.]), np.diag([4.]))-(4*fp+9*fpp)) < 1e-12


def test_bad_mass_and_linear_massless_block_are_not_silently_logged():
    with pytest.raises(ValueError):
        h.SpectralTrace(np.diag([1., -.01]), 1.5, 1.)
    trace = h.SpectralTrace(np.diag([0., 1.]), 1.5, 1.)
    with pytest.raises(ValueError):
        trace.second(np.diag([.01, 0.]), np.zeros((2, 2)))


def test_full_quantum_force_covariance_and_expanded_shift_identity():
    result = h.quantum()
    assert [row["mu"] for row in result["runs"]] == [.5, 1., 2.]
    for row in result["runs"]:
        assert max(row["kernel_force_and_stationarity_residual"]) < 1e-8
        assert row["SM_covariance_and_normal_shift_identity"]
        masses = np.asarray(row["Higgs_leading_mass_squared"])
        assert masses.shape == (8,) and np.isfinite(masses).all()
