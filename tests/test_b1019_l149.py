"""B1019 — locks: the entry-map facts, recomputed exactly; the doors stay counted."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1019_l149_silver_cascade"
sys.path.insert(0, str(ARC))


def test_the_three_shadows_recompute_exactly():
    from b1019_cells import analyze
    g = analyze(1)
    assert (g["order"], g["involutions"], g["su2_embeddable"]) == (120, 1, True)
    s = analyze(2)
    assert (s["order"], s["involutions"], s["su2_embeddable"]) == (32, 7, False)
    assert s["contains_minus_I"] is False
    b = analyze(3)
    assert (b["order"], b["involutions"], b["su2_embeddable"]) == (2184, 1, False), (
        "bronze must stay non-embeddable BY ORDER (2184 > 120) despite its unique involution -- "
        "the necessary-vs-sufficient slip this arc caught must never regress")


def test_the_verdict_keeps_its_scope():
    v = json.loads((ARC / "arc_verdict.json").read_text())
    c = v["claim_one_line"]
    assert "DIVERGES" in c and "NOWHERE TO BEGIN" in c
    assert "not excluded" in c, "the non-McKay-entry door-back must stay stated"
    assert "m = 2, 3" in c or "m = 2,3" in c, "the family scope must stay bounded to the sealed controls"


def test_the_replacement_sentence_is_stated():
    f = (ARC / "FINDINGS.md").read_text()
    # full doc normalization: markdown emphasis AND blockquote markers both break naive
    # substring checks on wrapped lines -- the third such bug today; strip both.
    flat = " ".join(f.lower().replace("*", "").replace(">", " ").split())
    assert "insofar as the entry is the word's own" in flat
    assert "one grammar, one door, one cascade, one endpoint" in flat
