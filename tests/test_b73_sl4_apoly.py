"""B73 -- SL(4) figure-eight A-variety (rank-4 B71 pipeline): Sym^3 geometric-branch validation."""
import importlib.util
import pathlib

import numpy as np

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b73_probe", _ROOT / "frontier" / "B73_sl4_apoly" / "probe.py")
b73 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b73)


def test_sym_power_lands_in_sln():
    """Sym^3 of an SL(2) matrix is in SL(4) (det 1)."""
    g = np.array([[2.0, 1.0], [1.0, 1.0]], dtype=complex)  # det 1
    M = b73.sym_power(g, 3)
    assert M.shape == (4, 4)
    assert abs(np.linalg.det(M) - 1) < 1e-9


def test_sl4_monodromy_and_meridian_commute():
    """The 32x16 Kronecker monodromy solves and the meridian mu=A^-1 t commutes with [A,B] (rank-4
    confirmation that the V46 fix is rank-independent)."""
    for xv in (3, 4, -1):
        A4, B4, _, _ = b73.sym3_branch(xv)
        mu, cdev = b73.meridian(A4, B4)
        _t, res = b73.monodromy(A4, B4)
        assert res < 1e-6
        assert cdev < 1e-6


def test_sym3_shadow_of_cooper_long():
    """eig(t4) is a 4th-root-of-unity multiple of {mu^3, mu, mu^-1, mu^-3} (the Sym^3 shadow of the
    SL(2) figure-eight monodromy) -- the rank-degree eigenvalue pattern."""
    for xv in (3, 4, 5, -1):
        res, shadow = b73.shadow_residual(xv)
        assert res < 1e-6
        assert shadow < 1e-8
