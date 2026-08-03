"""Locks B876 -- THE DESCENT."""
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B876_descent"
RES = json.loads((_D / "results_stage1.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")


def test_the_imposed_levi_tower_is_exact():
    assert RES["cent_y"] == 25
    assert RES["cent_y2"] == 13 and RES["cent_both"] == 13
    assert RES["so10_dim"] == 45 and RES["sector_dims"] == [16, 16, 16]


def test_the_grading_trilogy():
    assert RES["z1_clusters"] == [16, 16]
    assert RES["y_multiplicities"] == [10, 10, 5, 5, 1, 1]
    assert RES["joint_multiplicities"] == [6, 6, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1]


def test_transversality_blowup():
    """SM-graded states are near-cancelling combinations of large V2/V3 vectors:
    the maxima blow up together (>10) while every piece stays far from lying in
    a single sector."""
    t = RES["transversality"]
    assert len(t) == 6
    big = [p for p in t if p["dim"] > 1]
    assert all(p["v2_max"] > 10 and p["v3_max"] > 10 for p in big)


def test_the_verdict_both_halves():
    assert "exactly one sm generation's multiplet pattern" in _F
    assert "the triple's identity does not survive within a single breaking" in _F
    assert "across the three breakings" in _F
    assert "unweighted" in _F


def test_the_design_correction_is_recorded():
    assert RES["per_sector_grading_ill_posed"] is True
    assert "ill-posed" in _F and "refused to cluster" in _F
