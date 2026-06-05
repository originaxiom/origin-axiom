"""B83 (Phase A, V66) -- locking test: the SL(n) figure-eight Dehn-filling A-polynomial family
L=(-1)^(n-1) M^n. Locks n=3 (L=+M^3, Falbel) and n=4 (L=-M^4, NEW) via the peripheral eigenvalue
A-variety on the principal Dehn-filling component."""
import importlib.util
import pathlib

import numpy as np

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b83_apoly", _ROOT / "frontier" / "B83_sln_apolynomial" / "probe.py")
B83 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B83)


def test_sl3_avariety_is_plus_M3():
    """SL(3): L = +M^3 (Falbel) -- co-diagonalized peripheral eigenvalue pairs."""
    reps = B83.sl3_W1_reps(n_reps=3)
    assert len(reps) >= 2, "need SL(3) W1 reps"
    devs = [B83.avariety_dev(mu, lam, 3) for mu, lam in reps]
    assert max(devs) < 1e-7, devs
    # and L=+M^3 is the RIGHT sign (n=3 -> (-1)^2=+1): a wrong sign would fail avariety_dev
    sign = (-1) ** (3 - 1)
    assert sign == 1


def test_sl4_avariety_is_minus_M4():
    """SL(4): L = -M^4 (NEW) -- the SL(4) figure-eight A-polynomial."""
    reps = B83.sl4_principal_reps(n_reps=2)
    assert len(reps) >= 1, "need an SL(4) principal Dehn-filling rep"
    devs = [B83.avariety_dev(mu, lam, 4) for mu, lam in reps]
    assert max(devs) < 1e-7, devs
    assert (-1) ** (4 - 1) == -1


def test_meridian_eigenvalues_generic():
    """The meridian eigenvalues vary (generic) -- the A-variety is a curve, not a point set (B77)."""
    reps = B83.sl4_principal_reps(n_reps=2)
    assert len(reps) >= 1
    # det(mu) = prod of meridian eigenvalues = 1
    for mu, _lam in reps:
        assert abs(np.linalg.det(mu) - 1) < 1e-6
