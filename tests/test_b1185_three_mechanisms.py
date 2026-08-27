"""B1185 lock -- L186 answered (three mechanisms, pairwise distinct) + the evaluator's benchable half."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1185_yukawa_three_mechanisms"


def test_arc_verdict():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1185" and d["verdict"] == "PROVED"
    c = d["claim_one_line"]
    assert "GENUINELY THREE" in c and "INV-3 INDEX SPACE" in c
    assert "SKEW ZERO" in c and "Q(zeta_12)" in c
    assert "single next artifact" in c          # the commissioned half stays typed, not claimed


def test_results():
    d = json.loads((ARC / "b1185_results.json").read_text(encoding="utf-8"))
    assert d["l186"].startswith("CLOSED: THREE")
    assert "810/810" in d["theorem"] and "generation-NULL" in d["theorem"]
    assert "C12 trivial on B_0" in d["dual_homed_this_arc"]
    assert "certify_yukawa_down_tail_cech_308.sage" in d["commissioned"]


def test_findings_fences():
    t = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "mechanism cannot both kill and allow the same coupling" in t
    assert "possibility-space fence" in t       # the E8 fence stays a fence
    assert "NOT committed" in t                 # the dual-homing debt recorded


def test_reproduce_exactness():
    r = (ARC / "verification" / "reproduce.sh").read_text(encoding="utf-8")
    assert "sum(raw) % 12 == 3" in r and '(8, 4, 0)' in r
    assert "combinations_with_replacement" in r and "(4, 4)" in r
    assert "x**2 - x + 1" in r                  # INV-3's degree-2 anchor computed, not quoted
