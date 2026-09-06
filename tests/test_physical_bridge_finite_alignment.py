"""R10 live determinant, extraction, geometry and relaxation controls."""
import numpy as np
import pytest

from reports.physical_bridge_2026_09_05 import finite_alignment as f


def test_extrapolator_recovers_and_rejects_corruption():
    controls = f.instrument_controls()
    assert controls["corrupted_polynomial_rejected"]
    assert controls["invalid_matrix_controls_rejected"] == 5
    assert abs(controls["known_polynomial_intercept"]-1.25) < 1e-10


def test_mass_polynomials_normal_force_and_mixed_response():
    result = f.geometry_controls()
    assert max(result["mass_polynomial_and_tree_normal_force_errors"]) < 1e-10
    assert result["normal_mixed_derivative_error"] < 2e-8


def test_hard_quartic_two_methods_and_all_angles():
    result = f.matching()
    assert result["orientation_agreement"] < f.QUARTIC_TOL
    assert all(r["method_discrepancy"] < f.QUARTIC_TOL for r in result["all_orientation_fits"])
    assert len(result["all_orientation_fits"]) == 6


def test_spectral_separation_counts_are_not_soft_mode_deletions():
    result = f.matching()
    for path in result["raw_paths"]:
        for row in path:
            for spec, count, total in zip(row["spectral_envelopes"], f.COUNTS, [294, 27, 78]):
                assert spec["hard_count"] == count
                assert spec["soft_count"] == total-count
                assert spec["hard_min"] > 0
                assert spec["low_max"] < .85*spec["hard_min"]


def test_exact_all_field_fierz_and_triplet_holdouts():
    assert f.fierz() == ["0", "0", "0"]
    result = f.triplet()
    assert result["source_shape_error"] < f.SOURCE_TOL
    assert abs(result["relaxation_cB"]-result["endpoint_cB"]) < 1e-9
    for row in result["angles"]:
        assert row["stationarity_residual"] < 1e-12
        assert row["relaxation_energy_over_epsilon4"] <= 0


def test_all_color_octet_sources_remain_zero():
    result = f.octet_control()
    assert np.max(np.abs(result["hard_source"])) < 2e-8
    assert np.max(np.abs(result["normal_source"])) < 2e-8


def test_combination_retains_all_terms_and_inherited_log_slope():
    result = f.combined()
    assert len(result["angle_samples"]) == 28
    neutral = [row for row in result["angle_samples"] if row["eta"] == 1.]
    expected = float(f.a.symbolic()["fixed_coefficient"])/(64*np.pi**2)*np.prod(f.matching()["rU_rD"])
    left, right = neutral[:2]
    assert abs((left["sum_over_epsilon4"]-right["sum_over_epsilon4"])
               /np.log(left["epsilon"]/right["epsilon"])-expected) < 1e-12
    for row in result["angle_samples"]:
        assert abs(sum(row[k] for k in ["logarithm", "finite_soft", "finite_hard", "triplet_relaxation"])
                   -row["sum_over_epsilon4"]) < 1e-12


def test_invalid_extraction_data_cannot_be_silently_accepted():
    with pytest.raises(ValueError):
        f.extrapolate([1, 2, 3], 1e-5)
    with pytest.raises(ValueError):
        f.extrapolate([np.nan]*6, 1e-5)
