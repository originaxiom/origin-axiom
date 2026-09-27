import pytest
from verify_centralizer import (
    certificate, diagonal_control, enhanced_matter, finite_control,
    inputs, point, root_control, tangent_control,
)


def test_entire_D5_root_system_not_only_dimension():
    row = root_control()
    assert row["commuting_root_count"] == 40 and row["commuting_Cartan_dimension"] == 5
    assert row["full_D5_root_labels_match"]


def test_full_parent_branching_and_actual_dual_spinor_control():
    row = root_control()
    assert row["full_248_branching_match"]
    assert row["spinor_weights_distinct_and_contragredient"]
    assert row["wrong_spinor_conjugation_rejected"]


def test_center_breaks_exactly_the_extra_D5_roots():
    row = root_control()
    assert row["fifth_center_invariant_roots"] == 20
    assert row["D5_extra_torus_root_charges"] == {0: 20, 4: 10, -4: 10}


@pytest.mark.parametrize("seed", [0, 1])
def test_actual_M6_finite_image_and_scalar_character_independence(seed):
    row = finite_control(seed)
    assert row["M6_permutation_image_order"] == 60
    assert row["permutation_and_chi5_image_order"] == 300
    assert row["invariants_U_wedgeU_adU"] == [0, 0, 0]


@pytest.mark.parametrize("seed", [0, 1])
def test_exact_all_t_global_minor_certificates_and_every_factor(seed):
    row = certificate(seed)
    assert diagonal_control(seed)["H0"] == 0
    assert row["generic_full_parent_dimension"] == 24
    for factor in row["candidate_factors"]:
        assert len(factor)-1 <= inputs()["max_factor_degree"]
        result = point(seed, tuple(factor))
        assert result["full_parent_dimension"] >= 24
        assert result["H0"]["E"] == result["H0"]["dual_E"]


@pytest.mark.parametrize("seed", [0, 1])
def test_actual_undeformed_multiplets_against_independent_branch_bookkeeping(seed):
    row = enhanced_matter(seed)
    assert row["full_degree_one_dimension"] == row["original_branching_total"]
    assert row["conditional_D5_degree_one_spectrum"]["16"] == row["conditional_D5_degree_one_spectrum"]["16_dual"]


@pytest.mark.parametrize("seed", [0, 1])
def test_actual_harmonic_tangent_enters_both_spinor_slots(seed):
    row = tangent_control(seed)
    assert row["norm_fractions_U_dualU_adU"] == ["1/5", "1/5", "3/5"]
    assert row["orthogonal_parallel_projection"] and row["nonzero_actual_harmonic_class_rechecked"]
    assert not row["individual_nonlinear_integrability_claimed"]
