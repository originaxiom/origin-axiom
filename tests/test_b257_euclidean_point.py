"""B257 locks -- the Euclidean transition point: the discriminant branch point (hyperbolic complex / spherical real
branches collide at u=-2), the order-3 Eisenstein meridian, complex volume = 0. FIREWALLED (geometry/arithmetic,
not physics); nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B257_euclidean_point" / "euclidean_point.py"
_spec = importlib.util.spec_from_file_location("b257", _PATH)
b257 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b257)


def test_euclidean_is_the_branch_point():
    # hyperbolic (x>1) complex branches, spherical (x<1) real branches, collide at x=1 (u=-2 double)
    assert b257.branch_nature(1.5) == "hyperbolic"
    assert b257.branch_nature(0.5) == "spherical"
    assert b257.branch_nature(1.0) == "euclidean"
    roots, disc = b257.char_variety_roots(1.0)
    assert abs(disc) < 1e-12
    assert all(abs(u - (-2)) < 1e-12 for u in roots)      # double root u = -2


def test_meridian_is_order_3():
    assert b257.meridian_psl_order_at_euclidean() == 3    # the Z/3 cone (zeta_6 -> omega)


def test_complex_volume_vanishes():
    assert b257.VOL_EUCLIDEAN == 0.0 and b257.CS_EUCLIDEAN == 0.0


def test_cusp_shape_is_2sqrt_minus3_rectangular():
    # 2 sqrt(-3) = 2 sqrt3 i ; in Q(sqrt-3) but purely imaginary (rectangular, not hexagonal)
    assert abs(b257.CUSP_SHAPE.real) < 1e-9
    assert abs(b257.CUSP_SHAPE.imag - 2 * (3 ** 0.5)) < 1e-6
