"""B1198 lock -- the Lee-motives retrieval (CITED-grade, fences enforced)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1198_lee_motives_retrieval"


def test_verdict_and_fences():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1198" and d["verdict"] == "OPEN"     # a retrieval, not a result
    c = d["claim_one_line"]
    assert "NOT CANONICAL" in c                              # the load-bearing retrieved fact
    assert "CITED/UNVERIFIED" in c or "CITED not" in c       # E37 fence present
    assert "HYPOTHESIS" in c                                 # the shape-match is not a theorem
    assert "does not supply W0" in c                         # no overclaim


def test_own_half_is_the_banked_number():
    d = json.loads((ARC / "b1198_results.json").read_text(encoding="utf-8"))
    assert d["own_computation"]["Vol"].startswith("2.02988321281930725")
    assert d["paper"]["grade"].startswith("CITED")
    assert "mathematics NOT read" in d["paper"]["read"]


def test_verification_step_named():
    d = json.loads((ARC / "b1198_results.json").read_text(encoding="utf-8"))
    assert "Appendix A" in d["verification_step"] and "torsor" in d["verification_step"]
