"""B77 (Phase 1a, V60) -- locking test: the degree=rank sign refinement + unification refuted.

Locks: (1) [A,B]=c*mu^n with c=(-1)^(n-1) (c=+1 at n=3, c=-1 at n=4); (2) eig(mu) varies across reps
(generic -> NOT the fixed Dickson char(M^n) roots; the unification is refuted, not asserted)."""
import importlib.util
import pathlib

import numpy as np

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b77_drm", _ROOT / "frontier" / "B77_degree_rank_mechanism" / "probe.py")
drm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(drm)


def test_sl3_scalar_c_is_plus_one():
    """SL(3) W1, n=3: [A,B]=c*mu^3 with c=+1=(-1)^2, and eig(mu) varies across reps."""
    cs, devs, spread = drm.c_over_reps(drm.sl3_reps(n_reps=4), 3)
    assert len(cs) >= 3, "need reps"
    assert max(devs) < 1e-6
    assert abs(np.mean(cs) - 1.0) < 1e-5, np.mean(cs)
    assert np.max(spread) > 0.05, ("eig(mu) must vary (generic, not fixed Dickson roots)", spread)


def test_sl4_scalar_c_is_minus_one():
    """SL(4) {1,1,w,w^2}, n=4: [A,B]=c*mu^4 with c=-1=(-1)^3, and eig(mu) varies across reps."""
    cs, devs, spread = drm.c_over_reps(drm.sl4_reps(n_reps=4), 4)
    assert len(cs) >= 3, "need reps"
    assert max(devs) < 1e-6
    assert abs(np.mean(cs) - (-1.0)) < 1e-5, np.mean(cs)
    assert np.max(spread) > 0.05, ("eig(mu) must vary (generic, not fixed Dickson roots)", spread)
