"""B109 -- locking tests for the trace-map dynamics at the void (D2 / Task 2).
The rigorous linearization (not the non-reproducing coordinate-axis facts): DT1^2 at (2,2,2) has eigenvalues
{1, phi^4, phi^-4} -- 1 center (the A<->B asymmetry), 1 unstable, 1 stable; the void is a (2,1) saddle of kappa;
and the SL(3) center manifold has dim 2 (= the tower's root-of-unity parity sector). NO physics; P1-P16 untouched."""
import importlib.util
import math
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b109", _ROOT / "frontier" / "B109_trace_map_dynamics" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_sl2_void_linearization_one_center_asymmetry():
    r = B.sl2_void_linearization()
    assert (r["n_center"], r["n_unstable"], r["n_stable"]) == (1, 1, 1)
    assert r["center_is_asymmetry"] is True              # center eigvec is (+-)(1,-1,-1)
    assert 0.0 in r["lyapunov"]                            # the center direction is marginal (Lyapunov 0)
    assert any(abs(l - r["four_log_phi"]) < 1e-3 for l in r["lyapunov"])   # unstable = +4 log phi


def test_sl2_center_orbit_locally_bounded():
    o = B.sl2_center_orbit()
    assert o[1e-3] < 5.0 and abs(o[1e-3] - 3.46) < 0.1    # bounded ~3.46 at small eps
    assert o[1e-2] == float("inf")                         # escapes for larger eps (local center manifold)


def test_kappa_void_is_2_1_saddle():
    k = B.kappa_void_critical_point()
    assert k["kappa_at_void"] == 2 and k["is_critical"] is True
    assert k["hessian_eigenvalues"] == {-2: 1, 4: 2}
    assert k["signature"] == (2, 1)                        # indefinite -> saddle


def test_sl3_center_manifold_is_tower_parity_sector():
    for word in (("U", "L"), ("U", "S")):
        r = B.sl3_void_center_count(word)
        assert r["n_center"] == 2                          # 2 of 8 are root-of-unity (the parity sector)
    s = B.center_manifold_summary()
    assert s["SL2"] == 1 and s["SL3_figure_eight"] == 2 and s["SL3_single_twist"] == 2
