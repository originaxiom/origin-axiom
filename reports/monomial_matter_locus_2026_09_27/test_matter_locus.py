import sympy as sp
from flint import fmpq_mat

from verify_matter_locus import (
    candidate_point, certificate, dual_monomials, ex, pullback_monomials,
    specialization, symbolic_complex,
)
from verify_exceptional import evaluate, matrix, modules, selected_minor, t
from verify_global_seed import eye, pullback
from verify_relative_capacity import relative_h1


def test_signed_dual_is_inverse_transpose():
    gens = [((1, 2, 0), (2, -1, 3), (-1, 1, -1))]
    dual = dual_monomials(gens)
    assert all(sp.simplify(x) == 0 for x in matrix(dual[0])-matrix(gens[0]).inv().transpose())


def test_minor_zero_need_not_be_a_rank_jump():
    a = sp.Matrix([[t-1, 0, 1], [0, 1, 0]])
    record, determinant = selected_minor(a, 2)
    assert determinant.eval(1) == 0
    assert evaluate(a, 1).rank() == record["rank"] == 2


def test_schreier_symbols_and_direct_cone_controls():
    for seed in ex.inputs()["seeds"]:
        gens = pullback_monomials(modules(seed)["E"])
        rep = specialization(gens, fmpq_mat([[2]]))
        down = specialization(modules(seed)["E"], fmpq_mat([[2]]))
        assert rep.mats == pullback(down).mats
        d0, cone = symbolic_complex(gens)
        assert evaluate(d0, 2).rank() == 5
        assert evaluate(cone, 2).rank() == 32
        assert relative_h1(rep, 6, 1)["interior"] == 0


def test_generic_minor_certificates_for_both_actual_duals():
    for i in range(2):
        result = certificate(i)
        for side in ("E", "dual"):
            item = result["coefficients"][side]
            assert item["global_d0"]["rank"] == 5
            assert item["relative_cone"]["rank"] == 32
            assert item["interior_upper_bound_away_from_minor_roots"] == 0


def test_known_equal_nonzero_interior_spaces_not_erased():
    for i in range(2):
        result = candidate_point(i, ("1", "-1"))
        assert result["indexed"]["I"] == 0
        assert result["E_relative"]["interior"] == result["dual_relative"]["interior"] == 1
        assert result["E_relative"]["ordinary"][0] == 1
