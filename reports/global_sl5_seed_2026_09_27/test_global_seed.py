from itertools import product

import pytest
from flint import fmpq_mat

from verify_topology import (
    abelian_diagonal, canonical, cover, data, diagram_certificate,
    generator_words, inv, longitude_commutator_certificate, reduce, rewrite, substitute,
)
from verify_global_seed import (
    Rep, cohom, eye, hs, indexed, mixed_control, native_doublet, null_columns,
    one_twist, parent, scalar_rep, wedge_over_field, zero, zeta5,
)


def test_schreier_free_word_identity():
    for n in (2, 6):
        images = dict(enumerate(generator_words(n), 1))
        for length in range(5):
            for word in product((1, -1, 2, -2), repeat=length):
                for start in range(n):
                    output, finish = rewrite(word, n, start)
                    assert reduce((1,)*start+word) == reduce(substitute(output, images)+(1,)*finish)


def test_literal_input_and_cover_inclusion():
    d = data()
    rels, mu, lam = cover(2)
    assert [list(r) for r in rels] == d["M2_relators"]
    assert list(mu) == d["M2_meridian"] and list(lam) == d["M2_longitude"]
    images = dict(enumerate(generator_words(2), 1))
    for w6, w2 in zip(generator_words(6), d["M6_generators_in_M2"]):
        assert reduce(w6) == substitute(w2, images)
    assert abelian_diagonal(2) == [1, 5]
    assert abelian_diagonal(6) == [1, 1, 1, 1, 8, 40]


def test_longitude_normal_closure_certificate():
    assert longitude_commutator_certificate()["commutator_word"]


def test_diagram_and_rewrite_proof():
    result = diagram_certificate()
    target = tuple(data()["base_relator"])
    for step in result["longitude_rewrite_proof"]:
        a, pos, lhs, rhs = tuple(step["before"]), step["position"], tuple(step["lhs"]), tuple(step["rhs"])
        assert a[pos:pos+len(lhs)] == lhs
        assert canonical(lhs+inv(rhs)) == canonical(target)
        assert reduce(a[:pos]+rhs+a[pos+len(lhs):]) == tuple(step["after"])


def test_exact_field_and_nullspace():
    z = zeta5()
    assert sum((z**k for k in range(5)), zero(4, 4)) == zero(4, 4)
    a = fmpq_mat([[1, 2, 3], [2, 4, 6]])
    kernel = null_columns(a)
    assert kernel.ncols() == 2 and a*kernel == zero(2, 2)
    assert hs(a.transpose(), kernel).rank() == 3


def test_trivial_coefficients_on_both_covers():
    for n in (2, 6):
        assert cohom(Rep([eye(4) for _ in range(n+1)]), n) == (1, 1, 1, 2, 1)


def test_native_exact_control_not_saved_json():
    result = indexed(native_doublet(), 2)
    assert result["V"] == result["dual"] == (0, 1, 1, 2, 1)
    assert mixed_control()["V"] == (0, 1, 1, 2, 1)


def test_circle_and_torus_relative_not_conflated():
    result = mixed_control()["restriction_profile"]
    for row in result.values():
        assert row["H1"] == 1 and row["torus_kernel"] == 0
        for name in ("meridian", "longitude"):
            assert row[name+"_rank"]+row[name+"_kernel"] == row["H1"]
            assert row[name+"_kernel"] >= row["torus_kernel"]


def test_wedge_is_over_coefficient_field():
    e = parent(1)
    assert e.d == 20
    assert wedge_over_field(e.mats[0]).nrows() == 40
    a, b = e.mats[:2]
    assert wedge_over_field(a*b) == wedge_over_field(a)*wedge_over_field(b)
    assert wedge_over_field(a.inv()) == wedge_over_field(a).inv()
    assert all(m.det() == 1 for m in e.mats)


@pytest.mark.parametrize("q", [0, 1, 2, 3, 4])
def test_joint_global_transfer_and_split_comparators(q):
    result = one_twist(q)
    assert result["E"]["deck_indices"][1:] == [0, 0]
    assert len(set(result["wedge2E"]["deck_indices"])) == 1
    for coefficient in result.values():
        assert sum(coefficient["deck_indices"]) == coefficient["up"]["I"]
        a, b = coefficient["up"]["V"], coefficient["up"]["dual"]
        assert coefficient["up"]["I"] == a[0]-b[0]+b[2]-a[4]


def test_selfdual_untwisted_control():
    result = one_twist(0)
    assert result["E"]["up"]["I"] == result["wedge2E"]["up"]["I"] == 0


def test_scalar_character_relators():
    rels, mu, lam = cover(2)
    for q in range(5):
        rep = scalar_rep(q)
        assert all(rep.word(r) == eye(4) for r in rels)
        assert rep.word(mu) == rep.word(lam) == eye(4)
