"""Post-failure exact-expression comparison repair; producer and proof unchanged."""
import importlib.util
from pathlib import Path
import pytest
import sympy as s

spec = importlib.util.spec_from_file_location('f07_original_tests', Path(__file__).with_name('test_verify.py'))
original = importlib.util.module_from_spec(spec)
spec.loader.exec_module(original)
m = original.m

UNCHANGED = (
    'test_reference_complex_and_contraction_are_nonvacuous',
    'test_nondiagonal_complex_metric_has_exact_equivalence_constants',
    'test_same_homotopy_remains_bounded_and_gap_bound_holds',
    'test_new_orthogonality_not_old_orthogonality_controls_the_proof',
    'test_metric_family_saturates_the_bound_without_a_finite_zero',
    'test_bounded_nonunitary_chain_map_is_not_fixed_norm_dirac_conjugacy',
    'test_changing_the_differential_can_create_zeros_without_a_chain_isomorphism',
    'test_nonflat_differential_is_outside_the_comparison',
    'test_circle_holonomy_control_changes_the_entire_two_degree_kernel',
    'test_nonperiodic_circle_gauge_cannot_be_used_as_a_bounded_global_chain_map',
    'test_unbounded_end_gauge_preserves_ordinary_flatness_but_not_L2_kernel',
    'test_degreewise_metric_scaling_is_not_only_the_fiber_metric',
)


@pytest.mark.parametrize('name', UNCHANGED)
def test_unchanged_original_assertions(name):
    getattr(original, name)()


@pytest.mark.parametrize('degree', [0, 1, 2, 3])
def test_unchanged_original_degree_assertions(degree):
    original.test_form_norm_comparison_includes_volume_and_degree(degree)


def test_exact_adjoint_comparison_and_all_unreached_original_assertions():
    d, g = m.acyclic_complex(), m.metric()
    star = m.adjoint(d, g)
    assert (g*star-d.H*g).applyfunc(s.expand) == s.zeros(4)
    assert star != d.H
    lap = m.laplacian(d, g)
    assert (g*lap-lap.H*g).applyfunc(s.expand) == s.zeros(4)
    assert lap != s.eye(4)
    lam = s.symbols('lambda')
    expected = (lam-s.Rational(2, 9))**2*(lam-s.Rational(1, 8))**2
    assert s.factor(lap.charpoly(lam).as_expr()-expected) == 0
    assert lap.det() != 0
    names = {name for name in vars(original) if name.startswith('test_')}
    assert names == set(UNCHANGED) | {
        'test_form_norm_comparison_includes_volume_and_degree',
        'test_new_adjoint_and_laplacian_use_the_new_metric',
    }


def test_exact_cancellation_does_not_hide_a_genuinely_wrong_adjoint():
    entry = (-s.Rational(1, 16)-s.I/16)*(1-s.I)+s.Rational(1, 8)
    assert s.expand(entry) == 0
    d, g = m.acyclic_complex(), m.metric()
    wrong = m.adjoint(d, g)
    wrong[0, 0] += 1
    residual = (g*wrong-d.H*g).applyfunc(s.expand)
    assert residual == s.diag(9, 0, 0, 0)
    assert residual != s.zeros(4)
