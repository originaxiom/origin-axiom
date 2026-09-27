import pytest
import verify_admission as v


def test_all_parent_weights_and_actual_duals():
    assert v.parent_control()["all_parent_weight_multiplicities"] == 248


def test_hypercharge_must_be_in_the_centralizer_question():
    x = v.parent_control()
    assert (x["SM_connected_centralizer_dimension"], x["without_Y_centralizer_dimension"]) == (25, 35)


def test_exact_common_kernel():
    assert v.parent_control()["line_structure_kernel_mod5"] == [(a, -a % 5) for a in range(5)]


def test_nonintegral_parent_weight_is_rejected():
    with pytest.raises(AssertionError):
        v.gl_weight((1, 0, 0, 0), 2)


def test_marked_homology_and_fifth_power_fibers():
    x = v.topology_control()
    assert x["smith_factors_after_free_split"] == [1, 1, 1, 1, 8, 40]
    assert (x["torsion_character_count"], x["fifth_image_count"], x["fifth_kernel_count"]) == (320, 64, 5)


def test_all_five_obstruction_classes_represented():
    x = v.topology_control()
    assert x["all_cosets_exhaustive_and_disjoint"] and len(x["witness_coset_representatives_mod40"]) == 5


def test_actual_nonliftable_unitary_witness_and_peripheral_words():
    x = v.diagonal_witness()
    assert x["honest_unitary_representation"] and not x["separate_flat_lift_exists"]
    assert x["all_peripheral_matrices_identity"]
    assert x["charged_ranks"] == {"Q": 5, "u": 5, "e": 5, "d": 10, "L": 10}


def test_scalar_twisting_cannot_change_obstruction():
    assert v.controls()["all_320_scalar_twists_preserve_nonliftability"]


def test_fifth_power_map_two_sided_controls():
    x = v.controls()
    assert x["C4_fifth_power_surjective"] and x["C5_fifth_power_not_surjective"]
