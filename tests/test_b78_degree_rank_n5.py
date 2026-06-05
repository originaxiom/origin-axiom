"""B78 (Phase 1b, V61) -- locking test: the finder reproduces n=3, and n=5 yields only reducible reps.

Locks (1) the n-generic figure-eight finder reproduces the known n=3 sign law (M^3=L, c=+1) -- so the
finder is trustworthy; (2) at n=5 the bundle condition yields only REDUCIBLE reps (the honest
method-limit: the irreducible principal Dehn-filling rep is not numerically locatable). Kept fast."""
import importlib.util
import pathlib

import numpy as np

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b78_n5", _ROOT / "frontier" / "B78_degree_rank_n5" / "probe.py")
B78 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B78)


def test_finder_reproduces_n3_sign_law():
    """n=3 {1,i,-i}: the finder gives M^3=L with c=+1 (validates the n-generic figure-eight finder)."""
    found, med, bestk, cbest = B78.reproduce([1, 1j, -1j], 3, (2, 3, 4), n_reps=2, budget=120)
    assert found >= 1, "finder must produce an SL(3) Dehn-filling rep"
    assert bestk == 3 and med[3] < 1e-7, (bestk, med)
    assert abs(cbest - 1.0) < 1e-5, cbest


def test_n5_bundle_reps_are_reducible():
    """n=5 {1,1,1,w,w2}: converged bundle reps are REDUCIBLE (the honest method-limit)."""
    W = np.exp(2j * np.pi / 3)
    conv, irr = B78.irreducible_fraction([1, 1, 1, W, W ** 2], starts=20)
    assert conv >= 3, ("the bundle condition should be solvable", conv)
    assert irr == 0, ("n=5 yields only reducible reps in this search (method-limit)", conv, irr)
