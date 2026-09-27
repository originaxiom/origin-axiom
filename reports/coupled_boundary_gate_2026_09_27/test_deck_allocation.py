import sympy as s

from verify_boundary_gate import boundary_models, dual, fixed, inputs, wedge2
from verify_deck_allocation import allocations, transfer_comparator, twisted_pair_fixed


def test_three_necessary_fundamental_distributions():
    expected = {(1, 1, 1), (2, 0, 1), (2, 1, 0)}
    assert set(allocations((2, 1, 1), 3)) == expected
    assert set(allocations((2, 1, 1), -3)) == {tuple(-v for v in x) for x in expected}
    assert (3, 0, 0) not in expected
    assert allocations((2, 1, 1), 5) == []


def test_galois_extra_condition_not_silently_assumed():
    assert allocations((2, 1, 1), 3, True) == [(1, 1, 1)]
    assert allocations((2, 1, 1), -3, True) == [(-1, -1, -1)]
    assert (2, 0, 1) in allocations((2, 1, 1), 3, False)


def test_exterior_target_not_forced_by_fundamental():
    rows = allocations((3, 2, 2), 3)
    assert (1, 1, 1) in rows and (3, 0, 0) in rows
    # These are allowable dimension data, not global cohomology examples.
    assert len(rows) > len(allocations((2, 1, 1), 3))


def test_fundamental_transfer():
    u, _, w = boundary_models()
    r = transfer_comparator(u, w)
    assert r["twisted_pair_fixed"] == [2, 1, 1]
    assert r["pushforward_pair_fixed"] == r["upstairs_pair_fixed"] == 4
    assert r["invariant_pair_fixed"] == 2


def test_exterior_transfer():
    u, _, w = boundary_models()
    r = transfer_comparator(wedge2(u), wedge2(w))
    assert r["twisted_pair_fixed"] == [3, 2, 2]
    assert r["pushforward_pair_fixed"] == r["upstairs_pair_fixed"] == 7
    assert r["invariant_pair_fixed"] == 3


def test_deck_is_not_internal_transport():
    u, _, w = boundary_models()
    r = transfer_comparator(u, w)
    assert r["deck_order_three"]
    assert not r["holonomy_cube_is_identity"]
    p = s.Matrix(inputs()["permutation"])
    d = s.kronecker_product(p, s.eye(5))
    projector = (s.eye(15) + d + d*d) / 3
    assert projector*projector == projector and projector.rank() == 5
    # The projector's fiber rank is not the boundary-cohomology dimension.
    assert projector.rank() != r["invariant_pair_fixed"]


def test_inverse_character_in_dual():
    u, _, w = boundary_models()
    for k in range(3):
        assert twisted_pair_fixed(u, w, k) == twisted_pair_fixed(dual(u), dual(w), -k)


def test_longitude_can_remove_nontrivial_twist_sectors():
    u, _, _ = boundary_models()
    w = s.diag(1, 1, s.Matrix(inputs()["permutation"]))
    assert w.det() == 1 and u*w == w*u
    assert [twisted_pair_fixed(u, w, k) for k in range(3)] == [2, 0, 0]
    assert fixed(u**3, w) == 2


def test_odd_alternating_map_countercontrol():
    a = s.zeros(5)
    a[0, 1], a[1, 0], a[2, 3], a[3, 2] = 1, -1, 1, -1
    assert a.T == -a and a.det() == 0 and a.rank() == 4
    # Even dimension does admit an invertible alternating matrix.
    b = a[:4, :4]
    assert b.T == -b and b.det() == 1
