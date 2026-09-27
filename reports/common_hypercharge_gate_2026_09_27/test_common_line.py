from itertools import product
import sympy as sp
from flint import fmpq_mat

from verify_common_line import (
    absorption, candidate_point, certificate, character_reduction,
    finite_dual, ml, parent_center, specialization, twisted_gens,
)


def test_finite_dual_against_independent_bruteforce_control():
    a = sp.Matrix([[2, 1], [0, 3]])
    values, _ = finite_dual(a, 6)
    expected = sorted(x for x in product(range(6), repeat=2)
                      if all(v % 6 == 0 for v in a*sp.Matrix(x)))
    assert values == expected and len(values) == 6


def test_marked_character_reduction_not_abstract_homology_only():
    r = character_reduction()
    assert r["character_count"] == 320 and r["fourth_power_count"] == 20
    assert len(r["quadratic_characters"]) == 4
    assert r["longitude_exponents"] == (0,)*7
    assert all(c[0] == 0 for c in r["quadratic_characters"])
    assert len({tuple(x["character"]) for x in r["fourth_power_decomposition"]}) == 20


def test_global_kernel_and_wrong_central_compensation():
    r = parent_center()
    assert (1, 4) in r["line_structure_kernel"]
    assert (1, 1) not in r["line_structure_kernel"]
    assert not r["nonliftable_bundles_classified"]


def test_fifth_root_absorption_is_entrywise_for_both_seeds():
    for number in range(2):
        r = absorption(number)
        assert r["entrywise_residuals_mod5"] == [[0]*5]*3


def test_quadratic_twists_are_actual_duals_and_have_same_cusp():
    for number in range(2):
        for e in character_reduction()["quadratic_characters"]:
            gens = twisted_gens(number, tuple(e))
            rep = specialization(gens, fmpq_mat([[2]]))
            assert specialization(ml.dual_monomials(gens), fmpq_mat([[2]])).mats == rep.dual().mats
            d0, cone = ml.symbolic_complex(gens)
            assert d0.shape == (35, 5) and cone.shape == (40, 40)


def test_all_candidates_are_exactly_processed_without_outcome_assumption():
    for number in range(2):
        for e in character_reduction()["quadratic_characters"]:
            eta = tuple(e)
            cert = certificate(number, eta)
            for factor in cert["candidate_factors"]:
                assert len(factor)-1 <= 12, "An unanalysed factor blocks completeness"
                r = candidate_point(number, eta, tuple(factor))
                assert r["indexed"]["I"] == r["E_relative"]["interior"]-r["dual_relative"]["interior"]


def test_untwisted_positive_paired_matter_is_retained():
    for number in range(2):
        r = candidate_point(number, (0,)*7, ("1", "-1"))
        assert r["E_relative"]["interior"] == r["dual_relative"]["interior"] == 1
        assert r["indexed"]["I"] == 0
