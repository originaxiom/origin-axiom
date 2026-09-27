from itertools import permutations

from flint import fmpq_mat

from verify_finite_seed import (
    augmentation, compose, doubly_transitive, even, generated_group, inputs,
    inverse, symmetric_tracefree_action, word_value,
)
from verify_global_seed import DEGREE, Rep, eye, kron
from verify_topology import cover


def test_finite_group_domain():
    elements = [p for p in permutations(range(6)) if even(p)]
    assert len(elements) == 360
    identity = tuple(range(6))
    for p in elements:
        assert compose(p, inverse(p)) == identity


def test_irreducibility_control_not_presumed_to_satisfy_group_relators():
    gens = [tuple(p) for p in inputs()["irreducibility_comparator"]]
    group = generated_group(gens)
    assert len(group) == 360 and doubly_transitive(group)
    rels, _, _ = cover(2)
    assert any(word_value(r, gens) != tuple(range(6)) for r in rels)


def test_abelian_actual_representation_fails_irreducibility():
    identity = tuple(range(6))
    rels, _, _ = cover(2)
    for t in inputs()["meridians"].values():
        gens = [tuple(t), identity, tuple(t)]
        assert all(word_value(r, gens) == identity for r in rels)
        assert not doubly_transitive(generated_group(gens))


def test_augmentation_functor_and_positive_form():
    gens = [tuple(p) for p in inputs()["irreducibility_comparator"]]
    q = eye(5)+fmpq_mat([[1]*5 for _ in range(5)])
    assert q.det() == 6
    for a in gens:
        g = augmentation(a)
        assert g.det() == 1 and g.transpose()*q*g == q
        for b in gens:
            assert augmentation(compose(a, b)) == g*augmentation(b)


def test_symmetric_module_dimension_and_functor():
    a, b = [augmentation(tuple(p)) for p in inputs()["irreducibility_comparator"][:2]]
    x, y, xy = symmetric_tracefree_action([a, b, a*b])
    assert x.nrows() == x.ncols() == 14
    assert x*y == xy


def test_changed_meridian_classes_are_explicit():
    for name, t in inputs()["meridians"].items():
        m = augmentation(tuple(t))
        assert m**3 == eye(5)
        fixed = 5-(m-eye(5)).rank()
        assert fixed == (3 if name == "single_three_cycle" else 1)
        # They are NOT the earlier nontrivial-unipotent meridian on M6.
        assert m**3-eye(5) == fmpq_mat(5, 5)
