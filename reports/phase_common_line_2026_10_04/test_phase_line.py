import pytest
from verify_phase_line import (
    absorption, candidate_point, certificate, field_controls, old, retained_points, split_factor,
)


def test_split_field_control_does_not_average_distinct_roots():
    row = field_controls()
    assert sorted(row["two_roots_with_different_toy_ranks_distinguished"]) == [0, 1]
    assert row["irreducible_quadratic_has_Q_degree_four"]


def test_retains_every_preceding_actual_matter_point():
    assert len(retained_points()) == 12


@pytest.mark.parametrize("seed", [0, 1])
@pytest.mark.parametrize("component", [1, 2])
def test_new_M6_phase_preserves_all_fifth_twist_absorptions(seed, component):
    assert absorption(seed, component)["M6_entrywise_residuals_zero"]


@pytest.mark.parametrize("seed", [0, 1])
@pytest.mark.parametrize("component", [1, 2])
@pytest.mark.parametrize("eta_index", range(4))
def test_all_minor_candidates_processed_over_each_actual_field(seed, component, eta_index):
    eta = tuple(old.character_reduction()["quadratic_characters"][eta_index])
    cert = certificate(seed, component, eta)
    for records in cert["coefficients"].values():
        assert records["interior_upper_bound_off_candidate_roots"] >= 0
    for coefficients in cert["candidate_factors_over_Q"]:
        for factor in split_factor(tuple(coefficients)):
            assert factor["degree_over_K"] <= 12, "Unprocessed root blocks completeness"
            point = candidate_point(seed, component, eta, tuple(tuple(x) for x in factor["coefficients_ab"]))
            assert point["indexed"]["I"] == point["n"]-point["n_dual"]
            assert point["each_irreducible_K_factor_not_an_average"]
