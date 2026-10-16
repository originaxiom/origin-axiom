"""Pre-run normal-shift locks, without a desired displacement size or sign."""
import numpy as np
import pytest

from reports.physical_bridge_2026_09_05 import quantum_shift as s
from reports.physical_bridge_2026_09_05 import quantum_vacuum as q


def mass_derivative_matches(numerical, analytic, atol):
    """Same per-entry tolerance as the original numerical assertion.

    Explicitly reject nonfinite or differently shaped results. The original
    np.testing.assert_allclose uses rtol=1e-7; np.allclose's default differs.
    """
    actual, expected = np.asarray(numerical), np.asarray(analytic)
    if actual.shape != expected.shape:
        return False
    if not (np.isfinite(actual).all() and np.isfinite(expected).all()):
        return False
    return bool(np.allclose(actual, expected, rtol=1e-7, atol=atol, equal_nan=False))


def test_full_quadratic_constraint_reconstruction_and_normal_term_control():
    result = s.primitive_checks()
    assert result["omitted_normal_term_radial_max_error"] > 1


def test_fprime_matrix_on_independent_scalar_toy():
    actual = s.fprime_matrix(np.diag([0., 2.]), 1.5, 1.)
    np.testing.assert_allclose(actual, np.diag([0., 2*(2*np.log(2)-2)]), atol=1e-12)
    with pytest.raises(ValueError):
        s.fprime_matrix(np.diag([1., -.01]), 1.5, 1.)


def test_vector_and_complex_Weyl_mass_derivatives():
    geo = q.geometry()
    z = s.vacuum_coordinates()
    rng = np.random.default_rng(2640)
    direction = rng.normal(size=186)
    direction /= np.linalg.norm(direction)
    eps = 1e-4
    go, dg = s.orbit(z), s.orbit(direction)
    analytic = dg.T@geo["ks"]@go+go.T@geo["ks"]@dg
    def vm(point):
        g = s.orbit(point)
        return g.T@geo["ks"]@g
    assert mass_derivative_matches(
        (vm(z+eps*direction)-vm(z-eps*direction))/(2*eps), analytic, 1e-10)
    mf, dm = s.fermion_mass(z, .25), s.fermion_mass(direction, .25)
    analytic = dm.conj().T@mf+mf.conj().T@dm
    def fm(point):
        m = s.fermion_mass(point, .25)
        return m.conj().T@m
    assert mass_derivative_matches(
        (fm(z+eps*direction)-fm(z-eps*direction))/(2*eps), analytic, 1e-11)


def test_mass_derivative_predicate_has_positive_and_rejecting_controls():
    expected = np.array([[1., 2j], [-2j, 3.]], dtype=complex)
    assert mass_derivative_matches(expected.copy(), expected, 1e-11)
    changed = expected.copy()
    changed[0, 1] += 1e-3
    assert not mass_derivative_matches(changed, expected, 1e-11)
    changed[0, 1] = np.nan
    assert not mass_derivative_matches(changed, expected, 1e-11)
    changed[0, 1] = np.inf
    assert not mass_derivative_matches(changed, expected, 1e-11)
    assert not mass_derivative_matches(expected[:1], expected, 1e-11)


def test_full_kernel_force_stationarity_and_shifted_SM_action():
    result = s.solve_shift()
    assert result["kernel_gradient_max_abs"] < 1e-9
    assert result["first_order_stationarity_max_abs"] < 1e-9
    assert result["SM_singlet_dimensions"] == {"real": 13, "gauge": 4, "physical_normal": 9}
    assert result["shifted_unbroken_dimension_at_tolerance_1e-8"] == 12


def test_weak_coupling_scaling_and_constrained_curvature_identity():
    a = s.solve_shift()
    b = s.solve_shift(.05, .25, .125, .5)
    np.testing.assert_allclose(b["coordinate_displacement"], np.array(a["coordinate_displacement"])/4, atol=1e-10)
    for values in a["angular_shift_identity"].values():
        assert abs(values["normal_shift_tree_mass_correction"]-values["curved_path_gradient_term"]) < 1e-9
