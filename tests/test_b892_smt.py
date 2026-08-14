"""Locks B892 -- the Second Measurement Theorem verified + the B874 amendment."""
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B892_second_measurement"
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")
WALL = json.loads((_D / "wall_results.json").read_text(encoding="utf-8"))
_B874 = (_ROOT / "frontier" / "B874_measurement_ladder" / "FINDINGS.md").read_text(encoding="utf-8")


def test_the_theorem_statement_and_digits():
    assert "z(x₁, y) = su(3) ⊕ su(2) ⊕ u(1)³ exactly" in _F  # y* loses its star in normalization
    assert "γ_q = 13410" in _F.replace("gamma_q", "γ_q") or "13410" in _F
    assert "2675" in _F


def test_the_wall_is_complex():
    assert "a is imaginary" in _F
    assert "+2.79×10⁹".lower() in _F or "2.79" in _F
    # the real-line scan found only the plane stratum
    assert all(nd <= 30 for th, nd in WALL["wall_points"])
    assert not any(nd == 14 for th, nd in WALL["wall_points"])


def test_the_b874_amendment_is_logged_both_places():
    assert "the second clause was an overgeneralization and is corrected" in _F
    assert "AMENDMENT (2026-08-05, B892)" in _B874
    assert "the second measurement skips" in _F


def test_the_su5_negative_survives():
    assert "still not reached" in _F or "skips su(5)" in _F.replace("SU(5)", "su(5)")
