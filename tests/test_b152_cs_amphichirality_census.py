"""B152 — CS-as-parity-order-parameter census (V141).

Locks the banked census summary (committed census.json) and live-checks the
method on the three crux manifolds (m004, m003, m208). SnapPy-gated: skips
cleanly when SnapPy is absent (REPRODUCIBILITY convention).
"""
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
B152 = ROOT / "frontier" / "B152_cs_amphichirality_census"


def _load_census():
    p = B152 / "census.json"
    if not p.exists():
        pytest.skip("census.json not generated (run probe.py)")
    return json.loads(p.read_text())


def test_banked_summary():
    """The committed census reproduces the banked counts."""
    data = _load_census()
    s = data["result"]["summary"]
    assert s["n_scanned"] == 240
    assert s["n_amphichiral"] == 7
    assert s["amphichiral_names"] == [
        "m003", "m004", "m135", "m136", "m203", "m206", "m207"
    ]
    assert s["necessity_violations"] == []          # amphichiral => CS 2-torsion
    assert s["converse_cs0_chiral"] == ["m208"]      # unique converse failure
    assert s["n_indeterminate_symgroup"] == 0


def test_live_crux_manifolds():
    """Live-verify the method on the three corners (fast: 3 manifolds)."""
    snappy = pytest.importorskip("snappy")
    import importlib.util

    spec = importlib.util.spec_from_file_location("b152_probe", B152 / "probe.py")
    probe = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(probe)

    # m004 (figure-eight): amphichiral, CS = 0
    M = snappy.Manifold("m004")
    assert probe.amphichirality(M) is True
    assert probe.cs_two_torsion(float(M.chern_simons()))
    assert probe._near_mod_half(float(M.chern_simons()), 0.0)

    # m003 (sister): amphichiral, CS = 1/4
    M = snappy.Manifold("m003")
    assert probe.amphichirality(M) is True
    assert probe._near_mod_half(float(M.chern_simons()), 0.25)

    # m208: chiral but CS = 0 -- the necessary-not-sufficient witness
    M = snappy.Manifold("m208")
    assert probe.amphichirality(M) is False
    assert probe._near_mod_half(float(M.chern_simons()), 0.0)


def test_modulo_guard():
    """A tiny negative CS (genuinely 0) must register as 2-torsion, not wrap to 1/2."""
    import importlib.util

    spec = importlib.util.spec_from_file_location("b152_probe", B152 / "probe.py")
    probe = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(probe)
    assert probe._near_mod_half(-2.0e-16, 0.0)
    assert probe.cs_two_torsion(-2.0e-16)
