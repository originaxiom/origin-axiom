"""B250 locks -- the complex-volume profile of the E6<->E8 geometric transition: hyperbolic Vol=6*Lambda(pi/3)
(=2.0299, the '-3' tetra), Euclidean 0, spherical Vol=pi^2/5 (=1.9739, the '5'=det(4_1)), lens CS denominator 5.
FIREWALLED (geometry/McKay, not physics); nothing to CLAIMS.md."""
import importlib.util
import pathlib
import mpmath as mp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B250_volume_profile" / "volume_profile.py"
_spec = importlib.util.spec_from_file_location("b250", _PATH)
b250 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b250)


def test_hyperbolic_end_matches_snappy():
    # E6 end: Vol(4_1) = 6 Lambda(pi/3) = 2.02988321281931 (SnapPy)
    assert abs(b250.hyperbolic_volume() - mp.mpf("2.02988321281931")) < mp.mpf(10) ** -10


def test_spherical_end_is_pi2_over_5():
    # E8 end: Vol(spherical Z/2 orbifold) = pi^2/5 (det(4_1)=5 in the denominator)
    assert b250.spherical_volume() == mp.pi ** 2 / 5
    assert abs(b250.spherical_volume() - mp.mpf("1.9739208802")) < mp.mpf(10) ** -8


def test_lens_cs_denominator_is_the_determinant():
    # flat-connection CS of L(5,2) lives in (1/5)Z/Z -> denominator = det(4_1) = 5
    assert b250.lens_cs_numerators() == [0, 2, 3]


def test_two_ends_comparable_different_geometries():
    # the hyperbolic and spherical end volumes are comparable (2.030 vs 1.974) but opposite curvature
    vh, vs = b250.hyperbolic_volume(), b250.spherical_volume()
    assert abs(vh - vs) < mp.mpf("0.06")
    assert vh > vs > 0
