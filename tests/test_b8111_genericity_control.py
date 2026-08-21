"""B8111 -- locks the genericity control's MATHEMATICS, read from results.json, not from prose."""
import json, os, hashlib, math
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARC = os.path.join(ROOT, "frontier", "B8111_genericity_control")
R = json.load(open(os.path.join(ARC, "results.json")))
PHI = (1 + 5 ** 0.5) / 2


def test_seal_is_over_the_preregistration_and_matches():
    b = open(os.path.join(ARC, "PREREGISTRATION.md"), "rb").read()
    assert hashlib.sha256(b).hexdigest() in open(os.path.join(ARC, "SEAL.txt")).read()


def test_menu_sizes_are_three_four_five():
    assert R["menu_sizes"] == {"2T": 3, "2O": 4, "2I": 5}


def test_the_five_golden_tones_are_the_pentagon_census():
    got = [float(v) for v in R["menus"]["2I"]]
    want = [0.0, 1 / (2 * PHI), 0.5, PHI / 2, 1.0]
    assert all(abs(a - b) < 1e-12 for a, b in zip(sorted(got), want))


def test_exactly_three_tones_are_shared_by_all_three_groups():
    """The bite: {0, 1/2, 1} discriminate NOTHING."""
    shared = [float(v) for v in R["shared_by_all_three"]]
    assert sorted(shared) == [0.0, 0.5, 1.0]
    assert R["discriminating_fraction_vs_2O"] == "2/5"


def test_only_phi_over_2_and_one_over_2phi_are_golden_unique():
    got = sorted(float(v) for v in R["golden_minus_silver"])
    assert all(abs(a - b) < 1e-12 for a, b in zip(got, [1 / (2 * PHI), PHI / 2]))


def test_silver_carries_root2_and_2T_is_entirely_rational():
    assert R["2O_menu_contains_sqrt2"] and R["2I_menu_contains_sqrt5"]
    assert R["2T_menu_all_rational"]
    assert abs(float(R["silver_minus_golden"][0]) - 2 ** 0.5 / 2) < 1e-12


def test_shape_is_not_generic_so_the_outcome_is_A_not_the_predicted_B():
    assert R["same_cardinality_2O_2I"] is False
    assert R["outcome"] == "A"


def test_resolution_requirement_is_phi_over_2_minus_root2_over_2():
    assert abs(R["min_resolution_required"] - (PHI / 2 - 2 ** 0.5 / 2)) < 1e-12


def test_bronze_has_no_binary_polyhedral_partner():
    assert R["bronze_has_no_partner"] is True
    for orders in R["element_orders"].values():
        assert 13 not in orders
    # the field half of the proof: Q(sqrt13) would have to BE one of the three quadratic subfields
    assert not any(math.isqrt(13 * d) ** 2 == 13 * d for d in (2, 5, 10))


def test_fricke_invariant_is_preserved_across_the_metallic_index():
    """The hazard CONFIRMED on the kappa route: generic for golden, silver AND bronze."""
    assert all(R["fricke_preserved_m"][m] in (True, "True") for m in ("1", "2", "3"))
