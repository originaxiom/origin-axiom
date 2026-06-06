"""B97 -- locking tests: the Lorentzian (2,1) form lives on the SL(2,R)/Teichmuller side (the so(2,1)
gauge algebra) and not the Euclidean su(2) side; the fiber has an explicit SL(2,R) Fuchsian rep; and the
holonomy preserves the (2,1) Minkowski form (SO(2,1) local Lorentz)."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b97", _ROOT / "frontier" / "B97_sl2r_lorentzian" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_gauge_algebra_signatures():
    """sl(2,R)=so(2,1) trace form is Lorentzian (2,1); su(2)=so(3) is Euclidean (0,3)."""
    sR, su = B.gauge_signatures()
    assert sR == (2, 1)                            # 2+1 Minkowski (Lorentzian)
    assert su == (0, 3)                            # Euclidean


def test_explicit_fuchsian_fiber_rep():
    """The fiber F_2 has a real SL(2,R) Fuchsian rep: det 1, |tr|>2, tr[X,Y] = -2 (parabolic boundary)."""
    import numpy as np
    X, Y, trc = B.fuchsian_fiber_rep()
    assert abs(np.linalg.det(X) - 1) < 1e-9 and abs(np.linalg.det(Y) - 1) < 1e-9
    assert abs(np.trace(X)) > 2 and abs(np.trace(Y)) > 2          # hyperbolic
    assert abs(trc - (-2)) < 1e-9                                 # boundary parabolic => Teichmuller point


def test_holonomy_preserves_minkowski():
    """Ad(holonomy) preserves the (2,1) form -> SO(2,1) local Lorentz invariance."""
    assert B.holonomy_preserves_minkowski() < 1e-9
