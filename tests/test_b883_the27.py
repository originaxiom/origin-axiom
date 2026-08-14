"""Locks B883 -- the 27 on the B854 frame."""
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B883_the_27"
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
REP = json.loads((_D / "rep27.json").read_text(encoding="utf-8"))


def test_verification_ladder():
    assert RES["jacobi_triples"] == 1500
    assert RES["frame_pairs"] == 3000
    assert RES["hom_pairs"] == 6084
    assert RES["weights_distinct"] == 27


def test_minuscule_with_omega1_dominant():
    assert RES["dominant_weights"] == [[1, 0, 0, 0, 0, 0]]


def test_branching_validation():
    assert RES["s1_multiplicities"] == [1, 10, 16]
    assert RES["validated"] is True


def test_the_instrument_is_complete_and_integral():
    assert len(REP["rep"]) == 78
    assert len(REP["weights"]) == 27
    M = REP["rep"]["6"]
    assert len(M) == 27 and len(M[0]) == 27
    assert all(isinstance(x, int) for row in M for x in row)
    assert "B854" in REP["convention"]
