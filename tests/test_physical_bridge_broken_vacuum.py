"""R8 pre-run controls: full light space, spectra, phase and finite-VEV kernels."""
import json

import numpy as np
import pytest

from reports.physical_bridge_2026_09_05 import broken_vacuum as b


def test_complete_light_space_is_actual_tree_kernel_modulo_gauge():
    geometry = b.light_geometry()
    assert geometry["L"].shape == (294, 19)
    assert len(geometry["positive_ev"]) == 209
    assert max(geometry["errors"].values()) < 1e-9
    assert [len(indices) for indices in geometry["generator_indices_O_T"]] == [8, 3]


def test_all_quartic_coefficients_and_heavy_exchange_bad_control():
    report = b.quartic()["report"]
    assert report["quadratic_monomial_count"] == 190
    assert report["quartic_monomial_count_checked"] == 7315
    assert len(report["nonzero_quartic_coefficients"]) == 44
    assert report["maximum_coefficient_error"] < 1e-9
    assert report["bare_vs_integrated_octet_quartic"][0] > .19
    assert abs(report["bare_vs_integrated_octet_quartic"][1]) < 1e-16
    assert report["exact_weak_identity"]["both_doublet_square_remainders"] == ["0", "0"]


def test_full_quantum_matrix_and_fresh_all_component_force_scaling():
    result = b.quantum_data()["report"]
    assert np.array(result["entire_19_curvature_matrix"]).shape == (19, 19)
    assert result["block_form_error"] < 1e-9
    assert [row["epsilon"] for row in result["fresh_scaled_forces"]] == [.01, .0025]
    for row in result["fresh_scaled_forces"]:
        assert np.array(row["gradient_parts"]).shape == (3, 294)
        assert row["normalized_scaling_error"] < 1e-9


@pytest.fixture(scope="module")
def result():
    return b.analyze()


def test_neutral_and_charged_leading_minima_are_both_kept(result):
    for epsilon in b.EPSILONS:
        pair = [row for row in result["broken_states"] if row["epsilon"] == epsilon]
        assert len(pair) == 2
        assert abs(pair[0]["leading_potential"]-pair[1]["leading_potential"])/epsilon**3 < 1e-9
        assert all(row["positive_light_modes"] == 13 and row["angular_zero_modes"] == 6 for row in pair)
        assert [row["remaining_physical_leading_zero_modes"] for row in pair] == [3, 2]
        m_o, m_t, m_u, m_d = result["quantum"]["masses_O_T_U_D"]
        triplet = m_t+.02/12*(-m_u/.2-m_d/.2)
        expected = np.sort([0.]*6+[m_o]*8+[triplet]*3+[-2*m_u, -2*m_d])
        for row in pair:
            assert np.max(np.abs(np.array(row["light_mass_squared_over_epsilon_squared"])-expected)) < 1e-9
            assert abs(row["leading_potential"]/epsilon**3+(m_u**2+m_d**2)/.8) < 1e-9


def test_actual_electromagnetic_and_color_stabilizers_and_vector_masses(result):
    for row in result["broken_states"]:
        assert len(row["vector_mass_squared_all_78"]) == 78
        assert row["color_action_error"] < 1e-9
        if row["orientation"] == "neutral":
            assert row["unbroken_gauge_dimension"] == 9
            assert row["electromagnetic_action_norm"] < 1e-9
            predicted = row["neutral_W_W_Z_leading_prediction"]
            assert abs(predicted[2]/predicted[0]-8/5) < 1e-12
        else:
            assert row["unbroken_gauge_dimension"] == 8
            assert row["electromagnetic_action_norm"] > 1e-6


def test_every_fermion_singular_mass_and_exact_finite_VEV_control_is_reported(result):
    assert len(result["exact_fermion_controls"]) == 2
    for row in result["broken_states"]:
        assert len(row["fermion_singular_masses_all_27"]) == 27
        assert len(row["fermion_leading_projection_all_17"]) == 17
        assert np.isfinite(row["fermion_singular_masses_all_27"]).all()
        if row["orientation"] == "neutral":
            assert row["fermion_leading_projected_rank"] == 16
            assert row["Q_Yukawa_invariance_error"] < 1e-9
    # Full finite-VEV ranks are outputs, not overwritten by the leading rank.
    for orientation in ["neutral", "charge_breaking"]:
        rows = [row for row in result["broken_states"] if row["orientation"] == orientation]
        assert rows[1]["fermion_projection_relative_error"] < rows[0]["fermion_projection_relative_error"]+1e-12
        control = next(c for c in result["exact_fermion_controls"] if c["orientation"] == orientation)
        for row in rows:
            assert row["fermion_full_numerical_rank"] == control["rational_control_full_rank"]
            assert row["fermion_leading_projected_rank"] == control["leading_projected_rank"]


def test_phase_symmetry_is_checked_on_full_action_and_anomaly_not_ignored(result):
    phase = result["phase_symmetry"]
    assert phase["residual_U_D_charges"] == ["-18/5", "-12/5"]
    assert phase["mixed_color_anomaly_trace"] == "3"
    assert not phase["quantum_exact_Goldstone_claimed"]
    assert phase["classical_potential_phase_error"] < 1e-10
    for row in result["broken_states"]:
        if row["orientation"] == "neutral":
            assert row["global_phase_physical_norm"] > 1e-6


def test_export_round_trip_keeps_numpy_integer_keys_and_all_states(result):
    assert json.loads(json.dumps(b.native({np.int64(7): np.int64(3)}))) == {"7": 3}
    loaded = json.loads(json.dumps(result, allow_nan=False))
    assert len(loaded["broken_states"]) == 4
    assert all(len(row["fermion_singular_masses_all_27"]) == 27 for row in loaded["broken_states"])
    with pytest.raises(TypeError):
        b.native(object())
