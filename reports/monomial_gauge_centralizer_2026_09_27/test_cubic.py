import pytest
from verify_cubic import gauge_weight_control, overlap_control, result_locks, symmetric_mode_control


@pytest.mark.parametrize("seed", [0, 1])
def test_all_three_neutral_modes_are_symmetric_not_just_examples(seed):
    row = symmetric_mode_control(seed)
    assert row["projector_ranks"] == [9, 6, 1]
    assert row["cohomology"]["skew"]["n"] == 0
    assert row["cohomology"]["symmetric_tracefree"]["n"] == 3
    assert row["neutral_finite_coefficient_split"] == {"U": 1, "irreducible_five": 2}


def test_symbolic_singlet_and_mixed_overlaps():
    row = overlap_control()
    assert row["all_symmetric_singlet_cubic_zero"] and row["shared_profile_mixed_cubic_zero"]


def test_nondegenerate_positive_controls():
    row = overlap_control()
    assert row["skew_singlet_counterexample"] == -4
    assert row["skew_mixed_counterexample"] == 2
    assert row["independent_profile_counterexample"] == 1


def test_actual_spinor_weight_parity_and_contragredience():
    row = gauge_weight_control()
    assert row["spinor_pairing_opposite_only"] and row["no_three_spinor_zero_weight"]


def test_observed_full_parent_result_regressions():
    assert result_locks()["post_result_gauge_and_matter_locks"]
