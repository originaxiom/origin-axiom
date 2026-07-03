"""Locks for B372 — the level-45 sweep (banked sweep45.json)."""

import json
import os
from fractions import Fraction as Fr

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B372_level45_sweeper")
R = json.load(open(os.path.join(HERE, "sweep45.json")))
IMAG = (2, 3, 6, 7, 10, 11)


def test_no_identification_failures():
    assert R["failures"] == []


def test_singles_wall_exact():
    assert set(R["singles1"]) == {"1", "16", "31", "46"}
    for v in R["singles1"].values():
        assert Fr(v[0]) == Fr(1, 4) and all(Fr(x) == 0 for x in v[1:])
    for v in R["singles2"].values():
        assert all(Fr(v[i]) == 0 for i in IMAG)


def test_seam_persists_and_saturates():
    assert len(R["pair"]) == 144
    for v in R["pair"].values():
        assert any(Fr(v[i]) != 0 for i in IMAG)          # every cell imaginary
    s15 = sum(1 for v in R["pair"].values()
              if any(Fr(v[i]) != 0 for i in (3, 7, 11)))
    assert s15 == 144                                     # sqrt(-15)-type everywhere


def test_cubic_dependence_everywhere():
    for v in R["pair"].values():
        assert any(Fr(v[i]) != 0 for i in range(4, 12))   # genuine Q(zeta9)+ content


def test_full_rerun_matches_banked():
    if not os.environ.get("OA_SLOW"):
        import pytest
        pytest.skip("OA_SLOW not set")
    import sys
    sys.path.insert(0, HERE)
    from sweep45 import run_level
    from fp_engine import primes_1_mod
    fresh = run_level(45, primes_1_mod(720, 3))
    assert fresh["pair"] == R["pair"]
