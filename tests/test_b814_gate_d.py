"""B814 — locks Gate D: the GKY dim-1 hypothesis fails at E6 on 4_1."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _b575():
    return (ROOT / "frontier" / "B575_bridge_obstruction" / "FINDINGS.md").read_text()


def test_the_six_blocks_are_one_space_not_six_components():
    """The survival branch: six separate dim-1 components would SATISFY GKY. They are not separate."""
    t = _b575()
    assert "fifteen cross-pairings" in t, "the joint-deformation evidence must be present"
    assert "smooth 6-fold" in t, "B575's own conclusion carries the verdict"
    assert "H¹ = 6" in t, "the total tangent must be ONE 6-dimensional space"


def test_the_obstruction_vanishes_in_every_direction_and_pairing():
    t = _b575()
    assert "vanishes identically" in t
    assert "all six diagonal components" in t


def test_the_verdict_is_evidence_not_proof():
    """The prereg fixed this ceiling before the run; it must survive in the findings."""
    f = " ".join((ROOT / "frontier" / "B814_gate_d" / "FINDINGS.md").read_text().split())
    assert "STRONG EVIDENCE, not proof" in f
    assert "conditional by nature" in f   # whitespace-normalised: the phrase wraps in the source


def test_sl2_case_is_explicitly_untouched():
    """The failure is specific to E6 and is a failure of DIMENSION, not of the identity."""
    f = " ".join((ROOT / "frontier" / "B814_gate_d" / "FINDINGS.md").read_text().split())
    assert "SL(2) case is untouched" in f
