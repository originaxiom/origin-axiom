"""R50 finite controls; no claim to machine-certify the global analytic proof."""
import importlib.util
from pathlib import Path

import pytest
import sympy as s

PATH = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/neutral_second_order.py'
SPEC = importlib.util.spec_from_file_location('r50_neutral_second_order', PATH)
r = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(r)


def test_actual_end_twojet_including_radial_derivative():
    assert all(r.tail_controls().values())


def test_free_graded_transport_not_commuting_matrix_proxy():
    assert r.formal_flat_residual() == {}
    assert r.differential({('c', 'sigma'): r.F(1)}) == {('c', 'p'): r.F(-1)}


@pytest.mark.parametrize('change', [dict(commutator_sign=-1), dict(half=0), dict(include_c2=False)])
def test_transport_mutants_are_detected(change):
    assert r.formal_flat_residual(**change)


def test_graded_differential_squares_to_zero():
    for word in [('c2',), ('sigma', 'c2'), ('c2', 'sigma'), ('sigma', 'c', 'sigma')]:
        assert not r.differential(r.differential({word: r.F(1)}))


def test_hilbert_green_and_independent_least_squares():
    assert all(r.hilbert_controls().values())


def test_exact_correction_with_actual_nonidentity_grams():
    beta, r2, r0, norm = r.relax(s.Matrix([7, 0, 0]), s.Matrix([3, 0]))
    assert beta == s.Matrix([s.Rational(6, 5), -s.Rational(7, 2), 0, 0])
    assert r2 == s.zeros(3, 1) and r0 == s.zeros(2, 1) and norm == 0


@pytest.mark.parametrize('j2,j0,expected', [([7, 0, 5], [3, 0], 575),
                                         ([7, 0, 0], [3, 5], 75),
                                         ([0, 1, 0], [0, 0], 19)])
def test_curvature_zeroform_and_nonclosed_obstructions(j2, j0, expected):
    assert r.relax(s.Matrix(j2), s.Matrix(j0))[3] == expected


def test_quartic_cannot_kill_a_relaxed_direction():
    assert all(r.polynomial_controls().values())


def test_strict_weight_margins_and_endpoint_control():
    assert all(r.weight_controls().values())


def test_all_predicates_are_true_but_not_a_global_certificate():
    groups = r.controls()
    assert sum(len(group) for group in groups.values()) == 39
    assert all(bool(value) for group in groups.values() for value in group.values())
