"""B1201 lock -- the Lee verification corrects B1198; the harvest closes."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1201_lee_verified_and_harvest"


def test_the_correction_is_explicit():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1201" and d["verdict"] == "PROVED"
    c = d["claim_one_line"]
    assert "WITHDRAWN AS STATED" in c and "ONE-ELEMENT SET" in c
    assert "NO USE OF CS = 0" in c
    assert "ABSENT FROM THE LITERATURE" in c
    assert "RE-RUNS CLEAN" in c        # the CITED debt paid


def test_b1198_carries_the_addendum():
    t = (ROOT / "frontier" / "B1198_lee_motives_retrieval" /
         "ADDENDUM_corrected_B1201.md").read_text(encoding="utf-8")
    assert "WITHDRAWN for our object" in t and "|a₁| = 1" in t
    assert "RELOCATED" in t


def test_results():
    d = json.loads((ARC / "b1201_results.json").read_text(encoding="utf-8"))
    assert d["lee"]["b_appendix_uses_CS0"] is False
    assert "UNIQUE" in d["lee"]["a_tangent_vectors"]
    assert d["cloud"]["quine_cert"].startswith("RE-RUNS CLEAN")
