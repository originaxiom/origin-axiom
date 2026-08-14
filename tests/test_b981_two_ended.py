"""B981 locks — the object spans all three curvature signs; the sign-mismatch no-go is withdrawn."""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _prose import contains  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B981_two_ended_correction"


def test_verdict_is_PROVED_because_this_arc_is_an_auditor():
    """B818: an auditor establishing that ANOTHER claim fails is positive work, not a
    self-retraction. This arc's own headline -- the object spans all three curvature signs --
    stands; what it withdraws is a session claim that never entered a tracked file."""
    assert json.loads((CELL / "arc_verdict.json").read_text())["verdict"] == "PROVED"


def test_all_three_curvature_signs_are_recorded():
    assert contains(CELL / "FINDINGS.md", "hyperbolic", "euclidean", "spherical")


def test_it_depends_on_the_arc_that_refutes_it():
    """B250's own headline carries both ends -- that is the sharpest part of this correction."""
    dep = json.loads((CELL / "arc_verdict.json").read_text())["depends_on"]
    assert "B250" in dep and "B248" in dep


def test_the_cc_problem_is_still_NOT_solved():
    assert contains(CELL / "FINDINGS.md", "no solution to the cosmological-constant problem")


def test_the_near_zero_hook_is_firewalled_not_claimed():
    assert contains(CELL / "FINDINGS.md", "hook", "numerology risk")


def test_the_phrase_is_registered_for_the_sweep():
    assert contains(ROOT / "docs" / "RETRACTED_PHRASES.md", "the object is hyperbolic")
