"""B808 — locks the VACUOUS verdict and the multiple-comparisons reading."""
import json
from pathlib import Path

ARC = Path(__file__).resolve().parents[1] / "frontier" / "B808_empty_cells"


def _r():
    return json.loads((ARC / "null_test.json").read_text())


def test_the_verdict_is_vacuous_against_sealed_thresholds():
    r = _r()
    assert r["verdict"] == "VACUOUS"
    assert r["artifact"] >= 30, "sealed: VACUOUS requires >= 30 of 35 artifact"
    assert r["artifact"] + r["real"] == 35


def test_the_single_real_gap_is_below_chance_expectation():
    """35 cells at p<0.10 => ~3.5 expected by chance. Observing 1 is FEWER than chance."""
    r = _r()
    expected_by_chance = 35 * 0.10
    assert r["real"] < expected_by_chance, (
        "if real gaps ever exceed 3.5, the multiple-comparisons reading changes and B808's "
        "stronger conclusion ('no real gaps at all') must be re-derived")


def test_large_face_completeness_is_not_surprising():
    """The prereg's second measurement, which also came back negative."""
    p = _r()["p_full"]
    assert p["being"] > 0.5, "being's motif-completeness must be common under the null"
    assert p["hearing"] > 0.3
