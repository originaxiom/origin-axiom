"""R11 locks compare actual actions, not only equal orders or transcript strings."""
from fractions import Fraction as F

import pytest
import sympy as sp

from reports.physical_bridge_2026_09_05 import family_action as f


@pytest.fixture(scope="module")
def result():
    return f.run()


def test_lattice_integrality_and_a_corrupt_root_are_checked(result):
    row = result["lattice"]
    assert row["denominator"] == 4 and row["gram_determinant"] == 1
    assert row["scale_two_rejected"]
    with pytest.raises(ValueError, match="truncation forbidden"):
        f.integerize(sp.Matrix([[sp.Rational(1, 4)]]), 2)
    rr = list(f.roots())
    rr[0] = f.scale(rr[0], 2)
    with pytest.raises(ValueError, match="norm-two roots"):
        f.lattice_check(rr)


def test_marked_map_verifies_all_products_and_rejects_bad_assignment(result):
    iso = result["marked_isomorphism"]
    assert iso["all_product_checks"] == 14400 and len(iso["map"]) == 120
    assert iso["invalid_equal_generator_assignment_rejected"]
    assert f.qmul(f.qmul(result["founding_g"], result["founding_g"]), result["founding_g"]) == f.ONE


def test_root_space_actions_are_not_identified_from_orbit_counts(result):
    assert len(result["all_twenty_actions"]) == 20
    for row in result["all_twenty_actions"]:
        assert row["root_space_fixed_dimensions"] == {"L": 0, "W": 6, "U": 2}
        assert row["E6_fixed_roots"] == {"L": 0, "W": 72, "U": 0}
        assert row["family_action_predicate"] == {"L": False, "W": True}


def test_commuting_split_reconstructs_literal_action_exactly(result):
    row = next(r for r in result["all_twenty_actions"] if "matrices" in r)
    L, W, U = (sp.Matrix(row["matrices"][k]) for k in ("L", "W", "U"))
    assert L == U*W == W*U and L != W
    rebuilt = sp.eye(8)
    for j in row["E6_reflection_word_for_U"]:
        rebuilt *= f.reflection(row["simple_roots"][j])
    assert rebuilt == U
    assert all(f.operator(W)(r) == r for r in row["E6_roots"])


def test_six_classes_have_the_same_cycles_but_distinct_internal_actions(result):
    row = next(r for r in result["all_twenty_actions"] if "matrices" in r)
    assert row["class_permutations"]["L"] == row["class_permutations"]["W"]
    assert all(k == v for k, v in row["class_permutations"]["U"])
    assert sum(len(v) == 27 for k, v in row["root_classes"]) == 6
    assert row["E6_root_cycles"]["L"] == {3: 24}
    assert row["E6_root_cycles"]["W"] == {1: 72}


def test_map_is_equivariant_and_orientation_is_not_silently_fixed(result):
    assert result["unit_conjugation_covariance_checks"] == 2400
    assert result["inverse_orientation_checks"] == 20
    assert result["unoriented_Eisenstein_planes"] == 10
    assert result["order_four_complement_control"] != 72


def test_family_lift_has_order_three_and_lie_centralizer_control(result):
    n = sp.Matrix(result["SU3_order_three_representative"])
    assert n**3 == sp.eye(3) and n.det() == 1 and n.T*n == sp.eye(3)
    assert n != sp.eye(3) and (n-sp.eye(3)).rank() == 2
    for row in result["all_twenty_actions"]:
        assert row["mixed_E6_A2_root_sum_checks"] == 432


def test_exact_arithmetic_and_input_provenance_are_retained(result):
    assert f.bil(f.ONE, f.ONE) == F(2)
    assert f.qmul(f.ONE, f.ONE) == f.ONE
    assert len(result["source_receipts"]) == 3
    assert all(len(r["sha256"]) == 64 and len(r["commit"]) == 40 for r in result["source_receipts"])
