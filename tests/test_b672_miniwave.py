"""B672 locks — the RR recognition + the branch dichotomy."""
import os

_B = os.path.join(os.path.dirname(__file__), "..", "frontier",
                  "B672_grading_hunt")


def _text(cell):
    d = os.path.join(_B, cell)
    t = ""
    for f in os.listdir(d):
        if f.endswith((".md", ".txt")):
            t += open(os.path.join(d, f), errors="ignore").read()
    return t


def test_grading_hunt_rr_match():
    t = _text("cellG")
    assert "301" in t and ("Rogers" in t or "RR" in t)


def test_branch_lemma_dichotomy():
    t = _text("cellB")
    assert "A₄" in t or "A4" in t
    assert "√5" in t or "sqrt(5)" in t or "sqrt5" in t
