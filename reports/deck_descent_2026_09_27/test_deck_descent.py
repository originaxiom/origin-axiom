import importlib.util
from pathlib import Path

import pytest
import sympy as sp

spec = importlib.util.spec_from_file_location(
    "deck_descent_exact", Path(__file__).with_name("verify_deck_descent.py"))
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


@pytest.mark.parametrize("c", [1, -2, 0])
def test_prespecified_controls(c):
    v.validate(v.data(c))


@pytest.mark.parametrize("c", [1, -2])
def test_actual_nonsplit_monodromy_is_not_removed(c):
    m, t = v.companion(c)
    n = m-sp.eye(2)
    assert n.rank() == 1 and n**2 == sp.zeros(2)
    assert t**3-sp.eye(6) == sp.diag(n, n, n)
    assert (t**3-sp.eye(6)).rank() == 3


@pytest.mark.parametrize("c", [1, -2])
def test_seam_is_the_exact_inverse_transition(c):
    _, t = v.companion(c)
    assert t**-2 == (t**3).inv()*t
    assert t*t.inv() == sp.eye(6) == t.inv()*t
    d = v.three_fibres(t)
    for j in range(18):
        e = sp.eye(18)[:, j]
        assert d*(d*(d*e)) == e


def test_projector_fixes_exactly_equivariant_fibre_data():
    _, t = v.companion(1)
    d = v.three_fibres(t)
    p = (sp.eye(18)+d+d**2)/3
    graph = sp.Matrix.vstack(sp.eye(6), t, t**2)
    assert d*graph == graph and p*graph == graph
    assert graph.rank() == p.rank() == 6


def test_wrong_seam_rejected_without_a_tolerance():
    _, t = v.companion(1)
    wrong = v.three_fibres(t, include_seam=False)
    assert wrong**3 == sp.diag(t**3, t**3, t**3)
    assert wrong**3 != sp.eye(18)


def test_circle_h1_dimensions_match_but_are_not_a_chiral_index():
    for c, base, cover in [(1, 1, 3), (-2, 1, 3), (0, 2, 6)]:
        _, t = v.companion(c)
        assert t.rows-(t-sp.eye(6)).rank() == base
        assert t.rows-(t**3-sp.eye(6)).rank() == cover
        assert len((t-sp.eye(6)).nullspace())-base == 0
        assert len((t**3-sp.eye(6)).nullspace())-cover == 0
