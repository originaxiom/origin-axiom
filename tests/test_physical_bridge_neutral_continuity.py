"""R52 exact finite controls; analytic proof acceptance remains separate."""
import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/neutral_continuity.py'
SPEC = importlib.util.spec_from_file_location('r52_continuity', PATH)
r = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(r)


def test_barrier_sign_slope_and_negative_controls():
    assert all(r.barrier_controls().values())


def test_strict_weighted_integrability_and_L2_counterexample():
    assert all(r.envelope_controls().values())


@pytest.mark.parametrize('degree', [0, 1, 2, 4, 8])
def test_moment_formula_independently_by_recurrence(degree):
    val = r.weighted_moment(degree, r.s.Rational(1, 8), 4)
    if degree == 0:
        assert val == 2
    else:
        assert val == 2*degree*r.weighted_moment(degree-1, r.s.Rational(1, 8), 4)


def test_undecided_margin_does_not_get_a_finite_value():
    with pytest.raises(ValueError):
        r.weighted_moment(1, r.s.symbols('unknown', real=True), 4)
    with pytest.raises(ValueError):
        r.weighted_moment(-1, 0, 4)


def test_matrix_square_root_requires_noncommuting_derivatives():
    assert all(r.matrix_controls().values())


def test_positive_isometry_transports_actual_flat_connection():
    assert all(r.transport_controls().values())


def test_literal_parent_detector_and_root_enumeration():
    assert all(r.parent_controls().values())


def test_parent_detector_is_local_not_global_reciprocal_distinction():
    q, _, _, _, _, total, _, _, _, _, _ = r.parent_character_data()
    assert r.zero(total.subs(q, 2)-total.subs(q, r.s.Rational(1, 2)))
    assert total.subs(q, 3) > total.subs(q, 2) > total.subs(q, 1)


def test_all_declared_finite_controls_not_the_global_PDE():
    groups = r.controls()
    assert sum(map(len, groups.values())) == 35
    assert all(bool(v) for group in groups.values() for v in group.values())
