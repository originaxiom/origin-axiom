"""R26 mathematical controls; finite models are not physical PDE certificates."""
import importlib.util
from pathlib import Path

import pytest
import sympy as sp

SPEC = importlib.util.spec_from_file_location('r26_test', Path(__file__).resolve().parents[1]/
                                            'reports/physical_bridge_2026_09_05/index_stability.py')
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)


def test_actual_metric_adjoint_gives_the_declared_zero_order_perturbation():
    r = m.perturbation_symbol()
    assert r['actual_map'] and m.simplify_matrix(r['operator']-r['expected']) == sp.zeros(8)
    assert r['hermitian'] and r['odd']


def test_scalar_connection_and_real_mass_have_the_exact_pointwise_norm():
    r = m.perturbation_symbol()
    assert r['scalar_norm']
    assert m.simplify_matrix(r['square']-r['norm_square']*sp.eye(8)) == sp.zeros(8)


def test_wrong_adjoint_and_grading_even_shift_are_rejected():
    r = m.perturbation_symbol()
    assert r['wrong_adjoint_rejected'] and r['wrong_adjoint_not_hermitian']
    assert r['even_scalar_not_odd']


def test_compact_patch_connection_is_genuinely_curved():
    r = m.curvature_witness()
    epsilon, q = sp.symbols('epsilon q', real=True)
    assert r['nonflat'] and r['centre_curvature'][(0, 1)] == epsilon/sp.E
    assert r['centre_square'] == -sp.I*q*epsilon/sp.E
    assert r['zero_form_square_nonzero']
    assert r['zero_amplitude_flat']


def test_curved_covariant_square_is_curvature_on_every_form_degree():
    r = m.curvature_witness()
    assert len(r['square_rows']) == 8
    assert all(x['identity'] for x in r['square_rows'])


@pytest.mark.parametrize('k', [0, 1, 3, 5])
def test_rank_one_model_preserves_index_but_can_add_a_pair(k):
    for n in (1, 2, 4):
        for t in (-2, 0, sp.Rational(1, 2), 1, sp.Rational(3, 2)):
            r = m.channel(k, n, t)
            assert r['computed_index'] == k
            assert r['hermitian'] and r['odd']
            assert (r['odd_kernel'], r['even_kernel']) == ((k+1, 1) if t == 1 else (k, 0))
            if r['small_norm']:
                assert r['even_kernel'] == 0 and r['odd_kernel'] == k


def test_channel_inputs_do_not_silently_change_the_comparison_class():
    for args in ((-1, 2, 0), (1, 0, 0), (1, 1, .5), (1, 1, sp.I)):
        with pytest.raises(ValueError):
            m.channel(*args)
    with pytest.raises(ValueError):
        m.channel(1, 1, 0, 0)


def test_resolvent_factorization_and_identity_use_the_correct_order():
    r = m.resolvent_controls()
    assert r['factorization'] and r['inverse_difference']
    assert r['wrong_order_rejected']


def test_noncompact_resolvent_model_retains_an_infinite_nonescaping_tail():
    for d in (1, 2, 3):
        r = m.tail_controls(d)
        assert r['orthonormal'] and r['both_eigenvectors']
        assert r['distance_formula']
        assert r['resolvent_distance_squared'] == sp.Rational(2, d*d+1)
        assert [v['full_kernel'] for v in r['tail_kill']] == [5, 7, 11, 19]


def test_original_flat_pair_free_and_paired_cases_are_distinguished():
    rows = m.initial_kernel_controls()
    assert [(r['odd'], r['even']) for r in rows] == [(3, 0), (4, 1), (4, 1)]
    assert all(r['index'] == 3 and r['euler'] == -3 for r in rows)
