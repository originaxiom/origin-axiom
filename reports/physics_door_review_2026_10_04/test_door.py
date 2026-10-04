import pytest
from verify_door import (
    axis_control, coefficient_controls, commutant_control,
    exterior_differential_control, punctured_sphere_relative,
    relative_controls, torus_scope_control,
)


def test_transformed_representation_composition_and_actual_relation():
    rows = coefficient_controls()
    assert len(rows) == 5
    assert all(row["transformed_c_equals_ab_relation_fails"] for row in rows[1:])
    assert not rows[0]["transformed_c_equals_ab_relation_fails"]


def test_commutant_one_with_proper_invariant_flag():
    row = commutant_control()
    assert row["commutant_dimension"] == 1
    assert row["proper_invariant_flag_dimensions"] == [1, 2, 3, 4]


def test_generic_transverse_source_not_erased_by_mixing_quartic():
    assert axis_control()["finite_quartic_not_exact_generic_source_selector"]


def test_every_declared_relative_partition_and_sign_reversal():
    assert len(relative_controls()) == sum(2**N-2 for N in range(2, 9))


@pytest.mark.parametrize("N", range(2, 9))
def test_diagnostic_is_not_only_favorable_three(N):
    row = punctured_sphere_relative(N, (N-1,))
    assert row["b1_relative"] == 0
    assert row["b2_relative"] == N-2


def test_three_diagnostic_not_an_OA_source_derivation():
    assert punctured_sphere_relative(5, (4,))["relative_Euler"] == 3
    assert punctured_sphere_relative(5, (0, 1, 2, 3))["relative_Euler"] == -3
    assert not exterior_differential_control()["OA_source_law_derived"]


def test_actual_deformed_differential_squares_to_zero():
    assert exterior_differential_control()["D_squared_zero_test_forms"] == 4


def test_torus_and_annulus_zero_is_retained_in_its_scope():
    assert len(torus_scope_control()) == 16
