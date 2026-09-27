"""R53 finite identities, not a global PDE certification."""
import importlib.util
from pathlib import Path
import pytest

PATH = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/neutral_velocity.py'
SPEC = importlib.util.spec_from_file_location('r53_velocity', PATH)
r = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(r)


def test_local_jacobi_and_moment_cancellations():
    assert all(r.jacobi_controls().values())


def test_metric_and_compact_projection_are_distinct_steps():
    assert all(r.projection_controls().values())


def test_rate_preserving_rescaling_and_integrability():
    assert all(r.scaling_controls().values())


@pytest.mark.parametrize('B', [0, 1, 2, 100, 10000])
def test_small_ball_coefficients_have_uniform_bounds(B):
    s = r.s
    rho = (1+s.Integer(B))**-4
    for exponent in (1, s.Rational(3, 2), 2, s.Rational(5, 2)):
        assert 0 <= rho**exponent*B <= 1


def test_actual_parent_detector_and_kinetic_normalization():
    assert all(r.kinetic_controls().values())


def test_zero_kernel_assumption_cannot_be_dropped():
    s = r.s
    J = s.diag(1, 0)
    t = s.symbols('t', positive=True)
    xi = s.Matrix([t, s.sqrt(t)])
    assert J*xi == s.Matrix([t, 0])
    assert s.limit(xi[1]/t, t, 0, dir='+') == s.oo


def test_finite_count_and_predicates():
    groups = r.controls()
    assert sum(map(len, groups.values())) == 34
    assert all(bool(x) for group in groups.values() for x in group.values())
