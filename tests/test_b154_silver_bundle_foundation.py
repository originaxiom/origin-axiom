"""B154 -- silver bundle (m=2, R^2 L^2) foundation (V146).

Locks: the silver monodromy abelianization (M2^2), the geometric-component kappa formula
(1/2 z^2 + 8/z^2 - 2) vs the figure-eight control (x^2+z^2-x-z-2, B67), and the convention-free
monodromy solver (tA=phi(A)t at ~machine precision). The exact fixed-locus decomposition is the
Sage derivation (silver_tracemap.sage), not this fast test.
"""
import importlib.util
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
B154 = ROOT / "frontier" / "B154_silver_bundle_foundation"


def _probe():
    spec = importlib.util.spec_from_file_location("b154_probe", B154 / "probe.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_probe_passes():
    assert _probe().check()


def test_silver_kappa_and_figeight_control():
    m = _probe()
    # figure-eight control: y=z, x=z/(z-1) -> kappa = x^2+z^2-x-z-2 (B67)
    for z in [2.4 + 0.5j, 1.3 - 0.4j]:
        y = z; x = z / (z - 1); A, B = m.AB_from_traces(x, y, z)
        assert abs(m.kappa(A, B) - (x**2 + z**2 - x - z - 2)) < 1e-9
    # silver geometric: y=xz/2, x^2=2+8/z^2 -> kappa = 1/2 z^2 + 8/z^2 - 2
    for z in [2.4 + 0.5j, 1.3 - 0.4j, 3.0 + 0.7j]:
        x = np.sqrt(2 + 8 / z**2); y = x * z / 2; A, B = m.AB_from_traces(x, y, z)
        assert abs(m.kappa(A, B) - (0.5 * z**2 + 8 / z**2 - 2)) < 1e-9


def test_monodromy_solver_exact():
    m = _probe()
    # silver geometric point: t must conjugate (A,B) to (phi(A),phi(B)) at machine precision
    z = 2.4 + 0.5j
    x = np.sqrt(2 + 8 / z**2); y = x * z / 2; A, B = m.AB_from_traces(x, y, z)
    t = m.solve_monodromy(A, B, m.phi_silver)
    assert t is not None
    Ap, Bp = m.phi_silver(A, B)
    assert np.max(np.abs(t @ A - Ap @ t)) < 1e-8
    assert np.max(np.abs(t @ B - Bp @ t)) < 1e-8
    assert abs(np.linalg.det(t) - 1) < 1e-8
