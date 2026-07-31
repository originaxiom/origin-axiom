"""B832 — locks wave 3's gate, the four-category fix, and the consistency finding."""
import glob
import importlib.util
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B832_verdict_wave3"
_SPEC = importlib.util.spec_from_file_location(
    "fleiss_kappa", ROOT / "scripts" / "checks" / "fleiss_kappa.py")
fk = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(fk)


def _ratings():
    return json.loads((ARC / "calibration_ratings.json").read_text(encoding="utf-8"))


def test_the_calibration_block_EXERCISED_all_four_categories():
    """The fix wave 3 exists for -- wave 2's block used two while licensing four."""
    used = {v for m in _ratings().values() for v in m.values()}
    assert used == {"PROVED", "NEGATIVE", "OPEN", "RETRACTED"}, f"only {used} exercised"


def test_kappa_clears_the_sealed_gate():
    table, _, _ = fk.table_from_ratings(_ratings())
    k, _, _, _, _ = fk.fleiss_kappa(table)
    assert k >= 0.75
    assert abs(k - 0.9305) < 0.002, f"recorded kappa is 0.9305; got {k}"


def test_the_block_is_complete_12x16():
    r = _ratings()
    assert len(r) == 16 and {len(v) for v in r.values()} == {12}


def test_the_three_corpus_disagreements_are_recorded():
    """A self-consistent panel uniformly drifted -- the thing kappa cannot see.

    B834 resolved the disagreement IN THE PANEL'S FAVOUR after replication, so comparing the panel
    to the corpus now agrees. The enduring fact is what the panel said, which is what this arc
    measured -- so assert that directly rather than a difference that has since been closed.
    """
    modes = {a: Counter(m.values()).most_common(1)[0][0] for a, m in _ratings().items()}
    for a in ("B61", "B556", "B746"):
        assert modes[a] == "PROVED", (
            f"{a}: wave 3's panel called it PROVED against a corpus label of OPEN/NEGATIVE; "
            f"B834 replicated that and corrected the corpus")


def test_all_three_disagreements_drift_toward_PROVED():
    for a in ("B61", "B556", "B746"):
        mode = Counter(_ratings()[a].values()).most_common(1)[0][0]
        assert mode == "PROVED", f"{a} panel mode was {mode}; B832's finding is a one-way drift"


def test_the_findings_reports_my_failed_prediction_and_the_execution_error():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "I was wrong" in f
    assert "hand-typed the reader work-lists" in f
    assert "126" in f, "the exact cost of the frame error must be stated"
