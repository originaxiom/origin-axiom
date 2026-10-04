import pytest
import verify_interaction as m


@pytest.mark.parametrize("seed", [0, 1])
@pytest.mark.parametrize("component", [1, 2])
@pytest.mark.parametrize("dual", [False, True])
def test_actual_ordinary_and_fixed_peripheral_continuation(seed, component, dual):
    row = m.continuation(seed, component, -1, "E", dual)
    assert row["interior_input_dimension"] == 1
    assert row["ordinary_obstruction_rank"] <= row["fixed_peripheral_obstruction_rank"] <= 1
    assert (row["ordinary_witness"] is None) == (row["ordinary_obstruction_rank"] == 0)
    assert row["boundary_connecting_obstruction_zero"] and row["dual_number_fox_check"]


@pytest.mark.parametrize("seed", [0, 1])
@pytest.mark.parametrize("component", [1, 2])
def test_actual_new_harmonic_and_parent_transfer(seed, component):
    row = m.harmonic_transfer(seed, component)
    assert row["actual_diagonal_bundle_unchanged"] and row["nonzero_interior_exponent_class"]
    assert row["finite_unitary_center"] and row["structure_adjoint_H0"] >= 0


def test_instrument_discriminates_relative_only_and_higher_order():
    assert all(m.instrument_controls().values())


def test_absent_modes_and_original_zero_cubic_comparator():
    assert len(m.comparators()) == 12
