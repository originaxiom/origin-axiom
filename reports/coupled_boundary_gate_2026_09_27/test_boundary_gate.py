"""Tests sealed before import; all arithmetic is exact."""
import pytest
import sympy as s

from verify_boundary_gate import (
    boundary_models, cubic_fixed, dual, fixed, index_interval, inputs,
    jordan_wedge_count, mixed, unipotent, universal_interval, wedge2,
)


@pytest.mark.parametrize("partition,expected", [
    ([5], 2), ([4, 1], 3), ([3, 2], 4), ([3, 1, 1], 4),
    ([2, 2, 1], 6), ([2, 1, 1, 1], 7), ([1, 1, 1, 1, 1], 10),
])
def test_jordan_formula_independent_of_minor_rank(partition, expected):
    u = unipotent(partition)
    assert fixed(u) == len(partition)
    assert fixed(wedge2(u)) == jordan_wedge_count(partition) == expected
    assert fixed(dual(wedge2(u))) == expected
    assert (len(partition), expected) != (3, 3)


def test_cover_cube_and_wedge_functor():
    down, up, w = boundary_models()
    assert down**3 == up
    assert wedge2(down)**3 == wedge2(up)
    assert wedge2(down * w) == wedge2(down) * wedge2(w)
    assert wedge2(dual(down)) == dual(wedge2(down))
    assert down.det() == up.det() == w.det() == 1


@pytest.mark.parametrize("which,expected", [(0, (2, 3, 1)), (1, (4, 7, 3))])
def test_true_coefficients_not_mixed_six(which, expected):
    down, up, w = boundary_models()
    u = [down, up][which]
    for a, b, count in zip([u, wedge2(u), mixed(u)], [w, wedge2(w), mixed(w)], expected):
        assert fixed(a) == fixed(a, b) == fixed(dual(a), dual(b)) == count
    assert expected[0] != expected[2] and expected[1] != expected[2]


def test_longitude_can_reduce_meridian_bound():
    down, up, _ = boundary_models()
    w = s.diag(-1, -1, 1, 1, 1)
    assert w.det() == 1
    for u in [down, up]:
        assert u*w == w*u
        assert fixed(u, w) < fixed(u)
        assert fixed(wedge2(u), wedge2(w)) < fixed(wedge2(u))


def test_common_invariants_need_not_equal_dual():
    u, w = s.eye(3), s.eye(3)
    u[0, 1], w[0, 2] = 1, 1
    assert u*w == w*u and u.det() == w.det() == 1
    assert fixed(u, w) == 1
    assert fixed(dual(u), dual(w)) == 2


def test_full_global_H0_terms_change_bound():
    # Dimension algebra only, not a claimed topological realization.
    assert index_interval(2, 2, 0, 0) == (-2, 2)
    assert index_interval(2, 2, 1, 0) == (-1, 3)
    assert index_interval(2, 2, 0, 1) == (-3, 1)
    assert universal_interval(2, 2) == (-4, 4)


def test_principal_excluded_even_without_balance():
    assert universal_interval(1, 1) == (-2, 2)
    u = unipotent([5])
    assert [cubic_fixed(u, k) for k in range(3)] == [1, 0, 0]
    assert fixed(2*u) == 0
    assert fixed(dual(2*u)) == 0


def test_cover_room_is_not_realization():
    assert index_interval(4, 4, 0, 0) == (-4, 4)
    assert universal_interval(4, 4) == (-8, 8)
    assert universal_interval(0, 0) == (0, 0)


def test_exact_cubic_twists():
    down, up, _ = boundary_models()
    assert [cubic_fixed(down, k) for k in range(3)] == [2, 1, 1]
    assert [cubic_fixed(wedge2(down), k) for k in range(3)] == [3, 2, 2]
    assert [cubic_fixed(up, k) for k in range(3)] == [4, 0, 0]
    assert [cubic_fixed(wedge2(up), k) for k in range(3)] == [7, 0, 0]
    for k in range(3):
        assert cubic_fixed(down, k) == cubic_fixed(dual(down), -k)


def test_one_hypercharge_line_and_cubic_pullback():
    down, up, _ = boundary_models()
    q = inputs()["hypercharge_exponents"]
    assert q == {"Q": 1, "u": -4, "e": 6, "d": 2, "L": -3}
    for phase in [1, 2]:
        assert cubic_fixed(up, phase*q["Q"]) == 0
        # A nontrivial DOWNSTAIRS phase pulls back to a trivial upstairs one.
        assert cubic_fixed(up, 3*phase*q["Q"]) == 4
        assert cubic_fixed(down, phase*q["Q"]) == 1
        assert cubic_fixed(down, phase*q["e"]) == 2
