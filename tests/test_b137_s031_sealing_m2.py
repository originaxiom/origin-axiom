"""Locks for B137 -- S031 sealing extended to m=2 (SL(3), Q(i)); the reducible-filter (MB7)."""
import importlib.util
import pathlib

import pytest

_ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load():
    spec = importlib.util.spec_from_file_location(
        "b137_probe", _ROOT / "frontier/B137_s031_sealing_m2/probe.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


B137 = _load()


def test_m1_sealed_reproduce():
    pytest.importorskip("scipy")
    r = B137.sealing_search(1, "Q(sqrt-3)", starts=50)
    assert r is not None and r["irreducible"] >= 4 and r["irreducible_escapes"] == 0 and r["sealed"]


def test_m2_sealed_in_Qi():
    pytest.importorskip("scipy")
    r = B137.sealing_search(2, "Q(i)", starts=70)
    # silver SL(3) tower sealed in Q(i) among irreducible fixed points (the reducible 'escapes' are artifacts)
    assert r is not None and r["irreducible"] >= 4
    assert r["irreducible_escapes"] == 0 and r["sealed"]
    assert r["reducible_artifacts_ignored"] >= 1   # MB7: reducible degenerate points faked escapes, correctly filtered
