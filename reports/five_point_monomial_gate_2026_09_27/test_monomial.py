from flint import fmpq_mat

from verify_monomial import (
    algebra_dimension, bilinear_nullity, compose, exponent_space, five_point_action,
    inputs, minverse, monomial_matrices, mword, offdiagonal_action, one_seed,
    pmat, primitive, product, rowperm,
)
from verify_global_seed import Rep, eye, zero
from verify_topology import cover


def test_monomial_product_and_inverse_conventions():
    p, q = (1, 2, 0, 3, 4), (1, 0, 2, 4, 3)
    x, y = fmpq_mat([[i] for i in range(5)]), fmpq_mat([[2-i] for i in range(5)])
    a, b = (p, x), (q, y)
    r, z = product(a, b)
    assert r == compose(p, q)
    assert z == x+rowperm(y, p)
    identity, exponent = product(a, minverse(a))
    assert identity == tuple(range(5)) and exponent == zero(5, 1)
    assert pmat(p)*pmat(q) == pmat(compose(p, q))


def test_burnside_control_needs_full_algebra_not_only_small_commutant():
    shift = pmat((1, 2, 3, 4, 0))
    diagonal = fmpq_mat([[i+1 if i == j else 0 for j in range(5)] for i in range(5)])
    assert algebra_dimension([shift, diagonal]) == 25
    assert algebra_dimension([eye(5)]) == 1
    assert bilinear_nullity([eye(5)]) == 25


def test_primitive_integer_conversion():
    assert primitive([0, "1/2", "-1/3"]) == [0, 3, -2]
    assert primitive(["-2/3", "4/3"]) == [1, -2]


def test_both_exact_five_point_actions():
    for seed in inputs()["seeds"]:
        pg, info = five_point_action(seed)
        assert info["faithful_even_image_order"] == 60
        assert info["V4_count"] == 5
        assert sum(i == pg[0][i] for i in range(5)) == 2
        assert Rep([pmat(p) for p in pg]).word(cover(2)[2]) == pmat(info["longitude"])


def test_family_relators_hold_at_unfitted_parameters():
    for seed in inputs()["seeds"]:
        pg, info = five_point_action(seed)
        directions, _ = exponent_space(pg)
        for direction in directions:
            for t in (-1, 3, 5):
                matrices = monomial_matrices(pg, direction, t)
                rep = Rep(matrices)
                assert all(g.det() == 1 for g in matrices)
                assert all(rep.word(r) == eye(5) for r in cover(2)[0])
                assert rep.word(cover(2)[2]) == pmat(info["longitude"])
                assert len(offdiagonal_action(matrices, pg)) == 3


def test_reported_diagnostics_respect_invariant_identity():
    for i in range(2):
        result = one_seed(i)
        assert result["finite_control"]["algebra_dimension"] < 25
        assert result["finite_control"]["bilinear_form_dimension"] > 0
        for row in result["candidates"]:
            for coefficient in row["diagnostics"]["coefficients"].values():
                for level in ("M2", "M6"):
                    data = coefficient[level]
                    v, dual = data["V"], data["dual"]
                    assert data["I"] == v[0]-dual[0]+dual[2]-v[4]
                    assert v[4]+dual[4] == v[3]
