"""B1167 lock -- two-seat harvest. (A) codex R017 pays the SEAM-Y up-Yukawa provenance debt
(character arithmetic own-verified, certs cited-from-branch, cohomology fenced). (B) cc3
B8138-extended's cusp-shape 2nd object-level separator is ORIENTATION-BLIND (mirror-fixed) -> B1163
strengthened not overturned. Asserts on COMMITTED files only. Gate 5 clean."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1167_seat_harvest"


def _d():
    return json.loads((ARC / "b1167_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_open():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1167" and d["verdict"] == "OPEN"
    assert d["instrument"] is False and d["creates_law"] is False


def test_A_codex_provenance_paid():
    a = _d()["A_codex_r017_provenance"]
    assert "PAID" in a["disposition"]
    # the character arithmetic is own-verified (C12-neutral => permits, not a texture zero)
    assert "C12-neutral" in a["character_arithmetic_own_verified"]
    assert "Sym^2(C^3)" in a["character_arithmetic_own_verified"]
    # the cohomological vanishing is fenced as codex's typed input
    assert "H^1(G_Y)=0" in a["fenced_codex_input"] and "NOT re-derived here" in a["fenced_codex_input"]
    assert "byte-identical" in a["certs_reproduced"]


def test_B_cusp_separator_orientation_blind():
    b = _d()["B_cc3_b8138_cusp_separator"]
    assert "2sqrt3 i" in b["finding"] and "unique" in b["finding"]
    # cc's answer to cc3's handed question: orientation-blind
    assert "NO" in b["cc_answer_ORIENTATION_BLIND"]
    assert "PURELY IMAGINARY" in b["cc_answer_ORIENTATION_BLIND"]
    assert "MIRROR-FIXED" in b["cc_answer_ORIENTATION_BLIND"] and "does NOT supply W0" in b["cc_answer_ORIENTATION_BLIND"]
    # B1163 strengthened, two separators both orientation-blind
    assert "STRENGTHENED not overturned" in b["effect_on_b1163"]
    assert "BOTH orientation-blind" in b["effect_on_b1163"]


def test_C5_seed_object_supplies_archimedean_modulus():
    d = _d()
    assert "object-canonical ARCHIMEDEAN datum" in d["C5_seed"]
    assert "withholds only the ORIENTATION" in d["C5_seed"]


def test_reproduce_runner_committed_and_reproduces():
    runners = list((ARC / "verification").glob("reproduce*.sh"))
    assert runners, "no committed reproduce runner"
    assert "REPRODUCES" in runners[0].read_text(encoding="utf-8")


def test_no_crossing_gate5_clean():
    d = _d()
    assert "No firewall crossing" in d["fences"] and "Gate 5 clean" in d["fences"]
