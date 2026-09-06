"""R9 pre-execution locks: all complex orientations and honest matching scope."""
import json

import numpy as np
import pytest
import sympy as sp

from reports.physical_bridge_2026_09_05 import infrared_alignment as a


def test_exact_full_complex_field_fourth_trace_identities():
    result = a.symbolic()
    assert result["report"]["quartic_monomials_covered"] == 330
    assert result["report"]["vector_fourth_trace_remainder"] == "0"
    assert result["report"]["fermion_fourth_trace_remainder"] == "0"
    assert result["fixed_coefficient"] == sp.Rational(23, 80)
    assert result["vector_matrix"].shape == (4, 4)
    assert result["fermion_matrix"].shape == (17, 17)


def test_complete_operator_basis_and_no_unpriced_phase_breaking_term():
    rows = a.invariant_basis()
    assert [row["all_monomials"] for row in rows] == [8, 36, 120, 330]
    assert [row["invariant_dimension"] for row in rows] == [0, 2, 0, 4]
    assert len(rows[-1]["basis"]) == 4


def test_actual_generator_and_tensor_controls_are_independent_of_trace_formula():
    result = a.matrix_controls()
    assert np.max(result["generic_complex_vector_fermion_errors"]) < 1e-10
    assert result["Q_action_charged_neutral"][0] > .1
    assert result["Q_action_charged_neutral"][1] < 1e-10


def test_all_resummed_scalar_modes_and_physical_charged_penalty():
    result = a.scalar_and_angular_controls()
    assert len(result["resummed_scalar_squared_masses_all_19"]) == 19
    assert max(result["scalar_orientation_errors"]) < 1e-9
    eigenvalues = np.asarray(result["penalty_Hessian_eigenvalues"])
    assert np.count_nonzero(eigenvalues > 1e-9) == 2
    assert np.count_nonzero(np.abs(eigenvalues) < 1e-9) == 6
    assert result["phase_Hessian_residual"] < 1e-10


def test_logarithmic_preference_on_every_predeclared_orientation():
    result = a.alignment()
    assert result["neutral_minus_charged_log_coefficient"] > 0
    for row in result["all_orientation_runs"]:
        assert row["log_slope_error"] < 1e-12
        assert [len(values) for values in row["squared_masses_scalar_Weyl_vector"]] == [19, 17, 12]
        if row["eta"]:
            assert all(run["logarithmic_part_over_epsilon4"] < 0 for run in row["runs"])


def test_finite_hard_terms_can_change_finite_point_verdict_and_are_not_inserted():
    result = a.alignment()
    assert not result["full_finite_matching_computed"]
    assert not result["finite_epsilon_vacuum_selection_claimed"]
    for control in result["finite_hard_counterterm_sensitivity"]:
        negative, positive = control["total_B2_coefficients_over_epsilon2"]
        assert negative < 0 < positive
    assert result["wrong_Weyl_sign_control"] == {
        "correct_pure_Yukawa_coefficient": "16", "wrong_coefficient": "-16"}


def test_invalid_inputs_and_negative_mass_logs_fail_closed():
    with pytest.raises(ValueError):
        a.representative(-.1)
    with pytest.raises(ValueError):
        a.representative(1.1)
    with pytest.raises(ValueError):
        a.log_potential([np.array([-1.]), np.zeros(1), np.zeros(1)], .01)
    with pytest.raises(ValueError):
        a.log_potential([np.zeros(1)]*3, 0)


def test_result_export_keeps_all_seven_orientations():
    result = json.loads(json.dumps(a.analyze(), allow_nan=False))
    assert len(result["alignment"]["all_orientation_runs"]) == 7
    assert all(len(row["runs"]) == 4 for row in result["alignment"]["all_orientation_runs"])
