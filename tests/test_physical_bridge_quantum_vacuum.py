"""Pre-run R5 locks; no desired vacuum selection is asserted."""
import numpy as np
import pytest

from reports.physical_bridge_2026_09_05 import quantum_vacuum as q


def test_complete_kinetically_normalized_spectrum_and_controls():
    checks = q.primitive_checks()
    assert checks["scalar_positive"] == 109
    assert checks["vector_massive"] == 66
    assert checks["generalized_mass_and_direct_kinetic_checks"]


def test_bad_kinetic_and_tachyonic_mass_are_not_hidden():
    with pytest.raises(ValueError):
        q.invsqrt_positive(np.diag([1., -1.]))
    with pytest.raises(ValueError):
        q.psd_eigenvalues(np.diag([1., -.001]))
    with pytest.raises(ValueError):
        q.log_sum([-.01], 1.5)
    assert q.log_sum([0., 0.], 1.5) == 0
    assert np.isfinite(q.log_sum([1e-18], 1.5))


def test_named_points_and_scale_control():
    points = q.named_backgrounds()
    spectra = {k: q.spectra(a) for k, a in points.items()}
    assert np.count_nonzero(spectra["SM_Y"][1] < 1e-8) == 12
    assert np.count_nonzero(spectra["SU4_U1"][1] < 1e-8) == 16
    assert np.count_nonzero(spectra["old_generic_competitor"][1] < 1e-8) == 4
    fourths = [[s@s, v@v] for s, v in spectra.values()]
    np.testing.assert_allclose(fourths, np.tile(fourths[0], (3, 1)), atol=2e-8)
    for candidate in ["SU4_U1", "old_generic_competitor"]:
        diffs = [np.sum(q.potential_parts(*spectra[candidate], .2, .5, mu)
                        -q.potential_parts(*spectra["SM_Y"], .2, .5, mu)) for mu in [.5, 1, 2]]
        assert max(diffs)-min(diffs) < 1e-9


def test_sphere_parametrization_and_non_cartan_gauge_equivalence():
    geo = q.geometry()
    a = q.cartan_background([1, 2, -3, 4])
    np.testing.assert_allclose(q.cartan_background(q.sphere_coordinates(a)), a, atol=1e-12)
    # A genuine compact SU5 rotation preserves S,N; this tests off-diagonal
    # background masses, not only a permutation of eigenvalue labels.
    from scipy.linalg import expm
    from reports.physical_bridge_2026_09_05 import vacuum as v
    root = v.representation()[2][tuple(v.CARTAN[:, 2])]
    u = expm(.37*np.array(root-root.T, complex))
    rotated = u@a@u.conj().T
    assert not np.allclose(rotated, a)
    for old, new in zip(q.spectra(a), q.spectra(rotated)):
        np.testing.assert_allclose(new, old, atol=1e-10)
    np.testing.assert_allclose(u@geo["s"], geo["s"], atol=1e-12)


def test_light_curvature_step_convergence_without_assuming_its_sign():
    geo = q.geometry()
    for i in [2, 5]:
        c1 = q.curvature_components(geo["y"], geo["T"][i].copy(), .01)
        c2 = q.curvature_components(geo["y"], geo["T"][i].copy(), .005)
        c3 = q.curvature_components(geo["y"], geo["T"][i].copy(), .0025)
        assert np.max(np.abs(c3-c2)) < np.max(np.abs(c2-c1))
        assert np.max(np.abs(c3-c2)) < 1e-4
        assert abs(c3[1]) < 1e-8


def test_fermion_angular_cancellation_and_coupling_scaling():
    points = q.named_backgrounds()
    center = q.spectra(points["SM_Y"])
    other = q.spectra(points["old_generic_competitor"])
    unit = q.potential_parts(*other)-q.potential_parts(*center)
    scaled = q.potential_parts(*other, .2, .5)-q.potential_parts(*center, .2, .5)
    assert scaled[1] == unit[1] == 0
    np.testing.assert_allclose(scaled, unit*np.array([.2**2, 1, .5**4]), atol=1e-10)
