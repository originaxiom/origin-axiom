"""B809 — locks the measured kappa against the masterplan's sealed gate."""
import json
from pathlib import Path

ARC = Path(__file__).resolve().parents[1] / "frontier" / "B809_kappa_gate"
GATE = 0.75          # the masterplan's sealed W1 gate


def _k():
    return json.loads((ARC / "kappa.json").read_text())


def test_kappa_meets_the_sealed_gate():
    k = _k()
    assert k["gate"] == GATE, "the gate moved -- kappa was re-scored against different goalposts"
    assert k["kappa"] >= GATE, f"kappa {k['kappa']:.3f} fell below the sealed gate {GATE}"
    assert k["n"] == 20


def test_kappa_is_computed_not_asserted():
    """p_o and p_e must reconstruct kappa exactly -- guards a hand-edited number."""
    k = _k()
    recomputed = (k["p_o"] - k["p_e"]) / (1 - k["p_e"])
    assert abs(recomputed - k["kappa"]) < 1e-9


def test_the_two_disagreements_are_the_known_vocabulary_boundaries():
    """If new disagreement kinds appear, the vocabulary has a third gap to close."""
    k = _k()
    assert set(k["disagreements"]) == {"B212", "B420"}, (
        "a disagreement outside the two diagnosed boundaries appeared -- diagnose it before "
        "fanning out")
