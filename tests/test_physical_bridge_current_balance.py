"""R41 matrix facts; global cutoff statements are not certified by finite tests."""
import importlib.util
from pathlib import Path

import pytest
import sympy as s

PATH = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/current_balance.py'
spec = importlib.util.spec_from_file_location('r41_current', PATH)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


@pytest.mark.parametrize('k', [1, 2, 3])
def test_all_flag_contractions_with_arbitrary_complex_diagonals(k):
    c, norms = m.upper(4)
    xi = m.flag(4, k)
    cross = m.cross_norm(norms, 4, k)
    assert m.clean(m.contraction(c, xi)+2*cross) == 0
    assert s.trace(xi) == 0
    assert s.trace(xi*xi) == 4*k*(4-k)
    assert cross != 0


@pytest.mark.parametrize('k', [1, 2, 3])
def test_split_and_nonsplit_pointwise_controls(k):
    xi = m.flag(4, k)
    diagonal = s.diag(1+s.I, 2-s.I, 3, -6)
    eta = m.elementary(4, k-1, k)
    assert m.contraction(diagonal, xi) == 0
    assert m.contraction(diagonal+eta, xi) == -2
    # The wrong overall sign must not satisfy the identity.
    assert m.contraction(diagonal+eta, xi)-2 != 0


def test_all_flag_source_gram_not_only_first_line():
    _, _, xis, _, _, _ = m.parent_directions()
    actual = s.Matrix(3, 3, lambda i, j: s.trace(xis[i]*xis[j]))
    assert actual == s.Matrix([[12, 8, 4], [8, 16, 8], [4, 8, 12]])
    assert actual.is_positive_definite


def test_scalar_on_four_source_and_both_noncentral_signs():
    t, u, xis, _, _, _ = m.parent_directions()
    assert [s.trace(xi*t) for xi in xis] == [0, 0, 0]
    assert s.trace(t*t) == 20
    assert [s.trace(xi*u) for xi in xis] == [12, 8, 4]
    assert [s.trace(xi*(-u)) for xi in xis] == [-12, -8, -4]


def test_neutral_parent_directions_have_a_noncentral_current():
    t, u, _, neutral, _, _ = m.parent_directions()
    assert sum((m.moment_commutator(k) for k in neutral), s.zeros(5)) == u
    assert all(t*k == k*t for k in neutral)
    assert u != t and s.trace(u*t) == 0


def test_charged_direction_has_both_flag_and_T_projection():
    t, _, xis, _, n, _ = m.parent_directions()
    assert t*n-n*t == 5*n
    mu = m.moment_commutator(n)
    assert mu == s.diag(1, 0, 0, 0, -1)
    assert [s.trace(xi*mu) for xi in xis] == [3, 2, 1]
    assert s.trace(t*mu) == 5
    assert m.moment_commutator(n.H) == -mu


def test_upper_and_lower_maps_have_different_invariant_subbundles():
    _, _, _, _, n, lower = m.parent_directions()
    pv = s.diag(1, 1, 1, 1, 0)
    assert (s.eye(5)-pv)*n*pv == s.zeros(5)
    assert (s.eye(5)-pv)*lower*pv != s.zeros(5)


def test_whole_rank_projector_blocks_the_triangular_shortcut():
    c, norms = m.upper(5)
    xi = m.flag(5, 4)
    norm = sum(norms[j, 4] for j in range(4))
    assert m.clean(m.contraction(c, xi)+s.Rational(5, 2)*norm) == 0
    assert m.contraction(m.elementary(5, 0, 4), xi) == -s.Rational(5, 2)
    assert m.contraction(s.eye(5), xi) == 0


def test_reused_counts_are_the_fixed_actual_coefficient_not_a_new_spectrum():
    # Explicitly a fixed-result reuse/custody check, not an independent cochain engine.
    counts = m.reused_counts()
    assert counts == {'V': (1, 0), 'W': (1, 0), 'wedgeW': (2, 1)}
    assert all(a-b == 1 for a, b in counts.values())


def test_every_cross_block_has_the_required_positive_norm_bound():
    c, norms = m.upper(4)
    _, psi = m.split(c)
    for k in range(1, 4):
        margin = m.clean(2*s.trace(psi.H*psi)-m.cross_norm(norms, 4, k))
        assert m.nonnegative_even_polynomial(margin)


def test_positive_coefficients_alone_do_not_certify_a_norm_bound():
    x, y = s.symbols('x y', real=True)
    assert m.nonnegative_even_polynomial(x*x+2*y*y)
    assert m.nonnegative_even_polynomial(s.Integer(0))
    assert not m.nonnegative_even_polynomial(-x*x+y*y)
    assert not m.nonnegative_even_polynomial(x*y)
    assert (x*y).subs({x: -1, y: 1}) < 0


def test_proper_flag_validation():
    for invalid in (0, 4, 5):
        with pytest.raises(ValueError):
            m.flag(4, invalid)
